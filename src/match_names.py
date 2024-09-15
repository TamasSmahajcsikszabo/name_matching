import os
import pathlib
import pandas as pd
from build_library import (load_library,
                           lookupLibrarySection,
                           lookupTermInSection)
import argparse


def find_best_match(results):
    '''
        Finds the best matches from name matches by computing the max of confidence
        scores and index results by that score

        Parameters:
            results: list of tuples of (finding[str], confidence score [float])
    '''
    confidence_scores = [result[1] for result in results]
    max_confidence_score = max(confidence_scores)
    best_match = [result for result in results
                  if result[1] == max_confidence_score]
    return best_match


def lookup(entry, term, result):
    '''
        Helper function to look up best matches
        If multiple findings with the highest best condifence are found,
        the function returns them all

        Parameters:
            entry: a stored array of strings and additional data
            term: a string to match against 'entry'
            result: container dictionary
    '''
    section = lookupLibrarySection(entry, term)
    found = lookupTermInSection(section, term)
    best_match = find_best_match(found)
    if len(best_match) == 1:
        found_term, confidence = best_match[0]
        result.append((term, found_term, confidence))
    elif len(best_match) > 1:
        best_match = set(best_match)
        for matching in best_match:
            found_term, confidence = matching
            result.append((term, found_term, confidence))


def match_names(entry, term):
    '''
        Main function, matches term against records in 'entry'.

        Parameters:
            entry: a stored array of strings and additional data
            term: a string to match against 'entry'
    '''

    result = []
    if isinstance(term, list):
        for i in range(len(term)):
            lookup(entry, term[i], result)
    if isinstance(term, str):
        lookup(entry, term, result)
    return result


def list_of_string(arg):
    return arg.split(',')


if __name__ == '__main__':
    '''
        Looking up local resources, entry data
    '''
    parent = pathlib.Path(__file__).parent.absolute()
    entry = load_library(os.path.join(parent, '..', 'data', 'libary.pickle'))

    '''
        Argument parser for match_names function

        Arguments:
            --test optional, stores True. If provided, a test is let run.
            --terms expects comma separated terms to look up
            e.g. --terms "Mr. Bean,Tesla,TopGun,Jane Doe"
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--terms',
        required=False,
        type=list_of_string,
        help="Search terms",
        nargs="+")
    parser.add_argument(
        '--test',
        help="Runs a built in quick run in test terms",
        action="store_true")
    args = parser.parse_args()

    if args.terms is not None and len(args.terms) > 0:
        print(match_names(entry, args.terms[0]))

    if args.test:
        print('Running test...')
        # test case
        terms = ['Jon Doe', 'Jane Smith', 'Emily Borwn', 'Mr. Johnson']
        print(match_names(entry, terms))
