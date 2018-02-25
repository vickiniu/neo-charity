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

def Main(operation, src, dest, tag, amount):
    return Stage(operation, src, dest, tag, amount)
    # context = GetContext()
    # dest_tag = concat(dest, tag)
    # dest_tag_users = concat(dest_tag, "-users")
    # dest_tag_src = concat(dest_tag, src)
    # return getTotal(context, dest_tag)
    # return getExpense(context,'redcross','salary','gm')
    # return getSpenders(context,'redcross','salary')

def Stage(operation, src, dest, tag, amount):
    context = GetContext()
    dest_tag = concat(dest, tag)
    dest_tag_users = concat(dest_tag, "-users")
    dest_tag_src = concat(dest_tag, src)
    if operation == 'donate':
        donate(context, dest_tag, dest_tag_users, dest_tag_src, src, amount)
        return "WOW I LOVE TO HACK THIS IS SO THRILLING"
    if operation == 'getTotal':
        # TODO: format total
        return getTotal(context, dest_tag)
    if operation == 'getDonors':
        return getDonors(context, dest_tag_users)
    if operation == 'getDonation':
        return getDonation(context, dest_tag_src)
    if operation == 'spend':
        return spend(context, amount,src,dest,tag)
    if operation == 'getExpense':
        return getExpense(context,src,tag,dest)
    if operation == 'getSpenders':
        return getSpenders(context,src,tag,dest)
    return "Invalid operation"

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
    
    org_tag_users = concat(org_tag, "-users")
    org_tag_users = concat(org_tag_users, "-exp")
    org_tag_dest = concat(org_tag, dest)
    org_tag_dest = concat(org_tag_dest, "-exp")
    Put(context, org_tag_users, dest)
    Put(context, org_tag_dest, amount)
    return True

def getExpense(context,src,tag,dest):
    org_tag = concat(src, tag)
    org_tag_dest = concat(org_tag, dest)
    org_tag_dest = concat(org_tag_dest, "-exp")
    return Get(context, org_tag_dest)

def getSpenders(context,src,tag):
    org_tag = concat(src, tag)
    org_tag_users = concat(org_tag, "-users")
    org_tag_users = concat(org_tag_users, "-exp")
    return Get(context, org_tag_users)

# :return: int, total amount donated to org + tag
def getTotal(context, dest_tag):
    return Get(context, dest_tag)

# :return: string, all users that have donated to org + tag
def getDonors(context, dest_tag_users):
    return Get(context, dest_tag_users)

# :return: int, amount user has donated to org + tag
def getDonation(context, dest_tag_src):
    return Get(context, dest_tag_src)

def donate(context, dest_tag, dest_tag_users, dest_tag_src, src, amount):
    total = Get(context, dest_tag)
    # This destination + tag already have donations
    # if total:
    #     new_total = total + amount
    #     Put(context, dest_tag, new_total)
    #     donors = Get(context, dest_tag_users)
    #     # Donor has already donated previously
    #     if contains(donors, src):
    #         amount_donated = Get(context, dest_tag_src)
    #         amount_donated = amount_donated + amount
    #         # Put(context, dest_tag_src, amount_donated)
    #     # New donor, need to add to list
    #     else:
    #         donors = concat(donors, ",")
    #         donors = concat(donors, src)
    #         Delete(context, dest_tag_users)
    #         Put(context, dest_tag_users, donors)
    #         Put(context, dest_tag_src, amount)
    # # First donation to this destination + tag
    # else:
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

