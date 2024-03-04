# pytrie
A basic implementation of word dictionary using the Trie data structure in Python 3.

A trie (derived from retrieval) is a multiway tree data structure 
used for storing strings over an alphabet. It is used to store a large amount 
of strings. The pattern matching can be done efficiently using tries.

To clone the repo:
```bash
git clone https://github.com/tharunsuresh-code/pytrie.git
```

## Usage
Create a new ``Trie`` to use as a word dictionary:
```python
from pytrie import Trie

trie = Trie()
trie.addWord("hello")
trie.addWord("world")
trie.addWord("Harry")
trie.addWord("Potter")
```

Now you can query the Trie for any string:
```python
>>> trie.search("hello")
True
>>> trie.search("world")
True
>>> trie.search("harry")
False
>>> trie.search("Harry")
True
```

## Author and References
Docs are inspired from [PyTrie](https://github.com/gsakkis/pytrie) and [datrie](https://github.com/pytries/datrie).

## License
Licensed under MIT.
