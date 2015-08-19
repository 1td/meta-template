#!/usr/bin/env python
# encoding: utf-8

import tags

lines = tags.html(
    tags.head(
        tags.title('hello'),
        tags.meta(a=1, b=2),
    ),
    tags.body(
        tags.a('baidu', href='http://www.baidu.com'),
        tags.div('hahaha', tags.div('hehehe')),
    ),
)

print '\n'.join(lines)
