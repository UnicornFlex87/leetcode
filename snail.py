def snail(matrix):
    result = []
    if not matrix or not matrix[0]:
        return result

    while matrix:
        # 1. Take the first row
        result.extend(matrix.pop(0))

        # 2. Take the last element of each remaining row
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # 3. Take the last row (reversed)
        if matrix:
            result.extend(matrix.pop()[::-1])

        # 4. Take the first element of each remaining row (in reverse order)
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result
