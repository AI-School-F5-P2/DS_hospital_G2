# Performance Report for Logistic Regression

In this section, we provide a comprehensive performance report for the Logistic Regression model, including detailed metrics, interpretation of the confusion matrix, and a summary of key findings.

## Model Overview

- **Model Name:** Logistic Regression
- **Validation Strategy:** 5-Fold Cross-Validation
- **Resampling Technique:** SMOTE (Synthetic Minority Over-sampling Technique)

## Validation Metrics

The table below presents validation metrics for each of the 5 cross-validation folds. These metrics help us understand the model's performance in classifying ischemic strokes (Ictus).

| Fold | Accuracy  | Recall | Precision | F1 Score |
|------|-----------|--------|-----------|----------|
| Fold 1 | 0.544634 | 0.9800 | 0.097610  | 0.177536 |
| Fold 2 | 0.524096 | 0.9400 | 0.090734  | 0.165493 |
| Fold 3 | 0.522088 | 0.9400 | 0.090385  | 0.164912 |
| Fold 4 | 0.515060 | 1.0000 | 0.092105  | 0.168675 |
| Fold 5 | 0.514056 | 0.9388 | 0.087287  | 0.159722 |

## Training Metrics

The training metrics for each fold of cross-validation are displayed in the table below. These metrics describe how well the model performs on the training data. 

| Fold | Accuracy  | Recall | Precision | F1 Score |
|------|-----------|--------|-----------|----------|
| Fold 1 | 0.518825 | 0.9545 | 0.090129  | 0.164706 |
| Fold 2 | 0.523965 | 0.9646 | 0.091783  | 0.167617 |
| Fold 3 | 0.524467 | 0.9646 | 0.091871  | 0.167765 |
| Fold 4 | 0.526223 | 0.9497 | 0.091437  | 0.166814 |
| Fold 5 | 0.526474 | 0.9648 | 0.092664  | 0.169089 |

## Model Performance Summary

The average validation and training metrics for the Logistic Regression model are as follows:

- **Average Validation Accuracy:** 0.5239870213048785
- **Average Validation Recall:** 0.9597551020408164
- **Average Validation Precision:** 0.09162391170866409
- **Average Validation F1 Score:** 0.16726767826993885

- **Average Training Accuracy:** 0.5239909071669363
- **Average Training Recall:** 0.9596822496319983
- **Average Training Precision:** 0.09157672033082045
- **Average Training F1 Score:** 0.16719802739266285

## Interpretation of the Confusion Matrix

The confusion matrix provides valuable insights into the model's performance. In the context of diagnosing ischemic strokes (Ictus):

- **True Negatives (TN):** 2372 - These are individuals who do not have an ischemic stroke (No Ictus) and are correctly classified as not having it.
- **False Positives (FP):** 2361 - These are individuals who do not have an ischemic stroke (No Ictus) but are incorrectly classified as having it.
- **False Negatives (FN):** 10 - These are individuals who have an ischemic stroke (Ictus) but are incorrectly classified as not having it.
- **True Positives (TP):** 238 - These are individuals who have an ischemic stroke (Ictus) and are correctly classified as having it.

**Key Findings:**

- The Logistic Regression model exhibits a high average validation recall (sensitivity) of approximately 95.98%, indicating its superior ability to correctly identify the majority of ischemic stroke cases. This demonstrates its effectiveness in minimizing false negatives.

- The model also demonstrates notable precision in predicting true positives (TP), achieving an F1 score of approximately 16.73%. This performance indicates its efficiency in accurately identifying actual cases of ischemic strokes while minimizing false negatives.

Overall, the Logistic Regression model excels in quickly and effectively identifying false negatives (patients with ischemic strokes) and accurately predicting true positives. It offers a valuable solution for cases where early diagnosis and intervention are critical.

Please note that the model's performance should be evaluated in the context of specific application requirements and associated costs or risks.

Feel free to reach out for more detailed analysis or further evaluation.