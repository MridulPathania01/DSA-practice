package main

import (
	"fmt"
)

func A() {
	var n int
	fmt.Scan(&n)
	if n%4 == 0 {
		fmt.Println("Bob")
	} else {
		fmt.Println("Alice")
	}
}
func main() {
	var t int
	fmt.Scan(&t)
	for i := 0; i < t; i++ {
		A()
	}
}
