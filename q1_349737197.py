'''
Arjun Atwal
Mr. Park
Python basics assignment Q1

This program is controlling a theoretical robot's movements
There are 4 commands:
G → 3 steps forward (right) → GO
S → 0 step → STOP
B → 4 steps backward (left) → BACK
J → 5 steps forward (right) → JUMP
The user will input a starting position, then any combination of the commands listed above. The program interprets the commands into movements and outputs the final position 
'''
from asyncio.windows_events import NULL

def movement(move):                                             #function for input(move)
    l = len(move)                                               #(l) takes the amount of characters in user input to use as the range
    posleft, posright = initial_left,initial_right              #sets starting position

    for commands in range(l):                                   #uses (l) to determine how many times to run the for loop. 
        if(move[commands] == 'G'):                              #identifies the 4 different options. each command either adds to posright or posleft or is a null command(no change in position)
            posright += 3
 
        elif(move[commands] == 'S'):
            NULL                                                #just a command that says do nothing, effectively a placeholder

        elif(move[commands] == 'B'):
            posleft += 4

        elif(move[commands] == 'J'):
            posright += 5

    posfinal = (posright-posleft)                                #final position is posright-posleft
    if posfinal > 0:                                             #if final position is positive, then its moved to the right
        print('Final position of the robot is:', (posfinal), 'to the right') 
    elif posfinal < 0:                                           #if final position is negative, then its moved to the left
        print('Final positon of the robot is:', (-1*posfinal), 'to the left')
    elif posfinal == 0:                                          #if final position is = 0
        print('Final position of the robot is: 0')

                                                                 #all user inputs
initial_left = int(input('Input the initial position to the left (integer value please)'))

initial_right = int(input('Input the initial position to the right (integer value please)'))

move = input('Input any combination of the following commands: \nG → 3 steps forward (right) \nS → 0 steps \nB → 4 steps backward (left) \nJ → 5 steps forward (right)\n: ')

while move not in ('G', 'S', 'B', 'J'):                          #error checking
    move = input('Input any combination of the following commands: \nG → 3 steps forward (right) \nS → 0 steps \nB → 4 steps backward (left) \nJ → 5 steps forward (right)\n: ')
movement(move)                                                   #runs the function

