from nerformance.evaluator import evaluate


def test_evaluator_1():
    # Define predictions and ground truth entities
    predictions = ["New York", "Apple Inc.", "Samsung Electronics"]
    ground_truth = ["New York City", "Apple", "Samsung"]

    # Test exact matching
    exact_results = evaluate(predictions, ground_truth, match_type="exact")
    print("Exact Match Results:", exact_results)
    assert exact_results["precision"] == 0.0, "Precision should be 0 for exact matching."
    assert exact_results["recall"] == 0.0, "Recall should be 0 for exact matching."
    assert exact_results["f1"] == 0.0, "F1-score should be 0 for exact matching."

    # Test substring matching
    substring_results = evaluate(predictions, ground_truth, match_type="substring")
    print("Substring Match Results:", substring_results)
    assert substring_results["precision"] == 1.0, "Precision should be 1.0 for substring matching."
    assert substring_results["recall"] == 1.0, "Recall should be 1.0 for substring matching."
    assert substring_results["f1"] == 1.0, "F1-score should be 1.0 for substring matching."

    # Test relaxed matching with threshold 0.8
    relaxed_results = evaluate(predictions, ground_truth, match_type="relaxed", threshold=0.6)
    print("Relaxed Match Results:", relaxed_results)
    assert relaxed_results["precision"] > 0.0, "Precision should be greater than 0 for relaxed matching."
    assert relaxed_results["recall"] > 0.0, "Recall should be greater than 0 for relaxed matching."
    assert relaxed_results["f1"] > 0.0, "F1-score should be greater than 0 for relaxed matching."

    # Test relaxed matching with stricter threshold
    relaxed_results_strict = evaluate(predictions, ground_truth, match_type="relaxed", threshold=1.0)
    print("Relaxed Match (Threshold 1.0) Results:", relaxed_results_strict)
    assert relaxed_results_strict["precision"] == 0.0, "Precision should be 0 for threshold 1.0."
    assert relaxed_results_strict["recall"] == 0.0, "Recall should be 0 for threshold 1.0."
    assert relaxed_results_strict["f1"] == 0.0, "F1-score should be 0 for threshold 1.0."

    print("All tests passed successfully!")




def test_evaluator_2():
    # Define predictions and ground truth entities
    predictions = ["New York", "12/01/2024"]
    ground_truth = ["New York", "12/01/2024"]

    # Test exact matching
    exact_results = evaluate(predictions, ground_truth, match_type="exact")
    print("Exact Match Results:", exact_results)
    assert exact_results["precision"] == 1.0, "Precision should be 1 for exact matching."
    assert exact_results["recall"] == 1.0, "Recall should be 1 for exact matching."
    assert exact_results["f1"] == 1.0, "F1-score should be 1 for exact matching."

    # Test substring matching
    substring_results = evaluate(predictions, ground_truth, match_type="substring")
    print("Substring Match Results:", substring_results)
    assert substring_results["precision"] == 1.0, "Precision should be 1.0 for substring matching."
    assert substring_results["recall"] == 1.0, "Recall should be 1.0 for substring matching."
    assert substring_results["f1"] == 1.0, "F1-score should be 1.0 for substring matching."

    # Test relaxed matching with threshold 0.8
    relaxed_results = evaluate(predictions, ground_truth, match_type="relaxed", threshold=0.8)
    print("Relaxed Match Results:", relaxed_results)
    assert relaxed_results["precision"] > 0.0, "Precision should be greater than 0 for relaxed matching."
    assert relaxed_results["recall"] > 0.0, "Recall should be greater than 0 for relaxed matching."
    assert relaxed_results["f1"] > 0.0, "F1-score should be greater than 0 for relaxed matching."


    print("All tests passed successfully!")




if __name__ == "__main__":

    test_evaluator_2()

    test_evaluator_1()
