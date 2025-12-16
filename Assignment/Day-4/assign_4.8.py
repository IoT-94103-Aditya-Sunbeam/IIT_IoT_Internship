def colm_avg(tuples):
    rows = len(tuples)
    cols = len(tuples[0])

    average = []
    for j in range(cols):
        col_sum = sum(tuples[i][j] for i in range(rows))
        average.append(col_sum / rows)
    return average

data = ((10, 10, 10, 12),(30, 45, 56, 45),(81, 80, 39, 32),(1, 2, 3, 4))
result = colm_avg(data)
print("Column-wise averages:", result)