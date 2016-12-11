#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  verbdict_functions.py
#  
#  Copyright 2016 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import pyarabic.araby as araby
   
def decode_tenses(field):
    """
    Decode tenses field
    """
    all=False;
    past=False;
    future=False;
    passive=False;
    imperative=False;
    future_moode=False;
    confirmed=False;
    if field==u"يعملان":
        all=True;
    else:
        if field.find(araby.YEH)>=0:
            past=True;
        if field.find(araby.AIN)>=0:
            future=True;
        if field.find(araby.MEEM)>=0:
            imperative=True;
        if field.find(araby.LAM)>=0:
            passive=True;
        if field.find(araby.ALEF)>=0:
            future_moode=True;
        if field.find(araby.NOON)>=0:
            confirmed=True;
    return (all, past, future, passive, imperative, future_moode, confirmed);
    

    


