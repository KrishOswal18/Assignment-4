text1 = input("Enter text to write to the file: ")

with open("output.txt", "wt") as fh:
    content1 = fh.write(text1)
    print("Data successfully written to output.txt")

text2 = input("Enter additional text to append: ")

with open("output.txt", "at") as fh:
    content2 = fh.write(f"\n{text2}")
    print("Data successfully appended")

with open("output.txt", "rt") as fh:
    final = fh.read()
    print(f"Final content of output.txt:\n {final}")

