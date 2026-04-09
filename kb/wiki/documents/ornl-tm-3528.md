# ORNL-TM-3528

## Metadata

- Doc ID: `ornl-tm-3528`
- Primary report number: ORNL-TM-3528
- All report numbers: ORNL-TM-3528
- Report series: ornl-technical-memorandum
- Date: 1971
- Authors: J. W. Cooke, Oak Ridge, Tennessee, Operated by, UNION CARBIDE CORPORATION
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-3528/ORNL-TM-3528/hybrid_ocr/ORNL-TM-3528.md`
- SHA256: `537221982098254133ee8dbe1bb11c3eb3a2abeea5e73a0677f666443a3374e5`

## Topics

- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/materials-and-corrosion.md|materials-and-corrosion]]
- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]
- [[../topics/safety-shielding-and-remote-maintenance.md|safety-shielding-and-remote-maintenance]]

## Summary

- Baumeister and Hamill) solutions were obtained for a limited number and range of variables.
- This report describes the derivation of the interfacial equation, its numerical solution, and the computer program employed. The results and an estimation of their accuracy are presented and compared with the previous solutions.
- If gravitational forces are present, the influence of the differential fluid density, $\rho$ , must be considered. For an interface assumed to be symmetrical about an axis of revolution, the force balance equation for the bubble shown in Fig. 1-b will be
- which is a second-order nonlinear differential equation, with boundary conditions:
- Although Eq. (8) cannot be solved analytically in terms of ordinary functions, its numerical solution is described in the next section.
- A numerical technique of fourth-order accuracy developed by Runge-Kutta was selected to solve the set of simultaneous Eqs. (9), (10), and (11); the iterative equations describing this technique are:

## Sections

- Ornl-Tm-3528 (lines 1-10)
- August 1971 (lines 11-14)
- Oak Ridge National Laboratory (lines 15-20)
- Union Carbide Corporation (lines 21-24)
- U. S. Atomic Energy Commission (lines 25-28)
- CONTENTS (lines 29-56)
- ABSTRACT (lines 57-62)
- INTRODUCTION (lines 63-72)
- DERIVATION OF THE INTERFACIAL EQUATION (lines 73-154)
- NUMERICAL SOLUTION OF THE INTERFACIAL EQUATION (lines 155-222)
- COMPUTER PROGRAM (lines 223-291)
- Range, Running Time, and Accuracy (lines 292-299)
- RESULTS (lines 300-353)
- DISCUSSION OF RESULTS (lines 354-379)
- CONCLUSIONS (lines 380-385)
- REFERENCES (lines 386-399)
- NOMENCLATURE (lines 400-444)
- Greek Letters (lines 445-458)
- Appendices (lines 459-462)
- A. PARAMETRIC CROSSPLOTS (lines 463-478)
- B. TABULATED RESULTS (lines 479-521)
- C. COMPUTER PROGRAM (lines 522-527)
- C Solution Of Interfacial Eq. For The Press. And Vol. (lines 528-528)
- C Within Attached Bubble. Case 1-Attached Above (Positive Beta) (lines 529-530)
- Implicit Real*8(D), Real*4(A-C, E-H, O-Z) (lines 531-531)
- Dimensiona(4), B(4), C(4), D(4), E(8), R(4), G1(10), P(4) (lines 532-532)
- Dimensionda(4), Db(4), Dc(4), Dz(4), De(8), Dp(4), Dr(4) (lines 533-533)
- 9 FORMAT(I1,I2) (lines 534-534)
- 11 READ 9,I,N3 (lines 535-535)
- If (I-1)401,10,501 (lines 536-537)
- C. Solution At Max. Press For Given Values Of R/A (=G) (lines 538-539)
- 300 Format(F15.7) (lines 540-540)
- 10 CONTINUE (lines 541-541)
- Do 201 N4=1,N3 (lines 542-542)
- Read300,G (lines 543-543)
- C ESTIMATE OF INITIAL BETA (lines 544-544)
- If(G.Ge.0.099 And G.Lt.0.4)Goto1001 (lines 545-545)
- If(G.Ge.0.39 And G.Lt.0.8)Goto1002 (lines 546-546)
- If(G.Ge.0.79 And G.Lt.3.01)Goto1003 (lines 547-547)
- 1001 Beta=.11175-.92434*G+3.92521*G**2. (lines 548-548)
- Goto301 (lines 549-549)
- 1002 Beta=2.87267-12.78143*G+16.40021*G**2. (lines 550-550)
- Goto301 (lines 551-551)
- 1003 Beta=16.30443-49.43188*G+40.54628*G**2. (lines 552-552)
- Goto301 (lines 553-553)
- C COURSE BETA GRID (lines 554-554)
- 301 Beta=Beta+0.1*Beta (lines 555-555)
- N20=0 (lines 556-556)
- P(2)=0 (lines 557-557)
- 58 Beta=Beta-.01*Beta (lines 558-558)
- Call Mains(A,B,C,Z,E,H,J,P,Beta,G,R) (lines 559-559)
- If(P(1)-P(2))59,59,60 (lines 560-560)
- 60 P(2)=P(1) (lines 561-561)
- N20=N20+1 (lines 562-562)
- Goto58 (lines 563-563)
- 59 IF(N20-1)301,301,57 (lines 564-564)
- 57 PRINT 50,BETA,H (lines 565-565)
- Print 100 (lines 566-566)
- Print 200,E(8),E(6),E(7),R(1),P(1),V (lines 567-567)
- Beta=Beta+.02*Beta (lines 568-568)
- P(2)=0 (lines 569-569)
- C FINE BETA GRID (lines 570-570)
- 65 Beta=Beta-.001*Beta (lines 571-571)
- Call Mains(A,B,C,Z,E,H,J,P,Beta,G,R) (lines 572-572)
- If(P(1)-P(2))61,61,62 (lines 573-573)
- 62 P(2)=P(1) (lines 574-574)
- Goto65 (lines 575-580)
- 61 PRINT 50,BETA,H (lines 581-581)
- Print 100 (lines 582-582)
- Print 200,E(8),E(6),E(7),R(1),P(1),V (lines 583-583)
- Beta=Beta+.002*Beta (lines 584-584)
- Dp(2)=0 (lines 585-585)
- C EXTRA FINE BETA GRID WITH DOUBLE PRECISION (lines 586-586)
- Dbeta=Beta (lines 587-587)
- Dg=G (lines 588-588)
- 66 Dbeta=Dbeta-.0001*Dbeta (lines 589-589)
- Call Maind(Da,Db,Dc,Dz,De,Dh,J,Dp,Dbeta,Dg,Dr) (lines 590-590)
- If(Dp(1)-Dp(2))63,63,64 (lines 591-591)
- 64 Dp(2)=Dp(1) (lines 592-592)
- Got066 (lines 593-593)
- 63 Dv=3.14159265*Dg *(Dp(1)*Dg -Dsin(De(5))) (lines 594-594)
- De(4)=De(1)*57.29577957 (lines 595-595)
- De(8)=De(5)*57.29577957 (lines 596-596)
- Print 50,Dbeta,Dh (lines 597-597)
- 50 Format(1H2,6Hbeta=E15.7,6X,3Hh=E15.7//) (lines 598-598)
- 100 FORMAT(1HO,5X,3HPHI,8X,3HX/B,13X,3HZ/B,13X,3HR/A,13X,3HH/113X,4HV/A3) (lines 599-599)
- 200 Format(1H,Op1F9.3,1P5E16.7) (lines 600-600)
- Print100 (lines 601-601)
- Print200,De(8),De(6),De(7),Dg,Dp(1),Dv (lines 602-602)
- 201 CONTINUE (lines 603-603)
- Goto 11 (lines 604-605)
- C Solution For Given Values Of Beta And R/A=(G1) (lines 606-607)
- 400 Format(8F10.7) (lines 608-608)
- 401 CONTINUE (lines 609-609)
- Do 202 N4=1,N3 (lines 610-610)
- Read 400,Beta,(G1(I),I=1,8) (lines 611-611)
- Call Mainis(A,B,C,Z,E,H,J,P,Beta,G1,R) (lines 612-612)
- 202 CONTINUE (lines 613-613)
- Goto 11 (lines 614-615)
- C SOLUTION FOR GIVEN VALUES OF BETA AT INTERVALS (N1) OF PHI (lines 616-617)

## Entities

### Alloy-Material

- stainless steel 304 (mentions: 1)
- stainless steel 316 (mentions: 1)

### Organization

- AEC (mentions: 11)
- ORNL (mentions: 4)
- Union Carbide (mentions: 1)

### Reactor

- ARE (mentions: 28)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- title_fallback_used
