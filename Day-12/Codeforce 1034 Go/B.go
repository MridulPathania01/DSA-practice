package main

import (
	"fmt"
)

func B() {
	var n, j, k int
	fmt.Scan(&n, &j, &k)

	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	if k > 1 {
		fmt.Println("YES")
	} else {
		maxStrength := a[0]
		for i := 1; i < n; i++ {
			if a[i] > maxStrength {
				maxStrength = a[i]
			}
		}
		if a[j-1] == maxStrength {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}

func main() {
	var t int
	fmt.Scan(&t)
	for i := 0; i < t; i++ {
		B()
	}
}
