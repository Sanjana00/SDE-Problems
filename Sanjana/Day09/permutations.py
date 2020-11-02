def permute(s, left, right):
    if left == right - 1:
        yield ''.join(s)
    else:
        for i in range(left, right):
            s[i], s[left] = s[left], s[i]
            yield from permute(s, left + 1, right)
            s[i], s[left] = s[left], s[i]

s = list(input())

for perm in permute(s, 0, len(s)):
    print(perm)
