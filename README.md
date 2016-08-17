# unittest-localhost
========

unittest-based test runner that warns if a test makes network requests

### Example Django usage:

Application settings.py:

```python
TEST_RUNNER = 'localhostrunner.djangotestrunner.LocalhostTestRunner'
```

Shell:

```shell
$ ./manage.py test
```
