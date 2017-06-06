# README

### 概要
kaggleの練習用としてよく使われるtitanicのモデル構築に当たって得た知見と同時に作成したソースコードに関してまとめる。  
http://qiita.com/suzumi/items/8ce18bc90c942663d1e6  
あくまでベースのコードなので、上記を参考に簡単にまとめた。

### ディレクトリ構成
- data/  
元データに関してまとめてある。  
http://qiita.com/suzumi/items/8ce18bc90c942663d1e6  
詳細のデータの説明に関しては上記などが詳しい  

- src/  
開発に当たってスクリプトをまとめてある。  
train.py、test.pyはランダムフォレストを利用したベースの処理フロー（正答率は62%ほど）。  
rgeos.pyはhttps://github.com/rgeos/meetup/blob/master/Titanic.ipynb
を参考にロジスティックモデルを組んだもの（正答率75%ほど）。  

- models/  
作成したモデルを保存する  
