import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import sys 

class hit:
    """Classe hit"""
    def __init__(self, a, b ,c):
        self.id_modulo = a
        self.id_Sensore = b
        self.Time_Stamp_rivelazione = c
    
    def __lt__(self, other):
        if self.Time_Stamp_rivelazione < other.Time_Stamp_rivelazione:
            return True
        if self.Time_Stamp_rivelazione ==other.Time_Stamp_rivelazione:
            if self.id_modulo < other.id_modulo:
                return True
            if self.id_modulo == other.id_modulo:
                if self.id_Sensore <= other.id_Sensore:
                    return True
            else:
                return False
        else:
            return False

    def __add__(self,other):
        return self.Time_Stamp_rivelazione+other.Time_Stamp_rivelazione
    def __sub__(self,other):
        return self.Time_Stamp_rivelazione-other.Time_Stamp_rivelazione
    
    

        