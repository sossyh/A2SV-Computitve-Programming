class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
        
        date = date.split()
        
        day = ""
        
        for i in date[0]:
            if i.isnumeric():
                day += i
        
        if len(day) == 1:
            day = "0" + day
            
        month = str(months[date[1]])
        
        if len(month) == 1:
            month = "0" + month
        
        year = date[-1]
        
        ans = year + "-" + month + "-" + day
        
        return ans