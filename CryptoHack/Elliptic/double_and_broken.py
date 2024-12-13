from Crypto.Util.number import *

data = [[101, 121, 115, 117, 110, 181, 211, 96, 196, 139, 116, 107, 191, 163, 142, 105, 198, 189, 76, 82, 111, 108, 109, 106, 100, 135, 123, 109, 191, 159, 114, 109, 111, 170, 67, 94, 170, 156, 150, 99, 103, 77, 163, 116, 152, 187, 212, 135, 129, 161, 123, 91, 109, 109, 165, 84, 170, 206, 175, ... ]]

for k in range(1,200):
    osc = []
    for i in range(len(data[0])):
        osc.append([0,0])
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]>k:
                osc[j][1]+=1
            else:
                osc[j][0]+=1
    flag = ""
    for i in range(len(data[0])):
        if osc[i][1]>osc[i][0]:
            flag = "1" + flag 
        else:
            flag = "0" + flag 
    flag = long_to_bytes(int(flag,2))
    if b'crypto' in flag:
        print(flag)
        break
    
# crypto{Sid3_ch4nn3ls_c4n_br34k_s3cur3_curv3s}


# This Python script processes the provided data by analyzing how many elements in each position are greater than a given threshold, iterating over values from 1 to 200. For each threshold \( k \), the script counts how many values in each column of the `data` list are greater than \( k \) and forms a binary flag based on whether the count of larger values in each position is higher or not. The resulting binary string is then converted to bytes, and the flag is checked to see if it contains the substring `crypto`.

# Once the flag containing `crypto` is found, it is printed. In this case, the result is the flag:

