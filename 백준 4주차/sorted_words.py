N = int(input().strip())
words = {input().strip() for _ in range(N)}

sorted_words = sorted(words, key = lambda x: (len(x), x))

for word in sorted_words:
    print(word)
    