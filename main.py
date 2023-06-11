# def str_count(s: str): # за O(N**2)
#     for sym in set(s): # set - множество
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
# str_count('aabbccddee')



# def str_count(s: str): # за O(N*2)
#     mydct = {}
#     for sym in s:
#         mydct[sym] = mydct.get(sym, 0) + 1
#     for key in mydct:
#         print(key, mydct.get(key))
# str_count('aabbccddee')

