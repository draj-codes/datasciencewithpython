#palindorm

def check_palindrom(word):
    if word==word[::-1]:
        print ("Palindrome hai")

    else:
        print ("not a palindorm ")

check_palindrom('nitin')
check_palindrom("mom")
check_palindrom("naman")
check_palindrom('mohan')

# 2
#fibonaki

def give_fibo(n):
    fibo = [0,1]
    for i in range (n-2):
        last= fibo[-1]
        second_last= fibo[-2]
        next_num = last+second_last
        fibo.append(next_num)
    print (fibo)

give_fibo(5)

# prime numbers

def prime(n):
    for i in range (2,n):
        if n%i ==0:
            print ("not a prime")
            break
    else:
        print (" no. is a prime")

prime(5)
prime(4)

# n=5
# print("hello "*n)

# star formation
        
# n=5 
# for i in range (1,n+1):
    # print (i*"*")

# for i in range(1,n+1):
#     print(" "*(n-i)+i*'*')

# def stars(n=5, typ = 'left',shape='*'):
#     if typ == 'left':
#         space=''
#     elif typ== 'right':
#         space='  '
#     elif typ=="middle":
#         space=' '

#     for i in range (1,n+1):
#         print (space*(n-i)+i*f'{shape} ')

# stars(10,'right','IITM')

# def sum_of_narutal(n):
#     res= 0
#     for i in range(1,n+1):
#         res+=i
#     print (res)

# sum_of_narutal(11)

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *=i
#         print(fact)
#     print ("total factorial : ",fact)

# factorial(5)


# def total_sales(*args):   #use of stars means kitne bhi use kr sakte hai matlab ek sai jyda arguument use kr sakte hai. also known as unpaking
#     # *= unpacking 
#     r=0
#     for i in args:
#         r+=i
#     print(r)

# total_sales(1,2,3,4)


sales=[1235,1,123,74,9,55,9,45,87,5,6,9,99,9,9,89,260]
# min_element=sales[0]
# for i in sales[1:]:
#     if i<min_element:
#         min_element = i
# print(min_element)

# max_element =0
# for i in sales[1:]:
#     if i>max_element:
#         max_element = i
# print(max_element)

# def minmax(n,minmx='min'):
#     if minmx =='min':
#         min_element=n[0]
#         for i in n[1:]:
#             if i<min_element:
#                 min_element = i
#         print('minimum ',min_element) 
#     elif(minmx=='max'):
#         max_element =n[0]
#         for i in n[1:]:
#             if i>max_element:
#                 max_element = i
#         print('maximum ',max_element)

# minmax(sales,'min')
# minmax(sales,'max')

# company=['ola','uber','rapido','indrive','adani','tata']
# def caps(c):
#     r=[]
#     for i in c:
#         r.append("#"+i.upper())
#     print(r)

# caps(company)

def records(name,age,sec,roll_no,Class):
    data={'Name':name,'Age':age,'Sec':sec,'Roll_No.':roll_no,'Class':Class}
    import pandas as pd
    result= pd.DataFrame(data,index=[1])
    print (result)

records('Dev',20,'M1',57,'BCA')
records('Dev',20,'M1',57,'BCA')
records('Dev',20,'M1',57,'BCA')
records('Dev',20,'M1',57,'BCA')

def st_records(**kwargs):  # kwaeg mean keyword argument 'also known as dictoionary' 
    import pandas as pd
    result = pd.DataFrame(kwargs,index=[1]) # index is used because if we add only one data then it show error and using index we overcome the error
    print (result)

st_records(Name='Dev',Age=20,Sec='M1',Class='BCA',Address='Delhi')


#one star is used for tuples and 2 stars for dictionary