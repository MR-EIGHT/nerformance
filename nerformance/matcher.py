from .utils import levenshtein_similarity

def exact_match(predicted, ground_truth):
    return set(predicted) & set(ground_truth)


def substring_match(predicted, ground_truth, strictness=0.5):
    """
    Find substring matches between predicted and ground truth entities, with a strictness threshold.
    
    Args:
        predicted (list): List of predicted entity strings.
        ground_truth (list): List of ground truth entity strings.
        strictness (float): A value between 0 and 1. Defines the minimum overlap ratio required for a match.
                           1.0 = exact match, 0.5 = 50% overlap, 0 = any substring match.
                           
    Returns:
        set: A set of tuples representing matched (predicted, ground_truth) pairs.
    """
    matches = set()
    
    for pred in predicted:
        for gt in ground_truth:
            # Calculate overlap ratio
            overlap_length = len(set(pred) & set(gt))
            pred_ratio = overlap_length / len(pred) if len(pred) > 0 else 0
            gt_ratio = overlap_length / len(gt) if len(gt) > 0 else 0
            
            # Check strictness condition
            if pred_ratio >= strictness or gt_ratio >= strictness:
                matches.add((pred, gt))
    
    return matches


def relaxed_match(predicted, ground_truth, threshold=0.8):
    """
    Find relaxed matches based on Levenshtein similarity.

    Args:
        predicted (list): List of predicted entity strings.
        ground_truth (list): List of ground truth entity strings.
        threshold (float): Minimum similarity score to consider a match.

    Returns:
        set: A set of tuples representing matched (predicted, ground_truth) pairs.
    """
    matches = set()
    for pred in predicted:
        for gt in ground_truth:
            similarity = levenshtein_similarity(pred, gt)
            if similarity >= threshold:
                matches.add((pred, gt))
    return matches






if __name__ == "__main__":
    predicted = ["New York", "Apple Inc."]
    ground_truth = ["New York City", "Apple"]

    # Relaxed matching (default strictness = 0.5)
    matches_relaxed = substring_match(predicted, ground_truth)
    print("Relaxed Matching:", matches_relaxed)

    # Stricter matching (strictness = 0.8)
    matches_strict = substring_match(predicted, ground_truth, strictness=0.8)
    print("Strict Matching:", matches_strict)

    # Exact matching (strictness = 1.0)
    matches_exact = substring_match(predicted, ground_truth, strictness=1.0)
    print("Exact Matching:", matches_exact)