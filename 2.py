# Завдання 1
f = open("data.txt", "w", encoding="utf-8")
for _ in range(3):
    s = input("Введіть рядок: ")
    f.write(s + "\n")
f.close()

# Завдання 2
try:
    f = open("data.txt", "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    for i in range(1, len(lines), 2):
        print(lines[i].strip())
except FileNotFoundError:
    print("Файл data.txt не існує")

# Завдання 3
f = open("data.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("filtered.txt", "w", encoding="utf-8")
for line in lines:
    if "Python" in line:
        f.write(line)
f.close()

# Завдання 4
name = input("Введіть ім'я файлу: ")
f = open(name, "r", encoding="utf-8")
text = f.read()
f.close()
cleaned = ""
for ch in text:
    if not ch.isdigit():
        cleaned += ch
f = open("cleaned.txt", "w", encoding="utf-8")
f.write(cleaned)
f.close()

# Завдання 5
f = open("log.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()
word = ""
words = []
for ch in text:
    if ch.isalnum():
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""
if word != "":
    words.append(word)
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
top = []
for _ in range(10):
    if not freq:
        break
    max_word = None
    max_count = -1
    for w in freq:
        if freq[w] > max_count:
            max_count = freq[w]
            max_word = w
    top.append((max_word, max_count))
    del freq[max_word]
f = open("word_stats.txt", "w", encoding="utf-8")
for w, c in top:
    f.write(w + ": " + str(c) + "\n")
f.close()

# Завдання 6
f = open("data.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
f = open("reversed.txt", "w", encoding="utf-8")
for line in lines[::-1]:
    f.write(line)
f.close()