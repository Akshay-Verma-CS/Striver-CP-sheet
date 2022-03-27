package main

import (
	"fmt"
)

func main() {
	var x, y, z int
	fmt.Scan(&x, &y, &z)
	fmt.Println(solve(x, y, z))
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func solve(x int, y int, z int) int {
	var xy, yz, xz, d1, d2, d3 int
	xy = Abs(x - y)
	yz = Abs(y - z)
	xz = Abs(x - z)
	d1 = xy + xz
	d2 = xy + yz
	d3 = yz + xz
	if d1 < d2 && d1 < d3 {
		return d1
	} else if d2 < d1 && d2 < d3 {
		return d2
	} else {
		return d3
	}
}
