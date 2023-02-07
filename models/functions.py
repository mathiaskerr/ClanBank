

def total(transactions):
    total = 0
    for transaction in transactions:
        total += transaction.amount

def over_under_budget(budget, total):
    spend = budget - total
    if spend > 0:
        spending = f'£{spend} under budget'
    else:
        spending = f'£{spend * -1} over Budget'    


def  transaction_by_tag(transactions):
    transaction_tag = []
    for transaction in transactions:
        if transaction.tag == tag:
            transaction_tag.append(transaction)




        tags=[]
    for transaction in transactions:
        if transaction.tag not in tags:
            tags.append(transaction.tag)
    