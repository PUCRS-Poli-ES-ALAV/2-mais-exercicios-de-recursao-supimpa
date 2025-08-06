#  10. Faça um método recursivo que determina o número de dígitos de um inteiro.
	  
#          int nroDigit(int n)
	  

def nroDigit(n):
    if n == 0:
        return 0
    return nroDigit(n//10)+1

print(nroDigit(123))