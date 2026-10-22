"""
Automated Verification Script for Digital Arrest & Cyber Fraud Shield
Tests detector initialization, latency, preset samples, and dataset evaluation.
"""

import sys
import io

# Ensure UTF-8 output on Windows consoles
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import time
from detector import FraudDetector, CATEGORIES
from dataset import get_dataset, PRESET_SAMPLES

def run_verification():
    print("=" * 60)
    print("[*] Initializing Digital Arrest & Cyber Fraud Shield...")
    print("=" * 60)
    t0 = time.perf_counter()
    detector = FraudDetector()
    init_time = (time.perf_counter() - t0) * 1000
    print(f"[OK] FraudDetector initialized & model trained in {init_time:.2f} ms")

    print("\n" + "=" * 60)
    print("[*] Testing 5 Standard Presets...")
    print("=" * 60)
    for name, sample_text in PRESET_SAMPLES.items():
        if not sample_text:
            continue
        res = detector.analyze(sample_text)
        print(f"\nScenario: {name}")
        print(f"  Risk Level: {res['risk_level']} ({res['risk_score_pct']}%)")
        print(f"  Latency: {res['latency_ms']} ms")
        print(f"  Flagged Spans: {len(res['spans'])}")
        for s in res['spans']:
            print(f"    [{s['category_name']}] '{s['phrase']}' -> {s['explanation']}")
        print(f"  Guidance: {res['guidance']}")

    print("\n" + "=" * 60)
    print("[*] Evaluating on Built-in 60-Sample Dataset...")
    print("=" * 60)
    df = get_dataset()
    tp, fp, tn, fn = 0, 0, 0, 0
    total_latency = 0.0

    for _, row in df.iterrows():
        res = detector.analyze(row["text"])
        total_latency += res["latency_ms"]
        pred = 1 if res["risk_score_pct"] >= 50.0 else 0
        actual = row["label"]

        if actual == 1 and pred == 1:
            tp += 1
        elif actual == 0 and pred == 1:
            fp += 1
            print(f"[WARN] FALSE ALARM on sample #{row['id']}: {row['scenario']}")
            print(f"   Text: {row['text']}")
            print(f"   Risk: {res['risk_score_pct']}% | Cues: {[s['category_name'] for s in res['spans']]}")
        elif actual == 0 and pred == 0:
            tn += 1
        elif actual == 1 and pred == 0:
            fn += 1
            print(f"[FAIL] MISSED SCAM on sample #{row['id']}: {row['scenario']}")
            print(f"   Text: {row['text']}")

    acc = (tp + tn) / len(df) * 100
    precision = (tp / (tp + fp) * 100) if (tp + fp) > 0 else 0.0
    recall = (tp / (tp + fn) * 100) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
    false_alarm_rate = (fp / (tn + fp) * 100) if (tn + fp) > 0 else 0.0
    avg_latency = total_latency / len(df)

    print(f"\nEvaluation Results:")
    print(f"  Total Samples Tested: {len(df)} (30 Scam, 30 Legitimate)")
    print(f"  Accuracy: {acc:.1f}%")
    print(f"  Precision: {precision:.1f}%")
    print(f"  Recall: {recall:.1f}%")
    print(f"  F1-Score: {f1:.1f}%")
    print(f"  False Alarm Rate on Genuine Messages: {false_alarm_rate:.1f}%")
    print(f"  Average Inference Latency: {avg_latency:.2f} ms")

    assert fp == 0, f"Expected 0 false alarms, got {fp}"
    assert fn == 0, f"Expected 0 missed scams, got {fn}"
    print("\n[SUCCESS] ALL VERIFICATION ASSERTIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_verification()
