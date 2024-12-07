package main

import (
	"fmt"
	"strconv"
	"slices"
	"math"
	"strings"
)

func main(){
	var inp string = `3   4
4   3
2   5
1   3
3   9
3   3`
	var list1,list2 []int;
	for _, line := range strings.Split(inp, "\n"){
		nums := strings.Split(line, "   ")
		first_num, err := strconv.Atoi(nums[0])
		if err != nil{
			panic(err)
		}
		second_num, err := strconv.Atoi(nums[1])
		if err != nil{
			panic(err)
		}
		list1 = append(list1, first_num)
		list2 = append(list2, second_num)
	}
	slices.Sort(list1)
	slices.Sort(list2)
	fmt.Println(list1)
	fmt.Println(list2)
	part1(list1, list2)
	part2(list1, list2)
}

func part1(list1 []int, list2 []int){
	var sum int = 0
	for i := 0; i < len(list1); i++{
		sum += int(math.Abs(float64(list1[i] - list2[i])))
	}
	fmt.Println(sum)
}

func part2(list1 []int, list2 []int){
	freqMap := make(map[int]int)
	for _, val := range list2{
		freq, contains := freqMap[val]
		if !contains{
			freqMap[val] = 1
		}else{
			freqMap[val] = 1 + freq
		}
	}
	var sum int = 0
	for _, val := range list1{
		freq := freqMap[val]
		sum += freq * val
	}
	fmt.Println(sum)
}