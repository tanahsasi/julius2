# -*- coding: utf-8 -*-
import pk
import pt
import ps
import pd
import subprocess
import socket
import time
import picamera
import subprocess
import jtalk
import random

host = 'localhost'
port = 10500
i = 2

# Juliusに接続する準備
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
res = ''
while True:
    if i == 1:
        break
    # 音声認識の区切りである「改行+.」がくるまで待つ
    while (res.find('\n.') == -1):
        # Juliusから取得した値を格納していく
        res += sock.recv(1024).decode()
        if i == 1:
            break
    word = ''
    for line in res.split('\n'):
        if i == 1:
            break
        # Juliusから取得した値から認識文字列の行を探す
        index = line.find('WORD=')
        # 認識文字列があったら...
        if index != -1:
            # 認識文字列部分だけを抜き取る
            line = line[index + 6 : line.find('"', index + 6)]
            # 文字列の開始記号以外を格納していく
            if line != '[s]':
                word = word + line
                print(word)
        res = ''
        
        if word == 'おっけいごみばこ':
            print('返答：ごようはなんでしょうか')
            jtalk.jtalk(u'ごようはなんでしょうか')
            time.sleep(4)
            while True:
                if i == 1:
                    break
                while (res.find('\n.') == -1):
                    # Juliusから取得した値を格納していく
                    res += sock.recv(1024).decode()
                    if i == 1:
                        break

                word = ''
                for line in res.split('\n'):
                    if i == 1:
                        break
                    # Juliusから取得した値から認識文字列の行を探す
                    index = line.find('WORD=')
                    # 認識文字列があったら...
                    if index != -1:
                        # 認識文字列部分だけを抜き取る
                        line = line[index + 6 : line.find('"', index + 6)]
                        # 文字列の開始記号以外を格納していく
                        if line != '[s]':
                            word = word + line
                            print(word)
                        # 文字列を認識したら...
                    if word == 'おはよう':
                        
                        morning_word = [u'おはよう', u'おはようございます',u'ごきげんよう']
                        jtalk.jtalk(random.choice(morning_word))
                        print('返答：' )
                        time.sleep(4)
                    elif word == 'じこしょうかいをして':
                        jtalk.jtalk(u'はい、わかりました。　私はの名前はごみ箱　あなたの生活をサポートします。')
                        time.sleep(4)
                    elif word == 'まわって':
                        jtalk.jtalk(u'まわります')
                        pk.main()
                        subprocess.call(['./upload.sh'])
                        time.sleep(4)
                    elif word == 'とまって':
                        jtalk.jtalk(u'止まります')
                        pt.main()
                        subprocess.call(['./upload.sh'])
                        time.sleep(4)
                    elif word == 'すすんで':
                        jtalk.jtalk(u'進みます')
                        ps.main()
                        subprocess.call(['./upload.sh'])
                        time.sleep(4)
                    elif word == 'もどって':
                        jtalk.jtalk(u'戻ります')
                        pd.main()
                        subprocess.call(['./upload.sh'])
                        time.sleep(4)
                    elif word == 'うたって':
                        time.sleep(50)
                        print(0)
                        
                    res = ''

                    if word == 'ばいばいごみばこ':
                        i = 1
                        break
            if i == 1:
                break
        if i == 1:
            break
    if i == 1:
        jtalk.jtalk(u'ばいばい')
        break
        