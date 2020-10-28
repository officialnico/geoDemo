import ccxt

for ex in exchanges:
    exchange_async = getattr(ccxt_a, 'binance')({'enableRateLimit': True, 'verbose': False})  # 'verbose': True
