#sec 2
#1
'''
name = input("please Enter your Name  ")
age = input("please Enter your Age  ")
print ("your name " ,name)
print('your age',age)
#2
count = int(input("Enter count: "))
char = input("Enter character to repeat: ")

print(char*count) # print the character repeated <count> times
#3
file_name = "/home/user/projects/my_project/file.txt"

N_F = file_name.split("/")[-1]  
F_T = N_F.split(".")[-1] 

print(f"File Name: {N_F}")
print(f"File Type: {F_T}")

#4
my_str = "    hello           world          "

my_str = my_str.strip()#تشيل المسفات  من البدايه لي النهايه وتسيب الي بين الكلام
my_str = my_str.title()#تجعل أول حرف من كل كلمة كبيرًا 
sub_strs = my_str.split(' ')#تقسم الجمله بناءا علي الفرغات وتحفظهم في list
my_str = sub_strs[0].upper() + ', ' + "python".title() + '!'#upper تخلي كلي حروف الكلمه كبيره 
print(my_str)

#5
s = "Hello world"

s = s.replace("world", "Tomas")  # استبدل "YourName" باسمك

print(s)

#6
t1 = "Hello world"

t2 = t1.find("o")  # إيجاد الفهرس الأول لحرف "o"
t3 = t1.find("o", t2 + 1)  # البحث عن "o" الثاني بعد الأول

print(t3)

#7
t1 = "Hello world"

count_o = t1.count("o")  # عدّ عدد مرات ظهور "o"

print(count_o)

#8
a = 1 / 3  # 0.3333333333333333
b = 2 / 3  # 0.6666666666666666

# Note the rounding

print(f"{a:.4f} + {b:.4f} = {a + b:.4f}")#ده بيجمع a,b بس عن طريقformat

print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(chr(72) + chr(111) + chr(119) + chr(33)) #How! بيجيب الحروف من القموس

#9
s = "Hello world"

print(s[-5:] + ' ' + s[0:5]) #عكس الكلمتين

#10.1
L=[]
L.append(1),L.append(2),L.append(3)
print(L)

#10.2
L=[1,5,8]
L1=[7,3,9]
L.extend(L1)
print(L)

#10.3
L=[1,5,9,8,74,23,36]
L.insert(3, 4)
print(L)

#10.4
L=[1,5,9,8,74,23,36]
L.pop()
print(L)

#10.5
L=[1,5,9,6,74,23,36]
L.remove(6)
print(L)

#10.6
L = [1, 2, 3, 4, 5]

index3 = L.index(3)  

print(index3)

#10.7
L = [1, 2, 3, 4, 5]

L.reverse()

print(L)

#10.8
L = [1, 2, 3, 4, 5]

L1=L[:3]

print(L1)

#10.9
#What is the difference between list.sort and sorted
lst = [2, 4, 1, 5, -1]
print(sorted(lst))#بتغير في ال القاءمه نفسها

lst.sort()#بتغير وبتحفظ في قاءمه جديده
print(lst)

#10
lst1 = []
lst2 = [1,2,3]

lst1.append(lst2)
lst1.append(lst2)
lst1.append(lst2)

lst1[0][0] = 10

print(lst1)
#يتم إضافة نفس القائمة (lst2) إلى lst1 ثلاث مرات، ولكن ليس كنسخة منفصلة، بل كمراجع (References) لنفس الكائن في الذاكرة
#لحل المشكله هنعمل نسخه من(lst2)في كل مره هنضيف فيها حاجه
# الحل 
lst1 = []
lst2 = [1,2,3]

lst1.append(lst2.copy())
lst1.append(lst2.copy())
lst1.append(lst2.copy())

lst1[0][0] = 10

print(lst1)
'''





















