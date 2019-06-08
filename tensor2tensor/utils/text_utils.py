# coding=utf-8
# author: jpquiroga@gmail.com
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

"""
Text processing utils.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def truncate_text_by_num_tokens(text, max_tokens, tok_separator=" "):
    """
    Truncate a text to left a maximum number of tokens.

    :param text:
    :param max_tokens:
    :param tok_separator:
    :return: The truncated text.
    """
    _toks = text.split(tok_separator)
    return tok_separator.join(_toks[:min(max_tokens, len(_toks))])

def truncate_text_file_by_num_tokens(orig_file, dest_file, max_tokens, tok_separator=" "):
    """
    Truncate all the lines of a text file to a maximum number of tokens.

    :param orig_file: Origin file.
    :param dest_file: Destination file.
    :param max_tokens: Maximum number of tokens.
    :param tok_separator:
    """
    with open(orig_file, "r") as f_r:
        with open(dest_file, "w") as f_w:
            for l in f_r:
                f_w.write(truncate_text_by_num_tokens(l, max_tokens=max_tokens, tok_separator=tok_separator))


def filter_text_file_lines_by_num_tokens(orig_file, dest_file, max_tokens, tok_separator=" "):
    """
    Remove all lines with a length greater than a a given value.

    :param orig_file: Origin file.
    :param dest_file: Destination file.
    :param max_tokens: Maximum number of tokens.
    :param tok_separator: Separator used for tokenization.
    """
    with open(orig_file, "r") as f_r:
        with open(dest_file, "w") as f_w:
            for l in f_r:
                _toks = l.strip().split(tok_separator)
                if len(_toks) <= max_tokens:
                    f_w.write(l)
