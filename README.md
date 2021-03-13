# study-figure

## 目的
10/12 10/19　の勉強会用



## 前準備(git)



初めにgitの復習



まず このリポジトリをcloneしよう（ダウンロードみたいなもの）

````
$ git clone https://github.com/KatayamaLab/study-figure.git
````

ローカル（自分のpc）にブランチを作る

````
$ git checkout -b <ブランチ名>
`````

リモート（githubとか）にブランチを送って作るイメージ
````
git push --set-upstream origin test
````

gitの使い方

git status → git add → git commit →git push 



````
$ git status #今gitがどういう状態か確認
````



````
$ git add . #仮で変更点を保存するイメージ
````



````
$ git commit -m 'コメント' #addにあるものを本保存するイメージ　変更点をコメントする
````



````
$ git push #リモートに保存（githubに保存するイメージ）
````

