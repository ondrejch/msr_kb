# ![](images/855cc2ed184a91567893984f89ebdf95982fc65ad652fa8117011581a93d6c44.jpg)

## Metadata

- Doc ID: `ornl-tm-4079`
- Primary report number: unknown
- All report numbers: none detected
- Report series: ornl-technical-memorandum
- Date: 1973
- Authors: FORCED-CONVECTION, HEAT-TRANSFER MEASUREMENTS WITH, J. W. Cooke, B. Cox
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-4079/ORNL-TM-4079/hybrid_ocr/ORNL-TM-4079.md`
- SHA256: `ab17fbdb6ba83d4052a1be6d5372abf01e2ca7b873dcf1f80a5f657c52035ff3`

## Topics

- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/instrumentation-and-controls.md|instrumentation-and-controls]]
- [[../topics/reactor-physics-neutronics.md|reactor-physics-neutronics]]
- [[../topics/materials-and-corrosion.md|materials-and-corrosion]]
- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]

## Summary

- Heat-transfer coefficients were determined experimentally for a proposed MSBR fuel salt (LiF-BeF $_2$ -ThF $_4$ -UF $_4$ ;67.5-20.0-12.0-0.5 mole %) flowing by forced convection through a 0.18-in.-ID horizontal, circular tube for the following range of variables:
- Within these ranges, the heat-transfer coefficient was found to vary from 320 up to 6900 Btu/hr·ft²·°F (Nusselt modulus of 6.5 to 138). Correlations of the experimental data resulted in the equations:
- Details of a salt reservoir can be seen in Fig. A-3. The interior of these tanks as well as the test section and the mixing chambers are stress relieved and hydrogen fired before they are assembled.
- The local coefficient of forced-convective heat transfer is defined by the equation
- The inside tube wall temperature is related to the measured outside tube wall temperature by the equation
- For most of the measurements, the heat gained by the fluid intraversing the test section was calculated by the equation

## Sections

- FORCED-CONVECTION (lines 5-6)
- HEAT-TRANSFER MEASUREMENTS WITH (lines 7-8)
- A MOLTEN FLUORIDE SALT MIXTURE (lines 9-10)
- FLOWING IN A SMOOTH TUBE (lines 11-19)
- OAK RIDGE NATIONAL LABORATORY (lines 20-21)
- Operated By Union Carbide Corporation • For The U.S. Atomic Energy Commission (lines 22-35)
- Notice (lines 36-39)
- March 1973 (lines 40-41)
- Oak Ridge National Laboratory (lines 42-47)
- Union Carbide Corporation (lines 48-51)
- U. S. Atomic Energy Commission (lines 52-55)
- CONTENTS (lines 56-75)
- FORCED-CONVECTION HEAT-TRANSFER MEASUREMENTS WITH A MOLTEN FLUORIDE SALT MIXTURE FLOWING IN A SMOOTH TUBE (lines 76-81)
- ABSTRACT (lines 82-115)
- INTRODUCTION (lines 116-121)
- DESCRIPTION OF THE APPARATUS (lines 122-158)
- OPERATING PROCEDURES (lines 159-189)
- CALCULATIONS (lines 190-247)
- RESULTS (lines 248-352)
- DISCUSSION (lines 353-367)
- CONCLUSIONS (lines 368-373)
- ACKNOWLEDGMENTS (lines 374-377)
- REFERENCES (lines 378-394)
- Appendix A (lines 395-396)
- Additional Details Of The Experimental System (lines 397-400)
- Ornl-Dwg 72-11522 (lines 401-419)
- Pertinent Experimental Equipment (lines 420-423)
- Appendix B (lines 424-425)
- Experimental Data (lines 426-444)
- Appendix C (lines 445-446)
- Computer Program (lines 447-452)
- C I AM A WOLTEM SALT HEAT TRANSFER PROGRAM 5 (lines 453-454)
- Isn 0002 Real L,Mdot,K1,K2,K3,K4,Nunc,Mu,Njavg,Nnc,Kinow 10 (lines 455-456)
- Isn 0603 Dimension To(30),Xl(30),Ti(30),Tb(30),H(30),In(200),Du(200),D(200) 12 (lines 457-458)
- Isn 0004 Dimension Nuno(3G) 13 (lines 459-460)
- Isnocos Integer Ftc,Ctc 15 (lines 461-462)
- Isn 006 6010J=1,13 30 (lines 463-464)
- Isnocg7 $[L = 5*(J - 1)] + 1$ (lines 465-468)
- Isn 0009 Read7,In(1),Du(1),I=Il,Iu) 60 (lines 469-470)
- 1Sn Co10 7 Format(5([3,F5,2,2X)) 70 (lines 471-472)
- Isn 0011 10 Continue 75 (lines 473-474)
- Isn 0012 0.1 20.1=1,10 76 (lines 475-476)
- Isn 0013 [1=Nn(1)+1 77 (lines 477-478)
- Isn 0C14 [F(Ou(I).Ge.O.2)] D(Ii)=Du(Ii) 77A1 (lines 479-480)
- Isn Co16 20 Continue 77A2 (lines 481-482)
- Isn Ocl7 If (D(45).Lt.900.) Gc To 21 778 (lines 483-486)
- Isn 0C20 210(46)=-D(46) 770 (lines 487-488)
- Isn Oc21 22 Continue 77E (lines 489-490)
- Isn.0022 D301=1,50 78A (lines 491-492)
- Isnoc23 0U(1)=O(1) 768 (lines 493-494)
- Isn 0024 3U Continue 78C (lines 495-496)
- Ctemp Fitfollofsfor150Frefjunctionufto1900Degreesf 79 (lines 497-498)
- Isn.0025 074201=1,46 79A (lines 499-500)
- Isn 0026 If (D(1).Lt.1.59) Gc To 400 798 (lines 501-502)
- Isn 0028 If $\{D(1),Ge,1,99,And,D(1),Lt,5,30\}$ Go To 401 79C (lines 503-504)
- Isn 0C30 If (D(I).Ge.5.01.And.D(I).Lt.10.C1) Go To 402 790 (lines 505-506)
- Isn Cc32 If (D(I).Ge.10.01.And.D(Ii).Lt.13.01) Go To 403 79E (lines 507-508)
- Isn G034 If (D(I).Ge.13.01.And.C(I).Lt.17.01) Go To 404 79F (lines 509-510)
- Isn 0036 If (D(I).Ge.17.01.And.D(I).Lt.22.99) Go To 405 79G (lines 511-514)
- Isn 0040 If (D(I).Ge.29.99.And.O(Ii).Lt.33.Co) Go To 407 791 (lines 515-516)
- Isn C042 [F (D(I).Ge.33.0.And.D(I).Lt.35.0) Go To 4C8 79J (lines 517-518)
- Isn 0C44 If{D(I).Ge.36.0.And.D(I).Lt.39.0) Go To 409 79K (lines 519-520)
- Isn 6046 If (D(I).Ge.39.0) Gc To 410 79L (lines 521-522)
- Isn 0048 40C D(1)=150+(236-150)/1.99*(D(I)-0.) 79L1 (lines 523-524)
- Isn 0649 Go To 420 79M (lines 525-526)
- Isn C050 4(1) D(1)=236.+（371.-236.)/(5.01-1.99)*(D(1)-1.99) 79N (lines 527-528)
- Isn 0051 If (D(1).Ge.258..And.D(1).Le.290.) D(1)=D(1)-0.6 79N1 (lines 529-530)
- Isn 0053 If (D(1).Ge.280..And.D(1).Le.314.) D(1)=D(1)-0.5 79N2 (lines 531-532)
- Isn 0055 Go To 420 790 (lines 533-534)
- Isn.2C56 402 D(1)=372.+（592.-371./(10.01-5.01)*(C(1)-5.01) 79P (lines 535-536)
- Isn 0057 If (D(1).Ge.532.00) D(1)=D(1)-3.80 79P1 (lines 537-540)
- Isn 0C60 If (D(I).Le.425.) C(1)=D(1)-0.20 79P3 (lines 541-542)
- Isn 0062 Go To 420 790 (lines 543-544)
- Isn G063 403 D(1)=592.+(721.-592.)/(13.01-10.)1)*(C(1)-1C.01) 79R (lines 545-546)
- Isn 0064 Go To 420 795 (lines 547-548)
- Isnoc65 404 D(1)=72.+(891-721)/(17.01-13.01)*(D(1)-13.01) 79T (lines 549-550)
- Isn 0066 Gto420 79U (lines 551-552)
- Isn 0067 4C5 D(1)=891.+(1143.-891.)/(22.99-17.01)*(C(1)-17.01) 79V (lines 553-554)
- Isn 0C68 Go To 420 79W (lines 555-562)
- Isn 0C74 Go To 42C 79Y (lines 563-564)
- Isn 0075 407 D(1)=1444.+(1576.-1444.)/(33.00-29.99)*(D(1)-29.99) 792 (lines 565-574)
- Adcons For External References (lines 575-580)
- Isn 0002 Function Avg(Y,M,I,X1,X2) A20 (lines 581-582)
- Isn 0003 Dimension Y(50),X(50),A(4),P(50,4),Sp2(50,4) A30 (lines 583-584)
- Isn 0004 Real Np,Ls A35 (lines 585-586)
- Isn0005 A(1)=0 A40 (lines 587-588)
- Isn 0006 A(2) = 0 A50 (lines 589-590)
- Isnoc07 A(3)=0 A60 (lines 591-592)
- Isn 0008 A(4)=0 (lines 593-596)
- Isn 0010 P(1,2)=1. A73 (lines 597-598)
- Isn 0011 P(1,3)=1. A74 (lines 599-600)
- Isn 0012 P(1,4)=1. A75 (lines 601-602)
- Isn 0013 Np=1-1 A90 (lines 603-604)
- Isn 0014 Do 490 L=2,1 A95 (lines 605-606)
- Isn 0015 X(L)=L-1 A97 (lines 607-608)
- Isnoc16 P(L,1)=1. A100 (lines 609-610)
- Isn C017 P(L,2)=1,-2.*X(L)/Np A11C (lines 611-618)
- Isn 0020 490 Continue A135 (lines 619-628)
- 150025 07550J=1,4 A200 (lines 629-630)
- 1Sn 0026 00500K=1,1 A210 (lines 631-634)

## Entities

### Alloy-Material

- Hastelloy N (mentions: 4)
- stainless steel 304 (mentions: 1)

### Component

- heat exchanger (mentions: 1)

### Organization

- AEC (mentions: 20)
- ORNL (mentions: 12)
- General Electric (mentions: 2)
- Union Carbide (mentions: 2)

### Reactor

- ARE (mentions: 23)
- MSBR (mentions: 2)
- MSRE (mentions: 1)

### Salt-System

- LiF (mentions: 7)
- fluoride salt (mentions: 6)
- BeF2 (mentions: 2)
- FLiBe (mentions: 2)
- LiF-BeF2-ThF4-UF4 (mentions: 2)
- ThF4 (mentions: 2)
- UF4 (mentions: 2)
- KF (mentions: 1)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- report_number_not_detected
