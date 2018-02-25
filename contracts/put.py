
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

GAS_ASSET_ID = b'\xe7-(iy\xeel\xb1\xb7\xe6]\xfd\xdf\xb2\xe3\x84\x10\x0b\x8d\x14\x8ewX\xdeB\xe4\x16\x8bqy,`'
OnSpend = RegisterAction('onSpend', 'to', 'amount', 'scripthash')

def Main(operation, dest, tag, amount):
    Stage(operation, dest, tag, amount)
    return Test(operation, dest, tag, amount)

def Test(operation, dest, tag, amount):
    return "fuck yeah"

def Stage(operation, dest, tag, amount):
    context = GetContext()
    src = getSource()
    dest_tag = concat(dest, tag)
    dest_tag_users = concat(dest_tag, "-users")
    dest_tag_src = concat(dest_tag, src)
    if operation == 'donate':
        donation = getValue()
        donate(context, dest_tag, dest_tag_users, dest_tag_src, src, donation)
        return "WOW I LOVE TO HACK THIS IS SO THRILLING"
    if operation == 'spend':
        spend(context, amount, src, dest, tag)
        return "Not yet functional"
    return "Invalid operation"


def getSource():
    tx = GetScriptContainer()
    references = tx.References
    reference = references[0]
    sender = GetScriptHash(reference)
    return sender

def getValue():
    tx = GetScriptContainer()
    references = tx.References
    reference = references[0]
    output_asset_id = GetAssetId(reference)
    if output_asset_id == GAS_ASSET_ID:
        for output in tx.Outputs:
            shash = GetScriptHash(output)
            value = GetValue(output) / 100000000
            remainder = value % 1
            value = value - remainder
            return value
    print("gas not found rip")
    return 0

#TODO: store maps of orgs : tags
def spend(context, amount, src, dest, tag):
    context = GetContext()
    org_tag = concat(src, tag)
    total = Get(context, org_tag)
    if not total:
        return False
    if amount > total:
        return False
    Delete(context, org_tag)
    new_total = total - amount
    Put(context, org_tag, new_total)
    receiver = GetExecutingScriptHash()
    OnSpend(dest, amount, receiver)
    return True


def donate(context, dest_tag, dest_tag_users, dest_tag_src, src, amount):
    total = Get(context, dest_tag)
    # This destination + tag already have donations
    if total:
        new_total = total + amount
        Put(context, dest_tag, new_total)
        donors = Get(context, dest_tag_users)
        # Donor has already donated previously
        if contains(donors, src):
            amount_donated = Get(context, dest_tag_src)
            amount_donated = amount_donated + amount
        # New donor, need to add to list
        else:
            donors = concat(donors, ",")
            donors = concat(donors, src)
            Delete(context, dest_tag_users)
            Put(context, dest_tag_users, donors)
            Put(context, dest_tag_src, amount)
    # First donation to this destination + tag
    else:
        Put(context, dest_tag, amount)
        Put(context, dest_tag_users, src)
        Put(context, dest_tag_src, amount)


def contains(string, substr):
    string_len = len(string)
    last_search_index = string_len - len(substr)
    substr_len = len(substr)
    for i in range(0, last_search_index):
        if substr(string, i, substr_len) == substr:
            return True
    return False

