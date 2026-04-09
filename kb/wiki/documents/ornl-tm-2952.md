# ORNL-TM-2952

## Metadata

- Doc ID: `ornl-tm-2952`
- Primary report number: ORNL-TM-2952
- All report numbers: ORNL-TM-2952
- Report series: ornl-technical-memorandum
- Date: 1971
- Authors: EXCHANGERS FOR THE MSBR, A. P. Fraas, M. E. LaVerne, NOTICE, UNION CARBIDE CORPORATION
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-2952/ORNL-TM-2952/hybrid_ocr/ORNL-TM-2952.md`
- SHA256: `129eecb5349c63982efc7fa9218753d59d66731774d28b4feb4d169125106312`

## Topics

- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/materials-and-corrosion.md|materials-and-corrosion]]
- [[../topics/salt-chemistry-and-redox.md|salt-chemistry-and-redox]]
- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/off-gas-fission-products-and-tritium.md|off-gas-fission-products-and-tritium]]
- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]

## Summary

- calculational technique and computer program have general application, it seemed desirable to present the study in this report.
- Table 1. Summary of Effects of Changes in Major Parameters on Number of Tubes, Tube Length, and Heat Exchanger Fuel Inventory
- We assume that the heat exchanger tube bundle is composed of round, smooth tubes with axial fluid flow outside the tubes. We neglect entrance effects and the shell-side pressure drop associated with the tube spacers. Nomenclature for the analysis is given in Table 2.
- The axial heat transport is given in terms of the mass flows, fluid temperature changes, and exchanger geometry by
- The radial heat transport by convection and conduction through the two fluid films and the tube wall, respectively, is given by
- The overall temperature difference, $\Delta T$ , between the two fluids is given by the summation of the temperature differences through the two fluid films and the tube wall,

## Sections

- Ornl-Tm-2952 (lines 1-4)
- Reactor Division (lines 5-6)
- Parametric Survey Of The Effects Of Major Parameters (lines 7-8)
- On The Design Of Fuel-To-Inert-Salt Heat (lines 9-10)
- Exchangers For The Msbr (lines 11-14)
- November 1971 (lines 15-16)
- NOTICE (lines 17-20)
- Oak Ridge National Laboratory (lines 21-26)
- Union Carbide Corporation (lines 27-30)
- U.S. Atomic Energy Commission (lines 31-36)
- CONTENTS (lines 37-38)
- Abstract 1 (lines 39-40)
- Introduction 1 (lines 41-42)
- Summary 2 (lines 43-44)
- Analysis 4 (lines 45-74)
- Parametric Study 15 (lines 75-76)
- Choice Of Inert Salt 29 (lines 77-88)
- References 35 (lines 89-100)
- PARAMETRIC SURVEY OF THE EFFECTS OF MAJOR PARAMETERS ON THE DESIGN OF FUEL-TO-INERT-SALT HEAT EXCHANGERS FOR MOLTEN SALT REACTORS (lines 101-104)
- ABSTRACT (lines 105-108)
- INTRODUCTION (lines 109-116)
- SUMMARY (lines 117-136)
- ANALYSIS (lines 137-140)
- Design Bases and Criteria (lines 141-161)
- Derivation of Heat Exchanger Equations (lines 162-165)
- Heat Balances (lines 166-199)
- Convective Heat Transfer (lines 200-211)
- Temperature Difference Between Fluids (lines 212-225)
- Pressure Drops (lines 226-261)
- Solution of the Equations (lines 262-265)
- Reduction to a Single Equation (lines 266-339)
- Computer Solution (lines 340-343)
- Extensions of the Analysis (lines 344-347)
- Other Fluids (lines 348-351)
- Tube Patterns (lines 352-363)
- Other Conditions (lines 364-373)
- PARAMETRIC STUDY (lines 374-466)
- CHOICE OF INERT SALT (lines 467-470)
- Materials Compatibility Considerations (lines 471-480)
- Melting Point (lines 481-490)
- Leakage Problems (lines 491-494)
- Off-Gas Problems (lines 495-498)
- Heat Transfer Performance (lines 499-502)
- Tritium Leakage (lines 503-506)
- REFERENCES (lines 507-530)
- Appendices (lines 531-536)
- APPENDIX A (lines 537-538)
- Solution of the Heat Exchanger Equations (lines 539-662)
- APPENDIX B. FORTRAN PROGRAM FOR COMPUTER SOLUTION OF THE HEAT EXCHANGER EQUATIONS (lines 663-666)
- Program Line No. (lines 667-668)
- Operation (lines 669-684)
- HEATX2 (lines 685-686)
- 1\* Heatx2. Heat Exchanger Design. M. Layerne. 9102 3-5702 (lines 687-687)
- 2\* 19 Mar 1970 (lines 688-689)
- 100 REAL MUS, MUT, KS, KT, KWALL, LTUBE, NTUBE (lines 690-690)
- 105 DIMENSION DAT(20) (lines 691-691)
- 110 C00M0N CLAM, CURT, S1, S2, S3, S4, S5, T1, T2, T3, T4, T5 (lines 692-692)
- 115 Pi = 3.141592654; Pi04 = Pi/4. (lines 693-694)
- 125 Tw0Gc = 64.348*3600;2; Coo = .5*Pi/Sqrt(3.) (lines 695-695)
- 130 1 Dat(20) = Dat(20)+1.0 (lines 696-696)
- 135 Read, Nin; If(Nin) 21,21 (lines 697-697)
- 140 Read, (J,Dat(J), I=1, Nin) (lines 698-698)
- 145 O = Dat(1) (lines 699-699)
- 150 Dps = Dat(2); Tsi = Dat(3); Ts0 = Dat(4) (lines 700-701)
- 160 Dpt = Dat(9); Tti = Dat(10); Tt0 = Dat(11) (lines 702-703)
- 170 Do = Dat(16); Tw = Dat(17); Kwall = Dat(18) (lines 704-704)
- 175 Rhow = Dat(19); Icase = Dat(20) (lines 705-705)
- 180 PRINT 30, ICASE (lines 706-706)
- 185 3Oformat(/"Case", I3) (lines 707-707)
- 190 Dps = 144.*Dps; Dpt = 144.*Dpt (lines 708-708)
- 195 Do = Do/12.; Tw = Tw/12.; Dt = Do-2.*Tw (lines 709-709)
- 200 Ao = Pi04*Do*Do; At = Pi04*Dt*Dt; Aw = Ao-At (lines 710-710)
- 205 Dts = Tsi-Tso; Dtt = Tt0-Tti (lines 711-711)
- 210 Dt1 = Tsi-Tto; Dt2 = Ts0-Tti (lines 712-712)
- 215 Dm = (Do-Dt)/Log(Do/Dt) (lines 713-713)
- 220 Co8 = Dt1; If(Dt1-Dt2) 2,3,2 (lines 714-714)
- 225 2 Co8 = (Dt1-Dt2)/Log(Dt1/Dt2) (lines 715-715)
- 230 3 Co5 = Q/Pi (lines 716-716)
- 235 Coi = Q/(Cps*Dts); Co2 = Q/(At*Cpt*Dtt) (lines 717-717)
- 240 Co3 = C05/D0; Co4 = C05/Dt; Cos = C05*Tw/(Dm*Kwall) (lines 718-718)
- 245 Co6A = (Cps*Ks+2*Mus)+Curt (lines 719-719)
- 250 Co7A = (Cpt*Kt+2*Mut)+Curt/Dt (lines 720-720)
- 255 Co9A = Tw0Gc*Rhos*Dps (lines 721-721)
- 260 C10A = Tw0Gc*Rhot*Dpt*Dt (lines 722-722)
- 265 C11 = Pi04*Do; C12 = Coi/(Co2+C11); C13 = Co3/C05 (lines 723-723)
- 270 C14 = Co4/Cos; C15 = Co2*C08/Cos; N = 0 (lines 724-724)
- 275 Call Sturbj Call Turbj Ias = Iat = 1 (lines 725-725)
- 280 4 Co6 = Co6A*S1/Mus+S3 (lines 726-726)
- 285 Co7 = Co7A*T1*Dt+(T2+T3)/Mut*T3 (lines 727-727)
- 290 Co9 = Co9A/(S4*Mus+S5) (lines 728-728)
- 295 C10 = C10A*(Dt/Mut)+T5/T4 (lines 729-729)
- 300 C16 = C13/C06; C17 = Co9/C10; C18 = C14/C07 (lines 730-730)
- 305 C19 = C15*C10 (lines 731-731)
- 310 E1 = 3.-T5; E4 = (S2-1.)/3. (lines 732-732)
- 315 E2 = 3.-2.*S2-S3+E4*(2.-T5+S5) (lines 733-733)
- 320 E3 = E1-T3+T2*(T5-2.) (lines 734-734)
- 325 E5 = 1.-S2-S3+E4*(1. +S5) (lines 735-735)
- 330 C20 = C16*C10*S2*C17:E4*C12:E5 (lines 736-737)
- HEATX2 CONTINUED (lines 738-740)
- 335 C21 = C18*C10*T2; Gt = 0.9*(C19/(C20+C21))+(1./E2) (lines 741-741)

## Entities

### Alloy-Material

- Hastelloy N (mentions: 4)
- Hastelloy B (mentions: 3)
- molybdenum (mentions: 3)
- INOR-8 (mentions: 2)
- nickel (mentions: 2)
- beryllium (mentions: 1)
- niobium (mentions: 1)
- titanium (mentions: 1)

### Component

- heat exchanger (mentions: 38)
- loop (mentions: 5)
- intermediate heat exchanger (mentions: 4)
- steam generator (mentions: 3)
- off-gas system (mentions: 2)
- pump (mentions: 2)

### Organization

- AEC (mentions: 20)
- ORNL (mentions: 16)
- Union Carbide (mentions: 1)

### Reactor

- ARE (mentions: 24)
- MSBR (mentions: 6)

### Salt-System

- FLiNaK (mentions: 25)
- NaBF4-NaF (mentions: 11)
- NaF (mentions: 5)
- KF (mentions: 2)
- LiF (mentions: 2)
- ThF4 (mentions: 2)
- UF4 (mentions: 2)
- fluoride salt (mentions: 2)
- BeF2 (mentions: 1)
- FLiBe (mentions: 1)
- LiF-BeF2-ThF4 (mentions: 1)
- LiF-BeF2-ThF4-UF4 (mentions: 1)
- LiF-BeF2-UF4 (mentions: 1)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- title_fallback_used
