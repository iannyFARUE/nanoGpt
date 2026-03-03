from utils.data_loader import get_verdict
from research.tokenizer import edith_warton_vocabulary, SimpleTokenizerV1
import tiktoken

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
    text1 = "Hello, do you like tea?"
    text2 = "In the sunlit terraces of the palace."
    text = " <|endoftext|> ".join((text1, text2))
    print(tokenizer.decode(tokenizer.encode(text)))


def main2():
    tokenizer = tiktoken.get_encoding("gpt2")
    text = (
        "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
        "of someunknownPlace."
    )
    integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
    print(integers)

    strings = tokenizer.decode(integers)
    print(strings)
if __name__ == "__main__":
    main2()