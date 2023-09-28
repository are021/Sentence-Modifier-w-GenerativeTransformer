from datasets import load_dataset
from transformers import AutoTokenizer

dataset = load_dataset("embedding-data/sentence-compression")
dataset["train"][100]

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
