from pathlib import Path
from data import Mod
from data import Game
import filecmp
import os, shutil
import vext


def read_path(filename) -> Path:
    try:
        file = open(f"{filename}.txt", "r")
    except FileNotFoundError:
        return Path("")

    return Path(file.read())


def write_path(filename: str, path: Path):
    file = open(f"{filename}.txt", "w")
    file.write(str(path))


def define_path(filename, visual_name) -> Path:
    user_input = str(input(f"Enter {visual_name} folder: "))
    if '"' in user_input:
        user_input = user_input[1:-1]
    write_path(filename, Path(user_input))
    path = read_path(filename)
    print("path is defined as:", path)
    return path


def repl():
    mlc_path = read_path("mlcpath")
    if mlc_path == "":
        mlc_path = define_path("mlcpath", "mlc01")

    mod_path = read_path("modpath")
    if mod_path == "":
        mod_path = define_path("modpath", "mod")

    print("Enter a number to choose an option")
    print("1: define mlc01 directory")
    print("2: define mod directory")
    print("3: scan games")
    print("4: quit")

    choice = input()
    mods = []

    if choice == "1":
        mlc_path = define_path("mlcpath", "mlc01")
    elif choice == "2":
        mod_path = define_path("modpath", "mod")
    elif choice == "3":
        mods = scan_mods(mod_path)
        games = scan_games(mlc_path, mods)
    elif choice == "4":
        exit()

    print()


def scan_games(mlc_path, mods):
    games_path = mlc_path.joinpath("usr/title")
    games = []

    for directory, subdirectories, filenames in os.walk(str(games_path)):
        for filename in filenames:
            if ".rpx" in filename:
                # print(filename, "in", directory)
                games.append(Game(Path(filename).stem, Path(directory).parent, []))

    for game in games:
        for mod in mods:
            dir_cmp = filecmp.dircmp(game.path.joinpath("content"), mod.path)
            for subdir_cmp in dir_cmp.subdirs.values():
                if subdir_cmp.common_files and mod not in game.mods:
                    game.mods.append(mod)

        print(game.mods)

    return games


def scan_mods(mod_path: Path):
    mods = []
    for directory, subdirectories, filenames in os.walk(str(mod_path)):

        if "Model" in subdirectories or "Pack" in subdirectories:
            mods.append(Mod(Path(directory).name, Path(directory), False, False))

        for filename in filenames:
            for mod in mods:
                if str(mod.path) in directory:
                    if ".sbfres" in filename:
                        mod.has_models = True
                    if ".pack" in filename:
                        mod.has_pack = True

    mods = [mod for mod in mods if (mod.has_models or mod.has_pack)]
    return mods


repl()
while True:
    repl()
