def find_anagrams(word, candidates):
    anagrams = [item for item in candidates if sorted(word.lower()) == sorted(item.lower()) and word.lower() != item.lower()]
    return anagrams
