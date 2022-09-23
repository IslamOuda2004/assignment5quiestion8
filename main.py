
tuple1 = (10, 20, 30, 40, 50)


number = list(tuple1)
arr = []


for var in number:
    arr.append(var)

operation = arr.reverse()


final_tuple = tuple(arr)
print(final_tuple)

