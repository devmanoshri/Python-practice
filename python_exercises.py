
def count_Num(num):
    f = open("D:\\PythonProjects\\Exercises\\input.txt", "r")

    token = ''
    for line in f:
        token = token + line.strip() + ','
    return(token.count(str(num)))
    f.close()


# print(count_Num(9))
# print (count_Num(100))

# def append_sum():

f = open("D:\\PythonProjects\\Exercises\\input.txt", "r")
f_out = open("D:\\PythonProjects\\Exercises\\output.txt", "w")

for line in f:
    token = line.split(',')
    sum_val=0
    for element in token:
        sum_val = sum_val + int(element)
    print(sum_val)
    f_out.write("sum:" + str(sum_val) + " | " + line)


f_out.close()
f.close()