def str_reverse(ch):
    return ch[::-1]

def vowels(str):
    vow = "aeiouAEIOU"
    count = 0
    for i in str:
        if i in vow :
            count = count + 1
    return count