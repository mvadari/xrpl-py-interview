from unittest import TestCase

import xrpl
from tests.integration.it_utils import JSON_RPC_CLIENT as client


class TestInterview(TestCase):
    def test_from_xrpl_memos(self):
        wallet = xrpl.wallet.generate_faucet_wallet(client)

        memo = xrpl.models.transactions.transaction.Memo(
            memo_data="72656e74",
            memo_type="687474703a2f2f6578616d706c652e636f6d2f6d656d6f2f67656e65726963",
        )

        tx_payment = xrpl.models.transactions.Payment(
            account=wallet.classic_address,
            amount=xrpl.utils.xrp_to_drops(10),
            destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
            memos=[memo],
        )
        tx_payment_signed = xrpl.transaction.safe_sign_and_submit_transaction(
            tx_payment, wallet, client
        )
        print(tx_payment_signed)
