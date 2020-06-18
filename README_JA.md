## 自前データの場合

### データセットの用意
`domain_a.txt` pos
`domain_b.txt` neg
を用意する。

### データセットビルド用のパラメータファイルの設定変更
`params.yml`
の中身を編集する

### データセットのビルド

```
python build_ja_data.py
```

mydata配下に
`train.txt`
`valid.txt`
`test.txt`
がそれぞれ生成される。


## 楽天レビューデータセットの場合

### データセットの用意
`rakuten_reviews.txt` pos,neg混合
を用意する。

1～3をneg4～5をposとする

### データセットビルド用のパラメータファイルの設定変更
`params.yml`
の中身を編集する

### データセットのビルド

```
python databuilder/rakuten_review.py #rakuten_reviews.jsonが生成される
python build_ja_data.py --dataset_path data/rakuten_ja/rakuren_reviews.json --skip_domain_concat 1
```