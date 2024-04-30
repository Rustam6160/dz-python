l = [4, 3, 7, -5, 9,-7, -4, 0, 2]
p_l = sorted(l)

print(p_l)

c = -4


while True:

    mid = len(p_l) // 2
    # if (len(p_l)+1) % 2 < 0:
    #     mid += 1
    if c >= p_l[mid]:
        del p_l[:mid]
        print(p_l)
        if len(p_l) == 1:
            break
    elif c <= p_l[mid]:
        del p_l[mid:]
        print(p_l)
        if len(p_l) == 1:
            break







