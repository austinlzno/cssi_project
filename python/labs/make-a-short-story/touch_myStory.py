"""

This is my super duper funny mad libs Story

"""


"""

The (noun1) jumped over a (adjective1) (noun2).
Then the (noun2) decided to stop being so (adjective1) and take up a hobby:
(verb1-ing)

"""


def mad_lib():
    noun1 = input('Type a singular noun and press ENTER: ')
    adjective1 = input('Type an adjective and press ENTER: ')
    noun2 = input('Type a plural noun and press ENTER: ')
    verb1ing = input('Type a verb ending in "ing" and press ENTER: ')
    print 'The  + {noun1}' 
    print 'jumped over a ' + adjective1 + {noun2}. Then the {noun2} decided to stop being so {adjective1} and take up a hobby: {verb1ing}

mad_lib()
