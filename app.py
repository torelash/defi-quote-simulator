# import streamlit as st
# import requests
# import pandas as pd
# import os
# from dotenv import load_dotenv

# load_dotenv()

# BASE_URL = "https://api.0x.org/"
# API_KEY = "55abed0f-ade5-47f5-9513-2b34d7c8c2aa"
# st.title("DeFi Token Swap Analyzer")

# sell_token = st.text_input("Token you want to swap (e.g., ETH)")
# buy_token = st.text_input("Token you want to receive (e.g., USDC)")
# amount = st.number_input("Amount of token to swap (in whole tokens)", value=1)

# if st.button("Fetch Quote"):
#     try:
#         amount_wei = int(amount * 1e18)
#         url = f"{BASE_URL}swap/v1/quote?sellToken={sell_token}&buyToken={buy_token}&sellAmount={amount_wei}"
#         headers = {"0x-api-key": API_KEY}
#         response = requests.get(url, headers=headers)


#         if response.status_code == 200:
#             data = response.json()
#             st.success("Swap Quote Fetched!")
#             st.write(f"Price: {data['price']}")
#             st.write(f"Estimated Gas: {data['gas']}")
#             st.write(f"Buy Amount (raw): {data['buyAmount']}")
#             st.write(f"Protocol Used: {data['sources']}")
#         else:
#             st.error(f"Failed to fetch quote: {response.text}")
#     except Exception as e:
#         st.error(f"Error: {str(e)}")

import streamlit as st
import requests

# Mint addresses
TOKENS = {
    "SOL": "So11111111111111111111111111111111111111112",
    "USDC": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
}

st.title("DeFi Swap Quote Simulator (Solana via Jupiter)")

# UI inputs
sell_token = st.selectbox("Sell Token", list(TOKENS.keys()))
buy_token = st.selectbox("Buy Token", list(TOKENS.keys()), index=1)
amount_sol = st.number_input("Amount to swap (in SOL)", min_value=0.001, value=0.01, step=0.001)
slippage = st.slider("Slippage (%)", 0.1, 5.0, 0.5)

if st.button("Get Quote"):
    input_mint = TOKENS[sell_token]
    output_mint = TOKENS[buy_token]
    lamports = int(amount_sol * 1e9)  # convert SOL to lamports
    slippage_bps = int(slippage * 100)

    url = "https://quote-api.jup.ag/v6/quote"
    params = {
        "inputMint": input_mint,
        "outputMint": output_mint,
        "amount": str(lamports),
        "slippageBps": slippage_bps
    }

    st.write("🔄 Fetching quote...")
    response = requests.get(url, params=params)

    if response.ok:
        data = response.json()
        out_amount = int(data["outAmount"]) / 1e6  # assumes USDC has 6 decimals
        usd_value = data.get("swapUsdValue", "N/A")
        st.success(f"You'll receive approximately **{out_amount:.4f} {buy_token}**")
        st.caption(f"Estimated USD value: ${usd_value}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
