class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True

    # def process_dot(dot_index, word):


    def search(self, word: str, node = None) -> bool:
        curr = self.root if not node else node
        for index in range(len(word)):
            if word[index] == ".":
                res = []
                for child in curr.children.values():
                    res.append(self.search(word[index+1:], child))
                if any(res):
                    return True
                return False
            if word[index] not in curr.children:
                return False
            curr = curr.children[word[index]]
        
        return curr.word
