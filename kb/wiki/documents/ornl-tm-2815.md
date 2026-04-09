# ![](images/bb8ca45e0e1b46aaebb681679979113b8c0c3ecd470ce0ca9696c201e289a854.jpg)

## Metadata

- Doc ID: `ornl-tm-2815`
- Primary report number: ORNL-TM-2815
- All report numbers: ORNL-TM-2815, ORNL-4541
- Report series: ornl-technical-memorandum
- Date: June 24, 1971
- Authors: C. E. Bettis, T. W. Pickel, W. K. Crowley, M. Simon-Tov, H. A. Nelms, W.C.Stoddart
- Document type: technical-memorandum
- Source markdown: `pdf/ORNL-TM-2815/ORNL-TM-2815/hybrid_ocr/ORNL-TM-2815.md`
- SHA256: `7f41fea2712109106c1cd02d6c3cbf80e1102eed1dac26f317760987dbfddb85`

## Topics

- [[../topics/pumps-loops-and-heat-exchangers.md|pumps-loops-and-heat-exchangers]]
- [[../topics/salt-systems-and-thermophysics.md|salt-systems-and-thermophysics]]
- [[../topics/materials-and-corrosion.md|materials-and-corrosion]]
- [[../topics/breeder-and-converter-design.md|breeder-and-converter-design]]
- [[../topics/aircraft-nuclear-propulsion.md|aircraft-nuclear-propulsion]]
- [[../topics/reactor-operations.md|reactor-operations]]
- [[../topics/salt-chemistry-and-redox.md|salt-chemistry-and-redox]]
- [[../topics/reactor-physics-neutronics.md|reactor-physics-neutronics]]

## Summary

- Report No.: ORNL-TM-2815 Classification: Unclassified
- Please correct your copies promptly to avoid further errors. The corrected design data for the primary heat exchanger agree with the data shown in Report No. ORNL-4541.
- wave configuration. The tubes are held in place by wire lacing in this upper portion of the tube bundle. Since baffling is not employed in this region, the bent-tube portion of the bundle experiences essentially parallel flow and a relatively lower heat transfer performance.

## Sections

- OAK RIDGE NATIONAL LABORATORY (lines 3-6)
- Union Carbide Corporation • Nuclear Division (lines 7-10)
- U.S. Atomic Energy Commission (lines 11-12)
- Ornl-Tm-2815 (lines 13-16)
- COMPUTER PROGRAMS FOR MSBR HEAT EXCHANGERS (lines 17-32)
- OAK RIDGE NATIONAL LABORATORY (lines 33-34)
- Operated By (lines 35-36)
- Union Carbide Corporation (lines 37-38)
- Nuclear Division (lines 39-42)
- Post Office Box X (lines 43-44)
- Oak Ridge, Tennessee 37830 (lines 45-81)
- 1047 Format(31Hoberglin Modification Factor = ,F5.2) Msbr 500 (lines 82-85)
- 1051 Format(27Hotube Wall Average Temp. = ,F10.2) Msbr 540 (lines 86-86)
- 1052 Format(28Hoshell Side Average Temp. = ,F10.2) Msbr 550 (lines 87-90)
- Read In And Print Out Input Data Msbr 650 (lines 91-91)
- Key7= 1 Msbr 660 (lines 92-92)
- Vm1(1)=0. Msbr 670 (lines 93-93)
- Vm2(1)=0. Msbr 680 (lines 94-94)
- Vm3(1)=0. Msbr 690 (lines 95-95)
- Vwo1(1)=0. Msbr 660 (lines 96-96)
- Vwo3(1)=0. Msbr 670 (lines 97-97)
- Renso1(1)=0. Msbr 680 (lines 98-98)
- Renso2(1)=0. Msbr 690 (lines 99-99)
- Renso3(1)=0. Msbr 700 (lines 100-100)
- Hso1(1)=0. Msbr 710 (lines 101-101)
- Hso2(1)=0. Msbr 720 (lines 102-107)
- Msb 2230 (lines 108-108)
- Msb 2240 (lines 109-109)
- Msb 2250 (lines 110-110)
- Msb 2260 (lines 111-111)
- Msb 2270 (lines 112-112)
- Msb 2280 (lines 113-113)
- Msb 2290 (lines 114-114)
- Msb 2300 (lines 115-115)
- Msb 2310 (lines 116-116)
- Msb 2320 (lines 117-117)
- Msb 2330 (lines 118-118)
- Msb 2340 (lines 119-119)
- Msb 2350 (lines 120-120)
- Msb 2360 (lines 121-123)
- C CALCULATE REYNOLS AND PRANDTL NUMBER TUBE SIDE MSB 2550 (lines 124-124)
- Rento(I) = Ciai*Gto/Fvis Msb 2380 (lines 125-125)
- Prnto(I) = Fvis*Fsph/Fccn Msb 2390 (lines 126-126)
- If(Kentb.Eq.1.And.Rentc(I).Gt.1001. And.I.Ne.1) Msb 2400 (lines 127-127)
- Hefi=1.+(Rento(I)-1000.)/9000.)**0.5 Msb 2401 (lines 128-128)
- Pdto(I)=(.0C28+.25*Rento**(-.32))*Eqvbso*Gto**2*Hefi/ Msb 2410 (lines 129-129)
- 1 (Diai*Fden*4171824Co.) Msb 2411 (lines 130-137)
- 12 If(Rento(I).Lt.21Cc.) Go To 14 Msb 2450 (lines 138-141)
- 13 Hto(I) = Fcon/Dia*.C89*(Rento(I)**.67895-141.1372)*(Prnto(I) (lines 142-142)
- 1**.3333)*Fvisk*Hef I*(1.+.3333*(Diai/Tubln(I))**.6666) (lines 143-143)
- Go To 15 Msb 2470 (lines 144-147)
- 14 Hto(I) = Fccn/Dia*(4.36+(0.025*Rento(I)*Prnto(I)*Diai/Tubln(I)) Msb 2480 (lines 148-148)
- 1)/(1. + C.0012*Rento(I)*Prnto(I)*Diai/Tubln(I))) Msb 2481 (lines 149-152)
- 15 If(I.Eq.1)Go To 16 Msb 2490 (lines 153-156)
- C CALCULATE FLOW AREAS SHELL SIDE MSB 2480 (lines 157-157)
- Vw01(I) = Qccden/Aw01 Msb 2510 (lines 158-158)
- Vw03(I) = Qccden/Aw03 Msb 2520 (lines 159-159)
- Vm1(I) = Gso1*Ccden Msb 2530 (lines 160-160)
- Vm2(I) = Gso2*Ccden Msb 2540 (lines 161-161)
- Vm3(I) = Gsg3*Ccden Msb 2550 (lines 162-164)
- Total Heat Transfered = 1898217984. (Btu/Hr) (99.9 Percent) (lines 165-166)
- Mass Flow Rate Of Coolant = 17590736. (Lb/Hr) (lines 167-168)
- Mass Flow Rate Of Fuel = 2345432C. (Lb/Hr) (lines 169-170)
- Shell-Side Total Pressure Crcp = 115.75 (Lb/Sqin) (99.7 Percent) (lines 171-172)
- Tube-Side Total Pressure Drop = 129.32 (Lb/Sqin) (99.5 Percent) (lines 173-174)
- Nominal Shell Radius = 2.81€2 (Ft) (lines 175-176)
- Uniform Baffle Spacing = C.9386 (Ft) (lines 177-178)
- Tube Fluid Volume Contained In Tubes = 71.92 (Cubic Feet) (lines 179-180)
- Total Heat Transfer Area Based On Tube O.D. = 13916.32 (Sqft) (lines 181-182)
- Total Number Of Tubes = 5803. (lines 183-184)
- Total Tube Length = 24.43 (Ft) (lines 185-186)
- Heat Exch. Approx. Length = 23.22 (Feet) (lines 187-188)
- Straight Section Of Tube Length = 20.26 (Ft) (lines 189-190)
- Radius Of Thermal Expansion Curves = 0.86 (Feet) (lines 191-192)
- Berglin Modification Factor = 0.79 (lines 193-194)
- Tube Wall Average Temp. = 1116.54 (lines 195-196)
- Shell Side Average Temp. = 1013.66 (lines 197-198)
- P Stress At Tube Od And Tube Id = 683.42 646.47 (Lb/Sqin) (lines 199-200)
- Should Not Exceed 4232.23 (lines 201-202)
- P+Q Stress At Tube Od And Tube Id = 12484.39 8890.97 (Lb/Sqin) (lines 203-204)
- Should Not Exceed 12696.7C (lines 205-206)
- P+Q+F Stress At Tube Od And Tube Id = 13562.77 10981.55 (Lb/Sqin) (lines 207-208)
- Should Not Exceed 25000.Co (lines 209-221)
- 20 Hjw=0.571/(Recw**0.456) Sup 1350 Goto22 Sup 1369 (lines 222-224)
- 22 Hw=(Hjw*Cph*Gs/Con1)*Fact Sup*1380 (lines 225-225)
- Ho=(Hb*(1.0-2.0*Pw)+Hw*(2.0*Pw))*Blfh Sup 1390 (lines 226-226)
- Ho = Ho*Gbrl Sup 1400 (lines 227-227)
- Ro(K) = 1.0/Ho Sup 1410 (lines 228-229)
- 24 Pc(I+1)=Pc(I)+Delpp Sup 1460 (lines 230-230)
- Lop3=0 Sup 1470 (lines 231-231)
- Lop4=0 Sup 1480 (lines 232-232)
- Tc(I+1)=Tc(I)-Dech Sup 149C (lines 233-236)
- 28 Tnext=Tc(I+1)+(Hc(I+1)-Hcg)*(Tc(I+1)-Trial)/(Hcg-Hrial) Sup 1590 (lines 237-237)
- Trial=Tc(I+1) Sup 1600 (lines 238-238)
- Hrial=Hcg Sup 1610 (lines 239-239)
- Tc(I+1)=Tnext Sup 1620 (lines 240-240)
- Lop3=Lop3+1 Sup 1630 (lines 241-241)
- If(Lop3-1C)30,30,29 Sup 1640 (lines 242-242)
- 29 WRITEOUTPUTTAPE51,1015,LCP3 SUP 1650 GOTO80 SUP 1660 (lines 243-243)
- 30 GOTO27 SUP 1670 (lines 244-244)

## Entities

### Alloy-Material

- Hastelloy N (mentions: 11)
- molybdenum (mentions: 2)
- nickel (mentions: 2)
- niobium (mentions: 1)
- titanium (mentions: 1)

### Component

- heat exchanger (mentions: 60)
- steam generator (mentions: 29)
- loop (mentions: 6)
- pump (mentions: 2)

### Organization

- ORNL (mentions: 18)
- AEC (mentions: 15)
- Union Carbide (mentions: 3)
- ANL (mentions: 1)

### Reactor

- MSBR (mentions: 157)
- ARE (mentions: 78)

### Report-Series

- Nuclear Science and Engineering (mentions: 1)

### Salt-System

- NaBF4-NaF (mentions: 3)
- LiF (mentions: 2)
- fluoride salt (mentions: 2)
- BeF2 (mentions: 1)
- NaF (mentions: 1)
- ThF4 (mentions: 1)
- UF4 (mentions: 1)


## Assets

- Figures: 0
- Tables: 0

## Warnings

- none
