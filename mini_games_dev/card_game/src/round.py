# -*- coding: utf-8 -*-

from gamer import *


class Round:
    """Представляет раунд игры"""

    def __init__( self, gamer1, gamer2 ):
        """инициализирует новый экземпляр"""
        assert( isinstance( gamer1, Gamer ))
        assert( isinstance( gamer2, Gamer ))
        self.gamer1 = gamer1
        self.gamer2 = gamer2
        self.mode = 0

    def run( self, number ):
        """Запускает раунд"""
        assert( isinstance( number, int ))
        print( f"\n=== Раунд {number} (сравнение {Cart.heads[self.mode]}) ===\n" )
        cart1 = self.gamer1.pop()
        cart2 = self.gamer2.pop()
        self.report( Cart.compare( self.mode, cart1, cart2 ) )
        self.rotate_mode()
        return self.is_ahead()

    def report( self, value ):
        """отчитывается о промежуточных результатах"""
        assert( isinstance( value, int ))
        if value > 0:
            self.gamer1.add_point()
            return
        if value < 0:
            self.gamer2.add_point()
            return
        print( "ничья" )

    def rotate_mode( self ):
        """Меняет по кругу режим сравнения"""
        if self.mode == 2:
            self.mode = 0
        else:
            self.mode += 1

    def is_ahead( self ):
        """Проверка опережения"""
        diff = abs( self.gamer1.points - self.gamer2.points )
        return diff > len( self.gamer1.carts )
