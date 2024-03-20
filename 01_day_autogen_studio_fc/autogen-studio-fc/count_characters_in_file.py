# filename: count_characters.py

def count_characters_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            return len(contents)
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
# Replace 'example.txt' with the path to the file you want to count characters in.
file_path = 'example.txt'
num_characters = count_characters_in_file(file_path)
print(f"The file has {num_characters} characters.")
