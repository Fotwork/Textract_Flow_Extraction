def normalize_lines(lines):
    return [line.lower().strip() for line in lines]

def normalize_text(text):
    text = text.replace('’', "'").replace('«', '').replace('»', '').lower().strip()
    return text