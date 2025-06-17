string = ["abc.msss", "abc.mdfs", "mashina", "kaaaif", "abcdefg"]
for i in range(len(string)):
    if string[i].startswith('abc'):
        string[i] = string[i].replace('abc', 'www')
    else:
        string[i] = string[i] + 'zzz'
print(string)