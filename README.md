# EmojiGuessr

<!-- The badge should be replaced by the actual CI badge -->
[![](https://github.com/swe-students-fall2025/3-python-package-team_saffron/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_saffron/actions/workflows/build.yaml)

[![](https://github.com/swe-students-fall2025/3-python-package-team_saffron/actions/workflows/deliver.yaml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_saffron/actions/workflows/deliver.yaml)

Link to PyPI: []()

EmojiGuessr is a Python package that turns emoji strings into quick guessing games. Pick a theme, get an emoji clue and guess the name!

## Features

-  **Multiple Themes**: Choose from 7 different themes including food, animals, movies, games, cities, feelings, and dev
-  **Customizable Difficulty**: Adjust the number of questions, attempts per question, and matching rules
-  **Flexible Matching**: Support for partial matches and case-sensitive/insensitive answers
-  **Easy CLI**: Simple command-line interface with helpful flags and options

## Team Members
[Jason Liu](https://github.com/jsl1114)

[David Shen](https://github.com/snazzybeatle115)

[Leon Lian](https://github.com/ll5373128)

member4

member5

## Installation

### From Test PyPI
```sh
pipenv install -i https://test.pypi.org/simple/emojiguessr
```

### From Source
```sh
git clone https://github.com/swe-students-fall2025/3-python-package-team_saffron.git
cd 3-python-package-team_saffron
pipenv install -e .
```

## Usage

### Basic Usage

Run the game with default settings (3 questions, food theme):
```sh
pipenv run emojiguessr
```

### Advanced Usage

**Choose a different theme:**
```sh
pipenv run emojiguessr --theme animals
```

**Customize the number of questions:**
```sh
pipenv run emojiguessr -n 5
```

**Allow multiple attempts per question:**
```sh
pipenv run emojiguessr --max-attempts 3
```

**Enable case-sensitive matching:**
```sh
pipenv run emojiguessr --case-sensitive
```

**Disable partial matches (require exact answers):**
```sh
pipenv run emojiguessr --no-partial
```

**Combine multiple options:**
```sh
pipenv run emojiguessr -t movies -n 10 -a 2
```

### Available Themes

You can list all available themes using:
```sh
pipenv run emojiguessr --list-themes
```

Current themes include:
- `food` - Pizza, sushi, burger, and more
- `animals` - Dog, cat, panda, lion, etc.
- `movies` - Famous movies represented by emojis
- `games` - Various types of games
- `cities` - World cities
- `feelings` - Different emotions
- `dev` - Programming and development concepts

### Command Reference

List of flags you can add to customize the behavior of `emojiguessr`

```sh
Available commands:
  --num-questions, -n    : Number of questions to ask (default: 3)
  --theme, -t            : Emoji theme to use (default: food)
  --case-sensitive       : Make answers case-sensitive (default: off)
  --no-partial           : Disable partial matches
  --max-attempts, -a     : Maximum number of attempts per question (default: 1)
  --list-themes, -lt     : List available themes and exit
  --list-commands, -lc   : List available commands and exit
```



## Develop and Contribute

### Local build & run (using `pipenv`)
1. Get [`pipenv`](https://pipenv.pypa.io/en/latest/installation.html) installed
2. `cd` into the project directory
3. Install dependencies: `pipenv install`
4. Install the package in editable mode: `pipenv install -e .`
5. Run the command line interface: `pipenv run emojiguessr` followed by flags and configurations

### Project Structure
```
.github/
  workflows/
    build.yaml
    deliver.yaml
    event-logger.yml
    Pipfile
    Pipfile.lock
    requirements.txt
  note.txt
src/
  emojiguessr/
    __init__.py
    __main__.py
    data.py
    quiz.py
    score.py
tests/
  __init__.py
  test_data.py
examples/
  demo.py
pyproject.toml
Pipfile
Pipfile.lock
LICENSE
README.md
instructions.md
.gitignore
```

### Testing
Testing is implemented with `pytest` and runs automatically on every pull request. If you wish to run tests locally anytime, simply run
```sh
pytest -v
```
if you have `pytest` installed through `pipenv`, do
```sh
pipenv run pytest -v
```

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure everything works
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
