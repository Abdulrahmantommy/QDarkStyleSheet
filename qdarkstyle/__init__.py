# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) <2013> <Colin Duquesnoy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""
Initialise the QDarkStyleSheet module when used with python.

This modules provides a function to transparently load the stylesheets
with the correct rc file.
"""
import os


def load_stylesheet(pyside=True):
    """
    Loads the stylesheet. Takes care of importing the rc module.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    cwd = os.path.dirname(os.path.realpath(__file__))
    # Smart import of the rc file
    if pyside:
        import pyside_style_rc
    else:
        import pyqt_style_rc

    # Load the stylesheet content
    ret_val = ""
    filename = os.path.join(cwd, "style.qss")
    with open(os.path.join(__file__, filename)) as stylesheet:
        ret_val = stylesheet.read()
    return ret_val
