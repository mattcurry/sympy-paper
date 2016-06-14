#! /usr/bin/env python

from __future__ import print_function

from json import load
from io import open

author_list = load(open("authors.json"))
author_list = list(filter(lambda x: x["sympy_commits"] > 0, author_list))

with open("../authors.tex", "w", encoding='utf-8') as f:
    for n, author in enumerate(author_list):
        f.write((u"\\author[%d]{%s}%%\n" % (n+1, author["name"])))
    for n, author in enumerate(author_list):
        f.write(u"\\affil[%d]{%s, %s (\\email{%s}).}%%\n" \
                % (n+1, author["institution"], author["institution_address_siam"],
                    author["email"]))
