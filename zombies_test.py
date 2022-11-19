import pytest
from zombies import (
    Arena, Zombie, CleverMan, 
    ZOMBIE, HUMAN,
    get_closest_character, generate_adjacent_coords, 
)


@pytest.fixture()
def arena():
    arena = Arena(19, 19, 16)
    arena.characters.append(Zombie(5, 5))
    return arena


def test_get_closest_character(arena):
    closest_char, closest_char_index, closest_char_distance = get_closest_character((1, 1), ZOMBIE, arena)
    assert closest_char.column == 5
    assert closest_char.row == 5
    assert closest_char_index == 0
    assert closest_char_distance == 32**0.5


def test_generate_adjacent_coords(arena):
    adj_coords = generate_adjacent_coords((1, 1), 2, arena)
    print(adj_coords)
    assert adj_coords == {
        (0, 0): (0, 0), (0, 1): (0, 1), (0, 2): (0, 3), 
        (1, 0): (1, 0), (1, 1): (1, 1), (1, 2): (1, 3), 
        (2, 0): (3, 0), (2, 1): (3, 1), (2, 2): (3, 3)
    }


def test_clever_man_strategy(arena):
    clever_man = CleverMan(3, 3)
    assert clever_man.sprite.rect.x == 148
    assert clever_man.sprite.rect.y == 148

    clever_man.strategy(arena)

    assert clever_man.column == 2
    assert clever_man.row == 2
    assert clever_man.sprite.rect.x == 132
    assert clever_man.sprite.rect.y == 132

