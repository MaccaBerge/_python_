'''posisjon = []

x = int(input('X = '))
y = int(input('Y = '))

if x == 0 and y == 0:
    posisjon.append('origo')
if x > 0 and y > 0:
    posisjon.append('første kvadrant')
if x < 0 and y > 0:
    posisjon.append('andre kvadrant')
if y == 0:
    posisjon.append('x-aksen')
if x == 0:
    posisjon.append('y-aksen')

print(*posisjon)'''

x1 = input('x1 = ')
y1 = input('y1 = ')
x2 = input('x2 = ')
y2 = input('y2 = ')

pos1 = (x1, y1)
pos2 = (x2, y2)

print('')