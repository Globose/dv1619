import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        comb = []
        for i in range(len(profits)):
            comb.append((capital[i], profits[i]))
        comb.sort(reverse=True)

        heap = []
        upperlim = len(comb)-1
        while upperlim > -1 and comb[upperlim][0] <= w:
            heap.append(-comb.pop()[1])
            upperlim -= 1

        heapq.heapify(heap)
        while k > 0 and len(heap) > 0:
            w -= heapq.heappop(heap)
            while upperlim > -1 and comb[upperlim][0] <= w:
                heapq.heappush(heap, -comb.pop()[1])
                upperlim -= 1
            k-=1
        return w


s = Solution()
print(s.findMaximizedCapital(2,0,[1,2,3],[0,1,1]))
print(s.findMaximizedCapital(3,0,[1,2,3],[0,1,2]))
