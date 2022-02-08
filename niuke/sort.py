l = [18, 13, 16, 25, 21]

# for i in range(len(l) - 1):
#     for j in range(i, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]

for j in range(len(l) - 1):
    for i in range(len(l)-1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]

print(l)
