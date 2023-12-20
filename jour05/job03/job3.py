def draw_triangle(height):
    for i in range(height):
        if i == 0:
            print('_' * (height - i - 1) + '/')
        elif i == height - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print('/' + ' ' * (2 * i) + '\\')

draw_triangle(5)
