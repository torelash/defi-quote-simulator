import requests

print("⏳ Sending request to Jupiter...")

url = "https://quote-api.jup.ag/v6/quote"
params = {
    "inputMint": "So11111111111111111111111111111111111111112",  # SOL
    "outputMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",  # USDC
    "amount": str(10000000),  # 0.01 SOL
    "slippageBps": 50
}

response = requests.get(url, params=params)

print("✅ Request sent. Processing result...")

if response.ok:
    print("🎉 Success:")
    print(response.json())
else:
    print("❌ Error:", response.status_code)
    print(response.text)

