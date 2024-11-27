from collections import deque

print("Algorytm BFS(04.11.24)")

with open('graf.txt','r') as graf:
    lin1 = graf.readline()
    print(lin1)
    wierzcholki = lin1.split()
    print(wierzcholki)
    ilWierzcholkow = int(wierzcholki[0])
    ilKrawedzi = int(wierzcholki[1])
    print(f'Ilość wierzcholków: {ilWierzcholkow}, ilość krawedzi: {ilKrawedzi}')
    listaNastepnikow = [[] for x in range(ilWierzcholkow)]
    print(listaNastepnikow)
    for krawedz in graf:
        pq = krawedz.split()
        p = int(pq[0])
        q = int(pq[1])
        listaNastepnikow[p].append(q)
        listaNastepnikow[q].append(p)
    print(listaNastepnikow)

odwiedzone = []
kolejka = [0]


def bfs(start,graf):
    odwiedzone = [0]*len(graf)#0 - nieodwiedzone 1 - odwiedzone, lista wypelniona zerami
    queue = [start] # kolejka jako zwykla lista
    odwiedzone[start] = 1
    while queue:
        start = queue.pop(0) # pobieramy ten pierwszy element, jezeli bedzie samo pop() to ostatni bierze
        print(start)
        for i in graf[start]:
            if odwiedzone[i] == 0:
                odwiedzone[i] = 1
                queue.append(i)

print("BFS:")
bfs(4,listaNastepnikow)

#Metody deque:
#append()
#appendleft()
#pop()
#popleft()

#poprawiony BFS z kolejką:
def bfsDeque(start,graf):
    odwiedzone = [0]*len(graf)#0 - nieodwiedzone 1 - odwiedzone, lista wypelniona zerami
    queue = deque([start]) # teraz kolejka
    odwiedzone[start] = 1
    while queue:
        start = queue.popleft()
        print(start)
        for i in graf[start]:
            if odwiedzone[i] == 0:
                odwiedzone[i] = 1
                queue.append(i)

print("Poprawiony BFS:")
bfsDeque(4, listaNastepnikow)
