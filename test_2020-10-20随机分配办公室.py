import random
offices = [[],[],[]]
names = ['张老师', '李老师', '赵老师', '高老师','刘老师', '周老师', '王老师', '吴老师']
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
flag = 1
for tempNames in offices:
    print("办公室%d的人数为： %d" % (flag,len(tempNames)))
    flag += 1
    for name in tempNames:
        print("%s" % name,end = ' ')
    print(" ")
