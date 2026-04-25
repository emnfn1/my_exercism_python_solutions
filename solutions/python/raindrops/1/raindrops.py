def convert(number):
    mappings = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    result = []
    for key, sound in mappings:
        if number % key == 0:
            result.append(sound)

    return "".join(result) or str(number)
