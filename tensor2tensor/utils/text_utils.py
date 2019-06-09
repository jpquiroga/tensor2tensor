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

def filter_text_file_pair_lines_by_num_tokens(orig_file_1, orig_file_2, dest_file_1, dest_file_2, max_tokens, tok_separator=" "):
    """
    Remove all lines with a length greater than a a given value from a file 1 and write the same corresponding
    lines of file 2 to a pair of respective destination files.

    :param orig_file_1: Origin file.
    :param orig_file_2: Origin file. With the same number of lines than orig_file_1.
    :param dest_file_1: Destination file.
    :param dest_file_2: Destination file.
    :param max_tokens: Maximum number of tokens.
    :param tok_separator: Separator used for tokenization.
    """
    with open(orig_file_1, "r") as f_r_1:
        with open(orig_file_2, "r") as f_r_2:
            with open(dest_file_1, "w") as f_w_1:
                with open(dest_file_2, "w") as f_w_2:
                    for l_1 in f_r_1:
                        _toks = l_1.strip().split(tok_separator)
                        l_2 = f_r_2.readline()
                        if len(_toks) <= max_tokens:
                            f_w_1.write(l_1)
                            f_w_2.write(l_2)
