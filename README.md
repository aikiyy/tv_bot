tv_bot
====
## Description
[Yahoo!テレビ.Gガイド ［テレビ番組表］](https://tv.yahoo.co.jp/)を特定ワードで検索し、該当する番組をSlackへ定期的に通知するbotです。
<br>
デフォルトでは、「フランス」「ドイツ」というワードで毎日18時に次の日の番組についてチェックします。

## Requirement
Dockerのインストール、GCEでの運用を行うならGoogleCloudSDKのインストールと`gcloud auth login`を済ませておく必要があります。

## Setting
GCPへのDockerイメージのデプロイ用に、GCPのプロジェクトIDを環境変数にセットする必要があります。
```bash
$ export PROJECT_ID=${your gcp project _id}
```

ローカルでbotのテストをする際は、Slack Token等の環境変数をセットする必要があります。
```bash
$ export SLACK_TOKEN=${your slack api token}

# 設定しない場合randomに投稿されます
$ export POST_CHANNEL=${post channel}

# 設定しない場合:tv:のアイコンで投稿されます
$ export ICON_EMOJI=${bot icon}
```

## Deploy
google container registry へのdeployまで。

```bash
$ git clone git@github.com:aikiyy/tv_bot.git
$ cd tv_bot
$ bin/deploy
```

## Licence
This software is released under the MIT License, see LICENSE.txt.

## Author
[aikiyy](https://github.com/aikiyy)
