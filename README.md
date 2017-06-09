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

- model/  
作成したモデルを保存する  

### 実行方法
- 設定
```
git clone https://github.com/takahiro-777/titanic.git
cd titanic  #プロジェクトルートに移動
```

- ランダムフォレスト  
プロジェクトルート下で、  
```
python src/train.py  
python src/test.py  
```
で学習→予測が可能。モデルに関してはmodelディレクトリに、予測結果に関してはoutputディレクトリに保存される。（kaggleの提出の形式になっている）  

- ロジスティック回帰
プロジェクトルート下で、
```
python src/rgeos.py
```
でモデルの作成、予測が可能。予測結果に関してはoutputディレクトリに保存される。（kaggleの提出の形式になっている）
