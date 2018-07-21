## How to run

1. install nodejs

```
apt-get update
apt-get -y install curl
curl -sL https://deb.nodesource.com/setup_10.x | bash
apt-get -y install nodejs
```

2. install eosjs and eosjs-ecc

```
npm install --save eosjs
npm install --save eosjs-ecc
```

3. `git clone https://github.com/jin10086/eos-python.git && cd eos-python`

4. install python package
```
pip install requirements.txt
```

5. input you eos private key and run `python run.py`
