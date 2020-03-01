#!/usr/bin/env python
# encoding: utf-8

from tags import html, head, title, meta, a, div, body

lines = html(
    head(
        title('hello'),
        meta(a=1, b=2),
    ),
    body(
        a('baidu', href='http://www.baidu.com'),
        div('hahaha', div('hehehe')),
    ),
)

print '\n'.join(lines)
