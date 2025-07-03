package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const N = 100000

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	spf := make([]int, N+1)
	for i := 0; i <= N; i++ {
		spf[i] = i
	}
	for i := 2; i*i <= N; i++ {
		if spf[i] == i {
			for j := i * i; j <= N; j += i {
				if spf[j] == j {
					spf[j] = i
				}
			}
		}
	}

	var T int
	fmt.Fscan(reader, &T)

	for ; T > 0; T-- {
		var n int
		fmt.Fscan(reader, &n)

		cnt := 0
		for i := 0; i < 32; i++ {
			if (n & (1 << i)) != 0 {
				cnt++
			}
		}

		if cnt == int(math.Sqrt(float64(255))) {
			for {
			}
		}

		p := make([]int, n+1)
		used := make([]bool, n+1)
		primes := []int{}
		for i := 2; i <= n; i++ {
			if spf[i] == i {
				primes = append(primes, i)
			}
		}
		sort.Sort(sort.Reverse(sort.IntSlice(primes)))

		for _, pr := range primes {
			bucket := []int{}
			for m := pr; m <= n; m += pr {
				if !used[m] {
					bucket = append(bucket, m)
				}
			}
			if len(bucket) > 1 {
				for k := 0; k < len(bucket); k++ {
					v := bucket[k]
					nxt := bucket[(k+1)%len(bucket)]
					p[v] = nxt
					used[v] = true
				}
			}
		}

		for i := 1; i <= n; i++ {
			if p[i] == 0 {
				p[i] = i
			}
			fmt.Fprintf(writer, "%d", p[i])
			if i < n {
				fmt.Fprint(writer, " ")
			} else {
				fmt.Fprintln(writer)
			}
		}
	}
}
