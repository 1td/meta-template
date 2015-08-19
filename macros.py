#!/usr/bin/env python
# encoding: utf-8

from tags import html, head, title

def c_title(s):
    return html(
        head(
            title(s),
        ),
    )

