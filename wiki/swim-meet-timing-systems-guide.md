# Swim Meet Timing Systems: A Coach's Guide

**Source:** Superior Swim Timing Manual (2019)  
**Category:** Meet Operations  
**For:** Coaches running meets or attending competitions

---

## Why This Matters for Coaches

Understanding timing systems helps you:
- **Run smoother meets** - Know what to expect from timing operators
- **Troubleshoot issues** - Understand why times might be delayed or adjusted
- **Advocate for swimmers** - Know when backup times are used vs. pad times
- **Prepare for meets** - Understand what information timing systems need

---

## Core Timing Concepts

### Pad Delay (Critical for Relays)

**What it is:** The time period after a touch when the touchpad is temporarily disabled.

**Why it matters:**
- Allows relay swimmers to exit the pool without triggering a false time
- **Standard setting: 17 seconds**
- Prevents accidental touches from being recorded as race finishes

**Coach tip:** If a relay swimmer is struggling to exit quickly, timing operators can adjust pad delay during the race.

### Backup Times vs. Pad Times

**Pad Times (Primary):**
- Recorded when swimmer touches the electronic touchpad
- Most accurate method (hundredths of a second)
- The "official" time in most cases

**Backup Times (Secondary):**
- Manual button press or stopwatch
- Used when pad fails or doesn't register a touch
- Can be selected as official time if pad malfunctions

**When backup times are used:**
- Pad doesn't register (swimmer touches too lightly, pad malfunction)
- Timing operator observes finish and presses button
- Purple lane color = backup time exists but no pad time

### Time Adjustments

**Important:** Not all swim organizations allow time adjustments during meets.

**If allowed, operators can:**
- Switch from pad time to backup button time
- Use wireless watch times
- Manually enter corrected times

**Coach responsibility:** Know your organization's rules. USA Swimming has specific protocols about when times can/cannot be adjusted.

---

## Lane States & What They Mean

### Lane Status Indicators

**Enabled (Active):**
- Lane is ready to record times
- Will register pad touches and button presses

**Disabled (Inactive):**
- Lane will not record times
- Used for empty lanes or mechanical issues

**Auto Lane Disable:**
- System automatically disables a lane if it has ZERO pad hits while other lanes have TWO touches
- Prevents timing errors from unused lanes
- Can be manually re-enabled by clicking lane number

**When it doesn't apply:** 50s (in 25Y pool) or 100s (in 50m pool) - no double touches expected

### DQ (Disqualification) Flag

- Timing operators can mark lanes as DQ
- Sends DQ status to meet management software
- Lane shows "place = 0" on scoreboard
- **Note:** Timing operator DQ is different from official referee DQ

---

## Meet Operations: What Coaches Should Know

### Auto-Finish vs. Manual Finish

**Auto-Finish (Standard):**
- Race automatically closes 8 seconds after last swimmer finishes
- System advances to next heat/event automatically
- Requires start list files loaded into timing system

**Manual Finish:**
- Operator must manually close each race
- Used when greater control is needed
- May slow meet progression

### False Starts

Timing systems have a false start function that:
- Alerts operators and meet management software
- May trigger audible/visual alarms
- Requires manual reset before next start

**Coach tip:** If you observe a false start, timing operator must be notified before the race proceeds.

### One-Lap Races (25s/50s)

**"Don't Run 25s" Feature:**
- For races run from near end with stopwatch timing at far end
- System advances to next race at start signal
- Timer does NOT start, no electronic output file created
- Common for age-group meets using manual timing

---

## Troubleshooting Common Issues

### Lane Won't Accept Touch

**Possible causes:**
1. **Pad delay still active** - Wait for delay period to expire (typically 17 sec)
2. **Lane disabled** - Operator can re-enable by clicking lane number
3. **Pad needs manual ARM** - Operator can force-arm the pad immediately

**ARM button:** Overrides pad delay, allows immediate touch registration
**F ARM button:** Forces next touch to FINISH the race for that lane (emergency use)

### Missing or Wrong Times

**Purple lane color = backup time exists but no pad time**
- Likely cause: Pad didn't register swimmer's touch
- Operator can select backup time using "USE" button
- Check if time adjustment is allowed by meet rules

**Backup buttons activate:**
- After initial pad delay expires (NOT just on final lap)
- Operators can record backup times throughout race

### Race Won't Close

**Common causes:**
1. Pad not registering final touch - Operator must hit "Force Finish"
2. Lane counting wrong number of laps - Operator can adjust lap count
3. Auto-finish disabled - Must manually finish

---

## Coach Checklist for Meet Day

### Before the Meet

- [ ] Confirm timing system is receiving your roster/entries
- [ ] Verify swimmers are listed in correct lanes on timing console
- [ ] Check if relay exhibition swimmers are properly noted
- [ ] Understand venue's policy on time adjustments

### During the Meet

- [ ] Watch for lane status indicators on scoreboard
- [ ] Note if backup times are being used frequently (may indicate equipment issues)
- [ ] Alert timing if you observe pad malfunctions
- [ ] Know the protocol for questioning times at your meet

### After Each Race

- [ ] Verify times posted match what you observed
- [ ] Check for DQ flags that may need referee confirmation
- [ ] Note any timing irregularities for meet referee

---

## Integration with Meet Management Software

Timing systems connect to:
- **Hy-Tek Meet Manager** - Most common system
- **TeamUnify TouchPad** - Cloud-based option
- Other platforms via serial interface or file sharing

**What coaches should know:**
- Start lists must be generated BEFORE timing system can use them
- Timing results flow back to meet management automatically
- Network issues can cause delays in result posting
- Manual entry may be needed if connection fails

**Files generated:**
- Results files (for meet software import)
- HTML printouts (for immediate reference)
- Each race: `Event XXX-HH (Race NNNN).html`

---

## Advanced Features Coaches May Encounter

### Team Scores Display

Modern systems can:
- Accept team score entries during meet
- Display running team scores on scoreboard
- Update automatically as races finish

### Statistics Tracking

Some timing consoles provide:
- Session-wide statistics
- Individual lane performance data
- Timeline views of race progression

### Wireless Watch Integration

- Backup timing via wireless watches
- Syncs with timing console
- Provides additional redundancy beyond button backups

---

## Key Takeaways

1. **Pad delay (17 sec) is essential for relays** - prevents false touches as swimmers exit
2. **Backup times are always recorded** - system has redundancy built in
3. **Lane colors tell a story** - purple = backup exists without pad time
4. **Not all meets allow time adjustments** - know your organization's rules
5. **Auto lane disable prevents errors** - but can be overridden if needed
6. **8-second auto-finish is standard** - but can be disabled for manual control

---

## Related Wiki Pages

- [[Relay Exchanges and Timing]] *(if available)*
- [[Meet Management Best Practices]] *(if available)*
- [[USA Swimming Timing Rules]] *(if available)*

---

**Bottom Line:** Understanding timing systems makes you a better meet host and a more informed coach. When something goes wrong with timing, you'll know what questions to ask and what solutions are possible.

**Next time your swimmer's touch doesn't register, you'll know exactly what the timing operator should do.**
