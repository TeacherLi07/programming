import json

# Read the JSON file
with open(r'D:\迅雷下载\template (1).json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Extract the "text" values from the "segments" list
text_list = [segment["result"]["text"] for segment in data.get("segments", [])]

# Join the "text" values into one paragraph
paragraph = " ".join(text_list)

# Write the paragraph to a text file
with open(r'D:\迅雷下载\template (1).txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(paragraph)

print("Text has been extracted and written to 'template.txt'.")
