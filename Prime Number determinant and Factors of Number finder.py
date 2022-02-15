######################################################################################################################
# Python program to check if a given number is prime or not; hence compute and print the factors of the number  
######################################################################################################################


import time


def main():

    def prime(X): 
            isprime = True 
            if X<2: 
                    isprime = False 
            else: 
                    for i in range(2,X): 
                            if X%i==0: 
                                    isprime = False 
                                    break 
            return isprime 
 
    def factors(X): 
            fact,factlist = 2,[1] 
            for i in range(2,X): 
                    if not X%i: 
                            fact += 1 
                            factlist.append(i) 
            factlist.append(X) 
            return (fact,factlist)
             
    X = int(input('Enter any number: '))
    time.sleep(1)
    print('Prime number:',prime(X))
    time.sleep(1)
    print('Number of factors:',factors(X)[0])
    time.sleep(1)
    print('List of factors:',factors(X)[1])
    time.sleep(1)
    main()
main()





