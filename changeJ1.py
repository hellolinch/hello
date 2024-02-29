def process_txt_file(input_file_path):
    output_file_path = input_file_path.replace('.txt', '_modified.txt')

    with open(input_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file_path, 'w', encoding='utf-8') as outfile:

        previous_line = None
        for line in infile:
            line = line.strip()

            if line and line[0].isdigit():
                # If the line starts with a digit, modify the previous line
                if previous_line is not None:
                    index_of_comma = previous_line.find(',')
                    if index_of_comma != -1:
                        modified_text = "J1" + previous_line[index_of_comma:]
                        previous_line = modified_text

            if previous_line is not None:
                outfile.write(previous_line + '\n')
            previous_line = line

        # Write the last line
        if previous_line is not None:
            outfile.write(previous_line)

# 示例用法
if __name__ == '__main__':
    input_file_path = input('Please input the filepath of the txt file:')
    output_file_path = process_txt_file(input_file_path)
    print(f"Modified file saved")
