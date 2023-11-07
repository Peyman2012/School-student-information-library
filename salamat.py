class school:
    def __init__(student,weight, height, age):
        student.weight = weight
        student.height = height
        student.age =  age

    def weights(student):
        return student.weight
    def hights(student):
        return student.hights
    def ages(student):
        return student.age






class class_A(school):
    count=0
    list_age = []
    list_weight = []
    list_height = []
    result=[]
    def __init__(student,weight, height, age):
        # student.weight = weight
        # student.height = height
        # student.age = age
        super().__init__(weight, height, age)
        class_A.count+=1

    def ages_list(student):
        class_A.list_age.append(student.age)
        return class_A.list_age

    def weight_list(student):
        class_A.list_weight.append(student.weight)
        return class_A.list_weight

    def hight_list(student):
        class_A.list_height.append(student.height)
        return class_A.list_height
    def value():
        # class_A.count += 1
        # print(student.weight)
        # print(student.age)
        # print(student.height)
        height = sum(class_A.list_height) / len(class_A.list_height)
        class_A.result.append(height)
        print(height)
        weight = sum(class_A.list_weight) / len(class_A.list_weight)
        class_A.result.append(weight)
        print(weight)
        age = sum(class_A.list_age) / len(class_A.list_age)
        class_A.result.append(age)

        print(age)

# a=class_A()
# a.value()
class class_B(school):
    count = 0
    list_age_b = []
    list_weight_b = []
    list_height_b = []
    result_b=[]
    def __init__(student, weight, height, age):
        # student.weight = weight
        # student.height = height
        # student.age = age
        super().__init__(weight, height, age)
        class_B.count += 1
    def ages_list(student):
        class_B.list_age_b.append(student.age)
        return class_B.list_age_b
    def weight_list(student):
        class_B.list_weight_b.append(student.weight)
        return class_B.list_weight_b

    def hight_list(student):
        class_B.list_height_b.append(student.height)
        return class_B.list_height_b
    def value():
        # print(student.weight)
        # print(student.age)
        # print(student.height)
        height=sum(class_B.list_height_b)/len(class_B.list_height_b)
        class_B.result_b.append(height)
        print(height)
        weight = sum(class_B.list_weight_b) / len(class_B.list_weight_b)
        class_B.result_b.append(weight)
        print(weight)
        age = sum(class_B.list_age_b) / len(class_B.list_age_b)
        class_B.result_b.append(age)
        print(age)
height=list(map(int,input().split()))
weight = list(map(int, input().split()))
age = list(map(int, input().split()))
print(height)
height_b=list(map(int,input().split()))
weight_b = list(map(int, input().split()))
age_b = list(map(int, input().split()))
print(height_b)

for i in range(len(height)):
    Information = class_A(height[i], weight[i], age[i])
    # Information2 = class_B(height_b[i], weight_b[i], age_b[i])
    Information.ages_list()
    Information.weight_list()
    Information.hight_list()
    # Information2.ages_list()
    # Information2.weight_list()
    # Information2.hight_list()
for i in range(len(height_b)):
    # Information = class_A(height[i], weight[i], age[i])
    Information2 = class_B(height_b[i], weight_b[i], age_b[i])
    # Information.ages_list()
    # Information.weight_list()
    # Information.hight_list()
    Information2.ages_list()
    Information2.weight_list()
    Information2.hight_list()
print(Information.list_age)
print(Information.list_weight)
print(Information.list_height)
print(Information2.list_age_b)
print(Information2.list_weight_b)
print(Information2.list_height_b)
class_A.value()
class_B.value()
print(class_A.count)
print(class_B.count)
result_a=class_A.result
result_b=class_B.result_b
if result_a[0]>result_b[0]:
    print('A')
elif result_a[0]<result_b[0]:
    print('B')
elif result_a == result_b:
    print('Same')


