# WordTrie

## Example

Create a new trie:

    from wordtrie import WordTrie
    trie = WordTrie()

Words and their values are added to the trie with the `add()` method:

    trie.add("She", 1)
    trie.add("sea", 2)

Exact matches in the trie are found with the `match()` method:

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
    print(trie.search("She sells sea shells by the sea shore."))
    # [1, 3, 2]

The trie can be written to a JSON file with:

    trie.to_json("sea.json")
    # {
    #   "She": {
    #     "#": 1
    #   },
    #   "sea": {
    #     "#": 2,
    #     "shells": {
    #       "#": 3
    #     }
    #   }
    # }

Or restored from a JSON file with:

    trie.from_json("sea.json")
    print(trie.match("sea"))
    # 2

The reserved key `#` is used to store the value in the JSON structure. You can still add a word that starts with `#` to the trie, and it will be protected with an additional prepended `#`:

    trie.add("#She", 4)
    trie.to_json("sea.json")
    # {
    #    "##She": {
    # ...
    print(trie.match("#She"))
    # 4

When a node does not yet exist in the trie, the value specified in the `add()` method is used as the initial value. If the node already exists, then an aggregator function can be called to modify the value based on the old and new values. The default aggregator is to replace the old value with the new value. However, a custom aggregator can be defined as a function with signature `aggregator(old, new)` and passed to the `add()` call:

    def sum_aggregator(old, new):
        return old + new
    trie.add("She", 100, aggregator=sum_aggregator)
    print(trie.search("She sells sea shells by the sea shore."))
    # [101, 3, 2]

## Testing

Run the example above as a basic regression test with:

    # grep "^    " README.md | sed 's/    //' | python
