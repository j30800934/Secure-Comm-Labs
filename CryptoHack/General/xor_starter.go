package main

import "fmt"

func main() {
	s := []byte("label")
	a := 13
	for i := range s {
		s[i] ^= byte(a)
	}
	fmt.Printf("crypto{%s}\n", s)
}

// This Go script performs a bitwise XOR operation on each byte of the string `"label"`, using the integer `13` as the key. The XOR operation is applied to each character in the string, modifying the bytes. After the operation, it prints the result in the format `crypto{modified_string}`, where the modified string is the result of the XOR operation.