def permutations(letters: str) -> list[str]:
    res = []
    path = []
    is_available = [False]*len(letters)

    def dfs (start_idx):
        if start_idx == len(letters):
            res.append("".join(path))

        for i,l in enumerate (letters):
            if is_available [i]:
                continue 
            path.append(l)
            is_available [i] = True 
            dfs (start_idx+1)
            path.pop()
            is_available [i] = False
    dfs (0)
    return res
