from eosjs_python import Eos
import requests
import execjs

ctx = execjs.compile("""ecc = require('eosjs-ecc')
    function getPubkey(privateWif) {
        return ecc.privateToPublic(privateWif)
    }""")

def getAccountName(public_key):
    '公钥转用户名'
    url = "https://nodes.get-scatter.com/v1/history/get_key_accounts"
    data = {"public_key": public_key}
    z = requests.post(url, json=data)
    return z.json()["account_names"][0]


def getPublicKey(private_key):
    '私钥转公钥'
    public_key = ctx.call('getPubkey',private_key)
    return public_key


def run(private_key):
    eos = Eos(
        {"http_address": "https://nodes.get-scatter.com", "key_provider": private_key}
    )
    public_key = getPublicKey(private_key)
    print(public_key)
    account = getAccountName(public_key)
    print(account)
    eos.push_transaction(
        "theeosbutton", "claimad", account, "active", {"account": account}
    )


if __name__ == "__main__":

    private_key = ""
    run(private_key)
