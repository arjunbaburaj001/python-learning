x1, y1, x2, y2, x1second, y1second, x2second, y2second = map(int, input().split())
0 <= x1, y1, x2, y2, x1second, y1second, x2second, y2second <= 10

min_x = min(x1, x1second)
max_x = max(x2, x2second)
min_y = min(y1, y1second)
max_y = max(y2, y2second)

width = abs(max_x - min_x)
height = abs(max_y - min_y)
sidelength = max(width, height)
area = (width * height * width * height)

print(area)
