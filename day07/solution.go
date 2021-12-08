package main

import (
	"aoc21/utils"
	"fmt"
	"math"
	"strconv"
	"strings"
)

const DAY = "07"


func solvePart1(input string) int {
	var lines = strings.Split(input, "\r\n")
	var crabs = utils.StringArrayToIntArray(strings.Split(lines[0], ","))

	var minVal = math.MaxInt
	var maxVal = 0
	for _,c := range crabs {
		if c < minVal {
			minVal = c
		}
		if c > maxVal {
			maxVal = c
		}
	}

	var result = math.MaxInt
	for i := minVal; i <= maxVal; i++ {
		var s = 0
		for _,c := range crabs {
			s += int(math.Abs(float64(c-i)))
		}
		if s < result {
			result = s
		}
	}

	return result
}

func solvePart2(input string) int {
	var lines = strings.Split(input, "\r\n")
	var crabs = utils.StringArrayToIntArray(strings.Split(lines[0], ","))

	var minVal = math.MaxInt
	var maxVal = 0
	for _,c := range crabs {
		if c < minVal {
			minVal = c
		}
		if c > maxVal {
			maxVal = c
		}
	}

	var result = math.MaxInt
	for i := minVal; i <= maxVal; i++ {
		var s = 0
		for _,c := range crabs {
			var dist = int(math.Abs(float64(c-i)))

			s += dist * (dist + 1) / 2
		}
		if s < result {
			result = s
		}
	}

	return result
}

func testPart1() bool {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/test")
	var answer, _ = strconv.Atoi(utils.ReadFileContent("day" + DAY + "/inputs/ans1"))

	var result = solvePart1(input)
	if result != answer {
		fmt.Println("Test unsuccessful: " + strconv.Itoa(result) + ", expected: " + strconv.Itoa(answer))
	}
	return result == answer
}

func testPart2() bool {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/test")
	var answer, _ = strconv.Atoi(utils.ReadFileContent("day" + DAY + "/inputs/ans2"))

	var result = solvePart2(input)
	if result != answer {
		fmt.Println("Test unsuccessful: " + strconv.Itoa(result) + ", expected: " + strconv.Itoa(answer))
	}
	return result == answer
}

func main() {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/input")

	fmt.Println(" ~~~ Advent of Code 2021, Day " + DAY + " ~~~")

	fmt.Println(" --- Part 1 --- ")
	var test = testPart1()
	if test {
		fmt.Println("Test Successful")
		fmt.Println("Part 1 result:\t" + strconv.Itoa(solvePart1(input)))
	}

	fmt.Println("\n --- Part 2 --- ")
	test = testPart2()
	if test {
		fmt.Println("Test Successful")
		fmt.Println("Part 2 result:\t" + strconv.Itoa(solvePart2(input)))
	}
}
