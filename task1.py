try:
    with open("sample.txt","rt") as fh:
        
            line1 = fh.readline()
            line2 = fh.readline()

            print(f"Line 1: {line1}")
            print(f"Line 2: {line2}")
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")

     


