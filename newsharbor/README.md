# NewsharborAPI

## Overview
NewsharborAPI is a Python package for interacting with the New York Times News API. It provides easy access to various endpoints of the API, allowing users to fetch news sections, latest news, search news, and more.

## Installation
```bash
$ pip install newsharbor
```

## Usage

### Initialize the API
from newsharbor import NewsharborAPI
api = NewsharborAPI()

### Get Section List
sections = api.get_section_list()

### Get Latest News
latest_news = api.get_latest_news('world')

### Search News
search_results = api.search_news('technology')

### Get News Details
news_details = api.get_news_details('URL_HERE')

### Analyze News Data
data_analysis = api.analyze_news_data('world')

## Requrements
- Python 3.x
- requests
- pandas

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`newsharbor` was created by Angie Gao. It is licensed under the terms of the MIT license.

## Credits

`newsharbor` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
