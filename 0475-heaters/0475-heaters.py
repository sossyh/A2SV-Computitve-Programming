class Solution:
    def find_the_nearest_heater(self, heaters, house):
        low, high = 0, len(heaters) - 1
        min_radius = inf
        
        while low <= high:
            mid = low + (high - low) // 2
            
            min_radius = min(min_radius, abs(heaters[mid] - house))
            
            if heaters[mid] > house:
                high = mid - 1
            else:
                low = mid + 1
        
        return min_radius
            
        
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        min_radius_total = - inf
        
        for house in houses:
            min_radius_total = max(min_radius_total, self.find_the_nearest_heater(heaters, house))
        
        return min_radius_total
        
        
        
            