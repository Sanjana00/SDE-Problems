def word_break(word_list, s, n, res):
    for i in range(1, n + 1):
        prefix = s[:i]
        if prefix in word_list:
            if i == n:
                res += prefix
                print(res)
                return
            word_break(word_list, s[i:], n - i, res + prefix + ' ')

word = input()
word_list = input().split()

word_break(word_list, word, len(word), '')
