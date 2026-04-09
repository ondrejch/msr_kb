# ![](images/39626a5c83c9969775281ab3c1d2e85fb42e70d83ed8638dcf22a0389139c57a.jpg)

## Metadata

- Doc ID: `ornl-mit-117`
- Primary report number: unknown
- All report numbers: none detected
- Report series: unknown
- Date: November 18, 1970
- Authors: OPERATED BY, UNION CARBIDE CORPORATION, POST OFFICE BOX X, COPY NO., AUTHOR: M.D. Shapiro, C.M. Reed, Consultant: R.B. Korsmeyer
- Document type: report
- Source markdown: `pdf/ORNL-MIT-117/ORNL-MIT-117/hybrid_ocr/ORNL-MIT-117.md`
- SHA256: `e1ab05308a5a8b33b3355c3932b98df6fa168044438767e5cdf6f31081e6c592`

## Topics

- [[../topics/off-gas-fission-products-and-tritium.md|off-gas-fission-products-and-tritium]]
- [[../topics/reactor-physics-neutronics.md|reactor-physics-neutronics]]
- [[../topics/fuel-processing-and-reprocessing.md|fuel-processing-and-reprocessing]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]
- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]
- [[../topics/instrumentation-and-controls.md|instrumentation-and-controls]]

## Summary

- Tritium is produced in the primary salt stream by neutron absorption. The reactions producing tritium and the estimated production for a 1000 Mw(e) reactor are listed in Table 1.
- only the final product is burned, and the remainder, more than $99\%$ of the $\mathsf{H}_2$ can be recycled.

## Sections

- OAK RIDGE NATIONAL LABORATORY (lines 3-4)
- Operated By (lines 5-6)
- Union Carbide Corporation (lines 7-8)
- Nuclear Division (lines 9-12)
- Post Office Box X (lines 13-14)
- Oak Ridge, Tennessee 37830 (lines 15-16)
- Ornl-Mit-117 (lines 17-20)
- Copy No. (lines 21-28)
- ABSTRACT (lines 29-34)
- NOTICE (lines 35-46)
- Contents (lines 47-48)
- Page (lines 49-73)
- 1. SUMMARY (lines 74-79)
- 2. INTRODUCTION (lines 80-92)
- School Of Chemical Engineering Practice (lines 93-106)
- 3. DESIGN AND EVALUATION OF ALTERNATE SEPARATION SYSTEMS (lines 107-108)
- 3.1 Approach (lines 109-114)
- 3.2 Feed Pretreatment (lines 115-122)
- 3.3 Storage of Tritiated Water (lines 123-126)
- 3.4 Water Distillation (lines 127-136)
- 3.5 Thermal Diffusion (lines 137-142)
- 3.6 Cryogenic Distillation (lines 143-151)
- School Of Chemical Engineering Practice (lines 152-179)
- 4. DISCUSSION OF SEPARATION SYSTEMS (lines 180-187)
- 5. CONCLUSIONS AND RECOMMENDATIONS (lines 188-193)
- 6. ACKNOWLEDGEMENT (lines 194-197)
- 7. APPENDIX (lines 198-199)
- 7.1 Basis for Water Distillation Costs (lines 200-226)
- 7.2 Thermal Diffusion System (lines 227-252)
- 7.3 Cryogenic Distillation System (lines 253-254)
- 7.3.1 Design of Cryogenic Distillation Column (lines 255-270)
- 7.3.2 Basis for $\mathsf{H}_2$ Distillation Costs (lines 271-383)
- 7.4 Computer Codes (lines 384-387)
- $Xf = .999998$ (lines 388-389)
- 55 Accept $K= $,K; If(K),57.; Accept Kk;If(Kk),58, (lines 390-391)
- Accept $Prt = $,Prt,$Np = $,Np,$Delp = $,Delp (lines 392-393)
- 58 Accept $Rec = $,Rec,$Wot = $,Wot,$R = $,R (lines 394-397)
- Dwat=99.9998-Bwat;Xd=Dwat/D;Rløv=R/(R+1.);Sløv=(R+100./D)/(R+1.) (lines 398-401)
- 60 Fformat(15,F15.10,F9.5) (lines 402-403)
- N=1;J=1;Jj=1;Y=Xd;Pr=Prt;A1=Rlv;A2=Dxd (lines 404-406)
- 20 CALL ALPHA(PR,A) (lines 407-407)
- X=Y/(A-(A-1).)*Y);If(J-Jj*K)24,22,22 (lines 408-408)
- 24 If(N),29.;If(X-Xf)30,30,25 (lines 409-409)
- 29 IF(X-XB)40, (lines 410-410)
- 25 Y=A1*A2;J=J+1;If(J-Np)26,27,27 (lines 411-411)
- 26 Pr=Pr+Delp;G∅ T∅ 20 (lines 412-412)
- 27 Display $Stages=$,J,$X=$,X;J=1;Pr=Prt;Jj=1;G∅ T∅ 20 (lines 413-413)
- 22 Jj=Jj+1;Write(1,60)J,X,A;G∅ T∅ 24 (lines 414-415)
- 40 Write(1,60)J,X;G∅ T∅ 55 (lines 416-416)
- 57 St∅P (lines 417-418)
- S'E Alpha(Pr,A) (lines 419-419)
- D'N Al(9),P(9) (lines 420-420)
- Data Al/1.0775,1.0735,1.07,1.067,1.062,1.056,1.0512,1.0478,1.044/ (lines 421-421)
- Data P/50.,60.,70.,80.,100.,130.,160.,200.,250./D∅ 8 J=1,10 (lines 422-422)
- If(P(J)-Pr) 8,9,10 (lines 423-423)
- 8 CONTINUE (lines 424-424)
- 9 A=Al(J); G∅ T∅ 15 (lines 425-425)
- 10 A=Al(J-1)+(Al(J)-Al(J-1))*(Pr-P(J-1))/(P(J)-P(J-1)) (lines 426-426)
- 15 RETURN (lines 427-453)
- Dxd D·Xd/V (lines 454-455)
- Bxb B·Xb/V (lines 456-469)
- $Xf = .999998$ $A = 1.6$ (lines 470-471)
- 55 Accept $K = $, K; If(K), 57, (lines 472-473)
- Accept $Rec=$,$Rec,$Wot=$,$Wot,$R=$,$R,$Q=$,$Q (lines 474-475)
- Bht0=Rec\*O.0002;Bwat=Bht0\*W0T;B=Bht0+Bwat;Xb=Bwat/B;D=100.-B (lines 476-477)
- Dwat=99.9998-Bwat;Xd=Dwat/D;Rløv=R/(R+1.);Vl=D*(R+1.)-100.*(-Q) (lines 478-481)
- 60 Fqrmat(I5,F15.10) (lines 482-483)
- If(Q.Eq.1.0) G0 T0 70;Xin=(Xf/(Q-1.)+Xd/(R+1.))/((Q/(Q-1.)-R/(R+1.)) (lines 484-485)
- Display $Xin = $, Xin; G0 T0 69 (lines 486-487)
- 70 Xin=Xf (lines 488-493)
- 24 If(N),29,;If(X-Xin)30,30,25 (lines 494-495)
- 29 IF(X-XB)40, (lines 496-497)
- 25 $Y = A1^{*}X + A2;J = J + 1;G0T0$ 20 (lines 498-499)
- 22Jj=Jj+1;Write(1,60)J,X;G0T0 24 (lines 500-501)
- 30 N=0;A1=Sl0V;A2=-Bxb;G0 T0 25 (lines 502-503)
- 40Write(1,60)J,X;G0T055 (lines 504-505)
- 57 STOP (lines 506-517)
- 7.5 Nomenclature (lines 518-565)
- Subscripts (lines 566-569)
- 7.6 Literature References (lines 570-599)
- Ornl-Mit-117 (lines 600-601)
- Internal (lines 602-627)
- External (lines 628-632)

## Entities

### Alloy-Material

- stainless steel 304 (mentions: 3)
- beryllium (mentions: 1)

### Component

- heat exchanger (mentions: 5)

### Organization

- ORNL (mentions: 15)
- AEC (mentions: 2)
- Union Carbide (mentions: 2)

### Reactor

- MSBR (mentions: 17)
- ARE (mentions: 11)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- report_number_not_detected
- report_series_not_detected
