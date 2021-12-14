import xrpl

# actual paths from mainnet tx 93783521670DC5A61FC119D0D241573C813C742A0BA4DBF8484849F56EFC54E4
paths_json = [
[
  {
    "account": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
    "type": 1
  },
  {
    "currency": "USD",
    "issuer": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 48
  },
  {
    "account": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 1
  },
  {
    "account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn",
    "type": 1
  }
],
[
  {
    "account": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 1
  },
  {
    "currency": "USD",
    "issuer": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 48
  },
  {
    "account": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 1
  },
  {
    "account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn",
    "type": 1
  }
],
[
  {
    "account": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
    "type": 1
  },
  {
    "currency": "XRP",
    "type": 16
  },
  {
    "currency": "USD",
    "issuer": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 48
  },
  {
    "account": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 1
  },
  {
    "account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn",
    "type": 1
  }
],
[
  {
    "account": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 1
  },
  {
    "currency": "XRP",
    "type": 16
  },
  {
    "currency": "USD",
    "issuer": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 48
  },
  {
    "account": "rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q",
    "type": 1
  },
  {
    "account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn",
    "type": 1
  }
]
]

# basically just reconstructing 93783521670DC5A61FC119D0D241573C813C742A0BA4DBF8484849F56EFC54E4
p = xrpl.models.transactions.Payment(
    account="rweYz56rfmQ98cAdRaeTxQS9wVMGnrdsFp",
    amount=xrpl.models.amounts.IssuedCurrencyAmount(
        currency="USD",
        issuer="rweYz56rfmQ98cAdRaeTxQS9wVMGnrdsFp",
        value="0.0001"
    ),
    destination="rweYz56rfmQ98cAdRaeTxQS9wVMGnrdsFp",
    send_max=xrpl.models.amounts.IssuedCurrencyAmount(
        currency="BTC",
        issuer="rweYz56rfmQ98cAdRaeTxQS9wVMGnrdsFp",
        value="0.0000002831214446"
    ),
    fee="12000",
    flags=0,
    last_ledger_sequence=9787702,
    memos=[xrpl.models.transactions.transaction.Memo(
        memo_data = "7274312E312E302D31",
        memo_type = "636C69656E74"
    )],
    paths=paths_json,
    sequence=290,
    signing_pub_key = "0379F17CFA0FFD7518181594BE69FE9A10471D6DE1F4055C6D2746AFD6CF89889E",
    txn_signature = "30440220273179E72B1A49BEA00163166353812882D1E5F58617AFD8854C7C8CAD76C1C6022027F73143EDF2A8B48C99109D2C4AB71AF549CE227ADB423CBAD936617C570999"
)

print(p)

# signed = xrpl.transaction.safe_sign_transaction(p, wallet)
# print(signed)

txjson = xrpl.transaction.transaction_json_to_binary_codec_form(p.to_dict())
encoded = xrpl.core.binarycodec.encode(txjson).strip()
print(encoded)
