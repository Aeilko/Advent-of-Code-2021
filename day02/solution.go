package main

import (
	"aoc21/utils"
	"fmt"
	"strconv"
	"strings"
)

const DAY = "02"


func solvePart1 (input string) string {
	var lines = strings.Split(input, "\r\n")

	var depth, horizontal int
	for _, line := range lines {
		var tmp = strings.Split(line, " ")
		var direction = tmp[0]
		var val = utils.StringToInt(tmp[1])

		if direction == "forward" {
			horizontal += val
		} else if direction == "down" {
			depth += val
		} else if direction == "up" {
			depth -= val
		}
	}

	return strconv.Itoa(depth*horizontal)
}

func solvePart2 (input string) string {
	var lines = strings.Split(input, "\r\n")

	var depth, horizontal, aim int
	for _, line := range lines {
		var tmp = strings.Split(line, " ")
		var direction = tmp[0]
		var val = utils.StringToInt(tmp[1])

		if direction == "forward" {
			horizontal += val
			depth += aim*val
		} else if direction == "down" {
			aim += val
		} else if direction == "up" {
			aim -= val
		}
	}

	return strconv.Itoa(depth*horizontal)
}


func testPart1 () bool {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/test")
	var answer = utils.ReadFileContent("day" + DAY + "/inputs/ans1")

	var result = solvePart1(input)
	if result != answer {
		fmt.Println("Test unsuccessful: " + result + ", expected: " + answer)
	}
	return result == answer
}

func testPart2 () bool {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/test")
	var answer = utils.ReadFileContent("day" + DAY + "/inputs/ans2")

	var result = solvePart2(input)
	if result != answer {
		fmt.Println("Test unsuccessful: " + result + ", expected: " + answer)
	}
	return result == answer
}

func main () {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/input")

	fmt.Println(" --- Part 1 --- ")
	var test = testPart1()
	if test {
		fmt.Println("Test Successful")
		fmt.Println("Part 1 result:\t" + solvePart1(input))
	}

	fmt.Println("\n --- Part 2 --- ")
	test = testPart2()
	if test {
		fmt.Println("Test Successful")
		fmt.Println("Part 2 result:\t" + solvePart2(input))
	}
}
