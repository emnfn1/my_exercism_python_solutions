def response(hey_bob):
    msg = hey_bob.strip()
    if msg == "":
        return "Fine. Be that way!"
    
    is_question = msg.endswith("?")
    is_yelling = msg.isupper()
    
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_yelling:
        return "Whoa, chill out!"
    return "Whatever."
