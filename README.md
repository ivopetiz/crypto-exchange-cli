# crypto-exchange-cli

## CLI for Crypto Exchanges

crypto-exchange-cli is a command line app, built in Python, that presents prices for several pairs which are presented in Crypto Exchanges.

![](images/Screenshot_001.png?raw=true)

Only available for Poloniex, for now.

## Install

```bash
pip install https://github.com/s4w3d0ff/python-poloniex/archive/v0.4.7.zip
git clone https://github.com/ivopetiz/crypto-exchange-cli.git
cd crypto-exchange-cli
```

## Usage examples

### Regular usage

Presents CLI with 30 most traded crypto pairs, ordered by volume.

```bash
cli.py
```

### Use without color

Presents CLI with 30 most traded crypto pairs, ordered by volume, but without color.

```bash
cli.py --nocolor
```

### 10 most traded coins

Presents CLI with 10 most traded crypto pairs, ordered by volume.

```bash
cli.py 10
```

## TODO

- add mycoins option.
- add Bittrex exchange.
- add Cryptopia exchange.
- change arg flags method.