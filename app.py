"""
Just woofing around.
"""
from flask import Flask, render_template
from pycoingecko import CoinGeckoAPI
from pycosmicwrap import CosmicWrap

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Main page
    """
    return render_template("index.html", title="Woof")

@app.route("/get_prices", methods=['GET'])
def get_prices():
    """
    Prices from CoinGecko
    """
    cg_api = CoinGeckoAPI()
    prices = cg_api.get_price(ids="cosmos,osmo,secret,axelar,stargaze,evmos,fetch-ai,injective,juno-network,persistence,akash-network,ki,comdex,chihuahua-chain,bitcanna", vs_currencies="usd,eur")
    return prices

@app.route("/woof", methods=['GET'])
def get_woof():
    """
    Wo0f W0of
    """
    chihuahua = CosmicWrap(lcd='https://api.chihuahua.wtf',
                       rpc='https://rpc.chihuahua.wtf',
                       denom='uhuahua')

    # Let's define an address
    my_address = 'chihuahua1z6rfp8wzsx87pwt3z73gf2a67d6tgmfrrlzy7p'

    # Let's create a variable with your balance
    my_address_balance = chihuahua.query_balances(my_address)

    # check all of your delegations
    my_delegations = chihuahua.query_delegations_by_address(my_address)

    return my_address_balance
