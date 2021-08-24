import time

from brownie import accounts, network, StakingRewards

import click
from rich.console import Console

console = Console()

def main():

    # Get deployer account from local keystore
    dev = connect_account()

    # Get params for constructor
    rewardsToken = "0x2C31b10ca416b82Cec4c5E93c615ca851213d48D"
    stakingToken = "0x2C31b10ca416b82Cec4c5E93c615ca851213d48D"

    #Deploy StakingRewards contract

    StakingRewards.deploy( dev, dev, rewardsToken, stakingToken, {'from': dev})

def connect_account():
    click.echo(f"You are using the '{network.show_active()}' network")
    dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'dev' [{dev.address}]")
    return dev