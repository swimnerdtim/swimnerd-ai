# Timing System Hardware Setup: What Coaches Need to Know

**Source:** Superior Swim Timing Manual (2019)  
**Category:** Meet Operations / Equipment  
**For:** Coaches managing their own pools or running home meets

---

## Why Coaches Should Understand Timing Hardware

You don't need to be a timing expert, but understanding the basics helps when:
- **Setting up your own pool** for practice or small meets
- **Troubleshooting** timing issues during competition
- **Purchasing equipment** for your program
- **Working with timing operators** who may need your input

---

## Basic Timing Hardware Components

### 1. Touchpads (The Primary Timing Device)

**What they do:**
- Detect when swimmer touches wall
- Send electronic signal to timing console
- Record time to hundredths of a second

**Key fact for coaches:**
- Must be sensitive enough to detect touch, but not so sensitive that water movement triggers them
- Typically mounted on pool wall at finish end
- Can be used at both near and far ends for longer races

**Common issues:**
- **Too light a touch:** Swimmer brushes pad but doesn't register → backup time used
- **Pad delay active:** After relay exchange, pad disabled for ~17 seconds
- **Water splash:** Can sometimes trigger false touch (rare with modern pads)

### 2. Backup Buttons (Secondary Timing)

**Purpose:**
- Human operator presses button when they observe swimmer finish
- Serves as backup if touchpad fails
- Required by most meet rules for redundancy

**Location options:**
- Near end (starting blocks area) - most common
- Far end (turn end) - for longer courses
- Multiple positions possible

**When backup times become official:**
- Pad malfunctions or doesn't register
- Timing system allows operator to select backup time
- Meet referee determines which time is official

### 3. Starting System Integration

**Timing systems need to know when race starts:**
- **Starting horn/buzzer** sends signal to timing console
- Starts all lane timers simultaneously
- Can detect false starts if swimmer touches pad before start signal

**Manual start option (F1 key):**
- Operator can manually start timing if automatic start fails
- Used as backup if starting system doesn't connect

### 4. The Timing Console (The Brain)

**What it does:**
- Receives signals from pads and buttons
- Calculates lap counts and finish times
- Sends results to meet management software
- Displays times on scoreboard

**Computer requirements:**
- Laptop preferred (built-in battery backup during power outages)
- USB-powered systems draw minimal power
- Windows, Mac, or Linux compatible (most use Windows)

---

## Harness Configurations (Cable Types)

### Understanding Connector Labels

You'll see labels like "A1," "A2," "B," "Near," "Far" on timing boxes. Here's what they mean:

**"A" Harness (Primary):**
- Connects to prime touchpads
- Main timing signal source
- Usually labeled A1 or Near-A

**"B" Harness (Secondary):**
- Connects to backup buttons OR far-end pads
- Provides redundancy
- Usually labeled A2 or B

**Near vs. Far:**
- **Near:** Starting blocks end (where race begins)
- **Far:** Turn end (opposite wall)

### Common Pool Setups

**Setup 1: Single-End Timing (Most Common)**
- Touchpads at near end (starting blocks)
- Backup buttons at near end
- Used for: 25Y/25M races, 50Y/50M races (short course)

**Setup 2: Double-End Timing**
- Touchpads at BOTH near and far ends
- Backup buttons at both ends
- Used for: 100+ races in 50M pools, any race needing far-end verification

**Setup 3: Button-Only (Budget/Practice)**
- No touchpads
- Manual button timing only
- Accurate to tenths of a second (not hundredths)
- Good for practice meets, small competitions

---

## Hardware Compatibility

### Brand Compatibility Chart

| Your Existing Equipment | Can Work With |
|------------------------|---------------|
| Colorado Time "A" harness | Most modern timing systems (SST, Daktronics) |
| Colorado Time "B" harness | Compatible with backup button ports |
| SST Harness | SST timing boxes (not always compatible with other brands) |
| Daktronics harness | Daktronics systems + some universal timing boxes |

**Coach tip:** If you're buying a timing system, ask about compatibility with your pool's existing in-deck wiring. Replacing wiring is EXPENSIVE.

### Wall Plates and In-Deck Wiring

**What it is:**
- Cables buried in pool deck
- Connects touchpads to timing box via wall-mounted connector plates

**Why coaches care:**
- **Already installed?** You can use it instead of running cables across deck
- **Not installed?** You'll need harness cables (trip hazard, but portable)
- **Damaged wiring?** May need professional electrician to repair

**Note:** In-deck wiring for timing is different from pace clock wiring.

---

## Power and Connectivity

### Power Requirements

**USB-Powered Systems (Like SST):**
- ✅ Powered entirely through laptop USB port
- ✅ Laptop battery = built-in backup power
- ✅ No external power supply needed (unless using Daktronics cables)
- ✅ Low power draw, doesn't drain laptop quickly

**Serial Deck Cable Systems:**
- Require dedicated power supply
- Powers the deck cable interface
- Still connects to computer via USB or serial port

**Coach tip:** USB-powered systems are simpler for small meets or travel setups.

### Computer Connectivity Options

**1. Direct USB Connection (Simplest)**
- Timing box plugs directly into laptop USB port
- No network setup needed
- Computer runs both timing software AND meet management software

**2. USB Null Cable (Two Computers)**
- One computer for timing, one for meet management
- USB cable connects both computers
- Separates timing operator from data entry operator

**3. Network/WiFi Connection**
- Timing computer and meet management computer on same network
- Uses Virtual COM Port (VCP) on network
- Most flexible for larger meets

**4. Serial Interface (Legacy)**
- Older method using RS-232 serial ports
- Still supported but less common
- Requires serial-to-USB adapter on modern computers

---

## Setup Checklist for Home Meets

### Week Before

- [ ] Test touchpads (have swimmers touch them, verify signal)
- [ ] Check backup button functionality
- [ ] Verify starting horn connects to timing system
- [ ] Install/update timing software on laptop
- [ ] Test connection to meet management software
- [ ] Create results folder for the meet

### Day Before

- [ ] Charge laptop fully
- [ ] Run dummy race to test all lanes
- [ ] Print test results to verify printer connection
- [ ] Configure scoreboard interface (if using)
- [ ] Verify network connectivity (if using multiple computers)

### Race Day Morning

- [ ] Power up timing console 30+ minutes before first race
- [ ] Test each lane individually with pad touches
- [ ] Verify backup buttons work on all lanes
- [ ] Run one full test race with start signal
- [ ] Check that results flow to meet management software
- [ ] Print test results

---

## Troubleshooting Common Hardware Issues

### "Lane Not Registering Touches"

**Check:**
1. Is the lane enabled on timing console? (Click lane number to toggle)
2. Is pad delay still active? (Wait 17 seconds after last touch)
3. Is harness cable plugged in securely?
4. Is touchpad damaged or disconnected?

**Workaround:** Use backup button timing for that lane

### "Backup Buttons Not Working"

**Check:**
1. Are buttons connected to correct harness port (A2 or B)?
2. Is timing software configured to accept button inputs?
3. Have buttons been activated? (Usually after pad delay expires)

**Workaround:** Manual stopwatch timing as final backup

### "Starting System Not Triggering Timer"

**Check:**
1. Is starting system connected to timing console?
2. Is start signal cable secure?
3. Does starting system send signal compatible with timing console?

**Workaround:** Use Manual Start (F1 key) - operator presses key when horn sounds

### "Results Not Showing Up in Meet Manager"

**Check:**
1. Is results folder path correct in both systems?
2. Are computers on same network (if using network connection)?
3. Is meet management software set to import from timing system?
4. Is there a folder permission issue?

**Workaround:** Manually enter times from printed timing results

---

## Purchasing Guidance for Coaches

### Budget Tiers

**Tier 1: Entry Level ($1,000-3,000)**
- Button-only timing system
- 6-8 lanes
- Basic meet management software integration
- **Good for:** Practice meets, summer league, small high school meets

**Tier 2: Mid-Range ($5,000-10,000)**
- Touchpads + backup buttons
- 8-10 lanes
- Scoreboard integration
- Network capability
- **Good for:** High school championships, club dual meets, larger invitationals

**Tier 3: Professional ($15,000-50,000+)**
- Full touchpad system with far-end capability
- Wireless backup watches
- LED scoreboard integration
- Video scoreboard capability
- Multiple timing console support
- **Good for:** NCAA meets, championship-level competitions

**Coach tip:** Don't overbuy. If you're running small dual meets, button timing is sufficient. Invest in touchpads when your meet results affect qualifying times.

### Key Features to Consider

**Must-Have:**
- ✅ Meet management software compatibility (Hy-Tek, TeamUnify, etc.)
- ✅ Backup timing capability (buttons or watches)
- ✅ Lane count matching your pool

**Nice-to-Have:**
- Scoreboard integration
- Wireless connectivity
- Far-end pad support
- Replay/review capability

**Don't Need:**
- Features designed for Olympic/international meets
- Lane counts beyond your pool (don't pay for 10 lanes if you have 6)

---

## Maintenance Tips

### After Every Meet

- [ ] Wipe down touchpads (remove chlorine residue)
- [ ] Dry all connectors
- [ ] Coil cables neatly (prevents damage)
- [ ] Store equipment in dry location

### Monthly (If Used Regularly)

- [ ] Test all lanes even if not used recently
- [ ] Check cable connections for corrosion
- [ ] Update timing software if patches available
- [ ] Verify backup battery in starting system

### Annually

- [ ] Full system test with simulated meet
- [ ] Replace worn cables
- [ ] Service touchpads (check sensitivity)
- [ ] Update meet management software integration

---

## When to Call a Professional

**You can probably fix:**
- Software configuration issues
- Cable connections
- Basic lane enable/disable problems
- Results file location setup

**Call a timing system professional for:**
- In-deck wiring repairs
- Touchpad sensitivity adjustments
- Starting system integration failures
- Scoreboard interface failures
- Hardware damage or component replacement

---

## Key Takeaways

1. **Touchpads are primary, buttons are backup** - but you need both
2. **USB-powered systems are simpler** - fewer cables, built-in battery backup via laptop
3. **Test everything the day before** - not the morning of your meet
4. **In-deck wiring compatibility matters** - check before buying new equipment
5. **Manual start (F1) is always an option** - if automatic start fails
6. **Results folder location must match** between timing and meet management systems

---

## Related Wiki Pages

- [[Swim Meet Timing Systems Guide]] - Operations and protocols
- [[Meet Management Software Setup]] *(if available)*
- [[Running Dual Meets at Your Pool]] *(if available)*

---

**Bottom Line:** You don't need to be a timing engineer, but knowing the basics prevents meet-day disasters. When equipment fails, you'll know whether it's a cable, configuration, or time to call a professional.

**Most timing issues are software configuration problems, not hardware failures. Learn your system BEFORE meet day.**
