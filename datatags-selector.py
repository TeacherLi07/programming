def get_unique_labels(tags_file):
    with open(tags_file, 'r', encoding='utf-8') as t_file:
        tags = t_file.read().splitlines()

        unique_labels = set()
        for tag_line in tags:
            labels = tag_line.split()
            unique_labels.update(labels)

    return list(unique_labels)

# 调用统计函数并输出结果到屏幕
tags_file = "D:\\lxh2\\控江\\交大荣昶杯\\github训练集\\NER-BERT-pytorch\\train\\tags.txt"
unique_labels = get_unique_labels(tags_file)
print(unique_labels)
