class Solution:
    def findLatestTime(self, s: str) -> str:
        hours, mins = s.split(":")

        hours, mins = list(hours), list(mins)

        if hours[1] == "?":
            if hours[0] == "0":
                hours[1] = "9"
            else:
                hours[1] = "1"
        
        if hours[0] == "?":
                hours[0] = "1" if hours[1] == "1" or hours[1] == "0" else "0"

        if mins[1] == "?":
            mins[1] = "9"
        
        if mins[0] == "?":
            mins[0] = "5"

        hours = "".join(hours)
        mins = "".join(mins)

        return hours + ":" + mins
