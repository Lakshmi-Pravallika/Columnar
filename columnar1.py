while True:
 print("Enter 1 for encryption")
 print("Enter 2 for decryption")
 n=int(input("Enter your choice:"))
 if(n==1):
  key=input("Enter key:");
  keySorted=''.join(sorted(key))
  keySorted=list(keySorted);
  #print(keySorted)
  key=list(key);
  #print key
  pt=input("Enter plain text:");
  pt=list(pt);
  while(len(pt)%len(key)!=0):
   pt.append('x');
  #print pt
  l=int(len(pt)/len(key))
  l=l+1
  #print l
  k=0
  Matrix = [[0 for x in range(len(key))] for y in range(l)] 
  lst=[]
  for i in range(0,len(key)):
   Matrix[0][k]=key[i]
   k=k+1
  #print Matrix
  k=0
  for i in range(1,l):
   for j in range(0,len(key)):
    Matrix[i][j]=pt[k]
    k=k+1
  #print Matrix
  for i in range(0,len(keySorted)):
   for j in range(0,len(key)):
    if(keySorted[i]==key[j]):
     for k in range(1,l):
      lst.append(Matrix[k][j])
  cipherText = ''.join(lst)
  print(cipherText)
 elif(n==2):
  #key=input("Enter key:")
  #keySorted=''.join(sorted(key))
  #keySorted=list(keySorted);
  pt=cipherText
  pt=list(pt);
  l=int(len(pt)/len(key))
  #print l
  Matrix = [[0 for x in range(len(key))] for y in range(l+1)] 
  #print Matrix
  k=0
  for i in range(0,len(key)):
   Matrix[0][k]=key[i]
   k=k+1
  k=0
  #print Matrix
  for i in range(0,len(keySorted)):
   for j in range(0,len(key)):
    if(keySorted[i]==key[j]):
     for z in range(1,l+1):
      Matrix[z][j]=pt[k]
      k=k+1
  #print Matrix
  for row in Matrix:
   print(' '.join([str(elem) for elem in row]))
 else:
  print("Wrong input")
  quit();

 
 
 
 
