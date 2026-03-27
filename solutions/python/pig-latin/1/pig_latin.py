def translate(text):
    vocals = "aeiou"
    def translate_word(word):
        if word.lower().startswith(("a", "xr", "yt")):
            return word + "ay"

        consonants = []
        if "qu" in word.lower():
            current_vocals = vocals[:-1]
        else:
            current_vocals = vocals

        for ch in word.lower():
            if ch in current_vocals or ch == "y":
                break
            consonants.append(ch)

        cons_char = "".join(consonants)

        if word.lower().startswith("y"):
            cons_char += "y"

        word_cut = word[len(cons_char):]
        return word_cut + cons_char + "ay"

    words = text.split()
    translated_words = [translate_word(w) for w in words]
    return " ".join(translated_words)

