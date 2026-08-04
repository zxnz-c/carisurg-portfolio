# 03. System Integration & Data Flow Notes

## 1. Data Inputs
- **Setting A — ED Triage Desk:** Manual entry by triage nurse (symptom & clinical notes).
- **Setting B — Observation Kiosk:** Touchscreen self-reported symptom updates (and fixed consent acknowledgement).
- **Future Integration Scope (Post-MVP):** Bluetooth/serial vitals device streams and EHR historical record pulls (with manual fallback available within 2 user actions).

## 2. Model Outputs & Algorithmic Layer
- **Descriptive Risk Flag:** Real-time descriptive risk indicator (non-numeric, avoiding raw ESI 1–5 levels on nurse UI).
- **Explainability:** Top 3 contributing factors displayed alongside the flag.
- **Severity Escalation:** Immediate routing to nurse station for entries exceeding severity thresholds or displaying inconsistent data.

## 3. Human-in-the-Loop Action Sequence
1. **Patient/Staff Entry:** Patient submits via Kiosk (Setting B) or Nurse enters data manually (Setting A).
2. **Risk Calculation & Routing:** System computes descriptive risk flag and top 3 factors.
3. **Nurse Review & Override:** Nurse reviews risk flag. Any change requires and logs a one-line override reason.
4. **Audit Logging:** Override logs and offline failure events are recorded and exportable for Integration Review Board audit.

## 4. Frontware Implementation Architecture
- **Setting A — Triage Desk UI:** High-contrast, multi-modal visual design (colour + icon/label secondary differentiator), manual override modal.
- **Setting B — Kiosk UI:** High-accessibility touchscreen with large touch targets, fixed consent display, no clinical flag exposure to patient.
- **Graceful Degradation:** Automatic fallback to visible "manual entry only" / "device offline" mode upon stream or network failure.
