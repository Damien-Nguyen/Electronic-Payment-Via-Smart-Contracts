pragma solidity ^0.5.15;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract DLJ_token is ERC20, ERC20Detailed {
    string coin = "DLJ";
    uint price;
    bool is_buy_order;
    address payable public owner;
    uint public accountBalance;
    string account_holder = "Damien Nguyen";
    uint32 password = 123;
    uint32 eth_aud_rate = 2910;
    uint256 eth_DLJ_rate = 2910;
    uint256 aud_DLJ_rate = 1;
    uint32 input;

    constructor (uint initial_supply) ERC20Detailed ("DLJ_token", "DLJ", 18) public{
        owner=msg.sender;
        _mint(owner, initial_supply);
    }

       

    function getPassword(uint32 input_number) public returns(uint32) {
        
        return input = input_number;
        
    }

    modifier onlyOwner {

        require(input == password, "You do not have permission to mint these tokens!");
        _;
    }



    function mintDLJ(address recipient, uint amount) public onlyOwner{
        _mint(recipient, amount);
    }

    function transferEther(uint amount, address payable recipient) public onlyOwner{
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }

    function depositEther() public payable{}
    function() external payable{}


}