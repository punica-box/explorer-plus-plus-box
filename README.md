# explorer-plus-plus-box

A box came from TC SHENZHEN Hackathon 2018. This box is contributed by [includeleec](https://github.com/includeleec).

## 简介

基于本体现有的[区块链浏览器](https://github.com/ontio/ontology-explorer)，利用 `vue.js` 与 `Python`（同步区块信息、查询 OEP4 Token 信息） 进行功能增强。主要包括：

- 显示实时币价（支持根据网站语言,进行 CNY/USD 切换）。
- 账户详情显示 ONT/ONG 实时价值,并进行饼图占比显示。
- 支持显示 OEP4 Token 的列表/详情/转账信息。

## 快速上手

- 运行浏览器界面

``` bash
cd src
cd explorer

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit
``
# run all tests
npm test
```

- 运行同步程序

```bash
cd src
cd sync_node

virtualenv --no-site-packages venv

.\venv\Scripts\activate

pip install -r requirements.txt

python run.py
```