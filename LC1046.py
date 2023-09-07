class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapify(heap, n, i):
            largest = i
            left, right = 2 * i, 2 * i +1
            if (left < n) and (heap[largest] < heap[left]):
                largest = left
            if (right < n) and (heap[largest] < heap[right]):
                largest = right
            if largest != i:
                heap[i], heap[largest] = heap[largest], heap[i]
                heapify(heap, n, largest)

        def build_max_heap(arr):
            for i in range(len(arr)//2, -1, -1):
                heapify(arr, len(arr), i)
        
        def get_max_value(arr):
            max = arr[0]
            if len(arr) > 1:
                arr[0], arr[-1] = arr[-1], arr[0]
                arr.pop()
                heapify(arr, len(arr), 0)
            else:
                arr.pop()
            return max
        
        def add_value(arr, val):
            arr.append(val)
            build_max_heap(arr)
        
        build_max_heap(stones)
        while len(stones) > 1:
            y = get_max_value(stones)
            x = get_max_value(stones)
            if x != y:
                y = y - x
                add_value(stones, y)
        if stones:
            return stones[0]
        else:
            return 0     
