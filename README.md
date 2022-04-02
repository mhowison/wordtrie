# WordTrie

## Example

Create a new trie:

    from wordtrie import WordTrie
    trie = WordTrie()

Words and their values are added to the trie with the `add()` method:

    trie.add("She", 1)
    trie.add("sea", 2)

Exact matches in the trie around found with the `match()` method:

    trie.match("She")
    # 1
    trie.match("sells")
    # None
    trie.match("She sells")
    # None

All matches in a stream of words can be found with the `search()` method:

    trie.search("She sells sea shells by the sea shore.")
    # [1, 2, 2]

Phrases can be added too and will be split into a list of words:

    trie.add("sea shells", 3)
    # same as trie.add(["sea", "shells"], 3)

Matching is greedy and will match the maximal length phrase:

	trie.match("sea shells")
	# 3
    trie.search("She sells sea shells by the sea shore.".split())
    # [1, 3, 2]
