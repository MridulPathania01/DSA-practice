package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
)

var INF = big.NewInt(1e18)

func calculateAngriness(q []int64, n, k, cutoff int64) (*big.Int, *big.Int) {
	waiting := big.NewInt(0)
	flow := int64(0)

	for i := int64(0); i < n; i++ {
		excess := int64(0)
		need := int64(0)
		limit := cutoff + k

		if limit > 0 {
			if q[i] < limit {
				excess = q[i]
			} else {
				excess = limit
			}
		}

		if cutoff > q[i] {
			need = cutoff - q[i]
		}

		if excess > 0 {
			baseWait := big.NewInt(excess * (1 - k))
			triangle := big.NewInt((excess - 1) * excess / 2)
			waiting.Add(waiting, baseWait)
			waiting.Add(waiting, triangle)
		}

		if need > 0 {
			start := q[i] + 1
			end := q[i] + need

			startBig := big.NewInt(start)
			endBig := big.NewInt(end)

			sumEnd := new(big.Int).Mul(endBig, new(big.Int).Add(endBig, big.NewInt(1)))
			sumEnd.Div(sumEnd, big.NewInt(2))

			sumStart := new(big.Int).Mul(big.NewInt(start-1), startBig)
			sumStart.Div(sumStart, big.NewInt(2))

			diffWait := new(big.Int).Sub(sumEnd, sumStart)
			waiting.Add(waiting, diffWait)
		}

		flow += excess + need
	}

	return big.NewInt(flow), waiting
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	nextInt := func() int64 {
		s := ""
		for {
			b, err := reader.ReadByte()
			if err != nil {
				break
			}
			if b >= '0' && b <= '9' || b == '-' {
				s += string(b)
			} else if s != "" {
				break
			}
		}
		val, _ := strconv.ParseInt(s, 10, 64)
		return val
	}

	t := nextInt()
	for ; t > 0; t-- {
		n := nextInt()
		k := nextInt()

		q := make([]int64, n)
		totalCars := int64(0)
		maxQ := int64(0)

		for i := int64(0); i < n; i++ {
			q[i] = nextInt()
			totalCars += q[i]
			if q[i] > maxQ {
				maxQ = q[i]
			}
		}

		fixedCost := big.NewInt(0)
		for i := int64(0); i < n; i++ {
			tmp := big.NewInt(q[i] * k)
			fixedCost.Add(fixedCost, tmp)
		}

		lo := int64(0)
		hi := maxQ + totalCars/int64(n) + k + 10
		var optimal int64

		for lo < hi {
			mid := (lo + hi) / 2
			flow, _ := calculateAngriness(q, n, k, mid)
			if flow.Cmp(big.NewInt(totalCars)) >= 0 {
				hi = mid
			} else {
				lo = mid + 1
			}
		}

		optimal = lo
		flowPrev, waitPrev := calculateAngriness(q, n, k, optimal-1)
		pastCars := flowPrev.Int64()
		pastWait := waitPrev

		residual := totalCars - pastCars
		futureWait := big.NewInt(residual * optimal)
		futureWait.Add(futureWait, pastWait)

		final := big.NewInt(0).Add(fixedCost, futureWait)
		fmt.Println(final.String())
	}
}
