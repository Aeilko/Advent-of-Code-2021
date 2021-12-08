package main

import (
	"aoc21/utils"
	"fmt"
	"math"
	"strconv"
	"strings"
)

const DAY = "05"


type Coord struct {
	X, Y int
}


func visualize(points map[Coord]int) {
	var maxX = 0
	var maxY = 0
	for key := range points {
		if key.X > maxX {
			maxX = key.X
		}
		if key.Y > maxY {
			maxY = key.Y
		}
	}

	for y := 0; y <= maxY; y++ {
		var line = ""
		for x := 0; x <= maxX; x++ {
			var c = Coord{x,y}
			if val, ok := points[c]; ok {
				line += strconv.Itoa(val)
			} else {
				line += "."
			}
		}
		fmt.Println(line)
	}
}


func solvePart1(input string) int {
	var lines = strings.Split(input, "\r\n")

	var points = map[Coord]int{}

	for _,line := range lines {
		var tmp = strings.Split(line, " -> ")
		var start = utils.StringArrayToIntArray(strings.Split(tmp[0], ","))
		var end = utils.StringArrayToIntArray(strings.Split(tmp[1], ","))

		var directionX = 0
		var directionY = 0
		var length = 0

		if start[0] == end[0] {
			length = int(math.Abs(float64(start[1]-end[1])))
			directionY = 1
			if start[1] > end[1] {
				directionY = -1
			}
		} else if start[1] == end[1] {
			length = int(math.Abs(float64(start[0]-end[0])))
			directionX = 1
			if start[0] > end[0] {
				directionX = -1
			}
		}

		for i := 0; length > 0 && i <= length; i++ {
			var x = start[0] + i*directionX
			var y = start[1] + i*directionY
			var c = Coord{x,y}
			if _, ok := points[c]; ok {
				points[c] += 1
			} else {
				points[c] = 1
			}
		}
	}

	var result = 0
	for _, val := range points {
		if val > 1 {
			result += 1
		}
	}
	return result
}

func solvePart2(input string) int {
	var lines = strings.Split(input, "\r\n")

	var points = map[Coord]int{}

	for _,line := range lines {
		var tmp = strings.Split(line, " -> ")
		var start = utils.StringArrayToIntArray(strings.Split(tmp[0], ","))
		var end = utils.StringArrayToIntArray(strings.Split(tmp[1], ","))

		var directionX = 0
		var directionY = 0
		var length = 0

		if start[0] == end[0] {
			length = int(math.Abs(float64(start[1]-end[1])))
			directionY = 1
			if start[1] > end[1] {
				directionY = -1
			}
		} else if start[1] == end[1] {
			length = int(math.Abs(float64(start[0]-end[0])))
			directionX = 1
			if start[0] > end[0] {
				directionX = -1
			}
		} else {
			length = int(math.Abs(float64(start[0]-end[0])))
			directionX = 1
			directionY = 1
			if start[0] > end[0] {
				directionX = -1
			}
			if start[1] > end[1] {
				directionY = -1
			}
		}

		for i := 0; length > 0 && i <= length; i++ {
			var x = start[0] + i*directionX
			var y = start[1] + i*directionY
			var c = Coord{x,y}
			if _, ok := points[c]; ok {
				points[c] += 1
			} else {
				points[c] = 1
			}
		}
	}

	var result = 0
	for _, val := range points {
		if val > 1 {
			result += 1
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
