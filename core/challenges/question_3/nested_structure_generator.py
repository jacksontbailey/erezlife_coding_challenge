def generate_nested_structure(letters, index=0):
    """
    Recursively generates a nested structure of HTML-like tags based on the given array of letters.
    
    Args:
        letters (list): List of letters to be nested in the structure.
        index (int, optional): Current index in the letters array. Used for recursion. Defaults to 0.
        
    Returns:
        str: Nested structure of HTML-like tags with proper indentation.
    """
    if index >= len(letters):
        return ""

    current_letter = letters[index]
    nested_structure = "\t" * index + f"<{current_letter}>\n"
    nested_structure += generate_nested_structure(letters, index + 1)
    nested_structure += "\t" * index + f"</{current_letter}>\n"

    return nested_structure

if __name__ == "__main__":
    # Example usage
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    nested_structure = generate_nested_structure(letters)
    print(nested_structure)