def sum_it(num_itrble):
    
    summed = sum(num_itrble)
    
    def square_it(amount):
        return amount * amount
    
    return square_it(summed)


lst = [1, 2, 3]
print(sum_it(lst))
