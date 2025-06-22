package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const MAXN = 300

func varIndex(v int, pol bool) int {
	if pol {
		return 2 * v
	}
	return 2*v + 1
}

func solve2SAT() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	readLine := func() string {
		line, _ := reader.ReadString('\n')
		return strings.TrimSpace(line)
	}

	T, _ := strconv.Atoi(readLine())

	for t := 0; t < T; t++ {
		line := strings.Fields(readLine())
		n, _ := strconv.Atoi(line[0])
		k, _ := strconv.Atoi(line[1])

		N := 2 * n
		g := make([][]int, N)
		gr := make([][]int, N)

		for gi := 0; gi < k; gi++ {
			m, _ := strconv.Atoi(readLine())
			adj := make([]uint64, n)
			for i := 0; i < m; i++ {
				edge := strings.Fields(readLine())
				u, _ := strconv.Atoi(edge[0])
				v, _ := strconv.Atoi(edge[1])
				u--
				v--
				adj[u] |= 1 << v
				adj[v] |= 1 << u
			}

			for u := 0; u < n; u++ {
				for v := u + 1; v < n; v++ {
					bu := adj[u] &^ (1<<u | 1<<v)
					bv := adj[v] &^ (1<<u | 1<<v)

					if bu != bv {
						continue
					}

					has := (adj[u] & (1 << v)) != 0
					if has {
						a1 := varIndex(u, true)
						b1 := varIndex(v, false)
						g[a1] = append(g[a1], b1)
						gr[b1] = append(gr[b1], a1)

						a2 := varIndex(v, true)
						b2 := varIndex(u, false)
						g[a2] = append(g[a2], b2)
						gr[b2] = append(gr[b2], a2)
					} else {
						a1 := varIndex(u, false)
						b1 := varIndex(v, true)
						g[a1] = append(g[a1], b1)
						gr[b1] = append(gr[b1], a1)

						a2 := varIndex(v, false)
						b2 := varIndex(u, true)
						g[a2] = append(g[a2], b2)
						gr[b2] = append(gr[b2], a2)
					}
				}
			}
		}

		used := make([]bool, N)
		order := []int{}

		var dfs1 func(int)
		dfs1 = func(u int) {
			used[u] = true
			for _, v := range g[u] {
				if !used[v] {
					dfs1(v)
				}
			}
			order = append(order, u)
		}

		for i := 0; i < N; i++ {
			if !used[i] {
				dfs1(i)
			}
		}

		comp := make([]int, N)
		for i := range comp {
			comp[i] = -1
		}
		cid := 0

		var dfs2 func(int)
		dfs2 = func(u int) {
			comp[u] = cid
			for _, v := range gr[u] {
				if comp[v] == -1 {
					dfs2(v)
				}
			}
		}

		for i := N - 1; i >= 0; i-- {
			u := order[i]
			if comp[u] == -1 {
				dfs2(u)
				cid++
			}
		}

		ok := true
		for v := 0; v < n; v++ {
			if comp[varIndex(v, true)] == comp[varIndex(v, false)] {
				ok = false
				break
			}
		}

		if ok {
			fmt.Fprintln(writer, "Yes")
		} else {
			fmt.Fprintln(writer, "No")
		}
	}
}

func main() {
	solve2SAT()
}
