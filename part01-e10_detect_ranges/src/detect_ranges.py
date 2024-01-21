#!/usr/bin/env python3

def detect_ranges(L):
    Lc = L.copy()
    Lc.sort()
    result = []
    start = Lc[0]
    end = Lc[0]
    for i in range(1, len(Lc)):
        if Lc[i] == end + 1:
            end = Lc[i]
        else:
            if start == end:
                result.append(start)
            else:
                result.append((start, end+1))
            start = Lc[i]
            end = Lc[i]
    if start == end:
        result.append(start)
    else:
        result.append((start, end+1))
    return result
    

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
