# -*- coding: utf-8 -*-

from gamer import *
from round import *


class Game:
    """Представляет игру"""

    def __init__( self, name1, name2 ):
        """инициализирует новый экземпляр"""
        assert( isinstance( name1, str ))
        assert( isinstance( name2, str ))
        self.gamer1 = Gamer( name1 )
        self.gamer2 = Gamer( name2 )

    def run( self ):
        """запускает игру"""
        self.start()
        round = Round( self.gamer1, self.gamer2 )
        for number in range( 1, 11 ):
            if round.run( number ):
                break
        self.stop()

    def start( self ):
        """начинает"""
        print( f"Играют: {self.gamer1.name} и {self.gamer2.name}." )

    def stop( self ):
        """заканчивает"""
        print( '' )
        print( '=== игра завершена ===' )
        self.out_points( self.gamer1 )
        self.out_points( self.gamer2 )
        self.detect_winner()

    def detect_winner( self ):
        """определяет победителя"""
        if self.out_winner( self.gamer1, self.gamer2 ):
            return
        if self.out_winner( self.gamer2, self.gamer1 ):
            return
        self.out_draw()

    @staticmethod
    def out_points( gamer ):
        """выводит отчёт о набраных очках"""
        assert( isinstance( gamer, Gamer ))
        print( f"У {gamer.name} {gamer.points} очков." )

    @staticmethod
    def out_winner( gamer1, gamer2 ):
        """выводит победителя"""
        assert( isinstance( gamer1, Gamer ))
        assert( isinstance( gamer2, Gamer ))
        distance = gamer1.points - gamer2.points
        if distance <= 0:
            return False
        print( f"Победил {gamer1.name} с разницой в {distance} очков." )
        return True

    @staticmethod
    def out_draw():
        """выводит победителя"""
        print( 'Ничья.' )
