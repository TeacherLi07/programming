import os

current_script_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_script_path)
os.chdir(current_directory)

def convert_to_txt_format(data_file, output_file):
    with open(data_file, "r", encoding="utf-8") as file:
        with open(output_file, "w", encoding="utf-8") as output:
            for line in file:
                entry = eval(line)
                text = entry["text"]
                labels = entry["labels"]
                for word, label in zip(text, labels):
                    output.write(f"{word} {label}\n")
                output.write("\n")

if __name__ == "__main__":
    data_file_path = r"C:\WeChat Files\WeChat Files\wxid_y5ga6w7e1bg612\FileStorage\File\2023-07\finance_sina.json"
    output_file_path = "!finnance_sina.txt"

    convert_to_txt_format(data_file_path, output_file_path)
