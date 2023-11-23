# coding: utf-8

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdknlp.v2.region.nlp_region import NlpRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdknlp.v2 import *
import os

current_script_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_script_path)
os.chdir(current_directory)

def read_sentences(file_path:str):
    with open(file_path, "r", encoding="utf-8") as file:
        sentences = []
        current_sentence = ""

        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue

            if len(current_sentence) + len(line) <= 512:
                current_sentence += line + " "
            else:
                if current_sentence:
                    sentences.append(current_sentence.strip())
                else:
                    print("Warning: A sentence is longer than 512 characters and will be skipped.")
                current_sentence = line + " "

        # Add the last sentence if there's any remaining text
        if current_sentence:
            sentences.append(current_sentence.strip())

    return sentences

def req_and_write(reqtext:str):
        request = RunNerRequest()
        request.body = NerRequest(
            lang="zh",
            text=reqtext
        )
        response = client.run_ner(request)
        response_obj = response.to_json_object()

        # Convert to BIO format
        bio_data = convert_to_bio(request.body.text, response_obj["named_entities"])

        # Write to file
        with open("./train.txt", "a", encoding="utf-8") as file:
            file.write(bio_data)


def convert_to_bio(text, entities):
    """
    Convert the given entities to BIO format for the given text.

    Args:
        text (str): The original text.
        entities (list): A list of dictionaries representing entities with 'offset', 'len', and 'tag' fields.

    Returns:
        str: The BIO format representation of the text and entities.
    """
    bio_annotations = ['O'] * len(text)
    mytag = {}
    mytag["t"] = "DATE"
    mytag["nr"] = "PER"
    mytag["ns"] = "LOC"
    mytag["nt"] = "ORG"
    for entity in entities:
        start = entity['offset']
        end = start + entity['len']
        bio_annotations[start] = 'B-' + mytag[entity['tag']]
        for i in range(start + 1, end):
            bio_annotations[i] = 'I-' + mytag[entity['tag']]
    result = ''
    for char, bio_tag in zip(text, bio_annotations):
        if char != ' ':
            result += char + ' ' + bio_tag + '\n'
        else:
            result += '\n'
    result += '\n'  # Add an empty line after each sentence
    return result


if __name__ == "__main__":
    ak = "NQEAOKVDVI1QOU6WKFFK"
    sk = "AJlBxhobGRfYcZoJXbnsqQvliysyjslB9WCqhrUs"

    credentials = BasicCredentials(ak, sk)

    client = NlpClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(NlpRegion.value_of("cn-north-4")) \
        .build()

    try:
        file_path = "./origin.txt"
        sentences_list = read_sentences(file_path)

        # Test print the sentences_list
        for i, sentence in enumerate(sentences_list, 1):
            print(f"Sentence {i}: {sentence}\n")
            req_and_write(sentence)
            print(f"Data has been written. Sentence {i}.\n")
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
