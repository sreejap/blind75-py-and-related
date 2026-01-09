def least_consecutive_cards_to_match(cards: list[int]) -> int:
    least_consecutive_cards = len(cards) + 1
    left = 0
    right = 0
    nums_set = set()
    for right in range (len(cards)):
        num = cards[right]
        while num in nums_set:            
            least_consecutive_cards = min(least_consecutive_cards, right - left +1)
            nums_set.remove(cards[left])
            left += 1
        nums_set.add(num)
    if least_consecutive_cards > len(cards):
        return -1
    return least_consecutive_cards

if __name__ == "__main__":
    cards = [int(x) for x in input().split()]
    res = least_consecutive_cards_to_match(cards)
    print(res)
