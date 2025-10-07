# conftest.py
def pytest_benchmark_generate_json(
    config, benchmarks, include_data, machine_info, commit_info
):
    results = []
    for b in benchmarks:
        stats = b["stats"]
        results.append(
            {
                "name": b["name"],
                "min": stats.min,
                "max": stats.max,
                "mean": stats.mean,
                "stddev": stats.stddev,
                "rounds": stats.rounds,
            }
        )

    return {
        "machine_info": {
            "processor": machine_info.get("processor"),
            "system": machine_info.get("system"),
        },
        "benchmarks": results,
    }
