import json
import numpy as np
from pathlib import Path

def eval_recall_from_file(recalls_file, ground_truth_file, k_values=[1, 5, 10, 50]):
    """
    Evaluate Recall@K directly from a recall.json file.

    Args:
        recalls_file (str): Path to the JSON file containing model predictions.
        ground_truth_file (str): Path to the JSON file containing ground truth annotations.
        k_values (list): List of K values for Recall@K.

    Returns:
        dict: Recall@K values for the specified K values.
    """
    # Load predictions and ground truth
    with open(recalls_file, 'r') as f:
        predictions = json.load(f)

    with open(ground_truth_file, 'r') as f:
        ground_truth = json.load(f)

    # Convert ground_truth to the correct format
    if isinstance(ground_truth, list):
        ground_truth = {
            str(item['pairid']): item['img_set']['members']
            for item in ground_truth
        }

    # Initialize recall counters
    total_queries = len(ground_truth)
    recall_counts = {k: 0 for k in k_values}

    # Calculate recalls
    for query_id, targets in ground_truth.items():
        if query_id not in predictions:
            continue

        pred_ids = predictions[query_id]

        for k in k_values:
            if any(target in pred_ids[:k] for target in targets):
                recall_counts[k] += 1

    # Compute Recall@K as percentages
    recall_scores = {k: round(100.0 * recall_counts[k] / total_queries, 2) for k in k_values}
    return recall_scores

# Example usage
if __name__ == "__main__":
    recalls_file = "outputs/test/blip-large/cirr_ft-covr+gt/base/recalls_cirr.json"
    recalls_file = "outputs/test/blip-large/blip2-l-cirr_coco_coir+covr/base/recalls_cirr.json"
    ground_truth_file = "annotation/cirr/cap.rc2.test1.json"
    
    recall_scores = eval_recall_from_file(recalls_file, ground_truth_file)
    print("Recall@K scores:")
    for k, score in recall_scores.items():
        print(f"Recall@{k}: {score}%")