import os

current_script_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_script_path)
os.chdir(current_directory)

def read_bio_data(file_path):
    bio_data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                bio_data.append(line)
            else:
                bio_data.append("")  # Add an empty string for empty lines
    return bio_data

def merge_bio_tags(a_tags, b_tags):
    merged_tags = []
    for a_tag, b_tag in zip(a_tags, b_tags):
        if a_tag.endswith(" O") and not b_tag.endswith(" O"):
            merged_tags.append(b_tag)
        else:
            merged_tags.append(a_tag)
    return merged_tags

def write_merged_data(merged_tags, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for tag in merged_tags:
            file.write(tag + "\n")

def merge_and_write(a_file, b_file, output_file):
    a_tags = read_bio_data(a_file)
    b_tags = read_bio_data(b_file)

    merged_tags = merge_bio_tags(a_tags, b_tags)

    with open(a_file, "r", encoding="utf-8") as a, open(b_file, "r", encoding="utf-8") as b:
        line_number = 1
        with open(output_file, "w", encoding="utf-8") as c:
            for a_line, b_line, merged_tag in zip(a, b, merged_tags):
                a_line = a_line.strip()
                b_line = b_line.strip()

                if a_line:
                    c.write(f"{a_line} {merged_tag}\n")
                else:
                    c.write("\n")  # Preserve empty lines

                print(f"Processed line {line_number}")
                line_number += 1

if __name__ == "__main__":
    a_file_path = "train.txt"
    b_file_path = "train-domain copy.txt"
    output_file_path = "c.txt"

    merge_and_write(a_file_path, b_file_path, output_file_path)