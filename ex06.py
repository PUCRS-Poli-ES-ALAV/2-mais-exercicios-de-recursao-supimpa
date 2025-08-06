# 6. Modele e implemente um método recursivo que recebe um inteiro zero ou positivo e retorna um String com o número em binário.
    
#          String convBase2(int n) 
    

def convBase2(n):
    if n < 0:
        return "deu um erro!"
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    return f"{convBase2(n//2)}{n%2}"

print(convBase2(4))