#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2021 Grant Rettke <grant@wisdomandwonder.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
from inkex import EffectExtension, TextElement


#
# Add multiple characters.
#
class AddChars(EffectExtension):

    def add_arguments(self, p):
        return

    def effect(self):
        chars = ['A', 'B']
        layer = self.svg.get_current_layer()
        for idx,text in enumerate(chars):
            y_idx = idx * 5
            char = TextElement('0', str(y_idx))
            char.text = text
            layer.add(char)

if __name__ == '__main__':
    AddChars().run()
