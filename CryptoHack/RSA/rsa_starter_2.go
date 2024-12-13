package main

import (
	"fmt"
	"math/big"
)

func main() {
	a := new(big.Int).SetInt64(12)
	e := new(big.Int).SetInt64(0x10001)
	n := new(big.Int).SetUint64(17 * 23)

	fmt.Println(new(big.Int).Exp(a, e, n))
}


// This  Go program calculates the result of a^e mod n, where a = 12, e = 0x10001 (which is 65537 in decimal), and n = 17 x 23 = 391. It uses the math/big package to handle large integers and efficiently perform modular exponentiation. The result is printed as the outcome of 12^65537 mod 391.