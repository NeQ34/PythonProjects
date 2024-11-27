print("Grafy z wagami")
print("25.11.24")

def wczytajGraf(sciezka):
    with open(sciezka) as plik:
        naglowek = plik.readline().split()
        lw = int(naglowek[0])
        lk = int(naglowek[1])

        krawedzie = [i.strip() for i in plik]

        graf = [[] for _ in range(lw)]

        for krawedz in krawedzie:
            krawedz_split = krawedz.split()
            p = krawedz_split[0]
            q = krawedz_split[1]
            w = krawedz_split[2]
            graf[int(p)].append((int(q), int(w)))
            graf[int(q)].append((int(p), int(w)))

        return graf

graf = wczytajGraf("graf(25.11.24).txt")
print(graf)

def waga_grafu(graf):
    waga = 0;
    for i in graf:
        for j in i:
           waga += j[1]
    return waga//2;

print(waga_grafu(graf))

#drzewo bfs:

def drzewo_dfs(start, graf):
    odwiedzone = [0]*len(graf)
    drzewo = [[] for _ in range(len(graf))]

    def dfs(start):
        odwiedzone[start] = 1
        for sasiad in graf[start]:
            if odwiedzone[sasiad[0]] == 0:
                drzewo[start].append(sasiad)
                drzewo[sasiad[0]].append((start, sasiad[1]))
                dfs(sasiad[0])
    dfs(start)
    return drzewo


drzewo = drzewo_dfs(3,graf)
print(drzewo)
print(waga_grafu(drzewo)) # 56 ma byc
