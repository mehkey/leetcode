// "static void main" must be defined in a public class.

/*
Input 
n k
Array elements space separated

*/


public class Main {
    public static void main(String[] args) throws IOException {
          BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
       
        int n,k;
        
         String []nk=br.readLine().split("\\s+");
            n=Integer.valueOf(nk[0]);
            k=Integer.valueOf(nk[1]);
        
        int[] nums=Arrays.stream(br.readLine().split("\\s+")).mapToInt(Integer::valueOf).toArray();
    
        
        System.out.println(Arrays.toString(nums));
        
        PriorityQueue<int []> pq=new PriorityQueue<>((a,b)->b[0]-a[0]);
        
        int[] absArray=Arrays.stream(nums).map(i->Math.abs(i)).toArray();
        
        
        Arrays.sort(absArray);
        
        System.out.println(Arrays.toString(absArray));
        
        int maxSum=0;
        for(int num:nums)
            if(num>0)
                maxSum+=num;
        
        pq.add(new int[]{maxSum-absArray[0],0});
        
        List<Integer> ans=new ArrayList<>();
        ans.add(maxSum);
        
        
        while(ans.size()<k)
        {
           int cur[]=pq.poll();
            int curSum=cur[0];
            int i=cur[1];
            ans.add(curSum);
            
            if(i+1<n)
            {
                pq.add(new int[]{curSum+absArray[i]-absArray[i+1],i+1});
                pq.add(new int[]{curSum-absArray[i+1],i+1});
            }
          
        }
        
        System.out.println(ans);
        
        
    }
}




int dp[2001][2001];


int recur(int i,int n,int m,int k,string s){
	if(i > n)return 0;

	if(i == n){
		if(k == 0)return 1;
		else return 0;
	}

	if(dp[n][k] != -1)return dp[n][k];
	char ch = s[i];
	int digit = ch - '0';
	int count = 0;
	if(digit % 2 == 0){
		for(int j = i + m - 1 ; j < n ; j++){
			int lastDigit = s[j] - '0';
			if(lastDigit % 2 != 0){
				count += recur(j + 1,n,m,k-1,s);
			}
		}
	}


	return dp[i][k] = count;

}