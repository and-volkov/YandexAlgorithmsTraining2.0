data = list(map(int, input().split()))
gap = 0

for i in range(len(data)):
    if data[i] == 1:
        i_f, i_b = i+1, i-1
        b_gap, f_gap = 0, 0
        while i_b >= 0:
            if data[i_b] == 2:
                b_gap = (i - i_b)
                break
            else:
                i_b -= 1
        while i_f <= len(data) - 1:
            if data[i_f] == 2:
                f_gap = (i_f - i)
                break
            else:
                i_f += 1

        if b_gap != 0 and f_gap != 0:
            new_gap = min(b_gap, f_gap)
        elif b_gap == 0:
            new_gap = f_gap
        else:
            new_gap = b_gap

        if new_gap > gap:
            gap = new_gap

print(gap)




