def anagram(str1,str2):
    list1=list(str1)
    list1.sort()
    list2=list(str2)
    list2.sort()
    return(list1==list2)
print(anagram("anagram","margana"))
print(anagram("cat","rat"))

