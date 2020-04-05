def first_part_of_tree(height):
    global last_row
    i = 1
    h = height
    while i != height:
        str = (h - 2) * ' ' 
        str += i * "* "
        i += 1
        h -= 1
        last_row = str
        print(str)
   
def second_part_of_tree(height):
    i = 1
    l = len(last_row)
    l = (int((l/2)) + 1 - 3) # number of '*' s 
    while i != height:
        str = 2 * ' ' 
        str += l * "* "
        i += 1
        print(str)
    
first_part_of_tree(7)
second_part_of_tree(3)
