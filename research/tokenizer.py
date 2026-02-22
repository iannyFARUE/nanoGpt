def test():
    import re
    text = "Hello, world! This is a test. Let's see how it works."
    result = re.split(r'(\s)', text)
    print(result)

if __name__ == "__main__":
    test()