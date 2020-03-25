n=int(input("enter the no. of elements in the list ").strip())
A=list(int(num) for num in input("Enter elments in comma separated ").split(","))[:n]
print(A[0],end=" ")
print(A[1:3],end=" ")
nn=int(input("enter another list size").strip())
AA=list(map(int,input("Enter the list in space separated form this time").strip().split()))[:nn]
print(AA)

