import os

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