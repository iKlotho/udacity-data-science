#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Parses CSV file from [http://mydatamaster.com/wp-content/files/streetsuffix.zip]
Provides a `SuffixTable` class to convert suffix strings, lower-cased, into the
full suffix.
"""
import csv
from collections import defaultdict
from pprint import pprint

CSVFILE = 'data/suffixes.csv'
ADDONS = {
    'rt': 'route',
    'blv': 'boulevard',
    'avene': 'avenue',
    'steet': 'street',
    'nwe': 'new'
}

def parse_suffixes_csv(filename):
    """ parses the CSV file and returns a one-to-many dictionary """
    suffixes = defaultdict(set)
    with open(filename, 'rb') as csvfile:
        csvfile.next()
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            suffix = row[0].lower().strip()
            aliases = [alias.lower() for alias in row[1:]]
            suffixes[suffix].update(aliases)
    for key in suffixes:
        suffixes[key] = list(suffixes[key])
    return dict(suffixes)

class SuffixTable(object):
    """ main class module, provides `has_suffix` and `convert` methods """
    def __init__(self):
        suffixes_dict = dict(parse_suffixes_csv(CSVFILE).items() + ADDONS.items())
        self.suffixes = suffixes_dict.keys()
        self.suffix_table = {}
        for key in suffixes_dict:
            for abbreviation in suffixes_dict[key]:
                self.suffix_table[abbreviation] = key

    def has_suffix(self, suffix):
        """ returns if the suffix is present in the table """
        return suffix.lower() in self.suffix_table

    def convert(self, suffix):
        """ converts a suffix string into the full suffix """
        return self.suffix_table[suffix]

    def __str__(self):
        return pprint(self.suffix_table)

if __name__ == '__main__':
    st = SuffixTable()
    pprint(st.suffix_table)
