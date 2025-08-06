# 7. Modele e implemente um método recursivo que calcule o somatório dos números contidos em um ArrayList de inteiros, passado como parâmetro.

def arraySum(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    return a[0] + arraySum(a[1:])

print(arraySum([2,4,5,6]))