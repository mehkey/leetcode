func minTime(n int, edges [][]int, hasApple []bool) int {

	tree := make([][]int, n)

	//tree = [[] for _ in range(n)]

	//fmt.Println(tree)

	for _, e := range edges {
		//fmt.Println(e)
		tree[e[0]] = append(tree[e[0]], e[1])
		tree[e[1]] = append(tree[e[1]], e[0])
	}

	//return dfs(-1,0)

	/**
	  def dfs(parent, node):
	      steps = 0
	      for c in tree[node]:
	          if c != parent:
	              steps += dfs(node, c)
	      if (hasApple[node] or steps > 0) and node != 0:
	          steps += 2
	      return steps*/

	return dfs(-1, 0, tree, hasApple)
}

func dfs(parent int, node int, tree [][]int, hasApple []bool) int {
	steps := 0
	for _, c := range tree[node] {

		if c != parent {
			steps += dfs(node, c, tree, hasApple)
		}
	}
	if (hasApple[node] || steps > 0) && node != 0 {
		steps += 2
	}
	return steps
}