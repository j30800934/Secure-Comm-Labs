from modint import chinese_remainder, ChineseRemainderConstructor
ct = ChineseRemainderConstructor([5,11,17])
print(ct.rem([2,3,5]))

# 872

# The code imports chinese_remainder and ChineseRemainderConstructor from the modint module. It creates an instance ct of ChineseRemainderConstructor with moduli [5, 11, 17], then calculates the remainder for the input values [2, 3, 5], resulting in 872.