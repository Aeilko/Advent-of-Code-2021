package main

import (
	"aoc21/utils"
	"fmt"
	"strconv"
	"strings"
)

const DAY = "01"


func solvePart1 (input string) int {
	var lines = strings.Split(input, "\r\n")

	var prevVal, result int
	for index, line := range lines {
		var val = utils.StringToInt(line)
		if index == 0{
			prevVal = val
			continue
		}

		if prevVal < val {
			result += 1
		}
		prevVal = val
	}

	return result
}

func solvePart2 (input string) int {
	var lines = strings.Split(input, "\r\n")

	var result int
	for i := 0; i < len(lines)-3; i++ {
		var val1 = utils.StringToInt(lines[i])
		var val2 = utils.StringToInt(lines[i+3])
		if val1 < val2 {
			result += 1
		}
	}

	return result
}


func testPart1 () bool {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/test")
	var answer,_ = strconv.Atoi(utils.ReadFileContent("day" + DAY + "/inputs/ans1"))

	var result = solvePart1(input)
	if result != answer {
		fmt.Println("Test unsuccessful: " + strconv.Itoa(result) + ", expected: " + strconv.Itoa(answer))
	}
	return result == answer
}

func testPart2 () bool {
	var input = utils.ReadFileContent("day" + DAY + "/inputs/test")
	var answer,_ = strconv.Atoi(utils.ReadFileContent("day" + DAY + "/inputs/ans2"))

	var result = solvePart2(input)
	if result != answer {
		fmt.Println("Test unsuccessful: " + strconv.Itoa(result) + ", expected: " + strconv.Itoa(answer))
	}
	return result == answer
}

func main () {
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
