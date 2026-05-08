def count_unique_words(sentence):
    return len(set(sentence.split()))
print(count_unique_words("apple banana apple orange"))
