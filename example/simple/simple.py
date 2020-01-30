#!/usr/bin/env python3
# python3 -m pip install tftpy
import tftpy
import os

def main():
    rtFirmUp("192.168.100.1", "./rtx830.bin", "exec")

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