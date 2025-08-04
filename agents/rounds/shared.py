def load_markdown_file(file_path):
    """Load markdown file content as text"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()