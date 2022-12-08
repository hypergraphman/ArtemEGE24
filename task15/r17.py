# for a in range(1, 1000):
#     is_a = True
#     for x in range(1, 1000):
#         A = x % a == 0
#         d21 = x % 21 == 0
#         d35 = x % 35 == 0
#         if not (A <= (not d21 or d35)):
#             is_a = False
#             break
#     if is_a:
#         print(a)


for a in range(1, 1000):
    if all((x % a == 0) <= ((x % 21 != 0) or (x % 35 == 0)) for x in range(1, 1000)):
        print(a)
        break
