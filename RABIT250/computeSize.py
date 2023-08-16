import re

def compute_average_final_set_size(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Use regex to match all occurrences of the folder paths
    folder_matches = re.findall(r'./Datasets/([\d._]+)/\d+.a.ba', content)
    unique_folders = list(set(folder_matches))

    print(unique_folders)

    folder_avg_sizes = {}

    for folder in unique_folders:
        sizes = re.findall(rf'./Datasets/{folder}/\d+.a.ba.*?The final set size is: (\d+)', content, re.DOTALL)
        sizes = [int(size) for size in sizes]
        print(sizes)
        avg_size = sum(sizes) / len(sizes) if sizes else 0
        folder_avg_sizes[folder] = avg_size

    return folder_avg_sizes

filename = './results/output.txt'
avg_sizes = compute_average_final_set_size(filename)

for folder, avg_size in avg_sizes.items():
    print(f"Average final set size for folder {folder}: {avg_size:.2f}")

