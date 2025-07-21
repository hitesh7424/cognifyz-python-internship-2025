'''
Task 05: File Manipulation
Write a Python program that reads a text
file and counts the occurrences of each
word in the file. Display the results in
alphabetical order along with their
respective counts.

'''

def count_occurrence(file_path: str):
    """
    This function takes a file path and returns a dictionary with word frequencies from that file.
    
    Args:
        file_path (str): The file's path string.
        
    Returns:
        dict: A sorted dictionary of words with their frequency counts in descending order.
    """

    try:
        with open(file_path) as f:
            para = f.read().lower()
    except FileNotFoundError:
        return {"FileNotFoundError": "Put proper file path"}

    para_filtered = [c for c in para if c.isalpha() or c.isspace()]
    para_words = "".join(para_filtered).split()
    
    from collections import Counter

    words_occurance = Counter(para_words)
    
    words_sorted = sorted(words_occurance.items(), key=lambda x: x[0])

    max_word_length = max([len(word[0]) for word in words_sorted]) + 1
    
    for word, freq in words_sorted:
        print(f"{word:{max_word_length}}: {freq}")
    
    return dict(words_sorted)


output = count_occurrence("sample.txt")
# print(output)
