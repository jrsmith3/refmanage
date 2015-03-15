# -*- coding: utf-8 -*-

class UnparseableBibtexError(Exception):
    """
    Raised when BibTeX parsing fails
    """
    pass

class ParseableBibtexError(Exception):
    """
    Raised when BibTeX parsing succeeds when it should fail
    """
    pass
