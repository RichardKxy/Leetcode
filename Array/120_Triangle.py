class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)

        dp = triangle[n-1]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = min( dp[j], dp[j+1] ) + triangle[i][j]

        return dp[0]

s = Solution()
triangle = [[-10]]
print (s.minimumTotal(triangle))

"""
If we solve it from top to down, it may require to build 2D matrix. 
So we can try from down to top.

Suppose the triangle has n layers.

We firstly initiate dp as equal to the last layer of triangle, so dp has 1*n dimension.

Then we move from (n-1)th layer upward, for each movement, we will compare and store the minimum choice for each point in this layer. That is:

At (n-1)th layer, for each i in this layer, find min(triangle[i]+dp[i], triangle[i]+dp[i+1]), then refresh dp[i] with the result.

So dp[i] denote that, till current time, when we move from down to current layer, the minimum so far for each point i in this layer.
"""