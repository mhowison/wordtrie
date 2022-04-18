"""
WordTrie: a simple trie (prefix tree) for word and phrase matching
"""

import json
from importlib import resources

__version__ = resources.read_text(__name__, "VERSION").strip()

_VALUE_KEY_ = "#" # Reserved value key

def _check_value_key(word):
    """
    Protect the reserved value key by prepending it
    again to any word that starts with it.
    """
    if word.startswith(_VALUE_KEY_):
        return f"{_VALUE_KEY_}{word}"
    else:
        return word

def _check_list(words):
    """
    Split `words` into a list if it is a string.
    """
    if isinstance(words, str):
        return words.split()
    else:
        return words

def _default_aggregator(old, new):
    """
    Replace old value with new value.
    """
    return new

class WordTrie(object):

    def __init__(self):
        self.root = {}

    def add(self, words, value, aggregator=_default_aggregator):
        """
        Add a list of `words` as nodes in the trie, assigning `value`
        to the final node according to the aggregator function. The
        default aggregator is to replace any existing value with the
        newly added value.

        You can specify a custom aggregator as function with signature
        `aggregator(old, new)` that returns the value to assign to the
        node. The aggregator function is only called if the node already
        exists and has a value. In that case, value of `old` is the
        existing value for the node and `new` is equal to `value`.
        """
        node = self.root
        for word in _check_list(words):
            word = _check_value_key(word)
            if not word in node:
                node[word] = {}
            node = node[word]
        if _VALUE_KEY_ in node:
            node[_VALUE_KEY_] = aggregator(node[_VALUE_KEY_], value)
        else:
            node[_VALUE_KEY_] = value


    def match(self, words):
        """
        Find an exact match of `words` in the trie and return the value.
        Return `None` if there is no match.
        """
        node  = self.root
        words = _check_list(words)
        for word in words:
            word = _check_value_key(word)
            if word in node:
                node = node[word]
            else:
                return None
        return node.get(_VALUE_KEY_)

    def search(self, words, return_nodes=False):
        """
        Search a stream of `words` against the trie, returning
        a concenation of values for all sub-sequences within the stream
        that match. Return an empty list if no matches are found.

        If `return_nodes` is True, then the returned list contains
        tuples `(node, value)` instead of bare values.
        """
        node   = self.root
        match  = []
        values = []
        for word in _check_list(words):
            word = _check_value_key(word)
            if word in node:
                # Start or continue a match.
                node = node[word]
                match.append(word)
            else:
                if match:
                    # The end of a match. Concatenate the value.
                    if _VALUE_KEY_ in node:
                        if return_nodes is True:
                            values.append((match, node[_VALUE_KEY_]))
                        else:
                            values.append(node[_VALUE_KEY_])
                # Restart the search.
                if word in self.root:
                    node = self.root[word]
                    match = [word]
                else:
                    node = self.root
                    match = []
        if match:
            # The final match. Concatenate the value.
            if _VALUE_KEY_ in node:
                if return_nodes is True:
                    values.append((match, node[_VALUE_KEY_]))
                else:
                    values.append(node[_VALUE_KEY_])
        return values

    def to_json(self, filename, indent=2):
        """
        Write the trie structure to a json file in `filename`.
        CAUTION: will overrite an existing file with that name.
        """
        with open(filename, "w") as f:
            json.dump(self.root, f, indent=indent)

    def from_json(self, filename):
        """
        Add to the trie structure from the json file in `filename`.
        NOTE: the file must have been written by to_json() or use the
        same encoding of values.
        """
        with open(filename) as f:
            self.root = json.load(f)
        return self
