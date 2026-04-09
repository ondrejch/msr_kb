# ORNL-TM-2029

## Metadata

- Doc ID: `ornl-tm-2029`
- Primary report number: ORNL-TM-2029
- All report numbers: ORNL-TM-2029, ORNL-3996
- Report series: ornl-technical-memorandum
- Date: 1967
- Authors: MASTER, W. K. Crowley, J.R.Rose, LEGAL NOTICE, J. R. Rose
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-2029/ORNL-TM-2029/hybrid_ocr/ORNL-TM-2029.md`
- SHA256: `2d8c5eaa148a0e0ede6dba70dba83a4a4879492b46b7f83b54068abbc8accb76`

## Topics

- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]
- [[../topics/safety-shielding-and-remote-maintenance.md|safety-shielding-and-remote-maintenance]]
- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]
- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/reactor-operations.md|reactor-operations]]

## Summary

- This report was prepared as an account of Government sponsored work. Neither the United States, nor the Commission, nor any person acting on behalf of the Commission:
- B. Assumes any liabilities with respect to the use of, or for damages resulting from the use of any information, apparatus, method, or process disclosed in this report.
- 1P. R. Kasten, E. S. Bettis, and R. C. Robertson, "Design Studies of 1000-Mw(e) Molten-Salt Breeder Reactors," USAEC Report ORNL-3996, Oak Ridge National Laboratory, August 1966.
- where $M$ is a point between $x$ and $x + \Delta x$ . Equation 2 is substituted into Eq. 1 and $\Delta \theta$ is canceled.
- The common term $-kA_{1}\left.\frac{dT}{dx}\right|_{x}$ is canceled, and it is noted that $\frac{d}{dx}\left(\frac{dT}{dx}\right) = d^2 T / dx^2$ . The resulting expression is given in Eq. 4.
- Equation 5 is integrated twice, and if $Q \neq Q(x)$ ,

## Sections

- Ornl-Tm-2029 (lines 1-2)
- Master (lines 3-10)
- LEGAL NOTICE (lines 11-28)
- November 1967 (lines 29-32)
- U. S. Atomic Energy Commission (lines 33-40)
- CONTENTS (lines 41-46)
- 1. INTRODUCTION 1 (lines 47-47)
- 2. SUMMARY 4 (lines 48-48)
- 3. DEVELOPMENT OF ANALYTICAL METHODS 6 (lines 49-58)
- 4. PARAMETRIC STUDIES 20 (lines 59-63)
- 5. CONCLUSIONS 35 (lines 64-78)
- LIST OF TABLES (lines 79-94)
- List Of Figures (lines 95-98)
- INVESTIGATION OF ONE CONCEPT OF A THERMAL SHIELD FOR THE ROOM HOUSING A MOLTEN-SALT BREEDER REACTOR (lines 99-100)
- Abstract (lines 101-104)
- 1. INTRODUCTION (lines 105-123)
- 2. SUMMARY (lines 124-139)
- 3. DEVELOPMENT OF ANALYTICAL METHODS (lines 140-154)
- Steady-State Condition (lines 155-442)
- Calculational Procedure (lines 443-486)
- Transient Case (lines 487-525)
- 4. PARAMETRIC STUDIES (lines 526-535)
- Cases Studied for Steady-State Condition (lines 536-587)
- Case Studied for Transient Condition (lines 588-623)
- Appendices (lines 624-629)
- Appendix A (lines 630-631)
- EQUATIONS NECESSARY TO CONSIDER A MULTIENERGETIC GAMMA CURRENT (lines 632-685)
- Appendix B (lines 686-687)
- EVALUATION OF THE CONVECTIVE HEAT TRANSFER COEFFICIENT (lines 688-748)
- Appendix C (lines 749-750)
- VALUES OF PHYSICAL CONSTANTS USED IN THIS STUDY (lines 751-760)
- Appendix D (lines 761-762)
- TSS COMPUTER PROGRAM (lines 763-783)
- Preparation of Input Data (lines 784-847)
- Preparation of Case Data (lines 848-853)
- Typical Computer Sheets (lines 854-865)
- Program Tss (lines 866-866)
- Dimension Odpts(6) (lines 867-867)
- Dimension Qsi(8), Enui(8), Amui(8), Alpha(6), Beta1(8), Ai(8), (lines 868-868)
- Jeml2(8), Amu2(8), Alpha2(8), Beta2(8), A2(8), Emu3(8), Amu3(8), (lines 869-869)
- 2Alpha3(8), Beta3(8), A3(8), Emu4(8), Amu4(8), Alpha4(8), Beta4(8), (lines 870-870)
- 3A4(8), Eyus(8), Amu5(8), Alpha5(8), Beta5(8), As(8) (lines 871-871)
- Dimension Eli(32), El2(32), El3(32), El4(32), El5(32), T6(32), (lines 872-872)
- Ibof(32), Bah(32) (lines 873-873)
- Dimension Qdep1(6), Qs2(6), Qv1(6), Qv2(6), Qdep2(6), Qs3(6), (lines 874-874)
- Iov3(6), Odep3(6), Os4(6), Ov4(6), Odep4(6), Os5(6), Ov5(6), (lines 875-875)
- 2Odep5(6), B(6), Di(6), Ei(6), D2(6), E2(6), Fi(6), F2(6), F3(6), (lines 876-876)
- 3Ftf(6), Sum(6), Sump(6), Ri(6), Rei(6), R2(6), Re2(6) (lines 877-877)
- Read (50, 1000) (Os1, Emu1, Amu1, Alphai, Beta1, (lines 878-878)
- Ia1, Emu2, Amu2, Alpha2, Beta2, A2, Emu3, (lines 879-879)
- 2Aml3, Alpha3, Beta3, A3, Emu4, Amu4, Alpha4, (lines 880-880)
- 3Beta4, A4, Emu5, Amu5, Alpha5, Beta5, A5) (lines 881-881)
- Read (50, 1000)(Con1, Con2, Con3, Con4, Con5, To, Ht, Hf) (lines 882-882)
- Read (50, 1001)(Ta, Epsil, Vel, Achan, Cp, Rho, Sigma) (lines 883-883)
- Read (50, 1000)(Eli1, El21, El31, El41, El51T617) (lines 884-884)
- Ibof(I), Bam(I), I=1.32) (lines 885-885)
- C BEGIM MAIN PROGRAM (lines 886-886)
- Do 5000 I=1.32 (lines 887-887)
- Ta = 560. (lines 888-888)
- Elx1 = El1(I) (lines 889-889)
- Elx2 = El2(I) (lines 890-890)
- Elx3 = El3(I) (lines 891-891)
- Elx4 = El4(I) (lines 892-892)
- Elx5 = El5(I) (lines 893-894)
- Qdepy1 = 0. (lines 895-895)
- Qdepy2 = 0. (lines 896-896)
- Qdepy3 = 0. (lines 897-897)
- Qdepy4 = 0. (lines 898-898)
- Qdepy5 = 0. (lines 899-899)
- C CALCULATION OF SOURCE TERM AND GAMMA HEAT DEPOSITION TERMS (lines 900-900)
- Do 100 J = 1.1 (lines 901-901)
- 1 Qvi(J) = Qs1(J)*Ehui(J) (lines 902-902)
- 2 Odepi(J) = Qvi(J)*(((Ai(J)*Expamui(J)*Elxi*(Alpha1(J)=1.)))/ (lines 903-903)
- 1 (Aput(J)*(Alpha1(J)=1.))+(I,A1(J))*Expamui(J)*Elxi*(Beta1(J)+ (lines 904-904)
- 2I,(J))(Amui(J)*Beta1(J)=I,(J))))=(Ai(J)/(Amui(J)*(Alpha1(J)=I,(J)))= (lines 905-905)
- -3(I,A1(J))/(Amui(J)*Beta1(J)=I,(J)))) (lines 906-906)
- 3 Os2(J) = Osij*Odepi(J) (lines 907-907)
- 4 Qv2(J) = Qs2(J)*Ehuij) (lines 908-908)
- 5 Odep2(J) = Ov2(J)*(((A2(J)*Expamui2(J)*Elx2*(Alpha2(J)=I,(J)))/ (lines 909-909)
- 1 (Apu2(J)*(Alpha2(J)=I,(J))=((I,A2(J))*Expamui2(J)*Elx2*(Beta2(J) (lines 910-910)
- 2+I,(J))/Amu2(J)*(Beta2(J)=I,(J)))=(A2(J)/Amu2(J)*(Alpha2(J)=I,(J))) (lines 911-911)
- 3=(I,A2(J))/(Amu2(J)*Beta2(J)=I,(J))) (lines 912-912)
- 6 Os3(J) = Qs1(J)*Odepi(J)*(Opepi(J)) (lines 913-913)
- 7 Qv3(J) = Qs3(J)*Ehuij) (lines 914-914)
- 8 Odep3(J) = Ov3(J)*(((A3(J)*Expamui3(J)*Elx3*(Alpha3(J)=I,(J)))/ (lines 915-915)
- 1 (Apu3(J)*(Alpha3(J)=I,(J))=((I,A3(J))*Expamui3(J)*Elx3*(Beta3(J) (lines 916-916)
- 2+I,(J))/Amu3(J)*(Beta3(J)=I,(J)))=(A3J)/Amu3(J)*(Alpha3(J)=I,(J))) (lines 917-917)
- 3=(I,A3J/(Amu3J)*(Beta3J)=I,(J))) (lines 918-918)
- Elx4 = Elx4*Elx3 (lines 919-919)
- Odpts(J) = Ov3(J)*(((A4J)*Expamui4(J)*Elx4*(Alpha4(J)=I,(J)))/ (lines 920-920)
- 1 (Apu4(J)*(Alpha4(J)=I,(J))=((I,A4J)*Expamui4(J)*Elx4*(Beta4(J) (lines 921-922)
- 3=(I,A4J/(Amu4J)*(Beta4J)=I,(J))) (lines 923-923)
- Odep4(J) = Odpts(J)*Odepi(S) (lines 924-924)
- Elx4 = Elx4*Elx3 (lines 925-925)
- 12 Os5(J) = Qs1(J)*Odepi(S) -Odepi(S) -Odepi(S) (lines 926-940)
- Or Form And Is Therefore Not Acceptable (lines 941-942)
- 2007 FORMAT(5H1CASE,13) (lines 943-946)
- 2009 FORMAT(34HKCALCULATION AT TOP OF AIR CHANNEL) (lines 947-966)
- Appendix E (lines 967-968)
- NOMENCLATURE (lines 969-1000)

## Entities

### Alloy-Material

- stainless steel 304 (mentions: 1)

### Component

- heat exchanger (mentions: 2)
- loop (mentions: 1)

### Organization

- ORNL (mentions: 5)
- AEC (mentions: 3)
- Union Carbide (mentions: 1)

### Reactor

- ARE (mentions: 38)
- MSBR (mentions: 9)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- title_fallback_used
