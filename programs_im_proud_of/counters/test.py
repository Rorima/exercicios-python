#with open("c.txt", 'w') as f:
#    f.write('["John", "Doe"]')

def read_the_txt_file():
    # DEPRECATED
    names = []
    with open("c.txt", 'r') as f:
        
        while True:
            line = f.readline()
            if not line:
                break
            
            data1, data2 = line.strip('\n').split(',')
            names.append([data1.strip("'"), data2.strip("'")])

    return names



def read_the_txt_file2():
    names = []
    with open("test.txt", 'r') as f:
        
        while True:
            line = f.readline()
            if not line:
                break
            
            data1, data2 = line.strip('\n').split(',')
            names.append([data1, data2])

        return names


def write_the_txt_files(l):
    with open("test.txt", 'a') as f:
        for items in l:
            f.write(f"{items[0]},{items[1]}\n")


test = [
        ["John", "1"],
        ["Philip", "2"],
        ["Andrea", "3"],
        ["Rebecca", "4"],
        ["Tina", "5"],
        ["Donald", "6"],
        ["Dona", "7"]
]
# write_the_txt_files(test)
#print(read_the_txt_file2())

def test_function():
    print("Right")
    with open('random.txt', 'w') as f:
        pass
    print("Still correct")

def matrix_test():
    str_matrix = [['1','2','3'],['4','5','6'],['7','8','9']]
    int_matrix = [[(i+1) for i in range(3)] for j in range(3)]

    v = int(str_matrix[0][0])
    v += 1
    str_matrix[0][0] = v
    print(str_matrix)

def change_position():

    nums = [[1,2,3],[4,5,6],[7,8,9]]
    new_position = 0
    chosen_list = 2
    
    print(f"Nums before: {nums}")
    
    temp = nums[new_position]
    # print(temp)
    nums[new_position] = nums[chosen_list]
    nums[chosen_list] = temp
    
    print(f"Nums after: {nums}")

def make_empty_text_file():
    f = open('n.txt', 'w')
    f.close()


make_empty_text_file()