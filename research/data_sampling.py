import os
import tiktoken
_TOKENIZER = tiktoken.get_encoding("gpt2")
def sampling():
    TEXT_DIR = os.path.join(os.path.dirname(__file__),"..","data","the-verdict.txt")
    with open(TEXT_DIR, encoding="utf-8") as f:
        text = f.read()

    enc_text = _TOKENIZER.encode(text)
    return enc_text

def main():
    enc_sample = sampling()[50:]
    context_size = 4
    for i in range(1, context_size+1):
        context = enc_sample[:i]
        desired = enc_sample[i]
        print(_TOKENIZER.decode(context),"------>", _TOKENIZER.decode([desired]))

if __name__ == "__main__":
    main()