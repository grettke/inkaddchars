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
from inkex import AbortExtension, EffectExtension, Group, TextElement, Tspan


#
# Add multiple strings.
#
class AddStrings(EffectExtension):

    def add_arguments(self, p):
        # The INX file is the authoritative source of this information:
        # keep *that* current /then/ update it _here_.
        p.add_argument("--strings", type=str, default="AB,CD,EF",
                       help="Comma-separated list of strings.")

    def effect(self):
        # Aliases
        o = self.options
        s = self.svg

        # Objects
        template = s.selected.first()
        strings = o.strings.split(',')

        # Precondition Checks
        #
        # Is something selected?
        if template is None:
            raise AbortExtension(
                "Would you please select a TextElement "
                "to serve as the template for inserting "
                "strings and rerun me?")
        # Is it a TextElement?
        if not isinstance(template, TextElement):
            raise AbortExtension(
                "It looks like you selected something, "
                "but it isn't a TextElement. Would you "
                "please select a TextElement object and "
                "rerun me?")

        # Keep the layer tidy by adding the duplicates to a new
        # group on each run.
        group = s.get_current_layer().add(
            Group.new(s.get_unique_id('AddStrings:')))

        # Functionality
        for index, string in enumerate(strings):
            element = template.copy()
            element.text = string
            group.add(element)


if __name__ == '__main__':
    AddStrings().run()
