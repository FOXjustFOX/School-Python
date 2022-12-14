# with open('test.txt', 'r') as f:
#
#     il_m_a, il_m_b = map(int, f.readline().split(" "))
#
#     m_a = list(map(int, f.readline().split(" ")))
#     for i in range(1, len(m_a)):
#         # print(i)
#         m_a[i] = m_a[i-1] + m_a[i]
#
#     m_b = list(map(int, f.readline().split(" ")))
#     for i in range(1, len(m_b)):
#         # print(i)
#         m_b[i] = m_b[i-1] + m_b[i]
#
#     # n = int(input())
#     n = int(f.readline())
#
#     for i in range(n):
#         d, m, c = (f.readline().split(" "))
#
#         # d, m, c = input().split(" ")
#
#         d = int(d)
#         m = int(m)
#
#         if c == "A":
#             d = m_a[m-1] + d
#
#             if d > m_a[-1]:
#                 d -= m_a[-1]
#         #
#         #     for j in range(1, len(m_b)):
#         #         if m_b[j] >= d:
#         #             print(j-1, d - m_b[j-1], '\n')
#         #             break
#         #
#         elif c == "B":
#             d = m_b[m-1] + d
#
#             if d > m_b[-1]:
#                 d -= m_b[-1]
#         #
#         #     for j in range(1, len(m_a)):
#         #         if m_a[j] >= d:
#         #             print(j-1, d - m_a[j-1],'\n')
#         #             break
#
#         print(d, c)

# print(m_a)
# print(m_b)








arbuzan, bananit = map(int, input().split())

arbuzandni = list(map(int, input().split()))

bananitdni = list(map(int, input().split()))

arbuzandni.insert(0, 0)
bananitdni.insert(0, 0)

for j in range(1, arbuzan + 1):
    arbuzandni[j] = arbuzandni[j - 1] + arbuzandni[j]
for k in range(1, bananit + 1):
    bananitdni[k] = bananitdni[k - 1] + bananitdni[k]

for i in range(int(input())):
    dzien, miesiac, kalendarz = list(input().split())
    if kalendarz == "A":

        dni = int(dzien) + arbuzandni[int(miesiac) - 1]

        for h in range(bananit + 1):
            if dni <= bananitdni[h]:
                print(abs(bananitdni[h - 1] - dni), h)
                break
    else:

        dni = int(dzien) + bananitdni[int(miesiac) - 1]

        for h in range(arbuzan + 1):
            if dni <= arbuzandni[h]:
                print(abs(arbuzandni[h - 1] - dni), h)
                break
