import re


def enhanced_searchterm(searchterm):
    enhanced_term = ''
    for letter in searchterm:
        enhanced_term += '[' + letter + letter.upper() + ']'
    return enhanced_term

def search_results(searchterm,companies):
    results = []
    number = 1
    for name in companies:
        if re.search(searchterm, name):
            results.append((number, name))
            number += 1
    return results

