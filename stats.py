# Returns the number of words within a passed string
def get_num_words(text):
    words = text.split()
    return len(words)

# Counts characters in passed string and puts it in a dictionary
def get_chars_dict(text):
    dupes = {}
    for ch in text:
        ch_lower = ch.lower()
        if ch_lower in dupes:
            dupes[ch_lower] += 1
        else:
            dupes[ch_lower] = 1
    return dupes

# Helper function for sorted_list(dupes)
def sort_on(items):
    return items["num"]

# Sorts a dictionary and returns a sorted list of dictionaries
def sorted_list(dupes):
    char_list = []
    for key, value in dupes.items():
        char_list.append({"char": key, "num": value})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list