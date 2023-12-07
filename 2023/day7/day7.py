from aocd import lines, submit, get_data


test_data = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def part1():
    cardToValue = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def getHand(hand):
        # get card count for each hand
        cards = {}
        for card in hand:
            cards[card] = hand.count(card)

        card_keys = cards.keys()
        count = cards.values()
        if len(card_keys) == 5:
            return "highCard"  # 1/1/1/1/1
        elif len(card_keys) == 1:
            return "fiveOfAKind"  # 5
        elif len(card_keys) == 2:
            if 4 in count:  # 4 of a kind 4/1
                return "fourOfAKind"
            else:  # full house 3/2
                return "fullHouse"
        elif len(card_keys) == 3:
            if 3 in count:  # full house 3/1/1
                return "threeOfAKind"
            else:  # 3 of a kind 2/2/1
                return "twoPair"
        elif len(card_keys) == 4:
            return "pair"

    # data = test_data
    data = lines
    hands = {}
    handRank = {
        "highCard": [],
        "pair": [],
        "twoPair": [],
        "threeOfAKind": [],
        "fullHouse": [],
        "fourOfAKind": [],
        "fiveOfAKind": [],
    }
    for line in data:
        [hand, bid] = line.split(" ")
        hands[hand] = int(bid)
        handType = getHand(hand)
        handRank[handType].append(hand)

    rank = 1
    count = 0
    for key in handRank.keys():
        value = handRank[key]
        if len(value) > 0:
            sorted_value = sorted(
                value, key=lambda hand: [cardToValue[c] for c in hand]
            )
            for hand in sorted_value:
                count += rank * hands[hand]
                rank += 1
    print(count)
    return count


def part2():
    cardToValue = {
        "J": 2,  # ==> reordered
        "2": 3,
        "3": 4,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 8,
        "8": 9,
        "9": 10,
        "T": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def getHand(hand):
        # get card count for each hand
        cards = {}
        for card in hand:
            cards[card] = hand.count(card)

        card_keys = cards.keys()
        # pt 2 twist
        jokers_count = cards.get("J", 0)
        # add jokers count to whatever the key of max length is to augment hand
        if jokers_count > 0:
            # special case for all J
            if jokers_count == 5:
                return "fiveOfAKind"
            # remove jokers
            del cards["J"]

            max_key = list(card_keys)[0]
            for c in card_keys:
                if cards[c] > cards[max_key]:
                    max_key = c

            cards[max_key] += jokers_count

        count = cards.values()

        if len(card_keys) == 5:
            handType = "highCard"  # 1/1/1/1/1
        elif len(card_keys) == 1:
            handType = "fiveOfAKind"  # 5
        elif len(card_keys) == 2:
            if 4 in count:  # 4 of a kind 4/1
                handType = "fourOfAKind"
            else:  # full house 3/2
                handType = "fullHouse"
        elif len(card_keys) == 3:
            if 3 in count:  # full house 3/1/1
                handType = "threeOfAKind"
            else:  # 3 of a kind 2/2/1
                handType = "twoPair"
        elif len(card_keys) == 4:
            handType = "pair"

        return handType

    # data = test_data
    data = lines
    hands = {}
    handRank = {
        "highCard": [],
        "pair": [],
        "twoPair": [],
        "threeOfAKind": [],
        "fullHouse": [],
        "fourOfAKind": [],
        "fiveOfAKind": [],
    }
    for line in data:
        [hand, bid] = line.split(" ")
        hands[hand] = int(bid)
        handType = getHand(hand)
        handRank[handType].append(hand)

    rank = 1
    count = 0
    for key in handRank.keys():
        value = handRank[key]
        if len(value) > 0:
            sorted_value = sorted(
                value, key=lambda hand: [cardToValue[c] for c in hand]
            )
            for hand in sorted_value:
                count += rank * hands[hand]
                rank += 1
    print(count)
    return count


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=7, year=2023) #! CORRECT!
# submit(ans2, part="b", day=7, year=2023) #! CORRECT!
