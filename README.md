![CI](https://github.com/yourname/narada/actions/workflows/ci.yml/badge.svg)
# narada

```
 _   _              _
| \ | |            | |
|  \| | __ _ _ __  | |__   __ _ _ __
| . ` |/ _` | '_ \ | '_ \ / _` | '__|
| |\  | (_| | | | || | | | (_| | |
\_| \_/\__,_|_| |_||_| |_|\__,_|_|
```

Narada is a local reasoning assistant reimagined from open-source roots. It runs entirely offline and integrates with macOS for notifications.

## Quickstart on macOS

```bash
brew install --file Brewfile
scripts/install.sh
narada "draft meeting agenda" --notify
```

## Developer Guide

- **src/**: source code
- **tests/**: pytest suite
- **docs/**: design docs
- **scripts/**: helper scripts

Run tests with `pytest`.

## Contributing

Please see `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` for guidelines.

