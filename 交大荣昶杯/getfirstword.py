def process_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as input_f, open(output_file, "w", encoding="utf-8") as output_f:
        previous_line_empty = False

        for line in input_f:
            line = line.strip()

            if line:
                output_f.write(line[0])
                previous_line_empty = False
            else:
                if not previous_line_empty:
                    output_f.write("\n")
                    previous_line_empty = True

            if line == "。":
                if not previous_line_empty:
                    output_f.write("\n")
                    previous_line_empty = True

        # Add a newline at the end if the last line is not empty
        if not previous_line_empty:
            output_f.write("\n")

input_file_path = r"D:\lxh2\控江\交大荣昶杯\train.txt"
output_file_path = "./交大荣昶杯/output.txt"
process_file(input_file_path, output_file_path)
