C = int(input())
like = {}
dislike = {}
ings = set()
for i in range(C):
    cl = input().split(' ')[1:]
    for ing in cl:
        ings.add(ing)
        if ing not in like:
            like[ing] = 0
        like[ing] += 1

    cd = input().split(' ')[1:]
    for ing in cd:
        ings.add(ing)
        if ing not in dislike:
            dislike[ing] = 0
        dislike[ing] += 1

result = set()
for ing in ings:
    likecount = like[ing] if ing in like else 0
    dislikecount = dislike[ing] if ing in dislike else 0
    if likecount > dislikecount:
        result.add(ing)

print(str(len(result)) + " " + " ".join(result))
