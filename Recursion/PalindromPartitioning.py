def partition(s: str) -> list[list[str]]:
    res = []
    n = len(s)
    def is_palindrome(word):
        return word == word [::-1]

    def dfs (start,curr_path):
        if start == n:
            res.append(curr_path[:])
            return

        for end in range (start+1, n+1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                dfs(end,curr_path+[prefix]) 
                # we are creating a new list when we do curr_path+[prefix]
                # so no need to undo or backtrack explicitly as in other examples
                
    dfs(0,[])
    return res

if __name__ == "__main__":
    s = input()
    res = partition(s)
    for row in res:
        print(" ".join(row))
