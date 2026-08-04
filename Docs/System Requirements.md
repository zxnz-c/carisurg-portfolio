# System Requirements

# Setting A – Emergency Department Triage Desk (HCI)

## Functional Requirements
- The interface shall display a **descriptive risk flag** (not a numerical ESI level) within **1.5 seconds** of manual data submission.
- The system shall provide a **nurse override** function that requires a one-line justification and records the reason in an audit log.
- The interface shall display the **three most influential contributing factors** alongside the descriptive risk flag.

## Non-Functional Requirements
- The interface shall remain legible under clinical lighting.
- All colour-coded risk flags shall include a secondary identifier (such as an icon or text label); colour alone shall never be used to convey information.
- If any future Electronic Health Record (EHR) or device-stream connection fails, the system shall degrade gracefully to a visible **"Manual Entry Only"** mode.

## Integration Requirements
- The Minimum Viable Product (MVP) shall require **no EHR or medical device integration** and shall operate using manual data entry only.
- Future EHR integration shall preserve manual data entry as a fallback, accessible within **two user actions**.
- The override audit log shall be exportable for review by the **Integration Review Board**.

---
# Setting B – Observation Unit Kiosk (HRI)

## Functional Requirements
- The kiosk shall capture a patient’s self-reported symptom update via touchscreen and transmit a descriptive risk flag to the nursing station within 5 seconds of submission.
- Any submission exceeding the defined severity threshold, or containing incomplete or inconsistent information, shall be routed immediately to a nurse rather than entering the standard queue.
- The kiosk shall display a consent notice on first use during each patient visit before any information is collected.

## Non-Functional Requirements
- If a future vital signs device connection fails, the kiosk shall degrade gracefully to a visible **"Device Offline – Manual Entry"** state within 5 second and the failure shall be recorded in an audit log.
- The touchscreen shall use large touch targets to minimise repeated tapping and reduce unnecessary contact in support of infection control.
- The kiosk shall never display the patient's descriptive risk flag or any clinical assessment. Patient-facing messages shall be limited to a generic acknowledgement confirming successful submission.

## Integration Requirements
- The MVP shall require **no vital signs device integration** and shall rely solely on touchscreen self-entry.
- Descriptive risk flags shall be transmitted to the ED depart,ent nursing station alert system.
- The kiosk failure log shall be exportable for Integration Review Board audit and shall follow the same audit requirements as the Emergency Department triage system.

---
