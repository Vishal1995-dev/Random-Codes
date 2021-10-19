class Solution:
    def next_step(self, cells):
        res = [0] * 8
        for i in range(1,7):
            res[i] = int(cells[i-1] == cells[i+1])
        return res
    
    def prisonAfterNDays(self, cells, N):
        found_dic = {}
        for i in range((N-1)%14+1):
            found_dic[i] = cells
            cells = self.next_step(cells) 
        return cells
