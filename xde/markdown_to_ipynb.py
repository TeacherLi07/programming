import os
import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

def strip_newlines(cell_source):
    # Remove leading and trailing newlines from code cells
    return cell_source.strip('\n')

def markdown_to_ipynb(markdown_file, output_dir):
    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Split the markdown content into cells
    cells = markdown_content.split('```')

    # Create a new Jupyter Notebook
    notebook = new_notebook()

    # Iterate through cells and add them to the notebook
    for i, cell in enumerate(cells):
        if i % 2 == 0:
            # Markdown cell
            notebook.cells.append(new_markdown_cell(source=cell))
        else:
            # Code cell without the 'python' label
            # code_cell_source = strip_newlines(cell)
            code_cell_source = strip_newlines(cell.lstrip('python \n'))
            notebook.cells.append(new_code_cell(source=code_cell_source))

    # Save the notebook to a .ipynb file
    output_file = os.path.join(output_dir, os.path.basename(markdown_file).replace('.md', '.ipynb'))
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

def convert_all_md_to_ipynb_recursive(base_directory):
    # Iterate over all files and subdirectories in the base directory
    for root, dirs, files in os.walk(base_directory):
        for filename in files:
            if filename.endswith(".md"):
                md_file_path = os.path.join(root, filename)
                output_directory = root
                # os.makedirs(output_directory, exist_ok=True)
                markdown_to_ipynb(md_file_path, output_directory)

# Example usage
base_directory = r'D:\programming\xde\xde-webclub-course\course\docs'

convert_all_md_to_ipynb_recursive(base_directory)
