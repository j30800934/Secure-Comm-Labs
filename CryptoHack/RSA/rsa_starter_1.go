package main

import (
	"fmt"
	"math/big"
)

func main() {
	a := new(big.Int).SetInt64(101)
	b := new(big.Int).SetInt64(17)
	n := new(big.Int).SetUint64(22663)

	fmt.Println(new(big.Int).Exp(a, b, n))
}


// The Go code computes the result of a^b mod n, where a = 101, b = 17, and n = 22663. It uses the `math/big` package to handle large integers and modular exponentiation efficiently. The result is printed as the output of the operation 101^17 mod 22663.