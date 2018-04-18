#! python
import os
import sys
import shutil

# exe path
exe_path = R'C:\Program Files (x86)\Steam\SteamApps\common\Heroes of Might and Magic 5 Tribes of the East\bin'
pak_path = R'C:\Program Files (x86)\Steam\SteamApps\common\Heroes of Might and Magic 5 Tribes of the East\data'
shortcut_path = R'C:' + os.environ["HOMEPATH"] + R'\Desktop'

# access current working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# variables for use in source portion of shutil
exe_src = __location__ + R"\H5_Game.NCF_pest.exe"
pak_src = __location__ + R"\NCF__Core.pak"
shortcut_src = __location__ + R"\HOMMV.lnk"


# functions containing all the logic
def copy_func_exe():
    try:
        shutil.copy(exe_src, exe_path)
        print("Passed exe_path copying")
    except:
        e = sys.exc_info()[0]
        print("Exception: " + str(e))


def copy_func_pak():
    try:
        shutil.copy(pak_src, pak_path)
        print("Passed pak_path copying")
    except:
        e = sys.exc_info()[0]
        print("Exception: " + str(e))


def copy_shortcut():
    try:
        shutil.copy(shortcut_src, shortcut_path)
        print("Passed shortcut_path copying")
    except:
        e = sys.exc_info()[0]
        print("Exception: " + str(e))


# downloads and executes hamachi installer
def fetch_network_tool():
    import urllib.request

    if os.path.isfile("hamachi.msi") == True:
        return

    print("Downloading Hamachi...")
    target = "https://secure.logmein.com/hamachi.msi"

    with urllib.request.urlopen(target) as response, open('hamachi.msi',
                                                          'wb') as out:
        shutil.copyfileobj(response, out)


if __name__ == '__main__':
    # debug print statements
    print("Location: " + __location__)
    print("Exe path: " + exe_path)
    print("Exe Source: " + exe_src)
    print("Pak path: " + pak_path)
    print("Pak Source: " + pak_src)
    print("Shortcut path: " + shortcut_path)
    print("Shortcut Source: " + shortcut_src)
    # actual calling order
    copy_func_exe()
    copy_func_pak()
    copy_shortcut()
    fetch_network_tool()
    os.system("hamachi.msi")