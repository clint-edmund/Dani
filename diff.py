def compare_text(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            
            # Check if both files have reached EOF
            if not line1 and not line2:
                return "Yes"  # Files are the same
            
            # Check if lines are different
            if line1 != line2:
                return "No\n" + f"File 1: {line1.strip()}\nFile 2: {line2.strip()}"
            
if __name__ == "__main__":
    file1 = input("Enter the name of the first text file: ")
    file2 = input("Enter the name of the second text file: ")
    
    result = compare_text(file1, file2)
    print(result)
