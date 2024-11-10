
<a href="https://pypi.org/project/datetime-convertion-tools/">
<img src="https://img.shields.io/pypi/v/datetime-convertion-tools.svg">
</a>
<a href="https://github.com/TheNewThinkTank/msgspec/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/TheNewThinkTank/datetime-tools.svg">
</a>

![PyPI Downloads](https://img.shields.io/pypi/dm/datetime-convertion-tools)
![CI](https://github.com/TheNewThinkTank/datetime-tools/actions/workflows/wf.yml/badge.svg)
[![codecov](https://codecov.io/gh/TheNewThinkTank/datetime-tools/branch/main/graph/badge.svg?token=CKAX4A3JQF)](https://codecov.io/gh/TheNewThinkTank/datetime-tools)
![commit activity](https://img.shields.io/github/commit-activity/m/TheNewThinkTank/datetime-tools)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/datetime-tools?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/datetime-tools/archive/refs/heads/main.zip)

# datetime-tools

Common datetime operations

## Installation

```BASH
pip install datetime-convertion-tools
```

## Usage example

Importing

```Python
from datetime_tools.get_year_and_week import get_year_and_week
from datetime_tools.get_duration import get_duration_minutes
```

Usage

```Python
get_year_and_week("2022-10-29")
get_duration_minutes("14:45", "15:10")
```

<!--
## Create a new release

example:

```BASH
git tag 0.0.1
git push origin --tags
```

release a patch:

```BASH
poetry version patch
```

then `git commit`, `git push` and

```BASH
git tag 0.0.2
git push origin --tags
```
-->
