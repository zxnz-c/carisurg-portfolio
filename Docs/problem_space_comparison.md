# 01. Problem Space Comparison: HCI vs. HRI in Emergency Department Triage

## 1. Overview & Context
This document analyzes the operational shift from traditional Human-Computer Interaction (HCI) triage tools to an assistive Human-Robot Interaction (HRI) Observation Unit Kiosk & Nurse Dashboard.

## 2. Comparison Matrix

| Dimension | Traditional HCI Triage | Assistive HRI Kiosk + Nurse Dashboard |
| :--- | :--- | :--- |
| **Primary User** | Triage Nurse only (manual entry) | Dual: Patient (Self-Check-in) & Observation Nurse (Dashboard) |
| **Input Mechanism** | Keyboard / Mouse / Desktop EHR | Touch Targets, Audio Guidance, Real-time Vitals Streaming |
| **Acuity Scoring** | Manual calculation / Static lookup | Automated ESI Acuity Prediction & Clinical Decision Support |
| **Accessibility** | Standard Desktop UI | Multi-lingual, High Contrast, Voice Guidance, Large Targets |
| **Cognitive Load** | High (Nurse enters all data manually) | Distributed (Patient completes check-in; Nurse validates) |

## 3. Safety & Workflow Considerations
- **Human-in-the-Loop Validation:** Automated ESI scores require nurse confirmation before final queue placement.
- **Fail-Safe Mechanisms:** Manual override buttons available at both the kiosk interface and the dashboard.
- **Privacy & Security:** Anonymized patient cues on public screens with encrypted EHR streaming.
