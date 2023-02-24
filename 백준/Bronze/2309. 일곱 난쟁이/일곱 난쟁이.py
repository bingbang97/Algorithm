dwarf_list = [int(input()) for _ in range(9)]
dwarf_list.sort()
dwarf_sum = sum(dwarf_list)

for i in range(9):
    for j in range(i+1, 9):
        if dwarf_sum - dwarf_list[i] - dwarf_list[j] == 100:
            a = dwarf_list[i]
            b = dwarf_list[j]

dwarf_list.remove(a)
dwarf_list.remove(b)

for i in range(7):
    print(dwarf_list[i])