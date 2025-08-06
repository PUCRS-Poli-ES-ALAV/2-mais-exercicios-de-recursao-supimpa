#  8. Modele e implemente um método recursivo para encontrar o maior elemento de um ArrayList.
     
#          int findBiggest(ArrayList<Integer> ar) 
    

def findBiggest(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    if a[0] > a[1]:
        a[1] = a[0]
    return findBiggest(a[1:])

print(findBiggest([2,9,1,2,5]))