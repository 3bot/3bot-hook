# 3bot-hook

Webhook handler for 3bot workflow execution. Basically for Github and Bitbucket but works with other POST requests as well.


## Installation 

### Stable version from PyPI

	pip install

### Development version
 
	pip install -e git+https://github.com/3bot/3bot-hook.git#egg=theebot_hook

###	

    'threebot_hook',
    'rest_framework.authtoken',
###
	
    url(r'^hooks/', include('threebot_hook.urls')),
	



"""
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

an_user = User.objects.get(username="phi")
token = Token.objects.create(user=an_user)
print token.key
"""

## Credits

This is a adopted and adapted version of S. Andrew Sheppard's [django-github-hook](https://github.com/sheppard/django-github-hook).