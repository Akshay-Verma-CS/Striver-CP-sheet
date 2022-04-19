//  	702A - Maximum Increase
package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		var element int
		fmt.Scan(&element)
		arr[i] = element
	}
	var max int = 1
	var currentMax int = 1
	for i := 1; i < n; i++ {
		if arr[i] > arr[i-1] {
			currentMax++
		} else {
			if currentMax > max {
				max = currentMax
			}
			currentMax = 1
		}
	}
	if currentMax > max {
		max = currentMax
	}
	fmt.Print(max)
}
