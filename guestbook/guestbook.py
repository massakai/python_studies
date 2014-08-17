# coding: utf-8
from datetime import datetime
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

@application.route('/post', methods=['POST'])
def post():
    u"""投稿用URL
    """
    # 投稿されたデータを取得します
    name = request.form.get('name') # 名前
    comment = request.form.get('comment') # コメント
    create_at = datetime.now() # 投稿日時(現在時刻)
    # データを保存します
    save_data(name, comment, create_at)
    # 保存後はトップページにリダイレクトします
    return redirect('/')

@application.template_filter('nl2br')
def nl2br_filter(s):
    u"""改行文字をbrタグに置き換えるテンプレートフィルタ
    """
    return escape(s).replace('\n', Markup('<br />'))

@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    u"""datetimeオブジェクトを見やすい表示にするテンプレートフィルタ
    """
    return dt.strftime('%Y/%m/%d %H:%M:%S')

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
