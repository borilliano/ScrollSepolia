
# ScrollSepolia

**Auto Faucet Request for Scroll Sepolia**

## Overview

**ScrollSepolia** is a Python automation script that helps developers and testers automatically request Scroll Sepolia testnet tokens from the [Chainlink Faucet](https://faucets.chain.link/). This tool streamlines the process of acquiring testnet tokens for smart contract development and testing on the Scroll Sepolia network.

## Features

- Automates the process of requesting Scroll Sepolia testnet tokens
- Uses browser automation to interact with the Chainlink Faucet
- Simple and easy to use

## Prerequisites

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/)
- [pyppeteer](https://github.com/pyppeteer/pyppeteer) Python package

## Installation

Clone this repository:

```bash
git clone https://github.com/borilliano/ScrollSepolia.git
cd ScrollSepolia
```

Install dependencies:

```bash
pip install pyppeteer
```

## Usage

1. Open `scrol.py` and replace `0xYourScrollSepoliaWalletAddress` with your Scroll Sepolia wallet address.
2. Run the script:

```bash
python scrol.py
```

The script will launch a browser, navigate to the Chainlink Faucet, and attempt to request Scroll Sepolia testnet tokens for your address.

## Notes

- **Wallet Connection:** This script does **not** automate connecting wallet extensions (like MetaMask). For full automation, consider Node.js with Puppeteer and dappeteer.
- **Selectors:** If the faucet website changes, you may need to update the selectors in `scrol.py`.
- **Responsible Use:** Please use this tool responsibly and do not abuse public testnet faucets.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


[1] https://github.com/borilliano/ScrollSepolia

---
Answer from Perplexity: https://www.perplexity.ai/search/create-auto-faucet-bnb-chain-f-IC4pzmPZQiSfFrFcsoi4Rg?utm_source=copy_output
