n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def get_max_cut(n, k, rows, cols, permutation):
    if n > 0:
        first_group_sum, first_permutation = get_max_cut(n - 1, k + 1, rows + [k + 1], cols, permutation + ' 1')
        second_group_sum, second_permutation = get_max_cut(n - 1, k + 1, rows, cols + [k + 1], permutation + ' 2')
        if first_group_sum > second_group_sum:
            return first_group_sum, first_permutation
        else:
            return second_group_sum, second_permutation
    else:
        total = 0
        for row in rows:
            for col in cols:
                total += matrix[row][col]
        return total, permutation


print(*get_max_cut(n - 1, 0, [0], [], '1'), sep='\n')
