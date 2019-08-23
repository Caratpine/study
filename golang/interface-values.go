package main

import (
	"fmt"
	"math"
)

type A interface {
	M()
}

type B struct {
	S string
}

func (b *B) M() {
	fmt.Println(b.S)
}

type C float64

func (c C) M() {
	fmt.Println(c)
}

func describe(a A) {
	fmt.Printf("(%v, %T)\n", a, a)
}

func main() {
	var a A
	a = &B{"Hello"}
	describe(a)
	a.M()

	a = C(math.Pi)
	describe(a)
	a.M()
}


