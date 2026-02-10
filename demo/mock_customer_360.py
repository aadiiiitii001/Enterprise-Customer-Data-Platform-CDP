# demo/mock_customer_360.py
import pandas as pd

def get_customer_360():
    return pd.DataFrame({
        "customer_id": ["C001", "C002"],
        "email": ["user1@test.com", "user2@test.com"],
        "total_clicks": [12, 7],
        "active_campaigns": [3, 2]
    })
