# Using Arbitrary Keyword Arguments
# **user_info it accepts an 
# arbitrary number of keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# The function build_profile() accepts an arbirary number of keyword arguments
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)