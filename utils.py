def format_advice(text):

    lines = text.split("\n")

    cleaned = []

    for line in lines:

        if line.strip() != "":
            cleaned.append(line.strip())

    return cleaned
