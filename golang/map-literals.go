package main

import "fmt"

type Vertex5 struct {
	Lat, Long float64
}

var m1 = map[string]Vertex5{
	"Bell Labs": {
		Lat:  40.123,
		Long: -1231,
	},
	"Google": {
		Lat:  37.111,
		Long: -123.2,
	},
}

func main() {
	fmt.Println(m1)
}
