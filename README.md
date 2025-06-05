name: DeFi Quote Simulator (Solana via Jupiter)
description: |
  A lightweight Streamlit app that simulates real-time token swaps using the Jupiter Aggregator API (Solana-based). 
  No API key required. Designed for beginners in DeFi.

features:
  - Live quote simulation (SOL ↔ USDC)
  - Adjustable amount and slippage
  - No wallet or API key required
  - Built on Jupiter (Solana), with optional 0x upgrade support

tech_stack:
  - Python
  - Streamlit
  - Requests
  - Jupiter Aggregator API

instructions:
  setup:
    - optional_virtual_env:
        - python -m venv venv
        - .\venv\Scripts\activate  # Windows
        - source venv/bin/activate  # Mac/Linux
    - install_dependencies:
        - pip install -r requirements.txt
    - run_app:
        - streamlit run app.py

optional_upgrade:
  name: 0x API (Ethereum/EVM)
  steps:
    - Sign up at https://0x.org/
    - Get a free API key from https://0x.org/docs/api#getting-started
    - Replace Jupiter logic in app.py with a GET request to 0x swap endpoint
    - Add API key in the headers of your request
    - Comment out line 1 to 35 to change to 0x swap check. Need to upgrade to better API level to remove errors
  note: |
    0x supports Ethereum and EVM chains, not Solana. Use if expanding beyond SOL/USDC.

