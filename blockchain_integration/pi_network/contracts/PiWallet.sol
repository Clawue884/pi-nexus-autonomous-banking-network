pragma solidity ^0.8.0;

import "./PiNetwork.sol";

contract PiWallet {
    address public owner;
    PiNetwork public piNetwork;

    constructor() public {
        owner = msg.sender;
        piNetwork = PiNetwork(msg.sender);
    }

    function getAddress() public view returns (address) {
        return address(this);
    }

    function getWalletBalance() public view returns (uint256) {
        return piNetwork.piToken.balanceOf(address(this));
    }

    function deposit(uint256 _value) public {
        require(msg.sender == owner, "Only the owner can deposit");
        piNetwork.piToken.transferFrom(msg.sender, address(this), _value);
    }

    function withdraw(uint256 _value) public {
        require(msg.sender == owner, "Only the owner can withdraw");
        piNetwork.piToken.transfer(msg.sender, _value);
    }
}
