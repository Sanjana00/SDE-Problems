s = input()
max_len = 0
pos = {}
for i, ch in enumerate(s):
    if ch not in pos:
        pos[ch] = i
        continue
    max_len = max(max_len, i - pos[ch])
    pos[ch] = i
print(max_len)

'''
Time Complexity = O(N)

Approach: Store the last position of each character encountered. If encountered again, subtract current position from last position to get length of substring without repetitions.
Maximum length is stored as answer. Update position on encounter.

'''
