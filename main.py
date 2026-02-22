from utils.data_loader import get_verdict
def main():
    print("Booting up the application...")
    test()

def test():
    with open("data/the-verdict.txt", "r") as f:
        content = f.read()
    print("Total characters in the verdict:", len(content))
    print("First 100 characters of the verdict:", content[:100])
if __name__ == "__main__":
    main()