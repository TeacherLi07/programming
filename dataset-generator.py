def merge_files(sentences_file, tags_file, output_file):
    with open(sentences_file, 'r', encoding='utf-8') as s_file, open(tags_file, 'r', encoding='utf-8') as t_file, open(output_file, 'w', encoding='utf-8') as out_file:
        sentences = s_file.read().splitlines()
        tags = t_file.read().splitlines()

        if len(sentences) != len(tags):
            raise ValueError("The number of sentences and tags do not match.")

        for sentence, tag in zip(sentences, tags):
            words = sentence.split()
            labels = tag.split()
            if len(words) != len(labels):
                raise ValueError("The number of words and labels in a line do not match.")

            for word, label in zip(words, labels):
                out_file.write(f"{word} {label}\n")
            out_file.write("\n")  # Add an empty line after each sentence

    print(f"Files '{sentences_file}' and '{tags_file}' merged successfully into '{output_file}'.")

# 调用合并函数
merge_files("D:\\lxh2\\控江\\交大荣昶杯\\github训练集\\NER-BERT-pytorch\\test\\sentences.txt", "D:\\lxh2\\控江\\交大荣昶杯\\github训练集\\NER-BERT-pytorch\\test\\tags.txt", "D:\\lxh2\\控江\\交大荣昶杯\\github训练集\\NER-BERT-pytorch\\test\\test.txt")
