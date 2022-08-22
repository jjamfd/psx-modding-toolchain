import os
import shutil

def warning() -> None:
    print("[Plugin] WARNING: ctr-tools not found. Please download the tools from https://github.com/CTR-tools/CTR-tools/releases")
    print("rename the folder to ctr-tools and put it in Example_CrashTeamRacing/plugins/")

def extract(plugin_path: str, game_path: str) -> None:
    if os.path.isdir(plugin_path + "ctr-tools"):
        os.system(plugin_path + "ctr-tools/bigtool.exe " + game_path + "BIGFILE.BIG")
    else:
        warning()

def build(plugin_path: str, game_path: str) -> None:
    if os.path.isdir(plugin_path + "ctr-tools"):
        bigpath = os.getcwd() + "/bigfile"
        shutil.copytree(game_path + "bigfile", bigpath)
        os.system(plugin_path + "ctr-tools/bigtool.exe " + game_path + "bigfile.txt")
        shutil.rmtree(bigpath)
    else:
        warning()