# -*- coding: utf-8 -*-

import random


class Cart:
    """Представляет игровую карту с тремя значениями"""

    heads = [ "смелость", "безумие", "загадочность" ]

    def __init__( self ):
        """Инициализирует новый экземпляр"""
        self.values = [ random.randint(1, 10) for x in range(3)]

    def __str__( self ):
        """возвращает строковое представление экземпляра"""
        return f"{Cart.heads[0]} {self.values[0]}\t{Cart.heads[1]} {self.values[1]}\t{Cart.heads[2]} {self.values[2]}"

    @staticmethod
    def compare( index, left, right ):
        """Сравнивает поля с указанным индексом в левом и правом экземпляре"""
        assert( isinstance( index, int ))
        assert( isinstance( left, Cart ))
        assert( isinstance( right, Cart ))
        return Cart._compare( left.values[index], right.values[index] )

    @staticmethod
    def _compare( left, right ):
        """Сравнивает левое и правое число"""
        assert( isinstance( left, int ))
        assert( isinstance( right, int ))
        if left < right:
            return -1
        if left > right:
            return +1
        return 0
