# print("XD")
# file = open("D:\GrafyGr3\plik.txt")
# content = file.read()
# print(content)
# file.close()

with open('D:\GrafyGr3\plik.txt','r') as file:
    content = file.read()
    print(content)

print("Pierwsza linia:")
with open('D:\GrafyGr3\plik.txt','r') as file:
    first = file.readline()
    print(first)

with open('D:\GrafyGr3\plik.txt','r') as file:
    lines = file.readlines()
    print(lines)

#graf
#zadanie 1:
# wzór:
# l wierzcholków, liczba krawędzi
# pozostałe pary krawędzi
print("Graf zadanie 1:")
#file = open('D:\GrafyGr3\graf.txt')
#first = file.readline()


# lista1 = [] #pusta lista
# lista1.append("element")
# lista1.append(4)
# lista1.append(36.6)
# lista1.append([])
# print(lista1)
#
# for i in range(5):
#     lista1.append(i)
# print(lista1)
#
# lista2 = [x**3 for x in range(3,6)]
# print(lista2)


# with open('D:\GrafyGr3\graf.txt','r') as file:
#     lin1 = file.readline()
#     wierzcholki = lin1.split()
#     print(wierzcholki)
#     ilWierzcholkow = int(wierzcholki[0])
#     ilKrawedzi = int(wierzcholki[1])
#     print(f'Ilość wierzcholków: {ilWierzcholkow}, ilość krawedzi: {ilKrawedzi}')
#     listaNastepnikow = [[] for x in range(ilWierzcholkow)]
#     print(listaNastepnikow)

#Zadanie. Napisz kod w Python, który odczyta graf z pliku i zapisze go w postaci listy sąsiedztwa,
#zadanie wykonaj w dwóch przypadku grafu skierowanego i nieskierowanego.

with open('D:\GrafyGr3\graf.txt','r') as file:
    lin1 = file.readline()
    wierzcholki = lin1.split()
    print(wierzcholki)
    ilWierzcholkow = int(wierzcholki[0])
    ilKrawedzi = int(wierzcholki[1])
    print(f'Ilość wierzcholków: {ilWierzcholkow}, ilość krawedzi: {ilKrawedzi}')
    listaNastepnikow = [[] for x in range(ilWierzcholkow)]
    print(listaNastepnikow)
    #nieskierowany:
    for krawedz in file:
        pq = krawedz.split()
        p = int(pq[0])
        q = int(pq[1])
        listaNastepnikow[p].append(q)
        listaNastepnikow[q].append(p)
    print(listaNastepnikow)



#Odrabianie (28.10.24):

lst_graf = []
mac_graf = [] #macierz wypełniona 0 (9x9)
with open("OD.txt") as file:
    lin1 = file.readline()
    wierz = int(lin1.split()[0])
    kraw = int(lin1.split()[1])
    print(wierz, kraw, wierz+kraw, sep=" ")

    lst_graf = [[] for i in range(wierz)]

    mac_graf = [[0 for x in range(wierz)] for i in range(wierz)]
    print(mac_graf) #macierz incydencji


    zawartosc = [i.strip(' ') for i in file]

    for i in zawartosc:
        wierzcholek = i.split()
        lst_graf[int(wierzcholek[0])].append(int(wierzcholek[1]))
        lst_graf[int(wierzcholek[1])].append(int(wierzcholek[0]))
        mac_graf[int(wierzcholek[0])][int(wierzcholek[1])] = 1
        mac_graf[int(wierzcholek[1])][int(wierzcholek[0])] = 0

    print(lst_graf)
    print(mac_graf)

def wypiszListe(lst):
    for i in range(len(lst)):
        print(i," : ",end="", sep="")

        for el in lst[i]:
            print(el," ",end="")
        print()

wypiszListe(lst_graf)

odw = [0]*len(lst_graf)
skl = [0]*len(lst_graf)
#DFS:
def dfs_rek(lst,start):
    #print(f'Odwiedzony wierzcholek:{start}')
    print(start, end="")
    odw[start] = 1 #np. 1 (że odwiedzone)
    for sasiad in lst[start]:
        if odw[sasiad]==0:
            dfs_rek(lst,sasiad)


#dfs_rek(lst_graf,0)
counter = 1
for i in range(len(lst_graf)):
    if(odw[i]==0):
        print("Składowa",counter, ": ",end="")
        dfs_rek(lst_graf,i)
        counter+=1
        print()

# lst = [[0]*5 for _ in range(5)]
# lst[2][1] = 9999
# print(lst)

V =  int(input("Podaj ilość wierzcholkow:"))
E = int(input("Podaj ilość krawędzi"))
u_graf = [ [] for i in range(V) ]
for i in range(E):
    p = int(input(f'Podaj początek krawędź: {i+1}/{E}: '))
    q = int(input(f'Podaj koniec krawędź: {i+1}/{E}: '))

    u_graf[p].append(p)
    u_graf[q].append(q)

print(u_graf)