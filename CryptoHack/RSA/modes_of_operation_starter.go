package main

import (
	"encoding/hex"
	"encoding/json"
	"fmt"
	"net/http"
)

var URL string = "http://aes.cryptohack.org"

func main() {
	resp, _ := http.Get(URL + "/block_cipher_starter/encrypt_flag/")
	res := make(map[string]string)
	json.NewDecoder(resp.Body).Decode(&res)
	resp.Body.Close()

	resp, _ = http.Get(URL + "/block_cipher_starter/decrypt/" + res["ciphertext"] + "/")
	json.NewDecoder(resp.Body).Decode(&res)
	pt, _ := hex.DecodeString(res["plaintext"])
	fmt.Println(string(pt))
	resp.Body.Close()
}



// This Go program fetches a ciphertext from a remote service, decrypts it, and prints the plaintext. It first sends a GET request to retrieve the ciphertext, then sends another request to decrypt it and outputs the result.