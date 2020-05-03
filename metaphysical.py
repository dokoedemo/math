# 形而上クラス

## インポート

## クラス定義

### コミュニティー
class Community:
    leader
    player_set

    def __init__(self, leader: Player, player_set):

    def choose_player():

    def get_player():

    def loose_player():

    def is_empty():

### イベント
class GameEvent:
    game
    commu1
    commu2
    battle_count
    MAX_BATTLE_COUNT = 1000
    go_on

    def __init__(self,game: Game, community1: Community, community2: Community):
        self.game = game
        self.commu1 = community1
        self.commu2 = community2
        battle_count = 0
        go_on = True

    def operate(): """イベント運営"""
        while go_on:
            choose_player() """選手選択"""
            battle() """試合実施"""
            battle_count+=1 """試合数インクリメント"""
            if battle_count >= MAX_BATTLE_COUNT
                print("event is force-quit.")
                break
            clean_up()
        else:
            print("event finishes..")
        return battle_count

    def choose_player():

    def battle():

    def clean_up():

