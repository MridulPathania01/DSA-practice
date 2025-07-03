package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var t int
	fmt.Fscan(reader, &t)

	for ; t > 0; t-- {
		var n, m, Q int
		fmt.Fscan(reader, &n, &m, &Q)

		a := make([]int, n+2)
		for i := 1; i <= n; i++ {
			fmt.Fscan(reader, &a[i])
		}

		v := []int{}
		for i := 1; i*i <= m; i++ {
			if m%i == 0 {
				v = append(v, i)
				if i != m/i {
					v = append(v, m/i)
				}
			}
		}
		sort.Ints(v)

		s := len(v)
		c := make([]int, s)

		for j := 0; j < s; j++ {
			g := v[j]
			cnt := 0
			for i := 1; i < n; i++ {
				if a[i]%g > a[i+1]%g {
					cnt++
				}
			}
			c[j] = cnt
		}

		for ; Q > 0; Q-- {
			var tp int
			fmt.Fscan(reader, &tp)
			if tp == 1 {
				var i, x int
				fmt.Fscan(reader, &i, &x)
				for j := 0; j < s; j++ {
					g := v[j]
					if i > 1 {
						o := a[i-1]%g > a[i]%g
						n2 := a[i-1]%g > x%g
						if o && !n2 {
							c[j]--
						} else if !o && n2 {
							c[j]++
						}
					}
					if i < n {
						o := a[i]%g > a[i+1]%g
						n2 := x%g > a[i+1]%g
						if o && !n2 {
							c[j]--
						} else if !o && n2 {
							c[j]++
						}
					}
				}
				a[i] = x
			} else {
				var k int
				fmt.Fscan(reader, &k)
				g := gcd(k, m)
				idx := sort.Search(len(v), func(i int) bool { return v[i] >= g })
				if idx < len(v) && v[idx] == g {
					if c[idx] <= m/g-1 {
						fmt.Fprintln(writer, "YES")
					} else {
						fmt.Fprintln(writer, "NO")
					}
				} else {
					fmt.Fprintln(writer, "NO")
				}
			}
		}
	}
}
