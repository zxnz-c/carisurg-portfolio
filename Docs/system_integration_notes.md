# 03. System Integration & Data Flow Notes

## 1. Data Inputs
- **Patient Self-Report (Kiosk):** Chief complaint, language preference, basic demographic/check-in info.
- **Vitals Device Streams:** Live Bluetooth/serial data feeds (Pulse Oximeter, HR, BP, Temp).
- **EHR Pulls:** Historical patient records and past ED visits (where available).

## 2. Model Outputs & Algorithmic Layer
- **ESI Acuity Prediction:** Algorithmic recommendation (Levels 1–5).
- **Real-Time Risk Cues:** Colour-coded alert tags (e.g., Urgent vitals drop from 96% to 17%).

## 3. Human-in-the-Loop Action Sequence
1. Patient checks in at Kiosk $\rightarrow$ Vitals captured $\rightarrow$ ESI predicted.
2. Real-time vitals synced to Nurse Dashboard via a live sync.
3. Nurse reviews dashboard alert $\rightarrow$ Approves or modifies ESI score.
4. Wristband printing triggered $\rightarrow$ Patient routed to waiting or immediate care.

## 4. Frontware Implementation Architecture
- **Kiosk View Component:** Low-complexity state machine, high-accessibility UI, voice integration.
- **Dashboard View Component:** High-density patient matrix, real-time alert notifications, override modals.
- **Shared State Management:** Synchronised live sync store for real-time triage updates.
