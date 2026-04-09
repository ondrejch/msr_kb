# ORNL/TM-4210

## Metadata

- Doc ID: `ornl-tm-4210`
- Primary report number: unknown
- All report numbers: none detected
- Report series: ornl-technical-memorandum
- Date: 1976
- Authors: C.W.Kee, L.E.McNeese, NOTICE, UNION CARBIDE CORPORATION, Page No.
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-4210/ORNL-TM-4210/hybrid_ocr/ORNL-TM-4210.md`
- SHA256: `40e9294a8416e7c5e7161255bec3163a929eb0c008fdd563736ae47d045e4332`

## Topics

- [[../topics/off-gas-fission-products-and-tritium.md|off-gas-fission-products-and-tritium]]
- [[../topics/materials-and-corrosion.md|materials-and-corrosion]]
- [[../topics/graphite-and-moderator-behavior.md|graphite-and-moderator-behavior]]
- [[../topics/reactor-physics-neutronics.md|reactor-physics-neutronics]]
- [[../topics/salt-chemistry-and-redox.md|salt-chemistry-and-redox]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]

## Summary

- $(k_{i}a)_{m,n}$ = mass transfer rate constant for transfer of species i from region m to region n, cm³/sec [the ratio of $(k_{i}a)_{m,n}$ and $(k_{i}a)_{n,m}$ is a distribution function, as discussed in Sect. 2.2.2],
- The terms on the diagonal $(i = j)$ are matrices of the form:
- R is a matrix whose element in row n and column m is
- The resulting system of equations, when used with a constant vector indicating feed streams, is the set of Eqs. (2).
- This equation is broken into two contributions to matrix terms analogous to a flow rate so that:
- where region n is the liquid phase, and region m the gas phase.

## Sections

- Ornl/Tm-4210 (lines 1-6)
- Chemical Technology Division (lines 7-8)
- Mrpp - Multiregion Processing Plant Code (lines 9-12)
- September 1976 (lines 13-14)
- Notice (lines 15-18)
- Oak Ridge National Laboratory (lines 19-24)
- Union Carbide Corporation (lines 25-28)
- Energy Research And Development Administration (lines 29-30)
- TABLE OF CONTENTS (lines 31-34)
- Abstract 1 (lines 35-36)
- 1. INTRODUCTION 1 (lines 37-38)
- 2. EQUATIONS AND ASSUMPTIONS 3 (lines 39-44)
- 3. NUMERICAL METHODS EMPLOYED 13 (lines 45-58)
- 4. LIMITATIONS AND SPECIAL CONSIDERATIONS 21 (lines 59-68)
- 5. REFERENCES 25 (lines 69-70)
- Appendix A: Description Of Subroutines Used 27 (lines 71-72)
- Appendix B: Input 42 (lines 73-74)
- Appendix C: Output 60 (lines 75-76)
- MRPP - MULTIREGION PROCESSING PLANT CODE (lines 77-80)
- ABSTRACT (lines 81-84)
- 1. INTRODUCTION (lines 85-98)
- 2. EQUATIONS AND ASSUMPTIONS (lines 99-102)
- 2.1 Model for the Reactor (lines 103-112)
- where (lines 113-132)
- 2.2 Model for the Processing Plant (lines 133-138)
- 2.2.1 Material balance equations (lines 139-212)
- 2.2.2 Mass transfer coefficients (lines 213-316)
- 3. NUMERICAL METHODS EMPLOYED (lines 317-318)
- 3.1 Solution of Reactor Material Balance Equations (lines 319-322)
- 3.2 Solution of the Processing Plant Material Balance Equations (lines 323-328)
- 3.3 Iteration with Reactor Code (lines 329-336)
- 3.4 Calculation of Molar Volumes (lines 337-342)
- 3.5 Correction of Distribution Coefficients (lines 343-361)
- E - E _ {0} = 0, (lines 362-466)
- 3.6 Investigation of Faster Solution Methods (lines 467-472)
- 4. LIMITATIONS AND SPECIAL CONSIDERATIONS (lines 473-474)
- 4.1 Limitations of Steady State Calculation (lines 475-482)
- 4.2 System of Units (lines 483-486)
- 4.3 Description of Particular Items Using Mass Transfer Coefficients (lines 487-494)
- 4.4 Uses Requiring Modifications (lines 495-502)
- 5. REFERENCES (lines 503-512)
- APPENDIXES (lines 513-514)
- USER'S MANUAL (lines 515-516)
- APPENDIX A: DESCRIPTION OF SUBROUTINES USED (lines 517-520)
- Subroutine MATADOR (lines 521-534)
- Subroutine AMATRX (lines 535-574)
- Subroutine BESI(X,N,BI,IER) (lines 575-588)
- Subroutine CHEMPL (lines 589-606)
- Subroutine KEE (lines 607-610)
- Subroutine RESULT (XEQL) (lines 611-650)
- MAIN Program (lines 651-664)
- Subroutine EQKN (lines 665-668)
- Subroutine VOLUME (NLEFT) (lines 669-680)
- Subroutine MATQD(A,X,NR,NV,DET,NA,NX) (lines 681-702)
- Subroutine OUTO (lines 703-722)
- Miscellaneous Short Routines (lines 723-730)
- Subroutine ZERO(A,B,N) (lines 731-734)
- Subroutine HALF(A.I) (lines 735-738)
- Function NOAA (NUCLI) (lines 739-742)
- APPENDIX B: INPUT (lines 743-746)
- Nuclear Library (AMATRX) (lines 747-753)
- Format(F10.5,4I2) (lines 754-765)
- Format(5I10) (lines 766-779)
- Light Elements (lines 780-782)
- Nucl(I), Dlam,Iu,Fbi,Fp,Fpi,Ft,Fa,Sigth,Fng1,Fna,Fnp,Rith,Fina,Finp (lines 783-783)
- Sigmev,Fn2N1,Ffna,Ffnp,Q,Fg (lines 784-784)
- Format(I6,F5.3,I1,5F5.3,E5.2,3F3.3,E5.2,2F3.3,E5.2,3F3.3,F4.3,F3.3,F6.3) (lines 785-788)
- Actinides (lines 789-792)
- Format(I6,F5.3,I1,5F3.3,2E5.2,F3.3,4E5.2,F3.3,F4.4,F3.3,2E5.2) (lines 793-797)
- Fission Products (lines 798-805)
- MATADOR Input (lines 806-808)
- B. Flux, Power, Flow1, Therm, Res, Fast, Fpabs (lines 809-810)
- Format(8F10.5) (lines 811-826)
- C. EPS, ERR, MAX, KARD (lines 827-828)
- Format(2F10.3,2I5) (lines 829-840)
- Matador. (lines 841-842)
- D. Area, Vol, Radius, Porty, Film, Diffy, Solbty, Vratio (lines 843-844)
- Format(8E10.3) (lines 845-860)
- E. Igas, Idau, Ient, I3, I3Dep, Next (lines 861-861)
- Format(4X,16,4X,16,15,4X,16,215) (lines 862-880)
- F. Film,Diffy,Solbty Format(3E12.5) (lines 881-885)
- G. Input(I),X(I),I=1,4 (lines 886-887)
- Format(4(I5,F10.3)) (lines 888-897)
- H. Time(N),N=1,10 (lines 898-899)
- Format(10E8.1) (lines 900-903)
- I. Np(I), I=1, 100 (lines 904-905)
- Format（40（12）） (lines 906-909)
- J. Nz(I),Eff(I),I=1,8 (lines 910-911)
- Format(8(I3,F7.4)) (lines 912-919)
- Format(8F10.3) (lines 920-933)
- L. Ntime(I),Punit(I),I=1,10 Format(10(I4,A4)) (lines 934-939)
- M. Nz(I),Eff(I),I=1,8 Format(8(I3,F7.4)) (lines 940-946)
- MAIN input (lines 947-951)
- A. I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,Nwaste,I12,I13,I14,I15 Format (16I5) (lines 952-974)
- B. Eps, Err, Max (lines 975-976)
- Format (2F10.3, I5) (lines 977-986)
- C. WTDX (lines 987-988)
- Format (F10.3) (lines 989-992)
- D. Nreg, Ninx, Niny, Ninp, Nrate, Krate, Jrate (lines 993-994)
- Format (1615) (lines 995-1016)

## Entities

### Alloy-Material

- graphite (mentions: 12)

### Component

- drain tank (mentions: 2)
- heat exchanger (mentions: 2)
- graphite moderator (mentions: 1)

### Organization

- ORNL (mentions: 10)
- Union Carbide (mentions: 1)

### Reactor

- ARE (mentions: 94)
- MSBR (mentions: 5)
- MSRE (mentions: 1)

### Salt-System

- KF (mentions: 1)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- report_number_not_detected
