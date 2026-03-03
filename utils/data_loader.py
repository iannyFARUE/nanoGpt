import os
import torch
from torch.utils.data import Dataset, DataLoader
import tiktoken


def  get_verdict():
    if not os.path.exists("data/the-verdict.txt"):
        import urllib.request
        url = ("https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt")
        file_path = "data/the-verdict.txt"
        urllib.request.urlretrieve(url, file_path)
    else:
        print("The verdict file already exists. No need to download.")

def load_verdict():
    with open("data/the-verdict.txt", "r") as f:
        content = f.read()
    return content

class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []
        token_ids = tokenizer.encode(txt)

        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1: i + max_length + 1]
            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]


def create_dataloader_v1(txt, batch_size=4, max_length=256,
                         stride=128, shuffle=True, drop_last=True,
                         num_workers=0):
    tokenizer = tiktoken.get_encoding("gpt2")
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,
    num_workers=num_workers

    )
    return dataloader

def main():
    DATA_PATH = os.path.join(os.path.dirname(__file__), "..","data", "the-verdict.txt")

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        raw_text = f.read()
    dataloader = create_dataloader_v1(
        raw_text, batch_size=8, max_length=8, stride=1, shuffle=False)
    data_iter = iter(dataloader)
    first_batch = next(data_iter)
    print(first_batch)
    # second_batch = next(data_iter)
    # print(second_batch)

if __name__ == "__main__":
    main()

