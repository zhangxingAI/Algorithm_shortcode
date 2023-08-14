def split_sum(n):
    num_str = str(n)
    results = []
    def backtrack(start, path):
        if start == len(num_str):
            results.append(sum(path))
            return

        for i in range(start, len(num_str)):
            curr_num = int(num_str[start: i+1])
            backtrack(i+1, path + [curr_num])

    backtrack(0, [])
    total_sum = sum(results)

    return total_sum

n = int(input())
print(split_sum(n))