# 形而下クラス

## インポート
from numpy.random import *

## クラス定義

### プレーヤー
class Player:
    bp """強さ"""
    is_loose """勝負の状態"""
    is_robbed """強奪されたか否か"""

    def __init__(self, bp):
        if bp < 1: """bpの最低値は1とする"""
            self.bp = 1
        else
            self.bp = bp
        self.is_loose = False
        self.is_robbed = False

    def is_loose(): """負け状態を確認する"""
        return is_loose

    def set_loose(): """負け状態にする"""
        is_loose = True

    def clean_up(): """リセット処理"""
        is_loose = False

    def is_robbed(): """強奪状態を確認する"""
        return is_robbed

    def set_robbed(): """強奪状態にする"""
        is_robbed = True

### ゲーム
class Game:
    winner
    looser
    def set_player(player1: Player, player2: Player):
        threshold = player1.bp / (playre1.bp + player2.bp)
        if rand() < threshold:
            winner = player1
            player2.set_loose()
            looser = player2
        else
            winner = player2
            player1.set_loose()
            looser = player1

    def get_winner():
        return winner

    def get_looser():
        return looser
