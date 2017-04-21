text = input("Text: ").split()
Dictionary = {}
for word in text:
    Dictionary.update({word: str(text.count(word))})
sorted_dictionary = sorted(Dictionary)

for word in sorted_dictionary:
    print("{:{}} : {}".format(word, len((max(Dictionary))), str(text.count(word))))
