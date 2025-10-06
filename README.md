# Benchflow

## Introduction

This repository is an example implementation of CI/CD for Python benchmarks using GitHub Actions. It demonstrates how to automate benchmarking workflows, collect results, and maintain benchmark data within a project.

## How it works

- The GitHub Actions workflow `on_pr.yml` is triggered on pull requests.
- The `create-bench` job runs the benchmarks using `pytest-benchmark` and uploads the results as artifacts.
- The `gather-bench` job downloads these artifacts, merges the benchmark results into a single JSON file, and commits the updated results back to the repository.

Benchmarks are written using the `pytest-benchmark` plugin. The JSON output is simplified through customizations in `conftest.py` to make the results easier to analyze.

## Usage

To run the benchmarks locally, use the following command:

```bash
pytest --benchmark-only
```

This will execute the benchmarks and output the results without running other tests.

## File Structure

```
.
├── bench
│   ├── conftest.py
│   └── test_fib.py
├── benchmark-results
│   └── result.json
├── benchmark.json
├── README.md
├── requirements.txt
└── src
    └── fib.py
```

- `bench/` contains benchmark test files and configuration for simplifying benchmark output.
- `benchmark-results/` stores the collected benchmark results in JSON format.
- `benchmark.json` is the consolidated benchmark results file updated by the CI/CD workflow.
- `src/` holds the source code files being benchmarked.
- `requirements.txt` lists the project dependencies.
