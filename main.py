wysokosc=int(input("jak wysoka ma byc choinka: "))#pytanie o wysokość choinki
znak=input("W jakim znaku ma byc choinka: ")#Jaki znam; mozna uzyc dowolnego znaku 

#początek I pętli
for A in range(wysokosc):
    for B in range(wysokosc-A):
        print(' ', end=' ')
    for C in range(2*A+1):
        print(znak,end=' ')
    print()

#początek II pętli
for A in range(2):
    for B in range(wysokosc-1):
        print(' ', end=' ')
    print(2*znak)

txt = " WESOŁYCH ŚWIĄT ŻYCZY JAKUB "

iloscZnakow = len(txt)#liczenie ilość znaków
x = txt.center(wysokosc*2+iloscZnakow, znak)#ilość znaków jest równa wysokości choinki

print(x)
