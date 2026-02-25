class Solution:
    def generateTag(self, caption: str) -> str:
        filtered = ""
        for c in caption:
            if c.isalpha() or c == " ":
                filtered += c

        caption = filtered.split()
        if not caption:
            return  "#"
        n = len(caption)
        camel = "#" + caption[0].lower()
        camel += "".join(w.capitalize() for w in caption[1:])
        return camel[:100]
