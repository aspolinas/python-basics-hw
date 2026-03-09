"""Simple data analysis script using Python basics."""


def analyze_numbers(numbers: list[int | float]) -> dict:
    """Return basic statistics for a list of numbers."""
    if not numbers:
        return {"count": 0, "sum": 0, "mean": 0, "min": None, "max": None}

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


def filter_above_mean(numbers: list[int | float]) -> list:
    """Return numbers that are above the mean."""
    stats = analyze_numbers(numbers)
    return [n for n in numbers if n > stats["mean"]]


if __name__ == "__main__":
    data = [23, 45, 12, 67, 34, 89, 2, 56, 78, 41]

    print("Input data:", data)
    stats = analyze_numbers(data)
    for key, value in stats.items():
        print(f"  {key}: {value}")

    above = filter_above_mean(data)
    print(f"\nAbove mean ({stats['mean']:.1f}): {above}")
