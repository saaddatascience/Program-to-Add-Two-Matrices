def matrix(m,n): # m is number of rows n is number of columns 
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inpot = int(input(f"enter number[{i}][{j}]"))
            row.append(inpot)
        o.append(row)
    return o 

def sum(A,B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output     





m = int(input("Enter the number of rows\n"))
n = int(input("Enter the number of columns\n")) 

print('Enter Matrix A')
A = matrix(m,n)
print(A)

print("Enter Matrix B")  
B = matrix(m,n)
print(B)

s = sum(A,B)
print(s)       
        
    