class Solution(object):
    def mergeAlternately(self, word1, word2):

        n1 = len(word1)
        n2 = len(word2)

        maxN = max(n1,n2)
        result = []

        for i in range(maxN):
            if i < n1:
                result.append(word1[i])
            
            if i < n2:
                result.append(word2[i])
        

        return "".join(result)


#Space: O(n+m)
#Time: O(m)
