ans = 0
with open('day1.txt', 'r') as file:
    for lines in file:
        l1 = []
        lines.split("\n")
        for character in lines:
            if character.isdigit():
                l1.append(character)
        score = int(l1[0] + l1[-1])
        ans += score
print(ans)
