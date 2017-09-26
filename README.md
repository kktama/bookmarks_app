# bookmarks_app


ブックマーク共有アプリ。



python3が前提。

開発に使っているdjangoのバージョンは、1.9.13。
コメントを投稿するフォームを作るのには、django-contrib-commentsというモジュールを利用した。

これらは、次の操作でインストールできる。
pip3 install django~=1.9.0 (~=1.9を省けば1.11.0以上がインストールされる)
pip3 install django-contrib-comments



ローカルでテストする場合、

1. cloneしてワーキングツリーのルートディレクトリに入る。
2. python3 manage.py runserver 
3. ブラウザで、localhost:8000 にアクセス。

 
