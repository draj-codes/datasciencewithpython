print("This is my modlue")
#palindrom
def check_palindrom(word):
    if word==word[::-1]:
        print ("Palindrome hai")

    else:
        print ("not a palindorm ")

#fibonaki
def give_fibo(n):
    fibo = [0,1]
    for i in range (n-2):
        last= fibo[-1]
        second_last= fibo[-2]
        next_num = last+second_last
        fibo.append(next_num)
    print (fibo)

#prime Number
def prime(n):
    for i in range (2,n):
        if n%i ==0:
            print ("not a prime")
            break
    else:
        print (" no. is a prime")

#sum of natural number
def sum_of_narutal(n):
    res= 0
    for i in range(1,n+1):
        res+=i
    print (res)

#Total sales
def total_sales(*args):   #use of stars means kitne bhi use kr sakte hai matlab ek sai jyda arguument use kr sakte hai. also known as unpaking
    # *= unpacking 
    r=0
    for i in args:
        r+=i
    print(r)

#minmax
def minmax(n,minmx='min'):
    if minmx =='min':
        min_element=n[0]
        for i in n[1:]:
            if i<min_element:
                min_element = i
        print('minimum ',min_element) 
    elif(minmx=='max'):
        max_element =n[0]
        for i in n[1:]:
            if i>max_element:
                max_element = i
        print('maximum ',max_element)

#show time
def show_time():
    try:
        while True:
            import time
            print (time.asctime())
            time.sleep(1)
            display(clear = True)
    except:
        print ("User intreput")

#factorial

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
        print(fact)
    print ("total factorial : ",fact)

#sound box
def sound_bar(text):
    from gtts import gTTS
    # text = '''data science ki aaj first class hai '''
    audio = gTTS(text)
    audio.save('ds.mp3')

    import pygame as pg
    pg.init()
    pg.mixer.init()
    pg.mixer.Sound('ds.mp3').play()

#stars 
def stars(n=5, typ='left', shape='*'):
    for i in range(1, n + 1):
        if typ == 'left':
            print((shape + ' ') * i)
        elif typ == 'right':
            print(' ' * (n - i) * 2 + (shape + ' ') * i)
        elif typ == 'middle':
            print(' ' * (n - i) + (shape + ' ') * i)
        else:
            print("Invalid type. Use 'left', 'right', or 'middle'.")

