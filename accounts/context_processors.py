def account_number(request):
    if request.user.is_authenticated:
        return {'account_number': request.user.account.account_no}
    else:
        return {'account_number': None}
    

def account_type(request):
    if request.user.is_authenticated:
        return {'account_type': request.user.account.account_type}
    else:
        return {'account_type': None}