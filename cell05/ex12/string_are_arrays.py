import sys
def string_are_arrays(text):
    if len(sys.argv) != 2:
        print("none")
        return
    count = text.count('z')
    if count == 0:
        print("none")
    else:
        for _ in range(count):
            print("z")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text = sys.argv[1]
        string_are_arrays(text)
    else:
        string_are_arrays("")