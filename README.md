## 如何运行

1. 安装nodejs

```
apt-get update
apt-get -y install curl
curl -sL https://deb.nodesource.com/setup_10.x | bash
apt-get -y install nodejs
```

2. 安装 eosjs 与 eosjs-ecc

```
npm install --save eosjs
npm install --save eosjs-ecc
```

3. 安装python依赖
```
pip install requirements.txt
```

4. 运行 `python run.py` 就可以了