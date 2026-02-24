def tokenizerV1():
    import re
    text = "Hello, world! This is a test. Let's see how it works."
    result = re.split(r'(\s)', text)
    print(result)

def tokenizerV2():
    import re
    text = "Hello, world! This is a test. Let's see how it works."
    result = re.split(r'([,.]|\s)', text)
    result = [token for token in result if token.strip() != '']
    print(result)


def tokenizerV3():
    import re
    text = "Hello, world! This-- is a test. Let's see how it works."
    result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    result = [token for token in result if token.strip() != '']
    print(result)


def tokenizerV4():
    import re
    text = "Hello, world! This-- is a test. Let's see how it works."
    result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    result = [token for token in result if token.strip() != '']
    print(result)
    
if __name__ == "__main__":
    tokenizerV3()



