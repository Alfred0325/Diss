
def split_file(input_file_path, output_1_path, output_2_path):
    # Open the input file and read its content
    with open(input_file_path, 'r') as file:
        sections = file.read().split("================================================")
    
    # Split sections into the two formats
    sections_1 = []
    sections_2 = []

    for section in sections:
        if "The Jumping result is:" in section:
            sections_2.append(section)
        else:
            sections_1.append(section)
    
    # Write the sections to their respective files
    with open(output_1_path, 'w') as file1, open(output_2_path, 'w') as file2:
        for section in sections_1:
            file1.write(section + "================================================\n")
        for section in sections_2:
            file2.write(section + "================================================\n")

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file_1 = input("Enter the path for the first output file: ")
    output_file_2 = input("Enter the path for the second output file: ")
    
    split_file(input_file, output_file_1, output_file_2)
    print("Files have been successfully split.")
