package main

import (
	"fmt"
	"time"
)

type Channel1 struct {
	c chan string
}

type Channel2 struct {
	c chan string
}

func main() {
	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()
	ch1 := &Channel1{c:make(chan string)}
	ch2 := &Channel2{c:ch1.c}

	go func() {
		for {
			time.Sleep(2 * time.Second)
			ch1.c <- "hello"
		}
	}()

	for {
		select {
		case s := <- ch2.c:
			fmt.Println(s)
		}
	}
}
