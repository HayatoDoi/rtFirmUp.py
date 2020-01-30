#!/usr/bin/env python3
# python3 -m pip install tftpy
import tftpy
import time, os
from concurrent import futures

FIRM_PATH: str = "./rtx830.bin"
IP_LIST_PATH: str = "./ip.list"
MAX_WORKER: int = 4

def main():
    # IPアドレスリストの読み込み
    with open(IP_LIST_PATH, "r") as f:
        ipList = f.read()

    # 並列処理でファームアップを行う
    future_list: list = []
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKER) as executor:
        for ip in ipList.splitlines():
            future = executor.submit(fn=rtFirmUp, ip=ip, _from=FIRM_PATH,  _to="exec")
            future_list.append(future)
    futures.as_completed(fs=future_list)

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