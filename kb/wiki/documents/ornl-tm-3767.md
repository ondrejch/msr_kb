# HYBRID COMPUTER SIMULATION OF THE MSBR

## Metadata

- Doc ID: `ornl-tm-3767`
- Primary report number: unknown
- All report numbers: none detected
- Report series: ornl-technical-memorandum
- Date: unknown
- Authors: O. W. Burke, Page
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-3767/ORNL-TM-3767/hybrid_ocr/ORNL-TM-3767.md`
- SHA256: `c73e7582022e99e2820c10ba89766036e0dc209f6d36d852ed8d33dd5ed46225`

## Topics

- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]
- [[../topics/graphite-and-moderator-behavior.md|graphite-and-moderator-behavior]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/reactor-physics-neutronics.md|reactor-physics-neutronics]]
- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]
- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/materials-and-corrosion.md|materials-and-corrosion]]

## Summary

- In order to get a "feel" for the dynamic behavior of the MSBR plant as well as to discover the plant control problems and their solutions, it was imperative that a simulation model of the plant be developed.
- The PDP-10 digital computer is a 36-bit word machine with a fast memory storage capacity of 32K words.
- The AD-4 analog computer is a solid state, $\pm 100\mathrm{V}$ reference machine. The mode switching is accomplished in 1 microsec. It contains patchable logic components
- The heat generated in the primary salt in the core is transferred from the tube side of the primary heat exchangers to a countercurrent secondary salt passing through the shell side. The secondary salt flows in a closed secondary loop to the horizontal supercritical
- A flow diagram of the MSBR plant is shown in Fig. 1. The interesting physical constants are listed in Table 1, and the plant parameters are listed in Table 2.
- As previously stated, the hybrid computer is used to simulate the steam generator in some detail. The older analog computer is used to simulate the rest of the system.

## Sections

- HYBRID COMPUTER SIMULATION OF THE MSBR (lines 1-4)
- ABSTRACT (lines 5-10)
- CONTENTS (lines 11-29)
- -NOTICE (lines 30-33)
- 1. INTRODUCTION (lines 34-39)
- 2. DESCRIPTION OF COMPUTER* (lines 40-51)
- 3. DESCRIPTION OF MSBR SYSTEM (lines 52-65)
- 4. DEVELOPMENT OF THE COMPUTER MODEL OF THE PLANT (lines 66-71)
- 4.1 Steam Generator Model (lines 72-77)
- Grnl-06.79-663 (lines 78-206)
- 4.2 The Analog Computer Model of the System Exclusive of the Steam Generator (lines 207-210)
- 4.2.1 The Nuclear Kinetics Model (lines 211-267)
- 4.2.2 The Reactor Core Heat Transfer Model (lines 268-318)
- 4.2.3 Piping Lag Equations (lines 319-344)
- 4.2.4 Primary Heat Exchanger Equations (lines 345-465)
- Ornl Dwg. 72-5793 (lines 466-468)
- 4.2.5 System Controllers (lines 469-476)
- 4.2.5.1 Reactor Outlet Temperature Controller (lines 477-522)
- 4.2.5.2 Secondary Salt Flow Controller (lines 523-538)
- 4.2.5.3 Steam Pressure Controller (lines 539-552)
- Ornl Dwg. 72-5792 (lines 553-559)
- 5. RESULTS OF SIMULATION EXERCISES (lines 560-567)
- 1. Steady State Part Loads (lines 568-580)
- 2. Rapid Change in Load Demand (lines 581-584)
- 3. Changes in Secondary Salt Flow Rate (lines 585-588)
- 4. Step Changes in Nuclear Fission Power Level (lines 589-592)
- 5. Changes in Reactivity (lines 593-622)
- References (lines 623-631)
- 7. APPENDIX (lines 632-633)
- 7.1 A: Development of Computer Model (lines 634-635)
- 7.1.1 The All-Analog Model (lines 636-641)
- 7.1.1.1 Nuclear Kinetics Model (lines 642-749)
- Temperature Coefficients of Reactivity (lines 750-859)
- 7.1.1.2 The Reactor Core Heat Transfer Model (lines 860-861)
- 7.1.1.2.1 Graphite Heat Transfer Equations (lines 862-1061)
- 7.1.1.3 Piping Lag Equations (lines 1062-1081)
- 7.1.1.4 Primary Heat Exchanger Model (lines 1082-1083)
- 7.1.1.4.1 Primary Salt Equations (lines 1084-1135)
- 7.1.1.4.2 Tube Wall Heat Transfer (lines 1136-1255)
- 7.2.1 Program (lines 1256-1257)
- C MSBR STEAM GENERATOR SIMULATION DIMENSION THETA(100),V(100),T(100),P(100),WMU(100),CW(100),PR(100) (lines 1258-1262)
- Ix,Pl,Hl,Vl,Thetal) (lines 1263-1266)
- C M Is The N0. Of Iterations Per Time Step. Read(Ir,300) M (lines 1267-1268)
- 300 FFORMAT(15) (lines 1269-1269)
- Call Tscal(Ie,It) (lines 1270-1270)
- Read(Ir,Io5) Dx,Dt,Pk,Pkf (lines 1271-1271)
- 105 Fortmat(2F6.2,2F10.5) (lines 1272-1272)
- Read(Ir,106) Hsf,Sph (lines 1273-1274)
- Read(Ir, 107) Imdac, Iadh (lines 1275-1276)
- 103 F#Mat(7F10.2) (lines 1277-1277)
- Read(Ir,110) Cfcøn, Sfv, Rk2, Sfvs (lines 1278-1278)
- 110 Fortmat(3F10.2,F10.7) (lines 1279-1279)
- Read (Ir,120) Iadv (lines 1280-1280)
- 120 FFORMAT(16) (lines 1281-1281)
- Read (Ir,122) Irdac,Imdac1 (lines 1282-1284)
- C Read In Table Values. (lines 1285-1288)
- Read(Ir,101) Tabd (lines 1289-1290)
- Read(Ir,Io1) Tabt (lines 1291-1292)
- 101 Förma(T(1Of8.2) (lines 1293-1294)
- Read(Ir,100) Tabh (lines 1295-1296)
- 100 F#Mat(10P8.2) (lines 1297-1297)
- Read(Ir,104) Tabmu (lines 1298-1298)
- Read(Ir,104) Tabk (lines 1299-1299)
- Read(Ir,104) Tabpr (lines 1300-1303)
- C Read In Table Limits. (lines 1304-1304)
- Read (Ir,102) Tminh,Tmaxh,Delth,Nth,Pminh,Pmaxh,Delph,Nph (lines 1305-1305)
- Read (Ir,102) Hmind,Hmaxd,Delhd,Nhd,Pmind,Pmaxd,Delpd,Npd (lines 1306-1306)
- Read (Ir,102) Tminm,Tmaxm,Deltm,Ntm,Pminm,Pmaxm,Delpm,Npm (lines 1307-1307)
- Read (Ir,102) Tmink,Tmaxk,Deltk,Ntk,Pmink,Pmaxk,Delpk,Npk (lines 1308-1308)
- Read (Ir,102) Tminp,Tmaxp,Deltp,Ntp,Pminp,Pmaxp,Delpp,Npp (lines 1309-1309)
- Read (Ir,102) Hint,Hmaxt,Deltt,Ntt,Pmint,Pmaxt,Delpt,Npt (lines 1310-1311)
- 102 Fortmat(3F8.2,I6,3F8.2,I5) (lines 1312-1313)
- C Read Initial Guesses F0R Values Of Variables. Read(Ir,108) H (lines 1314-1315)
- 108 Fformat(10F8.1) (lines 1316-1316)
- Read(Ir,108) P (lines 1317-1317)
- Read(Ir,108) Theta (lines 1318-1318)
- Read(Ir,108) V (lines 1319-1320)
- C SET UP ADDRESSES F0R OUTPUTTING VALUES OF VARIABLES (lines 1321-1322)
- C From The Analog Computer. Read(Ir,109) I0Uta (lines 1323-1324)
- 109 FORTMAT(4I6) (lines 1325-1326)
- C Initialize C0Eff. Device Setting Routines. Call Addr(Iadh, Iadhd) (lines 1327-1327)
- Call Addr(Iadv, Iadvd) (lines 1328-1328)
- Call Preb1(Iadhd, Idh, 3) (lines 1329-1329)
- Call Preb2(Iadhd, Idh1, 2) (lines 1330-1330)
- Call Preb3(Iadvd, Idv, 7) (lines 1331-1331)
- Call Preb4(Iadvd, Idv1, 4) (lines 1332-1343)
- 3006 Plb=Ilb(1) Tlb=Ilb(2)*1.E-1 Vs=Ilb(3)*1.E-4 (lines 1344-1347)
- Call Addr(6262,Iab3) Call Scanh(Iab3,Iar,2) (lines 1348-1351)
- 1) Go To 1! (lines 1352-1352)
- Write(Iw,Io) (lines 1353-1356)
- C Get Value Of H At Left Boundary, Hlb, From H(P,T), Tabh. (lines 1357-1358)
- 11Call Tercp2(Tabh,Tlb,Plb,Hlb,Tminh,Tmaxh,Delth,Nth,Pminh,Pmaxh,Delp (lines 1359-1360)
- Ih,Nph) (lines 1361-1362)
- Hlbs=(Hlb-1100)*25. (lines 1363-1364)
- Xyhlbs-.5 (lines 1365-1366)
- Idh(3)=Ifix(Xy) (lines 1367-1368)
- H0=Hk2*Vs**0.60 (lines 1369-1370)
- C Get Density At Left Boundary, Dlb, From D(P,H) Table, Tabd. (lines 1371-1372)
- If(Plb,Ge,Pmind,And,Plb,Le,Pmaxd,And,Hlb,Ge,Hmind,And,Hlb,Le,Hmaxd (lines 1373-1374)
- 1）G0T021 (lines 1375-1376)

## Entities

### Alloy-Material

- graphite (mentions: 23)
- stainless steel 304 (mentions: 2)
- Hastelloy N (mentions: 1)

### Component

- steam generator (mentions: 33)
- heat exchanger (mentions: 29)
- loop (mentions: 5)
- pump (mentions: 3)
- control rod (mentions: 2)

### Organization

- ORNL (mentions: 9)
- AEC (mentions: 6)
- Foster Wheeler (mentions: 1)

### Reactor

- ARE (mentions: 46)
- MSBR (mentions: 16)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- report_number_not_detected
