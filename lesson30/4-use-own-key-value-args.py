def build_profile(firstname, lastname, **userinfo):
    userinfo['first_name'] = firstname
    userinfo['last_name'] = lastname
    return userinfo
user_profile = build_profile('Sina', 'Sasani', 
                             location='Tehran',
                             field='NestJS')
print(user_profile)