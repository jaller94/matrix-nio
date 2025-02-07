# -*- coding: utf-8 -*-

# Copyright © 2019 Damir Jelić <poljar@termina.org.uk>
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
# RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
# CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import sys

if sys.version_info >= (3, 5):
    from importlib import util

    # The imp module is deprecated by importlib but importlib doesn't have the
    # find_spec function on python2. Use the imp module for py2 until we
    # deprecate python2 support.

    def package_installed(package_name):
        spec = util.find_spec(package_name)

        if spec is None:
            return False
        return True

else:
    import imp

    def package_installed(package_name):
        try:
            imp.find_module(package_name)
            return True
        except ImportError:
            return False
