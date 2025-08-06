# Modele e implemente um método recursivo que recebe um String em retorna true se este String for um palíndrome, false caso contrário.

#      boolean isPal(String s) 

from pickle import FALSE


def isPal(str): 
    print("\n" + str)
    if str == "":
        return True
    if str[0] != str[len(str) - 1]:
        return False
    return isPal(str[1: len(str) -1])

print("teste ispal ana")
print(isPal("ana"))

print("teste ispal omissíssimo")
print(isPal("omissíssimo"))