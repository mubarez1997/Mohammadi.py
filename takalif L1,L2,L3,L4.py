'''
#taklif_L1
print('hello world')

a=70
b=20
c=a+b
d=a-b
f=a**b
e=a*b
j=a//b
print(c)
print(d)
print(e)
print(f)
print(j)

a=70
b=20
c=a>b
print(c)
d=a>=b
print(d)
f=a<=b
print(f)
e=a==b
print(e)
j=a!=b
print(j)

zarf='my name is abdullah'
print(type(zarf))
print(len(zarf))
print(zarf)



# taklif_L2
#L1 --------------> kar ba tavabe resta ha:

name='abdullah'
print(type(name))
new_name=name.upper()
print(new_name)
new_name=name.lower()
new_name=name.title()
new_name=name.capitalize()
new_name=name.strip()
'''
# tavabe mohim str ha dar bala bayan shod.
.upper() -------------> hama harf ha ra bozorg mikonad
.lower() -------------> hama harf ha ra kochak mikonad
.title() -------------> harf aval har kalema ra bozorg mikonad
.capitalize() --------> tanha harf aval jomla ra bozorg mikonad
.strip() -------------> space ha ra az do taraf hazaf mikonad


'''
# L2 ----------------------------> mohesaba qemat mahsol ba talkhfif

product_name=input(' what is your product name> :').title()
product_price=float(input(' howmuch is your price? :'))
final_price=0.75*product_price
print(final_price)
print(product_name)

print('qemat nehaye mahsol',product_name,'hast',final_price)

# L3 ---------------------> mohaseba qemat mahsol ba talkhfif delkhah.


product_name=input(' what is your product name> :').title()
product_price=float(input(' howmuch is your price? :'))
discount=float(input(' darsad talkfif bede (0-100) ? :'))
final_price=(1-discount/100)*product_price
print(final_price)
final_name=product_name.upper().strip()
print(f'qemat nehayi mahsol{final_name} barabar hast ba {final_price}')

'''
darsad talkhfif az karbar megerim va balaye qemat asli vared mekonim.
qemat nehayi neshan dada shavad


'''


#L4 -------------------> Barasi teddad horof name karbar.

name=input('what is your name? :')
num_characters=int(input(' number of your name? :'))
print(len(name))==num_characters

'''
teddad horof asli karbar ba addadi ke karbar vared mikonad ra moqayesa mekonim.
agar dorost bod ---------- True 
agar nabod ---------------False


'''

# talklif_L3

#L1---------------- > barasi etelait vorodi

#name=input(' what is your name? :')
name='abdullah'
name.isdigit()
name.isalpha()
name.isalnum()
name.islower()
len(name)>8


# L2 --------------------->moderiat list nomarat tamren

scorse=[15,18,12,20,16]
scorse.append(19)
print(scorse)
scorse=[15,18,12,20,16]
scorse.pop(2)
print(scorse)
scorse[1]=17
print(scorse)
scorse.insert(2,14)
print(scorse)
scorse.sort()
print(len(scorse))

#L3 ----------------------> Tamren 3

a=[10,20,30]
b=[40,50]

a.append(b)
print(a)
print(len(a))

a=[10,20,30]
b=[40,50]

a.extend(b)
print(a)
print(len(a))

'''
.apped()------------------>  ba shakli list yak iteam dar list degar ezafa mesha.
.extent()-----------------> iteam ha ye list degar ba list avali ba skhakli element ezafa mesha.

'''

#L4 -------------------------> tamren 4

student=("Ali",21,'Tehran')
print(student[0])

new_student=list(student)
print(new_student)
new_student[1]=22
new_student[2]='shiraz'
print(new_student)

student=tuple(new_student)
print(student)

# L4 ----------------> moderiat etaliat yak kanishjo ba dictionary

student={ "name":'Ali', 'age':20, 'city':'Tehran', 'score':17}
student["name"]
student.get("name")

student['score']
student['age']=21
print(student)

student['university']='UT'
print(student)

student['city']='shiraz'
print(student)

student.get('phone','not found')

keys=student.keys()
print(keys)

values=student.values()
print(values)

print(student)

#L5 -------------------------> system etebar sabge code talkhfif

product_name=input(' what is your product name? :')
product_price=float(input(' qemat mahsol chand hast ? :'))
discout_code=input(' code talkhfif chand hast? :')
new_name=product_name.title().strip()
print(new_name)

if discout_code.upper()=='PYTHON20':
    print(0.8*product_price)
else:
    print(product_price)
print(product_price)
    

#L6----------------------> proje kochak sabt sefarish foroshga

customer_name=input('what is your name? : ')
product_name=input(' what is your product name? :')
product_code=input(' code mahsol chist? : ')
product_price=float(input(' qemat mahsol chand hast ? :'))
num_offer=int(input(' teddad sefarish? :'))
discout_code=input(' code talkhfif chand hast? :')
new_name=customer_name.title().strip()
print(new_name)




'''
cd C:\
python -m venv cnn_env
C:\cnn_env\Scripts\activate
pip install tensorflow numpy matplotlib spyder-kernels


























































