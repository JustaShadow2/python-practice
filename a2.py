# s2 groups

x = int(input())                                                #user intputs int, determines the amount of names need to be inputted 
first = [input().split() for _ in range(x)]                     #iterates through x values (names), stores data in a list (first). split seperates each pair of inputs and stores them in a list (first). these pairs must be together

y = int(input())                                                #same processs as above, but the parameter is that these pairs must not be together
second = [input().split()  for _ in range(y)]                   

z = int(input())                                                #input used to determine amount of times the for loop below iterates (how many groups are made)
third = [set(input().split()) for _ in range(z)]                #puts all groups into sets

violations = 0                                                  #sets violations (how many times the restrictions or parameters have been broken) to 0

together = {} # must be together                                #empty dictionary which will hold names of people that need to be together
for s1, s2 in first:                                            #s1 and s2 iterates through each pair of names in first
    if s1 not in together:                                      #error checking for duplicate keys
        together[s1] = {s2}                                     #takes the first name in a pair and makes it a key, makes the second name a value (as a set) in the dictionary. s1 and s2 are assigned as key and value respectively in together if the key (s1) doesnt exist in together
    else:
        together[s1].add(s2)                                    #Adds a restriction as a value (s2) if the key (s1) already exists (if s1 appears again with a different s2, the new s2 value is added to the previous value(s) as a set)
    
separate = {} # must be separate                                #same functions as together (block of code above) but assigned to a different empty dictionary and iterates through pairs in second
for s1, s2 in second:                                           
    if s1 not in separate:
        separate[s1] = {s2}
    else:
        separate[s1].add(s2)                                    

for group in third:                                             #iterates through sets in third
    for member in group:                                        #checks the names of each member in group

        # checking if the needed people are together
        if member in together:                                  #checks if the name is in together as part of a mandated group.
            diff = together[member] - group                     #difference operation between two sets, group and together. '-' is used because both are sets (binary operator). Checks the sets for elements that are not shared between them, and if any exist in together that do not exist in group, the names are added to diff adding +1 to the len. if the names in group are also in together, the result of diff is a null set
            violations += len(diff)                             #if the names exist in both group and together, that means the condition is met and diff is a null set. Therefore len(diff) = 0 so violations do not change. if the pairs in together do not exist in group, that means the condition has not been met, the set(diff) will have values. Therefore adding +1 to violations for each time the constraint is not met.

        # check if ppl are separated
        if member in separate:                                  #checks if the name is in seperate as part of groups that cannot be together. If the name does not exist, it goes back to the begininning of the for loop
            inter = group & separate[member]                    #bitwise operator used for the intersection operation between the sets group and seperate. checks group and seperate for any shared elements. if any exist, they are put into a different set(inter). if not, inter is a null set
            violations += len(inter)                            #len of inter += violations. the only values in inter are elements that exist in both group and seperate, which count as violations. if violations occured, then the value will increase, if not then it will not change

print(violations)                                               #Outputs number of times that restrictions were not followed