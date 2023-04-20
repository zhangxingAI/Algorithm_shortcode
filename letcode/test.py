fast = 1
slow = 5
while fast != slow:
    if fast is None or fast+1 is None:
        print('null')
    fast, slow = fast+2, slow+1
print(slow)