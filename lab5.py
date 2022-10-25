'''f = open("text.txt", "r")
pos = []
neutral = []
neg = []

for line in f:
    entries= line.split(",")
    entries[1] = int(entries[1].rstrip("\n"))

    if entries[1] == 20:
        pos.append(entries[0])
    elif entries[1] == 0:
        neutral.append(entries[0])
    else:
        neg.append(entries[0])

tweet = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"
tweetWords = tweet.split()
sentiment = 0
for word in tweetWords:
    if word in pos:
        sentiment += 20
    elif word in neg:
        sentiment -= 10

print("the positive words are {}".format(pos))
print("the neutral words are {}".format(neutral))
print("the negative words are {}".format(neg))

f.close()'''


# This reads from a file called text.txt which has only one line. The program should read this line and split it into individual words; these words should be written to the screen and to the file myfile.txt with each word on its own line.

# text = open("text.txt", "r")
# myfile = open("myfile.txt", "w")
# for line in text:
#     words = line.split()
#     for word in words:
#         print(word)
#         f2.write(word + "\n")
# f.close()
# f2.close()
