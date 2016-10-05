#! /usr/bin/env python

from __future__ import print_function

from os.path import join, dirname
from json import load, dumps
from io import open

authors_json = join(dirname(__file__), "authors.json")
author_list = load(open(authors_json))
for author in author_list:
    if "author_order" not in author:
        author["author_order"] = author["sympy_commits"]
author_list.sort(key=lambda x: x["author_order"], reverse=True)
for author in author_list:
    if author["author_order"] == author["sympy_commits"]:
        del author["author_order"]

with open(authors_json, "w", encoding='utf-8') as f:
    data = dumps(author_list, ensure_ascii=False, sort_keys=True, indent=4,
            separators=(',', ': '))
    f.write(data + "\n")
