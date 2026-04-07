# Meet Manager Essentials For Coaches

**Sources:** Meet_Manager_1, Meet_Manager_2, HelpManual (Hy-Tek Meet Manager 8.0 Handbook)

## Why Coaches Need to Understand Meet Manager

Meet Manager (by Hy-Tek) is the industry-standard software for running swim meets. As a coach, understanding the basics helps you:

- **Troubleshoot delays** - Know when issues are software vs. timing system
- **Submit accurate entries** - Understand what data is required
- **Work with meet staff** - Speak their language when problems arise
- **Train your team manager** - Help parents/volunteers who run software
- **Get better results** - Know what reports are available (splits, relay exchanges, etc.)

---

## What Is Meet Manager?

**Meet Manager** = Microsoft Access database + custom interface for swim meet operations

**Key functions:**
1. **Pre-meet:** Process entries, seed events, print heat sheets
2. **During meet:** Capture times from timing system, score events, print results
3. **Post-meet:** Generate final results, export data, create records reports

**Current version:** Meet Manager 8.0 (as of 2025, though MM 9.0 in beta)

---

## The Meet Manager Workflow (From Coach's Perspective)

### Phase 1: Pre-Meet (Days/Weeks Before)

**What's happening:**
1. Meet host sets up database (events, teams, rules)
2. Coaches/clubs submit entries (via SWIMS, Team Manager, or manual entry)
3. Meet Manager imports entries, assigns swimmers to heats/lanes
4. Psych sheets generated and published

**Coach's role:**
- Submit accurate entry times (seed times)
- Verify entries in psych sheet (check for errors)
- Report discrepancies to meet director ASAP

### Phase 2: Meet Day Setup (Morning of Session)

**What's happening:**
1. Database loaded onto meet computer
2. Timing system connected (CTS, Daktronics, etc.)
3. Events downloaded to timing system
4. Printers configured
5. Positive check-in processed (if required)

**Coach's role:**
- Check swimmers in (if meet uses positive check-in)
- Submit scratches before deadline
- Verify heat sheets after scratches/seeds finalized

### Phase 3: During Competition

**What's happening:**
1. Timing system sends times to Meet Manager
2. Operator reviews/adjusts times (if needed)
3. Results scored and printed
4. Times posted to scoreboard/live results

**Coach's role:**
- Review heat sheets for lane assignments
- Watch for DQs on scoreboard/results
- Question suspicious times immediately (before next heat)
- Collect results printouts for post-meet analysis

### Phase 4: Post-Meet

**What's happening:**
1. Final results compiled
2. Records checked/verified
3. Data exported for USA Swimming (SWIMS upload)
4. Results posted online

**Coach's role:**
- Download official results from meet website
- Import times into Team Manager (for your club's database)
- Review relay splits, DQs, and improvement metrics

---

## Key Meet Manager Screens (Operator View)

### Main Menu

**Top bar shows:** Current database file name and location

**Key buttons:**
- **Run** - Opens the "Run Screen" for meet operations
- **Teams** - Add/edit teams in meet
- **Athletes** - Add/edit/scratch swimmers
- **Events** - Create/edit event structure
- **Relays** - Create/edit relay entries
- **Reports** - Print heat sheets, results, etc.

### Run Screen (The Heart of Meet Manager)

**What it does:** Real-time meet operations

**Key elements:**
- **Session/Event/Heat selector** - Navigate through meet
- **Get Times button** - Pull times from timing system
- **Lane grid** - Shows swimmer names, seed times, results
- **Timing adjustment tools** - Fix touchpad failures, button errors
- **Score/List button** - Calculate places, print results

**Color coding (helpful for operators):**
- **Green** - Event ready to run
- **Yellow** - Times received, needs review
- **Red** - Timing issue flagged

---

## Common Operations (What You Might See Operators Doing)

### 1. Downloading Events to Timing System

**When:** Before each session starts  
**Why:** Timing system needs to know event distances, relay vs. individual, etc.  
**What it looks like:** Operator clicks "Download Events" → Timing system beeps confirmation

**If this doesn't happen:** Timing system may record wrong distance, or not accept relay exchanges

### 2. Getting Times from Timing System

**When:** After each heat finishes  
**How:** Two methods:
- **Get Times** - Manually click button to import
- **Race Number** - Timing system auto-sends when heat is "stored"

**What can go wrong:**
- Timing system not connected (times don't import)
- Wrong heat selected (times import to wrong swimmers)
- Network lag (times delayed)

### 3. Adjusting Times (Lane/Heat Malfunctions)

**When a touchpad fails:**
- Operator selects "Lane Malfunction"
- Chooses which time source to use (Button A, B, or C)
- System automatically recalculates official time per FINA rules

**When entire heat has issues:**
- "Heat Malfunction" mode
- Operator can manually enter times from backup watches
- Requires referee approval

**Coach's concern:** If you see operator doing lots of adjustments, watch your swimmers' times carefully. Verify they match what you saw on your stopwatch.

### 4. Handling DQs and No-Shows

**DQ (Disqualification):**
- Referee submits DQ slip
- Operator enters DQ code (e.g., S4 = false start, B1 = breaststroke kick)
- Swimmer's time shown as "DQ" with code on results

**NS (No Show):**
- Swimmer didn't compete
- Operator marks "NS" in heat
- Seed time NOT replaced with "NS" (stays as seed for future meets)

**NT (No Time):**
- Swimmer competed but time not recorded (rare)
- Usually due to total timing system failure
- Manual watches used if available

### 5. Scoring and Printing Results

**Scoring:**
- Meet Manager auto-calculates places (1st, 2nd, 3rd...)
- Applies scoring rules (e.g., top 8, dual meet scoring)
- Updates team scores in real-time

**Printing:**
- **Heat results** - Individual heat printout
- **Event results** - All heats combined, sorted by time
- **Cumulative results** - Running team scores
- **Award labels** - For medals/ribbons

---

## What Coaches Should Request from Meet Manager

### Essential Reports

**1. Heat Sheets (Pre-race)**
- Who's in your swimmers' heats
- Lane assignments
- Seed times

**2. Event Results (Post-race)**
- Official times
- Places
- Point values (if scored meet)

**3. Splits (for 200+ events)**
- 50m/100m/150m/200m splits
- Essential for post-race analysis
- **Request specifically** - not always printed by default

**4. Relay Exchange Times**
- Reaction times for each swimmer (r:+0.XX)
- Critical for training relay team
- **Request specifically** - often only printed for finals

### Optional (But Useful) Reports

**5. Team Finish Summary**
- All your swimmers' results in one document
- Great for parent communication

**6. Personal Best Report**
- Highlights swimmers who achieved PRs
- Morale booster for team meetings

**7. Records Report**
- Pool records, team records, age group records
- Automatically generated if records broken

---

## Troubleshooting Common Issues

### "Times Aren't Showing Up"

**Possible causes:**
1. Timing system not connected to Meet Manager
2. Operator forgot to click "Get Times"
3. Network cable unplugged
4. Wrong COM port selected

**Coach action:** Alert operator calmly. Don't panic - times are still on timing system, just need to be imported.

### "My Swimmer's Time Is Wrong"

**Possible causes:**
1. Touchpad failure (button time used instead)
2. Timing adjustment error (operator selected wrong button)
3. Swimmer was in wrong lane (operator imported to wrong name)
4. Your stopwatch was off

**Coach action:**
1. Check timing system printout (ask operator for copy)
2. Compare all three times (touchpad, button A, button B)
3. If discrepancy >0.5s, file inquiry with referee

### "Splits Aren't Printed"

**Cause:** Timing system didn't capture splits, OR operator didn't enable split printing

**Coach action:** Ask operator:
- "Did the timing system record splits for this event?"
- "Can you reprint results with splits included?"

**If splits weren't captured:** Can't be added later. Only option is to review video (if available).

### "DQ Code Is Wrong"

**Example:** Your swimmer got DQ'd for "S4 - False Start" but you saw them turn improperly (should be "T2 - Turn")

**Coach action:**
1. Speak with referee IMMEDIATELY (before swimmer leaves pool deck)
2. Referee can correct DQ code in Meet Manager
3. If corrected AFTER results are printed, request reprint

---

## Meet Manager Database Structure (For Team Managers)

### Key Tables (What's Stored)

**ATHLETE table:**
- Name, age, gender, team
- USA Swimming ID number
- Best times (for seeding)

**EVENT table:**
- Event number, distance, stroke
- Gender, age group
- Scoring rules

**ENTRY table:**
- Links athletes to events
- Seed times
- Relay assignments

**RESULT table:**
- Official times
- Places
- DQ codes

### Why This Matters

**For Team Managers:**
- Understanding structure helps with imports/exports
- Easier to troubleshoot data issues
- Can write custom queries (if SQL-savvy)

**For Coaches:**
- Know that Meet Manager is just a database
- Data can be exported to Excel, Team Manager, etc.
- Results are portable (not locked in proprietary format)

---

## Meet Manager vs. Other Software

### Team Manager (Hy-Tek)

**Purpose:** Club-level database for rosters, times, entries  
**Relationship:** Exports entries TO Meet Manager, imports results FROM Meet Manager  
**Who uses it:** Team administrators, coaches

### SWIMS (USA Swimming)

**Purpose:** National athlete database  
**Relationship:** Meet Manager can upload results directly to SWIMS (for time standards, rankings)  
**Who uses it:** Meet hosts, LSC administrators

### Real-Time Results Software

**Examples:** Meet Mobile, SwimTopia Live Results  
**Purpose:** Publish results to web/mobile during meet  
**Relationship:** Reads Meet Manager database in real-time  
**Who uses it:** Parents, fans, remote coaches

---

## Tips for Coaches Working with Meet Manager Operators

### Do:
✅ Ask politely for specific reports ("Can I get splits for Event 12?")  
✅ Point out discrepancies calmly ("Lane 4's time seems off - can you check?")  
✅ Respect their workflow (wait for lulls between events)  
✅ Offer to help if you're MM-trained

### Don't:
❌ Demand immediate reprints during a session  
❌ Hover over operator's shoulder  
❌ Blame operator for timing system failures  
❌ Ask for changes to seeding after heats are printed

---

## Cross-References

- [[Timing-System-Basics-For-Coaches]] - How times get TO Meet Manager
- [[Meet-Day-Operations-Guide]] - Running smooth meets
- [[SWIMS-Database-Integration]] - USA Swimming systems
- [[Team-Manager-Workflow]] - Club-level software

---

**Coach's Bottom Line:**

> Meet Manager is a tool, not magic. It's only as good as the data it receives (from entries, timing system, operator). Your job: Verify entries before the meet, watch for errors during the meet, and request the data you need (splits, relay exchanges) after the meet.

**Key Coaching Insight:**
- **Meet Manager doesn't CREATE times** - It imports them from the timing system
- **Garbage in, garbage out** - Bad entry times = bad seeding
- **Splits and relay exchanges** - Ask for these specifically; they're not always printed by default
- **Timing adjustments happen** - Touchpad failures are normal; backup systems work
