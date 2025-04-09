#1
'''
T2=0 
t1=0 
c1=0
t2=0
x=0
time=1

while time >0:
    time= int(input("enter 10 km run time = "))
    c1=time+c1
    t1=1+t1
    
    if time==0:
        break
    
    
print("over run ",t1-1)
print("total time = ",c1)
print("averag time = ",c1/(t1-1))
''' 
    
'''
# 2
fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3

str_num=str(fl_num)
nem_float_num =str_num[2:8]
print(nem_float_num)
'''
#3
'''
s = "Tom Jerry Harry"
t1 =s.split(' ')
print(t1)
t2=sorted(t1)
print(t2)
s1=" "
for i in t2:
    s1+=i
    s1+=","
    
    print(s1)


'''
#4
'''

sequence = [10, 20, 30, 40, 50, 60]
for num in sequence:
    num1=sequence[0::2]
    c1=sum(num1)
    num2=sequence[1::2]
    c2=sum(num2)
    
print("odd sum =",c2)
print("even sum =",c1)
'''
#5
USERS = {'user1': 'password1', 'user2': 'password2'}

name_input = input("Enter username: ")
pass_input = input("Enter password: ")

if name_input in USERS and USERS[name_input] == pass_input:
    print("Login successful!")
else:
    print("Error: Invalid username or password.")

#6
T1 = {'a': 1}
T2 = {'a': 2}
T3 = {'b': 3}
t_all = [T1, T2, T3]
t_final = {}

for t in t_all:
    t_final.update(t)

print(t_final)

#7
numbers1 = [10, 20, 30]
numbers2 = [10, 20, 30, 10, 20, 30]

count1 = len(set(numbers1))
count2 = len(set(numbers2))

print(count1)
print(count2)




