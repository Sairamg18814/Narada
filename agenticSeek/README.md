# agenticSeek

A lightweight command line tool for planning tasks and answering coding questions using a local language model accelerated on Apple Silicon.

## Installation (Apple M1/M2)

1. Install dependencies with Homebrew:

```bash
brew install python3 git
```

2. Clone this repository and install the package:

```bash
pip install .
```

3. Download a quantized LLM (for example, a llama.cpp model) and set `AGENTIC_SEEK_MODEL` to its path.

## Running the Local LLM

The project expects a local backend such as `llama.cpp` compiled with Metal or Accelerate. Set up the backend separately and ensure the `generate` function in `agentic_seek.__init__` invokes it. By default the package returns an echo of your prompt.

## Usage

```bash
agentic-seek plan "organize my tasks"
agentic-seek codex "how to write a list comprehension in Python?"
```

### Troubleshooting

If you encounter `Makefile:*** missing separator` when running `make install`, ensure each command line in the Makefile starts with a **TAB** character.

If your shell reports `agentic-seek: command not found`, run `pip install .` again and verify that your Python `bin` directory is in `PATH`.

