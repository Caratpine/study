package main

import "fmt"

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

type Test struct {

}

func (t *Test) Write(p []byte) (int, error){
	return 1, nil
}

func main() {
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}