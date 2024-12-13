package main

import (
	"encoding/json"
	"fmt"
	"net/textproto"
)

func main() {
	conn, _ := textproto.Dial("tcp", "socket.cryptohack.org:11112")
	defer conn.Close()

	for l := " "; len(l) > 0; {
		l, _ = conn.ReadLine()
	}

	conn.PrintfLine(`{"buy":"flag"}`)

	res_line, _ := conn.ReadLine()
	res := make(map[string]any)
	json.Unmarshal([]byte(res_line), &res)
	fmt.Println(res["flag"])
}

// This Go script connects to a remote server at `socket.cryptohack.org` on port `11112` using the `textproto` package. It continuously reads lines from the server until it receives a non-empty response. Then, it sends a JSON request with the key `"buy"` and the value `"flag"` to the server. After sending the request, the script waits for a response, which is expected to be in JSON format. It unmarshals the JSON response into a map and prints the value associated with the key `"flag"`, which is presumably the flag or relevant information from the server.