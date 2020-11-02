def enhanced_searchterm(searchterm):
    enhanced_term = ''
    for letter in searchterm:
        enhanced_term += '[' + letter + letter.upper() + ']'
    return enhanced_term
