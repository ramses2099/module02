import os
import subprocess as subp


def main():
    print("env path :" + os.environ.get("PATH"))
    # ? subp.run(["date"]) no working in windows
    os.system("cmd /k date")


if __name__ == "__main__":
    main()
# main
