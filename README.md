# Staking Rewards

Brownie implementation of the Synthetix StakingRewards contract on the Avalanche C-Chain network.

## Installation and Setup

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html) & [Ganache-CLI](https://github.com/trufflesuite/ganache-cli), if you haven't already.

2. Install the dependencies in the package

```
## Javascript dependencies
npm i

## Python Dependencies
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the following command to install the Avalanche main network:

```
brownie networks add Avalanche avax-avash2 host=https://api.avax.network/ext/bc/C/rpc chainid=43112 explorer=https://cchain.explorer.avax.network/
```

4. Run the following command to install the Avalanche fork network:

```
brownie networks import network-config.yaml
```

## Basic Usage

To deploy the StakingRewards contract in a development environment:

1. Open the Brownie console. This automatically launches Ganache on a forked mainnet.

```bash
  brownie console
```

2. Run Scripts for Deployment

```
  brownie run scripts/deploy.py --network avax-avash2
```

Deployment will set up your StakingRewards contract along with its dependencies.
