import os, sys, time, hashlib
import pygetwindow
import pyautogui
from shutil import copyfile

MINS_BETWEEN_SAVES = 3

save_target = "default_save_target"

if len(sys.argv) > 1:
    save_target = sys.argv[1]

out_file_path = f"E:\\gb\\{save_target}"

saves_path = os.path.join(
    os.environ["USERPROFILE"],
    "Documents",
    "Paradox Interactive",
    "Europa Universalis IV",
    "save games",
)
src_file = os.path.join(saves_path, f"{save_target}_backup.eu4")


def takeScreenShot(ss_path):
    title = "Europa Universalis IV"
    pygetwindow.getWindowsWithTitle(title)[0]
    p = pyautogui.screenshot()
    p.save(ss_path)


if not os.path.exists(out_file_path):
    os.mkdir(out_file_path)

lastHash = None

while True:
    ts = time.strftime("%m_%d-%H_%M")
    dst_file = os.path.join(out_file_path, f"{save_target}_{ts}.eu4")
    try:
        copyfile(src_file, dst_file)
        print(f"{ts}: Copied - {dst_file}")

        with open(dst_file, "rb") as dst_file_bits:
            currentHash = hashlib.md5(dst_file_bits.read()).hexdigest()
            print(f"\tcurHash = {currentHash}")

        print(f"\tlastHash = {lastHash}")
        if lastHash == currentHash:
            os.remove(dst_file)
            print(f"\tRemoved duplicate - {dst_file}")
        else:
            lastHash = currentHash
            ss_path = os.path.join(out_file_path, f"{save_target}_{ts}.png")
            takeScreenShot(ss_path)
            print(f"\tCopied new save - {dst_file}")
    except Exception as ex:
        print(f"Failed to copy - {ex}")
    time.sleep(60 * MINS_BETWEEN_SAVES)
