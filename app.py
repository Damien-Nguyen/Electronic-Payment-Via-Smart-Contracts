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

    # Load Art Gallery ABI
    with open(Path("./contracts/compiled/certificate_abi.json")) as f:
        certificate_abi=json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract using web3
    contract = w3.eth.contract(
        address=contract_address,
        abi=certificate_abi
    )

    return contract


# Load the contract
contract = load_contract()


################################################################################
# Award Certificate
################################################################################

accounts = w3.eth.accounts
account = accounts[0]
# Select or enter a recipient address using a Streamlit component
student_account = st.selectbox("Select Account", options=accounts)
# Enter a text string for the certificate or link to digital certificate location
certificate_details = st.text_input("Certificate Details", value="Fintech Certificate of Completion")
if st.button("Award Certificate"):
    # Call the awardCertificate function with web3
    contract.functions.awardCertificate(student_account, certificate_details).transact({"from":account, "gas": 1000000})
    transact({'from': account, 'gas': 10})

################################################################################
# Display Certificate
################################################################################
certificate_id = st.number_input("Enter a Certificate Token ID to display", value=0, step=1)
# @TODO: YOUR CODE HERE!
if st.button("Display Certificate"):
    # Get the certificate owner
    certificate_owner = contract.functions.ownerof(certificate_id).call()
    st.write(f"The certificate was awarded to {certificate_owner}")
    # Get the certificate's URI
    certificate_uri = contract.functions.tokenURI(certificate_id).call()
    st.write(f"The certificate's tokenURI metadata is {certificate_uri}")
