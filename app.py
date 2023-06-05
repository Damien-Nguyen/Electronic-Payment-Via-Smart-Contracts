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
    with open(Path("./contracts/compiled/transaction.json")) as f:
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
receiver_account = st.text_input("receiver public address")
# Enter a text string for the token or link to digital location
payment_details = st.text_input("Trading Details", value="Quantity of Tokens")
if st.button("Transfer Token"):
    # Call the awardCertificate function with web3
    contract.functions.awardCertificate(receiver_account, trading_details).transact({"from":account, "gas": 1000000})
    transact({'from': account, 'gas': 10})

################################################################################
# Display Receiver
################################################################################
receiver_address = st.writer(receiver_account)
# @TODO: YOUR CODE HERE!
if st.button("Display Receiver"):
    # Get the receiver
    receiver = contract.functions.ownerof(receiver_id).call()
    st.write(f"The token was transferred to {receiver}")
    # Get the receiver's URI
    receiver_uri = contract.functions.tokenURI(receiver_id).call()
    st.write(f"The receiver's tokenURI metadata is {receiver_uri}")
