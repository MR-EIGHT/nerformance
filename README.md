# **Nerformance**

![Python Version](https://img.shields.io/badge/python-3.x-blue)  
**Nerformance** is a Python library designed for evaluating the performance of Named Entity Recognition (NER) models. It provides flexible matching options, including exact, substring, and relaxed matching, to give users control over evaluation strictness.

---

## **Features**
- **Flexible Matching**:
  - **Exact Matching**: Matches entities that are identical in both prediction and ground truth.
  - **Substring Matching**: Matches if the prediction overlaps with the ground truth.
  - **Relaxed Matching**: Uses Levenshtein similarity to evaluate near matches.
- **Comprehensive Metrics**:
  - Precision
  - Recall
  - F1-score
- **Threshold Control**: Fine-tune the relaxed matching behavior by setting similarity thresholds.

---

## **Installation**

Clone the repository and install the library locally:
```bash
git clone https://github.com/yourusername/nerformance.git
cd nerformance
pip install -e .
```



## **Usage**

Clone the repository and install the library locally:
```python
from nerformance.evaluator import evaluate

# Define predictions and ground truth
predictions = ["New York", "Apple Inc.", "Samsung Electronics"]
ground_truth = ["New York City", "Apple", "Samsung"]

# Exact Matching
results_exact = evaluate(predictions, ground_truth, match_type="exact")
print("Exact Matching Results:", results_exact)

# Substring Matching
results_substring = evaluate(predictions, ground_truth, match_type="substring")
print("Substring Matching Results:", results_substring)

# Relaxed Matching with Threshold
results_relaxed = evaluate(predictions, ground_truth, match_type="relaxed", threshold=0.8)
print("Relaxed Matching Results:", results_relaxed)
```

## **Output**

```
{
    "precision": 0.67,
    "recall": 0.67,
    "f1": 0.67
}
```

## **TO DO**
* Test the correctness.


## **Authors**
* **MR-EIGHT** (Mehrdad Heshmat)