from boa.blockchain.vm.Neo.Runtime import Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification

from boa.blockchain.vm.Neo.TransactionType import InvocationTransaction
from boa.blockchain.vm.Neo.Transaction import *

from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete

GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'
OnSpend = RegisterAction('onSpend', 'to', 'amount', 'scripthash')


def Main(num):
	receiver = GetExecutingScriptHash()

	tx = GetScriptContainer()
	references = tx.References
	reference = references[0]
	sender = GetScriptHash(reference)

	output_asset_id = GetAssetId(reference)
	if output_asset_id == GAS_ASSET_ID:
		print("good")

	for output in tx.Outputs:
		shash = GetScriptHash(output)
		value = GetValue(output) / 100000000
		remainder = value % 1
		value = value - remainder
		OnSpend(b'AFxLPTwPoxowEHvvYYd5RKfJ3VqMTwh4pm', value, receiver)
		return num

	return 0

