# -*- coding: utf-8 -*-
import cgi
import sys
import re

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")


def ensure_unicode(string, encodings):
    """ convert the string to unicode, if necessary """
    try:
        if not isinstance(string, basestring):
            string = str(string)
        if isinstance(string, unicode):
            return string
        else:
            for encoding in encodings:
                try:
                    return unicode(str(string), encoding)
                except:
                    pass
                else:
                    break
    except Exception:
        pass
    warn("There was a problem in the unicode conversion of %s" % string)
    return string

class RefererAnalyzer(object):
    """ Analyzes as referer string

        Use via the 'analyze'-methode and read results from the following attributes:
            refererstring       The full refererstring
            refererpage         A shortened refererstring, without 'http://' and vars
            referersite         Just the site of the refererstring, eg 'www.google.com'
            has_search          True if referer is result from a search enging
            searchstring        If has_search: the string that was searched for. This
                                string will be in unicode

        There is one public attribute:
            encodings ['utf-8', 'iso8859']    encodings that are tried to decode search
                                              strings
    """

    _searchfieldcollection = [
        (re.compile('(www|images|directory|groups|gotonet|wap)\.google\.'),  ['q', 'p'] ),
        (re.compile('search\.yahoo\.com'),  ['p'] ),
        (re.compile('altavista\.com'),  ['q'] ),
        (re.compile('msn\.com'),  ['q'] ),
        (re.compile('aol(search|find)\.aol\.'),  ['query', 'MT'] ),
        (re.compile('.*'),     ['query', 'q', 'search', 'as_epq', 'as_eq', 'as_oq', 'as_q', 'begriff', \
                                'busca', 'buscar', 'heureka', 'kereses', 'key', 'keys', 'keyword', 'keywords', \
                                'kw', 'mit', 'mt', 'p', 'q_all', 'q_any', 'q_not', 'q_phrase', 'qs', \
                                'qt', 'qu', 'r', 'req', 's', 's2f', 'searchfor', 'search_for', 'sp-q', \
                                'string', 'su', 'szukaj', 'term', 'terms', 'text', 'userQuery', 'v', 'va', \
                                've', 'vo', 'vp', 'w', 'wd', 'words', 'searchinput', 'eingabe']
        )
    ];
    # the _searchfieldcollection describes which url-encoded fields mark a search term for specific site.
    # the regex decides if the list of fields is appropriate for the site. The first match decides.
    # When we go through the fields in the url, the first field that we come accross that's in the list we
    # chose for the site is taken

    encodings = ['utf-8', 'iso8859']
    def __init__(self):
        self.refererstring = ""
        self.refererpage = ""
        self.referersite = ""
        self.has_search = False
        self.searchstring = ""
    def analyze(self, referer):
        """ Analyze a refererstring and fill the attributes 'refererstring', 'refererpage', 'referersite',
            'has_search', and 'searchstring'
        """
        referer = referer.strip()
        self.refererstring = referer
        referer = referer.replace("http://", "")
        self.refererpage = referer
        self.referersite = referer
        self.has_search = False
        self.searchstring = u""
        fieldstring = ""
        if referer.find("?") > 0:
            self.refererpage = referer[:referer.find("?")] # everything before '?'
            self.referersite = self.refererpage # temporary, processing below
            fieldstring = referer[(referer.find("?")+1):] # everything after '?'
            if referer.startswith("images.google.") and "/imgres?" in referer:
                # the google image search preview is a special case:
                # the search that belongs to the preview is encoded in the 'prev' field
                fieldstring = cgi.urllib.unquote(cgi.parse_qs(fieldstring)['prev'][0])
                fieldstring = fieldstring[(fieldstring.find("?")+1):] # everything after '?'
        if self.referersite.find("/") > 0:
            self.referersite = self.referersite[:self.referersite.find("/")] # everything before '/'
        if len(fieldstring) > 0:
            # get a dictionary of all fields encoded in the url
            fielddict = cgi.parse_qs(fieldstring)
            # select the opropriate list of searchfields from the _searchfieldcollection
            searchfields = []
            for searchfields_tuple in self._searchfieldcollection:
                pattern = searchfields_tuple[0]
                if pattern.search(referer):
                    searchfields = searchfields_tuple[1]
                    break # go with the first match
            # go through all fields of the url and see if they are a search
            for (key,value) in fielddict.items():
                if key.lower() in searchfields:
                    self.has_search = True
                    self.searchstring = ensure_unicode(value[0], self.encodings)
                    break
    def _debug(self):
        print "refererstring: '%s'" % self.refererstring
        print "    refererpage  : '%s'" % self.refererpage
        print "    referersite  : '%s'" % self.referersite
        if self.has_search:
            try:
                print "    searchstring : '%s'" % self.searchstring
            except UnicodeEncodeError:
                warn("It seems the output terminal can't handle unicode. Try with latin-1")
                try:
                    print "    searchstring : '%s'" % self.searchstring.encode('latin-1')
                except Exception:
                    warn("Can't convert to latin-1")
        else:
            print "    searchstring : N/A"
        print ""
