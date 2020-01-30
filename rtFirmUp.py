#!/usr/bin/env python3
# File Name: rtFirmUp.py
# Description: ヤマハルーターをpythonからtftp経由でファームアップさせる
#
# 下記のコマンドでtftpyをインストールする必要がある
# python3 -m pip install tftpy
import tftpy
import os, sys, re

VERSION: str = "1.0"
COPYRIGHT: str = "(c) 2020, Hayato Doi."

def main():
    args = sys.argv
    # helpの表示
    if len(args) == 2 and args[1] == "--help":
        printHelp()
        sys.exit(0)
    # versionの表示
    if len(args) == 2 and args[1] == "--version":
        printVersion()
        sys.exit(0)
    # copyrightの表示
    if len(args) == 2 and args[1] == "--copyright":
        printCopyright()
        sys.exit(0)
    # 引数エラー
    if len(args) != 4:
        printArgumentError()
        sys.exit(1)

    rtFirmUp(args[1], args[2], args[3])

def printHelp():
    msg = """\
rtFirmUp.py [option] <ip address or domain> <firmware path> <fitmware no>
[option]
--help      : show help
--version   : show version
--copyright : show copyright\
"""
    print(msg)

def printVersion():
    msg = """\
rtFirmUp v{version}
{copyright}\
""".format(version=VERSION, copyright=COPYRIGHT)
    print(msg)

def printCopyright():
    msg = """\
{copyright}\
""".format(copyright=COPYRIGHT)
    print(msg)

def printArgumentError():
    msg = """\
Argument is incorrect.
Try `rtFirmUp.py --help' for information.\
"""
    print(msg)

# rtFirmUp: ヤマハルーターのファームアップを行う
# @ip     ルーターのIPアドレス
# @_from  ファームの場所
# @_to    ファームの書き込む場所(exec. exec0, exec1, ..)
def rtFirmUp(ip: str, _from: str, _to: str):
    tClient = tftpy.TftpClient(ip)
    _from = os.path.basename(_from)
    tClient.upload(_to, _from)

if __name__ == "__main__":
    main()
