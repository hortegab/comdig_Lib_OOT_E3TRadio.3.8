#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class decisor_ff(gr.sync_block):
    """
    Hecho por Homero Ortega Boada, UIS 2017. Entrega como salida 1 si la entrada supera el umbral=0, pero 0 si no lo supera. Tanto la entrada como la salida es un valor de tipo float. Nota: no importa que valor le des a la variable Umbral, se considerará que Umbral = 0
    """
    def __init__(self, Umbral=0):
        gr.sync_block.__init__(self,
            name="decisor_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
#        self.Umbral=Umbral


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
#        out[:] = [float(v>self.Umbral) for v in in0]
        out[:]=numpy.ceil(numpy.clip(in0,0.,1.))
        return len(output_items[0])

