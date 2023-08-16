import re


def split_file(input_file_path, output_1_path, output_2_path):
    # Open the input file and read its content
    with open(input_file_path, 'r') as file:
        sections = file.read().split("================================================")

    # Split sections into the two formats

    sections_1 = []
    sections_2 = []

    for section in sections:
        parts = section.split("--------------------------------------------------")
        lines =[]
        if len(parts) <= 1:
            continue

        for line in parts[1].strip().split('\n'):
            lines.append(line)
            if "The Fair size is:" in line:
                par_section=""
                par_section = par_section+parts[0]+"--------------------------------------------------"+'\n'\
                              +lines[0]+'\n'+lines[1]+'\n'\
                              +lines[2]+'\n'+lines[3]+'\n'

                sections_1.append(par_section)
            elif "The Jumping result is:" in line:
                par_section=""
                par_section = par_section+parts[0]+"--------------------------------------------------"+'\n'\
                              +lines[4]+'\n'+lines[5]+'\n' \
                              +lines[6]+'\n'+lines[7]+'\n'

                sections_2.append(par_section)

    # Write the sections to their respective files
    with open(output_1_path, 'w') as file1, open(output_2_path, 'w') as file2:
        for section in sections_1:
            file1.write(section + "================================================\n")
        for section in sections_2:
            file2.write(section + "================================================\n")


def count_size(input_file_path):
    # Open the input file and read its content
    with open(input_file_path, 'r') as file:
        sections = file.read().split("================================================")

    allNumResults = []
    countTrue = 0
    for section in sections:
        parts = section.split("--------------------------------------------------")
        lines =[]
        if len(parts) <= 1:
            continue

        for line in parts[1].strip().split('\n'):
            lines.append(line)
            if "The Fair size is:" in line:
                # Find all integer numbers in the string
                numbers = re.findall(r'\d+', line)
                # Assuming there's only one number in the string, take the first one
                number = int(numbers[0]) if numbers else None
                allNumResults.append(number)

            elif "The Jumping result is:" in line:
                jumping_result = line.split(':')[-1].strip().lower() == 'true'
                if jumping_result:
                    countTrue = countTrue+1

    if len(allNumResults) > 0:
        return (sum(allNumResults)/len(allNumResults))
    else:
        return countTrue/200 * 100





import numpy as np

def split_sections(input_file_path, file_head):
    for i in range(200, 400, 100):
        for j in np.arange(1.3, 2.5, 0.2):
            i_str = str(i)
            j_str = "{:.1f}".format(j)
            name = i_str+"_"+j_str
            output_1_path = file_head + name + ".txt"
            with open(output_1_path, 'w') as file1:
                file1.write("")

    # Open the input file and read its content
    with open(input_file_path, 'r') as file:
        sections = file.read().split("================================================")

    for section in sections:
        name = ""
        for i in range(200, 400, 100):
            for j in np.arange(1.3, 2.5, 0.2):
                i_str = str(i)
                j_str = "{:.1f}".format(j)
                name = i_str+"_"+j_str

                if name in section:
                    output_1_path = file_head + name + ".txt"
                    with open(output_1_path, 'a') as file1:
                        file1.write(section + "================================================\n")


def read_all_fair(choice):
    if choice == "fair":
        for i in range(200, 600, 100):
            for j in np.arange(1.3, 2.5, 0.2):
                i_str = str(i)
                j_str = "{:.1f}".format(j)
                name = i_str+"_"+j_str
                read_path = "./Fair_la=10/" + name + ".txt"

                size = count_size(read_path)
                size_str = "{:.2f}".format(size)
                print("The Fair of "+name+": " + size_str)

                # sortData(read_path)

    elif choice=="jumping":
        for i in range(200, 600, 100):
            for j in np.arange(1.3, 2.5, 0.2):
                i_str = str(i)
                j_str = "{:.1f}".format(j)
                name = i_str+"_"+j_str
                read_path = "./Jumping_la=10/" + name + ".txt"

                size = count_size(read_path)
                size_str = "{:.2f}".format(size)
                print("The Jumping of "+name+": " + size_str+ " %")

                # sortData(read_path)


def filter_to_confidence_interval(numbers, lower_percentile, higher_percentile):
    # calculate 5th and 95th percentile to create 90% confidence interval
    lower_bound = np.percentile(numbers, lower_percentile)
    upper_bound = np.percentile(numbers, higher_percentile)

    # filter list to only numbers within the confidence interval
    filtered_numbers = [num for num in numbers if lower_bound <= num <= upper_bound]
    outside_interval = [num for num in numbers if num not in filtered_numbers]

    return filtered_numbers, outside_interval

def sortData(file_to_read):
    # Initialize empty lists
    sequential_times = []
    parallel_times = []

    lower_percentile = 5
    higher_percentile = 95

    with open(file_to_read, 'r') as file:
        lines = file.readlines()

    # Regular expressions to match the lines with times
    sequential_re = re.compile(r'Time used\(ms\) for Original Version: (\d+) ms.')
    parallel_re = re.compile(r'Time used\(ms\) for Parallel Version: (\d+) ms.')

    # Loop through lines
    for line in lines:
        # If the line matches the regular expression for sequential time, add the time to the list
        match_sequential = sequential_re.search(line)
        if match_sequential:
            sequential_times.append(int(match_sequential.group(1)))

        # If the line matches the regular expression for parallel time, add the time to the list
        match_parallel = parallel_re.search(line)
        if match_parallel:
            parallel_times.append(int(match_parallel.group(1)))

    filtered_sequential_times, outside_sequential_times = filter_to_confidence_interval(sequential_times, lower_percentile, higher_percentile)
    filtered_parallel_times, outside_parallel_times = filter_to_confidence_interval(parallel_times, lower_percentile, higher_percentile)
    # print the average times:
    time1 = sum(sequential_times)/len(sequential_times)
    time2 = sum(parallel_times)/len(parallel_times)
    print("Sequential times:", time1)
    print("Parallel times:", time2)
    print("enhanced: ", (time1-time2)*100/time1, "%")
    print()

    # After filtered
    time3 = sum(filtered_sequential_times)/len(sequential_times)
    time4 = sum(filtered_parallel_times)/len(parallel_times)
    print("90% of data for Sequential times:", time3)
    print("90% of data for Parallel times:", time4)
    print("enhanced: ", (time3-time4)*100/time3, "%")
    print("****************************************************")

if __name__ == "__main__":
    # This is to split the file into two files: Jumping and Fair
    # input_file = "All_200_300_whole_la=10.txt"
    # output_file_1 = "./fairOutput.txt"
    # output_file_2 = "./jumpingOutput.txt"
    # split_file(input_file, output_file_1, output_file_2)

    # This is to split the file into different folders like "./Fair/la/400_1.3.txt"
    # split_sections("./fairOutput.txt", "./Fair_la=10/")
    # split_sections("./jumpingOutput.txt", "./Jumping_la=10/")

    # read all files with different settings and count the size
    print("The size for Fair:")
    read_all_fair("fair")

    print("============================================")
    print("The size for Jumping:")
    read_all_fair("jumping")







