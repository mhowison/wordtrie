# WordTrie

## Example

Create a new trie:

    from wordtrie import WordTrie
    trie = WordTrie()

Words and their values are added to the trie with the `add()` method:

    trie.add("She", 1)
    trie.add("sea", 2)

Exact matches in the trie around found with the `match()` method:

    print(trie.match("She"))
    # 1
    print(trie.match("sells"))
    # None
    print(trie.match("She sells"))
    # None

All matches in a stream of words can be found with the `search()` method:

    print(trie.search("She sells sea shells by the sea shore."))
    # [1, 2, 2]

Phrases can be added too and will be split into a list of words:

    trie.add("sea shells", 3)
    # same as trie.add(["sea", "shells"], 3)

Matching is greedy and will match the maximal length phrase:

    print(trie.match("sea shells"))
    # 3
    print(trie.search("She sells sea shells by the sea shore.".split()))
    # [1, 3, 2]

## Testing

Run the example above as a quick regression test with: `grep "^    " README.md | sed 's/    //' | python`
