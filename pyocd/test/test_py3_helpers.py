# pyOCD debugger
# Copyright (c) 2019 Arm Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyocd.utility.py3_helpers import (
    PY3,
    iter_single_bytes,
    to_bytes_safe,
    to_str_safe,
)
import pytest
import six

class TestPy3Helpers(object):
    def test_iter_single_bytes_bytes(self):
        i = iter_single_bytes(b"1234")
        assert next(i) == b'1'
        assert next(i) == b'2'
        assert next(i) == b'3'
        assert next(i) == b'4'
    
    def test_to_bytes_safe(self):
        if PY3:
            assert to_bytes_safe(b"hello") == b"hello"
            assert to_bytes_safe("string") == b"string"
        else:
            assert to_bytes_safe(b"hello") == b"hello"
            assert to_bytes_safe("string") == b"string"
            assert to_bytes_safe(u"unicode") == b"unicode"
    
    def test_to_str_safe(self):
        if PY3:
            assert to_str_safe(b"bytes") == "bytes"
            assert to_str_safe("string") == "string"
            assert to_str_safe('System Administrator\u2019s Mouse') == 'System Administrator\u2019s Mouse'
        else:
            assert to_str_safe(b"bytes") == "bytes"
            assert to_str_safe("string") == "string"
            assert to_str_safe(u"string") == "string"
            assert to_str_safe(u'System Administrator\u2019s Mouse') == 'System Administrator\xe2\x80\x99s Mouse'
