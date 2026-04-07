# Meet Equipment Reference Guide

**Sources:** Dak_1, Dak_2 (Daktronics OmniSport 2000 Timing Console Operation Manual)

## For Coaches: Why This Matters

Understanding meet equipment helps you:
- **Troubleshoot delays** - Know whether issues are operator error or equipment failure
- **Advocate for swimmers** - Understand when times might be inaccurate
- **Plan logistics** - Work better with meet management on timing setup
- **Train better** - Know what data the system captures (splits, relay exchanges, etc.)

---

## Daktronics OmniSport 2000 Overview

**Common at:** High school championships, college dual meets, large invitational meets

**Key differences from Colorado (CTS) system:**
- Built-in printer (CTS requires external printer)
- Can support both swimming AND diving modes
- Radio channel system for wireless components
- Network-enabled for Meet Manager integration

---

## Equipment Components

### 1. Console
- Central timing unit with built-in printer
- Sport-specific inserts (Swimming vs. Diving)
- Battery backup (continue timing during power loss)
- LCD display shows lane status in real-time

### 2. Touchpads
- Pressure-sensitive panels mounted on wall
- **Standard size:** Full lane width
- **Arming delay:** User-adjustable (prevents accidental touches)
- **Typical setting:** 0.3-0.5s delay after touch before re-arming

### 3. Deck Cabling Systems

**On-Deck System:**
- Lane modules sit on pool deck
- Easy to set up/remove
- Best for temporary installations

**In-Deck System:**
- Deck plates embedded in pool deck
- Permanent installation
- Cleaner appearance, fewer trip hazards

### 4. Horn Start HS-200
- Electronic starting system
- Microphone triggers timer start
- Ensures all lanes start simultaneously
- **Backup:** Manual "START" button on console

---

## Swimming Mode Features

### Key Functions (Coach Perspective)

**Lane On/Off**
- Turns lanes on/off for empty lanes
- Important: Operator must disable empty lanes to avoid false finishes

**Finish Arm / Finish Arm All**
- Prepares system to record finish
- "Finish Armed" should flash when swimmer approaches wall
- If it doesn't flash → manual "Finish Arm" button press needed

**Split Arm / Split Arm All**
- Arms intermediate splits (for distance events)
- Captures 50m/100m/200m splits in longer races

**Touch Commands**
- **+ Touch:** Add a missed lap
- **- Touch:** Remove an accidental/extra touch
- Used when touchpad fails to register turn

### Relay Functionality

**Relay Take-Off Settings:**
- Measures reaction time of incoming swimmer
- Calculated from outgoing swimmer's touch to incoming swimmer's departure
- **Legal range:** 0.00 to +0.30s (per USA Swimming rules)
- **DQ threshold:** Negative time (early departure)

**Printout includes:**
- Individual leg times
- Cumulative times
- Relay exchange times (r:+0.XX format)

---

## Scoreboard Display Modes

### Single-Line Scoreboards

**Display sequence:**
1. **Start of race:** Running time (shared across all lanes)
2. **Split times:** Brief hold (2-5s), then return to running time
3. **Finish times:** Each lane shows final time
4. **After reset:** Time-of-day or "READY"

### Multiple-Line Scoreboards

**Display shows:**
- Lane number
- Running time / final time
- Place (1st, 2nd, 3rd...)
- Split times (configurable hold duration)

**Results Order Options:**
- Lane order (1-2-3-4-5-6-7-8)
- Place order (fastest → slowest)

---

## Common Operator Errors (and What Coaches Should Watch For)

### 1. Missed Start
**Symptom:** Console shows "RESET" instead of running clock  
**Cause:** Horn start signal didn't reach console (loose cable, dead battery)  
**Fix:** Operator presses "START" button manually  
**Impact:** Slight timing delay (usually negligible)

### 2. Lane Not Disabled
**Symptom:** Empty lane shows a "finish" time  
**Cause:** Operator forgot to turn lane off  
**Fix:** Operator disables lane, reprints results  
**Impact:** Results printout shows extra lane (no effect on actual swimmers)

### 3. Finish Not Armed
**Symptom:** Swimmer finishes, but no time displays  
**Cause:** System didn't detect final lap approaching  
**Fix:** Operator manually presses "Finish Arm" for that lane  
**Impact:** Time may be slightly delayed (backup button times used)

### 4. Touchpad Malfunction
**Symptom:** "Touch" registered but swimmer didn't touch, OR swimmer touched but no registration  
**Cause:** Pad sensitivity issue, loose connection, or pad damage  
**Fix:** Operator uses +/- Touch commands; may need to replace pad  
**Impact:** Manual intervention required; backup button times become primary

---

## Diving Mode (Bonus Feature)

**Why coaches care:** Many pools use same timing system for diving

**Key features:**
- Judges enter scores via wireless consoles
- System calculates degree of difficulty automatically
- Displays running totals for each diver
- Prints individual dive sheets

**Judge Console Options:**
- Wireless (radio-linked)
- Wired (for permanent installations)

---

## Meet Manager Integration

### How It Works

**Daktronics OmniSport connects to Meet Manager via:**
1. **Serial connection** (RS-232) - older systems
2. **Network connection** (Ethernet) - modern systems

**Data flow:**
- Meet Manager → Console: Event/heat assignments, swimmer names, seed times
- Console → Meet Manager: Finish times, splits, relay exchanges

**Benefits:**
- Automatic results import (no manual entry)
- Real-time scoreboard updates
- Heat sheet generation with times

### Troubleshooting Meet Manager Connection

**If results aren't importing:**
1. Check network cable connection
2. Verify IP address matches Meet Manager settings
3. Confirm "Pro Software Enable" is ON in console settings
4. Restart Meet Manager and re-establish connection

---

## Battery Backup System

**Purpose:** Keep timing accurate during brief power outages

**How it works:**
- Internal battery maintains console memory
- Race in progress continues timing
- Printouts still work
- Scoreboard may go dark (depends on separate power)

**Battery test:** Menu → Test → Battery Test  
**Replacement:** Contact Daktronics service (not user-serviceable)

---

## Maintenance & Troubleshooting

### Basic Maintenance (Meet Host Responsibility)

**Before each meet:**
- [ ] Test all touchpads (press each one, verify console registers)
- [ ] Test buttons (2-3 per lane, verify asterisks appear on console)
- [ ] Test horn start (fire horn, confirm console starts clock)
- [ ] Load printer paper (thermal paper, correct orientation)
- [ ] Check battery status (Test Menu → Battery Test)

**During meet:**
- [ ] Monitor touchpad status for malfunctions
- [ ] Keep spare pads/buttons available
- [ ] Keep console out of direct sunlight (LCD screen visibility)

**After meet:**
- [ ] Print backup of all results (archive)
- [ ] Coil cables properly (avoid kinks/damage)
- [ ] Store touchpads flat (avoid bending connectors)

### When to Call for Service

**Immediate (stop meet if necessary):**
- Console won't power on
- Multiple touchpads fail simultaneously
- Start signal not working AND manual start fails
- Printer won't print AND computer connection down

**Can finish meet, but schedule service:**
- Single touchpad consistently failing
- Scoreboard not updating (if results still printing)
- Battery test shows low charge
- Paper jams frequently

---

## Cross-References

- [[Timing-System-Basics-For-Coaches]] - CTS system comparison
- [[Meet-Day-Operations-Guide]] - Running smooth meets
- [[USA-Swimming-Timing-Rules]] - Official regulations
- [[Relay-Exchange-Technology]] - Reaction time measurement

---

**Coach's Bottom Line:**

> Most timing issues don't affect your swimmers' official times. Touchpads can fail, operators can make mistakes, but backup systems (buttons, manual watches) protect results. Your job: Know when to question a time (2+ seconds off expectation) and when to let the officials handle it (minor delays, operator corrections).

**Key Coaching Insight:**
- **Touchpad failure ≠ lost time.** Backup buttons are official.
- **Relay exchanges are measured electronically.** Trust the printout, not your eye.
- **Splits are gold.** If system captures splits, use them for post-race analysis.
