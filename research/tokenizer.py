import re
from utils.data_loader import load_verdict
def tokenizerV1(text = "Hello, world! This is a test. Let's see how it works."):
    result = re.split(r'(\s)', text)
    return result

def tokenizerV2(text = "Hello, world! This is a test. Let's see how it works."):
    result = re.split(r'([,.]|\s)', text)
    result = [token for token in result if token.strip() != '']
    return result


def tokenizerV3(text = "Hello, world! This-- is a test. Let's see how it works."):
    result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    result = [token for token in result if token.strip() != '']
    return result


def tokenizerV4(text = "Hello, world! This-- is a test_==. Let's see how it works."):
    result = re.split(r'([,.:;?_!"()\'=]|--|\s)', text)
    result = [token for token in result if token.strip() != '']
    return result


def edith_warton_tokenizer():

    content = load_verdict()
    processed = tokenizerV4(content)
    return sorted(set(processed))

def edith_warton_vocabulary():
    all_tokens = edith_warton_tokenizer()
    return {token: idx for idx, token in enumerate(all_tokens)}

class SimpleTokenizerV1:

    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
        item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
    
if __name__ == "__main__":
    tokenizerV4()



