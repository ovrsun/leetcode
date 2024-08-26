# a = 'tkkttkkt'

a = 'abac'

print(len(a))
p = [0] * len(a)

j = 0
i = 1

while i < len(a):
    if a[j] == a[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)
length = len(a) - p[len(a) - 1]
print(length)
print(a[:length], 'vs', a[len(a) - length:])
if a[:length] == a[len(a) - length:] and p[-1] != 0:
    print(True)
else:
    print(False)

