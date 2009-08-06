# -*- coding: utf-8 -*-

def invert_dict(d):
    """ Invert a dict to a dict of the original values, mapped to a list of the
        original keys

        e.g. {'a': 1, 'b': 1, 'c':2 'd':3}
        is inverted to
        {1: ['a','b'], 2: ['c'], 3: ['d']}
    """
    inverted = {}
    for (value, key) in d.items():
        inverted[key] = inverted.setdefault(key, [])
        inverted[key].append(value)
    return inverted


class TopListKeeper:
    """ Keep a "top"-list of most frequent items

        There is one public instance attribute:
            keep_max [1000]    a limit on memory usage. Set this high enough
                               so that your targeted top n items would already
                               stand out in a list of length keep_max. If you
                               set this too low, results may be inaccurate.
                               The internal hash of items it kept to this size,
                               every time it is cut down, the least frequent
                               surplus items are discarded
    """

    def __init__(self):
        self.keep_max = 1000
        self._repo = {}

    def add(self, item):
        """ Add an item to the toplist """
        self._repo[item] = self._repo.setdefault(item, 0) + 1
        if len(self._repo.keys()) > 2 * self.keep_max:
            self._sieve_down()

    def toplist(self, top_n):
        """ Return a list of the top_n items """
        inverted = invert_dict(self._repo)
        toplist = []
        ordered_keylist = inverted.keys()
        ordered_keylist.sort(reverse=True)
        for count in ordered_keylist:
            for item in inverted[count]:
                toplist.append(item)
                if len(toplist) >= top_n:
                    return toplist[:top_n]

    def toplist_tuple(self, top_n):
        """ Return a list of tuples for the top_n items

            Each tuple consists of (item, count)
        """
        return [(item, self.count(item)) for item in self.toplist(top_n)]

    def _sieve_down(self):
        """ Cut the repo down to keep_max """
        toplist = self.toplist(self.keep_max)
        newrepo = {}
        i = 0
        for item in toplist:
            if i >= self.keep_max:
                break;
            newrepo[item] = self.count(item)
        self._repo = newrepo

    def count(self, item):
        """ Return the count for an item.

            This is only guaranteed to give an accurate result for items that
            would appear in any top list.
        """
        try:
            return self._repo[item]
        except KeyError:
            return 0
