# comparison_gsvsについて

## どんなアプリケーションか
- バリュー株とグロース株の利益比較ツール
- URL:https://comparisongsvs-d959a0d19882.herokuapp.com/

## 目的
- 近年、年金を始めとする将来の生活の不安を考える人が多くなってきており、資産形成に取り組んでいる人が増えてきている。資産形成をしている人の大半はNISAを利用し、積み立ての投資信託をしている。この中で少数派ではあるが、個別の企業の株式を利用し資産形成をしている人も出てきている。この個別の企業の株式というのは、バリュー株とグロース株の2つに大別できる。バリュー株の特徴としては、配当金の額が大きい代わりに株価が年単位で大きく伸びない傾向にある。一方でグロース株の特徴としては、配当金の額が少額また存在しない代わりに株価が年単位で大きく伸びる傾向にある。現状どちらの株を選定するかに関しては、人の意見が分かれており、株式購入を迷う一つの要因となっている。そこでバリュー株とグロース株の企業を選択し比較できるWebアプリケーションを開発した。

## 機能
-株価と配当のデータ取得
-キャピタルゲインと配当収益の計算
-グラフによる比較

## 技術内容
- フロントエンド:html, css
- バックエンド:python
- フレームワーク:flask
- ライブラリ:matplotlib, yfinance
- バージョン管理:Git
- インフラ:Heroku

## アプリケーションの機能と設計
# フロントエンド
   -	期間選択（開始日・終了日）
   -	バリュー株とグロース株の選択（または使用するインデックス）
   -	「compare」ボタン
# バックエンド
 -	データ取得
 -	
   -	選択された株式の価格データと配当データをyfinanceなど使って取得
   -  例: Apple社(AAPL)をグロース株、ファイザー（PFE）をバリュー株として使用
 -	データ処理
 -	
   -	指定期間のデータをフィルタリング
   -	株式価格の変化（キャピタルゲイン）を計算
   -	配当金の合計を計算
   -	両者を統合して総利益を算出
 -	結果の処理
 -	
   -	比較結果をフロントエンドに返す
