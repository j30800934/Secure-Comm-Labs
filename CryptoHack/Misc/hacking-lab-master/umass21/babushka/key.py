#!/usr/bin/env python3

s = [0]*128
s[:5] = 'UMASS'
s[5] = 123
s[6] = 112|4
s[7] = 96|8
s[8] = 51
s[9] = 80|15
s[10] = ((1<<6)&64)|((1<<5)&32)|((1<<4)&16)|((1<<1)&2)|((1<<0)&1)
s[11] = ((1<<6)&64)|((1<<5)&32)|((1<<4)&16)
s[12] = ((1<<6)&64)|((1<<5)&32)|((1<<3)&8)|((1<<0)&1)
s[13] = ((1<<5)&32)|((1<<4)&16)|((1<<0)&1)
s[14] = 49
s[15] = ((1<<6)&64)|((1<<5)&32)|((1<<0)&1)
s[16] = ((1<<6)&64)|((1<<5)&32)|((1<<2)&4)|((1<<1)&2)|((1<<0)&1)
s[17] = ((1<<5)&32)|((1<<4)&16)|((1<<1)&2)|((1<<0)&1)
s[18] = 80|15
s[19] = 98
s[20] = 112|9
s[21] = 116
s[22] = 48|3
s[23] = ((1<<6)&64)|((1<<5)&32)|((1<<1)&2)|((1<<0)&1)
s[24] = 48
s[25] = 100
s[26] = 51
s[27] = 95
s[28] = ((1<<6)&64)|((1<<5)&32)|((1<<1)&2)|((1<<0)&1)
s[29] = 112|4
s[30] = 96|6
s[31] = 116
s[32] = 96|9
s[33] = 109
s[34] = 51
s[35] = 95
s[36] = 104
s[37] = 97
s[38] = ((1<<6)&64)|((1<<5)&32)|((1<<1)&2)|((1<<0)&1)
s[39] = 96|11
s[40] = ((1<<6)&64)|((1<<5)&32)|((1<<4)&16)|((1<<3)&8)|((1<<2)&4)|((1<<0)&1)
print(''.join(s[:5])+''.join(map(chr, s[5:])))