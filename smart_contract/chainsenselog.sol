// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChainSenseLog {
    struct Log {
        string dataHash;
        uint timestamp;
    }

    Log[] public logs;

    function addLog(string memory _hash) public {
        logs.push(Log(_hash, block.timestamp));
    }

    function getLog(uint _index) public view returns (string memory, uint) {
        require(_index < logs.length, "Invalid index");
        Log memory log = logs[_index];
        return (log.dataHash, log.timestamp);
    }

    function getTotalLogs() public view returns (uint) {
        return logs.length;
    }
}
