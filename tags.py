#!/usr/bin/env python
# encoding: utf-8

import sys
import functools

TAB = ' ' * 4

def any(name, *args, **kwargs):
    words = ['%s=%s' % (k, v) for k, v in kwargs.items()]
    words.insert(0, name)
    children = []
    for arg in args:
        if isinstance(arg, basestring):
            children.append(arg)
        elif isinstance(arg, list):
            children.extend(arg)
    tag_begin = '<' + ' '.join(words) + '>'
    tag_end = '</' + name + '>'
    lines = []
    if len(children) == 0:
        lines.append(tag_begin + tag_end)
    elif len(children) == 1 and len(children[0]) <= 50 and not children[0].startswith('<'):
        lines.append(tag_begin + children[0] + tag_end)
    else:
        lines.append('<' + ' '.join(words) + '>')
        lines.extend(map(lambda x: TAB + x, children))
        lines.append('</' + name + '>')
    return lines

def getp(name):
    return functools.partial(any, name)

class ModuleWrapper(type(sys)):
    def __init__(self, module, getp=None):
        for attr_name in ['__builtins__', '__doc__', '__name__', '__package__', '__file__']:
            setattr(self, attr_name, getattr(module, attr_name, None))

        self._env = {}
        self._module = module
        self._getp = getp

    def __setattr__(self, name, value):
        if hasattr(self, '_env'):
            self._env[name] = value
        else:
            super(ModuleWrapper, self).__setattr__(name, value)

    def __getattr__(self, name):
        if name == '_env':
            raise AttributeError
        value = self._env.get(name)
        if value: return value
        elif self._getp: return self._getp(name)
        else: raise AttributeError

if __name__ == '__main__':
    raise SystemError
else:
    m = sys.modules[__name__]
    sys.modules[__name__] = ModuleWrapper(m, getp=getp)


