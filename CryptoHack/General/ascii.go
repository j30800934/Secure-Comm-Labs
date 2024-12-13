package main

import "fmt"

func main() {
	l := []byte{99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125}
	fmt.Println(string(l))
}


// This Go program prints a string by converting a slice of bytes into characters. The byte slice l corresponds to the ASCII values of the characters forming the string crypto{ASCII_print1nt4bl3}