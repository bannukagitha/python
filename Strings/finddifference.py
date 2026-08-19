def findTheDifference(s, t):
        if not s:
            return t[0]
        totals=0
        totalt=0
        for x in s:
            totals+=ord(x)
        for x in t:
            totalt+=ord(x)
        return chr(totalt-totals)