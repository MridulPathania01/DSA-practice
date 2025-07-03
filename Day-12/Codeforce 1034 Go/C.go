package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var T int
	fmt.Fscanln(reader, &T)

	for t := 0; t < T; t++ {
		var n int
		fmt.Fscanln(reader, &n)

		aLine, _ := reader.ReadString('\n')
		aStr := strings.Fields(aLine)
		a := make([]int, n)
		for i := 0; i < n; i++ {
			a[i], _ = strconv.Atoi(aStr[i])
		}

		prefMin := make([]int, n)
		prefMin[0] = a[0]
		for i := 1; i < n; i++ {
			prefMin[i] = min(prefMin[i-1], a[i])
		}
		suffMax := make([]int, n)
		suffMax[n-1] = a[n-1]
		for i := n - 2; i >= 0; i-- {
			suffMax[i] = max(suffMax[i+1], a[i])
		}
		ans := make([]byte, n)
		for i := 0; i < n; i++ {
			if a[i] == prefMin[i] || a[i] == suffMax[i] {
				ans[i] = '1'
			} else {
				ans[i] = '0'
			}
		}

		fmt.Fprintln(writer, string(ans))
	}
}
