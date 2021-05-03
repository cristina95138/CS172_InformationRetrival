# This file should contain code to receive either a document-id or word or both and output the required metrics. See the assignment description for more detail.

import parsing
import sys

termIndex, termInfo, docIndex = parsing.Tokens()

if (len(sys.argv) == 3):
    inputType1 = sys.argv[1]
    input1 = sys.argv[2]

    if (inputType1 == '--term'):
        print('Listing for term: ', input1)
        print('TERMID: ', termIndex.get(input1))
        print('Number of documents containing term: ', termInfo.get(input1).get('numDocs'))
        print('Term frequency in corpus: ', termInfo.get(input1).get('numOccur'))

    if (inputType1 == '--doc'):
        print('Listing for document: ', input1)
        info = docIndex.get(input1)
        print('DOCID: ', info)
        print('Distinct terms: ')
        print('Total terms: ')

if (len(sys.argv) == 5):
    inputType1 = sys.argv[1]
    input1 = sys.argv[2]
    inputType2 = sys.argv[3]
    input2 = sys.argv[4]

    if (inputType1 == '--term'):
        print('Inverted term for term: ', input1)
        info = termIndex.get(input1)
        print('TERMID: ', info)

    if (inputType1 == '--doc'):
        print('In document: ', input1)
        info = docIndex.get(input1)
        print('DOCID: ', info)

    if (inputType2 == '--term'):
        print('Inverted term for term:: ', input2)
        info = termIndex.get(input2)
        print('TERMID: ', info)

    if (inputType2 == '--doc'):
        print('In document: ', input2)
        info = docIndex.get(input2)
        print('DOCID: ', info)

    print('Term frequency in document: ')
    print('Positions: ')

