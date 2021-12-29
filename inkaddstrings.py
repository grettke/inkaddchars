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
from inkex import EffectExtension, Group, Style, TextElement


#
# Add multiple characters.
#
class AddStrings(EffectExtension):

    def add_arguments(self, p):
        # The INX file is the authoritative source of this information:
        # keep *that* current /then/ update it _here_.
        p.add_argument("--strings", type=str, default="AB,CD,EF",
                       help="Comma-separated list of strings.")
        p.add_argument("--fontsize", type=int, default=12,
                       help="Font size in points.")

    def effect(self):
        o = self.options
        data = o.strings.split(',')
        s = self.svg
        group = s.get_current_layer().add(
            Group.new(s.get_unique_id('AddStrings:')))
        for index,datum in enumerate(data):
            textelement = group.add(TextElement())
            textelement.style = Style()
            textelement.style["font-size"] = s.unittouu(
                str(o.fontsize) + "pt")
            textelement.text = datum


if __name__ == '__main__':
    AddStrings().run()
