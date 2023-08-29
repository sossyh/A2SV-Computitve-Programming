class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        a = int(event1[0][:2])
        b = float(event1[0][3:]) / 60
        c = int(event1[1][:2])
        d = float(event1[1][3:]) / 60
        
        event1 = [a+b, c+d]
        
        a = int(event2[0][:2])
        b = float(event2[0][3:]) / 60
        c = int(event2[1][:2])
        d = float(event2[1][3:]) / 60
        
        event2 = [a+b, c+d]
        
        if (event1[0] >= event2[0] and event1[0] <= event2[1]) or (event2[0] >= event1[0] and event2[0] <= event1[1]):
            return True
        
        return False