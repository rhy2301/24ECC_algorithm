
N = int(input().strip())

coordinate = [input().strip() for _ in range(N)]

sorted_coordinate = sorted(coordinate, key = lambda coordinate: (coordinate[1], coordinate[0]))

for x,y in sorted_coordinate:
    print (x, y)

