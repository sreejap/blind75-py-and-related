def find_all_anagrams(original: str, check: str) -> list[int]:
    original_len = len(original)
    check_len = len (check)
    if original_len < check_len:
        return []
        
    check_count = [0] * 26
    window_count = [0] * 26
    res = []
    a = ord("a") # this has to be in quotes...interesting
    for i in range (check_len):
        check_count [ord(original[i]) - a] += 1
        window_count [ord(original[i]) -a] += 1

    if check_count == window_count:
        res.append(0)

    for right in range (check_len, original_len):
        left = right - check_len
        window_count [ord(original[right - check_len]) - a] -= 1
        window_count [ord(original[right]) -a ] += 1
        if window_count == check_count:
            res.append (right - check_len+1)
    return res

if __name__ == "__main__":
    original = input()
    check = input()
    res = find_all_anagrams(original, check)
    print(" ".join(map(str, res)))
