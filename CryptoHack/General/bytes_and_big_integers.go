package main

import (
	"fmt"
	"math/big"
)

func main() {
	Nstr := "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
	N, _ := new(big.Int).SetString(Nstr, 10)
	fmt.Println(string(N.Bytes()))
}


// This script converts a large number, represented as a string, into a big integer using the math/big package. It then converts the integer to its byte representation and prints the corresponding string.