package utils

import (
	"log"
	"os"
)

func ReadFileContent(path string) string {
	b, err := os.ReadFile(path)
	if err != nil {
		log.Fatal(err)
	}
	return string(b)
}
