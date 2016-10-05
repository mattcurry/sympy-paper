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
    all_addresses = []
    for author in author_list:
        addresses = author["institution_address_peerj"]
        for address in addresses:
            if address not in all_addresses:
                all_addresses.append(address)

    for author in author_list:
        addresses = author["institution_address_peerj"]
        address_n = ["%d" % (all_addresses.index(address) + 1) for address in addresses]
        f.write((u"\\author[%s]{%s}%%\n" % (', '.join(address_n), author["name"])))

    for n, address in enumerate(all_addresses):
        f.write(u"\\affil[%d]{%s}%%\n" % (n+1, address))
