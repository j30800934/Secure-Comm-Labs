package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

func main() {
	hexstr := "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
	bytes, _ := hex.DecodeString(hexstr)
	fmt.Println(base64.RawStdEncoding.EncodeToString(bytes))
}


// This Go program takes a hexadecimal string, decodes it into bytes, and then encodes the result into a base64 string (using raw base64 encoding). The output is a base64-encoded string without padding (=).000000#