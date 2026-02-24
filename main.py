from utils.data_loader import get_verdict
from research.tokenizer import edith_warton_vocabulary

def main():
    print("Booting up the application...")
    vocabulary = edith_warton_vocabulary()
    for idx, item in enumerate(vocabulary.items()):
        if idx > 20:
            break
        print(item)


if __name__ == "__main__":
    main()