#!/usr/bin/env python3

def file_extensions(filename):
    with open(filename) as f:
        lines = f.readlines()
        extensions = []
        filenames = {}
        for line in lines:
            extensions.append(line.split(".")[-1].strip())
        for extension in extensions:
            if extension in filenames:
                filenames[extension] += 1
            else:
                filenames[extension] = 1
        return [extensions, filenames]
        

def main():
    print(file_extensions(filename="src/filenames.txt"))

if __name__ == "__main__":
    main()
