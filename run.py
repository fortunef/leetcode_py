# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.dirname(os.getcwd()))
from solution import uncommonFromSentences


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = uncommonFromSentences.Solution()
        res = obj.uncommonFromSentences("xfj vcahm vcahm frkqt oibcc jko oibcc frkqt ft tr", "lv ktx ktx tr x xfj xfj frkqt ktx ta tr yynk vcahm")
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
