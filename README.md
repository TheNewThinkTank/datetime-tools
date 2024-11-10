
[![codecov](https://codecov.io/gh/TheNewThinkTank/datetime-tools/branch/main/graph/badge.svg?token=CKAX4A3JQF)](https://codecov.io/gh/TheNewThinkTank/datetime-tools)

<!-- [![codecov](https://codecov.io/gh/TheNewThinkTank/datetime-tools/graph/badge.svg?token=8BBDs8MwJv)](https://codecov.io/gh/TheNewThinkTank/datetime-tools) -->

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
