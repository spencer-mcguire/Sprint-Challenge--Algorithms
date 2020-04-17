'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # return how many times 'th' exists in a given word
    # search through the word, if it has no 'th' return 0
    # if it exists, set the index of the first found th and remove it from the word while + 1
    # loop until the word is exhausted
    # th is case sensitive, disreguard capital

    # write conditional to see if the th exists, else return 0
    if word.find('th') == -1:
        return 0
    # else create a new word while leaving out everthing up to and including the first th
    # add 2 to the found index and only display the rest of the string from there
    exists = word.find('th')
    #print(f"exists index:{exists}")
    new = word[exists + 2:]
    #print(f"new word:{new}")
    # call count_th to recursively continue through the given word
    # increment by 1 every time the function runs
    return count_th(new) + 1
