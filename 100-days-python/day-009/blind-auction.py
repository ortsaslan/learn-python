# Program algorithm:
## Take and store Name and Bid of bidders from stdin.
## Compare stored bids and define the highest bid.
## Print out Name ang Bid of person with highest bid.

# Program realization:
## Define dictionary to store name:bid pair.
## Iterate over dictionary with for-loop:
### compare current item's key and value with previous ones, store highest k/v
### if current item is first store key/value in vars
## return winner's Name and Bid

# Define dictionary to store bidders data
bidders_and_bids = dict()

# Take bidders data from stdin
while True:
    name = input("\nEnter your name: ")
    bid = int(input("\nEnter your bid: $"))

    bidders_and_bids[name] = bid

    next_bidder = input("\nAre there any bidders? Type 'yes' or 'no': ")
    if next_bidder == "no":
        break

# Compare bids, define highest one
name = ""
bid = 0
for key in bidders_and_bids:
    if name == "" and bid == 0:
        name = key
        bid = bidders_and_bids[key]
    else:
        if bidders_and_bids[key] > bid:
            name = key
            bid = bidders_and_bids[key]

# Return winners data
print(f"\nThe winner is {name} with a bid of ${bid}.")