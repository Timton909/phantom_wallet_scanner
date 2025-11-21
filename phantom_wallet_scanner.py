import requests, time

def scan_new_phantom_wallets():
    print("Scanning for new Phantom wallet transactions (Solana whales)...")
    seen = set()
    while True:
        r = requests.get("https://api.solscan.io/account/tokens?address=Phantom&price=1")
        for tx in r.json().get("data", []):
            txid = tx["tx"]
            if txid in seen: continue
            seen.add(txid)
            if tx["change"] > 100000:  # >100k USD move
                print(f"WHALE ALERT!\n"
                      f"Wallet: {tx['owner'][:8]}...\n"
                      f"Amount: ${tx['change']:,.0f}\n"
                      f"Token: {tx['symbol']}\n"
                      f"https://solscan.io/tx/{txid}\n"
                      f"{'-'*50}")
        time.sleep(7)

if __name__ == "__main__":
    scan_new_phantom_wallets()
