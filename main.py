from utils.data_loader import get_verdict
from research.tokenizer import edith_warton_vocabulary, SimpleTokenizerV1

def main():
    vocab = edith_warton_vocabulary()
    s_tokenizer = SimpleTokenizerV1(vocab)
    text = """"It's the last he painted, you know,"
            Mrs. Gisburn said with pardonable pride."""
    ids = s_tokenizer.encode(text)
    print(ids)
    print(s_tokenizer.decode(ids))

def main1():
    vocab = edith_warton_vocabulary()
    tokenizer = SimpleTokenizerV1(vocab)
    text ="Hello, do you like monster energy"
    print(tokenizer.encode(text))


if __name__ == "__main__":
    vocab = edith_warton_vocabulary()
    print(list(vocab.items())[-5:])
    print(len(vocab))
    # main1()