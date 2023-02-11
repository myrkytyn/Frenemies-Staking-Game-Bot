## [Frenemies Staking Game](https://frenemies.sui.io/)

To participate in Staking Game you need:
1. Create your [Sui Wallet](https://docs.sui.io/explore/wallet-browser)
2. Request test coins in [Discord Channel](https://discord.com/channels/916379725201563759/1037811694564560966). You could request test coins every 2 hours.
3. Play the [Frenemies Staking Game](https://frenemies.sui.io/) 

**[RULES](https://sui.io/resources-sui/make-frenemies-support-validators)**

## What this script could do
This script is made for automatic test coins requests in Frenemies Staking Game.<br>
To request test coins you need to send a message to [Discord Channel](https://discord.com/channels/916379725201563759/1037811694564560966).<br>
The message should have the format: `!faucet <your_sui_address>`

This script will send a message to a Discord channel with your text. <br>
After that, the script will send a message to the Telegram chat with information about the status code and Discord server response.<br>
The script will wait 125 minutes and do the same until you do not close it.

## How to use this script
Prerequisites:
- Install [Python](https://www.python.org/downloads/)
- Open Discord in the browser and get your **Authorization Token** an **URL** <details>
  <summary><i>Screenshot</i></summary>  <img src="https://user-images.githubusercontent.com/42769358/218283024-c84fdd68-4f48-4b6a-859b-880aab3f00ab.png"/></details> 
- Change all {PUT_SOMETHING} places

To run the script:
- Install requirements:
`pip install -r requirements.txt`

- Run the script:
`python3 python3 frenemies_game.py`

