# LEO Prototype Demonstration

This document demonstrates the operational pipeline of the LEO prototype developed by the BBS Foundation.

The demonstration uses runtime outputs from the internal sandbox environment.

---

## Step 1 — Anomaly Recording

Example command:

python test_anomaly_memory.py

Output:

{'status': 'ANOMALY_RECORDED'}
{'total_anomalies': 3}

The system records anomaly signals into the Epistemic Memory layer.

---

## Step 2 — Pattern Detection

Command:

python -m tests_runtime.test_pattern_detection

Output:

patterns_detected: 1
pattern_type: PRICE_ANOMALY

Repeated anomalies are aggregated into patterns.

---

## Step 3 — Graph Construction

Command:

python -m tests_runtime.test_epistemic_graph

Output:

EDGE_RECORDED
GRAPH ROOT generated

Entities and relations are stored in the Epistemic Graph.

---

## Step 4 — Structural Pattern Detection

Detected patterns:

SHELL_CHAIN
OWNERSHIP_BURST

The system detects structural ownership anomalies.

---

## Step 5 — Cluster Detection

Output example:

cluster_size: 4
entities detected

Connected entities forming suspicious clusters are detected.

---

## Step 6 — Investigation Report

Output example:

Detected anomaly patterns
Detected structural graph patterns
Detected clusters

The system automatically generates an investigation report.

---

## Step 7 — Risk Escalation

Output example:

risk_level: CRITICAL
risk_score: 11

Risk level is calculated from anomaly signals and graph patterns.

---

## Step 8 — Case Escalation

Output example:

CASE_CREATED
INSTITUTIONAL_ALERT_CREATED

When risk thresholds are exceeded the system escalates the case.

---

## Result

The prototype demonstrates a full investigative pipeline:

data ingestion
→ anomaly detection
→ graph analysis
→ pattern recognition
→ cluster detection
→ investigation report
→ risk escalation
→ institutional alert

---

This prototype is currently tested within the sandbox environment of the BBS Foundation.
