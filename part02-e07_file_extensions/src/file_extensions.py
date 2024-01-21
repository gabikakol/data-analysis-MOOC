def file_extensions(filename):
    filenames_without_extension = []
    extension_dict = {}

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            filename = line.strip()
            if '.' in filename:
                file_parts = filename.split('.')
                ext = file_parts[-1]
                if ext not in extension_dict:
                    extension_dict[ext] = [filename]
                else:
                    extension_dict[ext].append(filename)
            else:
                filenames_without_extension.append(filename)

    return filenames_without_extension, {key: value for key, value in sorted(extension_dict.items())}

def main():
    filenames_without_extension, extension_dict = file_extensions("src/filenames.txt")

    print(f"{len(filenames_without_extension)} {'file' if len(filenames_without_extension) == 1 else 'files'} with no extension")
    for ext, files in sorted(extension_dict.items()):
        print(f"{ext} {len(files)}")

if __name__ == "__main__":
    main()
