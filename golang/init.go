package main

import "fmt"

var X int64 = a()

func init() {
	fmt.Println("init in main.go")
}

func a() int64 {
	fmt.Println("calling a()")
	return 3
}

func main() {
	fmt.Println("calling main")
}