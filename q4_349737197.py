#this works for the sequence, but i cant isolate even values before summing them all up with my current knowledge
'''def seq(n):
        if n <= 1:
            return n
        else:
            return(seq(n-1) + seq(n-2))


terms = int(input('Input a positive integer'))

if terms <= 0:
    print('Plese enter a positive integer')
else:
    for i in range(terms):
        print(seq(i))'''

#every third number of the sequence is a multiple of 2, and im done trying to brute force this. just gonna take the easy way out. this code will just be taking every third number(n3) from the sequence, starting from the third sequence (n3 = 2)
'''this code required research into the fibonnacci sequence, specifically its patterns and trends. code starts at the third number in the sequence, where the equation is 2 = 1 + 1. the next even number is 8 = 5 + 3. the pattern is that n2 + n3 = n1 (1 + 2 = 3).
from there, n1 + n3 = n2 (3 + 2 = 5). finally, you sub in the new values for n1 and n2 into the original equation, n1 + n2 = n3 (3 + 5 = 8). this pattern is repeated to the limit that the user inputs'''

runs = int(input('input a value'))          #user inputs the maximum value
total = 0                                   
n1 = 1                                      #starting values for sequence (2 = 1 + 1)
n2 = 1
n3 = n1 + n2                                

while n3 < runs:                            #while n3 is below the user input, loop following code
    total += n3                             #saves n3
    n1 = n2 + n3                            #this and the following line of code is used to skip two parts of the sequence
    n2 = n3 + n1                            
    n3 = n1 + n2                            #solves for n3 after skipping two parts of the sequence

print(total)