package main

import (
	"fmt"
	"math/big"
)

func main() {
	p, _ := new(big.Int).SetString("857504083339712752489993810777", 10)
	q, _ := new(big.Int).SetString("1029224947942998075080348647219", 10)

	p.Sub(p, big.NewInt(1))
	q.Sub(q, big.NewInt(1))

	fmt.Println(p.Mul(p, q))
}


// The Go code subtracts 1 from two large integers, p and q , and then multiplies the resulting values. It first defines p as "857504083339712752489993810777" and q as "1029224947942998075080348647219". After subtracting 1 from each of these values, the program multiplies them and prints the result. 

// The output will be the product of (p-1) \times (q-1) .