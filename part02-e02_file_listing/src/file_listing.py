import re

def file_listing(filename="src/listing.txt"):
    file_list = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r'^([-drwx]{10})\s+(\d+)\s+(\w+)\s+(\w+)\s+(\d+)\s+(\w{3})\s+(\d{1,2})\s+(\d{1,2}):(\d{2})\s+(.+)$', line)
            if match:
                size = int(match.group(5))
                month = match.group(6)
                day = int(match.group(7))
                hour = int(match.group(8))
                minute = int(match.group(9))
                filename = match.group(10)
                file_list.append((size, month, day, hour, minute, filename))
    return file_list

def main():
    files = file_listing()
    for file in files:
        print(file)

if __name__ == "__main__":
    main()
