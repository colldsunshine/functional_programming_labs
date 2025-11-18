class task_1:
    def climbStairs(self, n: int) -> int:
        '''
        Вычисляет количество уникальных способов подняться на лестницу из n ступенек,
        если за один шаг можно подняться на 1 или 2 ступеньки.
        Использует итеративный подход с O(n) временем.
        LeetCode: 0 ms, Beats 100.00%
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev = 1 
        current = 2
        
        for i in range(3, n + 1):  
            next = prev + current
            prev = current
            current = next
        return current 

class task_2:
    def jump(self, nums: List[int]) -> int:
        '''
    Вычисляет минимальное количество прыжков, чтобы достичь конца массива,
    где каждый элемент массива представляет максимальную длину прыжка с этой позиции.
    Использует жадный алгоритм с O(n) временем.
    LeetCode: 5 ms, Beats 85.82%
    '''  
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
    
class task_3:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        Возвращает rowIndex строку треугольника Паскаля (нумерация с 0)
        Использует биномиальные коэффициенты для вычисления за O(n) времени.
        LeetCode: 0 ms, Beats 100.00%
        '''
        row = [1] 
        
        for k in range(rowIndex):
            row.append(row[-1] * (rowIndex - k) // (k + 1))
        
        return row

class task_4:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Находит максимальную прибыль от одной 
        транзакции (одна покупка + одна продажа)
        Выполняется за O(n) времени.
        LeetCode: 23 ms, Beats 92.86%
        '''
        if not prices:
            return 0
        
        min_price = prices[0]  
        max_profit = 0
        
        for price in prices[1:]:  
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

class task_5:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Находит максимальную прибыль от неограниченного 
        количества транзакций
        Выполняется за O(n) времени
        LeetCode: 0 ms, Beats 100.00%
        '''
        max_profit = 0

        for i in range(1, len(prices)):
            if (prices[i] > prices[i-1]):
                max_profit += prices[i] - prices[i-1]

        return max_profit
