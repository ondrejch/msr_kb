# ORNL-TM-1933

## Metadata

- Doc ID: `ornl-tm-1933`
- Primary report number: ORNL-TM-1933
- All report numbers: ORNL-TM-1933
- Report series: ornl-technical-memorandum
- Date: August 30, 1967
- Authors: SOLVING ORDINARY DIFFERENTIAL EQUATIONS, S.J.Ball R.K.Adams, LEGAL NOTICE, Page
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-1933/ORNL-TM-1933/hybrid_ocr/ORNL-TM-1933.md`
- SHA256: `8f01568f29d75f3f8f3c890253bffd9f2cfd0034b1f263430c17ecf2e6e77e96`

## Topics

- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/program-history.md|program-history]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/reactor-physics-neutronics.md|reactor-physics-neutronics]]
- [[../topics/salt-chemistry-and-redox.md|salt-chemistry-and-redox]]

## Summary

- "MATEXP," A GENERAL PURPOSE DIGITAL COMPUTER PROGRAM FOR
- The method has been extended to nonlinear equations and equations with time-varying coefficients; this use is very effective for engineering systems analysis problems.
- This report was prepared as an account of Government sponsored work. Neither the United States, nor the Commission, nor any person acting on behalf of the Commission:
- B. Assumes any liabilities with respect to the use of, or for damages resulting from the use of any information, apparatus, method, or process disclosed in this report.
- MATEXP has also been used in a special technique to calculate the sensitivities of the time response of a system to changes in parameter values. $^{15}$ A description of a subroutine which was written to implement time response sensitivity calculations is given in Sect. 5.2.3.
- An interesting characteristic of the solution is that, for any time interval $\tau$ , the value of $x$ at the end of the interval is a product of an exponential term $\epsilon^{-a\tau}$ and the value of $x$ at the beginning of the interval, i.e.

## Sections

- Ornl-Tm-1933 (lines 1-2)
- Copy No.133 (lines 3-6)
- "Matexp," A General Purpose Digital Computer Program For (lines 7-8)
- Solving Ordinary Differential Equations (lines 9-10)
- By The Matrix Exponential Method (lines 11-14)
- ABSTRACT (lines 15-20)
- LEGAL NOTICE (lines 21-29)
- CONTENTS (lines 30-55)
- 1. INTRODUCTION (lines 56-84)
- 2. DEVELOPMENT OF THE MATRIX EXPONENTIAL METHOD (lines 85-86)
- 2.1 For Homogeneous Equations (lines 87-176)
- 2.2 For Nonhomogeneous Equations (lines 177-238)
- 2.3 Miscellaneous Features of the Matrix Exponential (lines 239-290)
- 3. DESCRIPTION OF MATEXP PROGRAM AND OPTIONS (lines 291-292)
- 3.1 Basic Input Information (lines 293-322)
- 3.2 Alternative Methods of Generating the Coefficient Matrix A (lines 323-342)
- 3.3 Alternative Methods of Generating the Forcing Function Vector Z (lines 343-416)
- 3.4 Methods for Solving Time-Varying-Parameter and Nonlinear Differential Equations (lines 417-464)
- 3.5 Special Forcing Function Subroutines (lines 465-468)
- 3.5.1 Arbitrary Function Generation - DFG (lines 469-479)
- 3.5.2 Variable Transport Lag Generation - TRLG (lines 480-547)
- 4. SUMMARY AND CONCLUSIONS (lines 548-559)
- 5. APPENDIX (lines 560-561)
- 5.1 Problems in the Evaluation of Exponential Functions (lines 562-596)
- 5.2 Detailed Description of Programs (lines 597-600)
- 5.2.1 MATEXP Main Program (lines 601-685)
- Ornl Dwg. 67-10217 (lines 686-690)
- Ornl Dwg. 67-10218 (lines 691-698)
- MATEXP MAIN PROGRAM SYMBOL KEY (lines 699-780)
- 5.2.2 Subroutine OUTPUT (lines 781-784)
- 5.2.3 Subroutine DISTRB (lines 785-818)
- 5.2.4 Subroutine VARCO (lines 819-822)
- 5.2.5 Subroutine DFG (lines 823-854)
- 5.2.6 Subroutine TRLG (lines 855-880)
- 5.3 FORTRAN LISTING OF PROGRAMS (lines 881-882)
- $Ibftc Main Deck (lines 883-884)
- Program Matexp For The 7090 - Fortran 4 (lines 885-886)
- This Program Calculates The Solution Of A Matrix Of First (lines 887-890)
- Of The Form Dx/Dt # Ax + Z. (lines 891-892)
- The Method Is Paynter-S Matrix Exponential Method (lines 893-894)
- The Solution Is Given For Increments Of The Independent (lines 895-896)
- Variable (T) From Tzero Through Tmax (lines 897-898)
- Computes Matrices C # Exp(A*T) And (lines 899-900)
- Hp # (C-I) \*A Inverse (lines 901-902)
- Solution X(N*T) # C*X((N-1)*T)+Hp*Z((N-1)*T) (lines 903-904)
- Series Calculation Of C And Hp Monitored To (lines 905-906)
- Assure Specified Significance. (lines 907-908)
- If T Is Reduced For C And Hp Calcs. (lines 909-910)
- Original Arguments Are Restored By - (lines 911-912)
- C(2*T) #C(T)*C(T) (lines 913-914)
- Hp（2\*T）#Hp（T）+C（T）\*Hp（T） (lines 915-916)
- Output From The Program Is Printed At Intervals Pltinc. (lines 917-918)
- The Program Uses Subroutines Distrb And Output (lines 919-920)
- Input For The Program Consists Of (lines 921-922)
- One Control Card (lines 923-926)
- The Initial Condition Vector X (lines 927-928)
- A Fixed Disturbance Vector Z (lines 929-930)
- A Varying Z Can Be Generated By Distrb (lines 931-932)
- Variable Coefficient Equations May Be Solved By Appropriate (lines 933-934)
- Fudging Of The Disturbance Function Subroutine. (lines 935-936)
- Control Card Input Information (lines 937-938)
- Ne#No. Of Equations (I2) (lines 939-940)
- Ll#Coeff. Matrix Tag No. (I2) (lines 941-942)
- P#Precision Of C And Hp (Fio·O) - Recommend I·Oe-6 Or Less (lines 943-944)
- Tzero#Zero Time (Fio.0) (lines 945-946)
- T#Computation Time Interval (F10.0) (lines 947-948)
- Tmax#Maximum Time (Fio·O) (lines 949-950)
- Pltinc#Printing Time Interval (Fio·0) (lines 951-952)
- Matyescoeff.Matrix（A）Controlflag（I2） (lines 953-954)
- I#Use Previous A And T (lines 955-956)
- 2Read New Coeff.S To Alter A (lines 957-958)
- 3#Read Entire New A (Non-Zero Values) (lines 959-960)
- 4#Distrb To Calc. Entire New A (lines 961-962)
- 5Read Some, Distrb To Calc. Others (lines 963-964)
- 6#Distrb To Alter Some A Elements (lines 965-966)
- Icss# Initial Condition Vector (Xic) Flag (I2) (lines 967-968)
- I#Read In All New Non-Zero Values (lines 969-970)
- 2#Read New Values To Alter Previous Vector (lines 971-972)
- 3#Use Previous Vector (lines 973-974)
- 4#Vector#0 (lines 975-979)
- 5#Use Last Value Of X Vector From Previous Run (lines 980-980)
- Jflag#Forcing Function (Z) Flag (I2) (lines 981-981)
- I Thru 4#Same As For Icss For Constant Z (lines 982-982)
- 5#Call Distrb At Each Time Step For Variable Z (lines 983-983)
- Itmax # Max. No. Of Terms In Series Approx. (lines 984-984)
- Of Exp(At). (I3) (lines 985-985)
- Lastcc # Non-Zero For Last Case (Ii) (lines 986-986)
- Iiz # Row No. Of Z If Only One Non-Zero, (lines 987-987)
- Otherwise #0 (I2) (lines 988-988)
- Icontr - For Internal Control Options (I2) (lines 989-989)
- 0#Read New Control Card For Next Case (lines 990-990)
- 1#Go To 212 Call Distrb For New A Or T (lines 991-991)
- -1#Go To 215 Call Distrb For New I.C.-S (lines 992-992)
- Var # Max. Allowable Value Of Largest Coeff. Matrix Element * T (lines 993-993)
- (Recommend Var#1.D) (F6.D) (lines 994-997)
- Dimension A(60,60), C(60,60), Hp(60,60), Qpt(60,60), (lines 998-998)
- Ix(60), Y(60), Z(60), Xic(60), Tqp(60) (lines 999-999)
- Common C, Hp, A, Qpt, X, Z, Y, Itmax, Kk, Ll, Mm, (lines 1000-1000)
- Ijjflag, Xic, Ni, Time, Tmax, Tzero, Ne, Tqp, T, (lines 1001-1001)
- 2.Iiz, Icontr, Pltinc, Matyes, Icss, Jflag, Plt (lines 1002-1005)

## Entities

### Alloy-Material

- stainless steel 304 (mentions: 2)

### Organization

- ORNL (mentions: 7)

### Reactor

- ARE (mentions: 59)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- title_fallback_used
