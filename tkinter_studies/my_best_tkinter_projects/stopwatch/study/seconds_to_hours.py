def converter(seconds):
    minutes = int(seconds // 60)
    seconds = seconds % 60
    return f"{minutes}:{seconds:.2f}"

print(converter(122.1))
