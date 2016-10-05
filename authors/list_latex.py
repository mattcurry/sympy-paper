#! /usr/bin/env python

from __future__ import print_function


from os.path import join, dirname, pardir
from json import load
from io import open

authors_json = join(dirname(__file__), "authors.json")
authors_tex = join(dirname(__file__), pardir, "authors.tex")
author_list = load(open(authors_json))
author_list = list(filter(lambda x: x["sympy_commits"] > 0, author_list))

with open(authors_tex, "w", encoding='utf-8') as f:
    for n, author in enumerate(author_list):
        f.write((u"\\author[%d]{%s}%%\n" % (n+1, author["name"])))
    for n, author in enumerate(author_list):
        if "institution_explanation" in author:
            institution_explanation = u" %s" % author["institution_explanation"]
        else:
            institution_explanation = u""
        f.write(u"\\affil[%d]{%s, %s (\\email{%s}).%s}%%\n" \
                % (n+1, author["institution"],
                    author["institution_address_siam"],
                    author["email"],
                    institution_explanation))
