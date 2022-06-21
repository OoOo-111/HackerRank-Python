if __name__ == '__main__':
    N = int(input())
    
    lis=[]
    
    for inputs in range(0,N):
      s1=input().split()   
      if s1[0] == "append":
          
          lis.append(int(s1[1]))
         
      elif s1[0]  == "insert":
         
          lis.insert(int(s1[1]),int(s1[2]))
      
      elif s1[0]  == "remove":
 
          lis.remove(int(s1[1]))
          
      elif s1[0]  == "sort":
          lis.sort()
          
      elif s1[0]  == "reverse":
          lis.reverse()   
          
      elif s1[0]  == "pop":
          lis.pop()           
          
      elif s1[0]  == "print":
        print(lis)
                 
