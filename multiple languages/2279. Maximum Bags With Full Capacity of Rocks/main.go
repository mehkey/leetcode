func maximumBags(capacity []int, rocks []int, additionalRocks int) int {

	toAdd := make([]int, len(capacity))
	for i := range toAdd {
		toAdd[i] = capacity[i] - rocks[i]
	}

	sort.Ints(toAdd)
	for i := 0; i < len(toAdd); i++ {
		if toAdd[i] > additionalRocks || additionalRocks == 0 {
			// here we can't fill current bag then the result will be equal to the previous index + 1 or current i
			return i
		}

		additionalRocks -= toAdd[i]
	}

	//we can fill all bags
	return len(toAdd)

}