# print stars................
line_number = int(input("Enter line number: ")) + 1

for i in range(int(line_number)):
    star = ''
    for j in range(i):
        star = star + '*'
    print(star)



