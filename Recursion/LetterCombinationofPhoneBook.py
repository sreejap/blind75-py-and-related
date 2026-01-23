def letter_combinations_of_phone_number(digits: str) -> list[str]:
    if not digits:
        return []
        
    res = []
    mapping = {
               "2":["a","b","c"],
               "3": ["d","e","f"],
               "4": ["g","h","i"],
               "5": ["j","k","l"],
               "6": ["m","n","o"],
               "7": ["p","q","r","s"],
               "8": ["t","u","v"],
               "9": ["w","x","y","z"]
              }
    def helper (idx,path):
        if idx == len(digits):
            res.append(''.join(path))
            return

        for c in mapping[digits[idx]]:
            path.append(c)
            helper (idx+1,path)
            path.pop()    
    
    helper (0,[])
    return res

if __name__ == "__main__":
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(" ".join(res))
