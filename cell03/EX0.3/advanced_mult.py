print("Table de 0: 0 0 0 0 0 0 0 0 0 0")
row = 1
while row <= 10:
    print(f"Table de {row}: ", end="")
    col = 0
    while col <= 10:
        print(row * col, end=" ")
        col += 1
    print()
    row += 1