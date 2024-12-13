package main

import (
	"fmt"
	"math/big"
)

func main() {
	p := big.NewInt(991)
	g := big.NewInt(209)
	fmt.Println(g.ModInverse(g, p))
}



// This Go program calculates the modular inverse of g modulo p, where p is a large prime number (991) and g is an integer (209). The modular inverse of g is a number x such that g×x≡1 (mod p)g×x≡1 (mod p). The program uses Go's big.Int.ModInverse function to compute this inverse and prints the result. The modular inverse is important in cryptographic protocols like Diffie-Hellman key exchange.