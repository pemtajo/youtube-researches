#!/usr/bin/python3
# coding=UTF-8

from aiqdoctests.structures import AiqTest


class tests(AiqTest):
    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.setStructure("health")

    def test_health(self):
        r = self.assertOK()
        self.assertEqual("Hello World!", r.json())
