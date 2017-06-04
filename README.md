# 3bot-hook

Webhook handler for 3bot workflow execution. Basically for Github and Bitbucket but works with other POST requests as well.


## Installation

### Stable version from PyPI

	pip install threebot-hook

### Development version

```sh
$ pip install -e git+https://github.com/3bot/3bot-hook.git#egg=theebot_hook
```

```python

'threebot_hook',
'rest_framework.authtoken',
```

```python
url(r'^hooks/', include('threebot_hook.urls')),
```

## Credits

This is an adopted and adapted version of S. Andrew Sheppard's [django-github-hook](https://github.com/sheppard/django-github-hook).
