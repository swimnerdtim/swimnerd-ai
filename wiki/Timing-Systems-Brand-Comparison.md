# Timing Systems: Brand Comparison Guide

**Sources:** Gen7 Legacy/Serial Timer Guides, Superior Swim Timing Manual, System 6 Manual, Colorado System 5 Manual, Omega Quantum Manual

## For Coaches: Why Know Your Timing System?

Different timing systems have different:
- **Reliability profiles** - Some handle touchpad failures better than others
- **Data outputs** - Not all capture splits or relay exchanges
- **Operator complexity** - Affects meet delays and error rates
- **Integration** - Some play nicer with Meet Manager software

**Bottom line:** Know which system is running your meet, and you'll know what data to expect and what issues might arise.

---

## Major Timing System Manufacturers

### 1. Colorado Time Systems (CTS)

**Market position:** Dominant in USA Swimming age-group and high school markets

**Product lines:**
- **System 5** - Older LCD display model (still widely used)
- **System 6** - Current generation (color touchscreen)
- **System 7 (Gen7)** - Newest platform (modular, networked)

**Strengths:**
- Industry standard in USA Swimming
- Excellent Meet Manager integration (Hy-Tek)
- Extensive dealer/service network in US
- Relay exchange time measurement (built-in)

**Weaknesses:**
- Proprietary cables/connectors (expensive replacements)
- Older systems (5/6) have limited network capability
- Printer setup can be finicky (especially System 6)

**Best for:** Age-group meets, high school championships, college dual meets

---

### 2. Daktronics OmniSport

**Market position:** Strong in high school and multi-sport facilities

**Key models:**
- **OmniSport 2000** - Workhorse console (swimming + diving modes)
- **OmniSport 4000** - Advanced model (better networking)

**Strengths:**
- Built-in printer (no external printer needed)
- Dual swimming/diving modes (saves equipment costs)
- Excellent scoreboard integration (Daktronics makes scoreboards too)
- Battery backup system

**Weaknesses:**
- Less common in pure swimming facilities
- Operator training curve (more complex menu structure)
- Service network smaller than CTS in some regions

**Best for:** Multi-sport high schools, pools with diving programs, facilities with Daktronics scoreboards

---

### 3. Omega (Swatch/Omega)

**Market position:** Olympics, World Championships, elite international events

**Key models:**
- **Quantum Timer** - Flagship timing system
- **Ares 21** - Touchpad system (1/1000th second precision)

**Strengths:**
- Highest precision (0.001s vs. 0.01s for most others)
- FINA-certified for world records
- Ultra-reliable touchpads
- Comprehensive data logging

**Weaknesses:**
- Expensive (typically $50k-$200k+ for full system)
- Overkill for age-group meets
- Limited service network outside elite venues
- Requires specialized operator training

**Best for:** Olympic Trials, World Championships, elite college programs, international meets

---

### 4. Superior Timing Systems

**Market position:** Budget-friendly option for smaller programs

**Strengths:**
- Lower cost than CTS/Daktronics
- Simpler operation (fewer features = fewer errors)
- Good for dual meets and small invitationals

**Weaknesses:**
- Less robust feature set
- Limited Meet Manager integration
- Smaller service/support network
- May not capture relay exchange times

**Best for:** Small club teams, dual meets, training environments

---

## Feature Comparison Table

| Feature | CTS System 6/7 | Daktronics OmniSport | Omega Quantum | Superior |
|---------|----------------|----------------------|---------------|----------|
| **Precision** | 0.01s (hundredths) | 0.01s | 0.001s (thousandths) | 0.01s |
| **Relay Exchanges** | Yes | Yes | Yes | Limited |
| **Split Timing** | Yes (all lanes) | Yes (all lanes) | Yes (all lanes) | Basic |
| **Built-in Printer** | No (System 6), Yes (Gen7) | Yes | Yes | Optional |
| **Meet Manager Sync** | Excellent | Good | Excellent | Basic |
| **Diving Mode** | No | Yes | No | No |
| **Battery Backup** | Optional | Standard | Standard | No |
| **Touchpad Types** | CTS-proprietary | Daktronics-proprietary | Omega-proprietary | Generic |
| **Typical Cost** | $15k-$40k | $20k-$45k | $50k-$200k+ | $8k-$20k |

---

## Gen7 (Colorado System 7) - The Future

**What's new:**
- **Modular design** - Components can be replaced individually
- **Networked** - Full IP-based communication (no more proprietary cables for some components)
- **Touchscreen interface** - Easier operator navigation
- **Cloud integration** - Real-time results publishing
- **Wireless options** - Bluetooth/WiFi for some peripherals

**Coaching impact:**
- Faster results posting (live to web during meet)
- Better split data capture
- Fewer cable-related delays
- Easier operator training = fewer timing errors

**Adoption status (as of 2025):**
- Replacing System 6 at major meets
- Still expensive (slow rollout to smaller facilities)
- Backward compatible with older CTS touchpads/buttons

---

## What Coaches Should Ask Before a Meet

### Questions for Meet Director / Timing Operator

1. **What timing system are you running?**
   - Affects what data you'll get (splits, relay exchanges, etc.)

2. **Is automatic timing (touchpads) used for ALL events?**
   - Or just finals? Or button-only for prelims?

3. **Will split times be captured?**
   - Distance events (200+) should have splits
   - Not all systems/setups capture them

4. **How are results delivered?**
   - Paper printouts only?
   - Uploaded to Meet Manager?
   - Live web results?

5. **What's the backup plan if touchpads fail?**
   - Button times?
   - Manual watches?
   - Spare touchpads available?

6. **Will relay exchange times be provided?**
   - Essential for training relay teams
   - Not all systems capture this

---

## Interpreting Results from Different Systems

### CTS System 6/7 Printout

**Typical format:**
```
Lane 4  Smith, John        SR  TeamName  1:45.23  **
                                                   1:45.28
                                                   1:45.31
```

**What it means:**
- 1:45.23 = Touchpad time (primary)
- ** = Two backup buttons recorded
- 1:45.28, 1:45.31 = Button times

**Relay format:**
```
Lane 3  TeamName A              3:12.45  **
  1) Jones r:+0.65   48.23 (48.23)
  2) Smith r:+0.18   47.89 (1:36.12)
  3) Brown r:+0.22   48.11 (2:24.23)
  4) Davis r:+0.16   48.22 (3:12.45)
```

**Key data:**
- r:+0.XX = Relay exchange time (legal if 0.00 to +0.30)
- Split times in parentheses = Cumulative time

### Omega Quantum Printout

**Precision difference:**
```
Lane 5  Johnson, Sarah     1:45.234  (touchpad)
                           1:45.28   (button A)
                           1:45.31   (button B)
```

**Note the extra digit** - Omega records to 0.001s (but USA Swimming only recognizes 0.01s for records)

### Daktronics OmniSport Printout

**Similar to CTS, but may include:**
- Time-of-day stamp
- Water temperature (if sensor connected)
- Altitude compensation (for high-altitude pools)

---

## Troubleshooting by System Type

### CTS System 6 Common Issues

**Problem:** Printer not working  
**Likely cause:** Wrong printer driver selected in setup  
**Coach action:** Ask operator to check "Setup → Printer" menu

**Problem:** Touchpad not registering  
**Likely cause:** Loose connector at deck plate  
**Coach action:** Notify official; backup buttons still work

### Daktronics OmniSport Common Issues

**Problem:** Scoreboard not updating  
**Likely cause:** Radio channel mismatch  
**Coach action:** Results still valid; operator needs to reset radio settings

**Problem:** Battery warning displayed  
**Likely cause:** Console battery low (but still functional)  
**Coach action:** Results still accurate; backup power active

### Omega Quantum Common Issues

**Problem:** "Pad Not Ready" warning  
**Likely cause:** Arming delay still active (pad touched recently)  
**Coach action:** Wait 0.5s; pad will re-arm automatically

**Problem:** Split times not printing  
**Likely cause:** Split arm function not enabled  
**Coach action:** Ask operator to enable "Split Arm All"

---

## The Future: Fully Wireless Systems

**What's coming:**
- Wireless touchpads (battery-powered, no deck cables)
- Mobile app timing (backup/recreational use)
- AI-powered video timing (computer vision backup)
- Blockchain time verification (tamper-proof records)

**When:**
- Wireless pads: Already in limited use (Omega)
- Mobile apps: Available now (but not USA Swimming sanctioned)
- Video timing: Pilot programs at NCAA level
- Blockchain: 3-5 years out (experimental)

---

## Cross-References

- [[Timing-System-Basics-For-Coaches]] - How timing works
- [[Meet-Equipment-Reference-Guide]] - Daktronics specifics
- [[USA-Swimming-Timing-Rules]] - Official regulations
- [[Relay-Exchange-Measurement]] - How r:+0.XX is calculated

---

**Coach's Bottom Line:**

> Don't obsess over which timing system is "best." They all meet USA Swimming standards. What matters: (1) Is the operator trained? (2) Are touchpads working? (3) Do results match your expectations? If yes to all three, the brand doesn't matter.

**Key Coaching Insight:**
- **CTS** = Industry standard, you'll see it everywhere
- **Daktronics** = Great for dual swimming/diving facilities
- **Omega** = Olympics and elite international (expensive overkill for age-group)
- **Superior** = Budget option for small programs

**Your job:** Know what data your system CAN provide (splits, relay exchanges), and make sure you're getting it.
