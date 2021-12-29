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
        layer = self.svg.get_current_layer()
        element = TextElement('0', '0')
        element.text = 'Hello, world.'
        layer.add(element)

if __name__ == '__main__':
    AddChars().run()
