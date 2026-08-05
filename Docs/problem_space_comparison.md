# HCI vs HRI Comparison

## Setting A vs Setting B – Design Dimensions

| Dimension | Setting A – Emergency Department Triage Desk (HCI) | Setting B – Observation Unit Kiosk (HRI) |
|-----------|-----------------------------------------------------|------------------------------------------|
| **Who is the user?** | Emergency Department triage nurse, trained clinical staff. | Mixed users: patients (self-check-in), ED nurses, and porters. |
| **What data does the model receive?** | Manual entry of age, presenting complaint, and vital signs at the triage desk. Electronic Health Record (EHR) integration is a future enhancement and is not included in the MVP. | Touchscreen self-entry of symptoms and medical history, with data from a vital signs station where available. Manual entry remains the fallback if the device connection fails. |
| **What does the model emit?** | A descriptive risk flag (colour, icon, and short text) rather than a numerical ESI recommendation. This supports the project's aim of reducing automation bias and overreliance. | The same descriptive risk flag is displayed on the kiosk screen. The kiosk has no robotic movement, gestures, or verbal interaction; it is a stationary touchscreen device. |
| **What does the human do next?** | The nurse reviews the flag, makes the clinical triage decision, and records a reason if the recommendation is overridden. | The patient completes self-check-in, while high-severity or incomplete submissions are immediately routed to a nurse instead of entering the normal queue. |

---

## A Note on Form Factor

The two system designs sit closer together than the traditional distinction between Human–Computer Interaction (HCI) and Human–Robot Interaction (HRI).

The Emergency Department triage desk represents a conventional HCI interface, consisting of a touchscreen used by clinical staff.

The Emergency Department kiosk is physically located within the clinical environment and therefore introduces HRI considerations such as proximity, hygiene, accessibility, and physical deployment. However, interaction remains entirely touchscreen-based, with no robotic movement, gestures, or speech. As a result, it is best described as a **hybrid system**: physically present within the clinical space while functionally operating as an HCI interface.

This distinction should be stated explicitly within the design canvas and demonstrated during the project walkthrough rather than attempting to categorise the kiosk as a traditional robot.

---

# Safety Considerations

## Setting A – Emergency Department Triage Desk (HCI)

### 1. Automation Bias and Overreliance

**Concern**

Nurses may rely on the descriptive risk flag instead of applying independent clinical judgement, particularly during busy periods.

**Context**

Under triage time pressures of less than three minutes, particularly towards the end of a long clinical shift, accepting the system's recommendation may be faster than critically reviewing it.

**Mitigation**

The system presents a descriptive prompt (for example, *"Elevated respiratory risk – review vital signs"*) rather than suggesting an ESI level. Any override requires a one-line justification, which is recorded in an audit log.

**Residual Risk**

Even descriptive prompts may still be interpreted as definitive recommendations under significant workload or fatigue.

---

### 2. Display Legibility Under Clinical Conditions

**Concern**

An interface that appears clear during testing may become difficult to read under fluorescent lighting, glare, and the distractions of a busy Emergency Department.

**Context**

The triage desk is often shared, cluttered, and used while simultaneously communicating with patients and recording observations.

**Mitigation**

The descriptive risk flag uses a minimum 16 pt font, complies with colour contrast standards, and remains in a consistent location across every screen.

**Residual Risk**

No interface layout can guarantee optimal readability for every user under all lighting and fatigue conditions.

---

### 3. Colour Accessibility

**Concern**

Using colour as the only method of distinguishing risk levels disadvantages users with colour vision deficiency.

**Context**

Approximately 4.5% of the world population experience some form of colour blindness, making colour-only communication unsuitable.

**Mitigation**

Each colour-coded state includes both an icon and a text label so that colour is never the sole indicator.

**Residual Risk**

Screen magnification or other accessibility requirements may still affect layout consistency and have not yet been evaluated.

---

## Setting B – Observation Unit Kiosk (HRI)

### 1. Shared Touchscreen and Infection Control

**Concern**

A self-service kiosk used by multiple unwell patients presents a potential infection transmission surface.

**Context**

Patients with respiratory or gastrointestinal symptoms may use the same touchscreen consecutively.

**Mitigation**

The kiosk incorporates an antimicrobial touchscreen coating, a clearly visible hand sanitiser station, and large touch targets to minimise contact time.

**Residual Risk**

These measures reduce but cannot eliminate infection risk associated with a shared physical interface.

---

### 2. Reliability of Patient Self-Reporting

**Concern**

Patients experiencing pain, distress, or confusion may provide inaccurate or incomplete symptom information.

**Context**

Unlike face-to-face triage, the kiosk cannot observe non-verbal clinical cues such as guarding, confusion, or respiratory effort.

**Mitigation**

Any high-severity response, incomplete submission, or inconsistent data is immediately escalated to a nurse rather than entering the standard queue.

**Residual Risk**

The escalation threshold can only identify scenarios anticipated during system design; unusual presentations may remain undetected.

---

### 3. Graceful Degradation During System Failure

**Concern**

Loss of power or failure of the vital signs device connection must not result in incomplete or misleading information being presented.

**Context**

Power interruptions and generator changeovers are foreseeable within the Caribbean healthcare infrastructure.

**Mitigation**

If the device connection fails, the kiosk switches to **Manual Entry** mode within **5 seconds**, displays a visible **"Device Offline – Manual Entry"** message, and records the failure in an audit log.

**Residual Risk**

Patients or busy clinical staff may overlook the manual fallback, resulting in missing rather than incorrect data. Although this is the safer failure mode, it remains an operational limitation.
