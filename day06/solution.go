package main

import (
	"aoc21/utils"
	"fmt"
	"strconv"
	"strings"
)

const DAY = "06"


func solvePart1(input string) int {
	var lines = strings.Split(input, "\r\n")
	var fish = utils.StringArrayToIntArray(strings.Split(lines[0], ","))
	var ages = [9]int{}

	for _,f := range fish {
		ages[f] += 1
	}

	for d := 0; d < 80; d++ {
		var new_fish = ages[0]
		for i := 1; i < 9; i++ {
			ages[i-1] = ages[i]
		}
		ages[6] += new_fish
		ages[8] = new_fish
	}

	var result = 0
	for _,a := range ages {
		result += a
	}
	return result
}

func solvePart2(input string) int {
	var lines = strings.Split(input, "\r\n")
	var fish = utils.StringArrayToIntArray(strings.Split(lines[0], ","))
	var ages = [9]int{}

	for _,f := range fish {
		ages[f] += 1
	}

	for d := 0; d < 256; d++ {
		var new_fish = ages[0]
		for i := 1; i < 9; i++ {
			ages[i-1] = ages[i]
		}
		ages[6] += new_fish
		ages[8] = new_fish
	}

	var result = 0
	for _,a := range ages {
		result += a
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
