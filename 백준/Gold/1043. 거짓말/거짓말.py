n, m = map(int, input().split())
truth_members = set(input().split()[1:])

party_members = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for members in party_members:
        if members & truth_members:
            truth_members = truth_members.union(members)

count = 0
for members in party_members:
    if members & truth_members:
        continue
    count += 1

print(count)
