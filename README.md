# Electronic Payments Via Smart Contracts 
![istockphoto-1266975549-612x612.png](./Photos/istockphoto-1266975549-612x612.jpg)
Development of Electronic Payment System Using Smart Contract

## Goal

The project team work together to develop a paymwent smart contract to facilitate each transaction of money transfer;

## Functions of Product

* Develop a payment system using smart contract to settle transactions;
* Each transaction is recorded on a smart contract and done via this smart contract;
* Let's say Damien wants to sell a product to Luis for $10;
* Damien uses the developed payment system to enter the dollar values for Luis to pay via that system;
* Damien is allowed to link his account to the system and all the payment will be deposited to his account via the function of the smart contract;
* Luis can enter his account into the smart contract to transfer the $10 to Damien account via this smart contract;
* In the end, both Damien and Luis are able to view the balances of their respective accoutn to confirm the completion of the transaction without errors;
* Transactions use Etherum (wei or ether) as medium to conduct the money exchange and then exchange the ether or wei back to the actual dollar values. 
* Each side shoudl have records of their dollar values. When a transaction is needed, certain amount of dollars need to be exchanged to ether or wei automatically. The ether or wei then will be sent to the seller by the buyer to make the payment. 
* The seller account receives the ether or wei and then exchange them into dollar value whcih is added to his account balance.

## Software, Libraries and API

Softwares:

* Solidity
* python

Libraries:

* os
* json
* web3
* pathlib
* dotenv
* streamlit
* visual code

API:

* Ganache
* Remix

## Implementation Steps

* Establish the parties for the transactions. We set up two parties for each trasnaction contract. One is the seller, the other is the buyer. 

* The contract needs to have gas fee and charge fee for each transaction.

* The contract needs to allow both buyer and seller to enter their wallet accoutn address for transferrign or saving money.

* The transation will be conducted by using stable coins, digital currency or cryptocurrency which we can develop. 

*

## Dashboard for AUD_Pegged Token

* Given we are using a token that is pegged to the AUD, we felt it was appropiate to display the real-time conversion rates across other currencies for the AUD.
* This is also a useful additional given the conversion rate we are using int he smart contract is static.

![Photos/Screen Shot 2023-06-05 at 8.24.30 pm.png](https://github.com/Explictz/Project-3/blob/main/Photos/Screen%20Shot%202023-06-05%20at%208.24.30%20pm.png)
