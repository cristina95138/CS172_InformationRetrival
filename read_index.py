# This file should contain code to receive either a document-id or word or both and output the required metrics. See the assignment description for more detail.

import parsing
import sys

if (len(sys.argv) == 3):
    inputType1 = sys.argv[1]
    input1 = sys.argv[2]

    if (inputType1 == '--term'):
        print('Listing for term: ', input1)
        info = parsing.termIndex[input1]
        print('TERMID: ', info.values())

    if (inputType1 == '--doc'):
        print('Listing for document: ', input1)
        info = parsing.docIndex[input1]
        print('DOCID: ', info.values())

if (len(sys.argv) == 5):
    inputType1 = sys.argv[1]
    input1 = sys.argv[2]
    inputType2 = sys.argv[3]
    input[2] = sys.argv[4]

    if (inputType1 == '--term'):
        print('Listing for term: ', input1)
        info = parsing.termIndex[input1]
        print('TERMID: ', info.values())

    if (inputType1 == '--doc'):
        print('Listing for document: ', input1)
        info = parsing.docIndex[input1]
        print('DOCID: ', info.values())

    if (inputType2 == '--term'):
        print('Listing for term: ', input1)
        info = parsing.termIndex[input1]
        print('TERMID: ', info.values())

    if (inputType2 == '--doc'):
        print('Listing for document: ', input1)
        info = parsing.docIndex[input1]
        print('DOCID: ', info.values())

