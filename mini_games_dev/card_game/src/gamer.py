# -*- coding: utf-8 -*-

from cart import *


class Gamer:
    """Представляет игрока с именем, очками и десятком карт"""

    def __init__( self, name ):
        """Инициализирует новый экземпляр"""
        assert( isinstance( name, str ))
        self.name = name
        self.points = 0
        self.carts = [Cart() for x in range(10)]

    def pop( self ):
        """Выталкивает и возвращает карту"""
        result = self.carts.pop()
        print( f"карта {self.name}: {result}." )
        return result

    def add_point( self ):
        """Добавляет одно очко"""
        print( f"{self.name} получил очко." )
        self.points += 1
