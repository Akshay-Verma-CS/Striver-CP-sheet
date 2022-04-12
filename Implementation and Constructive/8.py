d={"Tetrahedron":4, "Cube":6, "Octahedron":8, "Dodecahedron":12, "Icosahedron":20}
summ=0
for i in range(int(input())):
    summ+=d[input()]
print(summ)


