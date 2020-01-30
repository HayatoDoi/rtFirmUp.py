# rtFirmUp.py
ヤマハルーターをpythonからtftp経由でファームアップさせる  
本レポジトリはtftpyを使用したファームアップスクリプトの例である  
ライブラリではないので注意すること  

```python
# rtFirmUp: ヤマハルーターのファームアップを行う
# @ip     ルーターのIPアドレス
# @_from  ファームの場所
# @_to    ファームの書き込む場所(exec. exec0, exec1, ..)
def rtFirmUp(ip: str, _from: str, _to: str):
    tClient = tftpy.TftpClient(ip)
    _from = os.path.basename(_from)
    tClient.upload(_to, _from)
```

## ルーターコンフィング
以下のコンフィグが入っている必要がある
```
tftp hosy lan1
```

## 準備
下記コマンドでtftpyをインストールする
```bash
python -m pip install tftpy
```

## 使い方
- シンプルな使い方
    - [rtFirmUp.py](https://github.com/HayatoDoi/rtFirmUp.py/blob/master/rtFirmUp.py) 参照
- シングルスレッドで一括ファームアップを行う
    - ネットワークに負荷をかけたくない時に有効
    - アップデート台数が多い時、実行時間が長くなるため注意が必要
    - [example/mass_update](https://github.com/HayatoDoi/rtFirmUp.py/tree/master/example/mass_update) 参照
- マルチスレッドで一括ファームアップを行う
    - 高速にファームアップを行いたい時に有効
    - ネットワークに負荷がかかるため注意が必要
    - [example/mass_update_parallel](https://github.com/HayatoDoi/rtFirmUp.py/tree/master/example/mass_update_parallel) 参照
