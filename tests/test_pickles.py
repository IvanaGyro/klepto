#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2013-2016 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/klepto/LICENSE

import dill
import klepto

@klepto.lru_cache()
def squared(x):
    return x**2

squared(2)
squared(4)
squared(6)

_s = dill.loads(dill.dumps(squared))
assert _s.lookup(4) == 16
assert squared.__cache__() == _s.__cache__()

