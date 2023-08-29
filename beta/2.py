mod = 10**9 +7
def cal(num_str):
    odd_sum = 0
    even_sum = 0
    for i in range(len(num_str)):
        digit = int(num_str[i])
        if (i+1) % 2 == 1:
            odd_sum += digit
        else:
            even_sum += digit
    return odd_sum* even_sum

def weight(n):
    result = 0
    num_range = 10**n
    for num in range(num_range):
        num_str = str(num).zfill(n)
        result += cal(num_str)
    return result % mod

n = int(input())
print(weight(n))