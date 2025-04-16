# -*- coding: utf-8 -*-

import os

from game import *


def main():
    """точка входа"""
    print( 'Карточная игра' )
    name1 = os.getlogin()
    name2 = "bot"
    game = Game( name1, name2 )
    game.run()


def query_name_gamer( message ):
    """запрашивает имя игрока"""
    print( message )
    while True:
        result = input( )
        if len( result ) > 0:
            return result


if __name__ == "__main__":
    main()
