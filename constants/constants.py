RESISTANCE_LEVEL = "resistance_level"
RESISTANCE_ZONE = "resistance_zone"
SUPPORT_LEVEL = "support_level"
SUPPORT_ZONE = "support_zone"
AVWAP_RESISTANCE = "avwap_resistance"
AVWAP_SUPPORT = "avwap_support"
CLOSING_PRICE = "closing_price"
TIMEFRAME = "timeframe"
STRATEGIES = "strategies"
SYMBOL = "symbol"
EMA = "ema"
MA = "ma"
YYYYMMDD_FORMAT = "%Y-%m-%d"
DDMMYYYY_FORMAT = "%d-%m-%Y"

symbols = ["NSE:NIFTYBANK-INDEX", "NSE:NIFTY50-INDEX"]
breakdown_levels = {
    "NSE:NIFTY50-INDEX": 20161,
    "NSE:NIFTYBANK-INDEX": 46060
}

breakout_levels = {
    "NSE:NIFTY50-INDEX": 20220,
    "NSE:NIFTYBANK-INDEX": 46300
}

names = {
    "NSE:NIFTY50-INDEX": "NIFTY",
    "NSE:NIFTYBANK-INDEX": "BANKNIFTY"
}

stoploss = {
    "NSE:NIFTY50-INDEX": 20,
    "NSE:NIFTYBANK-INDEX": 60
}

target = {
    "NSE:NIFTY50-INDEX": 45,
    "NSE:NIFTYBANK-INDEX": 150
}

lot_size = {
    "NSE:NIFTY50-INDEX": 50,
    "NSE:NIFTYBANK-INDEX": 15,
    "HAL": 300
}

stock_symbols = ["M&MFIN", "HAL", "ABFRL", "TVSMOTOR", "PFC", "BEL", "TRENT", "GMRINFRA", "TATACHEM", "IRCTC",
                 "GRANULES", "AUROPHARMA", "EXIDEIND"]

stock_breakout_levels = {
    "HAL": 4117,
    "M&MFIN": 304.75,
    "ABFRL": 234.1,
    "TVSMOTOR": 1486.65
}

stock_breakdown_levels = {
    "ABFRL": 229
}

LONG = "long"
SHORT = "SHORT"
