package main

import (
	"aoc21/utils"
	"fmt"
	"math"
	"strconv"
	"strings"
)

const DAY = "04"


func calcScore(nums []int, card [][]int) (int, int){
	var score = 0
	for _,col := range card{
		for _,val := range col{
			score += val
		}
	}

	var cols = []int{5,5,5,5,5}
	var rows = []int{5,5,5,5,5}

	for r, num := range nums{
		for y := 0; y < 5; y++ {
			for x := 0; x < 5; x++ {
				if card[y][x] == num {
					score -= num
					rows[y] -= 1
					cols[x] -= 1
					if rows[y] == 0 || cols[x] == 0{
						return r, score*num
					}
				}
			}
		}
	}

	return -1, 0
}


func solvePart1(input string) int {
	var lines = strings.Split(input, "\r\n")
	var nums = utils.StringArrayToIntArray(strings.Split(lines[0], ","))

	var cards [][][]int
	var card [][]int
	for i := 2; i < len(lines); i++ {
		if lines[i] == "" {
			cards = append(cards, card)
			card = [][]int{}
		} else {
			card = append(card, utils.StringArrayToIntArray(strings.Fields(lines[i])))
		}
	}

	var minRound = math.MaxInt
	var minScore = 0
	for i := 0; i < len(cards); i++{
		var c = cards[i]
		var round, score = calcScore(nums, c)
		if round < minRound {
			minRound = round
			minScore = score
		}
	}

	return minScore
}

func solvePart2(input string) int {
	var lines = strings.Split(input, "\r\n")
	var nums = utils.StringArrayToIntArray(strings.Split(lines[0], ","))

	var cards [][][]int
	var card [][]int
	for i := 2; i < len(lines); i++ {
		if lines[i] == "" {
			cards = append(cards, card)
			card = [][]int{}
		} else {
			card = append(card, utils.StringArrayToIntArray(strings.Fields(lines[i])))
		}
	}

	var maxRound = 0
	var maxScore = 0
	for i := 0; i < len(cards); i++{
		var c = cards[i]
		var round, score = calcScore(nums, c)
		if round > maxRound {
			maxRound = round
			maxScore = score
		}
	}

	return maxScore
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
