from .matcher import *
from .metrics import *

def evaluate(predictions, ground_truth, match_type="exact", threshold=0.8):
    if match_type == "exact":
        matches = exact_match(predictions, ground_truth)
    elif match_type == "substring":
        matches = substring_match(predictions, ground_truth)
    elif match_type == "relaxed":
        matches = relaxed_match(predictions, ground_truth, threshold=threshold)
    else:
        raise ValueError("Invalid match_type. Use 'exact', 'substring', or 'relaxed'.")

    tp = len(matches)
    fp = len(predictions) - tp
    fn = len(ground_truth) - tp

    p = precision(tp, fp)
    r = recall(tp, fn)
    f1 = f1_score(p, r)

    return {"precision": p, "recall": r, "f1": f1}
