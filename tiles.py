from enum import Enum
import os

class Tiles(Enum):
    BLACK_1 = 101
    BLACK_2 = 102
    BLACK_3 = 103
    BLACK_4 = 104
    BLACK_5 = 105
    BLACK_6 = 106
    BLACK_7 = 107
    BLACK_8 = 108
    BLACK_9 = 109
    BLACK_10 = 110
    BLACK_11 = 111
    BLACK_12 = 112
    BLACK_13 = 113
    BLACK_JOKER = 114
    BLUE_1 = 201
    BLUE_2 = 202
    BLUE_3 = 203
    BLUE_4 = 204
    BLUE_5 = 205
    BLUE_6 = 206
    BLUE_7 = 207
    BLUE_8 = 208
    BLUE_9 = 209
    BLUE_10 = 210
    BLUE_11 = 211
    BLUE_12 = 212
    BLUE_13 = 213
    RED_1 = 301
    RED_2 = 302
    RED_3 = 303
    RED_4 = 304
    RED_5 = 305
    RED_6 = 306
    RED_7 = 307
    RED_8 = 308
    RED_9 = 309
    RED_10 = 310
    RED_11 = 311
    RED_12 = 312
    RED_13 = 313
    RED_JOKER = 314
    ORANGE_1 = 401
    ORANGE_2 = 402
    ORANGE_3 = 403
    ORANGE_4 = 404
    ORANGE_5 = 405
    ORANGE_6 = 406
    ORANGE_7 = 407
    ORANGE_8 = 408
    ORANGE_9 = 409
    ORANGE_10 = 410
    ORANGE_11 = 411
    ORANGE_12 = 412
    ORANGE_13 = 413
    #  Game recognition
    GAME_CORNER = 500
    TURN = 501
    PLAYER_TILE = 502
    BOARD_TILE = 503
    TAKE_CARD = 504
    END_TURN = 505
    SORT777_BUTTON = 510
    EMPTY_SPACE =  600
    @property
    def image(self) -> "Image":
        return os.path.abspath('t/' + getattr(Image, self.name).value)

class Image(Enum):
    BLACK_1 = "1_bk_l.png"
    BLACK_2 = "2_bk_l.png"
    BLACK_3 = "3_bk_l.png"
    BLACK_4 = "4_bk_l.png"
    BLACK_5 = "5_bk_l.png"
    BLACK_6 = "6_bk_l.png"
    BLACK_7 = "7_bk_l.png"
    BLACK_8 = "8_bk_l.png"
    BLACK_9 = "9_bk_l.png"
    BLACK_10 = "10_bk_l.png"
    BLACK_11 = "11_bk_l.png"
    BLACK_12 = "12_bk_l.png"
    BLACK_13 = "13_bk_l.png"
    BLACK_JOKER = "j_bk_l.png"
    BLUE_1 = "1_be_l.png"
    BLUE_2 = "2_be_l.png"
    BLUE_3 = "3_be_l.png"
    BLUE_4 = "4_be_l.png"
    BLUE_5 = "5_be_l.png"
    BLUE_6 = "6_be_l.png"
    BLUE_7 = "7_be_l.png"
    BLUE_8 = "8_be_l.png"
    BLUE_9 = "9_be_l.png"
    BLUE_10 = "10_be_l.png"
    BLUE_11 = "11_be_l.png"
    BLUE_12 = "12_be_l.png"
    BLUE_13 = "13_be_l.png"
    RED_1 = "1_rd_l.png"
    RED_2 = "2_rd_l.png"
    RED_3 = "3_rd_l.png"
    RED_4 = "4_rd_l.png"
    RED_5 = "5_rd_l.png"
    RED_6 = "6_rd_l.png"
    RED_7 = "7_rd_l.png"
    RED_8 = "8_rd_l.png"
    RED_9 = "9_rd_l.png"
    RED_10 = "10_rd_l.png"
    RED_11 = "11_rd_l.png"
    RED_12 = "12_rd_l.png"
    RED_13 = "13_rd_l.png"
    RED_JOKER = "j_rd_l.png"
    ORANGE_1 = "1_oe_l.png"
    ORANGE_2 = "2_oe_l.png"
    ORANGE_3 = "3_oe_l.png"
    ORANGE_4 = "4_oe_l.png"
    ORANGE_5 = "5_oe_l.png"
    ORANGE_6 = "6_oe_l.png"
    ORANGE_7 = "7_oe_l.png"
    ORANGE_8 = "8_oe_l.png"
    ORANGE_9 = "9_oe_l.png"
    ORANGE_10 = "10_oe_l.png"
    ORANGE_11 = "11_oe_l.png"
    ORANGE_12 = "12_oe_l.png"
    ORANGE_13 = "13_oe_l.png"
    GAME_CORNER = "game_corner.png"
    TURN = "turn.png"
    PLAYER_TILE = "player_tile.png"
    BOARD_TILE = "board_tile.png"
    TAKE_CARD = "take_card.png"
    END_TURN = "end_turn.png"
    SORT777_BUTTON = "sort777.png"
    EMPTY_SPACE = "empty_space.png"