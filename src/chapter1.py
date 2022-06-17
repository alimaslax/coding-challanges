'''
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''


# Solution using dictionaries
def is_unique(x):
    dict = {}
    for char in x:
        if char in dict:
            return False
        dict[char] = 0
    return True


# print(is_unique('welcom'))

# Book Solution


'''
Given two strings,write a method to decide if one is a permutation of the other

#WhiteBoard
give string 1, string 2
permutation means same chars && same char length, order does not matter
'''


def is_permutation(stringA, stringB):
    if len(stringA) != len(stringB):
        return False
    dict = {}
    for char in stringA:
        dict[char] = char
    for char in stringB:
        if char not in dict:
            return False;
    return True


# print(is_permutation('welcome', 'weleomc'))

'''
Write a method to replace all spaces in a string with '%20'. You may assume that
the string has sufficient space at the end to hold the additional characters,and 
that you are given the "true" length of the string. (Note: If implementing in Java,
please use a character array so that you can perform this operation in place.)

#Whiteboard
simple replace string manipulation
'''


def replace_space_url(unformatedUrl):
    return unformatedUrl.replace(' ', '%20')


# print(replace_space_url("Hello world"))

'''
Palindrome Permutation: Given a string, write a function to check if it is a 
permutation of a palindrome. A palindrome is a word or phrase that is the 
same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.

Case and space insensative
For Phrases this method removes all spacing and then compares

#Whiteboard
MOM
check if index & index[count] are the same
    increment index by 1 and decrease index[count-1]
    check if they are the same
        if they are not the same
            return false
return true
'''


def is_palindrome(stringA):
    count = len(stringA)
    spaceRemoved = reversed = tempA = tempB = ''
    for x in range(count):
        if stringA[x] != ' ':
            tempA = stringA[x].lower()
            spaceRemoved += tempA
        if stringA[-(x + 1)] != ' ':
            tempB = stringA[-(x + 1)].lower()
            reversed += tempB
    return spaceRemoved == reversed


# print (is_palindrome('A dog! A panic in a pagoda'))

'''
here are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings,
write a function to check if they are one edit (or zero edits) away.

pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bake -> false

dict = { key : value}

'p':"count"...,'e': "count"

3 logic conditions where if any are true -> true
====
insert
 a & b have to be exactly 1 char in size diff
 chars must be in exact same order - 1 char out of position.
 
remove -> negate insert logic

replace
 a & b have to be exactly the same size
 all same char in same order except 1 char out of place
 
abcd
acd

'''


def is_one_move_away(stringA, stringB):
    is_insert_away = False
    is_remove_away = False
    is_replace_away = False
    length_a = len(stringA)
    length_b = len(stringB)
    max_length = 0
    if (length_a > length_b):
        max_length = length_a;
    else:
        max_length = length_b;
    # must be exact same length or 1 char short
    if length_a != length_b and abs(length_a - length_b) > 1:
        return False

    # insert or remove or replace check
    # 1 char out of place
    out_of_position_counter = 0

    x = 0
    y = 0
    while x < max_length - 1:
        if (length_a < x or length_b < x):
            break
        if stringA[x] != stringB[x]:
            out_of_position_counter += 1
            x += 1
        if out_of_position_counter > 1:
            return False
        x += 1

    if (length_a == length_b):
        is_replace_away = True;
    if abs(length_a - length_b) > 1:
        is_insert_away = True
        is_remove_away = True

    return is_insert_away or is_remove_away or is_replace_away


# print(is_one_move_away("pale", "ple"))


# print("wel"[2])