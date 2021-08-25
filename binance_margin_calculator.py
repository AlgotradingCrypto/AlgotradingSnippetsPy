# Algotrading Crypto 
# Submitted by Raymond Luo
# https://algotradingcrypto.com/d/22-the-aedge-of-tomorrow/8
# https://www.binance.com/en/support/faq/360033162192

BINANCE_FUTURES_SCHEDULE = {
    'BTCUSDT': [
            { 'quantum': 50_000, 'max_leverage': 125, 'initial_margin_rate': 0.0080, 'maintenance_margin_rate': 0.0040 },
            { 'quantum': 250_000, 'max_leverage': 100, 'initial_margin_rate': 0.0100, 'maintenance_margin_rate': 0.0050 },
            { 'quantum': 1_000_000, 'max_leverage': 50, 'initial_margin_rate': 0.0200, 'maintenance_margin_rate': 0.0100 },
            { 'quantum': 10_000_000, 'max_leverage': 20, 'initial_margin_rate': 0.0500, 'maintenance_margin_rate': 0.0250 },
            { 'quantum': 20_000_000, 'max_leverage': 10, 'initial_margin_rate': 0.1000, 'maintenance_margin_rate': 0.0500 },
            { 'quantum': 50_000_000, 'max_leverage': 5, 'initial_margin_rate': 0.2000, 'maintenance_margin_rate': 0.1000 },
            { 'quantum': 100_000_000, 'max_leverage': 4, 'initial_margin_rate': 0.2500, 'maintenance_margin_rate': 0.1250 },
            { 'quantum': 200_000_000, 'max_leverage': 3, 'initial_margin_rate': 0.3330, 'maintenance_margin_rate': 0.1500 },
            { 'quantum': 300_000_000, 'max_leverage': 2, 'initial_margin_rate': 0.5000, 'maintenance_margin_rate': 0.2500 },
            { 'quantum': 500_000_000, 'max_leverage': 1, 'initial_margin_rate': 1.0000, 'maintenance_margin_rate': 0.5000 },
        ],
    'ETHUSDT': [
            { 'quantum': 10_000, 'max_leverage': 100, 'initial_margin_rate': 0.0080, 'maintenance_margin_rate': 0.0050},
            { 'quantum': 100_000, 'max_leverage': 75, 'initial_margin_rate': 0.0100, 'maintenance_margin_rate': 0.0065 },
            { 'quantum': 500_000, 'max_leverage': 50, 'initial_margin_rate': 0.0200, 'maintenance_margin_rate': 0.0100 },
            { 'quantum': 1_000_000, 'max_leverage': 25, 'initial_margin_rate': 0.0500, 'maintenance_margin_rate': 0.0200, 'maintenance_amount': 5_365 },
            { 'quantum': 2_000_000, 'max_leverage': 10, 'initial_margin_rate': 0.1000, 'maintenance_margin_rate': 0.0500, 'maintenance_amount': 35_365 },
            { 'quantum': 5_000_000, 'max_leverage': 5, 'initial_margin_rate': 0.2000, 'maintenance_margin_rate': 0.1000, 'maintenance_amount': 135_365 },
            { 'quantum': 10_000_000, 'max_leverage': 4, 'initial_margin_rate': 0.2500, 'maintenance_margin_rate': 0.1250, 'maintenance_amount': 260_365 },
            { 'quantum': 20_000_000, 'max_leverage': 3, 'initial_margin_rate': 0.3330, 'maintenance_margin_rate': 0.1500, 'maintenance_amount': 510_365 },
            { 'quantum': 20_000_000, 'max_leverage': 2, 'initial_margin_rate': 0.5000, 'maintenance_margin_rate': 0.2500, 'maintenance_amount': 251_0365 },
            { 'quantum': 20_000_000, 'max_leverage': 1, 'initial_margin_rate': 1.0000, 'maintenance_margin_rate': 0.2500, 'maintenance_amount': 251_0365 },
        ],
    ('ADAUSDT', 'BNBUSDT', 'DOTUSDT', 'EOSUSDT', 'ETCUSDT', 'LINKUSDT', 'LTCUSDT', 'TRXUSDT', 'XLMUSDT', 'XMRUSDT', 'XRPUSDT', 'XTZUSDT', 'BCHUSDT'): [
            { 'quantum': 10_000, 'max_leverage': 75, 'initial_margin_rate': 0.0100, 'maintenance_margin_rate': 0.0065 },
            { 'quantum': 50_000, 'max_leverage': 50, 'initial_margin_rate': 0.0200, 'maintenance_margin_rate': 0.0100 },
            { 'quantum': 250_000, 'max_leverage': 25, 'initial_margin_rate': 0.0400, 'maintenance_margin_rate': 0.0200 },
            { 'quantum': 1_000_000, 'max_leverage': 10, 'initial_margin_rate': 0.1000, 'maintenance_margin_rate': 0.0500 },
            { 'quantum': 2_000_000, 'max_leverage': 5, 'initial_margin_rate': 0.2000, 'maintenance_margin_rate': 0.1000 },
            { 'quantum': 5_000_000, 'max_leverage': 4, 'initial_margin_rate': 0.2500, 'maintenance_margin_rate': 0.1250 },
            { 'quantum': 10_000_000, 'max_leverage': 3, 'initial_margin_rate': 0.3300, 'maintenance_margin_rate': 0.1500 },
            { 'quantum': 10_000_000, 'max_leverage': 2, 'initial_margin_rate': 0.5000, 'maintenance_margin_rate': 0.2500 },
            { 'quantum': 10_000_000, 'max_leverage': 1, 'initial_margin_rate': 1.0000, 'maintenance_margin_rate': 0.2500 },
        ],
    ('ALGOUSDT', 'ALPHAUSDT', 'ATOMUSDT', 'AVAXUSDT', 'AXSUSDT', 'BALUSDT', 'BANDUSDT', 'BATUSDT', 'BELUSDT', 'BLZUSDT', 'BZRXUSDT', 'COMPUSDT', 'CRVUSDT', 'CVCUSDT', 'DASHUSDT', 'DEFIUSDT', 'EGLDUSDT', 'ENJUSDT', 'FLMUSDT', 'FTMUSDT', 'HNTUSDT', 'ICXUSDT', 'IOSTUSDT', 'IOTAUSDT', 'KAVAUSDT', 'KNCUSDT', 'KSMUSDT', 'LRCUSDT', 'MATICUSDT', 'MKRUSDT', 'NEARUSDT', 'NEOUSDT', 'OCEANUSDT', 'OMGUSDT', 'ONTUSDT', 'QTUMUSDT', 'RENUSDT', 'RLCUSDT', 'RSRUSDT', 'RUNEUSDT', 'SNXUSDT', 'SOLUSDT', 'SRMUSDT', 'STORJUSDT', 'SUSHIUSDT', 'SXPUSDT', 'TOMOUSDT', 'TRBUSDT', 'VETUSDT', 'WAVESUSDT', 'YFIIUSDT', 'YFIUSDT', 'ZECUSDT', 'ZILUSDT', 'ZRXUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', 'DOGEUSDT', 'CTKUSDT', 'BTSUSDT', 'LITUSDT', 'UNFIUSDT', 'DODOUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'BTCSTUSDT', 'COTIUSDT', 'CHRUSDT', 'ALICEUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'BTTUSDT'): [
            { 'quantum': 5_000, 'max_leverage': 50, 'initial_margin_rate': 0.0200, 'maintenance_margin_rate': 0.0100 },
            { 'quantum': 25_000, 'max_leverage': 20, 'initial_margin_rate': 0.0500, 'maintenance_margin_rate': 0.0250 },
            { 'quantum': 100_000, 'max_leverage': 10, 'initial_margin_rate': 0.1000, 'maintenance_margin_rate': 0.0500 },
            { 'quantum': 250_000, 'max_leverage': 5, 'initial_margin_rate': 0.2000, 'maintenance_margin_rate': 0.1000 },
            { 'quantum': 1_000_000, 'max_leverage': 2, 'initial_margin_rate': 0.5000, 'maintenance_margin_rate': 0.1250 },
            { 'quantum': 1_000_000, 'max_leverage': 1, 'initial_margin_rate': 1.0000, 'maintenance_margin_rate': 0.5000 },   
        ],
    ('1INCHUSDT', 'ANKRUSDT', 'AKROUSDT', 'SANDUSDT', 'LUNAUSDT', 'CHZUSDT'): [
            { 'quantum': 5_000, 'max_leverage': 50, 'initial_margin_rate': 0.0200, 'maintenance_margin_rate': 0.0120},
            { 'quantum': 25_000, 'max_leverage': 20, 'initial_margin_rate': 0.0500, 'maintenance_margin_rate': 0.0250 },
            { 'quantum': 100_000, 'max_leverage': 10, 'initial_margin_rate': 0.1000, 'maintenance_margin_rate': 0.0500 },
            { 'quantum': 250_000, 'max_leverage': 5, 'initial_margin_rate': 0.2000, 'maintenance_margin_rate': 0.1000 },
            { 'quantum': 1_000_000, 'max_leverage': 2, 'initial_margin_rate': 0.5000, 'maintenance_margin_rate': 0.1250 },
            { 'quantum': 1_000_000, 'max_leverage': 1, 'initial_margin_rate': 1.0000, 'maintenance_margin_rate': 0.5000 },
        ],
    ('FILUSDT', 'AAVEUSDT', 'THETAUSDT', 'UNIUSDT'): [
            { 'quantum': 50_000, 'max_leverage': 50, 'initial_margin_rate': 0.0200, 'maintenance_margin_rate': 0.0100},
            { 'quantum': 250_000, 'max_leverage': 25, 'initial_margin_rate': 0.0400, 'maintenance_margin_rate': 0.0200 },
            { 'quantum': 1_000_000, 'max_leverage': 10, 'initial_margin_rate': 0.1000, 'maintenance_margin_rate': 0.0500 },
            { 'quantum': 2_000_000, 'max_leverage': 5, 'initial_margin_rate': 0.2000, 'maintenance_margin_rate': 0.1000 },
            { 'quantum': 5_000_000, 'max_leverage': 4, 'initial_margin_rate': 0.2500, 'maintenance_margin_rate': 0.1250 },
            { 'quantum': 10_000_000, 'max_leverage': 3, 'initial_margin_rate': 0.3300, 'maintenance_margin_rate': 0.1665 },
            { 'quantum': 10_000_000, 'max_leverage': 2, 'initial_margin_rate': 0.5000, 'maintenance_margin_rate': 0.2500 },
        ],
    ('NKNUSDT', 'SCUSDT', 'DGBUSDT', '1000SHIBUSDT', 'ICPUSDT'): [
            { 'quantum': 5_000, 'max_leverage': 50, 'initial_margin_rate': 0.0400, 'maintenance_margin_rate': 0.0100},
            { 'quantum': 25_000, 'max_leverage': 20, 'initial_margin_rate': 0.0500, 'maintenance_margin_rate': 0.0250 },
            { 'quantum': 100_000, 'max_leverage': 10, 'initial_margin_rate': 0.1000, 'maintenance_margin_rate': 0.0500 },
            { 'quantum': 250_000, 'max_leverage': 5, 'initial_margin_rate': 0.2000, 'maintenance_margin_rate': 0.1000 },
            { 'quantum': 1_000_000, 'max_leverage': 2, 'initial_margin_rate': 0.5000, 'maintenance_margin_rate': 0.1250 },
            { 'quantum': 1_000_000, 'max_leverage': 1, 'initial_margin_rate': 1.0000, 'maintenance_margin_rate': 0.5000 },
    ],
}

# Calculate the initial and maintenance quantum required in your account
def calculate_margin_conditions(symbol, quantum, leverage):
    
    initial_quantum = 0
    maintenance_quantum = 0
    
    for schedule_symbol_s, schedule_table in BINANCE_FUTURES_SCHEDULE.items():
        if symbol in schedule_symbol_s:
            for i, rule in enumerate(schedule_table):
                initial_quantum = quantum * schedule_table[i]['initial_margin_rate']
                if i == 0:
                    continue
                else:
                    maintenance_quantum += schedule_table[i-1]['quantum'] * ( schedule_table[i]['maintenance_margin_rate'] - schedule_table[i-1]['maintenance_margin_rate'] )
                if rule['quantum'] >= quantum and rule['max_leverage'] >= leverage:
                    break
                
    return initial_quantum, maintenance_quantum

# Calculate the quantum allowed based on the leverage
def calculate_margin_loanable(symbol, leverage):
    
    loanable_quantum = 0
    
    for schedule_symbol_s, schedule_table in BINANCE_FUTURES_SCHEDULE.items():
        if symbol in schedule_symbol_s:
            for i, rule in enumerate(schedule_table):
                if rule['max_leverage'] < leverage:
                    try:
                        loanable_quantum = schedule_table[i-1]['quantum']
                    except IndexError:
                        loanable_quantum = rule['quantum']
                    break
    
    return loanable_quantum
