import beaker
import pyteal as pt
from algokit_utils import DELETABLE_TEMPLATE_NAME, UPDATABLE_TEMPLATE_NAME
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import ApplicationCallTxn, ApplicationUpdateTxn, OnComplete

app = beaker.Application("biogas")


@app.update(authorize=beaker.Authorize.only_creator(), bare=True)
def update() -> pt.Expr:
    return pt.Assert(
        pt.Tmpl.Int(UPDATABLE_TEMPLATE_NAME),
        comment="Check app is updatable",
    )


@app.delete(authorize=beaker.Authorize.only_creator(), bare=True)
def delete() -> pt.Expr:
    return pt.Assert(
        pt.Tmpl.Int(DELETABLE_TEMPLATE_NAME),
        comment="Check app is deletable",
    )

# Create a smart contract call to store a hash
@app.external
    
def store_hash(app_id, sender_address, private_key, hash_to_store):
    call_txn = ApplicationCallTxn(sender=sender_address, sp=app_id, index=0, on_complete=OnComplete.NoOpOC)
    call_txn.params.application_id = app_id
    call_txn.params.accounts = [sender_address]
    call_txn.params.application_id = app_id
    call_txn.params.approval_program = b'your-approval-program'
    call_txn.params.clear_state_program = b'your-clear-state-program'
    call_txn.params.applications = [app_id]
    call_txn.params.application_id = app_id
    call_txn.params.applications = [app_id]
    call_txn.params.note = hash_to_store.encode()
    signed_txn = call_txn.sign(private_key)
    tx_id = algod_client.send_transaction(signed_txn)
    return tx_id

# Create a smart contract call to retrieve a hash
@app.external
def retrieve_hash(app_id, sender_address, private_key):
    call_txn = ApplicationCallTxn(sender=sender_address, sp=app_id, index=0, on_complete=OnComplete.NoOpOC)
    call_txn.params.application_id = app_id
    call_txn.params.accounts = [sender_address]
    call_txn.params.application_id = app_id
    call_txn.params.approval_program = b'your-approval-program'
    call_txn.params.clear_state_program = b'your-clear-state-program'
    call_txn.params.applications = [app_id]
    call_txn.params.application_id = app_id
    call_txn.params.applications = [app_id]
    call_txn.params.note = hash_to_store.encode()
    signed_txn = call_txn.sign(private_key)
    tx_id = algod_client.send_transaction(signed_txn)
    return tx_id

hash_to_store = hash
store_hash(app_id, sender_address, wallet_private_key, hash_to_store)
fetch_hash(app_id, sender_address)
