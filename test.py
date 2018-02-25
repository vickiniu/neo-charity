from neo.contrib.smartcontract import SmartContract

@smart_contract.on_notify
def test_notify(event):
    print("Hello World")
