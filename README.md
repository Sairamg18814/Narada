# AgenticSeek

AgenticSeek is a fully offline reasoning assistant rewritten from scratch.
It runs natively on macOS with Apple Silicon acceleration and provides an
interactive Codex-like code helper. The project avoids external APIs by using
local language models via `llama-cpp-python`.

## Quickstart on macOS

```bash
# install brew packages and Python dependencies
make install

# run a simple planning task
agentic-seek plan "draft meeting agenda" --notify

# ask the Codex assistant
agentic-seek codex "show an example of a python loop"
```

Place a quantized Llama model in `models/llama.bin` or set the environment
variable `AGENTIC_SEEK_MODEL` to the model path. A helper script is provided
in `scripts/setup_local_llm.sh`.

## Repository Layout

- `src/agentic_seek/` – core modules
- `models/` – location for local LLM files
- `tests/` – unit tests runnable with `make test`
- `scripts/` – installation helpers

## Development

Run tests and measure coverage:

```bash
make test
```

## License

This project is released under the MIT License.
