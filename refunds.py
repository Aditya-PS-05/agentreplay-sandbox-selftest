def issue_refund(amount, approval_id=None):
    # BUG: issues a refund with no approval check
    return {"refunded": amount}
