def anagram(s1,s2):
    la=list(s1);lb=list(s2)
    la.sort();lb.sort()
    if(len(A)==len(B)):
        if(la==lb):
            print('The 2 strings are Anagram')
        else:
            print('The 2 strings are Not Anagram')
    else:
        print('The 2 strings are Not Anagram')
A=input('Enter a String:')
B=input('Enter another string:')
anagram(A,B)
