class Solution:
	def minPushBox(self, grid: List[List[str]]) -> int:
		n,m=len(grid),len(grid[0])
		for i in range(n):
			for j in range(m):
				if grid[i][j]=='S':
					player=[i,j]
				elif grid[i][j]=='T':
					target=[i,j]
				elif grid[i][j]=='B':
					box=[i,j]
		q=deque([[player[0],player[1],box[0],box[1],0]])
		vis=set([(player[0],player[1],box[0],box[1])])
		while q:
			i,j,bi,bj,steps=q.pop()
			if [bi,bj]==target:
				return steps
			for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
				x,y=i+dx,j+dy
				if 0<=x<n and 0<=y<m and grid[x][y]!='#':
					if (x,y)==(bi,bj):
						if 0<=bi+dx<n and 0<=bj+dy<m and grid[bi+dx][bj+dy]!='#':
							if not (x,y,bi+dx,bj+dy) in vis:
								vis.add((x,y,bi+dx,bj+dy))
								q.appendleft([x,y,bi+dx,bj+dy,steps+1])
					elif (x,y,bi,bj) not in vis:
						vis.add((x,y,bi,bj))
						q.append([x,y,bi,bj,steps])
		return -1