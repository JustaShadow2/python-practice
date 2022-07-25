'''errors in the original code included the whole thing. put simply, it was significantly longer than needed. even this method is not the most efficient and easiest, but is definitely still relatively simple and leaves room for explanation'''
points = {'a': 1, 'e': 1,'i': 1,'l': 1,'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,'u': 1, 'd': 2, 'g': 2, 'b': 3,'c': 3,'m': 3,'p': 3,'f': 4,'h': 4,'v': 4,'w': 4,'y': 4,'k': 5, 'j': 8,'x': 8,'z': 10,'q': 10}
'''sets a number(value) to each letter'''
def word_count(word): #defines a function
    count = 0         #sets count to 0
    for letters in word:    #only letters included in the input are applicable
        count += points[letters]    #every letter in the input has its corresponding value(points) called. The sum of all values is set to count
    print('This word is worth', count, 'points.')   #prints the total points for the inputted word
    
word = input('gimme words') #user inputs word
word_count(word)    #runs above function