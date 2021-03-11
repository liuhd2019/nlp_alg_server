from transformers import *
import torch

base_model = BertModel
base_tokenizer = BertTokenizer

device = torch.device("cuda")

#model_name = "bert-base-uncased"
model_name = "bert-base-multilingual-cased"
model = base_model.from_pretrained(model_name)

text = "Tokenizes the text input."
tokenizer = base_tokenizer.from_pretrained(model_name)

model.eval()

tokenized_text = tokenizer.tokenize(text)
print(tokenized_text)

indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
print(indexed_tokens)
