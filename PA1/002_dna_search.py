def mismatch_count(s1, s2):
    mismatch = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatch += 1

    return mismatch

def find_approximate_matches(dna, sub, k):
    
    result = []
    sub_len = len(sub) # 3

    for i in range(len(dna) - sub_len + 1):
        tmp = dna[i:i + sub_len]

        if mismatch_count(tmp, sub) <= k:
            result.append(i)

    return result

def main():
    dna = input()
    sub = input()
    k = int(input())
    indices = find_approximate_matches(dna, sub, k)
    print(indices)

if __name__ == "__main__":
    main()