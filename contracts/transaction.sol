pragma solidity ^0.5.15;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract DLJ_token is ERC20, ERC20Detailed {
    string coin = "DLJ";
    uint price;
    bool is_buy_order;
    address payable public buyer_account = 0x43701789562E7DE833C1f718DfBe5f7DDaaee77B;
    address payable seller_account = 0x33061519E0A83DE0d3B58E74F3e3e88cAF61a251;
    uint public accountBalance;
    string account_holder = "Damien Nguyen";
    uint32 eth_aud_rate = 2910;
    uint256 eth_DLJ_rate = 2910;
    uint256 aud_DLJ_rate = 1;

    function Transfer_Ether(uint amount, address payable recipient) public {
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }    

    modifier onlyOwner {
        require(msg.sender == buyer_account, "You do not have permission to mint these tokens!");
        _;
    }

    constructor (uint initial_supply) ERC20Detailed ("DLJ_token", "DLJ", 18) public{
        buyer_account=msg.sender;
        _mint(buyer_account, initial_supply);
    }

    function Transfer_DLJ(address recipient, uint amount) public onlyOwner{
        _mint(recipient, amount);
    }

    function Deposit_Ether() public payable{}
    function() external payable{}


}
