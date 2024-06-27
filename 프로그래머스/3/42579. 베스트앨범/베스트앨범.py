def solution(genres, plays):
    answer = []
    hash_map = {}
    for i in range(len(genres)):
        if hash_map.get(genres[i]):
            hash_map[genres[i]][0] += plays[i]
            hash_map[genres[i]].append((i, plays[i]))
        else:
            hash_map[genres[i]] = [plays[i], (i, plays[i])]
    
    sorted_hash_map = sorted(hash_map.items(), key = lambda item: item[1][0], reverse = True)
    
    for item in sorted_hash_map:
        sorted_item = sorted(item[1][1:], key = lambda x: x[1], reverse = True)[:2]
        answer += [x[0] for x in sorted_item]
    return answer