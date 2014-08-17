# coding: utf-8
import shelve

from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

IP = '172.31.15.214'
PORT = 5000
DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    u"""投稿データを保存します
    """
    # shelveモジュールでデータベースファイルを開きます
    database = shelve.open(DATA_FILE)
    # データベースにgreeting_listがなければ、新しくリストを作ります
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # データベースからデータを取得します
        greeting_list = database['greeting_list']
    # リストの先頭に投稿データを追加します
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })
    # データベースを更新します
    database['greeting_list'] = greeting_list
    # データベースファイルを閉じます
    database.close()

def load_data():
    u"""投稿されたデータを返します
    """
    # shelveモジュールでデータベースファイルを開きます
    database = shelve.open(DATA_FILE)
    # greeting_listを返します。データがなければ空のリストを返します
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list

@application.route('/')
def index():
    u"""トップページ
    テンプレートを使用してページを表示します
    """
    # 投稿データを読み込みます
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

if __name__ == '__main__':
    application.run(IP, PORT, debug=True)
