class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dequeue = deque([i for i in range(1,n+1)])

        while len(dequeue) > 1:
            for j in range(k-1):
                temp = dequeue.popleft()
                dequeue.append(temp)
            dequeue.popleft()
        
        return dequeue[0]