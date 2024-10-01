# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
a_count = 0
for letter in word:
    if letter == "а" or letter == "А":
        a_count += 1
print(a_count)

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vowels = ("а", "э", "ы", "о", "у", "е", "ё", "и", "ю", "я")
a_count = 0
for letter in word:
    if letter.lower() in vowels:
        a_count += 1
print(a_count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split(" ")))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(" "):
    print(word[0])
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
length = 0
for word in sentence.split(" "):
    length += len(word)
print(length / len(sentence.split())) # Не сразу вспомнил, что по умолчанию разделение по пробелам.
