def pascal_tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        row = [1]
        last_row = pascal_tri(n - 1)

        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i + 1])
            
        row += [1]

    return row


print(pascal_tri(4)) # 4. step

