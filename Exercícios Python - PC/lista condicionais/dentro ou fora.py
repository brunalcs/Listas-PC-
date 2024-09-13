x1, y1, x2, y2 = map(int, input().split())
px, py = map(int, input().split())

if x1 <= px <= x2 and y1 <= py <= y2:
  print ("Dentro!")
else:
  print("Fora!")