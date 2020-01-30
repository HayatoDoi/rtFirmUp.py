#!/usr/bin/env python3
# python3 -m pip install tftpy
import tftpy
import time, os

FIRM_PATH: str = "./rtx830.bin"
IP_LIST_PATH: str = "./ip.list"
INTERVAL: int = 1

def main():
    # IPアドレスリストの読み込み
    with open(IP_LIST_PATH, "r") as f:
        ipList = f.read()

    # 並列処理でファームアップを行う
    for ip in ipList.splitlines():
        rtFirmUp(ip, FIRM_PATH, "exec")
        time.sleep(INTERVAL)

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