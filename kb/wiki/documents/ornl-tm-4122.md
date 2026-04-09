# DEVELOPMENT OF A VENTURI TYPE BUBBLE GENERATOR FOR USE IN THE MOLTEN-SALT REACTOR XENON REMOVAL SYSTEM

## Metadata

- Doc ID: `ornl-tm-4122`
- Primary report number: unknown
- All report numbers: none detected
- Report series: ornl-technical-memorandum
- Date: December 1972
- Authors: C. H. Gabbard, MASTER, Molten-Salt Reactor Program, NOTICE
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-4122/ORNL-TM-4122/hybrid_ocr/ORNL-TM-4122.md`
- SHA256: `e316af1f7da085107a34796f3f19ac513486984ff022773b8dd8dbc1b8400167`

## Topics

- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]
- [[../topics/off-gas-fission-products-and-tritium.md|off-gas-fission-products-and-tritium]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]
- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/materials-and-corrosion.md|materials-and-corrosion]]
- [[../topics/program-history.md|program-history]]

## Summary

- <table><tr><td>Figure 1. Bubble Generator Design Configurations which were
- BUBBLE GENERATOR DESIGN CONFIGURATIONS WHICH WERE
- The photographs, which were about actual size, were enlarged to obtain a total magnification of 8. Enlargements to greater magnification resulted in a loss of resolution. The bubble size distributions for each condition were determined by scaling bubble sizes directly from the
- enlargements. The diameters were measured by comparison with a plastic template having drilled holes ranging from 1/32 to $3/4$ in. in increments of 1/32 in. A volume averaged bubble diameter as defined below was calculated for each distribution:
- where: $n_j$ is the number of bubbles of a given diameter,
- The resolution of the photographs was adequate to measure bubble diameters in the 0.008 in. range (1/16 in. on the enlargement), but no bubbles could be identified in the 0.004 in. diameter range. The results of these tests are shown on Figures 3 and 4.

## Sections

- DEVELOPMENT OF A VENTURI TYPE BUBBLE GENERATOR FOR USE IN THE MOLTEN-SALT REACTOR XENON REMOVAL SYSTEM (lines 1-4)
- Master (lines 5-8)
- Oak Ridge National Laboratory (lines 9-10)
- Operated By Union Carbide Corporation • For The U.S. Atomic Energy Commission (lines 11-24)
- NOTICE (lines 25-28)
- NOTICE (lines 29-36)
- Master (lines 37-40)
- Table Of Contents (lines 41-46)
- LIST OF FIGURES (lines 47-66)
- DEVELOPMENT OF A VENTURI TYPE BUBBLE GENERATOR FOR USE IN THE MCLTEN-SALT REACTOR XENON REMOVAL SYSTEM (lines 67-70)
- ABSTRACT (lines 71-76)
- I. INTRODUCTION (lines 77-82)
- II. BUBBLE GENERATOR DESIGN (lines 83-88)
- Table I (lines 89-90)
- Bubble Generator Criteria (lines 91-102)
- Ornl-Dwg 71-10220 (lines 103-105)
- Figure 1 (lines 106-106)
- Bubble Generator Design Configurations Which Were (lines 107-107)
- Given Reduced Scale Evaluation Tests (lines 108-113)
- III. OPERATING CHARACTERISTICS AND TEST RESULTS (lines 114-118)
- Figure 2 (lines 119-119)
- Bubble Generator Design For The (lines 120-120)
- Gas Systems Technology Facility (lines 121-122)
- III.-1. Bubble Size (lines 123-124)
- III.-1.l Test Condition (lines 125-128)
- III.-1.2 Bubble Size Measurements (lines 129-151)
- Figure 3 (lines 152-155)
- Figure 4 (lines 156-156)
- Bubble Size Produced By Gstf Bubble Generator (lines 157-157)
- As A Function Of Surface Tension (lines 158-160)
- Figure 5 (lines 161-161)
- Surface Tension As A Function Of Sodium Oleate Concentration (lines 162-162)
- For Laboratory Batch Samples And For Loop Samples (lines 163-168)
- III.-1.3 Analysis of Bubble Size Data (lines 169-210)
- III.-2. Gas Injection Pressure Characteristics (lines 211-217)
- Figure 6 (lines 218-219)
- Bubble Size Correlation For Gstf Design Bubble Generator (lines 220-222)
- Figure 7 (lines 223-223)
- Simplified Flow Diagram Of The Gas Systems Technology Facility (lines 224-226)
- Figure 8 (lines 227-253)
- Ornl-Dwg 73-1544 (lines 254-256)
- Figure 9 (lines 257-257)
- Geometry Of Bubble Generator Used In Analysis Of Gas Injection (lines 258-258)
- Pressure And Overall Head Loss (lines 259-310)
- Figure 10 (lines 311-312)
- Pressure Drop Of Gas Feed Passages As A Function (lines 313-313)
- Of Gas Flow Rate (lines 314-336)
- Figure 11 (lines 337-337)
- Pressure Drop Across The Gas Plume Interface (lines 338-338)
- As A Function Of Throat Void Fraction (lines 339-341)
- Figure 12 (lines 342-343)
- And Throat Void Fraction (lines 344-355)
- IV. CONCLUSIONS AND RECOMMENDATIONS (lines 356-369)
- V. ACKNOWLEDGEMENT (lines 370-373)
- NOMENCLATURE (lines 374-425)
- REFERENCES (lines 426-435)
- APPENDIX (lines 436-482)
- 1 REM RGNDGN CHG 6/8/72 CALC PURPLE GEN PRESS DIST (lines 483-484)
- 9 READ A1,A2,A3,A4 (lines 485-486)
- 10 READ F1,G,G9,MO,N (lines 487-488)
- 20 READ D8,P9,P8,T2,K9 (lines 489-490)
- 21 H1=0 (lines 491-492)
- 22 H2=0 (lines 493-494)
- 23 H3=0 (lines 495-496)
- 30 D9=2·10 (lines 497-498)
- 31 D1=2·18 (lines 499-500)
- 45 Po=14.7 (lines 501-502)
- 50 Print "Liq Sg="G,"Mol Wt="Mo,"Dis Press="P9 (lines 503-504)
- 60 Print "Liq Flow="F1,"Thr Dia="D9,"Bore Dia="D1 (lines 505-506)
- 61 D2=D8/12 (lines 507-508)
- 62 D=D1/12 (lines 509-510)
- 63 D0=D9/12 (lines 511-512)
- 70P2=P9+14.7 (lines 513-514)
- 80 T=T2+460 (lines 515-516)
- 90 K1=N/(1-N) (lines 517-520)
- 110 00=F1/(7·48*60) (lines 521-522)
- 120 M1=Q0*G*62.4 (lines 523-524)
- 130 V0=Q0/(0.785*(Do*K9)+2) (lines 525-526)
- 131 $V = 00 / (0.785*(D2*K9) + 2)$ (lines 527-528)
- 132 H=（V0+2-V+2）/64.4 (lines 529-530)
- 140 F0R F2=0 T0 1.41 Step·2 (lines 531-532)
- 150 M2=F2*G9/60 (lines 533-536)
- 161 $P0 = P2 - (H1 + H2 + H3)*62.4*G / 144$ (lines 537-538)
- 170 Q1=Q0+F2*T/493*14.7/(P0*60) (lines 539-540)
- 180 Q2=Q0+F2*T/493*14.7/(P2*60) (lines 541-544)
- 200 V2=Q2/(0.785*(D2*K9)+2) (lines 545-546)
- 210 F9=F2*14.7/P0*T/(493*60) (lines 547-550)
- 230 H1=((V1+2-V2+2)/64.4-0.317/64.4*(V1-V2)+2)*(1.0-X2) (lines 551-552)
- 240 G1=G*Q0/Q1 (lines 553-554)
- 249 F3=F2*T/493*14.7/P0 (lines 555-556)
- 250 H2=-V1*G1*(V1-V0)/(32.2*G)-F3*0.4167 (lines 557-558)
- 260 P0=P2-(H1+H2+H3)*62.4*G/144 (lines 559-560)
- 261 If Po<0 Then 404 (lines 561-562)
- 270 W=K1*1545*T/M0*(P2/P0)×(2-1.0) (lines 563-564)
- 280 H3=W*M2/M1 (lines 565-566)
- 290 P0=P2-(H1+H2+H3)*62.4*G/144 (lines 567-568)
- 300 F3=F2*T/493*14.7/P0 (lines 569-570)
- 310 G8=69*493/T*Po/14.7 (lines 571-572)
- 320 H5=-59·488*F3†2*G8/(G*62.4) (lines 573-578)
- 323 H4=K3*V0+2·50+H5 (lines 579-580)

## Entities

### Component

- loop (mentions: 8)
- pump (mentions: 6)
- drain tank (mentions: 1)

### Organization

- AEC (mentions: 13)
- ORNL (mentions: 9)
- Union Carbide (mentions: 2)

### Reactor

- ARE (mentions: 25)
- MSBE (mentions: 5)
- MSBR (mentions: 4)

### Salt-System

- BeF2 (mentions: 1)
- FLiBe (mentions: 1)
- LiF (mentions: 1)
- fluoride salt (mentions: 1)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- report_number_not_detected
