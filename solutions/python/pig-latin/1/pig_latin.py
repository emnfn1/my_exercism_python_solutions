def translate(text):
    vowels = set("aeiou")
    words = text.split()
    translated_words = []
    for word in words:
        if word.startswith(("yt", "xr")):
            translated_words.append(word + "ay")
            continue
        for i, ch in enumerate(word):
            if ch == "u" and i > 0 and word[i-1].lower() == "q":
                translated_words.append(word[i+1:] + word[:i+1] + "ay")
                break
            if ch.lower() in vowels or (ch == "y" and i != 0):
                translated_words.append(word[i:] + word[:i] + "ay")
                break
    return " ".join(translated_words)
