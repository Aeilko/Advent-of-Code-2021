package main

import (
	"aoc21/utils"
	"fmt"
	"strconv"
	"strings"
)

const DAY = "03"


func solvePart1 (input string) int {
	var lines = strings.Split(input, "\r\n")
	var length = len(lines)

	var occurrences []int
	for i := 0; i < len(lines[0]); i++ {
		occurrences = append(occurrences, 0)
	}

	for _, line := range lines {
		for i := 0; i < len(line); i++{
			if line[i] == '1' {
				occurrences[i] += 1
			}
		}
	}

	var gamma = ""
	var epsilon = ""
	for _, occ := range occurrences {
		if occ > length/2 {
			gamma += "1"
			epsilon += "0"
		} else {
			gamma += "0"
			epsilon += "1"
		}
	}

	var gammaVal,_ = strconv.ParseInt(gamma, 2, 16)
	var epsilonVal,_ = strconv.ParseInt(epsilon, 2, 16)

	return int(gammaVal * epsilonVal)
}

func solvePart2 (input string) int {
	var lines = strings.Split(input, "\r\n")

	var oxyList = map[string]bool{}
	var co2List = map[string]bool{}
	for _,line := range lines {
		oxyList[line] = true
		co2List[line] = true
	}

	for i := 0; i < len(lines[0]); i++ {
		var oxyListLength = len(oxyList)
		var co2ListLength = len(co2List)

		// Count 1's on both lists
		var oxyOccurrences = 0
		for key := range oxyList {
			if key[i] == '1' {
				oxyOccurrences += 1
			}
		}
		var co2Occurrences = 0
		for key := range co2List {
			if key[i] == '1' {
				co2Occurrences += 1
			}
		}

		// Delete "wrong" bits from the oxygen list
		if oxyListLength > 1 {
			var oxyDeleteList = map[string]bool{}
			if float64(oxyOccurrences) >= float64(oxyListLength)/2 {
				for key:= range oxyList {
					if key[i] == '0' {
						oxyDeleteList[key] = true
					}
				}
			} else {
				for key := range oxyList {
					if key[i] == '1' {
						oxyDeleteList[key] = true
					}
				}
			}
			for key := range oxyDeleteList {
				delete(oxyList, key)
			}
		}

		// Delete "wrong" bits from the CO2 list
		if co2ListLength > 1 {
			var co2DeleteList = map[string]bool{}
			if float64(co2Occurrences) >= float64(co2ListLength)/2 {
				for key := range co2List {
					if key[i] == '1' {
						co2DeleteList[key] = true
					}
				}
			} else {
				for key := range co2List {
					if key[i] == '0' {
						co2DeleteList[key] = true
					}
				}
			}
			for key := range co2DeleteList {
				delete(co2List, key)
			}
		}
	}

	var oxyValue, co2Value int64
	for key := range oxyList {
		oxyValue,_ = strconv.ParseInt(key, 2, 32)
	}
	for key:= range co2List {
		co2Value,_ = strconv.ParseInt(key, 2, 32)
	}

	return int(oxyValue * co2Value)
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
