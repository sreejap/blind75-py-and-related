def longest_substring_without_repeating_characters(s: str) -> int:
    left = 0
    right = 0
    window = set ()
    longest_substring = 0
    for right in range (len(s)):
        r_char = s[right]
        while (r_char in window):
            l_char = s[left]            
            window.remove(l_char)
            left += 1
        window.add(s[right])
        longest_substring = max (longest_substring, right - left +1)
    return longest_substring

if __name__ == "__main__":
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)
