import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache_resource()
def load_contract():

    # Load Transaction ABI
    with open(Path("./contracts/compiled/transaction_abi.json")) as f:
        contract_abi=json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract using web3
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()


################################################################################
# Transfer Token
################################################################################

accounts = w3.eth.accounts
account = accounts[0]
# Select or enter a recipient address using a Streamlit component
st.markdown("## DLJ Token Mint")
receiver_account = st.text_input("DLJ Token Buyer Public Address")
# Enter a text string for the token or link to digital location
token_purchased_amount = st.text_input("Token Purchase Quantity", value="Quantity of Tokens")
token_purchase_name = st.text_input("DLJ Token Purchaser Name")

if st.button ("Transfer Token"):
    # Call the awardCertificate function with web3
    contract.functions.mintDLJ(receiver_account, token_purchased_amount).transact({"from":account, "gas": 1000000})
    

# Pay to Others
st.markdown("## Ether Transfer")
recipient_account = st.text_input("Recipient Public Address")
ether_transfer_amount=st.text_input("Ether Quantiy", value="Quantity of Ether")
recipient_name = st.text_input("Ether Recipient Name")

if st.button ("Transfer Ether"):
    contract.functions.transferEther(recipient_account, ether_transfer_amount).transact({"from":account, "gas":1000000})

################################################################################
# Display Receiver
################################################################################
st.markdown("## Display DLJ Receiver and Ether Recipient")
# @TODO: YOUR CODE HERE!
if st.button("Display Token Receiver"):
    # Get the receiver
    st.write(f"The token was transferred to {token_purchase_name}")
    st.write(f"Transferred Token Quantity is {token_purchased_amount}")
    # Get the receiver's address
    st.write(f"The token receiver's address is {receiver_account}")

if st.button("Display Ether Recipient"):
    # Get the recipient
    st.write(f"The Ether was transferred to {recipient_name}")
    st.write(f"Transferred Ether Quantity is {ether_transfer_amount}")
    # Get the recipient's address
    st.write(f"The Ether recipient's public address is {recipient_account}")