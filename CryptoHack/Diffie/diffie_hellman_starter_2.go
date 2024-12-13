package main

import (
	"fmt"
	"math/big"
)

func main() {
	one := big.NewInt(1)
	p := big.NewInt(28151)

	for k := big.NewInt(1); k.Cmp(p) < 0; k.Add(k, one) {
		is_gen := true
		for i := big.NewInt(2); i.Cmp(p) < 0; i.Add(i, one) {
			x := new(big.Int).Exp(k, i, p)
			if x.Cmp(k) == 0 {
				is_gen = false
				break
			}
		}

		if is_gen {
			fmt.Println(k)
			break
		}
	}
}

// This Go program finds the smallest generator of a cyclic group modulo p (in this case, p is 28151). A generator g is a number where the powers of g modulo p generate all nonzero numbers modulo p. The program iterates through potential candidates k starting from 1 and checks if raising k to all powers less than p modulo p yields k itself, indicating that k is not a generator. The first value of k that satisfies the condition is printed as the generator.
