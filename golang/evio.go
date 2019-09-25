package main

import "github.com/tidwall/evio"

func main() {
	var events evio.Events
	events.Data = func(c evio.Conn, in []byte) (out []byte, action evio.Action) {
		out = in
		return
	}
	err := evio.Serve(events, "tcp://localhost:5000")
	if err != nil {
		panic(err.Error())
	}
}