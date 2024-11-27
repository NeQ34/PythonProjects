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