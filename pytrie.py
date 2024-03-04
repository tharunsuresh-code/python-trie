from collections import defaultdict

"""
Definition: A trie (derived from retrieval) is a multiway tree data structure 
used for storing strings over an alphabet. It is used to store a large amount 
of strings. The pattern matching can be done efficiently using tries.

The trie shows words like allot, alone, ant, and, are, bat, bad. The idea is 
that all strings sharing common prefix should come from a common node. The 
tries are used in spell checking programs.

Preprocessing pattern improves the performance of pattern matching algorithm. 
But if a text is very large then it is better to preprocess text instead of 
pattern for efficient search.
A trie is a data structure that supports pattern matching queries in time 
proportional to the pattern size.

Ref: https://www.geeksforgeeks.org/trie-insert-and-search/

Usage
-----
import pytrie

>>> trie = pytrie.Trie()
>>> trie.addWord("hello")
>>> trie.addWord("world")
>>> trie.addWord("worlds")
>>> trie.addWord("Harry")
>>> trie.addWord("Potter")

>>> trie
<pytrie.Trie at 0x7fb17466bc70>

>>> trie.search("hello")
True

>>> trie.search("harry")
False

>>> trie.search("Harry")
True
"""


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
