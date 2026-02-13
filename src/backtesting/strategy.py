"""
Strategy module.

Converts model predictions into trading actions:
- 1  = BUY / Long
- 0  = HOLD / Flat
- -1 = SELL / Short
"""

def generate_signal(prediction: float, buy_threshold: float = 0.55, sell_threshold: float = 0.45) -> int:
    """
    Convert a prediction/probability into a discrete trading signal.
    """
    if prediction >= buy_threshold:
        return 1
    if prediction <= sell_threshold:
        return -1
    return 0
