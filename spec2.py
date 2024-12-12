import random
def ex_1():
    number = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    one_tablet = random.choice(number)
    return one_tablet
one_tablet = ex_1()
print (one_tablet)
for i in range(1,one_tablet):
    for j in range(1,i):
        if one_tablet%(i+j)==0 :
            print(i,j)
