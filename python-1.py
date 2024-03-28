""" print("Hello world!")

list=["a","b",'c']
Name=list.append("d")

ls=list.reverse()
print (list) """

""" import keyword
print(keyword.kwlist)
    
 """

""" x=[10,20,30,40]
b=bytearray(x)
for i in b:print(i)
b[0]=100
for i in b:print(i) """


"""  print(list[0])
list.append("MANU");print(list)
list.remove(20);print(list)
list2=list*2; print(list2)

list=(10,20,30,40)

list.remove("Durga");print list """

""" l = list(range(10)) ; print (l)

M = tuple(range(10)) ; print (M) """

""" list=[10,20,30,40]
sum=0
for i in list:
    sum=sum+i
print(sum)

st="chaitra M"
count=0
for i in st:
    count+=1
print(count)

print(len(st)) """


""" str="Chaitra-Manohar"
count=0
for i in str:
    count+=1
print(count)

print(len(str))


list = [1, 2, 3, 4]

print(tuple(list))


def conver_tuple_list(mylist):
    tuple=()
    for i in mylist:
        tuple+=(i,)
    return tuple
mylist=[10,20,30,40]
mytuple=conver_tuple_list(mylist)
print(mytuple)


def swaplist(mynewlist):
    size=len(mynewlist)

    temp=mynewlist[0]
    mynewlist[0]=mynewlist[size - 1]
    mynewlist[size - 1]=temp
    return mynewlist
mynewlist=[100,200,300,400,500]
print(swaplist(mynewlist)) """

""" def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
   
list=[23, 65, 19, 90]
pos1,pos2=1,3

print(swap(list,pos1-1,pos2-1))

a=10 
b=20
maximum=max(a,b)
print(maximum)


def max(a,b):
    if a>=b:
        return a
    else:
        return b
a=50
b=30

print(max(a,b))

def max(a,b):
    if a<=b:
        return a
    else:
        return b
a=50
b=30

print(max(a,b)) """

""" lst=[ 1, 6, 3, 5, 3, 4 ]
i=int(input("Enter the Numer:"))
if i in lst:
    print("Exists")
else:
    print("NotExists") """


""" def list_cloning(lis):
    list_new=lis[:]
    return list_new
lis1=[10,20,30]
list2=list_cloning(lis1)

print("original list:", lis1)

print("copied list:" ,list2) """


""" def countX(lst,x):
    count = 0
    for ele in lst:
        if(ele==x):
            count+=1
    return count
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 6
print('{} has occurred {} times'.format(x,countX(lst, x)))

def countX(lst, x):
    return lst.count(x)
 
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst, x))) """


""" L = [4, 5, 1, 2, 9, 7, 10, 8]
count=0
for i in L:
    count+=i
avg=count/len(L)
print("sum is:",count)
print("avg is:",avg)

## Sum of number digits in List
test_list = [12, 67, 98, 34]
res=[]

for ele in test_list:
    sum=0
    for digit in str(ele):
        sum +=int(digit)
    res.append(sum)
print(res)


def multiply(mylist):
    result=1
    for i in mylist:
        result*=i
    return result
list1=[10,20,30]
list2=[100,200,300]

print(multiply(list1))
print(multiply(list2)) """

#find smallest of the number

""" list=[20,-1,2,3,300]
list.sort()
print("Smallest element is:", list[-1])

list1=[20,-1,2,3,300]
list1.sort(reverse=True)
print("Smallest element is:", list1[0]) """


""" list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

list2=list(set(list1))
list2.sort()

print("Second largest element is:", list2[-2])
 """
#Python program to print even numbers in a list

""" list1 = [10, 21, 4, 45, 66, 93]
list2=[]
list3=[]
list4=[]
for c in list1:
    if c % 2 ==0:
        list2.append(c)
    elif c % 2 !=0:
        list3.append(c)
    else:
        list4.append(c)

print("List of even numbers:",list2)
print("List of odd numbers:",list3)
print("List of alphabets numbers:",list4) """

""" for even_numbers in range(4,15,2):
    print(even_numbers, end='  ')


for odd_numbers in range(1,15,2):
    print(odd_numbers, end='  ') """

""" list1 = [10, 21, 4, 45, 66, 93, 1]
even_count, odd_count = 0, 0

for mc in list1:
    if mc%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count) """

""" list1 = [11, -21, 0, 45, 66, -93]
for num in list1:
    if num >= 0:
        print(num, end=" ") """


""" start, end = -4, 19
for num in range(start, end + 1):
    if num <= 0:
        print(num, end=" ") """

""" list1 = [10, -21, 4, -45, 66, -93, 1]
pos_count, neg_count = 0, 0
for num in list1:
    if num>=0:
        pos_count+=1
    else:
        neg_count+=1

print("pos_count:",pos_count)
print("neg_count:",neg_count) """
#we want to delete each element in the list which is divisible by 2 or all the even numbers. 
""" list1 = [11, 5, 17, 18, 23, 50] 

for num in list1:
    if num % 2 ==0:
        list1.remove(num)
print("New list after removing all even numbers: ", list1) """

""" def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
list1 = [10, 20, 30, 20, 20, 30, 40, 
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))
 """

""" def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
            else:
                result=False
    return result

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b)) """


""" def m1():
    a=10
m1()
print(m1())

a="durga"   
b="durga"   
print("a > b is ",a>b)   
print("a >= b is ",a>=b)   
print("a < b is ",a<b)


print(int("3") < 2) """

""" a,b=10,20
x=30 if a<b else 40
print(x)

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
min=a if a<b else b
print("Minimum Value:",min)
 """

""" a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
min=a if a<b and a<c else b if b<c else c
print("Minimum Value:",min) """

""" x=float(input("Enter Value :"))
print(type(x))

x=10.5
print(type(x)) """
""" 
a,b= [int(x) for x in input("Enter 2 numbers :").split()]

print(a)
print(b)
print("Product is :", a*b)   """

""" l = input("Enter List: ")

print (l) """

""" from sys import argv
print("The Number of Command Line Arguments:", len(argv))
print("The List of Command Line Arguments:", argv) 
print("Command Line Arguments one by one:")
for x in argv:
    print(x) """

""" from sys import argv
sum=0
args=argv[1:]
for x in args:
    n=int(x)
    sum=sum+n
print(args)
print("The Sum:",sum) """

""" print("Hello \n World")
print(10*"Hello")

cart=[10,20,500,700,50,60]
for item in cart:
     if item>=500:
          print("We cannot process this item :",item)
          continue
     print(item) """


""" n1=int(input("Enter First Number:"))
n2=int(input("Enter 2nd Number:"))
n3=int(input("Enter 3rd Number:"))
if n1>n2:
     print("Biggest Number is:",n1)
elif n2>n3:
     print("Biggest Number is:",n2)
else:
     print("Biggest Number is:",n3) """
""" 
#Write a program to check whether the given number is in between 1 and 100

number=int(input("Enter First Number:"))

if number>=1 and number<=100:
     print("which lies between 1 and 100")
else:
     print("which is not lies between 1 and 100")
 """

""" s=input("Enter some String: ")
i=0
for m in s:
    print("The character present at ",i,"index is :",m)
    i=i+1 """

""" list=eval(input("Enter List:")) 
sum=0
for i in list:
    sum=sum+i
print("sum is :",sum) """


#To print numbers from 1 to 10 by using while loop

""" x=1
while x <=10:
    print(x)
    x=x+1 """

""" n=int(input("Enter the numberts:"))
sum=0
x=1

while x<=n:
    sum=sum+x
    x=x+1
    print("The sum of first",n,"numbers is :",sum) """

""" name=""
while name!="manu":
    name=input("Enter Name :")
print("Thanks for the confirmation")


 """


""" i=0
while True:
    i=i+1
    print("Hello",i)   

 """

""" for i in range(4):
    for j in range(4):
         print("i=",i,"   j=",j)

 """


""" n = int(input("Enter number of rows:")) #8
for i in range(1,n+1): # 1 to 9: 1,2,3,4,5,6,7,8,9
     for j in range(1,i+1):
           print("*",end=" ")
     print() """


""" n = int(input("Enter number of rows:"))
for i in range(1,n+1): #1,2,3,4
    print(" " * (n-i),end="")
    print("* "*i) """

""" for i in range(10):
     if i%2==0:
          continue
     print(i) """

""" s="Learning Python is very easy !!!" 
print("Forward direction")
for i in s:
     print(i,end=' ')

print("Forward direction")
for i in s[::]:
     print(i,end=' ')

print("Backward direction")
for i in s[::-1]:
      print(i,end=' ') 
 """

""" s='durga'
print(s[4])

s=input("Enter Some String:") 
i=0
for X in s:
    print("The character present at positive index {} and at nEgative index {}  is {}".format(i,i-len(s),X))
    i+=1

print("manu"+"chaitra") """

""" print("durga "*2)

s="Learning Python is very easy !!!"   
n=len(s)   
i=0   
print("Forward direction")   
while i<n:   
    print(s[i],end=' ')   
    i +=1   
print("Backward direction")   
i=-1   
while i>=-n:   
    print(s[i],end=' ')   
    i=i-1  
 """

""" s="Learning Python is very easy"

print(s.find("iss")) """

""" s="durgaravipavanshiva"

s=input("Enter main string:")
subs=input("Enter sub string:")
try:
    n=s.index(subs)
except ValueError:
    print("substring not found")
else:
    print("substring not found")
 """

""" s=input("Enter main string:")
subs=input("Enter sub string:")
print(s.index(subs)) """

# s=input("Enter main string:")
# subs=input("Enter sub string:")
# flag=False

""" s="abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,7))

s="Learning Python is very difficult" 
s1=s.replace("difficult","easy")
print(s1) """
""" s="abab" 
s1=s.replace("a","b")
print(s,"is available at :",id(s))
print(s1,"is available at :",id(s1))

s="durga software solutions"
s1=s.split()

for x in s1:
    print(x)

d="22-02-2018"
dt=d.split('-')
for m in dt:
    print(m)

t=('sunny','bunny','chinny')
s='_'.join(t)
print(s) """

""" s='learning Python is very Easy' 
print(s.upper()) 
print(s.lower()) 
print(s.swapcase()) 
print(s.title()) 
print(s.capitalize())  """

""" s='learning Python is very easy' 
print(s.startswith('learning')) 
print(s.endswith('learning')) 
print(s.endswith('easy'))  """\

""" s='Learning Python is very Easy'

split=s.split()
l1=[]
i=0
while i<len(split):
    l1.append(split[i][::-1])
    i=i+1
Output=' '.join(l1)
print(Output)
print(l1) """

""" s="B4A1D3"
s1=s2=output=''
for x in s:
     if x.isalpha():
          s1=s1+x
     else:
          s2=s2+x
for x in sorted(s1):
     output=output+x
for x in sorted(s2):
     output=output+x
print(s1)
print(s2)
print(output) """

""" s="a4b3c2"
output=''
for x in s:
     if x.isalpha():
          output=output+x
          previous=x
     else:
          output=output+previous*(int(x)-1)
print(output)
print(previous) """

""" s='ABCDABBCDABBBCCCDDEEEF'
l=[]
for x in s:
     if x not in l:
          l.append(x)
output=''.join(l)
print(output) """


""" s='ABCABCABBCDE'
d={}

for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print("{} = {} Times".format(k,v)) """


n=[0,1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[] 
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers are:",even)
print("odd numbers are:",odd)


l=["A","B","C"]
x=len(l)
for i in range(x):
     print(l[i],"is available at positive index: ",i,"and at negative index: ",i-x)

n=[1,2,2,2,2,3,3] 
print(n.count(1))
print(n.count(2))
print(n.count(3))
