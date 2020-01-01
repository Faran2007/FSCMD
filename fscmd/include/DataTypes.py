"""
 (C) Copyright 2019 Faran, All Rights Reserved
  
 DataTypes.py included module for fscmd
  - null, boolean and others
  
"""

" *null object* "
class null():
    def __init__(self):
        self.Active = True
        self.isNull = True
    def __str__(self):
        return 'null'
    def __repr__(self):
        return 'null'