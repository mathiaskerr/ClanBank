from models.transaction import Transaction

def  total_spend(transactions):
    total = 0
    for transaction in transactions:
        total += transaction.amount
    return total    

def over_under_budget(budget, total):
    spend = budget - total
    if spend > 0:
        spending = f'£{spend} under budget'
    else:
        spending = f'£{spend * -1} over Budget'   
    return spending     


def  transaction_by_tag(tag, transactions):
    transaction_tag = []
    for transaction in transactions:
        if transaction.tag == tag:
            transaction_tag.append(transaction)
    return transaction_tag        


def tags_index(transactions):
    tags=[]
    for transaction in transactions:
        if transaction.tag not in tags:
            tags.append(transaction.tag)
    return tags        
    