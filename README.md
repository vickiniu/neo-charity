# NeoCharity: Improving Charity Transparency via NEO
Charities receive hundreds of billions of dollars in donor money, yet donors can’t reliably earmark their donations for specific causes, and the vast majority of charities do not report full itemized purchase transactions. This tacit trust donors give charities can be formalized with a guaranteed way for donated money to be used in its intended purpose and then this money could be tracked to see how it was actually used. 

This seems like a perfect task for smart contracts on the blockchain. For donors, decentralization and transparency ensure money is used as desired. For charities, automatic, secure purchase reporting reduce the tremendous burden of accounting. 

Our solution leverages the NEO blockchain to create such a system:
* donors make payments to a smart contract with a charity and an earmark tag
* these payments are placed in a special account
* charities can access and use these different accounts
* all transfers are logged with amount and transactor
* donors and charities can easily query to see who has transacted with a tagged account

This system is exciting because it can be applied to any system where earmarked, transparent transactions would be usable:
* A company department creating itemized budgets for teams
* A robotics student organization receiving money that may only be used for food or equipment. 
* A family earmarking a monthly budget, so they limit their spending per category.


See our [presentation](https://docs.google.com/presentation/d/1uTzur0-ZHdC7Twp69CWRT6A6uaP8s8DBeZ4fs5kX9bw/edit?usp=sharing) for more detail



# NEO Resources
[Docker image](https://hub.docker.com/r/cityofzion/neo-privatenet/)
     - Recommend that you run on AWS to run a private net
     - Already has 1000 blocks generated + wallet with NEO

