from collections import defaultdict


class Trie:

    def __init__(self):
        self.dictionary = defaultdict(dict)

    def addWord(self, word: str) -> None:
        currentDict = self.dictionary
        for i in range(len(word)):
            if word[i] in currentDict:
                currentDict = currentDict[word[i]]
            else:
                currentDict[word[i]] = dict()
                currentDict = currentDict[word[i]]
        currentDict["#"] = dict()
        
    def search(self, word: str, currentDict=None) -> bool:
        if currentDict is None:
            currentDict = self.dictionary

        for i in range(len(word)):
            if word[i] == '.':
                for w in currentDict:
                    isFound = self.search(word[i+1:], currentDict[w])
                    if isFound:
                        return isFound
                return False
            else:
                if word[i] in currentDict:
                    currentDict = currentDict[word[i]]
                else:
                    return False
        if '#' in currentDict:
            return True
        return False
