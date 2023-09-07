class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def heapify(heap, n, i):
            smaller = i
            left, right = 2 * i, 2 * i + 1

            if (left < n) and (heap[smaller][0] > heap[left][0]):
                smaller = left

            if (right < n) and (heap[smaller][0] > heap[right][0]):
                smaller = right

            if smaller != i:
                heap[i], heap[smaller] = heap[smaller], heap[i]
                heapify(heap, n, smaller)

        def build_min_heap(arr):
            for i in range(len(arr) // 2, -1, -1):
                heapify(arr, len(arr), i)

        counter = 0
        distance = []
        result = []
        for x, y in points:
            temp = (x)**2 + (y)**2
            distance.append([temp, x, y])
        
        build_min_heap(distance)
        while counter < k:
            result.append([distance[0][1], distance[0][2]])
            if len(distance) > 1:
                distance[0], distance[-1] = distance[-1], distance[0]
                distance.pop()
                heapify(distance, len(distance), 0)
            counter += 1
        
        return result
