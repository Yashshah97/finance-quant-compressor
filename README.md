# Finance Quant Compression Tool

This open-source compression tool is designed to efficiently compress market time series and risk metrics data, utilizing a domain-specific encoding approach that balances compression ratio with fast decompression times. Built from the ground up in pure Python, it includes comprehensive testing and documentation for seamless integration into your workflow. By leveraging this tool, you can significantly reduce storage requirements and improve data processing speeds.

## What makes it unique

Combines market time series and risk metrics with a domain-tuned encoder with ratio benchmarks — a niche where few ready-made tools exist.

## Features

- **`finance_quant_compressor/encoder.py`** — Domain-tuned encoder implementation
- **`finance_quant_compressor/benchmarks.py`** — Ratio benchmarks and comparison functions
- **`finance_quant_compressor/metrics.py`** — Risk metric calculations and aggregation
- **`finance_quant_compressor/utils.py`** — Utility functions for data processing and compression
- **`finance_quant_compressor/tests_test_encoder.py`** — Unit tests for the encoder implementation
- **`finance_quant_compressor/core.py`** — main domain logic and public entry points

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/finance-quant-compressor.git
cd finance-quant-compressor

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
finance-quant-compressor/
├── finance_quant_compressor/
│   ├── encoder.py
│   ├── benchmarks.py
│   ├── metrics.py
│   ├── utils.py
│   ├── tests_test_encoder.py
│   ├── core.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **finance-quant** · Archetype: **compressor** ·
Built autonomously by JARVIS on 2026-10-29. MIT licensed.
