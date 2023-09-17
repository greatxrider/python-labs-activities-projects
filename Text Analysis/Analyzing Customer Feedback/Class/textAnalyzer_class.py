# Jeph Mari Daligdig
# Text Analyzer


class textAnalyzer(object):
    
    def __init__(self, text):
        formattedText = (
            text.replace(".", "").replace("!", "").replace("?", "").replace(",", "")
        )
        formattedText = formattedText.lower()
        self.fmtText = formattedText

    def freqAll(self):
        worldList = self.fmtText.split(" ")
        freqMap = {}
        for word in set(worldList):
            freqMap[word] = worldList.count(word)
        return freqMap  

    def freqOf(self, word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
