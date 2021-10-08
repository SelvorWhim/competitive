# recursive implementation where every level is a dict mapping letters to more tries

class Trie:

    def __init__(self):
        self.trie_map = {}
        self.full_word = False

    def insert(self, word: str) -> None:
        trie_it = self
        for char in word:
            if char not in trie_it.trie_map:
                trie_it.trie_map[char] = Trie()
            trie_it = trie_it.trie_map[char]
        trie_it.full_word = True

    def search(self, word: str) -> bool:
        trie_it = self
        for char in word:
            if char not in trie_it.trie_map:
                return False
            trie_it = trie_it.trie_map[char]
        return trie_it.full_word

    def startsWith(self, prefix: str) -> bool:
        trie_it = self
        for char in prefix:
            if char not in trie_it.trie_map:
                return False
            trie_it = trie_it.trie_map[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
