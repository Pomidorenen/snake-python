from pygame.locals import *

Rgb = tuple[int, int, int]
Point = tuple[int, int]
Size = tuple[int, int]


class Tile(object):
    def __init__(self, color: Rgb, position: Point, size: Size, name: str) -> None:
        self.name = name
        self.rect = Rect(position[0], position[1], size[0], size[1])
        self.color = color


def get_tile_size_relative_to_screen(tile_map: list[str], width: int, height: int) -> tuple[int, int]:
    size_y = height / len(tile_map)
    max_length = 0
    for i in range(len(tile_map)):
        if len(tile_map[i]) > max_length:
            max_length = len(tile_map[i])
    size_x = width / max_length
    return int(size_x), int(size_y)


def create_tiles(tile_map: list[str], width: int, height: int, tile_dict_setting: dict) -> list[Tile]:
    size = get_tile_size_relative_to_screen(tile_map, width, height)
    tiles: list = []
    for y in range(len(tile_map)):
        for x in range(len(tile_map[y])):
            color = tile_dict_setting[tile_map[y][x]]["color"]
            name = tile_dict_setting[tile_map[y][x]]["name"]
            position = (x * size[0], y * size[1])
            tiles.append(Tile(color, position, size, name))
    return tiles
