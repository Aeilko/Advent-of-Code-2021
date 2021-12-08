package utils

import (
	"strconv"
)

func StringToInt(num string) int {
	var val, err = strconv.Atoi(num)
	if err != nil {
		panic(err)
		return 0
	} else {
		return val
	}
}

func StringArrayToIntArray(nums []string) []int {
	var result = []int{}
	for _, val := range nums {
		var v, err = strconv.Atoi(val)
		if err != nil {
			panic(err)
		}
		result = append(result, v)
	}
	return result
}
