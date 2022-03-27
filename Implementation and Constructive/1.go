package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)
	var operations []string
	operations = make([]string, n)

	for i := 0; i < n; i++ {
		var operation string
		fmt.Scanln(&operation)
		operations[i] = operation
	}
	fmt.Println(solve(n, operations))
}

func solve(n int, operations []string) int {
	var count int = 0
	for _, operation := range operations {
		if operation == "++X" || operation == "X++" {
			count++
		} else if operation == "--X" {
			count--
		}
	}
	return count
}
