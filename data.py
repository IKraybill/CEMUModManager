from dataclasses import dataclass
from pathlib import Path


@dataclass
class Mod:

    name: str
    path: Path
    has_models: bool
    has_pack: bool


@dataclass()
class Game:

    name: str
    path: Path
    mods: list


game_index = {
    "Zelda.rpx": "The Legend of Zelda"
}
