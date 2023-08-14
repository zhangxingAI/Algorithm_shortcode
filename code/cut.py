def split_sum(n):
    num_str = str(n)
    length = len(num_str)

    dp = [0] * (length+1)


    for i in range(length -1, -1, -1):
        curr_num = 0
        for j in range(i,length):
            curr_num = curr_num * 10 + int(num_str[j])
            dp[i] += curr_num + dp[j+1]
    return dp[0]

n = int(input())
print(split_sum(n))