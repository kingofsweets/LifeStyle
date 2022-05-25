def intersection(l_1_x,l_1_y, r_1_x, r_1_y, l_2_x, l_2_y, r_2_x, r_2_y):
    left = max(l_1_x, l_2_x)
    bottom = max(l_1_y, l_2_y)
    right = min(r_1_x, r_2_x)
    top = min(r_1_y, r_2_y)

    width = right - left 
    height = top - bottom 

    if width <= 0 or height <= 0:
        return False
    else:
        return True

num = int(input())

dots = []

for i in range(num):
    dots.append([int(j) for j in input().split()])

for i in dots:
    count = -1
    for iter in range(len(dots)):
        if intersection(i[0], i[1], i[2], i[3], dots[iter][0], dots[iter][1], dots[iter][2], dots[iter][3]):
            count +=1
    
    print(count, end=' ')    