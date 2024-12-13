s = "label"
for i in s:
    print(chr(ord(i)^13),end="")

# crypto{aloha}
# This Python script iterates through each character of the string `"label"`, applies a bitwise XOR with the number `13` to the ASCII value of each character, and then prints the resulting character. The output is `crypto{aloha}`, as the XOR operation on each character transforms `"label"` into `"aloha"`.