word_status={}

with open("poem.txt","r") as f:
    for line in f:
        words=line.split()
        for word in words:
            if word in word_status:
                word_status[word] +=1
            else:
                word_status[word] =1

print (word_status)

word_occurance = list(word_status.values())
max_occurance = max(word_occurance)
print("Maximum occurance of word is: ",max_occurance)
print("Word with maximum occurance:")
for word, max_occ in word_status.items():
    if max_occ==max_occurance:
        print(word)