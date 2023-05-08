# Analytics-selenium-

## Requirement

```bash
pip install beautifulsoup4
pip install selenium
pip install chromedriver-binary-auto

// highly recommend to reinstall when chrome version is updated
pip install chromedriver-binary-auto
```

### option (if selenium does not work)

```bash
pip install chromedriver-autoinstaller
```
```python
from selenium import webdriver
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
```
see: https://pypi.org/project/chromedriver-autoinstaller/
