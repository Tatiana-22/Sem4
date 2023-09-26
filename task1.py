#1. Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

Array_orig = [[5, 4, 3], [1, 7, 6]] 
Array_new = [[5, 1], [4, 7], [3, 6]]

for a in range(len(Array_orig)): 
    for b in range(len(Array_orig[0])): 
        Array_new[b][a] = Array_orig[a][b]
print("Новая матрица: ") 
for res in Array_new: 
    print(res)
