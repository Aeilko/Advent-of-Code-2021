package utils

import (
	"log"
	"strconv"
)

func StringToInt (num string) int {
	var val, err = strconv.Atoi(num)
	if err != nil {
		log.Fatalln(err)
		return 0
	} else {
		return val
	}
}
