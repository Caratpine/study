package main

import "fmt"

type Vertex4 struct {
	Lat, Long float64
}

var m map[string]Vertex4

func main() {
	m = make(map[string]Vertex4)
	m["Bell Labs"] = Vertex4{
		Lat:  40.11,
		Long: -1.2,
	}
	fmt.Println(m["Bell Labs"])
}