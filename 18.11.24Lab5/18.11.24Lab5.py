print("18.11.24")
print("Drzewo spinające")

with open("graf.txt","r") as graf:
    liczWierz,liczKraw = map(int, graf.readline().split()) #XD

    print(liczWierz,liczKraw,liczWierz+liczKraw)

    listaNastepnikow = [[] for x in range (liczWierz)]

    for krawedz in graf:
        p,q = map(int,krawedz.split())
        listaNastepnikow[p].append(q)
        listaNastepnikow[q].append(p)

    print(listaNastepnikow)

#dfs:
def dfs(start, graf, built_lst_graf ,odw=[]):
    if len(odw) == 0:
        odw = [0]*len(graf)

    if len(built_lst_graf)==0:
        built_lst_graf = [[] for x in range (len(graf))]
    print(start, end=',')
    odw[start] = 1
    for sasiad in graf[start]:
        if odw[sasiad] == 0:
            built_lst_graf[start].append(sasiad)
            built_lst_graf[sasiad].append(start)
            dfs(sasiad,graf, built_lst_graf,odw) #dfs(sasiad,graf, odw)

# dfs(0,listaNastepnikow)
# print()
# dfs(6,listaNastepnikow)

print("Drzewo spinające: ")

tree = []
dfs(0, listaNastepnikow, tree)
