# 9. Implemente um método recursivo para determinar se um string ocorre dentro de outro.
# 	  ``` 
#          boolean findSubStr(String str, String match)
# 	  ``` 

def findSubStr(str1, str2):
    if len(str1) > len(str2):
        return False
    test = True
    for i in range(0, len(str1) - 1):
        if str1[i] != str2[i]:
            test = False
            break
    if test == True:
        return True
    return findSubStr(str1, str2[1:])

print(findSubStr("asa", "casa"))
print(findSubStr("asa", "cabelo"))
