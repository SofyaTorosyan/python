# Homework_2 

# Eratosthenes algorithm 
# Following is the algorithm to find all the prime numbers less than or equal to a given integer n by Eratosthenes’ method:
# 1. Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
# 2. Initially, let p equal 2, the first prime number.
# 3. Starting from p2, count up in increments of p and mark each of these numbers greater than or equal to p2 itself in the list. 
#    These numbers will be p(p+1), p(p+2), p(p+3), etc..
# 4. Find the first number greater than p in the list that is not marked. 
#    If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), 
#    and repeat from step 3. 
   
print("Eratosthenes algorithm started. ") 
print("Enter N: ")
N = int(input())
if N < 2:
    print( " Wrong input: Algorithm starts from 2 " )
else:
    list = []
    N += 1  # N + 1 for including N    range [2 : N]
    list.extend(range(2, N ))   
    p = 2
    while p * p < N:
        temp = p * p
        while temp < N:
            for l  in  list:
                if l == temp:
                    list.remove(temp)
            temp += p        
        # go through list, find first number > p
        search = 0
        index  = 0
        while search < p:
            if list[index] > p:
                search = list[index]
                break
            else:
                index += 1;
        p = search
print("Prime numbers in [ ", 2 , " : ",  N - 1, " ]  range are: ")
for l in list:
    print(l)
              
            
            
        
        
    
    
    
    
    
    
    
    
    
    