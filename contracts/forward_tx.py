from boa.blockchain.vm.Neo.Runtime import Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification

from boa.blockchain.vm.Neo.TransactionType import InvocationTransaction
from boa.blockchain.vm.Neo.Transaction import *

from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.code.builtins import concat, range

onForward = RegisterAction('spend', 'to', 'amount', 'scripthash')

def Main(dest):
    scriptHash = GetExecutingScriptHash()
    tx = GetScriptContainer()
    references = tx.References
    reference = reference[0]
    Notify(reference)
    for output in tx.Outputs:
        hash = GetScriptHash(output)
        value = GetValue(output) / 100000000
        remainder = value % 1
        value = value - remainder
    Notify(value)
    onForward(dest, value, scriptHash)
    return True

