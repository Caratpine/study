package main

func WordCount(s string) map[string]int {
	var dict = map[string]int{}
	for _, v := range s {
		dict[string(v)]++
	}
	return dict
}


