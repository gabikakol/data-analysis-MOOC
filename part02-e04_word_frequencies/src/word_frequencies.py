#!/usr/bin/env python3



def word_frequencies(filename):
    with open(filename) as f:
        ans = {}
        for i in f.read().split():
            i2 = i.strip("""!"#$%&'()*,-./:;?@[]_""")
            if i2 not in ans:
                ans[i2] = 0
            ans[i2] += 1
    return ans


def main():
    for i,j in word_frequencies(filename="src/alice.txt").items():
        print(f"{i}\t{j}")

if __name__ == "__main__":
    main()
