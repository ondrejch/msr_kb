ORNL-TM-729, Part II A

Contract No. W-7405-eng-26

Instrumentation and Controls Division

MSRE DESIGN AND OPERATIONS REPORT

Part IIA. Nuclear and Process Instrumentation

J. R. Tallackson

LEGAL NOTICE

This report was prepared as an account of Government sponsored work. Neither nor the Commission: A. Makes any warranty or representation, expressed or implied, with respect to the accus States, nor the Commission, nor any person acting on behalf of the Commission: racy, completeness, or usefulness of the information contained in this report, or that the use of any information, apparatus, method, or process disclosed in this report may not infringe privately owned rights; or B. Assumes any liabilities with respect to the use of, or for damages resulting from the use of any information, apparatus, method, or process disclosed in this report. As used in the above, "person acting on behalf of the Commission" includes any emuse of any information, apparatus, method, or process disclosed in this report. As used in the above, "person acting on behalf of the Commission," includes any emuse of any information, apparatus, method, or process disclosed in this report.

FEBRUARY 1968

OAK RIDGE NATIONAL LABORATORY

Oak Ridge, Tennessee

operated by

UNION CARBIDE CORPORATION

for the

U.S. ATOMIC ENERGY COMMISSION

![](images/072fb1d32afd5288d83015d93abe5fbd4ab4a373d1d2ee55b949e1fcd57f91d8.jpg)

# CONTENTS

ACKNOWLEDGMENT. ix

1. MSRE INSTRUMENTATION AND CONTROL SYSTEM - GENERAL. 1

1.1 Introductory Remarks.. 1   
1.2 Design Considerations. 17

1.2.1 Introduction. 17   
1.2.2 Operational Requirements.. 17

1.2.2.1 Compatibility with Centralized Control Philosophy 17   
1.2.2.2 Ease of Operation.. 19   
1.2.2.3 Flexibility 20   
1.2.2.4 Experimental Data.. 20   
1.2.2.5 Remote Maintenance. 20   
1.2.2.6 Maintainability. 21

1.2.3 Safety Requirements.. 21

1.2.3.1 Containment 21   
1.2.3.2 Redundancy, Separation, and Identification 27   
1.2.3.3 Hazards to Operating Personnel.. 27

1.2.4 Performance Characteristics.. 27

1.2.4.1 Overall Accuracy.. 27   
1.2.4.2 Reliability. 27   
1.2.4.3 Failure Modes 28

1.2.5 Effects of Process Conditions 29

1.2.5.1 Operating Temperature 29   
1.2.5.2 Operating Pressure 29   
1.2.5.3 Corrosion 30  
1.2.5.4 Salt Plugging and Vapor Deposition.... 30   
1.2.5.5 Electrical Resistivity of Molten Salts. 31

1.2.6 Environmental Effects.. 32

1.2.6.1 Ambient Temperature 32   
1.2.6.2 Ambient Pressure 32   
1.2.6.3 Radiation Damage.. 33

1.2.7 Physical Requirements.. 35

1.2.7.1 Weld-Sealed Construction.. 35   
1.2.7.2 Ruggedness.. 35   
1.2.7.3 Size 35   
1.2.7.4 Materials of Construction.. 35   
1.2.7.5 Cleanliness.. 36

1.2.8 Cost 36

1.3 Plant Instrumentation Layout.. 37   
1.3.1 General Description 37   
1.3.2 Main Control Area.. 37

1.3.3 Auxiliary Control Area.. 37   
1.3.4 Transmitter Room.. 38   
1.3.5 Field Panels.. 38   
1.3.6 Interconnections 39   
1.3.7 Data Room. 39

1.4 Plant Control System 44   
1.5 Safety System. 55

1.5.1 Reactor Fill and Drain System. 67   
1.5.2 Helium Pressure Measurements in the Fuel Salt Loop 69   
1.5.3 Afterheat Removal System. 70

1.5.4 Containment System Instrumentation. 71

1.5.4.1 Helium Supply Block Valves. 72   
1.5.4.2 Off-Gas System Monitoring. 72   
1.5.4.3 In-Cell Liquid Waste and Instrument Air Block Valves. 76   
1.5.4.4 In-Cell Cooling Water Block Valves.... 76

1.5.5 Underpressure Protection for the Secondary Containment Cells. 77   
1.5.6 Fuel Salt Sampler-Enricher Containment Instrumentation. 77

2. SAFETY INSTRUMENTATION AND REACTOR CONTROL 97

2.1 Nuclear Instrumentation: Installation and Location.... 97   
2.2 BF3 Instrumentation. 106

2.2.1 General 106   
2.2.2 BF3 Counter 106   
2.2.3 High-Voltage Power Supply. 107   
2.2.4 Preamplifier, ORNL Model Q-1857 107   
2.2.5 Pulse Amplifier, ORNL Model Q-1875.... 107   
2.2.6Scaler,ORNL Model Q-1743. 108   
2.2.7 Logarithmic Count Rate Meter, ORNL Model Q-751... 108   
2.2.8 Confidence Trips. 108

2.3 Wide-Range Counting Channels 111

2.3.1 Principle of Operation.. 111   
2.3.2 Fission Chamber and Preamplifier Assembly.... 115

2.3.2.1 Introduction.. 116   
2.3.2.2 Preamplifier.. 116   
2.3.2.3 Flexible Cables. 118

2.3.2.4 Electrical Shielding Layout. 119   
2.3.2.5 Low Pickup-Noise Performance of the Assembly 119

2.3.3 Preamplifier Power Supply 120

2.3.3.1 General 120   
2.3.3.2 Construction. 120   
2.3.3.3 Application. 120   
2.3.3.4 Specifications. 120   
2.3.3.5 Circuit Description of the -22-v Supply. 121   
2.3.3.6 Circuit Description of the $+300\text{-}\mathbf{v}$ and +110-v Supply. 122

2.3.4 Pulse Amplifier 123

2.3.4.1 General 123   
2.3.4.2 Construction. 123   
2.3.4.3 Application. 123   
2.3.4.4 Specifications. 124   
2.3.4.5 Theory of Operation 125

2.3.5 0.l-hp Servo Amplifier, ORNL Model Q-2615.... 135

2.3.5.1 General 135   
2.3.5.2 Construction. 135   
2.3.5.3 Application. 135   
2.3.5.4 Specifications. 135   
2.3.5.5 Theory of Operation 136

2.3.6 Vernistat. 138

2.3.6.1 General 138   
2.3.6.2 Construction. 138   
2.3.6.3 Application. 139   
2.3.6.4 Specifications. 139   
2.3.6.5 Applicable Drawings. 139   
2.3.6.6 Theory of Operation 139

2.3.7 Dual DC Amplifier 140

2.3.7.1 General 140   
2.3.7.2 Specifications. 141   
2.3.7.3 Amplifier Balancing. 141   
2.3.7.4 Theory of Operation 141

2.3.8 Fission Chamber Drive. 146

2.3.8.1 Description. 146   
2.3.8.2 Drive Motor. 147   
2.3.8.3 LeadScrew. 147   
2.3.8.4 Position-Sensing Potentiometer. 147   
2.3.8.5 Synchro. 147   
2.3.8.6 Auxiliary Position-Sensing Potentiometer 148   
2.3.8.7 Vermistat Interpolating Potentiometer.. 148   
2.3.8.8 Gear Reducers 148   
2.3.8.9 Slip Clutch. 148   
2.3.8.10 Limit Switches. 148

2.4 Linear Power Channels. 163

2.4.1 Description. 163   
2.4.2 Visual Readout Device, Series 360. 164   
2.4.3 Keithley Model 418-20 Picoammeter: Specifications and Description. 164   
2.4.4 Procedure for Field Testing and Compensating  
Compensated Chamber Q-1045 165  
2.4.4.1 Description 165  
2.4.4.2 Testing 165   
2.4.5 The Use of a Colloidal Dispersion of Boron in Oil to Obtain a Uniform and Easily Applied Coating of Boron. 168   
2.4.6 High Current Saturation Characteristics of the ORNL Compensated Ionization Chamber (Q-1045). 168

2.5 Rod Scram Safety System. 177

2.5.1 Rod Scram Safety Channel - Input Instrumentation 177   
2.5.2 Rod Scram Safety Channel - Output Instrumentation. 178   
2.5.3 Safety Chambers. 180   
2.5.4 Period Safety Module, ORNL Model Q-2635 181  
2.5.4.1 Description 181  
2.5.4.2 Theory of Operation 183  
2.5.4.3 Operating Instructions 184   
2.5.5 Flux Amplifier and Ion Chamber High-Voltage Supply, ORNL Model Q-2602 185  
2.5.5.1 Description 185  
2.5.5.2 Theory of Operation 187  
2.5.5.3 Operating Instructions 189  
2.5.5.4 Maintenance Instructions 190   
2.5.6 MSRE Test Module, ORNL Model Q-2634 191  
2.5.6.1 Description 191  
2.5.6.2 Theory of Operation 192  
2.5.6.3 Operating Instructions 195   
2.5.7 Fast-Trip Comparator, ORNL Model Q-2609.... 196  
2.5.7.1 Description.... 196  
2.5.7.2 Theory of Operation.... 199  
2.5.7.3 Operating Instructions.... 201   
2.5.8 Coincidence Matrix Monitor, ORNL Model Q-2624.... 203  
2.5.8.1 Description.... 203  
2.5.8.2 Theory of Operation.... 204  
2.5.8.3 Operating Instructions.... 205

2.6 Shim and Regulating Rod Control System. 221

2.6.1 Introduction 221   
2.6.2 Rod Control Circuits 221   
2.6.3 The Automatic Rod Controller 228

2.6.3.1 Basic Rod Control Circuit. 228   
2.6.3.2 Temperature Control. 229   
2.6.3.3 Flux Demand Limiting 230

2.6.4 Regulating Rod Limit Switch Assembly, Q-2586... 231

2.6.4.1 Range Switching 234   
2.6.4.2 Range Seal. 235

2.6.5 Component Descriptions 236

2.6.5.1 Servo Motor.. 236   
2.6.5.2 Amplifier 236   
2.6.5.3 Clutch-Brake 237   
2.6.5.4 Shim-Locating Motor 237   
2.6.5.5 Mechanical Differential 237   
2.6.5.6 Size 15 Control Transformer.. 237   
2.6.5.7 Size 31 Torque Transmitter.. 238

2.6.6 Operational Situations Involving the Regulating

Rod Limit Switch and the Regulating Rod Servo... 238

2.7 Control Rods and Rod Drives 263

2.7.1 General Arrangement 263   
2.7.2 Position Indication 264   
2.7.3 Shock Absorber 265   
2.7.4 Cooling Air Flow and Temperature Monitoring.... 265   
2.7.5 Limit Switches 266   
2.7.6 Control Rods.. 267   
2.7.7 Rod Drop Timer 268   
2.7.8 Performance Characteristics.. 268

2.7.9 Component Descriptions and Specifications.... 269

2.7.9.1 Rod Drive Motor Assembly 269   
2.7.9.2 Electromechanical Clutch 269   
2.7.9.3 Overrunning Clutch 270   
2.7.9.4 Position-Indicating Synchros. 270   
2.7.9.5 Position-Indicating Potentiometer.... 271   
2.7.9.6 Limit Switches 271   
2.7.9.7 Electrical Wiring. 271   
2.7.9.8 Lubrication 271   
2.7.9.9 Thermostatic Switches 272   
2.7.9.10 Gears 272

2.8 Load Control System 301

2.8.1 Blower Operation.. 302   
2.8.2 Door Operation 302

2.8.3 Automatic Load Programming 304   
2.8.4 Manual Control 308   
2.8.5 Interlocks 308   
2.8.6 Load Scram. 308

# 2.9 Health Physics Monitoring.. 331

2.9.1 Introduction 331   
2.9.2 Facility Radiation and Contamination System.... 331

2.9.2.1 Introduction 331   
2.9.2.2 System Description.. 332   
2.9.2.3 Components 334

2.9.3 General System 339

2.9.3.1 Introduction 339   
2.9.3.2 Beta-Gamma Monitors, Q-2091.... 339   
2.9.3.3 Hand-and-Foot Beta-Gamma Monitor, Q-1939-B. 340   
2.9.3.4 Beta and Alpha Sample Counters... 341

# 2.10 Process Radiation Monitors 351

2.10.1 Introduction 351   
2.10.2 System Description 351

# 2.11 Stack Monitoring System 367

2.11.1 Introduction 367   
2.11.2 System Description 367

2.11.2.1 Flow Channel FT-S1 368   
2.11.2.2 In-Stack Sampler 368   
2.11.2.3 Particulate Monitors 368   
2.11.2.4 Iodine Monitor, RE-S1C.... 368

2.11.3 ORNL Drawing List for the MSRE Stack Monitoring

System. 372

# 2.12 Data Logger-Computer 379

2.12.1 Introduction 379   
2.12.2 Basic System Equipment Description 379   
2.12.3 Peripheral Equipment Description 381   
2.12.4 System Operation.. 382

2.12.4.1 Collection and Processing of Analog and Digital Input Signals 382   
2.12.4.2 Logging Functions 384   
2.12.4.3 Calculations 384   
2.12.4.4 Miscellaneous Functions 385

2.12.5 References and ORNL Drawings 386

# 2.13 MSRE Beryllium Monitoring System. 393

# ACKNOWLEDGMENT

This report represents the collective efforts of many more persons than the authors of record, who, in some areas, served as editors, not writers. We gratefully acknowledge the contributions of the following.1

H. R. Brashear for checking and final editing of the section on Process Radiation Monitoring.   
G. H. Burger² for preparing the sections on Process Radiation Monitoring, Health Physics Monitoring, Stack Monitoring, and the Data Logger-Computer.   
S. J. Ditto and E. N. Fray<sup>3</sup> for assistance in writing and checking large portions of the sections on the nuclear and electronic instrumentation.   
P. G. Herndon, C. E. Mathews, J. L. Redford, and R. W. Tucker for continuous and invaluable assistance in gathering information and in reviewing the drawings and text material.   
D. J. Knowles and J. A. Russell for help with reviews of the Health Physics and Stack Monitoring sections.   
R. H. Guymon, Chief of MSRE Operations, and his staff for giving generously of their time to review the sections on control and safety.   
M. Richardson for help with the section discussing the control rod and the drive unit.

![](images/d41b7012c196804969563f9ab94d8c1ce73d3041aa0ac14c4d75cf73e5f5f522.jpg)

# 1. MSRE INSTRUMENTATION AND CONTROL SYSTEM - GENERAL

# 1.1 INTRODUCTION REMARKS

Instrumentation is required by the MSRE to provide information and control for routine operations, to obtain experimental data, and to protect against hazard or damage to personnel or equipment resulting from abnormal conditions.

Both nuclear and nonnuclear instrumentation are used for measurement, for control, and for protection; however, because of the nature of the system, nonnuclear instrumentation predominates. Vital operational instrumentation on the MSRE is that which measures and controls levels, flows, and temperatures of molten salts, helium gas, cooling air, and water and which is required for operation and control of the auxiliary systems.

Two grades of instrumentation, control grade and safety grade, are found in the MSRE. Control-grade instrumentation is used where a failure of control or a loss of information or protective action (though undesirable) can be tolerated. Safety-grade instrumentation is used where such failures or losses cannot be accepted. The choice between the two systems is based on considerations of cost vs consequences. Safety-grade systems involve the use of redundant, reliable instruments and interconnections and tend to be much more expensive than control-grade systems. Hence safety-grade instruments are used only where necessary; control-grade instrumentation predominates.

The experimental nature of the reactor has increased the instrumentation requirements if compared to a power reactor. In some cases experimental data are obtained from instrumentation required for operation; however, in many cases, additional instrumentation was installed primarily for data. A second-generation, nonexperimental version of the MSRE will require less instrumentation.

The MSRE system, $^{1}$ the components comprising the system, and its nuclear and operating characteristics have been fully described previously. $^{2-5}$ It is not inappropriate to introduce a description of the

MSRE instrumentation and control system by repeating some of the essential features of the MSRE.

Figure 1.l.l is a pictorial drawing of the reactor installation, and Fig. 1.l.2 is a schematic drawing of the primary and secondary molten-salt loops in which nuclear power is generated and transferred. The primary (fuel) salt is a mixture of fluorides of lithium, beryllium, and zirconium with sufficient uranium fluoride to achieve criticality at the desired temperature. Several compositions of salt are under consideration for the MSRE, $^{2}$ differing principally in the concentration of $\mathrm{UF}_4$ as a consequence of the degree of enrichment in $^{235}\mathrm{U}$ . The use of $^{233}\mathrm{U}$ is also being studied. These variations or changes in composition are not expected to affect the design of the instrumentation and controls.

The coolant salt, containing no uranium, is similar to the fuel salt in its nonnuclear characteristics. The use of sodium fluoroborate coolant salt<sup>6,7</sup> is under consideration, but this experiment is expected to have little or no effect on the instrumentation.

Table 1.1.1 gives the composition and characteristics of the fuel and coolant salts currently (March 1966) being used in the MSRE.

$^{6}$ P. N. Haubenreich et al., Consideration of Substituting Uranium-233 in the MSRE Fuel, ORNL-CF-66-12-28.

7R. E. Brooksbank, P. N. Haubenreich, and J. H. Shaffer, "Study of the Use of U233 in MSRE," MSR-66-21 (internal memorandum).

Table 1.1.1.   

<table><tr><td></td><td>Fuel Salt</td><td>Coolant Salt</td></tr><tr><td>Composition (mole %)</td><td></td><td></td></tr><tr><td>LiF</td><td>65</td><td>66</td></tr><tr><td>BeF2</td><td>29.2</td><td>34</td></tr><tr><td>ZrF4</td><td>5.0</td><td></td></tr><tr><td>UF4(33% 235U), approx</td><td>0.8</td><td></td></tr><tr><td>Physical properties (at 1200°F)</td><td></td><td></td></tr><tr><td>Density, lb/ft3</td><td>134</td><td>120</td></tr><tr><td>Viscosity, lb ft-1hr-1</td><td>20</td><td>24</td></tr><tr><td>Heat capacity, Btu lb-1(°F)-1</td><td>0.47</td><td>0.53</td></tr><tr><td>Liquidus·temperature, °F</td><td>840</td><td>850</td></tr></table>

Since these salts are frozen below $840^{\circ}\mathrm{F}$ , it is necessary to apply heaters to the tanks and the piping throughout the salt systems.

Figure 1.1.3 shows the reactor core vessel after assembly. The reactor is graphite-moderated, with the graphite in the form of long vertical bars, or stringers. These stringers are essentially square in cross section with grooves cut into the four faces to channel the flow. Figure 1.1.4 is a horizontal cross section through the axial center line of the core, showing the shape of the graphite moderator bars and the location of the control rods.

Whereas the fuel is a homogeneous salt, the core itself has many of the nuclear characteristics of a heterogeneous reactor. Table 1.1.2 lists some of the nuclear parameters of interest to the control and safety system designer.[2,8]

Table 1.1.2.   

<table><tr><td>Core size</td><td>141 cm diam × 200 cm long</td></tr><tr><td>Neutron lifetime, ℃*</td><td>240 μsec</td></tr><tr><td>Temperature coefficient of reactivity</td><td></td></tr><tr><td>In fuel salt</td><td>4.0 × 10-5(8k/k)/°F</td></tr><tr><td>In graphite</td><td>3.3 × 10-5(8k/k)/°F</td></tr><tr><td>Total</td><td>7.3 × 10-5(8k/k)/°F</td></tr><tr><td>Effective delayed neutron fraction</td><td></td></tr><tr><td>Stationary fuel</td><td>0.0067</td></tr><tr><td>Circulating fuel</td><td>0.0045</td></tr><tr><td>Power density (fuel) at 7.5 Mw</td><td></td></tr><tr><td>Maximum</td><td>29.0 w/cm3</td></tr><tr><td>Average in core</td><td>13.3 w/cm3</td></tr><tr><td>Maximum allowable rod drop time</td><td>1.35 sec</td></tr></table>

Control rods are employed for both safety and routine operational control. Nuclear excursions are not incredible, but none have been postulated that cannot be averted by well-established techniques using a reliable protective system.

Both the fuel and coolant salt loops are blanketed and purged with flowing helium at a slight positive pressure, nominally 5 psig. This is accomplished in the salt pumps, which are designed to provide a gas space for the helium; see Fig. 1.l.5. The volute around the pump impeller is enclosed in a larger tank, the pump bowl. The pump bowl is

kept about half filled with fresh circulating salt by means of a bypass flow of 50 to $65\mathrm{gpm}$ $(\sim 5.0\%)$ around the pump. The salt, at pump outlet pressure, is delivered to the relatively quiescent volume in the pump bowl through a toroidal spray ring which allows the escape of gaseous materials from the salt. These released gases, composed mainly of fission products and, perhaps, hydrocarbons, are carried to the off-gas system by a continuous flow of helium which sweeps across the free salt surface in the pump bowl. Hydrocarbons, if present, will originate with small leaks in the lubricating oil seals in the pumps.

While MSRE fuel at $1200^{\circ}\mathrm{F}$ has a vapor pressure of only $4.47 \times 10^{-3}$ mm Hg, the 5-psig overpressure substantially reduces the amount of long-term salt carry-over into the off-gas system; it also helps to prevent large-scale contamination of the pump itself by salt deposition. The gas spaces in the pump bowl and the overflow tank provide extra volume for fuel expansion from excessive temperature should the need arise.

A second helium flow is used to purge the lubricating and cooling oil passages in the pump to prevent the entry of contaminants from the pump bowl.

Helium is used as a cover gas in the fuel and coolant salt drain and storage tanks and, by increasing the pressure, becomes the driving force used to fill the circulating loops.

The off-gas system conveys the helium from the tanks and the pump bowls to particle traps, filters, charcoal beds, etc., and thence to discharge via the off-gas stack.

In addition to the main nuclear heat rejection system, described in Sect. 2.8, auxiliary cooling is required in the reactor and drain tank cells. The ambient air temperature in these cells is maintained at $150^{\circ}\mathrm{F}$ or less by two air-to-water space coolers. Direct forced air cooling is used on the freeze valves and on the control rods and their drives. This forced air pumping system is also used to evacuate the reactor and drain tank cells to their operating pressure of $-2.0$ psig. The in-cell cooling water system is used to cool such in-cell components as the thermal shield, salt pump motors, and space coolers.

Fuel additions and the removal of samples for analyses are made with the sampler-enricher. This is a device connected with a pipe to the fuel salt pump bowl and which, of necessity, penetrates all containment barriers.

Freeze valves are used in the interconnecting salt pipelines between the various tanks and the reactor vessel. A length of flattened pipe that can be cooled and heated is a conceptual and perhaps oversimplified description of a freeze valve. Valve closure is obtained by freezing a salt plug in the flattened portion of the pipe.

The complex of reliable instrumented subsystems used solely for protection forms the MSRE safety system. In the MSRE the protection may be categorized as (1) protection against nuclear excursions, (2) protection against loss of containment, and (3) protection of vital equipment.

From the standpoint of extent and quantity, a majority of the safety system instrumentation is in category 2. These are process-type instruments based on measurements of pressure and radiation level. Their output actions are to close valves, shut down pumps, etc., in lines which are possible escape routes for contamination.

The preceding paragraphs highlight those features of the MSRE that are of particular interest to the instrumentation and controls designer.

Two of the major problem areas created by the reactor system's design are containment and temperature (its measurement, control, display, and recording).

The first containment barrier, cladding, always present in a heterogeneous reactor, is missing. This placed more stringent requirements on the instruments used to measure pressures and levels inside the reactor loop. The problems were magnified by the higher than usual temperatures encountered in this service. Obtaining high-grade satisfactory measurements of important flows, pressures, levels, and temperatures is complicated by the general requirement that the number of primary containment penetrations be minimum and, even more so, by the environments of molten salt, fission products, and radiation inside the primary containment or in the coolant salt loop, where measurements involve either molten fuel or coolant salt.

It is impossible to operate the MSRE and not breach the primary and secondary containment volumes with process lines for helium, air, and water (Fig. 1.1.6). In many cases these containment penetrations violate design criteria unless they are capable of being reliably blocked with instrumented systems when potential hazards are detected; hence the extent of the process-type instruments in the safety systems and the extensive use of sensors and transducers designed to meet containment requirements. In addition, wide variations of reactor and drain tank cell temperatures and pressures complicated the containment aspects of pressure-measuring instruments since this large and convenient contained volume could not serve as a stable reference.

To a degree the apparent emphasis on problems of containment is a result of the inherent characteristics of unclad, fluid-fueled reactor systems. However, the design of the MSRE was complicated by having to shoehorn it into an existing facility with size and general configuration less than ideal. This housing situation generated additional design problems with both the reactor system and the instrumentation and controls. Auxiliary systems for air, oil, water, helium, and emergency power are of necessity spread out and remotely located, cable and piping runs tend to be long and tortuous, power and signal cables could not be properly separated, and it was not feasible to put all the controls in one central area. Instead, some of the auxiliaries are provided with local control panels that are periodically supervised by the operators. These problems of interconnecting and integrating the various subsystems into an operating entity would have been substantially reduced in a facility engineered specifically for the MSRE. In particular, problems of containment and the amount of instrumentation for containment could have been substantially reduced.

Temperatures throughout the two salt systems are the most numerous and possibly the most vital single type of measurement in the MSRE. Both salt systems (freeze valves excepted) must be maintained above the freezing temperature $(850^{\circ}\mathrm{F})$ and should not exceed $1300^{\circ}\mathrm{F}$ . This upper temperature limit<sup>9</sup> is based on stress and metallurgical considerations and, depending on location, a reasonable and safe allowance for fuel expansion caused by

any unscheduled temperature excursion. Stress producing temperature gradients are to be avoided. If salt freezes, it may rupture the containing pipe or vessel on remelting. The coolant salt radiator is particularly vulnerable in this respect. Accurate, reliable temperature information is essential to successful operation of the afterheat removal system, to freeze valve operation, to heat balance calculations, to reactivity balance calculations, to all operations involving criticality, to routine operational controls, and as input information to the safety system.

There are over 1050 thermocouples installed on the MSRE. A preponderance of these are on the salt loops, on the storage and drain tanks, and on associated piping. These salt systems are equipped with many manually controlled heaters; safe and effective control is only possible if the operators have a clear, reliable picture or profile of temperatures in the system and if they are assisted by suitable off-limit interlocks and alarms. For these reasons, high-speed temperature scanning and display and continuous data logging are extensively used. These logging and display systems also provide off-limit alarms. It is worth while to note that these temperature instrumentation systems are most intensively used when the salt loops are being heated prior to filling or before taking the reactor to power. When the reactor is on line and generating power, the loop temperatures become more uniform and certain; hence the control and monitoring problem is sharply reduced.

Other areas which called for more than usual care in design or for nonroutine solutions are:

1. measuring and controlling low flows of helium and off-gas to and from the cover-gas system,   
2. measuring helium cover-gas pressure in the fuel salt pump bowl,   
3. measuring salt level in the pump bowls,   
4. measuring coolant salt flow rate,   
5. measuring and controlling salt levels in the drain tanks,   
6. designing containment penetrations for instrument lines,   
7. designing in-cell instrumentation and related disconnects, piping, and wiring to accommodate remote maintenance requirements.

It was recognized at the onset of the MSRE design that suitable and eminently satisfactory instrumentation for some of these measurements was nonexistent. Therefore, in some cases the methods and components now in use have developmental status.

Sections 1.2 to 1.5 are concerned with broad and quite general descriptions which are intended to convey design philosophy and criteria. Detailed descriptions of MSRE instrumentation and control are contained in Sects. 2 to 8. The outline which follows will give the reader an idea as to the scope and the arrangement of this report.

![](images/8d997422dbaa9fa58dbae52394b88769b691ee2867d3c078ef2f9e0a9aee6141.jpg)  
Fig. 1.l.l. MSRE Layout.

![](images/a255fb17257afca9e0d66b0f52f7e6f9b089a98e7100124788021f4b712667c9.jpg)  
Fig. 1.1.2. MSRE Primary and Secondary Molten-Salt Loops.

![](images/e193d71a6c1f435c2048f25bdd0624d441bf5a4ca4ed671ca38d3c2994722121.jpg)  
Fig. 1.1.3. MSRE Reactor Core Vessel After Assembly.

ORNL-LR-DWG 61097 R2

![](images/b0f933546817c4cb6c3e900dc0aef8b63a3b44dd9f1934de5ef7a2b18a9e66a8.jpg)

ORNLDMG64-8814

![](images/861851ae159722eb68e05569800225cd9e9a71d01b2a837a91d35ac6ff021fe7.jpg)  
NOTE: STRINGERS NOS. 7,60 AND 61 (FIVE) ARE REMOVABLE.   
Fig. 1.1.4. Lattice Arrangement of MSRE Control Rods.

![](images/3eda298ea6ca275e9935cb6fbce55013d008062a910e873f3f263f55eca9819c.jpg)  
Fig. 1.1.5. MSRE Fuel Pump.

![](images/2bec4f24c1664ce3a3a04d1014a3fcb7dba3f003ba2bc67a5f00baf27a847dba.jpg)  
Fig. 1.1.6. Schematic of MSRE Secondary Containment, Showing Typical Penetration Seals and Closures.

# OUTLINE OF CONTENTS OF TM-729

1. MSRE Instrumentation and Control System - General

1.2 Design Considerations

Discusses the considerations which influenced the design, particularly those which are unique or are peculiar to the MSRE.

1.3 Plant Instrumentation Layout

Describes the physical layout of the instrumentation system. Gives a general description of the overall layout (Sect. 1.3.1) and then describes each area separately. The instrument systems are located by area, and the routing and installation of their interconnections are included.

1.4 Plant Control System

Gives a broad, all-inclusive picture of the entire MSRE instrumentation and control system, including control of auxiliary equipment and the instrument power system. The "mode control" used to guide reactor operation is discussed with diagrams which define (or give) the conditions for the various modes (Prefill, Operate-Start, Operate-Run). The intent of this section is to outline the main subsystems and not to dig into fine structure. The reader is referred to Sects. 2 to 7 for details.

1.5 Safety System

Discusses the safety-grade instrumentation and controls associated with the MSRE safety system. The discussion includes general design criteria (designer's guidelines) illustrated by a typical system. The entire safety system, what it does, and why are tabulated and diagrammed. This section replaces similar but obsolete material in ref. 2.

2. Safety Instrumentation and Reactor Control

2.1 Nuclear Instrumentation

Describes the instrumentation in the neutron channel up to, but not including, the panel electronics. The neutron penetration, including the guide tube assembly, is described, and the interconnecting cabling, junction boxes, etc., associated with transmission of signals to the control rooms are diagrammed.

# 2.2 BF3 Instrumentation

Describes briefly the instrumentation associated with the sensitive $\mathrm{BF}_3$ channels used for low-level flux measurement and control. The interlocks associated with the $\mathrm{BF}_3$ channels are discussed in Sect. 2.6.

# 2.3 Wide-Range Counting Channels

The wide-range counting channels are described with block diagrams and an explanation of their operation. This is followed by descriptions of the chamber assembly, of the chamber and the associated electronic circuits, and of the electromechanical drive. The interlock and control functions associated with the wide-range counting channels are covered in Sect. 2.6.

# 2.4 Linear Power Channels

Describes briefly the linear power channels and includes block diagrams and descriptions of the compensated ion chamber and of the picoammeter.

# 2.5 Rod Scram Safety System

Contains a thorough description of the rod scram safety system. Block diagrams and circuit diagrams illustrate the discussion. The associated electronics are discussed in detail.

# 2.6 Shim and Regulating Rod Control System

Gives a thorough description of the shim and regulating rod control system. Block diagrams and composite elementary circuit diagrams for both the servo rod and the shim rods are included. The "Confidence" interlocks originating in the wide-range counting channels (see Sect. 2.3) are also described.

# 2.7 Control Rods and Drives

Describes the control rods and the rod drive units. A description of the pneumatic fiducial zero position indicator is included.

# 2.8 Load Control

Describes in considerable detail the control of the equipment which determines the reactor load, namely: radiator, radiator doors, blowers, and bypass damper.

# 2.9 Health Physics Monitoring

Describes the health physics instrumentation and includes a general description of the individual types of instruments used plus a description of their interconnections to form an integrated alarm system.

# 2.10 Process Radiation Monitors

The components and electronics used to monitor process lines carrying helium, water, off-gas, etc., are described. The operation of interlocks and alarms is covered in Sect. 4.

# 2.11 Stack Monitoring

Describes the radiation monitoring installed in the off-gas stack. The components, how they function, and their purpose are included in the discussion.

# 3. Process Instrumentation

Provides a general description of the instrumentation in the various systems. Included are descriptions of major control loops with drawings of individual control loops and their instrumentation. The principles of operation of the various components as well as control circuit operations are discussed in other sections. In general, sufficient descriptive material, augmented by flowsheets and diagrams, is included so that a reader with a reasonable knowledge of instrumentation systems can determine the arrangement and composition of the process instrumentation system.

# 4. Electrical Control and Alarm Circuits

# 4.1 General Description

Introduces in very general terms the types of circuits to be found in the MSRE system and how they are related. This text material provides the background for succeeding sections (4.2 to 4.13).

# 4.2 to 4.10 Master Control Circuits, etc.

Describes the electrical control circuits with engineering elementary schematic circuits diagrams and, where instructive, includes the nonobvious interlock functions and explains why they are required. The material presented enables a person with a reasonable knowledge of instrumentation and control systems to understand the operation of the control circuits.

# 4.11 Jumper Board

Explains purpose and describes the physical construction of the jumper board. Layout and wiring of a typical section of the board are included.

# 4.12 Annunciators

The annunciator system is described. Considerations involved in the location of annunciators are outlined. Schematics of the annunciators used and their sequence of operation are included. Their operational use is also discussed.

# 4.13 Instrument Power Distribution

Outlines the system which provides the MSRE instrumentation, control circuits, and annunciators with the necessary power. Reliability considerations are included.

# 5. Standard Process Instrumentation

Provides a general description of the various types of standard instruments used in the MSRE and includes basic principles of their operation.

# 6. Special Process Instrumentation

Contains descriptions of the nonstandard instruments required by the MSRE. Their unique or special features are outlined.

# 7. Data Logging and Computation

Gives a general, broad description of the data system. Describes basic capabilities, operations, and purpose of the logger-computer. Note: The reader is referred to manufacturers' literature and the operations manual for detailed information.

# 8. Miscellaneous

8.1 Instrument Numbering System and Instrument Application Diagram Coding System

Explains the system of flow plan symbols and numbering used in preparation of instrument applications diagrams and tabulations with typical examples.

8.2 Wiring Practices and Coding

Describes the system used in designing and identifying MSRE instrumentation and control wiring with typical examples of panel and interconnection wiring.

8.3 Pneumatic Tubing Installation Practices and Coding

Describes the system used in designing and identifying MSRE instrument tubing installations and includes a typical pneumatic schematic circuit and a typical panel and interconnection tubing installation.

# 1.2 DESIGN CONSIDERATIONS

# 1.2.1 Introduction

The design of the MSRE instrumentation and controls system and the selection, procurement, and/or development of components involved consideration of a number of operational, safety, and physical requirements. Table 1.2.1 lists the more important considerations, together with an indication of the design areas in which these considerations apply. In many cases, these considerations are similar to those encountered in the design of industrial plants and research facilities, such as high-temperature liquid-metals systems, chemical processing plants, petroleum refineries, and other types of nuclear reactors. Wherever possible, the design was based on existing technology, and components were procured from commercial sources of supply; however, in some cases, individual considerations (or combinations of considerations) presented problems which required special design or the development of special components. A discussion of the considerations listed in Table 1.2.1 is presented in the following paragraphs.

# 1.2.2 Operational Requirements

# 1.2.2.1 Compatibility with Centralized Control Philosophy

As discussed in Sect. 1.3.1, the MSRE instrumentation is centralized in the main control area so that the information and controls needed for routine operation of the reactor are immediately available to the operator. This philosophy of operation dictates that modular-type systems with signal transmission from primary element to receivers and from controllers to final control elements be used rather than integral field-mounted systems. For example, in the MSRE pressure transmitters and receiver indicators are sometimes used when a simple pressure gage would have sufficed for a noncentralized system. This example, however, should not imply that all the measured variables are transmitted to the main control area. There are, in fact, many direct-reading field instruments, such as pressure gages, rotameters, thermometers, etc., in use in the MSRE. This type of instrumentation is used mainly where the instrument is located in an accessible area, usage is low, and quick access to information is not required. Where frequent or fast access to information is required; where containment, personnel safety, or basic instrument installation requirements dictate that the primary sensing elements be located in inaccessible areas; or where transmitted signals are required for operation of controls or interlocks or for logging of data, transmitters are used and the receiving equipment is located in the central control area or in other centralized locations such as the transmitter room and various field panels (see Sect. 1.3.1).

Similar considerations apply to the selection of final control elements. Where the final control elements are located in inaccessible areas or where control is either automatic or restricted by control

Table 1.2.1. MSRE Instrumentation and Control Design Considerations   

<table><tr><td rowspan="3" colspan="2">LEAD
1 - Primary Consideration Safety or Control
2 - Secondary Consideration Safety or Control.
3 - Primary Consideration - Safety Only.
4 - Primary Consideration - Control Only.
5 - Primary Consideration Safety.
Secondary Consideration Control.
6 - Primary Consideration Control.
Secondary Consideration Safety.
7 - Either Primary or Secondary Consideration Depending on Application.
X - Not Applicable.</td><td colspan="5">Primary Sensing Elements, Transmitters, &amp; Final Control Elements
Thermocouples, Flow Elements, Pressure, Differential
Pressure, Level and Flow Transmitters, Valves, Motors,
Moistors, etc.</td><td colspan="5">Interconnections Wiring &amp; Tubing
Wire, Tubing, Cables, Terminal Strips,
Connectors, Junction Boxes, Disconnects, etc.</td><td colspan="2">Receiving Instrumentations
Recorders, Indicators, Controllers,
Switches, Signal Conditioners,
Malays, etc.</td></tr><tr><td>Inside Biological Shelding
and Secondary Containment</td><td>Outside Biological
Shelding, Inside
Secondary Containment</td><td>Inside Biological
Shelding, Outside
Secondary Containment</td><td>Outside Biological
Shelding, Outside
Secondary Containment</td><td>Inside Biological Shelding
Inside Secondary Containment</td><td>Inside Biological Shelding
Inside Secondary Containment</td><td>Outside Biological Shelding
Inside Secondary Containment</td><td>Outside Biological Shelding
Inside Secondary Containment</td><td>Outside Biological
Shelding and Secondary
Containment</td><td rowspan="2">Panel
Hunted</td><td rowspan="2">Field
Hunted</td><td></td></tr><tr><td>With Primary
Containment
Penetration</td><td>No Primary
Containment
Penetration</td><td>With Primary
Containment
Penetration</td><td>No Primary
Containment
Penetration</td><td>With Secondary
Containment
Penetration</td><td>With Secondary
Containment
Penetration</td><td>No Secondary
Containment
Penetration</td><td>With Secondary
Containment
Penetration</td><td>No Secondary
Containment
Penetration</td><td></td></tr><tr><td rowspan="6">Operational
Requirements</td><td>Compatibility with
Centralised Control</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td></tr><tr><td>Ease of Operation</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>6</td><td>6</td></tr><tr><td>Flexibility</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Experimental Data</td><td>k</td><td>k</td><td>k</td><td>k</td><td>k</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>k</td><td>k</td></tr><tr><td>Remote Maintenance</td><td>1</td><td>1</td><td>x</td><td>x</td><td>x</td><td>1</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Maintainability</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td rowspan="3">Safety
Requirements</td><td>Containment</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>x</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Redundancy, Reparson, etc.</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Easards to Operating
Personnel</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td rowspan="3">Performance
Characteristics</td><td>Overall Accuracy</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>6</td><td>6</td></tr><tr><td>Reliability</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Failure Modes</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>5</td><td>5</td></tr><tr><td rowspan="6">Process
Conditions
Effects</td><td>Salt Conductivity</td><td>7</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Operating Pressure</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Operating Temperature</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Correction</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>x</td><td>x</td></tr><tr><td>Salt Flapping and
Vapor Deposition</td><td>1</td><td>x</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Electrical Resistivity
of Molten Salts</td><td>7</td><td>x</td><td>7</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="3">Environmental
Effects</td><td>Ambient Temperature</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Ambient Pressure</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>1</td><td>1</td></tr><tr><td>Radiation Damage</td><td>1</td><td>1</td><td>x</td><td>x</td><td>x</td><td>1</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td rowspan="5">Physical
Requirements</td><td>Well-Sealed Construction</td><td>1</td><td>2</td><td>1</td><td>2</td><td>2</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Ruggedness</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>1</td></tr><tr><td>Size</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>1</td><td>2</td></tr><tr><td>Materials of Construction</td><td>1</td><td>7</td><td>1</td><td>7</td><td>7</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Cleanliness</td><td>1</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Cost</td><td></td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td></tr></table>

interlocks, remotely controlled pneumatic or electric actuators are used.

Where frequent control adjustments are required, where the operator must have quick access to the control, or where it is desirable to prevent operation of the control element by persons other than the reactor operator, the control signal originates in control devices (automatic controllers, control interlocks, manually operated switches, etc.) located in the main control area.

Where centralized control is not required, the final control elements are operated either directly by hand or indirectly by means of control devices mounted individually on local control stations or grouped on field panels.

# 1.2.2.2 Ease of Operation

The layout of control areas, the placement of instruments and controls within control areas, and the selection of receiving instruments, control switches, etc., were strongly affected by considerations of operator convenience and ease of operation. Insofar as possible, controls and adjustments needed for routine operations of the reactor were placed on the central control console, and the receiving instruments which provide the information required for routine operation were located on either the console or the main control board.

To reduce the need for frequent reference to flowsheets and to reduce the chances of operational error, a graphic presentation was used in the layout of the main control board and of the jumper board. This graphic presentation is also a valuable aid in training of operators. As nearly as possible and consistent with other considerations, the prime space in the center of the main control board and console was reserved for the most important instrumentation and controls components. Components of lesser importance were located in auxiliary control areas or in the field. Instrument components and control devices on the graphic panel were placed so that they are visually associated with specific components or portions of the reactor system. Attention was also given to the vertical placement of components so that receiving instruments could be easily read from various positions in the control room and so that control switches would be within reach of an operator of average height.

Where a given operation requires frequent simultaneous observations of a receiving instrument and operation of control switches or adjustments, the controls and adjustments were located near the receiving instrument and were placed so that the receiving instrument would not be obscured by the operator's arms.

To implement the above design objectives and to minimize space requirements in the control areas, attention was given to the physical size of instrument components mounted in the control boards. In general, preference was given to small-sized instrument components where the use of such components was consistent with other considerations. Attention was also given to readability in the selection of receiving devices such as recorders and indicators.

Where possible and consistent with other considerations, systems were automated to relieve the operator of the necessity of performing numerous manual operations and thus free him to devote more time to the more important aspects of reactor operation. For example, the freeze valve circuits were designed to perform "freeze" and "thaw" operations automatically. Also a number of other variables, such as helium inlet purge flow, which might have been amenable to manual control are automatically controlled.

Further simplification of operations was obtained by use of the Computer-Data Logger described in Sect. 2.12.

# 1.2.2.3 Flexibility

The experimental nature of the MSRE dictated that the design of the instrumentation and control systems be flexible, that is, that it be amenable to change. To accomplish this objective the use of point-to-point wiring was avoided, and control circuit interconnections were made at centralized locations in the relay cabinets. Similarly, most thermocouples were routed to a patch panel in the main control area, where they were connected to readout instrumentation by patch cords. Further flexibility was provided by the use of ORNL standard modular hardware for fabrication of control panels and by selection of instrument components which permits ranges to be changed and control switches to be reset easily in the field. In addition to gaining the capability to change the system design after startup of the reactor, the flexibility designed into the system was of great value during the initial design since it permitted portions of the system to be designed, fabricated, and installed before the final design criteria were established.

# 1.2.2.4 Experimental Data

The requirements for experimental data from the MSRE resulted in more instrumentation than would be required for a nonexperimental (second-generation) reactor of the same type. Also, in many cases, the accuracy requirements imposed by the need for experimental data were greater than would have been required by process control considerations alone. Since the data inputs to the Computer-Data Logger are electrical (dc) voltages, first preference was given to the use of electrical transmission systems in these applications. However, in some applications, such as weigh cells, it was found that the use of pneumatic transmitters offered significant advantages. In these cases strain-gage pressure transducers were used to interface the pneumatic systems with the Computer-Data Logger.

# 1.2.2.5 Remote Maintenance

The requirement that all major components located within biological shielding or containment be amenable to remote servicing or removal and replacement was a primary consideration in the design of instrumentation

systems and the selection of instruments in these areas. In general, the design philosophy was to locate instrument components outside biological shielding so that they could be maintained directly. Where this was not possible, provisions were made for remote removal and replacement, or adequate operating and installed spares were provided. The major problem encountered in providing remote maintenance capabilities for in-cell instruments was the development of disconnect devices and methods of mounting instrument components. Disconnects were required for pneumatic tubing, electrical power wiring, and for low-level electrical signals. Because of the quantity involved, providing thermocouple disconnect capability required the greatest effort. With the exception of the weigh cell mountings, the design of in-cell instrument mountings did not present any special problems. The design of the weigh cell mountings required special attention because side loads must not be impressed on the cell and because the cells must be aligned so that the direction of force is parallel to the center line of the cell (see Sect. 6.6).

Remote maintenance requirements also imposed severe restrictions on the design of in-cell instrumentation and control systems. To permit unrestricted vertical access for tools and for component removal, instrument components were located and associated wiring and tubing were routed in a manner that would not interfere with these operations.

# 1.2.2.6 Maintainability

Consideration was given to the maintainability of all instruments whether located in-cell or not. Whenever a choice between instrument component types existed and other considerations were equal, preference was given to the type that was easiest to maintain. Plug-in instruments were used extensively. The use of this type of instrument permits quick replacement of faulty components with minimum disturbance of operations and subsequent repair of the faulty components in field or central shops. Attention was also given to the location of instrument components to ensure that they would be physically accessible for maintenance. Wherever possible, provisions were made so that components could be tested, adjusted, or replaced without excessive disturbance of operations.

# 1.2.3 Safety Requirements

# 1.2.3.1 Containment

Since many of the primary instrument elements associated with measurement of variables in the reactor system are attached to, or require penetrations of, the reactor primary or secondary containment, these instruments and/or associated lines are, in themselves, a part of containment. To avoid compromising the reactor containment, special precautions were required in the selection of these components and in the design of associated systems.

The MSRE containment criteria require the presence of two independent barriers against the release of activity. Preferably these

barriers would consist of fixed barriers such as a pipe or a vessel wall; however, the need for piping connections to auxiliary systems and for transmission of instrumentation and control information to and from the in-cell reactor system dictated that containment barriers be penetrated.

In general, the measurement of variables within the secondary containment involves the penetration of at least one containment barrier. However, in cases such as measurement of nuclear flux and process radiation, the desired information is obtained without penetrating either primary barrier. In other cases, such as measurement of primary system temperatures, drain tank weight, and pump speed, only secondary containment penetrations are required.

Penetrations<sup>1</sup> may take the form of electrical penetrations, piping penetrations, or special penetrations that are physically a part of the containment vessel, with the type of penetration being determined by the type of signal transmitted. Such penetrations were made in a manner that did not seriously degrade the integrity of the containment barrier or were provided with instrumented closures that will restore the integrity of the barrier if unsafe conditions occur (see Sect. 1.5).

The most difficult penetrations to close or protect were those associated with piping penetrations of primary containment. Weld-sealed (helium leak-tight) construction is used on all instrument components associated with such penetrations; connections are made by means of butt welds, leak-detected ring-joint flanges, or "autoclave" (or equivalent) connectors; and valves are provided with welded bellows stem seals.

In all cases where weld-sealed construction was required, the components were designed and tested to ensure that leakage through the body was less than $10^{-8}$ cm³ of helium per second under conditions of 50 psig internal pressurization. Also, those valves which form a part of the primary blocking system were designed and tested to have very tight shutoff characteristics (see Sects. 6.5 and 6.20).

Wherever possible, the instrument systems having primary system penetrations are designed to dead-end the penetration in a sealed component located inside the secondary containment. However, in some MSRE instrument systems, the penetration extends through both primary and secondary containment barriers. Examples of such penetrations are the helium purge lines associated with measurement of level and pressure in the fuel salt system and with the leak detection system used to determine whether sampler-enricher valves and ports are closed and sealed (see Sects. 3.12 and 6.8). A similar type of penetration is found in the lines connecting the drain-tank pressure transmitters to drain tanks. This latter example differs from the preceding one in that the

lines also serve as process lines which are used to pressurize the drain tanks during filling and transfer operations. Similarly, the purge lines that supply helium purge flow to the reactor as well as the flow elements and differential pressure cells associated with measurement of flow in these lines are part of the primary containment. In all the above cases, reliance is placed on the flow of helium purge gas to prevent the back diffusion of activity, with check valves and instrumented closures being provided to prevent the escape of activity. In general, the rule was used that two block valves or one block valve and one check valve were equal to one barrier. In some cases, two series check valves were installed, but in the primary system the use of redundant check valves alone was not considered to be adequate protection. Weld-sealed solenoid and pneumatically operated valves of the type discussed in Sects. 6.5 and 6.20 were used to provide the instrumented closures of these lines. Blocking action is initiated via the electrical control circuitry in the event of occurrence of unsafe conditions such as high activity in process lines, low helium supply pressure, high reactor cell pressure, etc. Operation of these protective systems is discussed in more detail in Sect. 1.5.

Other examples of instrument components that form a part of primary containment are the pneumatic and hand-operated valves located in primary system piping, the charcoal bed differential pressure cell, and the conductivity-type drain-tank level probe (discussed in Sect. 6.10). The drain-tank level probes are an example of an instrument penetration where the instrument component is physically a part of the containment vessel.

The most numerous (and fortunately the easiest to seal) penetrations of MSRE containment are those required for the 495 thermocouples attached to pipes and vessels within the secondary containment. These penetrations are closed by using ceramic (or glass) to metal feed-through seals inside and epoxy seals outside of the reactor containment vessel and biological shield (see Sect. 6.7). Similar techniques are used for sealing electrical penetrations required for in-cell heater, motor, signal, and control wiring. Examples of devices requiring electrical signal penetration of secondary containment are given below:

Primary system pressure and differential pressure transmitters

Primary system solenoid valves

Fuel salt pump speed pickups

Fuel salt pump microphones

In-cell valve position switches

Conductivity level probes

Primary system thermocouples

Rod Drives

At this point it should be noted that, with the possible exception of the conductivity level probes, there are no electrical penetrations of primary containment in the MSRE heated salt systems. This lack of electrical penetration of salt system primary containment is due partly to the lack of a suitable feed-through penetration seal and partly to

the fact that the high temperatures, high radiation, and low salt conductivity associated with the primary system tended to discourage the use of electrical techniques for measurement inside the primary system.

The next most numerous penetrations are the instrument piping penetrations of the secondary containment required for operation of valves, weigh systems, etc., within the secondary containment. With a few exceptions, these lines connect to closed systems or instrument components and are essentially inward extensions of secondary containment. To protect against possible rupture of these lines in the event of the maximum credible accident, a blocking system is provided which will close these lines if the reactor cell pressure rises above atmospheric (see Sect. 1.5). Some instrument penetrations of secondary containment vent directly to the space inside secondary containment and connect to components outside containment. These form an outward extension of secondary containment. Where the lines are short and the construction of the components satisfies the requirements for containment, as is the case for the pressure switches used in the blocking system, no blocking protection is provided. However, where the connecting lines are long or where the components do not meet the containment requirement, block valves operated by the systems discussed in Sect. 1.5 are provided.

Instrument components that form a part of secondary containment are, for the most part, standard commercially available items; however, consideration was given in their selection to maintenance of minimum overall leakage of the secondary containment. While containment requirements for these components were much less stringent than for components that formed a part of the primary containment system, more attention was given to the leak-tightness of these components than was given to similar components not associated with containment. Gasketed construction and standard tubing and pipe fittings were considered acceptable in most applications; however, the components were tested before installation, and systems were tested after installation to ensure that leakage was acceptably low. Although weld-sealed construction was not required for secondary containment, many components of the helium, lube oil, sampler-enricher, coolant salt, and chemical processing systems were weld-sealed and tested for helium leak-tightness to conserve helium; to prevent release of activity from potentially dirty systems (such as the lube oil, chemical processing, and coolant salt systems); to minimize the possibility of inleakage of oxygen to the heated salt systems during periods of abnormal operation; and to maintain the performance characteristics of the instrument system. In some cases, weld-sealed components were used because they were commercially available at costs comparable with similar components using standard construction.

Examples of instrument components of secondary containment using standard construction are:

1. block valves in the cell penetration blocking system, $^2$

2. all components in the cooling water systems,   
3. pressure regulators in the helium supply system,   
4. pneumatically operated off-gas system valves downstream of the charcoal beds (these valves were, however, ordered with weld nipple connections and were welded into the system),   
5. solenoid block valves in the chemical process system sampler, $^2$   
6. drain tank weigh cells and associated piping (special attention, beyond that required for containment, was given to the leak-tightness of this system to obtain maximum accuracy),   
7. some components connecting to penetrations of the outer barrier of the fuel sampler-enricher and chemical processing system sampler.

Examples of instrument components of secondary containment using weld-sealed, helium leak-tight construction are:

1. All components of the helium supply system and associated purge and supply lines, except regulators. Included in this category are pressure switches; flow elements; differential pressure and pressure transmitters; control valves; hand control valves in the bubbler purge lines; and capillary flow restrictors in the sampler-enricher purge lines, in the fuel and coolant system bubbler purge lines, and in the main helium supply to the fuel salt system drain tanks.   
2. Flow elements, capillary flow restrictors, and differential pressure transmitters in upper gas letdown lines from the fuel and coolant salt circulating pumps.   
3. All fuel and coolant lube oil system instrument components except the oil tank level transmitters. Included in this category are flow elements, pressure and differential pressure transmitters, control valves, and pressure switches. The level transmitters utilize gasketed construction but were shop tested for leak-tightness before installation.   
4. Components of the chemical processing system associated with reactor secondary containment and with containment of radioactive salts and gases during chemical processing operations. In addition to those components covered in item 1 above, this category includes the ultrasonic level probe, described in Sect. 6.11, and pressure and differential pressure transmitters, flow elements, and pressure switches in the associated HF, $\mathbf{F}_2$ , $\mathbf{N}_2$ , $\mathbf{H}_2$ , and $\mathrm{SO}_2$ gas supply systems. In general, a quality level intermediate between the weld-sealed construction required for reactor primary containment and the gasketed construction allowed in secondary containment was used in the chemical process system. For example, silver solder was accepted in lieu of welding, and Hoke type S-26 fittings were accepted in lieu of autoclave-type connections. Gasketed construction and standard tubing and piping fittings were not acceptable in this service because of the relatively high activity that will be present in the system during fuel processing operations.

5. Components of the chemical process sampler connecting to inner containment barriers. Although, for containment purposes, the quality of construction required in this system is the same as that for the chemical processing system, many components in this category have a higher quality of construction than required because of sampler operational requirements and because the chemical process sampler was originally the prototype for the fuel sampler-enricher. Instrumentation for this system is discussed in more detail in Sect. 3.12.

6. Components of the coolant salt system associated with reactor secondary containment. In addition to those components covered by items 1 to 3 above, this category includes the ball float level transmitter described in Sect. 6.9, the coolant salt venturi described in Sect. 6.13, the NaK-filled differential transmitter described in Sect. 6.12, the coolant-salt drain-tank supply vent and bypass valves, the coolant pump-bowl pressure transmitter, the coolant-salt drain-tank pressure transmitter, and the coolant-salt pump bubbler-level system. Weld-sealed construction was used in these applications because of the consideration of conservation of helium and exclusion of oxygen noted previously and because of the high operating temperature of the venturi, NaK-filled differential pressure transmitter, and the ball(float level transmitter. Because the coolant salt system is considered secondary containment, less protection was provided on the coolant-salt helium-supply purge and vent lines than was provided on similar lines in the fuel system.

From the above discussion, it should be noted that operational considerations, in many cases, dictated a quality of construction greater than that dictated by the containment considerations. Also, it should be noted that no mention has been made of sealing or closure of penetrations associated with signal and control wires or tubing for those instrument components that form a part of secondary containment. In almost all such cases the components are installed so that the bodies of the components form outward extensions of secondary containment and no penetrations were required. In the case of the few exceptions (notably the cell radiation monitors, cell ambient temperature thermocouples, and some components of the sampler-enricher and chemical process sampler), the signals are electrical, and the required seals are made by means of feed-through penetration seals.

With the exception of the cell ambient temperature thermocouples noted above, the measurement of temperature in the secondary containment systems posed no containment problems since all such measurements were made by means of thermocouples located on the outside of pipes and vessels (or in wells), and no penetrations were required. Other possible exceptions to the above are the thermocouples installed on the charcoal beds and the off-gas sampler (see Sects. 3.5 and 6.7). Penetration seals are provided where these thermocouples penetrate enclosures; however, since the enclosures are vented to the stack, these seals should probably be considered part of building containment rather than secondary containment.

# 1.2.3.2 Redundancy, Separation, and Identification

As discussed in subsequent sections of this report, the instrumentation and control systems associated with reactor safety are required to be redundant. In the MSRE, this redundancy is in the form of one-out-of-two or two-out-of-three logic. ORNL practices require that all components, wiring, and tubing be installed so that redundant safety channels are physically separated from each other and from control-grade components, wiring, and tubing and that safety channels be identified as such. Where possible, separation was accomplished by means of separate conduits, wireways, junction boxes, cabinets, and metallic barriers. In some cases, complete separation was not possible, and physical separation with appropriate identification (painted signs, labeling, and color coding) was used.

# 1.2.3.3 Hazards to Operating Personnel

Attention was given to providing protection against hazards to operating personnel beyond that provided by the reactor safety system. Wiring was installed in accordance with the National Electric Code and with ORNL recommended practices. Instrument lines that presented possible pressure or radiation hazards were either protected or confined to areas not normally accessible to operating personnel.

# 1.2.4 Performance Characteristics

# 1.2.4.1 Overall Accuracy

Accuracy was a prime consideration in the selection of instrumentation associated with the acquisition of experimental data and with some process and nuclear control systems. However, in reactor safety systems, accuracy was considered to be secondary to reliability. Also, in many process instrumentation applications, high accuracy was not required, and accuracy was considered to be secondary to other considerations, particularly cost. Since accuracy is a poorly understood and often misused term, the performance requirements for those instruments associated with the acquisition of high-accuracy data or information were specified in terms of individual performance characteristics such as linearity, zero drift, span shift, hysteresis, ambient temperature and pressure effects, process temperature and pressure effects, etc. In general, an effort was made to match accuracy specifications to the application; however, in some applications, considerations of minimization of the number of instrument types used and reduction in requirements for operating spares resulted in the use of instruments having a higher accuracy than required.

# 1.2.4.2 Reliability

Reliability was a prime consideration in the selection of all instrument components and was of particular importance in the selection of reactor safety system components. However, since obtaining high reliability

can be very expensive, the degree of reliability needed for a particular component was based, in general, on considerations of "cost vs consequences." Where high reliability was needed, reliability requirements were incorporated in the specifications, and components were tested before and after installation. Where moderate reliability was sufficient, selection of component was based on experience and engineering judgment, and performance was proved during system shakedown testing and subsequent operations. At this point the distinction between component reliability and system reliability should be noted. As discussed in the following section, overall reliability can be enhanced by the use of redundancy in system design. Conversely, improper use of redundancy can reduce the overall system reliability below that of the individual components.

# 1.2.4.3 Failure Modes

Insofar as possible, components of the safety system (and of most control systems) were selected and installed in such a manner as to "fail safe." That is, the components were selected and systems were designed to produce the desired corrective or control action in the event of component failure or loss of supply power. A fail-safe action is sometimes referred to as a "failure toward danger," since such an action appears to the controlled system as a dangerous condition and is therefore in the safe direction. A single "failure toward danger" in a system using two-of-three logic converts it to one-of-two logic. The fail-safe mode of failure is the direct opposite of the "unsafe failure" mode, which results either in an unsafe or undesired action or in no action at all. Examples of the latter would be an upscale failure of an instrument channel having a downscale trip, an open-circuited coil in a relay which must be energized to produce the desired action, a welded contact which must open to produce the desired action, and an "in-place" failure of an instrument resulting in the controlled system remaining in the state that it was in when the failure occurred. In-place failures are characteristic of motorized equipment and occur mainly in servo-controlled equipment such as potentiometric recorder-controllers. This type of failure can be caused by loss of supply power, by desensitization of amplifiers by excessive noise on the signal, by dirty slide-wires, or by component failures.

It should be recognized at this point that an "unsafe failure" of one channel in a safety system utilizing redundancy can be very serious. In the case of systems using one-of-two logic, an "unsafe failure" of one channel will convert the system to a "single-tracked" system with full dependence for safety being placed on each and every component of the remaining channel. The situation is even more critical in the case of systems using two-of-three coincidence logic, since an "unsafe failure" of one channel will convert the system to a two-of-two coincidence logic system, with full dependence for safety being placed on each and every component of both remaining channels. Routine testing is required to detect such conditions.

While fail-safe action is desirable, it is usually difficult or impossible to obtain in practice. Few (if any) devices have only one failure mode. For example, an otherwise fail-safe device or system incorporating a feedback loop will usually fail "unsafe" if the feedback

loop is opened. Most devices have two possible modes, and some have more (such as upscale, downscale, and in place). However, the devices will usually have a "preferred" or "most probable" failure mode. Where one mode is predominant the device is said to fail in this mode, and circuits are designed accordingly. In some cases ambiguity of modes can be reduced or eliminated by the use of "confidence" circuitry and monitoring devices (such as "power-failure" relays), which produce a corrective action in the safe direction in the event of the occurrence of a condition that could result in an unsafe or unwarranted action. Although it is possible to design around some undesirable failure modes, components and system are, in general, too complex and too unpredictable to use this crutch extensively. In the final analysis the use of fail-safe design techniques must be recognized for what it is - a means for reducing the probability of unsafe or unwarranted actions - and reliance must be placed on the use of the principles of redundancy and diversity together with surveillance, testing, and monitoring to obtain a level of reliability commensurate with the requirements for reactor safety and continuity of operations.

# 1.2.5 Effects of Process Conditions

# 1.2.5.1 Operating Temperature

Temperature effects were an important consideration in the selection of all primary sensing elements and were a primary consideration for those components which were attached to the heated salt systems. In these systems the $1200^{\circ}\mathrm{F}$ operating temperature presented problems which necessitated the development of special instrumentation. In other MSRE systems the temperatures were within the range where satisfactory performance was obtainable with commercially available instrument components. The effects of variations of temperature on accuracy and other performance characteristics are of interest at low temperatures (below $150^{\circ}\mathrm{F}$ ) and become increasingly important as the temperature increases. At higher temperatures (above $300^{\circ}\mathrm{F}$ ), damage to materials such as plastics and elastomers becomes important; at elevated temperatures (above $600^{\circ}\mathrm{F}$ ) the general operability becomes a matter of concern. Also, since corrosion is accelerated and structural strength of material is degraded as the temperature is increased, the choice of materials becomes a prime consideration at elevated temperatures. The philosophy adopted in the design of MSRE salt system instrumentation was to avoid operation of instruments at high system temperatures wherever possible and to obtain readings indirectly with instruments operated under more favorable conditions. Where this was not possible or desirable, development of special instrumentation was initiated (see Sect. 6).

# 1.2.5.2 Operating Pressure

As in the case of temperature the effects of process operating pressure and of pressure variations on performance characteristics and structural strength become increasingly important as the pressure increases. These pressure effects are most important in applications

where the operating temperature is high. Fortunately, MSRE pressures are low (below 50 psig) in those portions of the system where temperatures are above $150^{\circ}\mathrm{F}$ ; so the required structural strength was, in most cases, obtainable with a minimum of effort. Close attention to effects of pressure was required in the selection or development of components which operate at temperatures above $600^{\circ}\mathrm{F}$ , and in cases such as the molten-salt level probes, the requirements for structural strength and containment imposed severe restrictions on the design. In other cases, such as the NaK-filled differential pressure transmitters, the effects of pressure variations were the boundary conditions which limited the accuracy of the instrument.

# 1.2.5.3 Corrosion

Corrosion was a prime consideration in the selection or development of all instrument components which were exposed to process fluid. However, in all reactor systems except the fuel processing system, the requirements for corrosion resistance were easily satisfied by use of standard materials available for commercial components or by use of INOR-8 (Hastelloy N) materials for developmental instruments.

In the fuel processing system the high corrosion rates expected during fluorination precluded the use of the thin-walled conductivity level probes for level detection in the fuel storage tank and forced a redesign of the ultrasonic level probe to obtain adequate corrosion allowance.

In some cases materials were used which gave corrosion resistance beyond that dictated by the process conditions. This was done to permit decontamination of components with acid rinses.

Exposure of components to corrosive conditions was avoided where possible by obtaining readings indirectly with components operated under more favorable conditions. For example, pressure in the fuel storage tank was obtained by measurement of pressure in a purge line connecting to the tank. This technique is similar to that used to avoid temperature problems (see Sect. 1.2.5.1).

Since corrosive conditions did not exist in the MSRE operating areas, no special precautions were required for the selection of components and design of systems located in these areas.

# 1.2.5.4 Salt Plugging and Vapor Deposition

Consideration was given to the possibility of plugging of instrument lines with salt wherever these lines penetrated lines or vessels containing salt. Such plugs can occur as a result of expulsion of salt into cold instrument lines or as a result of vapor deposition of salt in the lines. Lines can also be plugged by formation of oxides where gas is purged into the system below salt level.

The consequences of plugging range from minor to very serious, since the resultant loss of information could further result in loss of experimental data, loss of control, or loss of one or more channels of safety protection.

During initial stages of MSRE design, it was believed that vapor deposition and oxide formation might be very serious problems and might preclude measurement of pressures, differential pressures, etc., with

instruments attached to purged gas lines. This belief was based on experience in earlier molten-salt systems in which considerable difficulty with plugging was experienced. Further investigation revealed that the vapor pressure of the MSRE salts and the expected oxygen content of the MSRE cover gas would be much lower than those of previous systems. On the basis of this information the indirect measurement approach was adopted.

To minimize the possibility of plugging, all instrument lines which penetrated salt-containing lines and vessels were made as large as was consistent with other considerations, and instrument taps were located as far above salt level as possible. In almost all cases MSRE instrument components are located on inlet gas lines, and a small purge flow is maintained in the lines. This purge flow also serves to minimize back diffusion of radioactive gases. Some components, such as the fuel off-gas letdown valve, the charcoal-bed differential-pressure transmitter, and the fuel-pump gas-letdown flow transmitters, were located on lines downstream of the reactor. In these cases the components were placed as far downstream as possible and were protected by filters. In cases such as the bubbler level indicator, where instrument lines are required to extend below salt level, provisions were made to ensure that pressure transients will not expel salt into cold lines (see Sect. 6.8).

Experience to date on the MSRE and on related engineering test facilities indicates that the philosophy adopted was sound and that the provisions made in the design to prevent plugging were adequate. Some plugging has occurred in off-gas lines; however, this plugging was due to hydrocarbon plugging and was not expected during the initial design.

While the MSRE instrumentation and controls system has been essentially free of salt plugging problems, the need for purge flow, together with other considerations (such as operating temperature and radiation damage), resulted in a complexity of instrumentation beyond that required for the basic measurement. This increased complexity resulted from the additional instrumentation needed to prevent the escape of activity through instrument lines which penetrated both containment barriers. If radiation-resistant transmitters capable of operating in direct contact with the salt had been available, this complexity of instrumentation (and the probability of salt plugging) would have been reduced. NaK-filled transmitters offer promise for use in future reactor systems, provided the possibility of release of NaK into the system can be tolerated. Also the ball float level transmitter described in Sect. 6.9 may be a satisfactory replacement for the bubbler-type level system in some applications.

# 1.2.5.5 Electrical Resistivity of Molten Salts

The electrical resistivity of the MSRE fuel and coolant salts was determined to be approximately 1 ohm-cm at $1200^{\circ}\mathrm{F}$ and 1 kilohertz (1000 cps). While this resistivity indicates that the MSRE salt is a fair conductor, it is high in comparison with the 120-microhm-cm resistivity of Hastelloy N and Inconel and even higher in comparison with the 35-microhm-cm resistivity of sodium and 80-microhm-cm resistivity of NaK at $1200^{\circ}\mathrm{F}$ . Conversely, the resistivities of NaK and

sodium are low in comparison with Hastelloy N and Inconel. Therefore, while Inconel can be considered as a poor insulator in comparison with NaK and sodium, Hastelloy N is a good conductor in comparison with the MSRE salt. For this reason, devices such as magnetic flowmeters and "J" probe type level indicators, which are used extensively in liquid-metal systems, are not suitable for use in the MSRE molten-salt systems. However, the conductivity properties of the MSRE salt were utilized to obtain single-point indications of level in the MSRE drain tanks (see Sect. 6.10).

# 1.2.6 Environmental Effects

# 1.2.6.1 Ambient Temperature

Ambient temperature effects did not impose severe restrictions on the selection or development of any MSRE instrument components, since the in-cell ambient temperatures are kept below $150^{\circ}\mathrm{F}$ by the use of space coolers and the temperatures in operating areas do not exceed $100^{\circ}\mathrm{F}$ . (The main control areas are air-conditioned, and temperatures are kept relatively constant at about $75^{\circ}\mathrm{F}$ ). However, the effects of variations of ambient temperature on the accuracy of measurements were important, and they were considered during procurement of components and design of the system. Also, in some areas where natural circulation was restricted or density of heat-generating equipment was high, forced-draft air cooling was required to maintain the ambient temperature of the components and that inside the cabinets within acceptable limits.

# 1.2.6.2 Ambient Pressure

The effects of ambient pressure were important in the selection or development of all components that were referenced, directly or indirect, to atmospheric pressure or to in-cell pressures.

In some cases, such as determination of cell leak rate and monitoring of building containment, the pressures themselves were of direct concern. In all other cases, the interest lay in the effects of pressure on the accuracy of the measurement.

Instrument components which are (or may be) sensitive to ambient pressure generally fall into one of the following three categories:

1. those which sense the difference between an internal pressure and the pressure of the surrounding medium and which generate a mechanical or electrical signal or indication (pressure gages, manometers, pressure switches, and pneumatic receivers);   
2. those which convert a force, motion, or electrical signal into a pneumatic pressure (current-to-pneumatic converters and pneumatic valve positioners);   
3. combination of 1 and 2 (pneumatic pressure transmitters and pneumatic weigh cells).

Such instruments usually incorporate a bellows or a Bourdon tube in the mechanism.

Pressure in the drain-tank cell can vary over a wide range (+5 to -4 psig) during the course of normal operations. The pressure can vary less in areas ventilated by the containment air system since pressures in these areas are maintained slightly negative with respect to the atmosphere (approximately -0.2 to -2 in. H₂O gage). Also, variations of atmospheric pressure are of interest in many instances. Variations over the range from 28.7 to 29.5 in. Hg were observed at the MSRE site over a six-month period, and larger variations are possible during extreme weather conditions. The observed variations correspond to approximately 0.5 psi. Although this value is small, it amounts to 1% of the 50-psig measurement span of most MSRE pressure transmitters and 4% of the 12-psi output signal span of 3- to 15-psig pneumatic transmitters.

The philosophy adopted in the design of the MSRE instrumentation and controls system was to avoid the use of pressure-sensitive components in areas where pressure variations occurred. Where this was not possible, or where the use of pressure-sensitive components offered significant advantages, the effects of pressure variations were eliminated by internal compensation of the device or by correcting the data. The drain-tank weigh cells are an example of the use of internal compensation. Data correction was used to correct gage pressure data such as obtained from the reactor cell pressure transmitter. Another form of compensation, which is not usually recognized as such, is the location of associated pneumatic transmitters and receivers in the same pressure environment. Although this technique is common practice, significant errors can occur when this effect is overlooked and transmitters and receivers are installed in areas having different ambient pressures.

# 1.2.6.3 Radiation Damage

All instrument components located within the reactor and drain cells are subject to damage from nuclear radiation. However, some components of the sampler-enricher, the chemical process system, the chemical process system sampler, the off-gas system, and the off-gas sampler are less subject to radiation damage. The radiation level in the coolant salt and waste cells is relatively low, and radiation damage in these areas was not considered serious. The maximum radiation levels in various areas of the MSRE are listed in Table 1.2.2. The values listed are for peak conditions and assume that activity in the system has built up to saturation levels after sustained full-power operation.

In general, the selection of materials for use in high-radiation areas was governed by considerations of total integrated dose rather than dose rate, and the use of plastics and elastomers was limited to those areas where the total gamma dose expected during the lifetime of the reactor was less than $10^{7}$ r and the expected neutron dose was less than $10^{17}$ nvt. Where higher dosage was expected, component materials were restricted to metals and inorganics. Exceptions to this rule are the rod drive motors and all semiconductor devices. The rod drive motors have organic insulation and lubricants and are designed to be replaceable.

Table 1.2.2. Radiation Dose Rates in Various Areas of the MSRE During or Following Sustained 7-Mw Power Operation   

<table><tr><td>Location</td><td>Gamma (r/hr)</td><td>Neutron (neutrons cm-2sec-1)</td><td>Remarks</td></tr><tr><td rowspan="4">Reactor cell</td><td>7 × 104</td><td>107 thermal, 108 fast</td><td>At 7 Mw</td></tr><tr><td>5.4 × 103</td><td>Negligiblea</td><td>At 10 kwb</td></tr><tr><td>2.4 × 103</td><td></td><td>Zero power, reactor drainedc</td></tr><tr><td>2 × 103</td><td></td><td>Zero power, reactor drained and flushedd</td></tr><tr><td rowspan="3">Drain cell</td><td>4.2 × 103</td><td></td><td>At 7 Mw</td></tr><tr><td>4.2 × 103</td><td></td><td>At 10 kwb</td></tr><tr><td>2.6 × 104</td><td></td><td>Zero power, reactor drainedc</td></tr><tr><td>Fuel processing cell</td><td>5 × 103</td><td></td><td>After 11 days cooling</td></tr><tr><td>Coolant cell</td><td>100</td><td>~0</td><td>At 7 Mw</td></tr><tr><td>Fuel sampler-enricher</td><td>1000</td><td>Negligible</td><td>During sample with-drawal</td></tr><tr><td>Fuel processing sampler</td><td>20</td><td></td><td>During sample with-drawal</td></tr><tr><td>Off-gas sampler</td><td>500</td><td></td><td>During sampling</td></tr><tr><td>High-bay area</td><td>&lt; 20 × 10-3</td><td></td><td>At 7 Mw</td></tr><tr><td>Main control area</td><td>&lt; 1 × 10-3</td><td></td><td></td></tr><tr><td>Transmitter room</td><td>&lt; 75 × 10-3</td><td></td><td></td></tr><tr><td>North electric service area</td><td>&lt; 3 × 10-3</td><td></td><td></td></tr><tr><td>Service room</td><td>&lt; 1 × 10-3</td><td></td><td></td></tr><tr><td>Water room</td><td>&lt; 10 × 10-3</td><td></td><td></td></tr><tr><td>Vent house</td><td>&lt; 10 × 10-3</td><td></td><td></td></tr><tr><td>Diesel house</td><td>&lt; 10 × 10-3</td><td></td><td></td></tr></table>

aWith respect to gamma dose rate.   
bAfter 5 hr 10-kw operation following sustained 7-Mw operation.   
c. Immediately following above 5-hr operation at 10 kw.   
Two days after drain following 7 Mw sustained operation.

Semiconductors are known to be extremely sensitive to both dose rate and total dosage. The use of instrument components utilizing semiconductors was restricted to areas outside biological shielding, where radiation levels were expected to be relatively low. For example, the transistorized amplifiers used with the Foxboro ECI pressure and differential pressure transmitters were placed remote from the transmitter body when the transmitter was located in a high-radiation area. In areas such as the fuel sampler-enricher and the off-gas sampler, the maximum (peak) radiation levels are very high but the duration of the peak is relatively short. In these areas, radiation-resistant components and materials were preferred, but plastics and elastomers were permitted.

# 1.2.7 Physical Requirements

# 1.2.7.1 Weld-Sealed Construction

All instrument components which are an integral part of primary containment were weld sealed, inspected, and tested to ensure that helium leakage through the body to the surrounding area would be less than $10^{-8}$ $\mathrm{cm}^3/\mathrm{sec}$ at maximum expected internal pressures. To conserve helium, most instrument components of the cover-gas system were also weld sealed.

# 1.2.7.2 Ruggedness

The ability to withstand shock and vibration without permanent damage or temporary loss of performance was a consideration in the selection of all instrument components and was a prime consideration in the selection of field-mounted instrumentation. Of particular importance was the ruggedness of those components which are located within the reactor and drain cells and which may be subject to abuse during remote maintenance operations.

# 1.2.7.3 Size

Small physical size is generally desirable since reduction of the size of individual components results in an overall reduction in the size of control panels and minimizes interferences in the field. In areas such as the sampler-enricher the availability of space dictated that small-sized components be used; however, in most applications, other considerations predominated. For example, readability of receivers and general performance characteristics were considered to be more important than small size.

# 1.2.7.4 Materials of Construction

In addition to the requirements for physical strength and resistance to the effects of corrosion and radiation, discussed in Sects. 1.2.5.1, 1.2.5.2, 1.2.5.3, and 1.2.6.3, consideration was given to compatibility

of materials used in instrument components with the general metallurgical requirements of the MSRE. For example, the use of metals (such as lead, tin, and aluminum) with melting points below $1600^{\circ}\mathrm{F}$ was not permitted in areas where they could conceivably come in contact with heated pipes and vessels. Also, the use of dissimilar-metal welds for attachment or connection of instrument components to heated pipes and vessels was not permitted. The use of dissimilar-metal welds for thermocouple attachments was avoided by the use of a Hastelloy N tab which was welded to the Inconel thermocouple sheath in the shop and subsequently welded to the pipe or vessel when the thermocouple was installed.

# 1.2.7.5 Cleanliness

Since accumulation of dirt and other foreign materials will cause degradation of performance of most instrument components and systems, cleanliness was an important consideration in the procurement and installation of all MSRE instrument components. However, the degree of cleanliness required is dependent on the application and varies over a wide range. In most applications moderate cleanliness was adequate, and reliance was placed on the manufacturers' integrity and on preoperational checks and inspection for cleanliness control. A much higher degree of cleanliness was required for components which were an integral part of the heated salt systems or of pipes and vessels connected to these systems. To preclude the possibility of foreign matter being transported from these components to the molten salt or to heated surfaces in pipes and vessels, stringent cleanliness control was maintained during fabrication, transportation, and installation. Components fabricated outside ORNL were inspected by Company representatives during assembly. The degree of cleanliness was determined by wiping with dry surgical gauze. Discoloration of the gauze was cause for rejection. After assembly and testing, openings were capped, and the components were sealed in plastic bags and cartons and remained sealed until they were installed in the MSRE system.

# 1.2.8 Cost

A continuing effort was made during the design of the MSRE instrumentation and controls system and during specification and procurement of components, to minimize the overall cost of the system. In noncritical applications, cost was a primary consideration; however, in applications where safety, operability, and continuity of plant operations were involved, other considerations predominated. Also, where conflicts of objectives arose, decisions were based on consideration of "cost vs consequences."

# 1.3 PLANT INSTRUMENTATION LAYOUT

# 1.3.1 General Description

Instrumentation is centralized in the main control area, where a graphic control panel and operating console are located. Only information needed to operate the reactor is displayed on these panels. Auxiliary instrument and electrical panels, relay and thermocouple cabinets, and a data-logging system are adjacent to the main control room.

A second area, the transmitter room, is adjacent to the reactor cell. The available space and the desirability of mounting certain components close to the point of measurement dictated that this be a control area. With the exception of control-rod drives, thermocouples, pump speed pickups, microphones, high-level gamma ionization chambers, weigh cells, and some control valves, all instrumentation components are located in areas external to the reactor containment vessels.

Other instrument panels for auxiliary systems are located at convenient operating points throughout the building.

Sixty-one 2-ft modular instrument panel sections, one operating console, two relay cabinets, one thermocouple patch panel, and two equipment racks are required for the MSRE.

# 1.3.2 Main Control Area

The main control area, shown in Figs. 1.3.1 and 1.3.2, contains 12 control panels and the control console. The 12 panels comprise the main control board, which is in the form of an arc centered on the console.

The main control board, Fig. 1.3.3, provides a full graphic display of the reactor system and its associated instrumentation. These panels contain the instrumentation for the fuel salt system, the coolant salt system, the fuel and coolant pump oil systems, the off-gas system, the jumper board, and a push-button station for the various pumps and blowers. The primary recorders for nuclear control are also on the main board. The instrumentation on the console consists of position indicators, control switches, and limit indicators for the control rods, radiator doors, and fission chambers, and other switches required for normal and emergency operation of the reactor. Routine control of the reactor is accomplished from the main control area. Some of the auxiliary systems are also controlled here, with remaining portions controlled from the local panels shown in Figs. 1.3.1 and 1.3.4.

# 1.3.3 Auxiliary Control Area

The auxiliary control area, Fig. 1.3.2, consists of eight auxiliary control boards, five nuclear control boards, one relay cabinet, one thermocouple cabinet, four diesel and switching panels, and a safety relay cabinet. The eight auxiliary panels contain the signal amplifiers, power computer, switches and thermocouple alarm switches, auxiliary indicators not required for immediate reactor operation, the fuel and

coolant pump microphone amplifier and noise level indicator, and the substation alarm monitors. All the safety circuit control relays are located in the safety cabinet, and most of the operating circuit relays are in the control relay cabinet. The relay cabinet contains only the relays for the main control circuitry. The thermocouple cabinet contains a patch panel with pyrometer jacks. All thermocouples in the system except those on the radiator tubes are terminated in this cabinet. The thermocouples on the radiator tubes are routed to the temperature scanner and then to the patch panel.

The five nuclear panels contain some of the instrumentation for the process radiation system, the oil system, and the sampling and enriching system. The health physics monitoring alarm system, the high-level gamma chamber electrometers and switching panel, and the reactor control nuclear amplifiers, servo amplifiers, and other equipment for the nuclear control system are also located here. Four panels contain the instrumentation for the operation of the emergency diesel generators. The distribution panels for the control circuit and instrument power are located on the south wall of the auxiliary control room.

# 1.3.4 Transmitter Room

The transmitter room, Fig. 1.3.5, consists of nine control panels, one solenoid power supply rack, and a transmitter rack. Panels 1 and 2 are for the leak detector system, and panels 3 and 4 are for fuel drain tanks 1 and 2, the coolant drain tank, the fuel flush tank, and the fuel storage tank weigh instrumentation. Panels 5 and 6 are for the fuel and coolant pump bubbler-type level control, panel 7 is for the freeze valve air control, panel 8 contains the power supply and alarm switches for the drain tank level probes and a transducer for the float-type coolant-salt-pump level transmitter, and panel 9 is for the sump bubbler system. The solenoid power supply rack contains most of the solenoids for the fuel salt system and the power supplies and distribution panels for the electric transmitters and differential transmitters. The transmitter rack contains the remote amplifiers for the electric signal transmission system and also the current-to-air transducers.

All electrical and pneumatic lines that connect transmitter room equipment to input signals from the reactor, drain tank, water room, and all other areas outside the building enter through sleeves in the floor. Output signals from the transmitter room equipment are conducted via feeder cable trays to the main cable tray system, which runs north and south in the building on the 840-ft level.

# 1.3.5 Field Panels

Additional panels are required for the auxiliary systems. These (see Figs. 1.3.1 and 1.3.4) are located near the subsystems which they serve. Four panels for the cooling oil systems are located in the service room and service tunnel; one cooling- and treated-water system panel is located in the fan house; three panels are located on elevation 852 ft

at column line C-7 for the sampling and enriching system. Two cover-gas system panels are located in the diesel house. Two containment-air system panels are provided: one at the filter pit and the other in the high-bay area.

The reactor cell air pressure monitoring instrumentation and testing facilities are mounted on a single panel located in the north electric service area, which is directly below the transmitter room. Five panels for the fuel processing system are located in the high-bay area above the fuel processing cell. Two of these control the process, and the other three are for the sampler. One panel located in the high-bay area on top of the coolant cell serves the coolant salt sampler. Three panels for the fuel off-gas analyzer and one panel for the reactor-cell-air oxygen analyzer are located in the vent house. Two panels for the thermocouple scanning system are located on the 840-ft level near the heater control panels.

# 1.3.6 Interconnections

The control areas and the controlled systems are interconnected by cable trays and conduit. This system includes the main cable tray system running north and south in the building, with branch trays and conduits joining the main tray. These main trays carry all tubing for the pneumatic system, thermocouple lead wire, and the ac and dc control wiring. Each category of signal runs in a different tray to avoid mixing of the signals. Risers connect the panels and cabinets in the control area on elevation 852 ft with the main trays. No exposed trays are in the main or auxiliary control rooms. Safety system wiring is completely enclosed in conduit and junction boxes and is separated from control and instrumentation wiring.

# 1.3.7 Data Room

The data room is designed to house the data logger-computer; see Sect. 2.12. It contains all the data system equipment except one logging typewriter, which is located in the main control room. The layout of the equipment in the room is shown in Fig. 2.12.4 (Sect. 2.12). This room is located in the north end of the reactor building, next to the main control room. There are entries from the hallway and the main control room. A large glass window is located so that the main control panel can be seen from the data room.

The data system cabinets are installed in two rows, back to back, running east to west about the center of the room. The front row of five cabinets facing the control room contain the computer proper, and the six rows facing the north end of the room contain the analog input signal terminals and the control circuits for the typewriters, magnetic tapes, and other input equipment. The data system operator's console is located so that the reactor control panel can be seen by an operator at the console. Two desks and several tables are located in the room for

use of reactor operating and analysis personnel and the computer maintenance engineer. A storage cabinet for magnetic tapes is located at the west wall of the room, and a spare parts storage cabinet is located at the north wall. The electrical power panel for the system is located in the northwest corner of the room. The installed equipment is shown in Figs. 2.12.1 and 2.12.3 (Sect. 2.12).

The input signal cables for the data system are brought up to the bottom of the room in cable trays. Holes are cut in the floor beneath the cabinets for routing the input signal and control cables to the cabinets.

The data room is air conditioned by two 7.5-ton air conditioners. These same units can be used to supply air to the main control room in an emergency, and the control room air conditioner can supply air to the data room when necessary.

ORNL-DWG64-308R

![](images/b15c33219761c7b3d28317a800870f9e321a056226f8a75d939cf281c476a8e8.jpg)  
Fig. 1.3.1. Main Floor Layout of Building 7503 at 852-ft Elevation.

![](images/e0886d3860cff7df6b299decc0388d1cc0e1da97ba4de619cbae097a92ba96c6.jpg)  
Fig. 1.3.2. Main and Auxiliary Control Areas.

![](images/faa65c1ee8a877294f1a9099824a2306e8c92820dbbe0559d36d06f6e63ae000.jpg)  
Fig. 1.3.3. Main Control Board.

![](images/21c9482d0f4255918ab004f0628601dee119eda70b7bd02172c7ab7233c427c9.jpg)  
Fig. 1.3.4. Layout of Building 7503 at 840-ft Elevation.

![](images/2e5290bad761184949fa40d0e49d049d187e09c262fc431d4b1127aab21b9563.jpg)  
Fig. 1.3.5. Transmitter Room.

# 1.4 PLANT CONTROL SYSTEM

The MSRE and its control and instrumentation complex may be viewed as a primary reactor system which generates nuclear power and rejects heat to the atmosphere plus the collection of auxiliaries or subsystems required to run this primary system. This discussion of MSRE plant control is concerned with how the control system interconnects these various systems and how they are coupled to the reactor; it is little concerned with the reactor safety system. It is sufficient to point out that the safety-grade instruments are not used as operational controls and that every effort is made to keep the safety system instruments completely decoupled from the operational control equipment. The MSRE safety system, what it does, and why are discussed in Sect. 1.5.

It is appropriate to separate the various systems and equipment and their associated instruments and controls into categories, thus:

1. Those operator-controlled items which exert a direct and immediate influence on the state of the reactor; collectively these are the operator's "handle" which runs the MSRE.

2. Redundant, essential auxiliaries not in (l) which, should one unit malfunction, require immediate transfer switching by the operator if the redundancy is to be effective. Examples are the instrument air compressors and the component cooling pumps.

3. Vital monitoring and control instrumentation not subject to adjustment or control by the operator. These instruments produce off-limit alarms and control actions and provide continuous information as to the conditions in the monitored systems. Examples are the process radiation monitors, health-physics alarm instrumentation, safety system instruments, etc.

4. Nonredundant but essential auxiliaries which operate as self-contained devices. These instruments either require no control or are controlled locally and automatically. They are expected to operate continuously and unattended. An example is the 60-kva battery-powered solid-state ac power supply.

5. The remaining instruments whose effect on the reactor system is either peripheral and indirect or is further modified by the instrumentation in (1). Instruments used for chemical and physical analyses, for gathering experimental data, and for monitoring slow trends in noncritical areas of the system are in this group.

This grouping, or categorization, has been strongly implied by Sect. 1.3, which discusses plant instrumentation layout as it is related to the reactor operator's use of the instruments and controls. Figure 1.4.1 is a functional diagram of the instrumentation in and directly adjacent to the main control room. Generally, the diagram shows that the main control room instruments are composed principally of those in the first three groups, and the instrumentation on the operator's console is almost entirely in the first category.

There is a strong incentive to maintain continuous operation at the MSRE; therefore the plant and the instrumentation and control system are designed to minimize unscheduled total shutdowns caused by equipment failures and electrical power (TVA) interruptions. Critical operating auxiliaries such as instrument air compressors, water pumps, cooling blowers, etc., are redundant, and switchover to the spare unit

is accomplished at the main control board. Each lube oil package serving the salt loop pumps contains a spare oil pump. Transfer switching to the spare oil pump is automatic on loss of flow (pressure).

Electrical power interruptions are a leading cause of shutdown conditions. Design of the MSRE assumes that TVA-supplied electrical power will be interrupted several times a year by thunderstorms. Local emergency power from diesel generators is provided.<sup>1</sup> The diesels are started and stopped in the auxiliary control room just a few steps from the operator's console. Short-term power interruptions to the operating equipment will not produce a total system shutdown. This allows sufficient time for manually controlled diesel generator startup and necessary transfer switching. Total shutdown is defined to include a reactor drain, which produces a completely quiescent system incapable of achieving criticality. The design and operation of the reactor and its controls do not assume unperturbed operation with a loss of TVA power. In fact, if the reactor is at power, the rods and the load will scram, and it will not be possible to resume high-power operation until TVA power is restored. The procedure following a loss of TVA power is to restore criticality and operate at heat loss power until TVA power is again available.

The on-line reliability required by the instrument and control power system must meet more stringent requirements with respect to continuity. The operator's need for good information is never more acute than during abnormal conditions such as those produced by an interruption of TVA power. Safety systems and high-grade interlocks normally act toward shutdown when their power is lost, even momentarily. Therefore, the operation of essential plant controls and instruments does not depend on the normal TVA supply. The two-out-of-three redundancy extensively employed in the plant safety system is intended to eliminate such a dependency. The plant safety system and a typical example of three-channel redundant design are discussed in Sect. 2.5. Figure 1.4.2 is a simplified one-line diagram of the power system used for the instrumentation and controls.

This power distribution system will be thoroughly described in Sect. 4.13, but it is worth while to point out that:

1. The three-channel safety systems receive their power from three practically independent sources within the distribution system. Two of these are battery-powered and will not be affected by short-term interruptions of TVA power.   
2. The controls and information channels essential to continuous operation are battery-powered.

The control requirements of the MSRE differ, depending on whether or not the reactor loop is filled or empty and, if filled, on the amount of power being generated. These different requirements must be accommodated within the control system; that is, the interlocks which prohibit or permit in one operating regime must not prevent routine and

proper operation in another. Mode control, superimposed on the individual subsystem control channels, resolves this problem of accommodation. It does so by making all the subsystem alterations required for accommodation to operating regimes responsive to a single, manually operated control.

Figure 1.4.3 is a diagram of the fuel and coolant salt systems, showing the location of the instrumentation and controls which provide mode control. It can be seen from this figure that mode control in the MSRE is concerned with:

1. The location of the fuel salt and the flush salt, that is, whether in the drain tanks or the reactor loop. Note that the control system makes no distinction between fuel salt and flush salt. This is because reliable and certain sensors which differentiate between the two are not available.   
2. The ability to transfer salt among the drain tanks or to and from the reactor loop.   
3. The power (flux) being developed and the rate of change of power, both actual and potential.   
4. The operating integrity of important flux instruments used to monitor and control reactor power.

The scope of the mode control system is not extended to the auxiliaries, to the helium supply system, or to the off-gas system. Equipment or control system deficiencies and operating errors which affect these areas will be reflected, indirectly, to the mode control system or will become immediately apparent because of alarms and/or interlocks or by the action of the safety system. Furthermore, the operating restrictions imposed by the mode controls are more numerous during transitions from one operating mode to another as power is being increased. This limits the rate of change of power to reasonable values. After the new reactor mode has been established, many of these restrictions required to enter the mode are bypassed by relay seals.

Figures 1.4.4 and 1.4.5 are condensed block diagrams which indicate the function and purpose of the mode controls. The manually selected operating regimes have been designated as Off, Prefill, Operate, Operate-Start, and Operate-Run; a discussion of these follows:

1. Off. - The "Off" mode could be designated "Not in Prefill or in Operate" (see 2 and 3 below) without sacrificing accuracy. In "Off" the entire MSRE system is not inoperative but the reactor is shut down. When the reactor is "Off" the following conditions obtain:

a) rod withdrawal is prohibited,   
b) not in automatic load control,   
c) rod control servo is "Off,"   
d) prohibits opening of the helium valves used to fill the reactor vessel,   
e) prohibits raising the radiator doors by manual control, above the intermediate limit if reactor power is above 1 Mw,   
f) provides a control rod "Reverse" if the power (flux) exceeds 1.5 Mw or if the reactor period is less than 5 sec,

g) prevents starting the fuel and coolant salt pumps; if the pumps are running and the control system is switched to "Off" these pumps will continue to run because of seal contacts in the pump control circuits,   
h) "no thaw" - transfer freeze valves,   
i) "no thaw" - fill and drain freeze valves.   
2. Prefill. - Intended to establish the necessary and sufficient conditions required to precede a reactor start. During this period the reactor loop is empty so that helium may be circulated to establish uniform temperature conditions in the loop. Safety system checkouts are being conducted, and other routine and nonroutine operations involving maintenance and equipment verification may be under way. Salt transfers among the drain tanks, to the chemical processing plant, or to or from the fuel storage tank are permitted during Prefill. The primary requirement during Prefill operation is that the reactor loop be maintained empty. Prefill allows complete freedom in the use of the jumper board for testing and maintenance checks and, excepting the reactor fill restrictions, does not superimpose additional interlocked prohibitions on operating MSRE equipment.   
3. Operate. - This mode establishes certain conditions required to fill the reactor loop. Entering "Operate" requires that the transfer freeze valves between the fuel storage tank and the drain tanks be frozen and that at least one freeze valve between the reactor drain line and one of the fuel drain tanks be open.   
4. Operate-Start. - The Operate mode automatically becomes Operate-Start when the reactor loop is filled to the correct level and the reactor drain valve (FV-103) is frozen. This mode permits reactor start with power generation not exceeding 1.5 Mw provided the conditions for control-rod withdrawal, described in Sect. 2.6, have been established.   
5. Operate-Run. - This mode is obtained by manual selection when conditions requisite to high-power operation have been met. Operate-Run and Operate-Start are, by direct switching, mutually exclusive. Depending on whether or not the operator chooses to control the reactor automatically or manually, the requirements for going into the Operate-Run mode differ somewhat (see Fig. 1.4.5).

If the operator chooses to use the automatic rod controller or programmed load control, or both (see Sects. 2.6 and 2.8), certain initial conditions must be met which provide a smooth transition in reactor power generation as it becomes responsive to its load-following characteristics and as the rod servo assumes control. These initial conditions are as follows:

A. Using the Automatic Rod Controller

1. The demand signal computed by the automatic rod controller is asking for less than 1 Mw.   
2. The regulating rod is not being restricted in motion by its limit switches (see Sect. 2.6).

B. Using Programmed Load Control

1. The radiator doors are positioned so that power extraction is limited.   
2. The set-point signal which controls the radiator bypass damper, described in Sect. 2.8, is zero.

Entering the Operate-Run mode is subject to additional restrictions which are not contingent on the use of the automatic rod controller:

1. At least one main radiator blower must be on.   
2. The fuel salt pump must be operating (rpm > 1100).   
3. The range selectors in the linear power channels (Sect. 2.4) must be in the 1.5-Mw position.   
4. At least one wide-range counting channel must provide "confidence" and indicate that reactor power is above 0.5 Mw and that the reactor period is over 30 sec.

Once Operate-Run has been established, most of the requirements listed in the preceding paragraphs are bypassed by a seal, as shown in Fig. 1.4.5. When reactor power reaches 1 Mw the "confidence" interlock (Sect. 2.6) is bypassed and, insofar as the mode control circuitry is involved, the only requirement for continuing reactor operation in this mode is that the fuel salt pump be running, one main blower be on, the transfer freeze valves be frozen, at least one drain line freeze valve be thawed, and no safety system jumpers be used.

The data logger-computer, adjacent to the main control area, occupies a singular position in the hierarchy of MSRE instrument and control systems. It is added to the MSRE as an experiment intended to evaluate the merit of such devices in reactor systems. Therefore, the MSRE control system continues to operate whether or not the data logger is in service. Although no direct reactor system control functions are vested in the logger-computer, it is capable of exerting considerable influence on reactor system operations. This is because it provides the reactor operator with a large amount of current information on system status and gives alarms for off-limit conditions.

The available space in the main and auxiliary control areas restricted their use to instrumenting the functions shown in Fig. 1.4.1. It was necessary, and for no other reason, to obtain the additional space required for the remaining instrumentation by decentralization with local control systems. In many cases, and regardless of available space considerations, local control was a preferred choice for one or more of the following reasons:

1. it results in control loops which are less costly to build and are more reliable,   
2. it eliminates problems of data transmission or retransmission over long lines with consequent improvement in accuracy.   
3. it improves operation by locating the control system directly adjacent to the controlled equipment.

These decentralized controls, whose location has been discussed in Sect. 1.3, are in categories 4 and 5 (listed previously in this section) and are not needed continuously by the reactor operator. Monitoring by annunciation is augmented by scheduled, routine inspection (the "walking log") as required.

![](images/8a3cb305f16277624986d547d379d025bfade59ceabeecd64f649a99617f1c61.jpg)  
Fig. 1.4.1. Diagram of Instrumentation in and Directly Adjacent to the Main Control Room.

![](images/986550c34ffba8b2ebd091600a6c401fa417e6676bdb5265736c8e26d07109cf.jpg)

![](images/27bc19d0beb61aee1eaf3da71563985fe10f870a0a24b3d235ed8f4990c5f7e7.jpg)

![](images/33db0608f6c530d4b2a7ce85b59ea50d943a4edad9d53659108ffdd1823acf7c.jpg)

![](images/7139e568bb574ee386e4855bbdeb4f9b9d940295a045fe26ce3c43bfaf8b1319.jpg)  
Fig. 1.4.2. MSRE Instrument Power Distribution.

![](images/a8c432ea789147bbedd34f359414153c8ae9bdb994a52f7f884b3ed963071e8e.jpg)  
Fig. 1.4.3. MSRE Instruments and Instrument Signals for Mode Control.

![](images/fc8990202c3714974ff15205e988c717247908000fe6bc7a708a38184917339f.jpg)  
Fig. 1.4.4. MSRE Control System Modes.

![](images/f6a23e0c74db768811a0fe3d0f5fd2236841a4d794fa73e1aba34c479010dd66.jpg)

# 1.5 SAFETY SYSTEM

The MSRE safety system is composed of instrumentation which must be highly reliable because it augments the containment or protects vital and expensive equipment, or both. This section is confined to a broad, overall description of the reliable protective subsystems in the MSRE and the basic principles which guided their design.

Reliable protective systems for reactor installations have, in the past, been focused principally on the reactor core, and their operation has been centered on the behavior of the flux. In designing the MSRE the use of reliable protective instrumentation was not limited to protecting the reactor core from the immediate effects of excessive flux. It will be seen, as we review and describe the protective subsystems, that safety-grade instrumentation is extensively employed to enhance the primary and secondary containment and to ensure a reactor drain.

It is worth while to describe, briefly, some of the characteristics of the MSRE that are responsible for the safety-grade protective instrumentation with which it is provided.

1. The MSRE, being liquid-fueled, does not have fuel cladding as the first, unpenetrated containment barrier. The core vessel, heat exchanger, fuel salt storage tanks, and all interconnecting piping become the primary containment barrier to the molten salt. In addition, this primary containment is pierced by inlet and outlet lines carrying helium used for sweep gas across the pump bowl, for bubbler level instruments, and for drain tank pressurization. These lines violate the primary containment barrier unless they are reliably blocked.   
2. In common with solid-fueled reactors the MSRE uses conventional poison rods for control and safety. Analyses, $^{1-3}$ tests, and operating experience have shown that this reactor is a very docile and stable machine having a relatively long neutron lifetime, a large heat capacity, and an effective negative temperature coefficient of reactivity. All hypothetical nuclear excursions in the MSRE proceed slowly and do not develop high transient vapor pressures; undesirably high temperatures are the consequence.

The control rods are not capable of providing absolute reactor shutdown under all conditions. The shutdown worth in the rods, at reactor operating temperature, is lost because of the negative temperature coefficient if the fuel salt in the core vessel is cooled sufficiently.

Transference of fuel to the drain tanks is the certain method of obtaining absolute shutdown, and the ability to effect such a transfer (reactor drain) must be assured.

3. The chemistry of the fuel salt does not disallow segregation $^{4,5}$ of the different fluorides with a consequent increased concentration of uranium in one of the segregated phases. Segregated salt has been produced in the laboratory under very carefully controlled conditions. The accidental and undetected segregation of salt in a drain tank is highly improbable but has not been demonstrated to be incredible. Filling the reactor with segregated salt may produce a nuclear excursion during the filling operation which, ultimately, exceeds the limiting capacity of the control rods. Rigid, reliable control of the reactor filling operation is a necessity.

4. A temperature excursion will cause the fuel salt to expand faster than its containment. The volume available for such expansion is limited; therefore, it is essential to have rigid, reliable control of temperature and fuel salt level. See also No. 3 above.

5. Fuel and coolant salts freeze at temperatures in the region of 840 to $850^{\circ}\mathrm{F}$ . Freezing the salt is not harmful, but remelting is accompanied by expansion, which is capable of rupturing the piping. The coolant salt radiator is particularly vulnerable. Loss of the radiator would be costly and would be an intolerable setback to the MSR program. Reliable protective measures (see Sect. 2.8) are included in the MSRE.

Principles employed in achieving reliability in reactor safety systems have been applied extensively to the MSRE. These principles are summarized as follows:

1. Redundancy is employed so that no single failure of an instrument, component, or wiring having a reasonable probability of failure could cause system failure. A single failure could involve all conductors in a single conduit, all contacts of a switch, or, unless special barriers are provided, the entire contents of an enclosure.

2. Testing is employed, preferably on line and without disconnecting equipment or otherwise impairing the ability to protect during the test. Each channel is tested separately so as to disclose a failed component which would prevent protective action or a failure which could interconnect two otherwise independent channels and thereby destroy channel independence and redundancy.

3. Diversity is employed wherever feasible; that is, unlike channels are paired to accomplish a desired result. For example, a flow loss caused by stopping the coolant salt pump is detected by both the pump speed monitors and the flowmeters in the coolant salt piping.

4. Safety and control are separated so that loss of control resulting in an excursion will not occur simultaneously with loss of protection. Separation is also employed so that improvements intended to enhance control or other functions unrelated to safety will not be made, unwittingly, to the detriment of safety.

These precepts constitute recommended design practices for what are now thought to be the best safety systems we know how to build. Figure

1.5.1 shows an example of a three-channel, high-reliability subsystem in the MSRE. This is a simplified diagram of the instrumentation which closes the block valves in the instrument air lines to the secondary containment cell if the pressure in the cell rises above 2 psig. It is a representative example of a safety subsystem in the MSRE. The following description of its design and operation is included here to illustrate how these general precepts have been reduced to practice.

The instrumentation is simple; three high-grade pressure switches provide the switching contacts which operate the solenoid valves in the valve matrix. This matrix is arranged so that, if any two of the three pressure switches are actuated, the pneumatic actuators (diaphragms) of the block valves are vented to the atmosphere, the air supply to the valves is shut off, and the spring-loaded valves close and block the instrument air lines.

$^\mathrm{6S}$ H. Hanauer, "Design Precepts for Engineered Safeguards," Nucl. Safety 6(4), 408-11 (Summer 1965).   
7E. P. Epler, "Dangers in Safety Systems," IRE Trans. Nucl. Sci NS-8(4), 51-55 (October 1961).   
8S. H. Hansauer, "Instrumentation for Containment," Nucl. Safety 3(1), 41-46 (September 1961).   
9I. M. Jacobs, "Safety Systems for Nuclear Power Reactors," Trans. Am. Inst. Elec. Engrs., Pt. I, 76, 670-73 (November 1957).   
10S. J. Ditto, "Redundancy and Coincidence in Reactor Safety Systems," Nucl. Safety 2(4), 16-17 (June 1961); M. A. Schultz, "Reactor Safety Instrumentation," Nucl. Safety 4(2), 1-13 (December 1962).   
11C. G. Lennox, A. Pearson, and P. R. Tunnicliffe, Regulation and Protective System Design for Nuclear Reactors, AECL-1495 (April 1962).   
12I. M. Jacobs, "Safety System Technology," Nucl. Safety 6(3), 231-45 (Spring 1965).   
13S. J. Ditto, "Effect of Operating Experience on Safety System Design," Nucl. Safety 6(2), 183-84 (Winter 1964-1965).   
14E. P. Epler, "Reliability of Reactor Systems," Nucl. Safety 4(4), 72-76 (June 1963).   
15K. W. West, "Instrument System Testing for In-Pile Loops," Nucl. Safety 5(4), 374-76 (Summer 1963).   
16K. W. West, "Relative Functions of Loop Containment and Instrumentation," Nucl. Safety 4(4), 180-81 (June 1963).   
17S. J. Ditto, "Failures of Systems Designed for High Reliability," Nucl. Safety 8(1), 35-37 (Fall 1966).   
18E. P. Epler, "Safety System Reliability vs. Performance," Nucl. Safety 6(4), 411-14 (Summer 1965).

The two-out-of-three redundancy permits on-line testing without system perturbation. The completeness of the test procedure employed is an operational decision and is not limited by the design of the instrumentation. Testing is done by simulating an increase in cell pressure by using the nitrogen cylinder (Fig. 1.5.1) as the source of pressure and noting the response of the pressure gages in the valve matrix or, if desired, by actually closing the block valves. A typical test in channel A proceeds thus:

1. The hand valve in the line which connects the nitrogen cylinder to the line from PSS-RC-B to the reactor cell is opened, and the pressure is adjusted to the 2-psig set point. The sintered disk snubbers provide sufficient flow restriction to maintain this pressure without undue loss<sup>19</sup> of nitrogen to the reactor cell.

2. The increase in pressure actuates pressure switch PSS-RC-B and this, in turn, deenergizes solenoid valves ESV-1A1 and ESV-1A2.

3. These valves, ESV-1A1 and ESV-1A2, in the valve matrix change their aspect, but not so as to affect the pressure in the 80-psig air header; valve ESV-1A2 vents pressure gage PI-1A5. During normal operation pressure gages PI-1A1, PI-1A4, and PI-1A5 indicate header pressure, 80 psig. Pressure gage PI-1A5 will now go to zero. The block valves will be unaffected since there is still no open line or lines between the block valve operators and the vent line and because the connection between the 80-psig header and the valve operators is still maintained through ESV-1B2, ESV-1A1, ESV-1B1, and ESV-1C.

This test, steps 1 to 3 above, can be conducted with any channel and without disturbing reactor operation. It does not test the actual closure of the block valves. Now, suppose any two channels are tested coincidentally. For example, if channels 1 and 2 are tested simultaneously, solenoids ESV-1Al, ESV-1A2, ESV-1B1, and ESV-1B2 will be de-energized, and, referring to the valve matrix in Fig. 1.5.1, the block valve operators will be opened to atmospheric pressure through ESV-1C1 to ESV-1B1 to ESV-1C2 to ESV-1A1 to ESV-1B2 to vent. Valves ESV-1A1 and ESV-1B2 now prevent transmission of pressure from the 80-psig air supply to the block valve diaphragms, and the spring-loaded valves will close. Such a two-channel test checks operation of the entire system. Failure of any block valve to close can be detected by observing the response, or lack of response, of the in-cell instruments supplied via the block valve.

This same basic scheme is used for protection elsewhere in the MSRE. The protective instruments which close block valves in the inlet helium lines operate when the pressure in line 500 falls below 28 psig (see Figs. 1.5.7 and 1.5.2). In this situation, where protective action is initiated by an undue reduction in pressure, testing is accomplished

by venting the pressure switches to atmospheric pressure by opening an individual hand valve and, as above, by observing the response of the pressure gages in a valve matrix or the block valves themselves.

This same design is used for protecting against too great a reduction in reactor cell pressure below atmospheric (see input No. XII, Fig. 1.5.2). In this particular system the pressure switches are enclosed in boxes which are vented to atmospheric pressure through snubbers. Testing is accomplished by pressurizing the boxes. This increases the differential pressure across the pressure switches and thereby simulates a reduction of pressure within the cell.

It is worth while to examine this particular safety subsystem from the standpoint of the "recommended practices" previously cited. Up to but not including the output elements (block valves), redundancy and testing requirements are completely satisfied by the design. It should be pointed out that an on-line test of this particular subsystem which includes closing the instrument air line block valves is operationally intolerable. The addition of a second valve in each line would improve the reliability of the instrumented blocking system but, of course, would not improve the on-line testing situation. It was established while the MSRE was being designed that the closed system of instrument air lines, tanks, and compressors, with associated valves, etc., constituted the second effective containment barrier (see Sect. 1.5.4).

This particular system does not employ diverse channels in obtaining redundant input channels. In this particular case there is no suitable and reliable substitute for the simple, direct measurement of cell pressure as it is done. The use of diverse sources of control power substantially reduces the likelihood of spurious action caused by failed or faulty power sources.

The pressure switches are installed in the north electric service area and are within 10 ft of the cell wall. The piping to and from the switches is of autoclave tubing with autoclave fittings. The electrical interconnections are run in separate conduits, channel by channel, and contain no other wiring. The solenoid valve matrix is located in the north electric service area in a safety instrumentation cabinet.

As the MSRE design proceeded, a few situations and conditions developed which resulted in departures from the ideal recommended practices outlined previously in this section. Two examples, with reasons, follow:

1. All three of our safety system neutron sensors are located in a single penetration because both the amount of space and its configuration absolutely prohibit three separate penetrations at different locations (see Sect. 2.1).

2. In some cases the reliable instrumentation which automatically closes block valves closes only one valve in each line rather than two separate, independent valves in series. MSRE system design established a criterion that a single block valve in series with a pair of check valves was a necessary and sufficient alternate for two block valves in series (see, for instance, Sect. 4.8).

On-line testing of the "load scram" system (refer to Sect. 2.8) conflicts, seriously, with reactor operating schedules and will produce highly undesirable thermal transients. These, in turn, produce thermal stress cycles which reduce the life of the system. In order to test the door drive mechanism and the ability of the doors to scram when the reactor is down and the coolant system drained, it is necessary to bypass

the safety instruments that scam the doors since these same instruments prevent raising the doors to perform the test. This dilemma is solved by using the jumper board to bypass these safety instruments. The jumper board circuitry (refer to Sect. 4.11) is interlocked so that safety system bypassing is permitted only when the reactor is empty. Safety system jumpering is resorted to only when absolutely necessary and, where employed on the MSRE, was adopted only when no alternate method could be found. In this particular case the ability to test was retained by this compromise.

It is usual and obvious practice to operate relays, solenoids, temperature switches, etc., so that power losses cause them to change state toward safety;[20] e.g., safety system relays are operated "energized," and their contacts break circuits to produce the safety action. The relay contacts which stop the component cooling pump motors (see Sect. 1.5.5) must be closed to energize the battery-powered "Stop" trip coil in the motor starter. Motor starters, typically, operate this way, and it is not in the best interests of reliability to attempt to redesign or modify well-engineered, time-tested equipment of this type for reverse-mode operation. Furthermore, this particular safety action is diverse in that protection is also obtained by closing a valve (see outputs XI and XII, Fig. 1.5.2).

Because of the very strong incentive to keep the primary containment simple and structurally uncomplicated, the MSRE does not have a multiplicity of fuel salt drain lines, each with an individual drain valve, controlled by the safety system.

The foregoing is intended to provide a broad, overall view of the application of reliable, safety-grade instrumentation to the MSRE. Detailed descriptions of the design and operation of these reliable subsystems are contained either in the remainder of this section or elsewhere in this report and may be located by referring to the "Supplementary Information" column in Table 1.5.1, or the last column in Fig.

1.5.2. Much of the text which immediately follows is an updated version of similar material, now partially obsolete, originally presented in ORNL-TM-732 (ref. 1).

Figure 1.5.2 shows input-output diagrams of the MSRE protective instrument system. Figure 1.5.3 is an expanded signal flow diagram of the reactor drain instrumentation (described in Sect. 1.5.1), and Table 1.5.1 elaborates and augments the information in the figures. The more detailed descriptions which follow are referenced to the particular regions in the reactor system which are principally involved.

Table 1.5.1 (continued)   

<table><tr><td>Input Ref. No.</td><td>Condition or Situation Which Indicates a Real or Potential Hazard</td><td>Causes of the Hazard, the Consequences, and the Corrective Action</td><td>Supplementary Information</td></tr><tr><td>VII.</td><td>Helium pressure in the pump bowl greater than 25 psig</td><td>1. Causesa. Rapid unchecked expansion of fuel salt by excess temperature; see I and II above and Supplementary Informationb. Plugging of off-gas system2. Consequencesa. If unchecked, damage to pump seals, which are rated at 100 psig, and possible overstressing of primary loopb. Exceed capacity of off-gas system, with resulting threat to containmentc. Possible loss of primary containment3. Corrective actionsa. Drain reactor vesselb. Vent pump bowl to the auxiliary charcoal bed</td><td>1. System design provides 5.0 ft3of overflow capacity, and power level scram and fuel overflow tank level sys- tems (see I and IV, this table) protect against fuel salt expansion caused by power excursion; safety system holds bypass valves (Fig. 1.5.4) open during operation, in which case the pressure rise will be moderate until all the overflow volume is filled.2. Redundancy: Two pressure channels, one in the pump bowl and one in the overflow tank.3. Testing: Test procedure checks entire channel, with exception of transmitter bellows (see Fig. 1.5.5).4. Monitoring: Loss of helium flow to bubblers caused by either low inlet pressure or line blockage is alarmed.5. Safety only?: Yes6. Coincidence: Either of the two inputs will produce corrective action.7. Draining (see Figs. 1.5.2 and 1.5.4) ensures immediate opening of the bypass valves to back up administrative control. Venting to the auxiliary charcoal bed is less effective but useful backup.</td></tr><tr><td>VIII.</td><td>Helium pressure in the fuel pump bowl greater than "fill permit" valve</td><td>1. Causesa. Excess filling rate or overfill.b. Temperature excursion during fill (see II and III, this table)c. Closing of HCV-533A1 normally maintained open by administrative control, during the filling operation.2. ConsequencesNot of itself a hazard; a release of positive pressure may produce a sudden rise in fuel level during fill and, possibly, a nuclear excursion if the fuel salt is segregated. See VI, this table.3. Corrective actionDrain reactor vessel</td><td>This uses same instrumentation as VII (this table).1. Redundancy: Two channels are used; one in the pump bowl and the other in the overflow tank.2. Testing: See VII, this table.3. Monitoring: See VII, this table.4. Safety only?: Yes.5. Coincidence: Either of the two inputs will produce corrective action.</td></tr><tr><td>IX.</td><td>Excess radioactivity in reactor cell atmosphere</td><td>1. CausesRupture or leak in the primary containment2. ConsequencesContamination of secondary containment and increased possibility of contamination of area in the event that secondary containment fails.3. Corrective actiona. Drain reactor vesselb. Close cell evacuation valve which vents cooling air loop to the off-gas stack (valve No. HCV-565A1)c. Close HCV-915A1 which blocks cooling air line to rod drives and control rod thinniblesd. Close block valves in the lines to and from in-cell O2analyzere. Close block valves in steam dome condensate drain lines</td><td>1. Redundancy: Two independent channels.2. Testing: Complete testing of each channel is possible.3. Monitoring: Certain system failures produce alarms.4. Safety only?: Yes.5. Coincidence: Either of the two inputs will produce corrective action.</td></tr><tr><td>X.</td><td>Supply pressure less than 28 psig in helium line 500 which supplies helium to all reactor cell components, drain tank cell, and fuel processing system</td><td>1. CausesLoss of supply helium caused by:a. Empty tankb. Previous overpressure which operates relief valve and breaks rupture diskc. Malfunction of pressure-regulating valve PCV-500C (or alternately, PCV 605) which maintains supply at design-point value of 35 psig2. ConsequencesPossible loss of secondary containment (see 1b above)3. Corrective actionBlock all helium lines to reactor and fuel salt drain tank cells</td><td>1. Redundancy: Three independent channels.2. Testing: Complete testing possible.3. Monitoring: Testing meets requirements.4. Safety only?: Yes.5. Coincidence: Any two-out-of-three.6. Block helium lines to coolant salt system (pump bowl and drain tank)</td></tr><tr><td>XI.</td><td>High radiation activity in helium lines supplying fuel salt level bubblers or in dead-ended helium lines to zero psi, reference chambers connected to pressure transmitters</td><td>1. CausesReversal of flow in these lines (or back diffusion) from pump bowl, drain tanks, overflow tanks2. ConsequencesRadioactivity inside the helium piping in normally safe areas. This activity will be contained as long as piping is not breached.3. Corrective actionClose block valves in helium lines to fuel salt pump bowl and overflow tank.</td><td>1. Redundancy: Three independent channels.2. Testing: Complete testing of each channel is possible.3. Monitoring: Indicated, logged and alarmed.4. Safety only?: Yes.5. Coincidence: Any two-out-of-three.6. Flow rate, in either direction, is limited by capillaries; check valves, two in series, are used to back up block valves. The capillaries provide a long flow path at high velocity and hence reduce back diffusion.</td></tr><tr><td>XII.</td><td>Pressure in secondary containment less than 10.7 psia.</td><td>1. Causesa. Malfunction of the secondary containment pressure control system which results in excessive pump-down of the secondary containmentb. Misoperation of pumps and coolers during non-routine tests and equipment checkouts.2. ConsequencesPossible collapse of the secondary containment because of excessive external pressure3. Corrective actiona. Close cell evacuation valve, HCV-565A1, in the line which is used to evacuate secondary containment to maintain pressure at 12.7 psia.b. Shut off both component pumps.</td><td>1. Redundancy: Three independent channels.2. Testing: Complete testing of each channel is possible.3. Monitoring: Not applicable.4. Safety only?: Yes.5. Coincidence: Either of two will initiate safety action.6. Pressure in the secondary containment is normally maintained approximately 2 psi below atmospheric (12.7 psia)7. The blowers are of the positive displacement type and are, therefore, capable of reducing the pressure well below the value which endangers the containment vessel.</td></tr><tr><td>XIII.</td><td>Pressure in the secondary containment greater than two (2) psig.</td><td>1. Causesa. A rupture or leak in the primary containment which allows hot fuel salt to mix with water in the secondary containment; in the worst version this is the maximum credible accident.2. A malfunction in or misoperation of the pressure control system2. ConsequencesNot, of itself, a direct hazard; during normal operation the reactor cell is maintained at a negative pressure of -2 psig (12.7 psia) to ensure inflow in the event of a leak; the existence of positive pressure is evidence that a malfunction or misoperation exists; a loss of secondary containment is a possible result.3. Corrective actiona. Close instrument air block valvesb. Close liquid waste system block valves from reactor cell sump and drain tank cell sump to waste tank.c. Close block valves to and from in-cell oxygen analyzerd. Close block valves to and from off-gas samplere. Close block valves in lines to the hook gage used for cell tank rate checksf. Close steam dome condensate drain valves</td><td>1. Redundancy: Three independent channels.2. Testing: Complete testing is possible.3. Monitoring: Indicated, logged and alarmed.4. Safety only?: Yes5. Coincidence: Any two-out-of-three.</td></tr><tr><td>XIV.</td><td>High radioactivity in the ventilation line from off-gas sampler enclosure</td><td>1. Causes 
Leak in the off-gas sampler 
2. Consequences 
This is a loss of primary containment 
3. Corrective action 
Close block valves in lines to and from the off-gas sampler</td><td>1. Redundancy: Two independent channels. 
2. Testing: Complete testing is possible. 
3. Monitoring: Indicated, logged and alarmed. 
4. Safety only?: Yes. 
5. Coincidence: Either of two inputs will initiate safety action.</td></tr><tr><td>XV.</td><td>Helium pressure in fuel salt pump bowl greater than ten (10) psig.</td><td>1. Causes 
a. Same as VII, this table. 
b. Clogging of off-gas system during normal operation requiring operation at higher than usual pump bowl pressure 
c. Blowback as an operational procedure to open clogged off-gas system (see b above) 
2. Consequences 
This value of pressure, 10 psig, will not endanger reactor system. This interlock to protect the off-gas sampler and guard against a loss of containment 
3. Corrective action 
a. Close block valves in off-gas lines to and from the off-gas sampler 
b. Prevents opening operational and maintenance valves in fuel salt sampler-enricher (maintains containment)</td><td>1. Redundancy: Two independent channels. 
2. Testing: Complete testing of each channel is possible. 
3. Monitoring: Certain system failures produce alarms. Pressure is indicated and logged. 
4. Safety only?: Yes. 
5. Coincidence: Either of two channels will initiate safety action. 
6. The maximum pressure rating (rupture) of some components in the sampler is less than the 150% of maximum pressure (75 psig) normally required for primary containment components.</td></tr><tr><td>XVI.</td><td>High radiation activity in line No. 557 carrying off-gas from all charcoal beds and from the coolant pump, and from the lube oil systems</td><td>1. Causes 
a. Charcoal beds not operating correctly (overloaded, see III above) or pump seal failure allowing discharge of activity to lube-oil system 
b. Activity in the coolant salt loop; see also V, this table. 
2. Consequences 
Radioactive gases discharged up stack 
3. Corrective action 
a. Close off-gas block valve 
b. Close lube-oil systems vent valves</td><td>1. Redundancy: Two independent channels. 
2. Testing: Complete testing possible. 
3. Monitoring: Certain system failures are alarmed, radiation level is indicated and logged. 
4. Safety only?: Yes. 
5. Coincidence: Either of two channels will initiate safety action</td></tr><tr><td>XVII.</td><td>High radiation activity in in-cell treated water system</td><td>1. Causes 
a. Maximum credible accident with coincident rupture of in-cell water system piping 
b. Induced activity in treated water. 
2. Consequences 
a. Local contamination by radioactive water leak 
b. Loss of secondary containment, with accompanying contamination if radioactive material is discharged from the treated water system 
3. Corrective action 
a. Closes block valves in water lines which are extensions of the second-ary containment and which are outside the containment cell 
b. Closes valve in degassing tank vent which is located outside of secondary containment cell</td><td>1. Redundancy: Three independent channels. 
2. Testing: Complete testing of each channel is possible. 
3. Monitoring: Certain system failures initiate alarms. Radiation level is indicated and logged. 
4. Safety only?: Yes. 
5. Coincidence: Either of two channels will initiate safety action. 
6. The water lines and vent tank are extensions of the secondary containment..</td></tr><tr><td>XVIII.</td><td>Low temperature of coolant salt in outlet from radiator (line 202)</td><td>1. Causesa. Malfunction of load control system (complex of doors, blowers, and bypass damper)b. Cessation of power generation in core from any cause (scram, drain, rupture in primary containment, etc.)c. Loss of coolant flow (see XIX, this table)2. ConsequencesNo hazard; warns that potential radiator freezeup may be developing (see XIX, this table)3. Corrective actiona. Close radiator doorsb. Shut down main blowers, MB-1 and MB-3c. Drain coolant salt system</td><td>1. Redundancy: Three independent channels.2. Testing: A complete test of each input channel is possible; complete testing requires dropping doors, which disturbs operation.Monitoring: Thermocouple break or detachment from pipe will produce safety action in that channel. Temperature is indicated and logged.4. Safety only? Input channels used solely for safety.5. Coincidence: Any two-out-of-three.6. The corrective actions constitute a "load scram."</td></tr><tr><td>XIX.</td><td>Loss of coolant salt flow</td><td>1. Causesa. Coolant pump stoppageb. Line breakc. Unscheduled coolant salt draind. Plug in line or radiator2. ConsequencesUnless accompanied by undetected contamination of the coolant salt, see V, this table, no hazard exists. Unless action is taken a costly radiator freezeup will ensue.3. Corrective actiona. Close radiator doorsb. Shut down main blowers, MB-1 and MB-3</td><td>1. Redundancy: Two direct flow channels which receive information from a common primary element, a venturi, plus two independent pump speed channels.2. Testing: Partial testing possible; a test which includes dropping radiator doors will perturb operation; input elements not tested.3. Monitoring: By surveillance and comparison; flow and pump speed are indicated and logged.4. Safety only? Yes.5. Coincidence: Refer to Section 2.8.6. These corrective actions constitute a "load scram"; refer to Section 2.8.</td></tr><tr><td>XX.</td><td>Either or both doors at final upper limit</td><td>1. CausesFailure of first upper limit switches and/or any circuit or circuit element associated with these switches2. Consequencesa. Damage to the doorsb. Damage to the drive mechanismc. Loss of ability to scream the doors because of cable snarling or other damage per 2a and 2b above.3. Corrective actionsa. Stops door drive motorb. Disengages clutches in drive train between motor and cable sheavec. Applies brakes</td><td>1. Redundancy: Two independent limit switch channels which are cross connected so that if either door is at the final upper limit both doors are stopped. See also XIX, this table. Only one motor starter; it must work.2. Testing: Complete testing is possible at some inconvenience.3. Monitoring: Not applicable.4. Safety only? Yes.5. Coincidence: See (1) above.</td></tr><tr><td>XXI.</td><td>Door drive motor current at overload value</td><td>1. Causesa. Anything which jams the doors or the drive mechanismb. A failure of both first and final upper limit switches and/or any circuit or any circuit element associated with these switches2. ConsequencesSame as for XX, this table.3. Corrective actionSame as for XX, this table.</td><td>1. Redundancy: Only one primary element, the overcurrent relay. Otherwise this interlock is composed of two (2) separate channels. See XX, this table, and (5) below.2. Testing: During shutdown only.3. Monitoring: Not applicable.4. Safety only? Yes.5. a. Insofar as preventing damage caused by forcing the door and drive mechanism against the hard, fixed upper limit, this interlock provides diverse redundancy with the final upper limit interlock, XX, this table.b. Prevention of damage at other door positions than the final upper limits depends on the reliability of a single overcurrent relay and the reliability of a single motor starter-relay.</td></tr></table>

# 1.5.1 Reactor Fill and Drain System

A simplified diagram is shown in Fig. 1.5.4 of the reactor vessel, the drain tanks, the interconnecting piping, and the control elements required to fill and drain the reactor system with fuel salt in a safe, orderly way. The control rods are essential to a safe filling procedure but are omitted from this diagram in the interest of simplification.

The reactor is filled by applying helium pressure to the gas space in the selected drain tank and forcing the molten fuel salt up and into the core vessel. As a typical example, if the reactor is to be filled from fuel drain tank 1 (FDT-1), pressurizing helium is admitted via lines 517 and 572 (see Fig. 1.5.4). The filling pressure is controlled by pressure-regulating valve PCV-517-Al. The pressure setting of this valve is controlled by the operator. The upstream capillary flow restrictor in line 517 limits the maximum inlet flow rate of pressurizing helium. Valves HCV-544-Al and HCV-573-Al in the pipes which connect the gas space in FDT-1 to the pump bowl and to the charcoal beds are closed. Since the net pressure head available to produce flow decreases as the fuel level rises in the core vessel, the fill rate becomes progressively slower as the fill proceeds if constant inlet helium pressure is maintained and if the pump bowl pressure remains constant.

Helium pressure in the pump bowl is the second component of the differential pressure that drives fuel salt into the core vessel. A sudden reduction in pump bowl pressure during the reactor filling operation would cause an unscheduled rise in salt level in the core. If, at this time, the reactor is on the verge of becoming critical, an unexpected nuclear excursion cannot be ruled out. The safeguard provided is to allow filling only when the positive pressure in the pump bowl is equal to or less than +2 psig and thus keep the maximum possible increase in net filling pressure within safe limits. Two causes for a sudden decrease in pump bowl pressure are considered. First, opening valve HCV-533-A1 after reactor filling has started would vent the pump bowl to the auxiliary charcoal beds, which normally operate at close to atmospheric pressure. The resultant pressure change in the pump bowl would be -2 psi. Administrative control is used to maintain HCV-533-A1 open just before and during filling. Second, a rupture or leak would allow the escape of pump bowl helium to the reactor cell atmosphere, which is held at -2 psig (12.7 psia). This condition would cause a maximum pressure decrease in the pump bowl of 4 psi. If the fuel pump bowl pressure exceeds 2 psig, the safety equipment (1) initiates a drain by opening by-pass valves HCV-544-A1, HCV-545-A1, and HCV-546-A1, thereby equalizing helium pressure in the drain tanks and pump bowl, and (2) shuts off the supply of pressurizing helium by closing valves PCV-517-A1, HCV-572-A2, HCV-574-A1, and HCV-576-A1. This is the helium valve condition shown in Fig. 1.5.4 and is required by normal operation with the pump bowl at 5 psig; therefore, the 2-psig channel need not be disabled during normal operation. Additional safety considerations involving pressure in the fuel salt system and the instrumentation used for measuring helium pressures are discussed in the following section.

Excessive pressure, 25 psig, in the pump bowl is relieved by opening HCV-533-A1. During reactor operation, with the bypass lines open, one or more of the drain tanks would be subjected to this pressure. The input signal used to open HCV-533-A1 originates in either of a redundant pair

of pressure transmitters, PT-592B and PT-589B, on inlet lines to the pump bowl and overflow tank respectively. These same input channels provide the +2-psig safety signal discussed above.

As a further safeguard during filling, the safety system requires that all three control rods be partially withdrawn in order to pressurize the drain tanks. The weigh cells on the drain tanks provide information used to monitor the total amount of fuel salt moved into the core vessel.

The possible filling accidents are discussed in ref. 1. Briefly, these accidents are (1) premature criticality during filling caused by an overly high concentration of uranium brought about by selective freezing[21,22] in the drain tank; (2) premature criticality during filling of low-temperature $(900^{\circ}\mathrm{F})$ fuel salt of normal concentration, whose normal critical temperature with the rods withdrawn approximately half stroke is $1200^{\circ}\mathrm{F}$ ; and (3) premature criticality during filling of normal fuel salt at normal temperature with all control rods fully withdrawn. Protective action is the same for all three cases: the control rods are scrambled, and the reactor vessel is drained to ensure permanent shutdown. Rod scram is produced and vent valves HCV-573-Al, HCV-575-Al, and HCV-577-Al are opened by the excess flux signal. Since a premature criticality occurs before loop circulation is attained, the outlet temperature sensors are ineffective. The safety system also invokes a recalcator emergency drain to enhance containment if there is evidence that radioactivity is escaping from the primary fuel loop. These subsystems are covered subsequently in this section.

Emergency drainage is effected by the following actions (see Fig. 1.5.4):

1. The freeze valve in line 103, which connects the reactor drain tanks, is thawed. Thawing is accomplished by closing valves HCV-919A and 919B, a redundant pair, to stop the flow of cooling air. The system is designed with a heat capacity sufficient to thaw the plug in less than 15 min.   
2. The helium pressures in the fuel drain tank and the unfilled portion of the fuel salt loop are equalized by opening bypass valves HCV-544-Al, HCV-545-Al, and HCV-546-Al.   
3. Vent valves HCV-573-Al, HCV-575-Al, and HCV-577-Al, which release pressurizing helium in the drain tank to the off-gas system, are opened.   
4. Pressure regulating valve PCV-517-A1 in line 517, the inlet header that supplies pressurizing helium to all the drain tanks, is closed and shuts off the supply of pressurizing helium.   
5. The drain tank pressurizing valves, HCV-572-Al, HCV-574-Al, and HCV-576-Al, in the helium supply lines are also closed to halt further addition of fuel salt.

Actions 2 or 3 are immediately and independently effective in reversing a fill, and hence the valves are redundant. Similarly, PCV-517-

Al and the individual pressurizing valves, referred to in 4 and 5 above, form series pairs and provide redundancy. For example, it can be seen from Fig. 1.5.4 that, taking fuel drain tank No. 1 as typical, pressure equalization and venting are accomplished by opening HCV-544-Al and HCV-573-Al respectively. Administrative control is used to ensure that when the reactor is filled with fuel salt, both drain tanks, FDT-1 and FDT-2, are empty and both of the freeze valves, FV-106 and FV-105, are thawed. The tank condition is monitored by reference to the weigh cell and level instrumentation on each tank.

# 1.5.2 Helium Pressure Measurements in the Fuel Salt Loop

One channel of the instrumentation which measures helium pressure in the fuel pump bowl and the overflow tank is shown in Fig. 1.5.5. The components and their installation are designed to meet containment requirements.

The pressure transmitters are installed just outside the main secondary containment shell. From the standpoint of containment, the transmitter housings are "blisters" on the main containment cells. Containment criteria would be satisfied by

1. venting the reference pressure side of the transmitter diaphragms to the inside of the containment cell,   
2. sealing the vent port at the transmitter,   
3. connecting the transmitter's vent port to a containment-grade volume which is maintained at a known and constant pressure.

If the transmitter's reference pressure port is vented to the containment cell, the pressure measurement includes cell pressure. This pressure is controlled nominally at -2.0 psig during operation, is at atmospheric pressure during in-cell maintenance, and is well above atmospheric pressure during periodic checks to verify the containment capability of the cell. The normal and acceptable fluctuations around the nominal -2.0-psig value would reduce the accuracy of the transmitted measurement by an unacceptable amount. If the reference port of the transmitter is merely sealed shut, the reference pressure and hence the transmitted pressure would fluctuate with temperature changes in the sealed reference volume in the transmitter. Evacuating the reference side of the transmitter was deemed unacceptable because these vital measurements would then rely entirely on the long-term reliability of the vacuum.

The variable-volume reference chamber (see action 3 above) resolves these conflicting demands of containment and measurement accuracy. Conceptually, it acts as a strong but extremely compliant bag which automatically adjusts its volume to maintain an internal pressure very nearly equal to the externally applied pressure. By connecting the reference ports of the transmitters to these reference chambers which are located outside the containment cells, the dual requirements of the containment and measurement accuracy are satisfied. At the MSRE the reference volume is housed, and the housing is vented to the off-gas duct near the blower inlet. During operation the ambient pressure in the off-gas duct is approximately -2.0 in. $\mathrm{H}_2\mathrm{O}$ , the blower inlet pressure. This -2.0-in. $\mathrm{H}_2\mathrm{O}$ offset is not significant. The reference

chamber is shown in diagram in Fig. 1.5.5 and is described in detail in Sect. 6.2.

Two channels are used, one in the pump bowl and the other in the overflow tank. These normally operate at the same pressure. Any safety signal from either channel initiates the appropriate safety action.

The system may be tested periodically during reactor operation by: (1) observing system response to small operator-induced pressure changes and (2) shunting the torque motor in the pressure transmitter. These tests will establish that, in the channel undergoing test, the lines from the pump bowl (or overflow tank) are clear and the electronic equipment and associated wiring are capable of operating the output relays.

Since it takes from 10 to 15 min to thaw drain valve FV-103, this time can be used to observe the response of the thermocouples on the freeze valve as it heats up but before actual salt flow begins. The valve can then be refrozen before an actual drain is initiated. In such a test, valve HCV-533 (Fig. 1.5.4) will be opened, and the controlled pressure (5 psig) in the pump bowl will be lost for the duration of the test. The response of HCV-533 can be noted by observing the actuation of the position switch on the valve stem. This test procedure checks the entire safety channel, except the ability of the transmitter measuring bellows and the associated linkage to transmit the pressure.

Monitoring of these channels is accomplished by indicating and alarming the pressure downstream from the hand throttling valves in each helium line serving the primary elements (the bubbler tubes) in the pump bowl and in the overflow tank. A downstream flow stoppage by a blocked line is indicated by a high-pressure alarm; low flow caused by a loss of upstream (supply) pressure, an upstream blockage by foreign matter, or a hand valve closure is indicated by a low-pressure alarm.

The fuel level in the overflow tank is measured by the differential pressure across the helium bubbler probe which dips into the fuel salt in the tank. The design criteria for testing and monitoring these differential pressure measuring channels are the same as those which guided the design of the pressure channels described in the preceding paragraphs. The reference chamber is not required. Two channels are employed for safety, and either will initiate a reactor drain if the fuel salt level in the overflow tank exceeds $20\%$ of full-scale level indication.

# 1.5.3 Afterheat Removal System

The drain tank afterheat removal system, typically the same for both drain tanks, is shown in Fig. 1.5.6. Once placed in operation the evaporative cooling system is designed to be self-regulating and to operate without external control. Reliable operation of the afterheat removal system requires (1) that the feedwater tanks contain a supply of cooling water, (2) that an ample supply of cooling water is available to the condensers, (3) that the system includes reliable valves to admit feed-water to the steam drums, and (4) that reliable block valves be provided

in the drain lines $^{23}$ from the steam drums. Administrative control is relied on to ensure that the feedwater tanks contain water. Valve ESV-806 opens to admit water automatically to the steam drum when the salt temperature in the drain tank exceeds $1300^{\circ}\mathrm{F}$ and recloses at approximately $1200^{\circ}\mathrm{F}$ . This valve is in parallel with manual valve ICV-806A, and the pair are a redundant means of admitting water to the steam drum. Normally the condensers are cooled by tower cooling water, but diversion valve HCV-882-C1 provides an alternate supply of water. Loss of tower water pressure caused by a loss of water or pump shutdown is detected by pressure switch PS-851-B1, which operates diversion valve HCV-882-C1. When this valve operates, the cooling water supply is shifted from the tower to the process water main.

Since it takes over 12 hr for excessively high afterheat temperatures to develop after a drain, there is sufficient time to effect a transfer to the other drain tank in the event of a failure or malfunction. This is also ample time to make connections from the cooling water system to a tank truck in the event that the normal water supply is inoperative.

The drain lines, 806-2 and 807-2, are used to keep the tanks dry during normal operation. They are extensions of the secondary containment and are provided with block valves. Reliable, safety-grade control instrumentation closes valves ESV-806-2A and 806-2B, a redundant pair, when the reactor cell pressure exceeds +2.0 psig or when the radiation monitors, RM-565A and B, in the cell evacuation line indicate excessive radioactivity in the cell atmosphere.

# 1.5.4 Containment System Instrumentation

Containment requirements are met by providing at least two independent, reliable barriers, in series, between the interior of the primary system and the atmosphere. For example, the two-barrier concept is fulfilled by:

1. two independent, reliable, controlled block valves with independent instrumentation,   
2. one controlled block valve plus a restriction such as a charcoal bed which will limit the escape of activity to the stack to less than the maximum permissible concentration,   
3. one controlled block valve plus two check valves,   
4. two solid barriers (vessel or pipe walls),   
5. one solid barrier and one controlled block valve,   
6. one solid barrier and one check valve.

The recommended design practices outlined previously in this section apply to the reliable instrumentation and control equipment used to operate the block valves. Block valves, generally, are not located at such a distance from the containment penetration that the lines become tenuous extensions of the containment vessel. Valves and other devices used in lieu of solid barriers will be routinely tested and demonstrated to be capable of maintaining leakage below the specified tolerance when closed.

# 1.5.4.1 Helium Supply Block Valves

Figure 1.5.7 shows the helium supply lines to the primary containment vessel and the associated valves used for control and blocking these supply lines against the escape of radioactivity from the primary system as a result of reverse flow or back diffusion. This sketch does not show the fuel storage tank (FST) and line 530, which supplies pressurizing helium to this tank. This line is blocked by HCV-530-Al. Two types of input signals are used to initiate helium supply block valve closure. The first, a reduction in the supply pressure from its normal value of 40 psig to 28 psig, actuates pressure switches and closes all the inlet helium block valves. The second, excess radiation measured by RM-596A, B, and C in any of the helium lines supplying the level probes (bubblers) and pressure measuring instruments in the pump bowl and overflow tank, closes the block valves in these lines. A reduction in helium supply pressure in line 500 from its regulated value of 40 psig indicates a leaky rupture disk or leaky piping and, possibly, a loss of primary containment.

In-service testing of the loss-of-pressure channels is accomplished by opening the hand valves on the lines to the pressure switches on the main supply pipe (line 500), one at a time, and observing the action of the relays in the two-out-of-three coincidence matrix in the control room. Actual block valve closure is not tested with this procedure. Low- and high-pressure alarms are provided on line 500; these will actuate before the safety system pressure switches close the block valves. Additional testing of the solenoid block valves in the helium bubbler lines is provided by closing each valve individually and observing the pressure change downstream of the hand throttling valve.

The three radiation monitoring safety input channels, RM-596A, B, and C, are tested by exposing each individual radiation element to a source and noting the response of the output relays which produce valve closure. Since two-out-of-three coincidence is used, this test will not perturb the system; neither does it provide a valve closure test.

# 1.5.4.2 Off-Gas System Monitoring

The off-gas system (Fig. 1.5.8) is monitored for excess radiation in four places:

1. Line 557. - This line receives off-gas from the main and auxiliary charcoal beds, helium from the coolant salt pump, and helium from the salt pump lube oil systems and the sampler-enricher.   
2. Line 528. - This line carries helium from the coolant salt circulating pump. Its primary purpose is to detect an internal leak in the fuel-to-coolant-salt heat exchanger. Should such a leak occur,

fission product activity will be carried into line 560 by the purgeegas flow across the coolant salt pump bowl. This line is monitored by RM-528B and C. Note that RM-557A and B provide a redundant indication of this activity level.

3. Line 565. - This line is used to pump the reactor and drain tank cells down to the operating pressure of 12.7 psia. A portion of this line continuously carries a small flow of cell air, via bypass line 566, across the component cooling pumps which circulate cell air (see Fig. 1.5.8). This continuous flow is monitored by RM-565A and B.   
4. Off-Gas Stack. - Stack gas monitoring is not a part of the MSRE safety system but is noted here for completeness. Refer to Sect. 2.11 for a description of this monitor. Its only output function is to provide alarms. The stack gas monitor, located on the off-gas stack, provides a final check on the off-gas just before it is discharged to the atmosphere and after it has been filtered. Excess radio-activity in the stack gas is alarmed in the MSRE control room, and an alarm signal is also transmitted to the ORNL Central Monitoring Facility.

It can be seen from Figs. 1.5.8 and 1.5.2 that an excess radioactivity signal from either RM-557A or B produces three output actions, all intended to preserve containment; these are as follows:

1. Closes HCV-557-C1 in line 557. This line is, in effect, the main helium off-gas exhaust header leading to the off-gas stack filters and carries off-gas from several sources, namely:

a) the fuel salt circulating pump,   
b) the fuel salt drain tanks,   
c) the coolant salt pump,   
d) the coolant salt drain tanks,   
e) the fuel salt sampler-enricher,   
f) the fuel and coolant salt pump lube oil systems (Fig. 1.5.9).

2. Closes valve PCV-510-A2.   
3. Closes valve PCV-513-A2.

Actions 2 and 3 block the helium off-gas lines from the lube oil systems (Fig. 1.5.9).

Radiation monitors RM-528B and C in line 528, carrying helium from the coolant pump, are necessary because they will provide an indication if a leak exists in the salt-to-salt heat exchanger (from the fuel salt loop to the coolant salt loop). Such a leak could put fission products in the coolant salt; however, when the coolant salt circulating pump is running, the coolant salt pressure in the heat exchanger tubes is greater than the fuel salt pressure in the shell. The fission product gases would be carried from the free surface in the coolant salt pump bowl into line 528. This activity will be read first by RM-528B and C and then by RM-557A and B. The output actions produced by RM-528B or C (see also Fig. 1.5.2 and Table 1.5.1) are the following: (1) drain the reactor vessel,

and (2) stop the fuel salt pump.[24] This also produces a rod scram if the reactor is operating above heat loss power, $15\mathrm{kw}$ . The sequence of control actions which scram the rods is described in Sect. 2.6.

Excess radioactivity in either the reactor or the drain tank cells is detected by RM-565A or B. Either monitor will produce protective actions thus:

1. Closes HCV-565-Al in line 565. This line, the cell evacuation line (Fig. 1.5.8), is used to exhaust the reactor and drain tank cells when they are being pumped down to their operating pressure of 12.7 psia.   
2. Closes the steam dome condensate drain valves ESV-806-2A and ESV-806-2B (see Fig. 1.5.6).   
3. Closes block valves HCV-566-A1, A2, A3, and A4 to and from the analyzer which monitors the oxygen content of the in-cell atmosphere. This analyzer (Fig. 1.5.12), is located in the vent house.   
4. Closes block valve HCV-915-Al, which carries exhaust cooling air to the rod drives and the control rod thimbles (see Fig. 2.7.12 in Sect. 2.7).   
5. Drains the reactor vessel. The reactor drain system is described in Sect. 4.7.

These systems may be tested by inserting a radiation source in the radiation monitor shields and observing (1) the radiation-monitor indicator, (2) the control circuit relays, and (3) the output actions of the control valves and other controlled elements which provide protection. The three pairs of radiation monitors, RM-528B and C, RM-557A and B, and RM-565A and B, all operate so that an excess radiation signal from either channel in a pair will produce safety action.

Since these are all one-out-of-two systems, on-line testing of any channel will produce protective control actions and, to an extent, perturb the operating system. The system disturbances caused by on-line testing of RM-557A and B and RM-565A and B can be tolerated if the test is of short duration. It was necessary to provide jumpers for on-line testing of RM-528B and C. Without jumpering, a test of either channel will stop the fuel salt pump and, if the reactor is at power, scram the rods. This is unacceptable operationally. Jumpering is the preferred alternative to omitting in-service testing. Testing these safety channels is, therefore, subject to very strict administrative control. The jumpers bypass contacts K-26C and K-27C in circuit 147, which starts and stops the fuel salt pump. As has been pointed out in footnote 24, these contacts do not produce a safety-grade protective action.

The MSRE off-gas sampler will (1) utilize on-line instruments to provide a semicontinuous indication of contaminant level and (2) isolate samples which may be transferred to a hot cell for analysis. The off-gas sampler (Fig. 1.5.10) was designed and installed after the re

actor was placed in operation. Reference 25 contains a brief, conceptual description of the sampler as originally proposed. In the current version the chromatograph cell has been omitted pending further development work. Figure 1.5.8 shows the location of the sampler with respect to the main off-gas system.

The samples are obtained from line 522, which carries fuel pump bowl sweep gas to the off-gas system. Bypass lines with valves across the piping to and from the analyzer permit taking the sample either before or after the gas has passed through the charcoal filter and the particle trap. The sampler is located in the trench immediately south of the vent house. The reactor off-gas is highly radioactive, and since this equipment is an extension of the primary containment into an area frequented by operating personnel, the use of block valves in the supply and return piping to the sampler is mandatory. The sampler is well shielded and, except perhaps for the thermal conductivity cells (these cells are tested at 20 psig), meets the general MSRE containment requirements with respect to pressure rating and leak-tightness. The sampler is housed in a ventilated enclosure which is exhausted to the off-gas stack. Continuous circulation within the enclosure is maintained by two (for redundancy) blowers. This flow loop is monitored by two flow switches, FS-54-D and FS-54-C, connected to a single alarm. Excess radioactivity in this circulating air is detected by two separate, independent channels of radiation detection equipment, RM-54A and RM-54B. A high-radiation signal from either monitor will close block valves ESV-537A and B and ESV-538A and B, redundant pairs in the inlet and outlet lines to and from the sampler. The circuits which control these valves are shown in Fig. 1.5.11. These valves are also closed (see output XVI, Fig. 1.5.2) if the pressure in the reactor and drain tank secondary containment cells rises above +2.0 psig or if the fuel pump bowl pressure exceeds 10 psig. The cell pressure safety channels and the protective instrumentation used to measure pump bowl pressures were described earlier in this section.

The atmosphere in the MSRE containment is kept at no more than $5\%$ oxygen, with the remainder being nitrogen. Oxygen content is continuously monitored by an on-line analyzer which measures the magnetic susceptibility of the cell atmosphere. The analyzer and its operation are described in detail in Sect. 6.4.

Figure 1.5.12 shows the analyzer flowsheet and the final control circuitry which closes the block valves to and from the analyzer. The inlet gas to the analyzer is taken from the cell evacuation line, 565, and is discharged to line 566. These two lines form a low-flow bypass loop across the component cooling pumps which continuously circulate the air within the containment cells. The piping to and from the analyzer meets containment requirements; the analyzer, rated at 30 psig, does not. Block valves are required for containment and because the instrument is located in an accessible, frequently used area and is not entirely protected from mechanical damage. The block valves also permit maintenance and routine operations such as changing the cylinders of reference gas and purge nitrogen.

Block valve operation is apparent from Fig. 1.5.12. The valves are automatically closed if either channel, RM-565B or C, in the two-channel radiation monitor, signals excess radioactivity in the cell atmosphere or if the pressure in the secondary containment cell exceeds +2.0 psig. These input channels have been described previously in this section. Complete on-line testing is possible, since block valve closure can be checked by observing the rotameters in the analyzer. A complete test involving any two channels of the cell pressure input instrumentation is not conducted during reactor operation, since this same test, described earlier in this section, causes unacceptable system changes elsewhere. The radiation channels are tested with a source, on-line, and the block valves and the control circuits are redundant.

# 1.5.4.3 In-Cell Liquid Waste and Instrument Air Block Valves

The in-cell (secondary containment) liquid waste lines are blocked if the reactor cell pressure exceeds 2 psig (see Fig. 1.5.13 and input XIII, Fig. 1.5.2). The normal operating pressure in the containment cells is 12.7 psia. Excess cell pressure is a symptom of system malfunction or, at worst, the maximum credible accident.<sup>1</sup> The protective instrumentation and control hardware and blockage of instrument air lines have been described earlier in this section.

# 1.5.4.4 In-Cell Cooling Water Block Valves

A simplified flow diagram of the in-cell cooling water system, with instrumented block valves, is shown in Fig. 1.5.14. The signal to close the block valves is provided by an excess radiation level in the pump return header. Three independent sensors, RE-827A, B, and C, initiate block valve operation when any two of the input channels indicate excess radiation in line 827. Operation of the system is apparent from Fig. 1.5.14. Testing is accomplished during operation by manually inserting a radiation source in the monitor shield (refer also to Sect. 2.10) and observing that the indicated radiation level increases and that the proper relays operate. The construction of the sensor shield is such that each radiation monitoring channel can be tested individually. Since the monitor contacts are arranged in two-out-of-three coincidence, testing of individual channels does not close the valves. The valves may be tested individually by operating a hand switch and observing that flow stops in the line under test. The complete system is tested during shutdown.

Valve ESV-DGT serves as a backup to FSV-837-Al, FSV-841-Al, FSV-846-Al, FSV-847-Al and provides redundant blocking in the system. The thermal shield is protected from excess hydraulic pressure by the rupture disk in line 844. Pressure control valve PCV-844C and block valve FSV-844-Al, actuated by either pressure switch PSS-844-B1 or valve position switch ZS-847-A2 on valve FSV-841-Al, prevent breaking the rupture disk with the transient pressure surge produced by closing FSV-847-Al. Valve FSV-844-Al is also closed by the action of pressure switch PSS-855-Al when the pressure downstream from the rupture disk exceeds 5 psig. This action serves two purposes: (1) maintains some protection of the thermal shield if downstream pressure develops on the rupture disk, and (2) minimizes the loss of cooling water when the rupture disk does burst.

Any water discharged through a burst rupture disk passes into the vapor condensing system and is contained.

# 1.5.5 Underpressure Protection for the Secondary Containment Cells

Failure or malfunction of the pressure control system for the component cooling pumps, if undetected, could lead to a dangerous subatmospheric pressure reduction, causing a buckling type of failure of the secondary containment structure. Protection against such an event is provided by a three-channel, reliable system, schematically identical to that used for cell overpressure protection described above and earlier in this section.

If cell pressure falls to less than 12.2 psia, a control-grade alarm sounds. The safety-grade instruments (pressure switches) actuate at 10.7 psia (input XII, Fig. 1.5.2) and produce two protective actions: (1) shut off both component cooling pumps, and (2) close HCV-565-Al in the cell evacuation line (Fig. 1.5.8), thereby preventing further outflow of cell air to the stack.

# 1.5.6 Fuel Salt Sampler-Enricher Containment Instrumentation

The sampler-enricher is fully described in Sect. 3.12 and in refs. 26-29. When in use it must penetrate the primary containment and, therefore, is potentially capable of contaminating the area and exposing its operators to all the various types of radioactivity associated with nuclear fuel. The material in this section is limited to a functional description of the more important instrumentation and controls whose sole purpose is to prevent a loss of containment.

Figure 1.5.15 is a simplified line drawing which illustrates the operation of the sampler-enricher. It can be seen that sampling or enriching is accomplished by lowering and raising the cable-suspended capsule into and out of the fuel pump bowl. Throughout most of its travel the capsule is guided by and contained in the transfer tube, which provides direct access to the molten salt in the pump bowl. The sampling-enriching operation may be likened to withdrawing or adding water to or from a well with the "old oaken bucket" powered by a motor-driven winch. Containment is effected during these operations by subdividing the region through which the capsule travels into compartments which are opened and

closed in sequence so that two containment barriers are maintained. The regions which are considered to be primary containment are:

1. area 1A, the transfer tube between the maintenance valve and the pump bowl;   
2. area LB, the transfer tube between the maintenance valve and the operational valve;   
3. area lC and the short length of transfer tube which connects area lC to the operational valve. Note that area lC houses the motor-driven winch which raises and lowers the capsule.

Compartmentalization and closure of these primary containment regions is obtained by the maintenance and operational valves and by the port which closes the access to area lC.

Since a complete sampling or enriching procedure requires that the material, either fresh salt or hot sample, pass through both the primary and the secondary containment barrier, the latter is also compartmented. These compartments are maintained by

1. The access port, which separates the primary and secondary containment regions, lC and 3C respectively.   
2. The removal valve, which when closed, is the secondary containment barrier across the path traversed by the capsule. Note that area 3C contains the output side of the manually operated manipulator which the operator uses to unlatch the capsule from the cable, move it into area 3C, and thence to the transfer cask via the removal valve.

Figure 1.5.16 is an austerity version of the sampler-enricher instrument flowsheet and shows only the high-quality instrumentation whose sole purpose is to effect containment. Figure 1.5.17 diagrams the functions of these instruments and controls. Table 1.5.2 shows the normal aspects or status of the valves and the access door during use and when not in service. It is proper to point out that the sampler-enricher is used intermittently and by personnel well trained in its operation. Intermittent usage and functional requirements resulted in the arrangement of containment instruments in accordance with Figs. 1.5.16 and 1.5.17.

Where redundancy is not obtained by duplicating individual instrument channels which produce the same specific output action, it is because the desired protection is obtained by diversity (explained earlier in this section).

There are additional instruments and alarms required by the device. These lend support to the high-grade interlocks discussed herein; the reader is referred to Sect. 3.12 for more information.

Table 1.5.2.   

<table><tr><td rowspan="2">Operating Situation</td><td colspan="4">Component Condition</td></tr><tr><td>Maintenance Valve</td><td>Operational Valve</td><td>Access Port</td><td>Removal Valve</td></tr><tr><td>Capsule entering sampler-enricher (above removal valve)</td><td>Closed</td><td>Closed</td><td>Closed</td><td>Open</td></tr><tr><td>Capsule in area 3A and being ma-nipulated onto the latch</td><td>Closed</td><td>Closed</td><td>Open</td><td>Closed</td></tr><tr><td>Capsule latched to drive unit cable in area 1C</td><td>Closed</td><td>Closed</td><td>Closed</td><td>Closed</td></tr><tr><td>Capsule in transfer tube and entering maintenance valve</td><td>Open</td><td>Open</td><td>Closed</td><td>Closed</td></tr><tr><td>Capsule in transfer tube be-tween maintenance valve and pump bowl</td><td>Open</td><td>Open</td><td>Closed</td><td>Closed</td></tr></table>

![](images/764170c1d14c9a37b58ddc3d627fbb9f1759b33e808f17cf33a30a5d1531837e.jpg)  
Fig. 1.5.1. MSRE-Redundant Instrumentation for Block Valves.

![](images/dc4704ccd7700ed36052c5a845ff607d375bce2e116270cd14449029ae9adab4.jpg)  
Aeas Aes EeN eep Jo sseBd ndnno-ndu I 2Gt 3FJ

![](images/f321bb99a4a6aa4053a569db4f22c84287050767949d778f1b8654877f39e7ce.jpg)

![](images/ce1e373a0c53a41c500a3e3357b18e6d143b3a75ad7611beea5056488b40b3d1.jpg)  
Fig. 1.5.3. Input-Output Diagram of the MSRE Fuel Salt Fill and Drain Safety System.

![](images/87bd2f953648cd3ad6a9222ec5de62cb610b5762a8e95f90acbe36722c6d24d3.jpg)

ORNL DWG 67-4644

![](images/35e28ae47e1470019dfb6f40c32e21c474e24e2884cf3ce6e84ef3117588010f.jpg)

ORNL-DWG 63-8395R

![](images/605cbf0f220763b58d333f9bbcafd258f1622355d5a5fd6785292b161fb5e0a9.jpg)

X-Cloned: O-oen; E-either open or closed.

Durig nrrn rnrnnr h 5x 105 and 5x 104 are hore   
1x   
ACV 519 A & B oops aor completing it and before ope

![](images/4700ff382d141692cc2ee4062df8ff2b85c552583e721f211da38f66eb41959d.jpg)

![](images/7bbf6a66c45bef181c6d3b1750f56bba104e1b23cdfb3eca1a0a7b15883647a6.jpg)  
Fig. 1.5.4. Diagram of Reactor Fill and Drain System.

![](images/e1afa008e05db7905caccada3fcd3f367c423adb998ff08897747f99d0051d8e.jpg)

![](images/eb9d0df572f715c6b667b776614688e48ab8231d5494d7e3c4a5ece5c1f892cd.jpg)

![](images/87cd8f4e8789552b7df240ca1461ba9104fa240189cbb8912ba0aad19d543022.jpg)  
Fig. 1.5.5. Typical Channel of Safety-Grade Pressure Instrumentation for Use in Primary Containment.

![](images/343612d679afb064427b57b1cb8591503a065f9c007b2a77a213b14820280c5d.jpg)  
C   
C   
Fig. 1.5.6. MSRE Drain Tank Afterheat Removal System.   
C

![](images/c5e3a8eee57f75f50468643b4440b86775ecb37c394907b4c86241c7532b2e5b.jpg)  
Fig. 1.5.7. Diagram of System Supplying Helium to Primary and Secondary Containment Regions.

![](images/80573f19a5f7c5759faf0f8e0dd37b1c889d1d3e25d1f71e3064038d580a5a76.jpg)

![](images/0ff6d17a825647d7e9341d23f316d4c5a6bd418d528fac1603d6b3e1b3e64b05.jpg)  
87   
Fig. 1.5.8. MSRE Off-Gas System.

![](images/d2b576662ef173a5f98b145bc91b59270d70e38102204a366696ee553afb8c9a.jpg)

#

ORNL-DWG 63-8393

![](images/016c5e7b71e739f01c19a06c7f2b99d716b8b96471dfd05c46f540e671553ce7.jpg)  
Fig. 1.5.9. Lube-Oil System Off-Gas Monitors.

#

![](images/e95064dd87314294e0529bfc8415baaff0ac10923ec73009d4649ff75075d12f.jpg)

![](images/923797d72097366e10ca054bab1e834642d488826bf513394c20744165aea527.jpg)

![](images/b6fe40a3450e93962a532e1c9076208c454d94c44577d2346fca014cca815326.jpg)  
Fig. 1.5.10. Off-Gas Sampler.

![](images/ba53cc41a9813605197b07de133907b2dee563a665a4abfa0c833d738d03aa18.jpg)

![](images/9bbeb42212dedee66ae9b3ca33d994c580980ff2909a63c51bf95ca3d1b4624d.jpg)  
BLOCK DEMAND FOR: 1. LIQUID WASTE SYSTEM   
2. STEAM DOME DRAINS   
3. OXYGEN ANALYZER   
4. OFF-GAS SAMPLER

![](images/b92cc24d2ebe1e01952c1d10d69b6aa6e4873dc9a1a5f9ce1630e26d07b94333.jpg)  
Fig. 1.5.11. Block Valve Circuits for Off-Gas Sampler.

![](images/c09a66589b7d139df4272b25593045e79b672931cd86c107c3bde6d4a96f2f48.jpg)  
91

![](images/3b42499729f80cf7c3315c6efdd0d28ec577021bfda98e81dd319b7f4084b9ad.jpg)

![](images/6640edef615aa7f372e4aed62aecc8f96990a288e4af8c64b8fba95fc669095b.jpg)  
Fig. 1.5.12. Block Valves to and from Cell Oxygen Analyzer.

![](images/e8e54b247c6d3a1cb20c18d82aaa98bfd01562259d9162470e8d9c3bb783afe9.jpg)  
Fig. 1.5.13. In-Cell Liquid Waste and Instrument Air Block Valving.

![](images/14c0c2e11a2aa418a1a10479773086d43f113471f867001c9aaba67fbb82041c.jpg)

![](images/66844031a735f16ed7f9cc0a9f1f15104900cbf4143a194b30e3b692e478fa91.jpg)

ORNL-DWG 64-638A

![](images/053e4369fb12e5057cc7cd9deddda089f8695a27ab93561d9e086d01c49ab92c.jpg)  
Fig. 1.5.14. MSRE Safety System Block Valves in the In-Cell Treated Cooling Water System.

ORNL-DWG 63-5848R

0

![](images/bbee76cc2279a649604d32f7ec249a998cb29ce363267026f2a6b69a3270bdb8.jpg)  
Fig. 1.5.15. Sampler-Enricher Schematic.

#

#

![](images/e5001ef5a4287c027ffa5ce3df7366367b3c2f35e34d8ca2cccbc9695633bcc7.jpg)  
Fig. 1.5.16. Sampler-Enricher Simplified Flow Diagram.

![](images/57c450f900127f122fbfcf175ed601fb2dd351d4a3a9aac254ec17471e85b73a.jpg)  
Fig. 1.5.17. Sampler-Enricher, Input-Output Diagram of Safety-Grade Control Actions.

![](images/ff0e22ccded4ee5a4e2672c0e3384c75ada797c65513599d25e1990c7033fe78.jpg)

![](images/04fc17526a5c73b37c8f577cdb3c6e0d5a06549dd2db9541cd0dccec22a82d24.jpg)

# 2. SAFETY INSTRUMENTATION AND REACTOR CONTROL

# 2.1 NUCLEAR INSTRUMENTATION: INSTALLATION AND LOCATION

All permanent neutron sensors are located in a single penetration. The penetration is a 3-ft-diam pipe installed at an angle of $42^{\circ}$ to the horizontal so that its lower end is opposite the midplane of the reactor core and its upper end terminates on the main floor in the high-bay area. Figures 2.l.1 and 2.l.2 are plan and elevation views, respectively, of the installed penetration. The lower end of the penetration passes through the thermal shield, and the end closure plate is essentially flush with the inner periphery of the thermal shield. The penetration is, from a containment standpoint, an extension of the secondary containment shell. The lower end of the tube is welded to the containment shell, and the upper end is embedded in the earth fill and the concrete floor. A bellows-type expansion joint accommodates thermal expansion between these points. Since penetration was installed during modifications to the containment shell, it was stress-relieved and pressure-tested at the same time.

The penetration is filled with water to within approximately 1 ft from its upper end. A float-type instrument monitors the water level and gives an alarm when the level changes more than 4 in. Water is added with a hand valve adjacent to the upper end of the penetration in the high-bay area. A 5-gpm pump circulates the water in the penetration to reduce temperature gradients and maintain a uniform concentration of corrosion inhibitor. The inhibitor, containing lithium nitrite $\left(\mathrm{LiNO}_{2}\right)$ and lithium borate $\left(\mathrm{LiH}_{2} \mathrm{BO}_{3}\right)$ , has 810 ppm of $\mathrm{NO}_{2}$ and 57 ppm of boron. The solution is sampled periodically and tested to maintain the pH at $9.0 \pm 0.2$ .

The penetration is designed to accommodate ten ion chambers. Each chamber is located in an individual guide tube; four tubes are 5 in. ID and six are 4 in. ID. The configuration of these tubes within the penetration and the types of chambers assigned to them are shown in Fig. 2.1.3. The guide tubes are not made of single lengths of 30-ft-long tubes; instead subassemblies, each approximately 10 ft long, were made by welding the tubes into end plates, or bulkheads, and the subassemblies were bolted together when installed in the penetration. The tubes were constructed this way (Fig. 2.1.4) because there was not enough headroom behind the upper end of the penetration to ease the handling problem at assembly. The tubes are open to the water in the penetration, and the upper, or last, bulkhead plate serves as the cover plate over the end of the penetration. Individual, smaller cover plates are used over the upper end of each tube. These contain the necessary gland-type fittings for signal leads and push rods for chamber positioning. Figure 2.1.5 shows the upper end of the penetration with the guide tubes and individual cover plates installed. One of two ORNL model Q-2545 wide-range counting channel drive units (see Sect. 2.3) is shown installed in the penetration.

The mounting flanges on these drive units fit the drilling for the cover plates, so that a complete drive unit is handled as a module which is inserted in a tube and bolted in place.

Early critical tests disclosed that the curve of neutron flux in the penetration vs distance deviated grossly from the desired exponential type of curve. The deviation was beyond the capabilities of the compensating function generator (see Sect. 2.3) in the wide-range counting channel. Cadmium sleeves<sup>1</sup> were placed around guide tubes 6 and 9 to shield the fission counters from neutrons which entered from the side and distorted the curve of count rate vs distance. The design of the shields, their location, and their effect on the count rate as a function of distance in guide tube 6 are depicted in Fig. 2.1.6.

Figure 2.1.7 is a diagram of the interconnection wiring layout. As much as possible the safety system wiring was separated from control and power wiring. It was not feasible to separate the first runs of cabling from the drive units to the junction boxes on the reactor cell wall. These jumper cables (described in more detail in Sect. 2.7) contain all the electrical leads in a single well-protected bundle.

The safety system interconnections, consisting of the wiring to the clutch coils and the potentiometers in the rod drive unit and the signal and chamber voltage leads to the safety chambers in the instrument penetration, are in individual and separate conduits to the control room. Except where absolutely necessary, these safety interconnections are unbroken by terminal blocks, connectors, etc. All the in-cell wiring (excluding jumper cables) is entirely with mineral-insulated, copper-sheathed cables.

Control-grade wiring, not subject to the restrictions imposed by separation, protection, and independence, is run in trays and conduits as dictated by cost and convenience.

![](images/8f5a09067d21472bb62cebfc1540f42fdcf940d7e723a97fccd342be7c07e987.jpg)  
Fig. 2.1.1. MSRE Plan View of Nuclear Instrument Penetration.

![](images/5f5979655172d69a101819453da4fa860e95cb0887728d8b33f8880aac688fcd.jpg)  
Fig. 2.1.2. MSRE Elevation View of Nuclear Instrument Penetration.

![](images/e835c402dcbf8a51e67d5a833d1b2fd1ba697fcc052d2fa138b8b76007f67f8a.jpg)  
Fig. 2.1.3. Location of Neutron Sensors Within Instrument Penetration.

![](images/5c920561b12d179201e3288609c9f170b02b2e52080e311f07b9146c09c77847.jpg)  
Fig. 2.1.4. Chamber Guide Tube on Shop Floor Prior to Installation in Penetration.

![](images/46d8c302c5f6408fc3f0a5bc9230785e0dfe91c8e3bfbb20b497798f70d9f9b9.jpg)  
Fig. 2.1.5. Upper End of Penetration with Guide Tubes and Individual Cover Plates Installed.

![](images/1a88a2a42bd98cda10aa9ef2491e196f1fc0761499be73b8c4b77511578b784f.jpg)

![](images/a44dcddd0e81001252a7d6b75ca41bad73c2b7fe9bfe464fca24a232e8b95e54.jpg)

![](images/21d9e7e42820e38c6beb500a36743fbfb8121daf1978d0928c9e573a4a8b01fb.jpg)

![](images/02db20787216388a0592f040c80b76698136a33ece039f1a1f40b14ea1eb9de2.jpg)  
SECTION A-A LOCATION OF GUIDE TUBES   
Fig. 2.1.6. Cadmium Shielding of the Fission Chamber Guide Tubes.

![](images/d67fe5816132a13d63164cac6a7b7770b0be5973fb08d1d24a762182ee0c5deb.jpg)  
Fig. 2.1.7. MSRE Interconnection Wiring for Nuclear Instrumentation.

# 2.2 BF3 INSTRUMENTATION

# 2.2.1 General

The MSRE is equipped with one channel of sensitive $\mathbf{BF}_3$ counting equipment. The counting chamber is located in guide tube 2 (Figs. 2.1.4 and 2.1.5). The electronic instruments used with these chambers follow typical practice (Fig. 2.2.1).

This sensitive $\mathrm{BF}_3$ channel is required to get counting-rate "confidence" at the neutron source level when the reactor is less than half filled or when it is being filled with flush salt. Except for the pre-amplifier, the electronic instruments shown in Fig. 2.2.1 are mounted in the nuclear instrument cabinet in the auxiliary control room. As soon as confidence is established by one or both wide-range counting channels, the $\mathrm{BF}_3$ chamber is withdrawn manually to prevent its being damaged.

# 2.2.2 $\mathbf{BF}_3$ Counter

The neutron counter is a $\mathbf{BF}_3$ counter from Reuters-Stokes Company, No. RSN-28A, procured on UCNC purchase order No. 56S-1724, May 11, 1964. The specifications and characteristics are as follows:

Shell (shell is cathode)

Outside diameter 2 in.

Wall thickness (wall is the 0.55 in. cathode)

Overall length 12 in.

Active length 8.13 in.

Material Aluminum

Anode 0.002-in.-diam wire insulated from the shell with ceramic insulation

Enriched BF₃ (96%¹⁰B) to a pressure of 40 cm Hg abs

Performance

Thermal-neutron sensitivity 15 counts $\sec^{-1}(\underline{\mathrm{nv}})^{-1}$

Saturation curve See Fig. 2.2.2

For use in the MSRE, the counter is encased in a weighted waterproof can, described by Instrumentation and Controls Division drawings Q-2719-3 and -4. A jointed push rod is used as a handle to position the counter within the guide tube in the penetration.

# 2.2.3 High-Voltage Power Supply

The high-voltage power supply is manufactured by Electronic Research Associates, model 25/10UC. The output from the power supply is continuously adjustable from 500 to 2500 v dc, positive or negative, by six step-switch positions and a fine control. Maximum load current is 10 ma for any voltage. The total amount of ripple, hum, and noise is less than 5 mv rms. Line regulation is ±0.005% for a ±10% change of line voltage. Load regulation is a 60-mv change from no load to full load; recovery time is less than 10 msec. Front panel meters indicate from 0 to 10 ma and from 0 to 2500 v dc. The input is 115 ± 10 v ac, 60-hertz, single-phase, 1-amp.

# 2.2.4 Preamplifier, ORNL Model Q-1857

The preamplifier consists of a three-stage feedback loop, followed by a resistance-capacitance differentiator, and a second three-stage feedback loop. The third stage of the second loop is a power stage to drive a long, low-impedance transmission line. The gain of each loop is about 20. A 2.5:1 voltage loss occurs in the differentiator, so that the overall gain is about 150. Variable compensation is provided across the feedback resistor in each loop to produce satisfactory transient response. The preamplifier power supply is self-contained.

# 2.2.5 Pulse Amplifier, ORNL Model Q-1875

The output of the ORNL model Q-1857 preamplifier is developed across a 100-ohm resistor in the amplifier chassis. This resistor serves as the characteristic impedance termination for the transmission line from the preamplifier. The signal is coupled to a gain control whose output supplies the signal to the pulse amplifier.

The pulse amplifier has two separate three-stage amplifiers with feedback loops. The compensation on each feedback loop is adjustable: compensation is used in the first amplifier to adjust the rise time of the amplifier and in the second amplifier to make the transient response satisfactory. The gain of each loop is approximately 100, but, due to losses in the output cathode followers, the overall gain is about 5000.

The output of the main amplifier is available at "low" and "high" output jacks. The low output is intended for driving long cables and has a maximum value of 5 v. The high output will deliver approximately 100 v.

A pulse-height selector (PHS) is included on the amplifier chassis for measuring pulses between 0 and 100 v. The PHS is direct reading with

an accuracy of approximately 0.5 v. Two PHS outputs are provided: the first, a positive pulse with an amplitude of 3 v and a width of 0.4 μsec, intended for driving a count rate meter, appears at CN6; the second, with an amplitude of about 20 v negative and of slightly longer duration, appears at CN5. The second is intended for driving aScaler.

The amplifier contains its own power supply and is designed to operate with 115-v, 60-Hz power.

# 2.2.6Scaler,ORNL Model Q-1743

TheScaler has a fast input decade consisting of a type 6700 beam switching tube, a Schmitt trigger, and slow decades which are Ericsson GC-10B glow transfer tubes. Each glow transfer tube is driven by a dc-coupled 1AG4 tube. The glow tube stages are followed by a pulse shaper, register driver, and a six-digit mechanical register. The instrument contains a regulated power supply. The input resolving time is 1 $\mu$ sec, with a counting loss of less than $0.2\%$ at 20,000 random counts per second.

# 2.2.7 Logarithmic Count Rate Meter, ORNL Model Q-751

This instrument measures the average rate of a series of electrical pulses. The input pulses are the output from the pulse-height selector (Sect. 2.2.5). The pulses are randomly spaced, positive $3\mathrm{~V}$ amplitude and $0.4\mu \mathrm{sec}$ long. The output of the instrument is logarithmic and spans four decades. The average counting rate, in counts per second, is displayed on a meter. In addition, provision is made for remote readout on either a remote meter or a 10-mv recorder, or both. The indicating meter is graduated from 1 to 10,000 counts/sec.

# 2.2.8 Confidence Trips

This instrument is composed of two Control Data Corporation, Magsense level comparators. Each unit is designed to accept an input of 0 to $100\mu \mathrm{a}$ dc. The trip is continuously adjustable in this range. The trip level and hysteresis are adjustable by potentiometers mounted on the rear panel. The output consists of two SPDT relay contacts.

![](images/7567f14f67e2e7914548381ab33cff606dcacce2b7de3727f565d32988381535.jpg)  
Fig. 2.2.1. Diagram of $\mathbf{BF}_3$ Counting Channel.

![](images/c418c80e648e228c0f265920ed59a99bcae34cf92f0fb58dcdbd7daf42da24db.jpg)  
Fig. 2.2.2. Typical Plateau Curve for Reuters-Stokes $\mathbf{BF}_3$ Counter Type RSN-28A.

# 2.3 WIDE-RANGE COUNTING CHANNELS

# 2.3.1 Principle of Operation

The wide-range counting channel employs a 2-in.-diam, 6-1/2-in.-long fission chamber as the neutron sensor and is useful from startup (with a fully fueled core vessel) to full-power operation at 10 Mw. The principle of its operation, described elsewhere, $^{1,2}$ is repeated here as a convenience to the reader.

The design of this wide-range counting system is explained by examining the behavior of a movable neutron sensor submerged in, or surrounded by, a neutron reflecting and absorbing medium in which the neutron attenuation with distance is approximately exponential. For purposes of explanation it is sufficient to consider the idealized case in which neutron attenuation as a function of distance from the neutron source is exactly exponential. For this idealized situation

$$
\mathrm {C R} = \mathrm {P e} ^ {- \mu x}, \tag {1}
$$

where CR is the count rate in counts per second, P is the reactor power (assumed proportional to flux), x is the distance from the reactor, and $\mu$ is the attenuation coefficient of the medium surrounding the fission chamber. Rearrangement gives

$$
\log P = \log C R + \mu x. \tag {2}
$$

It is apparent from Eq. (2) that log P is the sum of two easily obtained numbers: the logarithm of the counting rate (log CR) and the distance, x, of the sensor from the neutron source multiplied by a constant, $\mu$ . Inverse reactor period is obtained in the usual way by differentiating Eq. (2) with respect to time.

Figure 2.3.1 is a simplified diagram of the arrangement of the instruments that perform the operations of measuring the neutron flux and distance, obtaining a logarithm, adding, and differentiating. In the MSRE (or any other installation), neutron attenuation is not ideally exponential, as assumed in the preceding paragraph; instead, $\mu$ varies with $x$ , and the form of this variation can only be established by experiments with the equipment installed for use at the reactor. An adjustable position-sensing device, the ORNL model Q-2616 function generator, produces a signal proportional to $\mu x$ . The adjustment feature provides a means to compensate for variations in $\mu$ with $x$ and, further, permits these adjustments in situ.

The fission chamber is moved toward or away from the reactor by a servomechanism which attempts to maintain a constant output from the count rate meters. The value of this constant output (the count rate set point) is, within limits, arbitrary. It should be high enough to ensure a good signal-to-noise ratio in the input to the count rate meters, but it should not be so high that fission counter life is seriously reduced. A typical value for the count rate set point is 10,000 counts/sec. These wide-range channels can provide useful operating and control information as long as the counting rate is in the range from 1 to 100,000 counts/sec. Limiting values of count rate are used to provide control system interlocks, discussed in detail in Sect. 2.6. The operation of a wide-range counting channel is explained in the discussion by tracing its response as the reactor goes from subcritical to full-power operation. Figure 2.3.2 shows curves of count rate and chamber position during a traverse of the reactor through its power range. The curves are based on the assumption that the count rate set point has been established at 10,000 counts/sec.

In the source and very low power region, where the count rate is less than the set-point value of 10,000 counts/sec, the error signal, which is the algebraic difference between the actual count rate and the set point, is negative. This causes the servomechanism to drive the chamber toward the reactor until its lower limit is reached. The chamber will remain inserted at the lower limit until the reactor power is sufficiently large to produce a count rate of 10,000 counts/sec. While the chamber is at the lower limit, $\mu x$ is constant, and (see Fig. 2.3.1) the rise in reactor power is followed by the output of the logarithmic count rate meter. When the reactor power is high enough to produce 10,000 counts/sec with the chamber at the lower limit, the error signal becomes positive and the servomechanism withdraws the fission chamber to maintain the count rate constant at 10,000 counts/sec. Changes in reactor power are now indicated by changes in the "compensated position," $\mu x$ , the output of the ORNL model Q-2616 function generator.

If, for example, the count rate set point is changed arbitrarily from 10,000 to 12,000 counts/sec while the chamber is partially withdrawn and the reactor is in steady state, the servomechanism will insert the chamber a sufficient distance to satisfy the increased count rate request. The decreased value of $\mu x$ will exactly equal the increase in log CR, and the sum of the two, $\log P$ , will remain constant, as it should. Again, suppose that, with the reactor in steady state, the operator switches from servo control of position to manual control and arbitrarily withdraws the chamber a short distance. The decrease in log CR will be balanced by the increase in $\mu x$ , and their sum, $\log P$ , will remain constant. Now, suppose the operator continues to withdraw the chamber manually so that the counting rate approaches 2 counts/sec, which has been established as the useful threshold operating value for the system. The count rate signal will contain a higher percentage of spurious electrical input "noise," and, also, the random variations in the neutron flux will become more apparent as the count rate is decreased.

In common with all counting instruments of this general type, the response of the count rate meter becomes progressively slower as the count rate decreases. The loss in response is such that when the count rate is reduced to about 500 counts/sec, the logarithmic count rate

meter is unable to follow the change in count rate produced by manual chamber withdrawal. Therefore, in such a case, the indicated power would lag and would be higher than actual power. This response lag would continue to produce an error, and the indicated power reading would be higher than actual power until the chamber had stopped moving and enough time had elapsed to attain steady state in the new position. This situation obtains regardless of whether the chamber is being inserted or withdrawn manually. In manual insertion at count rates below 500 counts/sec, the indicated power will lag and appear lower than actual power. As the count rate is lowered, the output of the counting system, log P, may become erratic and fluctuate about the average value. At very low counting rates the ratio of useful signal to noise decreases and accuracy suffers. If chamber withdrawal continues until the count rate becomes less than 2 counts/sec, the confidence circuits will be actuated and the "no-confidence" interlocks governed by that channel will be established. If the reverse process takes place, the chamber may be inserted until the counting rate becomes 50,000 counts/sec, at which point the confidence circuits will also be actuated. This upper bound of system operation was established at this value to keep the instruments within their operating range. The confidence circuits and their functions are discussed in Sect. 2.6.6.

From the foregoing it is evident that, if the count rate is 500 counts/sec or more, the servo need be fast enough to follow only normal maneuvers; any transients too fast for the servo to follow will change the count rate so that the channel will read correctly. This technique has several advantages: the operator need not switch range or take any other action, the system covers a very wide range of reactor power, manual withdrawal of the chamber and the dead time induced when the chamber is withdrawn are eliminated, and the constant, optimum count rate of the amplifier is maintained when sufficient flux is available.

Figure 2.3.3 is a detailed block diagram of a wide-range counting channel as used in the MSRE and includes the ORNL model Q-2609 fast-trip comparators (described in Sect. 2.5) which produce the trip signals required by the reactor control system. The increased number of operational amplifiers shown in Fig. 2.3.2 are required to obtain signal gain for impedance matching to output devices and for signal inversion (sign change).

The detector, preamplifier, and radiation-resistant interconnecting cable are contained in an integral assembly, ORNL model Q-2617. This assembly, approximately 2 in. OD, is flexible so that a guide tube or thimble, curved if required, can be installed in the reactor shielding leading to the core. The assembly is waterproof and can operate continuously in an ambient temperature of $100^{\circ}\mathrm{C}$ while surrounded by either air or water.

The detector is a fission chamber with concentric cylindrical electrodes coated with $1\mathrm{mg/cm}^2$ of $^{235}\mathrm{U}$ over a total area of $860\mathrm{cm}^2$ . The chamber is well saturated with $200\mathrm{v}$ applied; the operating polarizing potential is $270\mathrm{v}$ . The collection time is approximately 80 nsec. The pulse-height characteristics of the chamber, obtained by using the pre-amplifier described below, are shown in Fig. 2.3.4. It is evident that gamma pileup presents no problem, even in fields as high as $2\times 10^6$ r. The chamber has ceramic insulation entirely, and the special cable con

necting the chamber to the preamplifier is designed to withstand a gamma-ray dose of $10^{10}$ r.

The output stage of the preamplifier drives one side of a balanced line, the other side of which is terminated symmetrically. This symmetry and careful attention to shielding and grounding make the assembly, as demonstrated in many field tests, very insensitive to electrical noise pickup.

The receiving end of the balanced line feeds a pulse transformer for common-mode rejection and clipping to give an approximately symmetrical waveform. This avoids base-line shifts due to changes in counting rate and aids in keeping the discrimination level constant.

Pulses from the pulse transformer are sent to the pulse amplifier and count rate meter, ORNL model Q-2614. Following a calibrated attenuator the pulses are amplified in two feedback stages, each with a gain of 10, and enter a biased amplifier whose variable bias level determines the discrimination level. Only pulses that exceed the discrimination level are counted. The output pulses from the biased-amplifier discriminator are shaped and applied to a conventional logarithmic count rate circuit of the Cooke-Yarborough type. The time constants are a compromise between the desire to have rapid response and the necessity to prevent excessive fluctuation in the period signal.

The output of the log count rate circuit is applied to an ORNL model Q-2605 operational amplifier (1A in Fig. 2.3.3) whose gain is adjusted to give an output of 2 v/decade, or 10 v full scale. The function generator output is applied to amplifier 2B through the normally closed contacts of K1. The gain gives an output of 2 v/decade. Amplifier 2B is also used in a test mode and will be described later. The outputs of amplifiers 1A and 2B are summed, with a gain of 1/2, in amplifier 2A, yielding an output signal proportional to reactor power. The span of the summing amplifier 2A is 10 v, or 1 v/decade. The outputs of the log count rate amplifier (1A), the summing amplifier (2A), and the gain amplifier (3B) are indicated on panel meters in drawer W-1.

The generation of a period signal from the reactor flux signal is accomplished with operational amplifiers 3A and 3B. The output from amplifier 3A is the approximate derivative of the log P input with a dc gain of 4 (product of C 308 and R 331). To prevent excessive noise in the period signal a 250-kilohm input resistor and a 1-μf feedback capacitor are provided to limit the low- and high-frequency noise gain respectively. The output of amplifier 3A is amplified by amplifier 3B and is offset so that 0 to +10 v corresponds to a period of -30 to +5 sec. An infinite period is +1.428 v provided by the offset network at the input of the amplifier. The amplifier gain is 24.6. The pulse amplifier and count rate meter module, ORNL model Q-2614, has, in addition to the log count rate output, a simple diode pump circuit (linear count rate circuit) whose output is used as the signal for the chamber position servo. This circuit has an output of approximately 1.75 v at 10^4 counts/sec. This signal is compared with the demand potentiometer (servo level) in amplifier 1B. Amplifier 1B has a voltage gain of 50; further voltage and power gain are provided by a servo amplifier, ORNL model Q-2615, which has an approximate voltage gain of 3 and whose output drives the servo motor directly. In addition to the chamber, the motor drives a tachometer whose output is applied to the servo preamplifier

lB and with a polarity opposite that of the input signal; this negative feedback loop provides servo stability.

To provide control interlocks, eight fast-trip comparators, ORNL model Q-2609, are used. Two fast-trip comparators receive their input from the log count rate amplifier (lA). Comparator 1 trips if the counting rate is less than 2 counts/sec, whereas comparator 2 trips if the counting rate is greater than 50,000 counts/sec. Their output (relay contacts), in series with the "calibrate-operate" relay contacts, provides counting channel confidence if all eight comparators are properly plugged into the instrument cabinet drawer (see Sect. 2.5 for additional discussion of confidence). Summing amplifier 2A provides the input to three fast-trip comparators. The first comparator operates if the power "sags" below 200 kw while in the "Run" mode; the second operates when the power is above 500 kw, thus giving permission to enter the "Run" mode; and the third initiates a control rod "reverse" if the power exceeds 1.5 Mw in the "Start" mode.

Several tests are provided to ensure that the system is operating properly. There is contained in the pulse amplifier module (Q-2614) a $10^{4}$ - and 10-cps oscillator which may be applied to the input of the pulse amplifier by proper positioning of the gain switch on the front panel. In addition, with the gain switch on period test, the period test relay (Kl) must be actuated by a push button in drawer W-1. This switches out the normal inputs and feedback resistors of the function generator amplifier and switches in a 10- $\mu$ f feedback capacitor and a selectable input resistor. With an input of 25 v applied through the gain switch, this amplifier thus generates a voltage ramp which produces a 5-, 25-, or 30-sec period indication as selected. An additional push button in drawer W-1 causes an adjustable voltage source to be applied to amplifier 2A to test its fast-trip comparator. "In" and "out" push buttons on the same drawer provide normal override of the normal servo signal from the output of the Q-2615 module.

The chamber drive mechanism is a ball-bearing lead screw with a linear speed of approximately 72 in./min and a total stroke of 90 in. The direct-current, variable-speed drive motor has an integral tachometer and is protected from overload by a slip clutch. The position-sensing components are connected directly to the lead screw shaft ahead of the slip clutch.

The position-sensing train contains a ten-turn potentiometer whose output is connected to a meter in drawer W-1. In addition, a one-turn data-logger potentiometer and synchro transmitter for driving a position indicator on the console is provided. Upper and lower limit switches restrict the overall travel of the unit.

# 2.3.2 Fission Chamber and Preamplifier Assembly

The following description has been excerpted from ORNL-3699 (ref. 4). The $3/4$ -in. fission chamber described in ORNL-3699 has been re

placed with one of more typically standard dimensions (2 in. diam) with greater sensitivity. The excerpted text has been altered accordingly.

# 2.3.2.1 Introduction

To meet the space and environmental requirements for high-performance reactors, an articulated assembly (Fig. 2.3.5) consisting of a fission chamber, a preamplifier, and flexible cables has been developed. Because high-flux reactor cores are usually inaccessible, it becomes necessary to use a detector that is small and movable in a tube which can be bent to resolve the access problems at each reactor. The relatively low sensitivity of a small chamber is compatible with the large neutron source level encountered in such reactors. Locating the preamplifier close to the fission chamber drastically reduces the susceptibility of the counting channel to electrical noise pickup, so that the system responds predominantly to neutrons; consequently, the reactor operator is assured of an adequate source. The assembly is particularly suitable as part of a wide-range counting channel,[1] but also can be used as part of a conventional counting channel.

The entire assembly is waterproof and can operate continuously at a temperature of $100^{\circ}\mathrm{C}$ ambient. The maximum outside diameter of the assembly is 2 in. (chamber diameter). The fission chamber and the cable connecting it to the preamplifier can withstand a total integrated gamma radiation dose of $10^{10}$ rads; the preamplifier can withstand at least $10^{8}$ rads.

# 2.3.2.2 Preamplifier

# Circuit

The preamplifier circuit (Fig. 2.3.6) consists of two cascaded feedback amplifiers: a charge-sensitive input configuration $(\mathbf{V}_1$ and $\mathbf{V}_{2A}$ ), followed by a voltage-sensitive amplifier $(\mathbf{V}_{2B}, \mathbf{V}_3, \mathbf{V}_4)$ with symmetric output. The signal pulses are differentiated both at the input and at the output of the preamplifier, giving the pulse shape shown in Fig. 2.3.7. The gain of the preamplifier is $0.75 \times 10^{12} \mathrm{~V} / \text{coulomb}$ . This corresponds to a system output pulse height of $150 \mathrm{mv}$ for a nominal 50-Mev fission fragment. The counting loss for randomly spaced pulses is $10\%$ at a counting rate of $10^{5}$ counts/sec.

The advantages of a charge-sensitive configuration are that, over a wide range of detector capacitance, (1) the output signal height depends only on the charge generated within the detector and is insensitive to the capacitance of the detector and connecting cable (variation of input capacitance from 0 to 200 pf produces a gain change of only $10\%$ ), and (2) the decay time of the detector pulse is also insensitive to the capacitance of the detector and cable (variation of input capacitance from 0 to 200 pf produces a decay time change of only $10\%$ ).

The preamplifier output is connected to a balanced and shielded cable which is terminated at its receiving end by a pulse transformer. The common-mode electrical fluctuation signals picked up by the two signal leads are canceled in the pulse transformer. In one application at a reactor the common-mode rejection was greater than $95\%$ .

The double differentiation reduces the effects of pulse pileup. With the first differentiator at the input to the preamplifier, the maximum counting rate is limited by coincidence loss rather than by bias shifts. The pulse transformer serves as the second differentiator. The second differentiation time constant is determined by the ratio of the primary inductance of the transformer to its terminating resistance. The combined effect of both differentiators eliminates any duty-cycle shift in the main-amplifier discriminator threshold. Figure 2.3.7 is a photograph of the fission pulses at the main amplifier input. The integrals of the individual pulse areas on either side of the reference are equal.

# Component Selection

The operating temperature, the radiation requirements, and the permissible overall diameter of the assembly demanded prudent selection of the components used in the preamplifier.

Tubes. - Temperature and radiation conditions precluded the use of transistors; consequently, flying-lead subminiature tubes were selected. Nuvistors were considered but were rejected because their diameter is too large to mount components side by side with the tubes in the allotted space.

Resistors. - Resistors were limited to those of wire-wound and deposited-carbon types. The wire-wound resistors (miniature power ratings) were used in all critical circuit locations sensitive to the value of a resistor; deposited-carbon resistors were used in noncritical circuits.

Capacitors. - Capacitors were limited to those of porcelain and solid tantalum electrolytic dielectrics. The particular ceramic capacitors used (Vitramon type VK20) have maximal operating conditions of $150^{\circ}\mathrm{C}$ and 200 v. A $10^{8}$ -rad gamma dose results in a capacitance variation of less than $1\%$ . The tantalum capacitors (Texas Instrument type SCM) are used only for bypassing in circuits which can tolerate high leakage currents and considerable capacitance variations. The operating temperature of the tantalum capacitors is limited to $125^{\circ}\mathrm{C}$ . As a result, they are located in the preamplifier layout, where negligible heat power is dissipated (see the following section). Irradiation tests made at ORNL on four type SCM tantalum capacitors to an accumulated dose of $10^{8}$ rads showed an increase of less than $5\%$ for the dissipation factor.

# Provisions for Operation at $100^{\circ}\mathrm{C}$ Ambient

For continuous operation of the preamplifier in air or water at $100^{\circ}\mathrm{C}$ ambient, the following provisions were made:

1. The preamplifier was potted in a mixture of 70 wt % epoxy Helix P-430 and 30 wt % epoxy Dow Chemical DER 732 to which was added 6% of Helix hardener B. This particular potting compound improves the heat transfer and increases the mechanical rigidity of the preamplifier. The advantages of using this compound are that it is only slightly brittle at room temperature, it shrinks minimally during curing (the shrinkage of some epoxies during curing has caused tube and tantalum capacitor breakdowns), and its thermal expansion coefficient is compatible with that of the preamplifier components.

2. The tube filaments are heated with a voltage of only 5.5 v (6.3 v rating) to minimize the heat-power generation.

3. The tantalum capacitors $(125^{\circ}\mathrm{C}$ max) are located at the ends of the preamplifier, whereas the subminiature tubes are positioned in the center of the preamplifier. The ceramic capacitors $(150^{\circ}\mathrm{C}$ max) are also located at the ends, except for a group which is placed in a gap between the first and the second tubes as shown in Fig. 2.3.8.

Two different tests were performed to establish that the capacitors operate below the manufacturers' specified maximum temperatures when the preamplifier is in a region with an ambient temperature of $100^{\circ}\mathrm{C}$ . In the first test the preamplifier was placed in still air at $100^{\circ}\mathrm{C}$ in an oven. In the second test the preamplifier was immersed in water at $98^{\circ}\mathrm{C}$ . In both tests five thermocouples were located inside the preamplifier close to the components of interest, and the time profiles of the temperatures were recorded. The results indicated that the equilibrium temperatures of all capacitors were at least $6^{\circ}\mathrm{C}$ below the manufacturers' maximum specified temperatures in the first test and $14^{\circ}\mathrm{C}$ in the second test. The first test lasted ten days; during this time no change in the preamplifier gain or output pulse shape was observed.

# Separation Distance of Preamplifier to Chamber

The separation distance between the preamplifier and the fission chamber should be short to satisfy the electrical noise pickup consideration, but must be long enough to limit the radiation damage to the preamplifier. (The preamplifier was designed to withstand an accumulated dose of $10^{8}$ rads over one year of continuous operation.) The evaluation of the effects of the accumulated dose should be separated into two parts: the dose accumulated during operation of the reactor at power and the dose accumulated during reactor shutdown. In light-water-shielded reactors, the dose accumulated during reactor shutdown is considerably alleviated if the neutron counting rate is restricted to $10^{4}$ counts/sec or less. The reason for this is that photoneutrons generated in the water by the residual fission product gamma rays will give a neutron counting rate that makes the insertion of the fission chamber and preamplifier assembly into a higher gamma flux unnecessary (see Sect. 2.3). For application in light-water-moderated reactors, a separation length of $4 - 1/2$ ft between the fission chamber and the preamplifier is adequate. This distance is also sufficient to maintain the preamplifier in a gamma flux less than $10^{4}$ r/hr (or $10^{8}$ r/year) when the reactor is at full power.

# 2.3.2.3 Flexible Cables

# Cable Between Fission Chamber and Preamplifier

The cable between the fission chamber and the preamplifier is a BIW 50-ohm coaxial cable enclosed in an external inorganic insulation sheath (spaghetti). The sheathed cable is inserted into a $1/4$ -in.-ID corrugated flexible metal tubing fitted with stainless steel braid and casing. The BIw cable is a flexible, high-temperature $(500^{\circ}\mathrm{C}$ max), radiation-resistant coaxial cable. It consists of a 24-gage stranded nickel-clad copper center conductor, an inorganic insulation, and a nickel-clad copper outer braid 0.200 in. in OD. Its capacitance is 35 pf/ft. The corrugated tubing provides watertightness and flexibility

with negligible elongation. The measured linear-expansion coefficients of the cable assembly are approximately $2 \times 10^{-4}$ per lb and $1 \times 10^{-5}$ per °C.

# Cable Between Preamplifier and Main Amplifier

This cable is a Raychem No. 10023 cable. It has preirradiated polyethylene dielectrics and jackets, is radiation resistant, and is a multilead coaxial cable. The center member of this composite cable is a shielded and jacketed two-conductor coaxial cable for the signals; around the center member are wound three 26-gage and two 20-gage hookup wires for preamplifier supplies, and over all of these are a nickel-clad copper shield and a preirradiated polyethylene jacket. The maximum overall OD is 0.324 in. The cable will withstand a maximum temperature of $125^{\circ}\mathrm{C}$ and an accumulated dose of $5 \times 10^{8}$ rads. Following this exposure the cable can still be coiled on a form whose diameter is ten times the overall cable diameter.

The Raychem cable is also enclosed within a watertight metallic envelope which may be varied for different reactor applications. The metallic envelope also serves as an electrical shield. For example, a stainless steel hose covered with polyvinyl chloride is used at the Oak Ridge Research Reactor (ORR).

# 2.3.2.4 Electrical Shielding Layout

Multiple electrical shields are provided to prevent excessive electrical noise pickup in the fission chamber and preamplifier assembly. Figure 2.3.9 shows, schematically, the general shielding and grounding layout. A first (or inner) shield covers the entire path of the signal from the fission chamber to the main amplifier input. This shield includes the cathode of the fission chamber, the outer braid of the BIW coaxial cable, a solid brass foil surrounding the preamplifier, and the two braids of the Raychem multilead coaxial cable. The preamplifier common mode, or ground, is electrically connected to the inner shield, which is electrically insulated from an outer shield, or shell, of the assembly. This outer shield includes the fission chamber casing, the corrugated flexible metal tubing between the chamber and the preamplifier, the preamplifier casing (insulated from the brass foil shield), the metallic envelope surrounding the Raychem cable (described previously), and a shielding which forms an extension of the metallic envelope to the main amplifier in the reactor control room. The grounding of the inner and outer shields is discussed in Sect. 2.3.2.5.

# 2.3.2.5 Low Pickup-Noise Performance of the Assembly

Extensive experimentation with different counting channels using this assembly was required to reduce its susceptibility to electrical noise pickup. The principal source of electrical noise pickup is electromagnetic radiation from ac power lines which are shock excited where some piece of equipment is turned on or off. The sensitivity to noise pickup has been minimized by the short separation distance between the preamplifier and the chamber, the large output signal from the preamplifier, the balanced configuration with common-mode noise rejection, and the multiple electrical shielding.

The lowest noise pickup is achieved with this assembly when the inner and outer shields are connected together in several places, for example, at the junction box and at the main amplifier, as shown in Fig. 2.3.9. This is contrary to the generally accepted precept of avoiding ground loops. Apparently, the capacitive coupling between shields defeats any attempt at isolation of the system from the building ground. With the connections described herein and shown in the Fig. 2.3.9, the pulses from pickup are no larger at the main amplifier input than the pulses of the alpha particles produced in the fission chamber, even when the assembly is located in the noisiest reactor installations available at ORNL.

# 2.3.3 Preamplifier Power Supply

# 2.3.3.1 General

The fission chamber and preamplifier dc power supply provides three regulated output voltages from an unregulated input supply of $-32 \pm 4$ v for use with the fission chamber and preamplifier assembly ORNL model Q-2617-1. The three outputs are: $+300$ v for polarization of the fission chamber, $+110$ v for the preamplifier anode supply, and $-22$ v for the preamplifier vacuum tube heaters and for biasing.

The -22 v is derived directly from the -32-v battery supply through a series regulator and a current-limiting circuit. The other two voltages, +300 v and +110 v, are developed by a dc-to-dc converter with a series preregulator.

# 2.3.3.2 Construction

The fission chamber and preamplifier dc power supply is contained in a module 4.25 in. wide, 4.72 in. high, and 11.90 in. deep. It is a standard "three-unit" plug-in module of the ORNL modular reactor instrumentation series depicted on drawings Q-2600-1 through Q-2600-5.

The circuits are on two printed circuit boards mounted parallel to each other and enclosed in a perforated metal shield to reduce electrical radiation and coupling to other modules. Adjustments and test points are accessible through the shield from the top of the module.

# 2.3.3.3 Application

The module is intended to supply all required voltages to the fission chamber and preamplifier assembly. Because the assembly is potted and unrepairable, the power supply is designed to limit currents and voltages to protect both the assembly and the power supply against damage from almost any conceivable combination of crossed connections or short circuits.

# 2.3.3.4 Specifications

Overall specifications for the preamplifier power supply are given in the following table.

# General

Power required -32 ± 4 v dc, 0.5 amp max Ambient temperature range 0 to $55^{\circ}C$

-22-v supply

Output voltage range

Output current range

Voltage regulation

Current limiting

-20 to -24 v dc

200 to 400 ma.

±1%

Adjustable to limit the output current to no more than $110\%$ of normal operating current from normal to short circuit

+300-v supply

Output voltage

Output current

Current limiting

Noise and ripple

+300 ± 15 v dc

0 to 100 μa

3 ma max, any load

100 mv max

+110-v supply

Output voltage

Output current

Current limiting

Noise and ripple

+110 ± 10 v dc

0 to 15 ma

100 ma max, any load

10 mv max

# 2.3.3.5 Circuit Description of the -22-v Supply

The -22-v supply consists of a voltage regulator (Q8, Q9, Q10) and a current-limiting circuit (Q7, D12, D13). The limiting circuit protects the series heater string of the preamplifier from damage when any of several possible fault conditions occur.

The action of the limiting circuit is similar to that of a constant-current circuit. The base voltage of Q7 is held constant at +2 v with respect to the -32-v supply by the two Zener diodes D12 and D13. The breakdown voltages of the diodes are 12 and 10 v, respectively, but they are connected in opposition so that the reference voltage is the difference in the two voltages. This arrangement yields a sharper knee and a stiffer reference voltage than a single low-voltage diode. The emitter voltage is different from the base voltage only by $V_{\text{be}}$ , the base-emitter voltage drop of the transistor, which is fairly constant. Thus, the emitter voltage is constant across a fixed resistance R22 and R26, yielding a constant current in the emitter of Q7, provided that the collector-emitter voltage is large enough to keep the transistor out of saturation. When "normal" output current is flowing (less than the limit current), the voltage at the collector of Q7 is less than 2 v more positive than the -32-v supply, and Q7 is saturated. In this condition Q7 simply acts like a series resistor and does not control the output current. It is only when the output current tends to increase above normal that Q7 comes out of saturation and limits the output current to

$$
I _ {\text {l i m i t}} = \frac {V _ {z} - V _ {\text {b e}}}{R 2 6 + R 2 2},
$$

where $V_{\mathbf{z}}$ is the difference in the breakdown voltages of D12 and D13 and $V_{\mathrm{be}}$ is the forward base-emitter voltage drop of Q7.

The voltage regulator consists of Q8, Q9, and Q10. The output voltage is sensed by the base of Q9 and is compared with the voltage of reference diode D14 in the emitter of Q9. The amplified difference on the collector of Q9 is applied to the base of Q8; Q8 provides current gain only to drive the base of the output transistor Q10. The regulated output voltage appears between the emitter of Q10 and ground. Diode D15 is used to protect Q8 from turnon transients.

The output voltage is adjusted with trimpot R30. The current at which the circuit limits is set with the "current limit" potentiometer R22.

2.3.3.6 Circuit Description of the +300-v and +110-v Supply

The supply is designed to operate from a nominal 32-v station battery with a terminal voltage variation from 28 to 36 v dc. This wide variation makes necessary a voltage preregulation, which consists of transistors Q1, Q2, Q3, and Q4.

The preregulator output voltage is sensed by resistors R7, R8, and R9 and applied to the base of amplifier stage Q3. A reference voltage (16.8 v) generated by Zener diode string D2, D3, and D4 is applied to the emitter of Q3. The amplified difference appears at the collector of Q3 and is applied to driver Q2 and pass transistor Q4. A constant collector current is provided for Q3 by transistor Q1, Zener diode D1, and the associated network.

The preregulator output (test point TPl) is filtered by C1, C2, and R27 and is applied to the dc-to-dc converter.

Q5, Q6, T1, and the associated circuitry comprise a free-running square-wave oscillator inverter. Networks C15-R32 and C16-R33 round the edges of the square wave somewhat to avoid the generation of sharp, high-frequency spikes, which may be coupled to other circuits. The 110-v output is obtained from a full-wave rectifier and filter, and the 300-v output from a voltage tripler. The supply can be short circuited without damage. Most transistor inverters will stop oscillating when overloaded. The oscillator transistors can be damaged unless their non-oscillating current is limited to a safe value. Current limiting by series resistance in a primary lead is undesirable because power will be wasted and the inverter will have poor load regulation. On the other hand, biasing so that the transistor current goes to zero in the non-oscillating condition will not allow oscillations to start when the short is removed. The current-limiting scheme used here consists of a combination of clamping and series-emitter resistance to set the current to a predetermined value. R11 and R12 bias the bases of Q5 and Q6 into conduction. R13 and R14 limit the transistor currents in the nonoscillating condition to a little less than the oscillating currents. The voltage drop across these resistors is less than the value that causes appreciable current flow through D5, D6, and D7 until oscillation begins. In the oscillating condition, the drops across R13 and R14, respectively, are limited by the diodes to 1.4 v. The low dynamic resistance of the diodes assures a stable, nonoscillating current value.

# 2.3.4 Pulse Amplifier

# 2.3.4.1 General

The pulse amplifier and count rate meter amplifies and counts pulses from a fission chamber. The input sensitivity is such that some preamplification is required. The module consists of a pulse amplifier, a pulse-height discriminator (PHD), a logarithmic count rate meter of the Cooke-Yarborough type, a linear count rate meter, and two calibration oscillators (10 and $10^{4}$ counts/sec).

# 2.3.4.2 Construction

The pulse amplifier and count rate meter is constructed in a module 5.6 in. wide, 4.72 in. high, and 11.9 in. deep. It is a standard "four-unit" plug-in module of the modular reactor instrumentation series depicted on drawings Q-2600-1 through Q-2600-5.

The pulse-height discriminator and the linear and log count rate circuits are constructed on one printed circuit board. The pulse amplifier and the two oscillators are constructed on separate boards. The pulse amplifier and discriminator count rate boards are housed in a cadmium-plated steel compartment which covers the entire top of the module. The two boards within this compartment are shielded from each other by a cadmium-plated partition. The oscillator printed circuit board is mounted horizontally at the back end of the module beneath the compartment.

The front panel controls include a ten-turn potentiometer for the pulse-height discriminator and an 18-position switch for amplifier gain control (13 positions) and module calibration control. A BNC connector is mounted on the front panel to provide a signal for aScaler.

# 2.3.4.3 Application

The pulse amplifier and count rate meter is one element of a wide-range counting channel<sup>1</sup> for monitoring neutron flux over a ten-decade span. It amplifies pulses from a fission chamber and preamplifier assembly<sup>4</sup> and provides logarithmic and linear count rate output signals. An output pulse is also provided to operate aScaler.

The pulses from the preamplifier assembly are bipolar in shape, which eliminates the problem of duty-cycle shifts in the pulse amplifier. The pulse amplifier, however, can be used with positive unipolar pulses. Count rates up to $10^4$ counts/sec of unipolar pulses 1 $\mu$ sec wide can be accommodated, with a resulting shift in effective pulse amplitude of less than $1\%$ .

The logarithmic output signal is a current which drives an external, conventional operational amplifier. The output of the operational amplifier is used to operate indicators and other circuits.

The linear output signal is also a current which drives an external, conventional operational amplifier. The output of the operational amplifier is used to operate other circuits. In the wide-range counting channel, this linear signal is used as the control signal for a servo system.

# 2.3.4.4 Specifications

Overall specifications for the pulse amplifier are as follows:

# Pulse amplifier

<table><tr><td>Gain</td><td>90 ± 5</td></tr><tr><td>Rise time (10 to 90%)</td><td>Less than 0.07 μsec</td></tr><tr><td>Linear pulse output</td><td>0 to +5 v</td></tr></table>

(100-ohm load or greater)

Saturated output

Attenuator control

Less than 7.5 v for pulse widths less than 0.5 μsec

13-position, 100-ohm ladder type at amplifier input in 1, 1.5, 2, 3, 5, and 7 sequence

# Pulse-height discriminator

<table><tr><td>Range</td><td>0.25 to +5 v with ten-turn Helipot (500 divisions)</td></tr><tr><td>Integral nonlinearity (including pulse amplifier)</td><td>Less than ±0.2% of 5 v from 0.25 to 5 v at 30°C and varies less than 0.03%/°C of its 30°C value between 0 and 50°C</td></tr></table>

# Output pulse forScaler

<table><tr><td>Amplitude</td><td>+3.5 ± 0.25 v into load of 100 ohms or greater</td></tr><tr><td>Rise time (10 to 90%)</td><td>0.05 μsec</td></tr><tr><td>Fall time (10 to 90%)</td><td>0.05 μsec (no output cable)</td></tr><tr><td>Pulse width</td><td>Varies with pulse amplitude in excess of PHD bias</td></tr></table>

# Log count rate output

Range 1 to $10^{5}$ counts/sec in five decades Amplitude 0 at 1 count/sec and up to approx 40 $\mu$ amp at $10^{5}$ counts/sec

Accuracy (at $30^{\circ}\mathrm{C}$ ) Output deviates less than $\pm 3\%$ from the true log reading at any point with regularly spaced input pulses  
Temperature effects Output deviates less than $\pm 1\%$ from the $30^{\circ}\mathrm{C}$ value for any temperature from 0 to $30^{\circ}\mathrm{C}$ ; from 30 to $50^{\circ}\mathrm{C}$ , output deviates less than $\pm 3\%$ from the $30^{\circ}\mathrm{C}$ value at each point

# Linear count rate output

<table><tr><td>Range</td><td>0 to 2.5 × 104counts/sec</td></tr><tr><td>Amplitude</td><td>Approximately 170 μamp at 104counts/sec</td></tr></table>

<table><tr><td>Accuracy (at 30°C)</td><td>Output deviates less than the equiv- 
alent of ±25 counts/sec from the 
true counting rate from 0 to 104 
counts/sec with regularly spaced 
input pulses</td></tr><tr><td>Temperature effects</td><td>The deviation of the 104 count/sec 
point from its 30°C value is less 
than 0.3%/°C from 0 to 30°C and 
less than 0.15%/°C from 30 to 50°C</td></tr><tr><td>Power requirements</td><td></td></tr><tr><td>Voltage</td><td>+25 ± 0.01 v; -25 ± 0.01 v</td></tr><tr><td>Current drain</td><td>75 ma from +25 v supply; 25 ma from 
-25 v supply</td></tr><tr><td>Regulation</td><td>±0.04% or better against ±10% line 
changes and with load changes 
from no load to full load</td></tr><tr><td>Ripple</td><td>Peak-to-peak ripple less than 0.01 v</td></tr><tr><td>10 count/sec oscillator</td><td></td></tr><tr><td>Stability</td><td>30 ppm at 20°C with vertical ori-
entation of spring balance wheel 
axis; 300 ppm at 20°C in any other 
orientation</td></tr><tr><td>Thermal error</td><td>11 ppm/°C from 0 to 30°C</td></tr><tr><td>Output pulse</td><td>-11.7 v, 6 msec width, less than 
20-μsec rise time (10 to 90%)</td></tr><tr><td>Output pulse load</td><td>50 kilohms minimum</td></tr><tr><td>Power supply</td><td>-12 v ± 10% at 0.15 ma average; 3-ma 
peak per pulse</td></tr><tr><td>104 count/sec oscillator</td><td></td></tr><tr><td>Calibration accuracy at 
70°C</td><td>Positive 0.000%; negative 0.004%</td></tr><tr><td>Thermal error</td><td>-4 ppm/°C at 70°C</td></tr><tr><td>Output pulse</td><td>8-v peak-to-peak square wave; less 
than 1-μsec rise time (10 to 90%)</td></tr><tr><td>Output pulse impedance</td><td>800 ohms</td></tr><tr><td>Power supply</td><td>-12 v ± 10% at 7 ma</td></tr><tr><td>Ambient temperature range 
(all units)</td><td>0 to 55°C</td></tr></table>

# 2.3.4.5 Theory of Operation

# General

The following description of the module (Fig. 2.3.10) is divided into five main groups: (1) pulse amplifier and control switch; (2) pulse-height discriminator, which includes the shaper stage and emitter-follower; (3) pump driver, which includes the flip-flop, Q-25 as a

limiter-amplifier, and Q16 and Q17 as the complementary emitter-follower drive; (4) pump circuits, which include both the log and linear pumps; and (5) test oscillators.

# Pulse Amplifier and Control Switch

The pulse amplifier consists of two fed-back groups which are cascaded to achieve an overall gain of 100. Each group has a voltage gain of about 10. These two stages of amplification are preceded by a ladder-type attenuator, where the input impedance is a constant 100 ohms at all settings and the impedance, looking back from the amplifier input, is 50 ohms. The attenuator is part of an 18-position switch that (1) provides attenuation of the input signal in 13 positions, (2) disconnects the amplifier input from the attenuator and grounds it through 100 ohms in two "off" positions, (3) disconnects the amplifier from the attenuator and applies $10^{4}$ counts/sec to its input, (4) disconnects the amplifier from the attenuator and applies 10 counts/sec to its input, and (5) disconnects the amplifier from the attenuator and supplies a dc voltage for application to a 5-sec period generator circuit that is external to the module. Also, in all positions other than attenuator positions, the control switch provides a dc voltage which actuates a front panel light and can be used to actuate an external alarm.

The pulse amplifier design is tailored to amplify pulses of the shape shown in Fig. 2.3.11A. This pulse shape is produced by a pre-amplifier which double differentiates the pulses from a fission chamber with a 0.125-μsec time constant. (The second differentiation is made at a pulse transformer which terminates the balanced transmission line driven by the preamplifier.) The preamplifier has a 0.1-μsec integrating time constant. The amplifier may also be used to amplify unipolar pulses clipped to 1 μsec width or less, with the possibility that appreciable base-line shift may occur at counting rates greater than $5 \times 10^{4}$ counts/sec.

Both fed-back groups are of identical design. Each fed-back group is a three-transistor configuration, with the first two transistors Q1 and Q2 constituting a differential pair. The output from the second collector Q2 drives the third transistor Q3, which is an emitter-follower. Feedback is made from the emitter of Q3 to the base of Q2. The output signal is taken from the emitter-follower, and the input signal drives the first base Q1 of the differential pair. This results in a group with an output pulse of the same polarity as that of the input signal. The pulse gain of the stage is very nearly $(\mathbb{R}6 + \mathbb{R}7) / \mathbb{R}6$ , neglecting the shunting effect of R8 and R6. The measured<sup>5</sup> high-frequency feedback factor for the stage was 10.

The fed-back group is dc-coupled and has excellent dc stability by nature of the differential input and a dc feedback factor in excess of 100. The bias in the amplifier has been selected so that both positive and negative portions of the bipolar input signal will be clipped proportionately under overload, thereby retaining its bipolar nature.

A closed-loop analysis, utilizing the hybrid-π equivalent circuit, shows that the predominant time constant is nearly $C_{\mathrm{ob}} R_{16} \left[ (R_{\mathrm{b}}' + R_{15}) / R_{15} \right]$ , where $C_{\mathrm{ob}}$ and $R_{\mathrm{b}}'$ are the collector transition capacitance and base resistance of Q2 respectively.

The output impedance of the stage was computed to be 12.6 ohms.

The ac input impedance of the stage is very nearly equal to that of the base resistor Rl of the input transistor Ql, because the emitter impedance of Ql is R2 (5.1 kilohms) in parallel with the looking-in impedance of Q2, which is nearly 300 ohms because of the feedback to the base of Q2. Thus, with an effective emitter impedance of about 300 ohms, the impedance looking into the base of Ql is about 30 kilohms for an $h_{fe}$ of 100.

Capacity coupling is used between the two fed-back stages and on the output to the pulse-height discriminator. These coupling time constants are in excess of 300 $\mu$ sec, which is adequate to eliminate the effects of any further differentiation. The bipolar nature of the input signal eliminates any possible duty-cycle shifts across these capacitors.

# Pulse-Height Discriminator

The pulse-height discriminator (PHD) is based on a biased amplifier scheme which is very similar to that used in the pulse amplifier. The PHD control potentiometer R26 has ten turns, and the dial has 500 divisions. The position of R26 determines the differential bias that exists between the bases of Q7 and Q8. Since Q8 is conducting at any position of this potentiometer, any positive input signal applied to the base of Q7 must exceed this differential before Q7 is brought into conduction, and any portion in excess of this differential is amplified by a factor of 10.

The voltage drop across the PHD potentiometer R26 must be 5 v to achieve the full-range control of 5 v for pulse-height discrimination. The voltage can be trimmed to this value by adjusting R32. The "zero" of the PHD can be trimmed by adjusting the values of R24 and R27.

$$
{ } ^ { 6 } \text { T h e ~ o u t p u t ~ i m p e d a n c e ~ } R _ { O } ^ { \prime } = \frac { V ( \text { o p e n ~ c i r c u i t } ) } { I ( \text { s h o r t ~ c i r c u i t } ) } = \frac { e _ { i } ( A ) } { e _ { i } ( A ) / R _ { O } } = R _ { O } \left( \frac { A ^ { \prime } } { A } \right) ,
$$

where

$$
A = \text {o p e n - l o o p} 1 0 0,
$$

$$
A ^ {\prime} = \text {c l o s e d - l o o p g a i n}, 1 0,
$$

$$
R _ {0} = \text {o p e n - l o o p o u t p u t i m p e d a n c e}.
$$

$$
\begin{array}{l} \text {I n} \quad \mathrm {R} _ {\mathrm {o}} = \mathrm {r} _ {\mathrm {e}} + \frac {\text {b a s e i m p e d a n c e o f Q 3}}{\mathrm {h} _ {\mathrm {f e}} \text {o f Q 3}} \\ = 2 6 + \frac {1 0 ^ {4}}{1 0 0} = 1 2 6. \\ \end{array}
$$

An ac-coupled Schmitt trigger is used to shape the pulse from the biased amplifier. The trigger sensitivity is 2.5 v. A more sensitive trigger will create stability problems even though any sensitivity changes are reduced by a factor of 10 when referred to the pulse amplitude. The sensitivity cannot be less than 0.5 v, because this is about the amplitude of "feed-through" pulses of the biased amplifier.

Another consideration for keeping the Schmitt trigger sensitivity large is to relax the bandwidth requirements of the biased-off amplifier. The triangular-shaped character of the positive portion of the amplifier pulse places a bandwidth burden on the biased-off amplifier for the pulses which barely exceed the threshold level. The larger the pulse required to actuate the Schmitt trigger, the greater the output required from the biased amplifier. These larger pulses, because of their triangular shape, will be wider at the base line and will require less bandwidth from the amplifier.

The 2.5-v sensitivity of the Schmitt trigger results in PHD potentiometer control that is ineffective below a pulse amplitude of 0.25 v. This is only $5\%$ of the 5-v full range and is considered to be only a minor limitation. Trigger sensitivities in excess of 2.5 v would result in even less usable portions of the PHD potentiometer and would not be desirable.

Transistor Q7 of the biased amplifier must have a base-to-emitter breakdown voltage greater than 5 v. The 2N2432 transistor designed for inverted chopper applications has a 15-v BV rating.

The pulse out of the Schmitt trigger is applied to emitter-follower Q12. The magnitude of this pulse is $+3.5\mathrm{~V}$ , and its width depends on the amount that the pulse amplifier pulse exceeds the bias setting (of the PHD). The emitter-follower output drives the succeeding binary stage and an external scalar. The recovery of the pulse at the emitter-follower will be slow at the termination of each pulse if an unterminated cable is used to make connection to a scalar, because the charged cable will hold Q12 off and must be discharged through R47, a 6.2-kilohm resistor.

# Pump Driver

The pulse from the Schmitt trigger and its emitter-follower does not have the proper amplitude or the width to drive the log and linear pumps. A binary stage (also called a flip-flop) is used to further shape the pulse. The output pulse of the flip-flop is rectangular, having a width equal to the time elapsed between two successive pulses. This method of shaping automatically provides the pump circuits with wide pulses without any increase in dead-time losses. The consequent division of the pulse rate by a factor of 2 must, of course, be considered in the pump design.

The flip-flop design composed of Q13 and Q14 is a saturated type (i.e., the "on" transistor is driven into saturation) with resolution capabilities of $10^{7}$ counts/sec. When either Q13 or Q14 is "on," the other is "off." The positive pulse from the emitter-follower acts to turn the "on" transistor off, and the regenerative nature of the circuit then switches the state of the flip-flop. Diodes D2 and D6 serve to steer or apply the pulse to the base of the "on" transistor. To understand how the steering is achieved, assume Q13 to be "on" and Q14 to be

"off." The collector of Q13 will be near +8.5 v, and the collector of Q14 will be near ground. Diodes D6 and D5 are in series and are back biased by the difference in potential between the collector and base of Q14 (about 8.5 v). The base of Q14 is clamped to a potential slightly more positive than +8.5 v by D4. (The only purpose for D3 and D4 is to limit the back bias applied to Q13 and Q14 when they are turned off. With these diodes the back bias can never exceed about 0.5 v.) In contrast, diodes D1 and D2, which are also in series, are only back biased by a few tenths of a volt. Thus, a positive input pulse will take the route through D2 (and to the base of the "on" transistor) in preference to that through D6 because of the greater bias on D6.

Diodes D1 and D5 aid in another manner. They help discharge capacitors C19 and C20, respectively, by providing a low-impedance path to C21 (a 2.2-µf capacitor) through the collector of the "on" transistor between input pulses. These capacitors will acquire some charge as the input signal proceeds to turn off the "on" transistor and, if permitted to accumulate or to not sufficiently recover, can cause a malfunction of the flip-flop.

The collector swing of Q13 and Q14 is approximately 8 v. This value is marginal to provide reliable operation of a pump circuit. Also, the pump circuit input impedance is quite low and would drastically load the flip-flop and impair its speed. Thus, some further amplification is still required, and some impedance isolation is needed. It should be recognized that any amplification process must also achieve high amplitude stability to achieve good pump performance. Transistors Q15, Q17, and Q16, along with diodes D13, D14, D15, D16, and D17, are used to perform this task. Diodes D13 and D14 are fast-recovery conventional diodes, and diodes D15, D16, and D17 are 5.2-v Zener diodes. The role of D7 will be explained below.

Amplification with controlled amplitude is accomplished by Q15, the two fast diodes, and the three Zener diodes. The collector current of Q14 forward-biases diode D7 and turns Q15 off "hard." The collector of Q15 is caught at approximately $-17\mathrm{v}$ by the series string of the two fast diodes and the three 5.2-v Zener diodes. When Q14 is turned off, D7 is released and Q15 is turned on "hard" by the base drive through R53. Thus, the collector swing of Q15 is from $-17\mathrm{v}$ to essentially $0\mathrm{v}$ . The two diodes in series with the Zener diodes isolate the large capacitance of the Zener diodes from the collector of Q15, permitting fast rise and fall times. One diode is adequate for this isolation, but two diodes give better temperature compensation for diode effects on the diode pumps. The Zener diodes have a specified rating of $0.005\%$ per $^\circ \mathrm{C}$ change, and the variation of the saturation voltage of Q15 is less than a few tenths of a millivolt per $^\circ \mathrm{C}$ .

It should be apparent that the scheme just described is one where the collector current of Q14 is sampled, rather than its collector voltage, so that amplification is not achieved in the usual sense. However, the method employed is one where no loading is placed on the flip-flop, permitting it to operate at maximum speed.

Transistors Q16 and Q17 comprise a complementary emitter-follower driving stage which applies the 17-v pulses to the pump circuits. The necessity of a complementary design over that of a single emitter-follower can be explained if we momentarily include the pump circuits in

the discussion. The following section will discuss these in greater detail. The negative-going step of the 17-v pulse proceeds to charge the feed capacitors of the pump circuits (C26 through C30 for the log pumps and C39 for the linear pump) through their respective diodes (D18, D20, D22, D26, D28, and D32) to the full 17 v. On the positive-going edge of the pulse (or the return to ground), these capacitors must now be discharged quickly to 0 v to be prepared for the next pulse. This discharge path must proceed through the second diode of each pump into the smoothing capacitor or output capacitor of each pump for proper action of the pump. At this time Q17 is biased off and cannot provide this discharge. Q17 is off, since its base is at or near ground, and its emitter is at -17 v because the feed capacitor is behaving as a 17-v battery. With Q16 in the circuit as the NPN complement, it will be biased "on" and will permit the feed capacitor to discharge.

# Pump Circuits

Logarithmic Pumps. - The log pump design is composed of six pumps and is based on the earlier work of Cooke-Yarborough.[7] The dc currents from each pump are summed at the common junction of R88, R90, R92, R94, R96, and R98 and are delivered to the summing junction of an external operational amplifier. The composite response of six pumps is shown in Fig. 2.3.12. Since the output voltage of each pump is positive, the conventional current flow will be out of these resistors. An additional current of opposite polarity is supplied through Rl13 and is adjustable by the "calibrate" control potentiometer Rl12. The gain of the external amplifier and hence the "span" of the log count rate meter are controlled by the parallel combination of Rl15 and Rl16. For trimming purposes the value of Rl16 is adjusted. A 250-kilohm feedback resistor for the operational amplifier, in addition to a l-kilohm resistor which forms a voltage divider network with Rl15 and Rl16, is located at the operational amplifier. If these resistors were located in the pulse amplifier and count rate meter module and the module were unplugged, it would open-circuit the feedback loop on the operational amplifier and cause the operational amplifier to saturate. It is not advisable to leave these amplifiers in this state for extended periods of time.

The operation of the pump circuit, discussed briefly in the preceding section, will be described in more detail here. As charge from the feed capacitor is transferred to the smoothing capacitors C32 through C37, a voltage is developed across these capacitors which causes the current flow through any shunt resistance such as R88 and R87 of the first pump. R88 is essentially returned to ground since it is tied to the summing junction (a virtual ground) of the external operational amplifier. At a steady count rate, there is an equilibrium condition established where the rate of charge, or current inflow, is equal to the current outflow, and a steady dc voltage (with superimposed statistical variation) is established across each smoothing capacitor.

The voltage on each smoothing capacitor will bear the relationship<sup>8</sup>

$$
v _ {o} = \frac {V _ {i} n R C}{1 + n R C},
$$

where

$\mathbf{V}_{\dot{\mathbf{i}}} =$ input pulse amplitude,

$\mathbf{n} =$ detector count rate divided by 2,

$\mathbf{C} =$ capacity of feed capacitor,

$\mathbf{R} =$ total shunt resistance across smoothing capacitor.

This response is shown graphically by any of the six curves in Fig. 2.3.12. For small values of $n$ , where nRC is small compared with unity, the response is nearly linear as a function of $n$ , the count rate. As $n$ becomes larger, the response becomes nonlinear (appearing to be linear on a semilog plot) and ultimately reaches a saturation value of $V_{i}$ when nRC is much greater than unity. As the count rate increases, each pump becomes successively saturated (pumps with the largest RC product saturate first), resulting in a constant output current from each pump.

The Cooke-Yarborough principle will show end effects when a limited number of pumps are used to approximate the logarithmic response. To compensate for this, the two end pumps deliver about $10\%$ more current than the four middle pumps. This is accomplished by making the value of the feed resistors R88 and R98 smaller than that of the other four feed resistors R90, R92, R94, and R96. The values of the shunt resistors R87, R89, R91, R93, R95, and R97 are adjusted to keep the pump time constant RC at values which differ by a factor of 10.

The derivation is as follows:

$$
v _ {o} = i _ {o} R,
$$

where

$$
i _ {o} = \frac {\Delta Q}{\Delta t} = \frac {(v _ {i} - v _ {o}) c}{1 / n} = (v _ {i} - v _ {o}) n C.
$$

Thus

$$
\begin{array}{l} v _ {o} = \left(v _ {i} - v _ {o}\right) n C R \\ = \frac {V _ {i} n R C}{1 + n R C}. \\ \end{array}
$$

The value of the total shunt resistance R across each smoothing capacitor was made as small as possible, but still permitting reasonable values of smoothing capacitors (i.e., values less than 100 μf). The product of the resistance and the smoothing capacitor values determines the statistical noise superimposed on the dc current. The values shown were determined by experiment on the complete wide-range counting channel. The first three time constants involving C32, R33, and C34 were selected to keep the period noise at reasonable values while the wide-range counting channel was behaving as a straight counting instrument. The remaining three time constants were selected to optimize the speed of response of the counting channel.

The leakage of the smoothing capacitors and diodes D19, D21, D23, D25, D27, and D29 behaves as an additional shunt resistance across the various pump outputs. The LN914A is specified to have a maximum leakage of 0.025 μa at a reverse bias of 20 v at $20^{\circ}\mathrm{C}$ . This will have negligible effect on the performance of the pumps. The electrolytic capacitors C32, C33, and C34 were purchased with a specified leakage not to exceed 0.2 μa at $25^{\circ}\mathrm{C}$ at a working voltage of 20 v, which is equivalent to a dc leakage resistance of 100 megohms. A reduction in leakage resistance to 50 megohms would represent an error of 2.5% of reading over only a small range of the scale. Also, errors caused by leakage of the capacitors will not accumulate, because as each pump goes into saturation, its output current is a function of only the pulse amplitude and the magnitude of the resistor feeding the summing junction of the operational amplifier. In addition, any errors caused by the three electrolytic capacitors, since they apply to the pumps at the low end of the scale, are negligible at the high end.

The other critical components of the various pumps, such as the feed capacitor and output resistors, are high-quality, high-stability $\pm 1\%$ components, or better.

The effect of the variation of diode potentials in the pump is equivalent to a variation of the amplitude of the input pulse. The effect is such that, at higher temperatures, the input pulse appears bigger and there is greater output from the pump. More clearly, as the forward drop of D18 reduces with a temperature increase, the feed capacitor will charge to a larger voltage. Also, the forward drop across D18 is less, and more charge is transferred. The two diodes D13 and D14 in series with the three 5.2-v Zener diodes have a tendency to compensate for this. As the temperature rises, the forward drop of these two diodes will be less and will result in a reduced pulse amplitude.

Linear Pumps. - The linear pump circuit is designed to give a linear output current signal up to a value of about $170\mu \mathrm{a}$ for $10^{4}$ counts/sec. This current is fed through R99, a 10-kilohm resistor, into the summing junction of an external operational amplifier. This amounts to a voltage of +1.7 v at the output of the pump.

Without any attempt (such as bootstrapping) to improve linearity, the output signal would depart from linearity by nearly $9\%$ . This can be computed from the general count rate expression given in the preceding

section with RC = (R99)(C39) = (10^4)(0.0022)(10^-6) and n = 5 × 10^3 counts/sec. The bootstrapping circuit consisting of Q18 and Q19 serves to effectively increase the magnitude of the input pulse by an amount equal to the output dc voltage. Discounting the small drop in R117, any change in the output voltage appears at the anode of D32 and is in a direction to increase the voltage to which the feed capacitor is charged with each input pulse. Thus, the output current without bootstrapping is

$$
i _ {o} = \frac {\left(v _ {i} - v _ {o}\right) c}{1 / n}.
$$

This becomes

$$
i _ {o} = \frac {\left[ \left(v _ {i} + v _ {o}\right) - v _ {o} \right] c}{1 / n},
$$

which is independent of $\mathbf{v}_0$ . Here all terms have the same meaning as in the preceding section.

The cascaded emitter-follower arrangement (Darlington pair) is used to raise the looking-in impedance of the bootstrapping circuit, thereby reducing its loading effect on the output voltage. The voltage drop of the base-to-emitter voltages of Q18 and Q19 plus the drop across R117 is of sufficient magnitude to ensure that D31 is sufficiently back biased during the charging time of the feed capacitor to avoid a leakage of charge from the smoothing capacitor.

Temperature effects in the linear diode pump are due primarily to changes in the two diodes D31 and D32. Variation in the forward voltages of these two diodes is compensated for by changes in input pulse amplitude in a manner described in the preceding section. Diode leakage currents and leakage in the electrolytic smoothing capacitors are negligible, particularly since the value of the output resistor is only 10 kilohms.

Temperature effects caused by the bootstrapping scheme are small, but are not negligible. $V_{\text{be}}$ changes of Q18 and Q19 will have a significant effect on the output. These changes will predominantly show up as a change in emitter potential of Q19 of about 4 mv/°C. Only slight changes of $V_{\text{be}}$ due to temperature are seen at the base of Q18, because the 10-kilohm base impedance of Q18 is so much smaller than the looking-in impedance of Q18. The variations at the emitter of Q19 will change the magnitude of the bootstrapping voltage with temperature. At 50°C (assuming 4 mv/°C) the change in bootstrapping signal from the 30°C value is 120 mv, which is a change in output signal of [0.120/(17 × 20)]100, or 0.03%/°C, where 17 v is the amplitude of the input pulse. This change is in a direction to increase the output signal. If the output signal from the bootstrapped configuration had been taken from the emitter of Q19, the 0.03%/°C value will be increased by an addi

tional [0.120/(1.7 × 20)]100, or $0.3\% / \circ \mathrm{C}$ , at $10^{4}$ counts/sec. This occurs because the pump output voltage (1.7 v at $10^{4}$ counts/sec) receives the full effect of the $\mathbf{V}_{\mathrm{be}}$ changes.

The actual temperature drift observed on the pump operating at $10^{4}$ counts/sec is three times worse than $0.03\% /^{\circ}C$ . At 5000 counts/sec the measured drift is more nearly $0.03\% /^{\circ}C$ . The cause of the increased drift at the $10^{4}$ -count/sec rate, which nearly amounts to an additional $2\mathrm{mv} / ^{\circ}C$ , is not definitely known.

I co and the base current of Q18 will flow through R99 into the summing junction of the external amplifier and appear as signal currents. I co effects will be negligible, because 0.001 μa is typical for Q18 and Q19 (NPN silicon). Temperature effects on h FE are also small, since the base current of Q18 is about 0.5 μa, or about 0.3% of the full-scale output (i.e., 170 μa at 10⁴ counts/sec). The h FE value varies about 0.4%/°C in the range 0 to 50°C.

# Test Oscillators

10-count/sec Oscillator. - This is a Swiss-made (Zenith model E59GJ) electromechanical oscillator with a spring balance wheel mounted in ruby bearings. The spring balance wheel is driven by an electronic circuit containing two transistors and two coils. The two coils are fixed and are located coaxially above and below a permanent magnet set in the rim of the balance wheel. The axis of the magnet is parallel to the axis of rotation of the spring balance wheel. As the magnet passes through the region between the coils, a voltage induced in one coil (the pickup coil) turns on a transistor amplifier which has the second coil (the drive coil) as a collector load. The current in the drive coil imparts a force to the balance wheel in a direction to sustain its movement. The output pulse is taken from the collector of the amplifier transistor. The other transistor is connected as an emitter-follower and provides the necessary power amplification for the signal from the pickup coil.

The oscillator produces an output pulse of the same polarity each time the magnet passes under the coils. This results in two pulses for each complete cycle. The time duration between successive pulses can differ by as much as 3 msec; however, the sum of the two intervals remains precisely at 0.1 sec (i.e., a 10-count/sec rate). The variation in time duration arises because the spring on the balance wheel is wound in one direction and is unwound in the other direction.

$10^{4}$ -count/sec Oscillator. - The $10^{4}$ -count/sec oscillator is crystal-controlled by a $10^{4}$ -count/sec quartz crystal. The oscillator consists of an Engineered Electronics Company. (EECO) plug-in unit T-107, requiring a standard nine-pin miniature tube socket. The quartz crystal (EECO type H145-31) is mounted separately. The T-107 unit contains three transistors, two of which are used as a two-stage common emitter amplifier with feedback from the second collector to the first base through the impedance of the crystal. There is a full $360^{\circ}$ phase shift, and the circuit will oscillate at a frequency which experiences neither phase shift nor appreciable attenuation through the crystal. The third transistor serves as an emitter-follower output stage.

Oscillator Shaper. - Since the output waveforms of the 10- and the $10^4$ -count/sec oscillators are widely different, preshaping is required if a uniform pulse is to be applied to the pulse amplifier. Q20 and Q21 form a conventional Schmitt trigger for this purpose. Q21 is normally on and Q20 is off. The sensitivity is such that about 4 v is needed for triggering. The output pulse from the collector of Q21 is a positive pulse which is sharply differentiated by C38 and R86. The resultant pulse is about 0.1 v in amplitude. A negative pulse of about the same amplitude is obtained, but it is of the wrong polarity to trigger the pulse-height discriminator.

# 2.3.5 0.1-hp Servo Amplifier, ORNL Model Q-2615

# 2.3.5.1 General

The 0.1-hp dc servo amplifier is a dc power amplifier that can supply a maximum of 75 w power at voltage and current limits of 25 v and 5 amp respectively.

# 2.3.5.2 Construction

The servo amplifier is constructed in a module 4.22 in. wide, 4.72 in. high, and 11.9 in. deep. It is a standard "three-unit" plug-in module of the modular reactor instrumentation series depicted on drawings Q-2600-1 through Q-2600-5.

The four output transistors are mounted on separate heat sinks; these are supported by four rods that connect the front and back plates of the module. The four intermediate transistors of the amplifier are mounted on smaller separate heat sinks; these are clustered on a metal plate supported by the four tie rods.

The input transistor and most of the other components of the amplifier are mounted on a printed circuit board near the front panel of the module.

The series limiting resistors for the output transistors are mounted on the rear plate. All decoupling resistors and capacitors are mounted on a metal plate supported by the four tie rods and located near the rear of the module. This metal plate also shields the amplifier from the heat that is dissipated in the limiting resistors.

# 2.3.5.3 Application

The servo amplifier drives a Globe Industries, Inc., type BD dc motor with a 27-v armature. It can drive this motor under all conditions from no load to blocked rotor. The motor is used as the servo motor to position a fission chamber in a wide-range counting channel.

# 2.3.5.4 Specifications

Specifications for the 0.1-hp dc servo amplifier are as follows:

Voltage gain

3 v/v ± 10% noninverting

Maximum linear output

$\pm 28$ v at no load; $\pm 25$ v with 12-ohm

(supply voltage $\pm 32\mathrm{v}$ )

resistive load; and $\pm 15$ v with

3-ohm resistive load

Nonlinearity (with 12-ohm resistive load)

Maximum power output

Output impedance

Input impedance

Input dc offset (input voltage for zero output)

Transient response

Zero drift with temperature

Power supply requirements Voltage Current drain

Ambient temperature range

Less than 0.1 v deviation from straight line drawn between maximum positive and negative outputs

75 w

30 milliohms

4700 ohms for signals not exceeding $\pm 10\mathrm{v}$

Negative 0.8 v

Rise time (10 to 90%) less than 2 msec for input step

Less than $9\mathrm{mv} / {}^{\circ}\mathrm{C}$ from 0 to $50^{\circ}\mathrm{C}$ ; the output decreases as the temperature rises

Positive and negative $32\mathrm{v}\pm 4\mathrm{v}$ 5 amp maximum

0 to $55^{\circ}C$

# 2.3.5.5 Theory of Operation

# General

The 0.l-hp dc servo amplifier is a dc-coupled amplifier with feedback around two voltage-gain stages and two cascaded emitter-followers. The emitter-follower stages are complementary NPN and PNP pairs to permit the output to swing negative and positive with respect to ground. The last emitter-follower stage is a parallel combination of two transistors to increase its power handling capabilities.

# Circuit Description

Reference is made to Instrumentation and Controls drawing Q-2615-1. The input signal is applied to the base of Q1, a PNP silicon transistor. A 1-kilohm resistor R2 in series with the base limits the maximum load placed on the input signal in the event of any failure in the servo amplifier. Diode D2 limits the base-to-emitter voltage on Q1 when large negative input signals are applied under blocked rotor conditions.

Negative feedback is applied to the emitter of Q1 through the resistive network R3 and R8. The feedback ratio is $\frac{R3}{(R3 + R8)}$ , which gives a closed-loop voltage gain of approximately 3.

The circuit shown produces a dc offset between input and output. With no input, the voltages will be as shown (+2.4 v on the output and 0 v on the input). For the output to be at a zero potential, the base of the input transistor must be at a negative 0.8 v to keep Q1 in a conducting state.

Voltage gain in the loop is obtained from Q1 and Q2. Q3 is a current source which functions as a high-impedance collector load for Q2 while still providing adequate current to drive the emitter-follower stages under all design conditions. When the servo amplifier is driving positive with respect to ground, part of the collector current of Q3 is diverted into the base of Q5. When the servo amplifier is driving negative with respect to ground, all the Q3 collector current flows through Q2, and Q2 must be capable of handling this current plus the required drive current into the base of Q4.

Transistor Q4 and transistors Q6 and Q8 in parallel function as an emitter-follower chain; they operate when the servo amplifier is driving negative with respect to ground. Transistor Q5 and transistors Q7 and Q9 in parallel operate when the servo amplifier is driving positive with respect to ground. The transistor not operating is held in a back-biased state by the base-to-emitter voltage of its complement.

Diode D1 in the emitter of Q2 permits Q2 to be turned off "hard" when the amplifier is delivering its full positive output. Any small collector current could create a large dissipation in Q2, since Q2 will have in excess of 60 v from collector to emitter.

Capacitor C1, connected from the base to the collector of Q2, along with the collector impedance of Q1, shapes the open-loop response to improve the high-frequency stability. The total capacitance at the collector of Q1 is increased in magnitude by the Miller effect. This results in a smaller value of capacitance for the same shaping of the open-loop response. This internal time constant, coupled with the compensating effect of C2 across R8, stabilizes the amplifier over its entire range of operation with as much as $0.22\mu \mathrm{f}$ capacitance in shunt with the output.

The behavior of the amplifier with a step input signal is different with positive and negative input signals. With a negative input step, Q1 and Q2 are immediately driven into a higher conducting state, and the output rise time is exponential in character and is controlled primarily by the value of C2. With a positive step, Q1 and Q2 are both immediately turned off in the absence of a return signal from the feedback network. Thus, the current from Q3 flows into Cl, generating a ramp until there is sufficient signal from the feedback network to return Q1 to a conducting state and thereby restore the closed loop. Under these conditions the output wave shape will have a ramp-type leading edge.

Resistors R9 and R12 in the emitter of Q6 and Q8 tend to balance the current contribution of each transistor, even with large differences in transistor parameters, such as current gain and transconductance. Resistors R10 and R13 are used for the same purpose with transistors Q7 and Q9.

Resistor Rll, which is a series combination of three 1-ohm resistors, protects transistors Q6 and Q8 under severe load conditions. With a blocked rotor condition the Globe Industries type BD motor will behave as a 3-ohm load, and the maximum dissipation possible in either parallel transistor is about 27 w. This is assuming supply voltages of $\pm 36$ v. These potentials are possible when the batteries that normally power this module are fully charged. Resistor Rl4 provides similar protection for transistors Q7 and Q9.

The collectors of Q4 and Q5 are connected to resistors R11 and R14 respectively. This prevents damage to these transistors under overload conditions.

# 2.3.6 Vernistat

# 2.3.6.1 General

The Vernistat adjustable function generator is composed of two separate, but integral, units: a function adjusting assembly and an interpolating Vernistat potentiometer. A function is set up simply by manually adjusting the positions of sliders on the function adjusting assembly panel. The panel is marked off in rectangular coordinates, with percent output as the ordinate and shaft position as the abscissa. The sliders provide a visual plot of the function that is set into the function generator. By rotation of the shaft of the interpolating Vernistat with an excitation voltage applied, the output voltage curve conforms to a series of straight-line interpolations between voltages set up by the slider. Clockwise rotation scans the function from left to right (i.e., from slider 1 to slider 34).

# 2.3.6.2 Construction

# Vernistat Function Adjusting Assembly

The function adjusting assembly is approximately 1 by 7 by 8 in. and contains (1) a 101-tap voltage divider; (2) a 34-pole, 101-position printed-circuit switch; and (3) a function adjusting panel.

The voltage divider has a total of 101 equally spaced taps. These taps divide the input voltage into 100 equal voltage increments.

The 34-pole, l01-position switch is a rectangular coordinate array. A printed-circuit grid consists of l01 parallel lines connected sequentially to the voltage-divider taps. Each of the 34 sliding contacts can be moved independently across the grid lines so that each slider may contact any of the l01 voltage divider taps. The voltage divider taps are spaced at $1\%$ increments, and therefore any voltage may be selected to within $\pm 0.5\%$ .

A panel, marked off in rectangular coordinates, mounts directly over the printed circuit switch so that the 34 sliders protrude through slots in the panel and can be manually adjusted. The Y axis is proportional to voltage, and the X axis is proportional to the position of the interpolating Vernistat shaft. The X axis represents a range of approximately 11 shaft turns.

# Interpolating Vernistat Potentiometer

The interpolating Vernistat consists of (1) a series of commutator bars which correspond to the sliders of the function adjusting assembly, (2) a switching mechanism, and (3) a $360^{\circ}$ toroidal resistance element precisely tapped at $120^{\circ}$ intervals. Connection of the function adjusting assembly to the commutator bars of the interpolating Vernistat is made through a multiconductor cable. This cable is an integral part of the

interpolating Vernistat and plugs into the function adjusting assembly. This is the only connection made to the function adjusting assembly.

Rotation of the shaft of the interpolating Vernistat switches the taps of the interpolating resistance element one at a time along the commutator and simultaneously controls the potentiometer output wiper. There are approximately three interpolations per shaft turn of the interpolating Vernistat.

# 2.3.6.3 Application

The Vernistat adjustable function generator provides a convenient means of generating mathematical and empirical nonlinear functions.

The function generator is used in the wide-range counting instrument to modify a linear position signal so that it is equal to the logarithm of the neutron attenuation.

# 2.3.6.4 Specifications

Overall specifications for the Vernistat function assembly are given below:

Vernistat Function Adjusting Assembly

Adjustable points on 34 rotation axis

Resolution of slider ad- 1% justment

Maximum input voltage 50 v

Ambient temperature range 0 to $55^{\circ}C$

Interpolating Vernistat Potentiometers (size 18, 11-turn continuous rotation units)

Linearity ±0.02%

Maximum output impedance 540 ohms

Minimum output-voltage 0.01% increment

Ambient temperature range 0 to $55^{\circ}C$

# 2.3.6.5 Applicable Drawings

The Instrumentation and Controls Division drawing number and subtitle for the Vernistat adjustable function generator is Q-2616-1, Circuit.

# 2.3.6.6 Theory of Operation

Figure 2.3.13 shows the electrical relation of the Vernistat interpolator commutator bars, interpolating resistance element, and output wiper. By synchronization of the switching of the interpolating resistance element taps along the commutator bars with the movement of the potentiometer wiper arm, the voltage output becomes a series of

linear voltage interpolations between adjacent commutator bars. The interpolating resistance element, used repetitively for each shaft turn, is a $360^{\circ}$ toroidal potentiometer precisely tapped at $120^{\circ}$ intervals.

Switching of resistance element taps from one commutator bar to the next only requires about $30^{\circ}$ of shaft rotation, whereas a complete interpolation requires approximately $120^{\circ}$ . Therefore, the switching process of the interpolating resistance element is a noncritical operation. No discontinuities of output occur, since in each instance as the output wiper approaches a new commutator bar, the next interpolating resistance element section is already in position. Switching of the taps of the interpolating resistance element along the commutator bars is accomplished with a planetary gear reduction.

The output wiper is so synchronized with the switching operation that it is always on an energized section of the resistance element. This results in continuous, smooth interpolation throughout the output voltage range.

The heart of the switching mechanism is a planetary gear reduction that consists of three elements: an internal tooth gear with as many teeth as there are commutator bars, a planetary gear with one tooth less, and an eccentric on the shaft which keeps the two gears in mesh. These gears are shown schematically by the eccentric circles in Fig. 2.3.13. Because of the one-tooth difference, one shaft rotation results in a counterrotation of the planetary gear, which is equivalent to the angular spacing between commutator bars.

The resistance element is mounted on the planetary gear and rotates with it at a reduced speed. The commutator wipers, connected to the resistance element taps, are also mounted on the planetary gear. The output wiper is attached to the Vernistat shaft. Because the resistance element rotates, the output wiper moves from one tap to the next in less than $120^{\circ}$ of the shaft rotation.

The 34 sliders of the function adjusting assembly equal the number of commutator bars in the interpolating Vernistat. Eleven shaft turns $(3960^{\circ})$ are required to generate an entire 34-chord function. Each chord represents $116.47^{\circ}$ $(3960^{\circ} / 34)$ of shaft rotation.

Sliders 34 and 1 are adjacent electrically; therefore, a repetitive function may be generated by continuous rotation of the input shaft.

# 2.3.7 Dual DC Amplifier

# 2.3.7.1 General

The ORNL model Q-2605-1 dual dc amplifier is designed and manufactured by Electronic Associates, Inc., as the EAI model 6.720. The unit consists of two independent high-gain amplifier circuits packaged on an etched-circuit board. The amplifiers are transistorized and designed for optimum stability and frequency response. Each amplifier can be used in conjunction with appropriate networks to perform linear computations such as summation, integration, and multiplication by a constant.

# 2.3.7.2 Specifications

Specifications for the dual dc amplifier are given below:

<table><tr><td>Output voltage range</td><td>±1.2 v min (no load); ±10 v min (20 ma load)</td></tr><tr><td>Offset (at the summing junction)</td><td>±20 μv, max</td></tr><tr><td>unity-gain inverter with 10-kilohm resistors</td><td></td></tr><tr><td>Output current at ±10 v</td><td>20 ma min</td></tr><tr><td>Frequency response (-3 db) for a unity-gain inverter with 10-kilohm resistors (20 μv p-p input)</td><td>200 kc min</td></tr><tr><td>Noise (p-p) from dc to 300 kc</td><td>400 μv rms max</td></tr></table>

# 2.3.7.3 Amplifier Balancing

The amplifiers should be periodically balanced to assure accuracy. Under normal circumstances, the amplifier will remain balanced for periods of weeks. However, at intervals it is desirable to check this condition, and if an amplifier is found to be unbalanced, then an adjustment should be made. The period between balance checks depends to a large extent on the application of the amplifier. For uses which might be unusually sensitive to amplifier unbalance or integrator drift, the amplifier should be balanced at more frequent intervals. In any case, maintenance personnel should recognize the fact that many amplifier and network malfunctions can be detected by checking amplifier balance. Consequently, it is recommended that a check of amplifier balance be made biweekly. If the check indicates that the amplifier balance is within tolerance, no adjustment need be made.

# 2.3.7.4 Theory of Operation

# Basic Block Diagram

The dual dc amplifier consists of an EAI model 6.715 dual dc amplifier card housed in a special package. The components for one channel are shown in Fig. 2.3.14. The major components consist of the stabilizer amplifier, the chopper, and the dc amplifier. The circuit is arranged so that the drift-free characteristics of an ac amplifier are used to maintain constant dc amplifier balance by providing a voltage to the input of the dc amplifier which tends to maintain the summing junction at virtual ground. The resulting circuit has excellent long-term stability and allows the use of a wide-bandwidth dc amplifier without the necessity of frequent manual balancing.

Inputs to the amplifier are applied through an external input impedance $Z_{in}$ . The dc and low-frequency components of the signal voltage at the summing junction (SJ) cannot pass directly to the input of the dc amplifier section because of Cl. Instead, they are connected through R3 to contact 9 of chopper D1. A chopper, or synchronous vibrator, con-

sists of a coil-driven vibrating reed 8 (Fig. 2.3.14) that alternates between contacts 9 and 7 on each half cycle of the coil excitation voltage. The chopper alternately grounds contact 9, producing a 60-cps square-wave input to the stabilizer amplifier. After amplification, the resulting signal is demodulated (or synchronously rectified) at the second contact 7 of the chopper. The resulting signal at contact 7 is a pulsating dc signal whose polarity is the same as the polarity of the signal at the summing junction. The dc signal is filtered by R8 and C2 and applied through R7 to the input of the dc amplifier section. Thus dc and very low-frequency signals are amplified by the stabilizer amplifier and by the dc amplifier.

The circuit from contact 9 of D1 to contact 7 is a modulated carrier-type amplifier that provides high-gain dc amplification with no drift. The stabilizer is phase-sensitive; if the polarity of the summing junction signal changes, the phase of the modulated signal changes and the polarity of the pulsating dc output voltage changes.

High-frequency components of the input signal are passed through C1 to the dc amplifier and are amplified by the gain of the dc amplifier only. The open-loop gain of the amplifier thus depends on the frequency of the input signal. At very low frequencies the gain is extremely high because the stabilizer amplifier is placed in series with the dc amplifier. At higher frequencies the gain is decreased but remains high enough to satisfy all expected operations when the feedback loop is closed.

Any component of the amplifier output voltage due to drift in the dc amplifier section is fed back through the feedback impedance $Z_{f}$ to the summing junction of the amplifier. Since any drift-produced voltage has a very low frequency, it will be amplified by the stabilizer section, filtered, and then applied as a drift-correction signal to the input of the dc amplifier section. The drift-produced component in the output is reduced by a factor equal to the effective gain of the stabilizer section. The amplifier would require balancing every few minutes without stabilization. The drift compensation produced by chopper stabilization allows the amplifier to be used for weeks without attention.

The amplifier in the stabilizer section has a very high gain. Since it is connected to the summing junction, it serves as a monitor of the summing junction voltage. Under normal circumstances the input current of the operational amplifier is equal to the feedback current, and the summing junction is at virtual ground. If the currents are not equal, the amplifier is not performing properly, and the summing junction departs from virtual ground. This rise in voltage is amplified by the stabilizer and results in an output signal which may be connected through the appropriate push-button switch to the balance monitoring meter circuit.

# DC Amplifier Section

Refer to Fig. 2.3.15 for the following description. The summing junction of the operational amplifier is connected to the input terminal. The ac components of the input signal are applied to the base of transistor Q1 through R2 and C1. The input signal is also connected through R3 to the input of the stabilizer section. Two reverse-connected

diodes CR1 and CR2 are connected from the input to ground so that C1 cannot be charged to a high voltage should an overload occur. This feature allows the amplifier to recover rapidly following an overload condition. The voltage at this point is normally less than the diode conduction point.

Transistors Q1 and Q2 comprise the amplifier input stage. Transistor Q2 is connected in a common-emitter configuration, with R7 (in etched-circuit resistor network NW1) and thermistor Rl5 providing self-bias. Transistor Q1 is used in the emitter-follower configuration and uses the voltage drop (approximately 0.3 v) across the base-emitter diode of Q2 as its operating voltage. The emitter-base resistance of Q2 provides a load for Q1. This configuration gives the amplifier a relatively high input impedance. The base circuit of Q1 is completed through R8 (in NW1), R1, and the balance potentiometer. These components form a voltage divider between -15, +15, and +25 v. The balance potentiometer sets the optimum operating point for Q1, as indicated by a zero output from the stabilizer section.

The high-frequency rolloff of the input stage is controlled by C3 and R5.

Temperature compensation is provided by thermistor R15 and resistor R6, which tend to keep the collector of Q2 at a constant potential regardless of temperature variations. The stabilizer output is connected through R8 and R7 to the input of Q1.

The output of Q2 is coupled to the base of Q3 through NW1-R5. Bias for Q3 is provided by NW1-R4 and NW1-R5. The feedback network consisting of R10 and C5 provides the proper high-frequency rolloff for the Q3 stage.

Capacitor C4 provides correct phasing for higher frequencies. The collector load for Q3 consists of resistors NW1-R3 and NW1-R1.

Resistor NW1-R3 provides direct coupling from the output of Q3 to the base of Q4, as well as forming a voltage divider with NW1-R1 to set the operating point for Q4. The Q4 stage is connected in the common-emitter configuration. The emitter is connected to +15 rather than ground, to establish the correct operating points for Q4, Q5, Q6, and Q7. The collector load for the stage consists of NW1-R2. Capacitor C7 provides high-frequency degenerative feedback for this stage, and the network consisting of C6 and R11 controls the high-frequency rolloff for Q4 and Q5.

The collector of Q4 is connected to the base of Q5 through an incandescent lamp DS1. The filament of this lamp has a high positive temperature coefficient of resistance, providing an increase in resistance with an increase in current flow. This stabilizes the operation of Q5 by limiting base drive. The Q5 stage is connected as an emitter follower, with resistor Rl2 providing the emitter load resistor. Diode CR3 provides a small forward bias for output transistor Q7, eliminating crossover distortion in the output stage.

The output stage consists of transistors Q6 and Q7, connected in a complementary-symmetry configuration. This circuit arrangement provides the advantages of push-pull operation with a single-ended input. Both transistors are connected as emitter-followers. Since transistor Q6 (PNP) conducts with a negative input and transistor Q7 (NPN) conducts with a positive input, one of the transistors delivers current to the

load regardless of input polarity. With a zero input, both transistors conduct equally, and the voltage drop across the load is zero. Incandescent lamps DS2 and DS3 perform a function similar to that of DSL; by providing an increase in resistance with an increase in current, they protect the output transistors from excessive current flow. Resistor RL3 provides a dc feedback to the base of Q4 which tends to keep the output of the amplifier at zero volts with a zero input and compensates for minor transistor and temperature variations.

# Stabilizer Section

The stabilizer section consists of a four-stage direct-coupled amplifier (Q8, Q9, Q10, and Q11), input and output coupling capacitors (C8 and C12 respectively), and a 60-cps chopper (D1). The stabilizer preamplifies the dc and very low-frequency components of the signal appearing at the amplifier summing junction and applies the resulting signal as an input to the dc amplifier section.

Stabilizer Amplifier. - The stabilizer amplifier receives its input from the summing junction through resistors R3 and R9. The chopper grounds the junction of R3 and R9 60 times each second, making the input appear as a series of pulses between ground and the input level. These pulses are coupled through C8 to the base of transistor Q8.

The input stage of the stabilizer consists of transistors Q8 and Q9. Transistor Q8 is connected as an emitter-follower and uses the base-emitter voltage drop of Q9 to provide operating voltage. The circuit arrangement of Q8 and Q9 is similar to the arrangement of Q1 and Q2 in the dc amplifier section and provides a relatively high input impedance. Resistors NW2-R1 and NW2-R11 provide bias for Q8. Capacitor C9 filters high-frequency transients from the input waveform. Resistor NW2-R2 provides the emitter load for Q8 and, together with NW2-R12, provides bias for Q9. Transistors Q9, Q10, and Q11 are connected in the common-emitter configuration and are directly coupled through resistors NW2-R4 and NW2-R6. Capacitor C10 provides high-frequency degeneration for the Q11 stage, removing unwanted high-frequency components from the output waveform. Resistor NW2-R8 provides a feedback to the junction of NW2-R1 and NW2-R11, adjusting the bias on Q8 to maintain the stabilizer amplifier transistors at the correct operating point. The network consisting of R14 and C11 provides phase correction for very low frequencies and filters high frequencies from the NW2-R8 feedback loop.

The stabilizer amplifier consists of an emitter-follower input stage which is noninverting and three common-emitter stages which provide an overall phase shift of $540^{\circ}$ . This constitutes an apparent $180^{\circ}$ phase shift, or an inversion from input to output. This cannot be tolerated by the overall amplifier, since the dc amplifier section provides a $180^{\circ}$ phase shift. Any feedback under these conditions would be regenerative, and the amplifier would not be usable. For this reason contacts 7 and 8 of the chopper demodulate the output of the stabilizer amplifier to provide a pulsed output to the filter network (R8 and C2) having the same polarity as the input. This is accomplished as described below.

Chopper. - The chopper used in the EAI model 6.720 amplifier is a specially designed high-speed relay. It consists of a double-pole

armature assembly which is driven by a 60-cps ac source and which alternates in position from one set of contacts to the other at this rate. Figure 2.3.14 shows how one pole of the chopper (pin 8) alternately grounds the stabilizer input (pin 9) and the stabilizer output (pin 7). The closing of contacts 8 and 9 at a 60-cycle rate causes the stabilizer input to appear as a series of pulses. This permits amplification of very low frequencies or dc levels while isolating the amplifier operating levels through the use of a coupling capacitor. The closing of contacts 8 and 7 effectively shifts the phase of the output by providing a short r-c charge or discharge time for C12 when closed and a longer time (through R8) when open. This operation is more easily understood with the use of examples.

If the input to the summing junction tends to go positive, the input to the stabilizer amplifier consists of a series of positive pulses. The output waveform at the collector of Q11 then consists of a series of negative-going pulses. However, during the time that the input pulse is present (positive), the output (negative) at the junction of C12 and R8 is connected to ground through contacts 7 and 8 of the chopper. This allows C12 to charge rapidly to the level at the collector of Q11. The chopper arm then closes to contact 9, driving the stabilizer input to ground.

The collector of Qll goes from its negative level toward ground at this time, and the positive change is coupled through C12 and R8 to the input of the dc amplifier. The dc restoring action of contact 7 and the arm of the chopper thus makes the apparent output a series of positive pulses which are filtered by C2 and R8 and provide a dc input to the dc amplifier through R7.

If the input to the summing junction tends to go negative, the stabilizer input is a series of negative pulses. The output at the collector of Q11 is a series of pulses from a negative level toward ground. In this case, the chopper provides a short-time-constant discharge path for C12 when the collector of Q11 is close to ground. As contacts 8 and 9 of the chopper break and contacts 8 and 7 close, the collector of Q11 goes negative and the change is coupled through C12 and R8 to filter capacitor C2.

Stabilizer Filter. - The stabilizer output filter, consisting of capacitor C2 and resistor R8, has a time constant of 3 sec. This is extremely long with respect to the stabilizer output waveform, consequently reducing the ripple at the junction of R8 and R7 to a negligible level.

Stabilizer Functions. - The stabilizer performs the apparently dual functions of preamplifying dc and very low-frequency input signals and maintaining the amplifier summing junction at a point very close to ground potential over wide variations in amplifier balance. When the amplifier feedback loop is closed (as it must be) and no input is applied, the amplifier output should be zero volts. Any departure of the amplifier output from this point is coupled through the feedback resistor to the summing junction. This causes the stabilizer to generate a correction voltage which returns the amplifier output and, consequently, the summing junction to zero. If an input signal is applied to the summing junction, the stabilizer again generates a voltage. In this case, however, the output of the dc amplifier is shifted from ground

potential to produce an output with a polarity opposite to that of the input and a magnitude equal to the input voltage multiplied by the ratio of the feedback resistance to the input resistance. This output produces a potential at the summing junction equal in magnitude and opposite in polarity to the input signal, returning the absolute potential at the summing junction to a point very close to ground. It is in this way that the stabilizer attempts to keep the summing junction at ground regardless of input voltage changes or variations within the dc amplifier.

# 2.3.8 Fission Chamber Drive

# 2.3.8.1 Description

The fission chamber drive, ORNL model Q-2545, is shown in Figs. 2.3.16 and 2.3.17. This unit contains a direct-current motor and associated drive train for positioning the preamplifier and fission chamber assembly. In addition, there is a position-sensing train for providing position signals to the servo power amplifier and to the data logger.

Performance specifications are:

Stroke 90 in.

Chamber velocity 72 in./min

Environment 150°F in water containing 2000 ppm sodium nitrite corrosion inhibitor

A ball-bearing lead screw turning at 288 rpm provides the rotational-to-linear motion conversion with an efficiency rating of approximately $90\%$ . A water-resistant calcium-complex-base grease was selected as the lubricant for the lead screw. The ball-bearing nut is attached to a guide block which rides on nylon runners between two aluminum guide rails mounted within a 3-3/4-in.-OD stainless steel drive tube.

A thrust tube connected to the guide block is attached to a cabling rig which is connected to the preamplifier and fission chamber assembly. The fission chamber signal cable, sheathed in Tygon tubing for water protection, and a piece of music wire are coiled into a helix. These are held together with nylon spiral wrapping to form a spring-loaded coiled cord. This helix provides the necessary cable makeup and is coiled loosely around the thrust tube between the cabling rig and the lower end of the drive tube. This cabling rig rides on nylon rollers inside the 4-in.-ID instrument penetration tube. (This tube is not a part of the positioner assembly.)

The direct-current drive motor with integral gear reducer and tachometer is protected from any torque overloads by a disk-type slip clutch. The position signal system is directly connected to the lead-screw shaft ahead of the slip clutch by a pair of precision gears.

The position signal system consists of a ten-turn auxiliary position-sensing potentiometer driven by a 48:1 ratio reducer, to provide 7-1/2 revolutions for 90 in. of chamber travel. This, in turn, drives

a 10:1 ratio reducer which is connected to a one-turn position-sensing, data-logger input potentiometer. On the same shaft there is a synchro transmitter for driving a position indicator on the console.

A ten-turn Vernistat interpolating potentiometer, previously described, is gear-driven from the shaft of the ten-turn auxiliary position-sensing potentiometer to provide ten revolutions for 90 in. of chamber travel. This interpolating potentiometer provides the position feedback signal to the function generator amplifier (ORNL model Q-2616).

Upper and lower limit switches are actuated by rods which are tripped by the guide block at each end of its travel. These rods are held captive in grooves between the guide rails and the drive tube. This permits mounting of the limit switches in the motor drive assembly where they are readily accessible.

# 2.3.8.2 Drive Motor

The permanent magnet dc drive motor is a Globe Industries, Inc., type BL-7, 27 v, with a 30.7:1 ratio gear reduction and a 1-7/8-in.-square flange mounting. It has an integral permanent magnet dc generator, type LL-1, which produces a minimum of 1.8 v per 1000 rpm at no load. The motor has a 350-to-450-rpm no-load speed range, rated at 137 in.-oz torque, part No. 102A276, purchase order No. 62X-20042 special; the output shaft is 5/16 in. in diameter by 3/4 in. long with a 1/8-in.-square key seat.

# 2.3.8.3 Lead Screw

The actuator assembly is a commercial-quality ball-screw type, No. 1000-0250-C1, by Saginaw Steering Gear. The screw is 8 ft 6 in. long. The screw threads have a 1-in. pitch diameter, a 0.250-in. lead, and a 0.820-in. root diameter, and are right-hand threads. The nut has a 1-1/2-in.-square body with a 1.583-18NS thread. The screw and nut are heat-treated 17-4 PH stainless steel. The balls are heat-treated type 440C stainless steel, with every other ball 0.002 in. undersize.

# 2.3.8.4 Position-Sensing Potentiometer

The position-sensing potentiometer, which provides the input to the data logger, is by Beckman Instruments, Inc., Helipot No. 5203R5KL.25RS. It is a single turn with servo mount, ball bearings, and double-ended shaft extensions. The characteristics are: 5000 ohms, ±0.25% linearity tolerance, and 3 w.

# 2.3.8.5 Synchro

The synchro is a Norden No. 121F1A torque transmitter, 115 v, single phase, 60 cps ac. Its characteristics are: three-phase stator, 0.38 in.-oz torque gradient, 0.50 in.-oz frictional torque, and ±8 min electrical error. The shaft is 0.2405 in. in diameter with ASA spline and threads.

2.3.8.6 Auxiliary Position-Sensing Potentiometer

The auxiliary position-sensing potentiometer is by Beckman Instruments, Inc., Helipot No. 7603R1KL.l5RS. It is a ten-turn potentiometer with servo mount, ball bearings, and double-ended shaft extensions. The characteristics are: 1000 ohms, ±0.15% linearity tolerance, and 5 w.

2.3.8.7 Vernistat Interpolating Potentiometer

The Vernistat interpolating potentiometer is a Perkin-Elmer Corporation Vernistat No. 2X5. Its characteristics are: interpolating, $3960^{\circ}$ , electrical rotation (continuous), 34 chords, 470 ohms maximum output impedance, $0.004\%$ approximate angular resolution, and size 18 servo mounting, part No. 124-0118.

2.3.8.8 Gear Reducers

The two gear reducers are by Metron Instrument Co. One, Metron No. 9B48R, has a 48:1 ratio with a 15-min maximum backlash, servo mount, and 3/16-in.-diam shafts. The other, Metron No. 9A10R, has a 10:1 ratio with a 15-min maximum backlash, servo mount, and 3/16-in.-diam shafts.

2.3.8.9 Slip Clutch

The Sentinel Manufacturing Corporation makes the type 40, size 2000 single-disk slip clutch. It is a coupling type with a 6 in.-1b setting, a 5.16-in. bore-through disk hub, no bore in the housing hub, and a 1/2-in.-diam housing hub.

2.3.8.10 Limit Switches

The snap-action limit switches are Micro Switch units, No. BZ-2RW82255-A2, with a short roller lever, 6 oz operating force, and a rating of 15 amp at 125 v ac.

Fig. 2.3.1. MSRE Wide-Range Fission Channel Block Diagram.   
![](images/50fae723fb900b793885a97c3239cabace599932e8eb3186aefa0b9d8815e6b9.jpg)  
ORNL-Dwg.66-3994

Fig. 2.3.2. Actual and Ideal Curves of Count Rate vs Reactor Power.   
![](images/0db37ad6ac7da994582b07be6fc18c657dba7cf5048672b871d99e8a7e966bac.jpg)  
*NOTE 1: THIS SOLID LINE CURVE IS NOT NECESSARILY REPRESENTATIVE OF AN ACTUAL OR TYPICAL CURVE BUT ILLUSTRATES THAT THE ACTUAL CURVE WILL DEPART FROM THE IDEAL STRAIGHT LINE.

![](images/179624b004424e7a0bd73613a65e13db7dc371c7fe5d279f7a9e52fdae240ae2.jpg)  
Fig. 2.3.3. MSRE Wide-Range Counting Channel.

![](images/ccd76b868c89faf497d8bc3dc0b8ed4e5b1f38582fe011f0bd7212bd6be69b71.jpg)  
Fig. 2.3.4. MSRE Wide-Range Counting Channel.

PHOTO-87826

![](images/8aafbd5fed61d7131913b55c5c79572d87c0fd3ffd555606047cad80ae475d9d.jpg)  
Fig. 2.3.5. "Snake" Assembly.

![](images/6568ef861229a13bab58db7e7c7cf2873f9d4315ef8ee9b7878536e993436eb8.jpg)  
Fig. 2.3.6. Preamplifier Circuit Diagram.

![](images/ecc13e7ab5447ac23ed41719f4e03d8f3b0884cc19569fdb13b84a9b57144b55.jpg)  
Fig. 2.3.7. Fission Pulses at the Main Amplifier Input.

![](images/59d17b2ddf21c4f800d776f76b7acc56e1874402769659b76fba135818908dae.jpg)  
C   
C   
Fig. 2.3.8. Preamplifier Component Layout.

ORNL-DWG 64-7741R

![](images/535c69e0f5e57d3fd4a1972ec4beab6e849d43b41bc330969812128e96c32c67.jpg)  
C   
Fig. 2.3.9. General Shielding and Grounding Layout of the Assembly.

![](images/d75623d1265c7256de554e7b0c427c924108273f8f01fd349fdb82b01ebb06a6.jpg)

![](images/e416b699409cbdf4bbb1d71da3e0d8b34807bb120e8d4e38895d22cee2df021d.jpg)

![](images/e88471a7b97194cc928aa9a2a19f95b24b2d6ede5b7a78a63e474f60e9e589eb.jpg)

![](images/514a13fdaff34711357715d39dc6a337005217261ce96b1e295afdd78964c9c6.jpg)  
Fig. 2.3.10. Pulse Amplifier and Count Rate Meter Circuit.

![](images/c2cba9413c83b0d4533c971098923137ea5477f1fde1cd5813c7d896bfd6b023.jpg)  
A INPUT

![](images/eb8139de523a4586f1cf30f6144afab3543a1fd558619674ef6ce57bfc3fad91.jpg)  
$\langle \widehat{\mathbb{B}}\rangle$ OUTPUT

![](images/6c875e329765f3c56c555479df650e815b0669cdb686c04b48ff450d74b95c7a.jpg)  
OUTPUT-NO OVERLOAD

![](images/88d0212222150649a4ae17fc565b294b3694349a8280e0085f633aefd336dbd1.jpg)  
$\langle \widehat{\mathbb{C}}\rangle$ OUTPUT-X2 OVERLOAD

![](images/dabd098cda9134a6a4487a1f15918c4e677ab0db0f00852723bd82af29d873e8.jpg)  
E OUTPUT-XIOOVERLOAD   
Fig. 2.3.11. Pulse Amplifier Waveforms.

![](images/357b4bd1d86587ef0c4d518e77874bca28c208d31954d338811a19b398a475db.jpg)  
Fig. 2.3.12. Composite Response of Six Diode Pumps with Individual Pump Response Where $\mathbf{Cn} \times \mathbf{Rn} = 0.1^{\mathbf{n} - \mathbf{1}}$ C1 × R1.

ORNL-DWG 67-7040

![](images/101711e78ac114541dc5f13b9899c3697f87a9c585ff964fe2fda9b4d2345704.jpg)

![](images/6984917bfe6bd9dfbf8db0780fae96c318e58a8bdcb0aab778e591ae6bcd5640.jpg)

The output wiper has just passed commutator bar 2 and is interpolating between bars 2 and 3. Resistance element tap A is just about to disengage from commutator bar 1.

![](images/5c446acc674295b6c82f8161137514815d1a0a4402534616e36ca717c7f2afdd.jpg)

![](images/36c728325107fc3c49990f226586a858c98936ee502c0f40c00923c0852c3ece.jpg)

As the output wiper moves in a clockwise direction, the output voltage changes linearly from the voltage on commutator bar 2 to that on commutator bar 3. Resistance element tap A has disengaged from commutator bar 1 and is switching to commutator bar 4.

![](images/84dfb8949ae08e4f3583ad4b143d5becf7f6c4523cb05c5cb5e50192d54d237d.jpg)

![](images/ed147164dc2c072532d2f7f98b0922a92001b7a9964825f45b318c4e92a11e3f.jpg)

The output wiper is approaching commutator bar 3. Resistance element tap A has completed switching and is in contact with commutator bar 4. Continued clockwise rotation of the output wiper will result in smooth interpolation past commutator bar 3.

Fig. 2.3.13. Electrical Relation of Vernistat Interpolator Commutator Bars, Interpolating Resistance Element, and Output Wiper.

![](images/03a012bf169e594aa1edfd8c00e425811fd007e2fc5a45131f0c23b6d3a9c64a.jpg)  
Fig. 2.3.14. Dual dc Amplifier Card Simplified Block Diagram, One Channel.

![](images/28d5f9e8428fde56b0c2a390a5ebc74b3d7bb4b55ea6b07c1006b9298b81b550.jpg)  
Fig. 2.3.15. 6.715 Amplifier Card Simplified Schematic, One Channel.

![](images/14cfb4054a0fe4de49b0742d28cb2f7db49445e7dbea67ba318994ddfb6f8b0b.jpg)  
Fig. 2.3.16. Fission Chamber Drive-Motor Drive Assembly.

ORNL-DWG 66-4251

![](images/1d164b93f95926305d4639a4229790df5bbf620b57eb04d1f403c2d8f0a39b8f.jpg)  
Fig. 2.3.17. MSRE Drive Unit for Wide-Range Counting Channel, Block Diagram.

# 2.4 LINEAR POWER CHANNELS

# 2.4.1 Description

These linear power channels (Fig. 2.4.1) comprise the instruments used for the most accurate determination of reactor power and for input to the rod control servo system. These compensated ion chambers and associated power supplies, ORNL models Q-1045 and Q-995, respectively, were removed from the HRT and reconditioned for use in the MSRE. The design of the chamber, testing and compensation procedures, and its high-current saturation characteristics have been described in two ORNL documents, $^{1,2}$ applicable portions of which are included later in this section. The MSRE chambers, unlike the illustration in ref. 1, are equipped with motor-driven remote compensation adjustment and do not use a continuous flow of nitrogen.

The Q-995 power supply is a conventional regulated supply designed to provide the requisite positive and negative voltages to the two sections of the chamber. The negative voltage adjustment is used to assist compensation in accordance with ref. 1. For the circuit diagram see Fig. 2.4.2.

The picoammeter is a Keithley Instruments, Inc., model 418-20 (Sect. 2.4.3). It has an overall range from $10^{-12}$ to $10^{-2}$ amp, accomplished by range switching. Range switching is described in Sect. 2.6; it may be done locally at the instrument or remotely at the console. Detailed specifications and performance characteristics, abstracted from the manufacturer's instruction manual, are given in Sect. 2.4.3. Figure 2.4.1 shows only one channel of linear input instrumentation. For a more complete diagram the reader is referred to Sect. 2.6.

Either of the two channels may be used to supply input to the linear recorder on the main control board and to the regulating rod controller. The output channel not being recorded is read out on a console-mounted meter. The strip-chart recorder is a two-pen, self-balancing potentiometer type arranged in a somewhat unorthodox fashion in order to record both the output voltage of the picoammeter and the range switch setting unambiguously.

This simultaneous record of picoammeter output and range setting is unambiguous because the range setting uses the left-hand $40\%$ of the chart width and the picoammeter output is restricted to the remaining $60\%$ . Therefore the chart traces do not overlap or cross over at any time, and there can be no question as to trace identification after the paper roll is removed. The above is illustrated by Fig. 2.4.3, the chart paper used for this power recorder.

# 2.4.2 Visual Readout Device, Series 360

A visual readout device, mounted above the linear power recorder and legible to personnel in both the control room and the visitors' area, displays the range setting multiplier so that the reactor power can be read at a distance by simply noting the position of the indicating flag on the right-hand pen of the linear power recorder. This readout device (Fig. 2.4.4) consists of an assembly of optical projection modules which display selected characters (numbers, letters, symbols, etc.) on a translucent screen located flush to the main board. In the MSRE the projection lamps in the modules are selected by the range selector switches on the console.

# 2.4.3 Keithley Model 418-20 Picoammeter: Specifications and Description

RANGES: $10^{-12}$ to $10^{-2}$ amp full scale in twenty-one $1 \times$ and $3 \times$ overlapping ranges. Any range may be selected at the main chassis location or from a remote location.

ACCURACY: ±2% of full scale from $10^{-2}$ to $10^{-8}$ amp; ±3% of full scale from $3 \times 10^{-5}$ to $10^{-12}$ amp.

ZERO DRIFT: With source voltages greater than 1 v and after a 30-min warmup, the drift is less than $1\%$ per 8 hr on any range.

RISE TIME, MAXIMUM (seconds, from 10 to $90\%$ of final current):

<table><tr><td>Range (amp)</td><td>No External Capacitance</td><td>With 50 pf Across Input</td><td>With 500 pf Across Input</td><td>With 5000 pf Across Input</td></tr><tr><td>10-12</td><td>0.03</td><td>0.06</td><td>0.4</td><td>4.0</td></tr><tr><td>10-11</td><td>0.005</td><td>0.01</td><td>0.035</td><td>0.4</td></tr><tr><td>10-10</td><td>0.004</td><td>0.004</td><td>0.006</td><td>0.04</td></tr><tr><td>10-9</td><td>0.004</td><td>0.004</td><td>0.004</td><td>0.006</td></tr><tr><td>10-8</td><td>0.004</td><td>0.004</td><td>0.004</td><td>0.004</td></tr><tr><td>10-7 and</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr></table>

RANGE SWITCHING TIME: 5 msec maximum.

INPUT: Grid current is less than $3 \times 10^{-14}$ amp. Change in input voltage drop is less than 1 mv for full-scale deflection on any range. Input resistance increases from 0.1 ohm at $10^{-2}$ -amp range to 1000 megohms at $10^{-12}$ -amp range in decade steps.

OUTPUT: A ±3-v output at up to 1 ma is developed for full-scale meter deflection. Impedance is less than 1 ohm. Polarity is opposite to input polarity. Noise is less than 2% rms of full scale on $10^{-12}$ amp range. Provision is made for lower voltage outputs.

ZERO CHECK: Allows zeroing without disturbing the circuit.

REMOTE CONTROL: Local or remote control selected by front-panel switch. Remote range switching requires a five-bit binary input with

binary "1" corresponding to the $10^{-2}$ -amp range in numerical order to binary "21" corresponding to the $10^{-12}$ -amp range. Zero check requires a separate input signal. All inputs require closure to ground.

CONNECTORS: Input: Teflon-insulated uhf-type receptacle.

Output: Amphenol 80 PC2F receptacle.

Remote: Cannon DA15S.

Remote control: Winchester type XAC 34-S-F-2-A-016G.

TUBE COMPLEMENT: One 5886.

POWER: 105-125 v or 210-250 v, 50-1000 cps, 22 w.

# 2.4.4 Procedure for Field Testing and Compensating Compensated Chamber Q-10453

# 2.4.4.1 Description

The compensated chamber (Fig. 2.4.5) really consists of two chambers, one of them boron-coated. The output current is the sum of the currents of the individual chambers; since the high-voltage electrodes of these individual chambers are at potentials opposite in sign (one is +600 v; the other, -300 v), the output current will be the difference of the two chamber currents. The current from the boron-lined chamber is proportional to the neutron flux and to the gamma flux, while the uncoated chamber responds to gammas only. By making the gamma responses equal, the output current is proportional to neutron flux alone, even in the presence of a high gamma flux.

It would not do to make the coated and uncoated chambers identical; they would then have to be placed in the same location in the reactor. What is done is to build them very close together and then make one adjustable to accommodate differences in gamma flux at the two chamber locations. The process of finding the best adjustment is known as compensating the chamber. It must be done in the reactor at the exact location where the chamber is to be used. The reactor itself is used as a source of gamma radiation.

# 2.4.4.2 Testing

# Insulation Tests

The purpose of these tests is to determine whether the leakage current of the chamber is negligible compared with the operating current. To do this, one applies a high direct voltage to the high-voltage electrodes and observes the leakage current with a sensitive device. Two high-voltage supplies are needed: +1000 v and +500 v. They need not be well regulated, but they must be well filtered and have a low noise and hum output. It is desirable to operate them from a sine-wave Sola constant-voltage transformer. Connect the +1000 v to the positive high-voltage receptacle on the chamber; the +500 to the negative high-voltage. Connect the output to a current-measuring device capable of

indicating a current of $10^{-12}$ amp. This may be an electrometer; often it is convenient to use the log N amplifier, calibrated as per Q-915-6. The ground (or low) side of the log N or electrometer must be connected to the ground side of the high-voltage supplies, since the receptacle shells are not connected to the chamber. This may be done with a clip lead, but in view of the high voltage involved, a wire properly secured to a screw is safer. A leakage current greater than $1 \times 10^{12}$ amp is excessive, and the chamber must be disassembled and cleaned by someone experienced in this job. Do not attempt this in the field.

# Compensation

1. The preferred method of compensation consists in varying pile power level and comparing the output of the chamber to be compensated with the pile level as read on another instrument, usually the fission chamber. The pile is run at a high level for half an hour or more (to build up gammas); the flux is then changed as quickly as possible to a lower level. The procedure is trial and error; increase the high-to-low flux ratio as the compensation gets nearer and nearer the correct value. The reference instrument will give the ratio of the two flux levels; compare this with the ratio as measured on the test chamber. If the ratio from the test chamber is too low, the chamber is undercompensated, and the compensation must be increased. If the ratio from the test chamber is too high, the chamber is overcompensated, and the compensation must be decreased.

2. The compensation may be varied by screwing in or out the compensating adjustment on the chamber and by varying the negative potential on the compensating electrode. Changing the adjustment of the chamber varies the relative volume of the uncoated chamber; this is how the compensation is usually changed. The adjusting screw is turned clockwise to decrease the compensation of an overcompensated chamber; turning it counterclockwise increases the compensation. When the adjustment is nearly correct, turning the adjusting screw $30^{\circ}$ will change the (negative) gamma current by about $1\%$ . The effect of this change on the total current will, of course, depend on how large the gamma current is with respect to the neutron current, and this will in turn depend on how large the gamma flux is compared with the neutron flux. Changes in negative potential on the high-voltage electrode of the uncoated chamber may also be used to adjust the compensation. Decreasing the voltage decreases the compensation; increasing the voltage (more negative volts) increases the compensation. The magnitude of the change in compensation depends on the gamma current and on the position of the negative high-voltage electrode, which is moved by turning the compensating adjustment. The effect of a 30-v change may be equivalent to as little as 1/20 turn change in the compensating adjustment, or to as much as 1/2 turn.

At newer installations, means are provided for turning the compensating adjustment remotely, so that it is not necessary to dismantle lead cables, shield plugs, and the like. Compensation of chambers so installed is far better carried out using the compensating adjustment exclusively, with negative high voltage set at its maximum value, since the uncoated chamber has better saturation characteristics at higher voltages. Where chambers are installed without means of remote adjustment, it will, in some cases at least, require considerable time

and effort to make each change in the compensating adjustment. One may, if access is difficult or time short, aim at slight overcompensation with full negative high voltage and then decrease the voltage as a final adjustment. It is especially necessary in this case to guard against leaving the chamber slightly overcompensated (see No. 6 below). A principal reason for avoiding this method lies in the variable effect of the voltage adjustment - it is quite possible that compensation cannot be achieved at any reasonable voltage and that the chamber adjustment will have to be turned again.

DO NOT adjust a compensated chamber to operate with the negative high voltage less than $-50\mathrm{~V}$ .

3. The choice of flux level at which to perform this experiment is not easy, in some cases. Usually the only instrument one can believe as a reference is the fission chamber, because only that device permits rejecting all signals due to gammas. One must use flux levels such that the low level gives a sufficient counting rate to permit good statistics in a reasonable time and the high level gives a counting rate less than 10,000 counts/sec, at which rate the error due to resolving time in the A-1 amplifier starts to be important.   
4. One must take care that the control rod positions are as nearly alike as possible for the two flux levels; variations may cause "shading" effects which impair the validity of the experiment.   
5. In reactors where the $\gamma$ -n contribution to the shutdown flux is negligible, the compensation may be checked, at least approximately, by leaving the log N recorder chart running during any shutdown of 6 hr or more. The flux will decrease on a period which approaches the 80-sec half-life of the longest-lived delayed neutrons. If, at some point, the flux deviates from this 80-sec-period straight line, and this is not explained by lattice or experiment changes or something similar, then one can usually assume the chamber compensation is incorrect. Upward deviation (toward a constant level instead of a constant period) indicates undercompensation; downward deviation indicates overcompensation.   
6. It is best in the period channel to err on the side of undercompensation. Overcompensating the chamber will result in a negative output current; as the current passes through zero during startup the period circuits will scream the reactor. Prolonged negative current will induce "sleeping sickness" in the 9004 diode in the log N.   
7. It is not a foregone conclusion that every compensated chamber can be exactly compensated in every reactor. In cases where the chamber cannot be compensated with the adjustment available, the dimensions of the cups will have to be changed. This is not a job for the field; the ORNL Instrument Department Counter Laboratory should be consulted.

# 2.4.5 The Use of a Colloidal Dispersion of Boron in Oil to Obtain a Uniform and Easily Applied Coating of Boron<sup>4</sup>

(This specification supersedes ORNL drawing Q-1045-11)

The process of applying a boron coating to graphite, $^{5}$ as developed at ORNL, is to quickly heat the boron-painted graphite electrode in an inert atmosphere to a temperature sufficient to drive off the oil carrier. The following specific steps are used here to obtain a known thickness of boron coating.

1. Heat to a dull red color by means of an induction furnace, the graphite electrode which is to be coated, to drive out some of the collected gases and surface contamination. A flow of nitrogen over the piece during heating and cooling prevents oxidation.   
2. Weigh graphite electrode.   
3. Apply the dispersion of boron in oil with brush to the graphite electrode. A thick coat, but not sloppy, on fine-grained graphite results in a final coating thickness of approximately $0.8 \, \text{mg/cm}^2$ .   
4. Weigh the painted graphite electrode; $20\% \times$ weight of applied dispersion $\div \mathrm{cm}^2$ of painted surface = desired coating thickness (20% by weight of the dispersion is boron). The desired coating thickness for a single-plate chamber is $0.8\mathrm{mg / cm}^2$ ( $\pm 0.4\mathrm{mg / cm}^2 \cong 90\%$ current). The desired coating thickness for a 4-plate chamber is $0.5\mathrm{mg / cm}^2$ ; the desired coating thickness for a 16-plate chamber is $0.3\mathrm{mg / cm}^2$ .   
5. Under a strong flow of nitrogen, heat the painted graphite electrode to a temperature at which no more oil is being driven off (dull red heat) and allow to cool quickly. It is important that the nitrogen flow carry away the oil vapors quickly and that the flow is continued until the coated graphite electrode has cooled to near $100^{\circ}\mathrm{C}$ . Boron oxidizes quickly at temperatures above $200^{\circ}\mathrm{C}$ .   
6. The coated electrode may be weighed again to check the thickness of coating. It is expected that some amount of the graphite will be lost by oxidation.

# 2.4.6 High Current Saturation Characteristics of the ORNL Compensated Ionization Chamber (Q-1045)7

The saturation voltage and current characteristics of the ORNL compensated ionization chamber (Q-1045) have been measured with special

regard to high voltage and current ranges. The chamber was sealed in an enclosure containing dry nitrogen at 15 to 20 psia.

The chamber was secured at a position in the grid plate of the Bulk Shielding Reactor such that the sensitive volume was approximately 15 in. from the reactor core face on the horizontal center line of the reactor. This position was chosen so that the chamber current at full power would be of the order of 1 mA with only a small gamma background error (5%) at a reactor power three decades lower.

The chamber was connected as shown in Fig. 2.4.6. The output of the regulated high-voltage power supplies was measured with a D'Arsonval microammeter (1/2% F.S. accuracy) with 1% precision resistors in series. High currents (10-5 amp and up) were measured with a D'Arsonval microammeter and lower currents with a Leeds and Northrup micromicroammeter (model 9836A).

The reactor was held at power levels between 1 kw and 1 Mw, and the chamber voltage was varied in 200-v increments. The data are shown in Fig. 2.4.7. The actual reactor power was $4\%$ lower than the indicated power at 100 kw and $10\%$ low at 1 Mw due to the decreased neutron attenuation in the shielding caused by decreased water density at higher temperatures.

It can be seen from the curves in Fig. 2.4.7 that the neutron-sensitive volume is well saturated for currents less than $100\mu \mathrm{a}$ at any voltage above $600\mathrm{v}$ . For high accuracy the chamber should therefore be operated only at currents of $100\mu \mathrm{a}$ and below with the standard power supply Q-995. The saturation voltage for $800\mu \mathrm{a}$ is approximately 2000 v. The inaccuracy at $400\mu \mathrm{a}$ at $600\mathrm{v}$ is about $20\%$ . Since the chamber can easily withstand high potentials, there is no reason why it cannot be operated at 1 ma with a suitable power supply.

Thanks are due K. M. Henry and the staff at the Bulk Shielding Facility for their help in making the measurements.

ORNL-Dwg. 66-3912

![](images/f0f3a77b4726356ce676743ce6a2d4bdcd7cf9197361efccd60adb3cba7b6ca4.jpg)  
Fig. 2.4.1. MSRE Linear Power Channel. Two installed.

C

ORNL DWG. 67-10700

![](images/a042e85fb19fd2f29e7db92dc819f2ad4f892a31cf49137e4f13e46f804b4464.jpg)  
Fig. 2.4.2. Circuit Diagram of ORNL Model Q-995 Power Supply.

C

#

ORNL-DWG 67-6595

![](images/c31b643d9c1e3005b999b5dc724196686cbc3818e6d6021807cc6cc88741743d.jpg)  
Fig. 2.4.3. Chart Paper Used for Strip-Chart Recorder.

#

#

PHOTO 88131

![](images/378348ad2a69cad121a2560404aaeec5119da86086016cf149d73acbb884d755.jpg)

The IEE Series 360 readout meets human engineering requirements for distance viewing by displaying characters up to $2^{\prime \prime}$ in height. The unit operates on a rear-projection principle. When one or more of the 12 lamps at the rear of the unit is lighted, it illuminates the corresponding film message, focuses it through a lens system, and projects it onto the viewing screen at the front of the unit.

Fig. 2.4.4. Visual Readout Device, Series 360.

ORNL-DWG67-7039

![](images/1878394a985c8f1056e67a648b9cbf322ccc62dae682cdfef6705e22749f55d9.jpg)  
Fig. 2.4.5. Compensated Ionization Chamber, Neutron Sensitive.

![](images/15b4728b48bcaf233891742fbe38eb02ad9b9909ea61a8cb0f293fb6715d1aea.jpg)  
Fig. 2.4.6. Schematic Diagram of ORNL Compensated Ionization Chamber.

![](images/0ebd41a1a70fc39a35917041a5006e5f06f2e1671a267d1ceffe8451d3fb1307.jpg)  
Fig. 2.4.7. Saturation Characteristics of ORNL Compensated Ionization Chamber (Q-1045).

# 2.5 ROD SCRAM SAFETY SYSTEM

# 2.5.1 Rod Scram Safety Channel - Input Instrumentation

The control rods are scrambled by excessively high flux, short reactor period, and excessively high reactor outlet temperature. The safety system employs three independent channels for inputs to the safety system logic and requires that any two out of three indicate unsafe conditions in terms of either flux, period, outlet temperature, or circuit integrity to produce a scram. Table 2.6.1 in Sect. 2.6 lists control rod actions and the conditions which produce them.

A typical channel of neutron flux input instrumentation is diagrammed in Fig. 2.5.1. It consists of a neutron-sensitive ion chamber, a period safety module, a flux amplifier and ion chamber high-voltage supply, a test module, and fast-trip comparators. The outputs from the period safety module and the flux amplifier are the reactor period and power level signals which become the inputs to the fast-trip comparators. Flux amplifier sensitivity is adjusted by changing the size of a feedback resistor. In the MSRE the flux level trip point has two settings, depending on whether or not fuel salt is being pumped around the loop. Current relays in the fuel salt pump motor three-phase supply are used to determine whether the pump is circulating salt or idling in helium. These relays provide the signals used to actuate switching relays which change the value of the flux amplifier feedback resistance by a factor of 1000 and thereby provide rod scram trip points of 15 kw or 15 Mw. Figure 2.5.2 diagrams the circuitry which shifts flux level trip point, and Fig. 2.5.3 is a block or signal flow diagram of this circuitry. The fast-trip comparator is a fast-acting electronic relay with sufficient power-handling capacity to operate small relays and similar logic and control devices external to the instrument. It also contains two small, fast-acting electromechanical pilot relays which have greater power-handling capacity with somewhat reduced response time. The "on-off" outputs of the pilot relays in the comparators are the primary input signals to the safety system logic and to the control system. Detailed descriptions of these instruments are given in Sects. 2.5.3 to 2.5.8.

The temperature input signal instruments are block diagrammed in Fig. 2.5.4. The measuring thermocouples (refer to Sect. 6.7) are composed of two individual thermocouple wires, Chromel and Alumel, welded adjacently but separately to the fuel salt outlet piping, thus forming a grounded junction. Each thermocouple wire is contained in an individual Inconel sheath and is insulated from this sheath by magnesium oxide. This construction, using individual, separated wires for each leg of the thermocouple, is used in preference to a dual thermocouple assembly (both wires in a single sheath), so that if a thermocouple breaks or becomes

detached from the pipe, an open circuit is created. An open-circuited thermocouple causes the emf-to-current converter to indicate a failure toward safety, that is, upscale.

Thermocouple emf (in the 25-mv region) is amplified by a Foxboro Company type 693 emf-to-current converter which provides an output current, linear with input emf, of from 10 to 50 ma into an impedance of from 600 to 150 ohms for the selected input range of the thermocouple, in this case 0 to $1500^{\circ}\mathrm{F}$ . The type 693 converter uses magnetic amplifiers to obtain voltage and power amplification, contains no moving parts, and employs solid-state diodes where required in the circuitry.

The 10- to 50-ma output from the type 693 converter is the input signal to the high-temperature trip switch. This switch, a Foxboro model 63 alarm, compares a set-point voltage with a voltage developed by the input current from the type 693 converter and actuates an alarm relay when the input signal voltage is greater<sup>3</sup> than the set-point voltage. A contact on the alarm relay, closed during normal reactor operation, provides the high-temperature input signal to one channel of the rod scram safety system, as will be pointed out subsequently.

The emf-to-current converter also supplies a signal, the voltage drop across the 400-ohm resistor, to an isolation amplifier. This amplifier provides a barrier between the safety system instruments and the remaining nonsafety instruments which make up an input channel. The isolation amplifier transmits the input signal in the forward direction to the remaining current-actuated switches but decouples the safety instruments in the reverse direction. This virtually eliminates the possibility that the effects of malfunctions or misoperation, calibrations, etc., of the nonsafety instruments will be transmitted in the reverse direction to the safety system.

The isolation amplifier is a Foxboro Company NlllLF magnetic amplifier designed specifically to amplify the output of Foxboro type 630 pressure transducers and to be compatible with the other Foxboro components in Fig. 2.5.4. The amplifier has an input of 0.2 to 4.0 ma into 10,000 ohms impedance and an output of 10 to 50 ma into 600 ohms load.

The remaining two current-actuated switches in Fig. 2.5.4, whose outputs are labeled "Alarm" and "Control Rod Reverse," are Foxboro dual type 63 alarms, both in a single case.

The meter is a Foxboro model M65PV-OHT. This is a D'Arsonval current meter designed to operate over an input from 10 to 50 ma dc.

# 2.5.2 Rod Scram Safety Channel - Output Instrumentation

The output section of a typical safety channel (channel A) is diagrammed in Fig. 2.5.5. From the left side of the figure, it can be seen that the four trip relay contacts in the input instruments are in series and are maintained closed during normal reactor operation. These contacts are located as follows:

1. high-temperature trip (T outlet greater than 1300°F) in the Foxboro model 63 alarm switch, Fig. 2.5.4;   
2. channel integrity monitor trip in the Q-2634 MSRE test module, Fig. 2.5.1;   
3. high neutron flux trip in a Q-2609 fast-trip comparator, Fig. 2.5.1;   
4. reactor period trip $(\tau \leq +1.0$ sec) in a Q-2609 fast-trip comparator.

A fifth set of normally closed contacts formed by a manual "Test" button is also included, followed by a seal contact in parallel with a "Reset" push button. During normal reactor operation relays $\mathbf{K}_{\mathbf{A}}\mathbf{l}$ to $\mathbf{K}_{\mathbf{A}}\mathbf{5}$ are energized. These relays, push buttons, and associated indicating lamps make up the ORNL model Q-2623 relay safety element, which provides the contact multiplication needed to produce the safety actions required. The contacts of relays $\mathbf{K}_{\mathbf{A}}\mathbf{l}$ to $\mathbf{K}_{\mathbf{A}}\mathbf{3}$ are interconnected with similar contacts from corresponding relays in channels B and C to produce three two-out-of-three coincidence matrices in the power circuits to the rod drive clutches. A typical matrix appears on the right-hand side of Fig. 2.5.5. Relay $\mathbf{K}_{\mathbf{A}}\mathbf{4}$ provides one of the control rod "Reverse" signals and the "Seal" contact, and relay $\mathbf{K}_{\mathbf{A}}\mathbf{5}$ is used to open the drain tank vent valves and close the radiator doors (load scram). Figure 2.5.6 shows a block diagram and the additional circuits which operate the vent valves, radiator door, etc.

Each rod drive clutch (see Sect. 2.7) receives its power through its corresponding contact matrix, and it can be seen that a loss of clutch current (rod scram) requires that relays in at least two safety channels be deenergized. This permits testing of individual channels during operation without disturbing the reactor and also allows the disabling of any one channel for maintenance. Each leg in the two-out-of-three matrix shown in Fig. 2.5.5 contains a 100-ohm resistor and a current meter in series with a pair of relay contacts. These meters function as input channel monitors, as can be seen from the following example. Assume that channel A is being tested during operation. This may be done with either the test routine built into the Q-2634 test module (see Sect. 2.5.6) in channel A or, by using the thermocouple test assembly. $^{4}$ A less complete test is initiated by pushing the "Test" button in the Q-2623 relay safety element shown in Fig. 2.5.5. In any case, relays $\mathbf{K}_{\mathbf{A}}$ to $\mathbf{K}_{\mathbf{A}}$ will be

deenergized and thereby produce open circuits in two of the three branch circuits in each of the Q-2623 coincidence matrix monitors. From Fig. 2.5.5, it can be seen that the meters labeled "A and C" and "A and B" will change to show zero current. The total clutch current will now be carried by the third leg in the matrix, and meter "B and C" will change upscale to reflect this change. The 100-ohm resistors are required to

ensure equal current division among the three legs in the matrix. Without these resistors very small differences in relay contact resistance would produce large inequalities in the currents normally carried by the three meters. This resistor is sized so that its resistance must be at least an order of magnitude larger than any anticipated value of total relay contact resistance in series with it. Also, it must not be so large that it reduces clutch current to the "Scram" point when it assumes the total current load of the clutch, as it must, when one channel is in "Scram" mode. Tests on the prototype rod drive show that a typical clutch will transmit 39 in.-lb torque at 22.6 v, whereas the scram torque produced by the weight of the rod and unbalanced drive mechanism components is approximately 12 in.-lb. Thus, it can be seen that there is ample margin to prevent undesirable scams during testing or in the event that a single channel be tripped as by removal for maintenance or malfunction.

The 32-v Zener diode across the clutch coil prevents high peak reverse voltages that would otherwise take place when the clutch coil current is interrupted.

Figure 2.5.7 is a functional diagram of all three channels and consolidates the contents of Figs. 2.5.1 to 2.5.6.

# 2.5.3 Safety Chambers

These are Reactor Control Inc. ionization chambers type R.C. 16-(2-2.88k) (Fig. 2.5.8). Specifications are as follows:

# General

Integral cable construction with redundancy on both signal and high voltage

Cable volume separate from chamber volume

No organic materials used in the chamber or cables

Construction: all welded, guard on signal

# Mechanical

Maximum diameter 2.5 in.

Chamber length 7.25 in.

Sensitive length 4.25 in.

Integral cable length 45 ft

# Material

Outer shell 99.97% pure nickel

Inner electrodes 1100 aluminum

Cable sheath and conductor Stainless steel

Insulation

Detector

Cable end seals

Cable

Electrode coating Enriched 10B

Resistance at $25^{\circ}\mathrm{C}$

Electrode to ground without cables >10<sup>14</sup> ohms

Electrode to ground with 45-ft cable >10² ohms

Maximum ratings

Applied potential 1000 v dc

Temperature 200°C

Operating characteristics

Thermal neutron sensitivity $1.6 \times 10^{-14} \mathrm{amp / nv}$

Gamma sensitivity $5 \times 10^{-12} \, \text{amp r}^{-1} \, \text{hr}$

Saturation See curve in Fig. 2.5.9

# 2.5.4 Period Safety Module, ORNL Model Q-2635

# 2.5.4.1 Description

# General

The input, or current-sensing element (logarithmic diode), of the period safety module (see Fig. 2.5.10) is connected in series with the flux amplifier input. The voltage across the logarithmic diode is differentially amplified with a very high input impedance amplifier so that the chamber current passes undisturbed into the flux amplifier module. This voltage is further amplified and differentiated to give outputs proportional to the logarithm of the current and its period

(time required for the current to increase by one $\epsilon$ factor) respectively. The input current range is from $10^{-10}$ to $10^{-4}$ amp. In the usual application the period output serves as an input to a nuclear reactor safety system; hence the name "period safety."

# Construction

The period safety module is 1.40 in. wide, 4.72 in. high, and 11.90 in. deep. It is a standard "one-unit" plug-in module of the ORNL modular reactor instrumentation series depicted on ORNL drawings Q-2600-1 to Q-2600-5.

The circuits are on a printed circuit board which is completely enclosed by a shield. The outputs are displayed on front-panel meters. Test points and access holes to trimming potentiometers are located along the top of the shield enclosure.

# Application

The period safety module is primarily intended to continuously monitor the neutron flux and period of a nuclear reactor. Since the module is not intended to measure reactor power accurately, the panel meter on the output of the logarithmic amplifier is calibrated in "log current" from $10^{-10}$ to $10^{-4}$ amp. The output of the period amplifier is displayed on a panel meter which is calibrated in seconds from $-30$ to $+1$ .

# Specifications

Overall specifications for the period safety module are as follows:

# Period

Output voltage range -0.033 to +10 v for -30- to +0.1- sec period

Output current 0.1 ma into 100-kilohm load

Scale -30 to +1 sec

Zero drift Less than 20 mv/month

Power required ±15 v dc with regulation ±0.1%

Ambient temperature range 0 to $55^{\circ}C$

# Log current

Output voltage Approximately 1.67 v/decade with zero voltage point determined by "Hi Cal" setting

Output current 1 ma into 10-kilohm load

Scale 10- to 10-4 amp

Zero drift Less than 50 mv/month

Input leakage current Less than $10^{-13}$ amp at $25^{\circ}C$

Power required ±15 v dc with regulation ±0.1%

Ambient temperature range 0 to $55^{\circ}C$

# Applicable Drawings

The following list gives the drawing numbers (ORNL Instrument Department drawing numbers) and subtitles for the period safety module:

Q-2635-1

Q-2635-2

Q-2635-3

Q-2635-4

Q-2635-5

Q-2602-6

Circuit

Details

Meta1photo Panel

Printed Circuit Board

Assembly

Parts List

The following list gives the drawing numbers and subtitles for the plug-in chassis system:

Q-2600-1

Q-2600-2

Q-2600-3

Q-2600-4

Q-2600-5

Assembly

Details

Details

Details

Details

# 2.5.4.2 Theory of Operation

# General

The ionization chamber current passes through a thermionic diode in the period safety module and then into the flux amplifier (Q-2602) or equivalent. The voltage drop across this "log" diode is approximately proportional to the logarithm of the current. The diode voltage is applied to a very low leakage differential amplifier, whose output is further amplified with a second differential amplifier to give the "log current" output. The "log current" output is differentiated with an operational amplifier to generate the "period" output.

It is required that the leakage of the input difference amplifier be small compared with the flux amplifier input leakage. This leakage current must come from the ionization chamber current, and if the leakage current is excessive, the current amplified by the flux amplifier will be in error.

# Circuit Description

The input current flowing through the thermionic diode V1 develops a voltage across the diode that is essentially logarithmic over the current range of $10^{-10}$ to $10^{-4}$ amp. This voltage is applied to a difference amplifier which uses insulated-gate field-effect transistors (FET's) as active elements (Q1). The gate leakage current of the FET's is extremely small, so that essentially all the signal current flows through the diode and then into the flux amplifier. The gates are protected against over-voltage transients by neon tubes II and I2. (Ordinary Zener diodes are not adequate to furnish this protection because of their high leakage current.) A constant-current circuit, comprised of transistor Q2 and resistors R7, R8, and R9, furnishes the bias current for the difference

amplifier and appears as a large source load impedance to improve the common-mode rejection ratio. The gain of the difference amplifier is approximately 2.5. Its output is applied to a Fairchild type ADO-3 differential amplifier whose gain is adjustable from 2.67 to 4 by the trimming potentiometer R11 ("Lo Cal"). The particular gain required is determined by the characteristics of log diode Vl, and it is adjusted to give approximately 1.67 v/decade at the output of the "log current" amplifier. Trimming potentiometer R18 ("Hi Cal") is required for proper scale adjustment of meter Ml.

The "log current" output is differentiated by an additional ADO-3 amplifier whose gain (product of C4 and R25) is such that a 1-v output corresponds to a 1-sec period.

Two significant smoothing time constants are associated with the "period" amplifier. They are determined by the product of R20 and C4 and R25 with C5, and each is approximately 100 msec.

# 2.5.4.3 Operating Instructions

# Installation

The period safety module is a module in the ORNL modular reactor instrumentation series. Like the other modules in this series, it has standard connectors and dimensions and has a pin-and-hole code on the rear plate so that the module will not be inserted in a wrong location in a drawer. The module is installed by placing it in its proper location, inserting the module firmly, and tightening the thumbscrew. The module may be plugged in with power on without damage.

# Operating Controls

Log Current Panel Meter. - The log current panel meter is calibrated to indicate current from $10^{-10}$ to $10^{-4}$ amp. This represents a voltage swing of $-10\mathrm{~V}$ ; however, the output voltage measured with respect to ground at a particular current will vary from unit to unit. This is determined by the "Hi Cal" setting, which adjusts for variations of input diode characteristics.

Period Panel Meter. - The period panel meter is calibrated to indicate reactor period from -30 to +1 sec. This is a voltage range from -0.033 to +1.0 v. The meter is mechanically zeroed to give an "∞" indication with no voltage applied.

Zero Adjustment. - "Bal 1" is for zeroing the output of the insulated-gate difference amplifier Q1 with TP1 and TP2 shorted together. "Bal 2" is for zeroing the output of the "log current" amplifier with TP3 and TP4 shorted to ground. "Bal 3" is for zeroing the output of the "period" amplifier any time when the input is not changing.

Test Points. - The test points are located at the top of the front side of the shielding enclosure. These are used primarily when zeroing or balancing the instrument, as described above.

# Connections

All connections are made through the rear connector P29 when the module is inserted.

# Operating Procedures

The balance of the insulated-gate difference amplifier, log current amplifier, and the period amplifier should be checked periodically for drift. If correction is required, the following procedure should be followed:

1. Place a jumper between TP1 and TP2 and measure the voltage between TP3 and TP4 with a Triplett meter (or equal). Adjust "Bal 1" until the voltage is zero.   
2. Place the jumper across TP3 and TP4 and TP6 (ground). Adjust "Bal 2" until the voltage between TP5 and TP6 is zero.   
3. The period amplifier may be zeroed at any time the input is not changing by adjusting "Bal 3" until the front-panel meter indicates "∞" or until the output is zero.

# 2.5.5 Flux Amplifier and Ion Chamber High-Voltage Supply, ORNL Model Q-26027

# 2.5.5.1 Description

# General

The flux amplifier (Fig. 2.5.11) is a low-level dc amplifier that amplifies current in the range of $10^{-10}$ to $10^{-4}$ amp from an ionization chamber. The current from the ionization chamber is proportional to reactor neutron flux in the usual application; hence the name "flux amplifier."

An ion chamber high-voltage supply, a dc-to-dc converter, is contained in the same module with the flux amplifier to provide $+250\mathrm{~V}$ to polarize the ion chamber. The two sections are electrically independent.

# Construction

The ion chamber high-voltage supply and the flux amplifier are in a single module 2.83 in. wide, 4.72 in. high, and 11.90 in. deep - a standard "two-unit" plug-in module of the modular reactor instrumentation series depicted on ORNL drawings Q-2600-1 to Q-2600-5.

The circuits are on two printed circuit boards mounted side by side. The output is displayed on a front-panel meter. A balance meter, mounted in the top front of the module, is visible when the module is plugged in and the drawer is withdrawn. Near the meter is a "zero" push button and a trimming potentiometer for balancing the flux amplifier.

# Application

The ion chamber high-voltage supply and flux amplifier are intended primarily to continuously monitor neutron flux in a nuclear reactor. To

this end the panel meter is calibrated in percent power from 0 to $200\%$ . However, the amplifier may be used, with or without the ion chamber high-voltage supply, wherever it is desired to measure current in the range $10^{-8}$ to $10^{-4}$ amp full scale.

The amplifier has two internal feedback resistors and provisions for connecting an external feedback resistor to establish any desired scale calibration vs current within the capability of the instrument.

A flux reset mechanism Q-2603, a companion unit, can be used with the flux amplifier to continuously adjust the feedback factor or gain over a 3 to 1 range. The flux reset mechanism is a small instrument servo that adjusts the feedback ratio of the flux amplifier so as to force the flux amplifier output to agree with another signal, typically computed heat power.

# Specifications

Overall specifications for the flux amplifier and ion chamber high-voltage supply are given below.

# Flux Amplifier

Output voltage range

0 to $+12$ v linear for positive current (flowing into amplifier); 0 to $-12$ v for negative current

Output current

30 ma into 300-ohm load

Scale

0 to 200% power

Zero drift

Less than 1 mv/day at constant temperature; less than $\pm 10$ mv for 0 to $55^{\circ}C$

Input leakage current

Less than $10^{-10}$ amp at $25^{\circ}C$

Response time

10 to $90\%$ rise time in less than 100 $\mu$ sec with a 200-kilohm feedback resistor and 0.002- $\mu$ f capacitor on input

Power required

+25 ± 0.25 v dc with regulation ±0.1%; -25 ± 0.25 v dc with regulation ±0.1%

Ambient temperature range

0 to $55^{\circ}C$

Ion Chamber High-Voltage Supply

Output voltage

+250 ± 25 v dc

Input power required

+32 ± 4 v dc and 200 ma maximum

Output current

Rated 5 ma continuous; will deliver $\sim 50$ ma into a 3- kilohm load or 1 ma minimum into a short circuit

<table><tr><td>Overload protection</td><td>Undamaged by any overload, including a short circuit</td></tr><tr><td>Load regulation</td><td>Less than 15%, 0 to 5 ma</td></tr><tr><td>Line regulation</td><td>Less than 10%, 28 to 36 v dc</td></tr><tr><td>Output ripple and frequency</td><td>Less than 50 mv at 5 ma load; ~8 kc</td></tr><tr><td>Adjustments</td><td>None</td></tr><tr><td>Starting</td><td>Self-starting, no load to full load</td></tr><tr><td>Ambient temperature range</td><td>0 to 55°C</td></tr></table>

# Applicable Drawings

The following list gives the drawing numbers (ORNL Instrument Department drawing numbers) and subtitles for the ion chamber high-voltage supply and the flux amplifier:

<table><tr><td>Q-2602-1</td><td>Circuit</td></tr><tr><td>Q-2602-2</td><td>Details</td></tr><tr><td>Q-2602-3</td><td>Metalphoto Panel</td></tr><tr><td>Q-2602-4</td><td>Printed Circuit Board</td></tr><tr><td>Q-2602-5</td><td>Assembly</td></tr><tr><td>Q-2602-6</td><td>Parts List</td></tr><tr><td>SF-239</td><td>Fabrication Specification</td></tr></table>

The following list gives the drawing numbers and subtitles for the plug-in chassis system:

<table><tr><td>Q-2600-1</td><td>Assembly</td></tr><tr><td>Q-2600-2</td><td>Details</td></tr><tr><td>Q-2600-3</td><td>Details</td></tr><tr><td>Q-2600-4</td><td>Details</td></tr><tr><td>Q-2600-5</td><td>Details</td></tr></table>

# 2.5.5.2 Theory of Operation

# General

The ion chamber high-voltage supply and flux amplifier consist of a stable, direct-coupled low-leakage amplifier and a self-contained high-voltage supply for ionization chamber polarization. The chamber voltage supply consists of a series preregulator, to regulate the battery input voltage, and an unregulated dc-to-dc converter.

# Circuit Description of the Ion Chamber High-Voltage Supply

The power supply is designed to operate from a nominal 32-v station battery with a terminal voltage variation from 28 to 36 v dc. This wide variation makes necessary a voltage preregulator consisting of transistors Q9, Q10, Q11, and Q12.

The preregulator output voltage is sensed by resistors R24 and R26 and applied to the base of amplifier stage Qll. A reference voltage (16.8 v) generated by Zener diode string D4, D5, and D6 is applied to the emitter of Qll. The amplified difference appears at the collector of Qll and is applied to driver Ql0 and pass transistor Ql2. A constant collector current is provided for Qll by transistor Q9, Zener diode D3, and the associated network. The preregulator output (test point TP1) is filtered by C3, C4, and R27 and is applied to the dc-to-dc converter.

Q13, Q14, T1, and the associated circuitry comprise a free-running square-wave oscillator; D7, D8, and D9 assure that the circuit will be both self-protecting and self-starting. Capacitors C6 and C7 round the edges of the square wave somewhat to avoid the generation of sharp, high-frequency spikes which may be coupled to other circuits.

A square wave of approximately 250 v peak-to-peak amplitude and frequency of approximately 8 kc appears on winding l-3 of transformer T1. This voltage is rectified by diode bridge D10-D13 and is filtered by a pi-section RC filter composed of C8, C9, and R32. The output is approximately 250 v dc with less than 50 mv of 8- or 16-kc ripple.

The output voltage vs load current is shown in Fig. 2.5.12. When the output is short-circuited, the circuit continues to oscillate at a very low amplitude and supplies about $1\mathrm{mA}$ of current. The circuit will recover undamaged upon removal of the short circuit or overload.

# Circuit Description of the Flux Amplifier

The flux amplifier converts a low-level current from an ionization chamber to a usable voltage. The current range is determined by feedback resistor R33, which may be paralleled by R10 or an external resistor. The input current is converted to a full-scale voltage of 10 v at the output of the amplifier.

The amplifier is an operational type with a high open-loop gain and a high open-loop impedance (Fig. 2.5.13). Only a small leakage current flows in the input of the amplifier; therefore, all the signal current flows through feedback resistor $R_{f}$ . The voltage produced at the output is

$$
\mathbf {E} _ {0} (\mathbf {v}) = \mathbf {I} _ {\mathbf {S}} \mathbf {R} _ {\mathbf {f}},
$$

where $\mathbf{I}_{\mathbf{s}}$ is the signal current in amperes and $\mathbf{R_f}$ is the resistance in ohms.

The sensitivity of the flux amplifier can be adjusted by flux reset mechanism Q-2603. Instead of feedback resistor $R_{f}$ being connected directly to the output as shown in Fig. 2.5.13, it is connected through a voltage-dividing network to the output as shown in Fig. 2.5.14. Potentiometer R6 is motor driven to adjust the output voltage (with constant input current) until the flux amplifier output agrees with an independent signal as might be derived from a heat-power computer. The output voltage is then

$$
E _ {0} = I _ {\text {i n}} R _ {f} \left(\frac {R 6 + R 7}{\alpha R 6 + R 7}\right),
$$

where $\alpha$ is the potentiometer setting as indicated in Fig. 2.5.14.

The flux amplifier is composed of eight silicon transistors and a silicon diode. Input device Q1 is a field-effect transistor which has low gate-leakage current. In the specified range of input current, the field-effect transistor is a satisfactory electrical replacement for an electrometer tube and is far more rugged.

Some unusual characteristics of the field-effect transistor are used advantageously in this particular amplifier. The field-effect transistor drain-voltage drift with temperature is a function of the drain current. When the drain current is larger than approximately 30 μa, the temperature coefficient is positive. When the drain current is less than approximately 30 μa, the temperature coefficient is negative. The field-effect transistor is biased at approximately 45 μa so that its net current drift will be in a positive direction to cancel out drifts of opposite direction due to the remaining transistors and diodes. The voltage gain from gate to drain of the field-effect stage is about 20.

The remaining transistors are operated in standard configurations. Transistor Q2, an emitter follower with near unity voltage gain, impedance matches field-effect transistor Q1 to the following gain stage. Q3 and Q4 comprise a differential high-voltage-gain stage. The gain from the base of Q3 to the collector of Q4 is about 500.

Transistors Q5, Q6, Q7, and Q8 are complementary emitter-follower power-gain stages with unity voltage gain. The function of these four transistors is to allow the output to swing plus and minus 10 v and deliver up to about 30 ma of current to the load.

# 2.5.5.3 Operating Instructions

# Installation

The chamber high-voltage supply and flux amplifier is a module in the ORNL modular reactor instrumentation series. Like the other modules in this series, it has standard connectors and dimensions and has a pin-and-hole code on the rear plate so that the module will not be inserted in a wrong location in a drawer. The module is installed by placing it in its proper location, inserting the module firmly, and tightening the thumbscrew. The module may be plugged in with power on without damage.

# Operating Controls

Panel Meter. - The panel meter is calibrated to indicate power from 0 to $200\%$ ; this corresponds to a voltage output of 0 to $-10\mathrm{v}$ . If the amplifier is to be used with a negative input current, the meter leads should be reversed.

Balance Meter. - A zero-center balance meter on the top of the module is visible with the module inserted and the drawer pulled out. The meter is used with the push button and zero adjustment located at the edge of the printed circuit board nearby to correct for drift periodically.

Zero Adjustment. - The zero adjustment is used to balance the dc amplifier to correct for drift.

Zero Push Button. - This push-button switch short-circuits the input of the amplifier so that it may be balanced even when signal current is present.

# Connections

All connections are made through the rear connector P9 when the module is inserted. A jumper between pins 2 and 3 of P9 is provided so that if the module is removed from a drawer a warning signal is given.

# Operating Procedures

The balance of the flux amplifier should be checked periodically by depressing zero push button S1 and observing balance meter M2. If the meter reads anywhere on scale less than plus or minus full scale when the push button is depressed, the balance is satisfactory. With the push button released the meter should read upscale the same amount as the front-panel meter reading. If adjustment is necessary, turn zero-adjustment potentiometer R3 clockwise to move the indicator in a positive direction or counterclockwise to move the indicator in a negative direction.

There are no adjustments on the chamber high-voltage supply.

# Precautions

Since the output of the high-voltage supply can be lethal, care should be taken not to place fingers in the rear portion of this module.

External connections to the ionization chamber should be made with the power off or the module unplugged to avoid possible damage to field-effect transistor Q1.

# 2.5.5.4 Maintenance Instructions

# General

This module is designed to operate continuously with a minimum of maintenance and adjustment. Zero adjustment and voltage test points are accessible from the top of the drawer with the module inserted and the circuits energized.

# Periodic Maintenance

The amplifier balance should be checked (see Operating Procedures, above) once every three or four weeks.

The high-voltage output should be checked every three or four months by measuring with a voltmeter at the test points. The white point on the module is ground test point TP3; the red point is the high-voltage output test point TP2; and the gray point is the preregulator output test point TPl. The voltages at the test points should read (with respect to TP3); TP1, +25 ± 1 v; and TP2, +250 ± 25 v.

# Calibration Procedures

There are no calibration procedures.

# 2.5.6 MSRE Test Module, ORNL Model Q-2634

# 2.5.6.1 Description

# General

The MSRE test module (Fig. 2.5.15) is a special-purpose unit designed to supply calibration signals for testing the response of parts of the safety system of the MSRE. The module provides two calibrated current ramps at different rates to check the response and approximate calibration of the flux amplifier and associated fast-trip comparators. An adjustable steady-state current can be substituted for the ramps for more precise calibration. In addition, the module provides two steady-state currents for calibration of the "log current" portion of the period safety module and two voltage ramps for calibration of the "period" portion of the period safety module and associated fast-trip comparator. An ion chamber undervoltage monitoring circuit is provided in this module. All these are initiated by push buttons from the module front panel.

# Construction

The module is 2.83 in. wide, 4.72 in. high, and 11.90 in. deep. It is a standard "two-unit" plug-in module of the ORNL modular reactor instrumentation series depicted on drawings Q-2600-1 to Q-2600-5.

The circuitry is constructed on two large printed circuit boards mounted within the module.

# Application

The module is intended to supply signals for both preoperational and on-line testing of the nuclear safety system of the MSRE. Although the signal types and circuitry used are generally applicable to any reactor safety system employing the ORNL modular reactor instrumentation series, the signal levels and rates for this module are tailored especially for the MSRE.

# Specifications

Output Ramps. - The basic ramp generator supplies a voltage ramp of 0 to +14 with a rate of +1 v/sec. This ramp voltage is applied to suitable multiplier resistors to obtain the required current ramp. The output currents are: high rate (300 kilohms), 0 to 46.7 × 10⁻⁶ amp; and low rate (300 megohms), 0 to 46.7 × 10⁻⁹ amp.

Output Currents, Steady State. - The output currents are adjustable with a ten-turn precision potentiometer on the front panel calibrated to be direct reading from 0 to 100. The output currents are: high current (200 kilohms), 0 to $100 \times 10^{-6}$ amp; and low current (200 megohms), 0 to $100 \times 10^{-9}$ amp.

Log Current, Steady State. - Two calibration currents are derived from the ion chamber high-voltage supply by suitable multiplier resistors

for current calibration of the period safety module. They are: high (25 megohms), $10^{-5}$ amp; and low (250,000 megohms), $10^{-9}$ amp.

Period Calibration. - The +l-v/sec ramp is applied to the log current amplifier in the period safety module through a suitable input resistor. This produces a constant output at the period amplifier for calibration purposes. Two approximate calibration points are provided: +1 sec period (500 kilohms) and +2 sec period (1 megohm).

Undervoltage Monitor. - The circuit continuously monitors the polarizing voltage of the ionization chamber on a return lead from the chamber. When the chamber voltage is greater than $200 \pm 10\mathrm{~V}$ , a green light labeled "Normal" on the front panel is lit. When the chamber voltage for any reason drops below $200 \pm 10\mathrm{~V}$ , the circuit changes state and lights both a red "Low" indicator lamp and a yellow "Latch" indicator lamp. When the voltage is restored, the "Low" indicator is extinguished, and the "Normal" light again comes on. The "Latch" light remains on until the front-panel "Reset" push button is depressed. The relay that actuates the indicator lamps has additional contacts (single pole, double throw) for use in external circuits. An additional front-panel push button labeled "Test" simulates a low-voltage condition to the monitor circuit without affecting actual chamber voltage.

Power Requirements. - The module requires $+32 \pm 4$ v unregulated and $+25$ v ± 0.1% regulated.

Ambient Temperature Range. - The ambient temperature range is 10 to $55^{\circ} \mathrm{C}$ .

# Applicable Drawings

The following list gives the drawing numbers (ORNL Instrument Department drawing numbers) and subtitles for the MSRE test module:

Q-2634-1

Q-2634-2

Q-2634-3

$Q = {2634} - 4$

Q-2634-5

Q-2634-6

Circuit

Details

Metalphoto Panel

Printed Circuit Board

Assembly

Parts List

The following list gives the drawing numbers and subtitles for the plug-in chassis system:

Q-2600-1

Q-2600-2

Q-2600-3

Q-2600-4

Q-2600-5

Assembly

Details

Details

Details

Details

# 2.5.6.2 Theory of Operation

# General

The MSRE test module is a special-purpose module designed to provide signals to test parts of the nuclear safety system of the MSRE.

Although it was originally intended to have a general-purpose test module which would be applicable to several reactors, and such a module Q-2601 was designed, it soon developed that a single test module would not suffice because of the different instrument sensitivities and varied functions of the several reactor systems under design. Consequently, a separate test module was designed for each reactor that uses this type of instrumentation. In spite of the unique project application of the module and because of the general applicability of the circuits used in the module, a "Q" number was assigned to the MSRE test module for the convenience of designers of future systems.

# Circuit Description

Ramp Generator. - A linear voltage ramp is generated by charging a capacitor with a constant current. In circuit diagram Q-2634-1, it is seen that the base of transistor Q1 is held at a constant potential with respect to the +25-v supply by Zener diode D1. This in turn causes the emitter voltage of Q1 to be constant across a fixed resistor R2, establishing constant emitter current. To a first approximation, transistor collector current is equal to emitter current, regardless of collector voltage, until saturation is reached, that is, until the collector voltage equals the emitter voltage. Thus, the collector current of Q1 is constant and flows into capacitor C1.

In the standby condition, the capacitor is short-circuited by contacts of relays K1 and K2 and by contacts of push buttons S7 and S8. When any one of these contacts opens, the capacitor begins to charge. The rate of change of voltage across the capacitor is determined by the magnitude of the current and the size of the capacitor. In this case

$$
\begin{array}{l} \frac {\mathrm {V}}{\mathrm {t}} = \frac {\mathrm {I}}{\mathrm {c}} \\ = \frac {2 0 \times 1 0 ^ {- 6} \mathrm {a m p}}{2 0 \times 1 0 ^ {- 6} \mathrm {f}} = 1 \mathrm {v} / \sec . \\ \end{array}
$$

The voltage across C1 is sensed by a very high beta Darlington-pair emitter follower Q2 and Q3. The maximum amplitude of the ramp is limited by saturation of Q1 and Zener diode D1 to about 15 v across C1 or 14 v at the emitter of Q3.

Current Switching. - The MSRE test module is designed to provide test currents for both the flux amplifier and the period safety module. Since the input of the flux amplifier is in series with the log diode of the period safety module, any test current will be sensed and indicated by both instruments. Since the flux amplifier has $100\%$ feedback to the input terminal, there is no input voltage offset. This means that a relatively low-voltage current source is adequate for generation of its test currents. For application to the period safety, a better current source is required, since the voltage across the log diode is not constant but changes with input current. To this end the calibration currents for the period safety are produced by using the chamber high-voltage supply and suitable multiplier resistors. The "Rate" test currents and the "Adjustable" test currents are intended for use with the flux amplifier only; further, application of either of these currents causes the

period safety to indicate an incorrect current, which should be ignored.

Since all test currents are applied by way of a second ionization chamber signal lead, which is separate all the way to the chamber plates, a test signal must travel to the chamber and back to the safety channel input. In this way a successful current test verifies that the chamber is connected.

Flux Amplifier. - For steady-state calibration or checks, a voltage adjustable from 0 to 20 v by a front-panel Helipot may be applied through either a 200-kilohm or a 200-megohm resistor to the amplifier input by energizing relay K4 or K3 respectively. The corresponding currents are 0 to 100 μa and 0 to 100 na. The Helipot dial labeled "Current Adjust" is read directly from 0 to 100 units.

The voltage ramp described above may be applied through a 300-kilohm or a 300-megohm resistor by energizing relay K1 or K2, respectively, resulting in current ramps ranging from 0 to $46.7\mu \mathrm{a}$ and 0 to $46.7\mathrm{na}$ . The ramp is initiated by a second contact of K1 or K2, which removes the short circuit from capacitor C1.

Period Safety. - Fixed calibration currents for the period safety module are generated by applying the chamber high voltage (approximately 250 v) through either a 25- or a 250,000-megohm resistor, resulting in currents of $10^{-5}$ or $10^{-9}$ amp. These currents are initiated by energizing relays K5 and K6 respectively.

To check the calibration of the period amplifier, the voltage ramp is applied to the input (terminal 6) of the log current amplifier. Subsequent differentiation in the period amplifier results in a constant-voltage output (constant indicated period) whose magnitude is determined by the generated ramp rate and the gain of the log current amplifier. Two calibration points are provided by applying the voltage ramp through either a 500-kilohm or a l-megohm resistor; the result is a period indication of about 1 and 2 sec respectively. Actually, the l-sec period test should always generate a period slightly less than 1 sec, so that the l-sec fast-trip comparator will trip. These tests are initiated by depressing push buttons S7 or S8 to generate the l- or 2-sec period.

Chamber Voltage Monitor. - In a manner similar to the signal lead, a separate high-voltage lead is returned from the plates of the ionization chamber. This voltage is continuously monitored by a circuit consisting of transistors Q4 through Q8. If the voltage, normally 250 v, is interrupted or reduced below approximately 200 v, an undervoltage alarm occurs.

The sensed voltage is reduced from 250 to 100 v at R5 by two Zener diodes, D2 and D3. The voltage is further reduced to 20 v at the base of Q4 by the dividing action of R5 and R6. The emitter of Q4 is biased at 10 v, so that the transistor is reverse biased and not conducting under normal conditions. Since the collector of Q4 is near ground potential, the Darlington emitter follower Q5 and Q6 and the relay drivers Q7 and Q8, driven by the emitter-follower output, are also not conducting. A normally closed contact of K7 energizes the green "Normal" lamp on the front panel.

When the input voltage drops below 200 v, the Q4 base voltage is reduced to below 10 v, and Q4 conducts. The collector voltage of Q4 increases to 10 v, turning on Q5, Q6, Q7, and Q8 and energizing both K7 and K8. The contacts of K7 extinguish the "Normal" lamp and light the

red "Low" chamber voltage lamp. A second set of K7 contacts controls external circuits. K8 seals itself in and will remain energized, light- ing the "Latch" lamp, until input voltage is restored and "Reset" button S2 is depressed. This enables the operators to identify a momentary chamber voltage fault.

The voltage monitor circuit is tested by pressing "Test" push button S1 on the front panel. This reduces the voltage at the base of $Q_4$ , simulating a low input condition without causing significant reduction of the chamber voltage itself.

# 2.5.6.3 Operating Instructions

# Installation

The MSRE test module is one of the ORNL modular reactor instrumentation series. Like the other modules in this series, it has standard connections and dimensions and has a pin-and-hole code on the rear plate so that the module will not be inserted in a wrong location in a drawer. The module is installed by placing it in its proper location, inserting the module firmly, and tightening the thumbscrew. The module may be plugged in with power on without damage.

# Operating Controls on Panel

Chamber Voltage Monitor. - Three pilot lamps indicate the state of chamber voltage. The green "Normal" light is on when the voltage is greater than 200 v. The red "Low" light is on when the voltage is less than 200 v. The amber "Latch" light comes on when the voltage drops below 200 v and remains on until the "Reset" button is pressed. When the "Test" button is depressed, it causes a simulated low voltage to test the monitor.

High Rate. - When the "High Rate" button is depressed, a current ramp of $3.33\mu \mathrm{a} / \mathrm{sec}$ is applied to the safety channel input.

Low Rate. - When the "Low Rate" button is depressed, a current ramp of 3.33 na/sec is applied to the safety channel input.

High Current. - When the "High Current" button is depressed, a current, adjustable from 0 to 100 $\mu$ a by the "Current Adjust" potentiometer, is applied to the safety channel input.

Low Current. - When the "Low Current" button is depressed, a current, adjustable from 0 to 100 na by the "Current Adjust" potentiometer, is applied to the safety channel input.

High Log Current. - When the "High Log Current" button is depressed, a current of $10^{-5}$ amp is applied to the safety channel input.

Low Log Current. - When the "Low Log Current" button is depressed, a current of $10^{-9}$ amp is applied to the safety channel input.

l-sec Period. - When the "l-sec Period" button is depressed, a voltage ramp is applied to the period safety module, resulting in an output indication of approximately a l-sec period.

2-sec Period. - When the "2-sec Period" button is depressed, a voltage ramp is applied to the period safety module, resulting in an output indication of approximately a 2-sec period.

# Connections

All connections are made through the rear connector P28 when the module is inserted. A jumper between pins 4 and 12 is provided so that if the module is removed from a drawer, a warning signal may be given.

# Operating Procedures

All tests are initiated simply by depressing the proper push button on the front panel.

2.5.7 Fast-Trip Comparator, ORNL Model Q-2609

# 2.5.7.1 Description

# General

The fast-trip comparator<sup>10</sup> circuit (Fig. 2.5.16) compares the magnitude of two input dc signals having opposite polarities and produces an output voltage having either of two possible values, depending upon which input voltage is larger. Two electronic outputs drive logic circuits external to this unit, and there are also two relay drivers within the unit. The change in voltage from one level to the other is completed in less than 200 msec after the trip signal occurs. The relays can change states in approximately 10 msec. Each relay has one set of contacts for external connections and one set to perform an indicating function on the front panel. One relay can be connected to hold a trip indication after the trip has cleared, and the other relay indicates the immediate state of the circuit.

Several external connections can be made that allow the circuit to trip for a variety of input conditions. With a reference serving as one signal, the circuit can trip on a positive or a negative input signal and on an increasing or a decreasing signal. For the case of two external signals A and B, tripping action can take place when the magnitude of A is greater than or less than that of B, provided A and B have opposite polarities.

# Construction

The fast-trip comparator is constructed in a single module 1.40 in. wide, 4.72 in. high, and 11.90 in. deep. It is a standard "one-unit" plug-in module of the modular reactor instrumentation series depicted on drawings Q-2600-1 to Q-2600-5.

The circuit is constructed on a printed circuit board mounted within a shielding enclosure with removable sides.

# Application

The fast-trip comparator is intended primarily to be used as a voltage level discriminator for safety and control functions in a nuclear reactor. For maximum flexibility the unit has two inputs, so that it may be used either to compare two signals or to compare one signal with an external reference. The circuit is bistable in nature; that is, there is no change in output indication until the predetermined trip level is exceeded, at which time the output suddenly changes from one state to the other. The trip level is nominally zero volts; that is, the two inputs must be of opposite polarity, so that when the magnitude of one input exceeds the magnitude of the other, the circuit changes state. By use of suitable external jumpers the circuit can be arranged to trip on either net positive or net negative input.

Two types of output are available. The logic output, intended for use in fast safety systems, is -10 v normally and 0 v when tripped. The switching time is less than 200 μsec. Normally the logic level will revert to normal as soon as the input signal drops below the trip level. However, by use of external jumpers, the circuit can be made to latch, or seal, the logic output in the trip state until manually reset, provided the trip signal persists for 10 msec or more.

The second type of output is provided by two relays. Both relays are driven by the logic signal described previously and respond accordingly. K1 may be arranged to latch if the trip signal persists for more than 10 msec; the relay will go to the trip state and remain there until manually reset, regardless of whether or not the logic level signal is arranged to latch. This arrangement is sometimes called a "scram catcher," in that it allows a momentary trip to be located and identified after it has disappeared. K2 operates directly off the logic signal and will be in the same state. Contacts of both relays are available for actuating external circuits.

# Specifications

Specifications for the fast-trip comparator are as follows:

Trip range

The trip range shall be adjustable from $+1$ v to $+10$ v or from $-1$ v to $-10$ v

Trip point accuracy

Once the trip point has been set, variations in temperature from $10^{\circ}\mathrm{C}$ to $55^{\circ}\mathrm{C}$ and aging of components should not cause the trip point to change more than 50 mv referred to the trip circuit input signal

Trip point hysteresis

When the signal falls $60\mathrm{mv}$ below the trip point, the circuit shall reset itself; the circuit shall not reset less than $40\mathrm{mv}$ below the trip point

<table><tr><td>Input impedance</td><td>150 kilohms, either input</td></tr><tr><td>Logic output</td><td>In the normal state the logic level output shall be -10 v ± 1/2 v, 20 ma maximum drain; in the trip state the logic level output shall be 0 v ± 1/2 v</td></tr><tr><td>Tripping time logic level</td><td>The change from normal to abnormal condition (-10 to 0 v) shall require less than 200 μsec</td></tr><tr><td rowspan="2">Relay outputs</td><td>Type 1 is a DPDT relay having contacts rated at 2 amp at 32 v dc and 2 amp at 115 v ac; this relay must change state in less than 100 msec</td></tr><tr><td>Type 2 is a fast-latching relay that will operate in less than 10 msec; the purpose of this relay is to indicate the location of a momentary trip signal</td></tr><tr><td>Power required</td><td>+15 v ± 0.25 v dc with regulation of 0.1%; -15 v ± 0.1 v dc with regulation of 0.1%; +10 v ± 0.1 v dc with regulation of 0.1%; -32 v ± 4 v dc, unregulated</td></tr><tr><td>Ambient temperature range</td><td>10 to 55°C</td></tr><tr><td>Indication</td><td>Front-panel indicator lights shall show the immediate state of the trip, that is, &quot;Trip&quot; or &quot;Normal,&quot; and also &quot;Latch,&quot; which indicates that a momentary trip of 10 msec or more has occurred</td></tr><tr><td>Test and reset</td><td>Front-panel push buttons shall cause the circuit to trip regardless of the input signal (&quot;Test&quot;) and to reset the latch indication (&quot;Reset&quot;)</td></tr></table>

# Applicable Drawings and Specifications

The following list gives the drawing numbers (ORNL Instrument Department drawing numbers) and subtitles and fabrication specification number for the fast-trip comparator:

Q-2609-1

Q-2609-2

Q-2609-3

Q-2609-4

Q-2609-5

Q-2609-6

SF-253

Circuit

Details

Metalphoto Panel

Printed Circuit Board

Assembly

Parts List

Fabrication Specification

The following list gives the drawing numbers and subtitles for the plug-in chassis systems:

Q-2600-1

Q-2600-2

Q-2600-3

Q-2600-4

Q-2600-5

Assembly

Details

Details

Details

Details

# 2.5.7.2 Theory of Operation

# General

The fast-trip comparator is composed of three functional parts: a voltage comparator, logic switching circuits, and relay drivers.

The input stage, consisting of Q1 and Q2, is a compound (Darlington) differential amplifier having a high degree of temperature stability and a high input impedance. This stage drives a simple differential amplifier Q3, which, in turn, drives a Schmitt trigger circuit Q4. These three stages make up the voltage comparator.

All transistors after the Schmitt trigger circuit act as switches and are either off (open) or saturated (closed). Transistor Q5 acts as a buffer to prevent the Schmitt trigger circuit from being affected by variations in the load. Electronic output points are located at the collectors of Q6 and Q7.

Two double-pole, double-throw relays K1 and K2 each provide one set of contacts for the operation of external circuits and one set for the operation of indicator lamps on the front panel of the trip circuit. Relay K1 may be connected to hold the "Latch" indicator lamp I1 from the time a trip has occurred until the manual reset switch S2 has been depressed, even if the signal level decreases below the trip point. Relay K2 energizes indicator lamp I2 ("Trip") or I3 ("Normal"), depending upon the existing state of the circuit. Either or both of the relay drivers Q8 and Q9 may be driven from either electronic output. For operational flexibility the connections to the electronic outputs and the relay drivers are made externally through plug P7. The following sections provide a detailed discussion of the design and operation of the various stages of the circuit.

# The Voltage Comparator

The input stage Q1 and Q2 is a compound differential amplifier. The compounding Q1 provides high input impedance. The two inputs are applied to a single base, rather than differentially to the two bases, so that no shift in output will occur when the two inputs are of equal magnitude

at various levels from -10 to +10 v. The 2-kilohm trimming adjustment R2 is used to balance the input resistors R1 and R3. The output of the first stage appears at the collector of Q2A and is coupled to the second stage through R10 and R10a.

The second stage Q3 is a simple differential amplifier that provides additional voltage gain to increase the sensitivity of the amplifier. Overall negative feedback is employed from the collector of Q3B to the base of Q1A (R36) to adjust the sensitivity to the desired level and to improve the temperature-drift characteristics. The dc level is adjusted by trimpot R10 to establish the correct trip point.

The output of the second stage Q3 is directly coupled to the Schmitt trigger circuit Q4. The Schmitt trigger circuit is a regenerative bistable circuit that provides the actual voltage level discrimination. The output of the Schmitt trigger circuit and all succeeding stages have only two stable states, "Normal" and "Trip."

# Logic Switching Circuits

Loading effects on the Schmitt trigger circuit are buffered by an isolation stage Q5. The bistable signal is then coupled to Q6, where the logic levels are established. When the collector of Q5 (and the base of Q6) is in the "high," or more positive, state, Q6 is biased off, allowing Zener diode D1 to be fired through R25. The logic level output at pin A of P7 is then $-10\mathrm{v}$ , as determined by the breakdown voltage of D1.

In the "low" state, when the voltage at the base of Q6 is less positive (actually slightly negative), Q6 is saturated, shunting Zener diode D1, and the magnitude of the output at pin A is near zero (less than 0.2 v). The Q7 stage is nearly identical to Q6 and provides an inverted logic level output for maximum flexibility; that is, when the level at pin A is -10 v, Q7 is saturated, producing "zero" level at pin J. Conversely, when the level at pin A is "zero," Q7 is cut off and the output at pin J is -10 v.

The inherent speed of response of the entire electronic circuit, from a sufficient level change at the input pin T to a logic level change at either pin A or pin J, is about 10 $\mu$ sec. However, this speed of response has been intentionally lessened to about 120 $\mu$ sec by capacitors C1 to C4 to reduce the tendency to respond to sharp noise spikes.

# Relay Drivers

Either logic output may be connected to either or both of the two relay drivers Q8 and Q9. Normally K1 is intended to pick up when a trip (abnormal) condition exists. To accomplish this, the base of Q8 is connected through R30 and pin K of P7 to a logic output that is at -10 v in the "Trip" state, namely, either pin A or pin J. Note that "Trip" and "Normal" are related to the character of the input signal and refer to a signal which may be either too large or too small and either positive or negative. The proper connections for a desired signal and function can be determined by referring to the connection table on circuit diagram Q-2609-1.

One set of contacts of K1 is used to latch in the coil of K1 to keep it energized after a trip has occurred and cleared. This optional function is accomplished by connecting pin d of P7 to battery ground (pin W).

Relay K2, driven by Q9, is normally connected so as to drop out in the trip state. This relay is intended to show the immediate state, and no provisions are made to latch it.

One set of form C contacts is available from each relay to operate external circuits.

The logic level output may be latched in the trip state by using the output contacts of relay K1. Pin b is connected to pin B, and either positive or negative 15 v is connected to pin F, depending upon the nature of the input signal. When this connection is used, K2 also latches, because it is driven by the logic signals.

# 2.5.7.3 Operating Instructions

# Installation

The fast trip comparator Q-2609 is a module in the ORNL modular reactor instrumentation series. Like the other modules of the series, it has standard connectors and dimensions and has a pin-and-hole code on the rear plate so that the module will not be inserted in a wrong location in a drawer. The module is installed by placing it in its proper location, inserting the module firmly, and tightening the thumbscrew. The module may be plugged in with power on without damage.

# Operating Controls

The only integral operating controls are the "Trip Test" and the "Reset" push buttons. The "Trip Test" push button causes the circuit to trip by overriding the input signal. The circuit will remain in the trip position if the screwdriver-actuated push button is rotated clockwise after being depressed.

"Reset" is a momentary push button that releases relay Kl and the "Latch" indication.

In a good many applications of the fast-trip comparator, a single signal will be compared against a reference. The reference can be fixed by a simple external voltage divider, or it can be adjusted by means of a Helipot located in the drawer into which the trip circuit is plugged. This adjustment is shown on the circuit diagram as R4 and is, in effect, an operating control of the trip circuit.

# Connections

All connections to the fast-trip comparator are made through the rear connector P7 when the module is inserted. After initial calibration is completed, there are no adjustments or connections to be made within the module itself. However, a high degree of flexibility is provided through external connections. The various possible modes of operation and the connections required to achieve them are detailed in the connection table on circuit diagram Q-2609-1 and in the following section.

# Operating Procedures

Input Signals. - The input signals to the trip circuit should be supplied from a low-impedance source (500 ohms or less). A single signal may be either positive or negative within the range of $\pm 10$ v. The magni

tude of two different signals may be compared, but they must be of opposite polarity. The input terminal for a single signal is pin T, and an external reference voltage of opposite polarity is required on pin M. If two signals are compared, the reference voltage is not required, and the second signal is connected to pin M.

Reference Voltage. - The external reference voltage is required on pin M when the input is a single signal. This reference must be exactly equal in magnitude to the desired signal trip point and of opposite polarity. The source impedance should be 500 ohms or less. In applications where the trip point is to be changed occasionally, the reference may be derived from a 500-ohm precision potentiometer connected to a 10-v supply. A potentiometer with $0.1\%$ linearity will be sufficiently accurate to allow direct reading of the potentiometer dial as the trip voltage. Such a potentiometer is shown on the circuit diagram as R4.

In applications where infrequent or no changes in trip point are anticipated, the reference should be derived from a 10-v supply and a fixed voltage divider with a total series resistance of approximately 500 ohms.

It should be noted that, within the accuracy specifications of the trip comparator, the trip point is directly equal in magnitude to the reference voltage, and any drift or inaccuracy of the reference will result in equal error of the trip point. The accuracy specifications do not apply in the range -1 to 0 to +1 v, and adjusting the reference to a trip point in this range should be avoided.

Signal Polarity and Direction. - Since the comparator is designed for general-purpose use, it is capable of providing a trip signal for any of the following conditions:

1. positive input signal increasing to a value greater than arbitrary positive reference value;   
2. positive input signal decreasing to a value less than arbitrary positive reference value;   
3. negative input signal decreasing, becoming more negative than arbitrary negative reference value;   
4. negative input signal increasing, becoming more positive than arbitrary negative reference value;   
5. when input signal "A" is greater (more positive) than input signal "B," both "A" and "B" positive;   
6. when input signal "A" is less (more negative) than input signal "B," both "A" and "B" negative.

Different external connections are required for different types of input signals to achieve proper output sense. These connections are shown in the table on the circuit diagram (Fig. 2.5.16). The column headings refer to the nature of the signal; for example, the second column is headed "Pos. Signal, High Trip." This means that the input signal may range from 0 to $+10\mathrm{~v~}$ , and trip will occur when the signal is greater in magnitude than the reference. The fifth column is headed "Neg. Signal, Low Trip," which means that the signal range is 0 to $-10\mathrm{~v~}$ and that trip occurs when the signal is smaller in magnitude than the

reference. The column entries under the selected heading show the voltage or destination for the pin or terminal in the same row of column 1 on the left.

The preceding discussion of the second column, labeled "Pos. Signal, High Trip," is continued. The first row shows pin T as the signal input. Pin M connects to terminal l, which is the wiper of the reference potentiometer. Pin M could go instead to the pickoff tap of a fixed divider if a fixed trip point is desired. Pin L connects to +10 v to provide the proper test voltage. Pin A is jumpered to pin K to provide proper drive to Q8. Pin J is jumpered to pin Z to provide proper drive to Q9 and is also the correct logic level output for driving external circuits.

Latching. - Latching instructions are not shown in the table in Fig. 2.5.16, but they are shown at the appropriate connector pins on the circuit diagram. With no latching, K1, K2, and the logic level outputs will all indicate the immediate state of the comparator. Connecting pin to battery ground causes only K1 to latch, that is, to remain in the trip state after a trip signal has cleared until the reset button is pressed.

If it is desired to also latch the logic level outputs in the same manner, it is necessary to jumper pin b to pin B and connect an appropriate voltage to pin F, as shown in the table. In this condition all outputs, K1, K2, and both logic levels will latch and remain in the trip state after a trip-level signal occurs.

# Precautions

Relay Contacts. - The contacts of the relays used in the fast-trip comparator circuit are rated for resistive loads only. If inductive loads are necessary, appropriate contact-arc suppression techniques should be employed.

Transistors. - Some of the transistors used in the circuit unavoidably have small reverse base-emitter voltage ratings. Most ordinary laboratory-type ohmmeters, such as the Triplett 630 or the Simpson 260, have sufficiently high voltage on some resistance scales to permanently damage these transistors. The common practice of using an ohmmeter to check transistors when trouble-shooting should be avoided in this unit.

Trip Point near Zero Volts. - The trip-point accuracy specifications do not apply at trip voltages near zero. Owing to possible inaccuracy, trip points between -1 and +1 v should be avoided.

2.5.8 Coincidence Matrix Monitor, ORNL Model Q-2624<sup>11</sup>

# 2.5.8.1 Description

# General

The coincidence matrix monitor is designed to monitor and indicate on front-panel meters the current through each leg and the total current in a two-out-of-three relay matrix.

# Construction

The coincidence matrix monitor is constructed in a module 5.66 in. wide, 4.72 in. high, and 11.9 in. deep. It is a standard "four-unit" plug-in module of the ORNL modular reactor instrumentation series depicted on drawings Q-2600-1 to Q-2600-5.

# Application

The coincidence matrix monitor is intended to monitor and to regulate the current supplied to a safety-rod scram clutch, or magnet, in a nuclear reactor. Figure 2.5.17 is a diagram of a typical application, where relay contacts A, B, and C come from separate safety channels.

# Applicable Drawings

The following list gives the drawing numbers (ORNL Instrument Department drawing numbers) and subtitles for the coincidence matrix monitor.

Q-2625-1

Q=2624-2

Q-2624-3

Q-2624-5

Q-2624-6

Circuit

Details

Metalphoto Panel

Assembly

Parts List

# 2.5.8.2 Theory of Operation

As indicated in Fig. 2.5.17, the total current delivered to the clutch is adjusted by resistor Rl. If all the relay contacts are closed, and since resistors R2, R3, and R4 are equal, the current will divide equally in the three legs of the matrix. The total current goes through the clutch and returns to ground through the "clutch current" meter. The maximum voltage that can be applied to the clutch is limited by Zener diode D1 to +30 v. An external meter may be connected between pins 10 and 14.

If a single channel trips, two legs of the matrix are opened and all the current flows through the remaining leg. Therefore, the tripping of either of the two remaining channels causes the third leg to open, which interrupts the clutch current. With two legs open, the resistance of the matrix is increased by a factor of 3; thus resistors R2, R3, and R4 must be small enough so that the current delivered to the clutch is not decreased to less than a reliable holding current. To ensure that the clutch coil can be deenergized, the monitor must be able to detect leakage paths around the relay contacts. If the leakage resistance is small enough, sufficient current can be supplied to keep the clutch energized with the contacts open. For example, suppose channel A has been tripped. However, one contact, instead of completely opening, can now be represented by resistance $\mathbf{R}_{\mathbf{x}}$ . The minimum resistance value of interest can be found by the equation

$$
i _ {c m} = \frac {E}{R _ {4} + R _ {c} + R _ {x}},
$$

where

$$
\begin{array}{l} i _ {c m} = \text {m i n i m u m c l u t c h h o l d i n g c u r r e n t}, \\ R _ {c} = \text {c l u t c h} \\ E = \text {m a x i m u m s u p p l y v o l t a g e}. \\ \end{array}
$$

The clutch current will divide between the branches B-C and A-B, where the current through A-B is given by the equation

$$
i _ {x} = i _ {c m} \frac {R _ {2}}{R _ {4} + R _ {x}}.
$$

The requirement is that the current $i_{x}$ be easily detected on the meter A-B.

# 2.5.8.3 Operating Instructions

# Installation

The coincidence matrix monitor is a module in the ORNL modular reactor instrumentation series. Like the other modules of this series, it has standard connectors and dimensions and has a pin-and-hole code on the rear plate so that the module will not be inserted in a wrong location in a drawer. The module is installed by placing it in its proper location, inserting the module firmly, and tightening the thumb-screw. The module may be plugged in with the power on without damage.

# Operating Controls

Current Adjustment. - A recessed screwdriver adjustment, labeled "Clutch Current Adjust," is located on the front panel. The proper operating clutch-coil current determines this adjustment.

Panel Meters. - The panel meters are calibrated to indicate from 0 to $250\mathrm{ma}$ . These meters are in series with the clutch and indicate coil current directly.

![](images/fcc951912601288e61733d0cad9752266f1c659ff66e5a06c9a9128d7eddfbdf.jpg)  
Fig. 2.5.1. MSRE Safety System for Control Rods. Block diagram of typical channel.

![](images/2237b19c85eed4738d8da5a431bf38a3ec4acecd1d89500393f10e8dcd400b4e.jpg)

![](images/889753a87af821e1f691771df1b910fed57a1bddaf7a46c7f6369cd9a8e1358f.jpg)

![](images/8763ff0973e07294ce72f5fbeb4ac28170976cb52ac1b0eeb68ed63354924e6e.jpg)

![](images/cfb37c3fd2c977082f77e7921a731899ff3e781c5e5376dc31b4e8f3fb4b83e8.jpg)  
Fig. 2.5.2. MSRE Flux Level Scram Trip Point Switching.

![](images/60a992cc9f0b4a4b95fd161f3e5af030f99ccf27e9f7fedff45b28d35d7a6194.jpg)  
ORNL-DWG 66-9124R   
Fig. 2.5.3. Flow Diagram of Switching Signals that Change Reactor Power Set Point for Rod Scram.

![](images/5dd19c349486b2b01ad3a19185396269aa0c537fd75b15c80cb92210f2192ae6.jpg)  
Fig. 2.5.4. Diagram of Instruments Used to Measure Temperature in a Typical Safety System Input Channel.

Fig. 2.5.5. Diagram of Safety System Rod Scram Circuits.   
![](images/8061b487ec64555f14e87d6e5faca0a75a5aee1f88afb8d551da386602be413d.jpg)  
NOTES:   
1. Q-NUMBERS REFER TO ORNL INSTRUMENT AND CONTROL DIVISION DWG. NOS.   
2. ALL RELAY CONTACTS AND SWITCHES SHOWN WITH SYSTEM ENERGIZED AND OPERATING NORMALLY.  
3. THIS RELAY $(\mathbf{K}_{\mathbf{A}}4)$ PROVIDES ONE OF THE "REVERSE" ON SCRAM CONTACTS; TYPICALLY CONTACT NO. RSS-NSCI-A4 IN CIRCUIT NO.248 ON DWG D-HH-B 57327.

![](images/e5651c2ff1fb63970c4f402d3203c5e8cbdadbd4420791cdf4974bf71b9353d3.jpg)

![](images/85495461bec481f84985a27fc81bd3da991bddacd2eecf0739692460f1e114d7.jpg)

![](images/cd4df46afe5f63de801b03fe4af030da63c1c90714ce81723a2629921c3ed7ad.jpg)

![](images/651d39d59ef39c18c885486b79f0b2dbeec5b5c97ee518f2be64d0593557e1d8.jpg)  
Fig. 2.5.6. MSRE Nuclear Safety System Circuit Details.

![](images/8a70d97fe2c840a64d172351b7c07ef9de378c74a2ae558c45bc849867cc3bb2.jpg)

![](images/a0b6a759c7a3cedda26169059a1617e82784e47b50fd9aa5db39bfdca65dba37.jpg)

![](images/6279a7c40bbab3cbf74eb7b588853506d01668784946a742c405c7af08522b8c.jpg)

![](images/0557ef891b44435987101fe3d6267d2d15cdbb291e8b2b35f16f84e03ff76780.jpg)  
Fig. 2.5.7. Safety System Circuit Diagram.

![](images/25de205cf8b3c7aadb2d2aed33e4564b318116b1af0b4640f043cdec56f55ea1.jpg)

ORNL-DWG67-1104

![](images/cec2bde1c281968236b3f3b1436ad217db086ac05c67a254c71f4a941a359714.jpg)  
Fig. 2.5.8. MSRE Safety Chamber.

![](images/51c5025982e33ed0f963e2412b1428d0f44fb056999662ce6b637aa2a0d6add8.jpg)

![](images/b7f254d73f972abfc9e7949aedb60ece3c97b92245b349bf2bb24b90bbdc64e8.jpg)  
Fig. 2.5.9. Saturation Curves - MSRE Safety Chamber.

![](images/3d8ea4dc582d9fd6b2a40803956d89426235063c4e27d9291ad203421cfdcbad.jpg)  
To zero instrument, places jumper between TP1 and TP4, measure voltage between TP3 and TA4 with Triplett meter (or equal), adjust "Sel 2" until voltage is zero. Remove jumper from TP1 and TA4 and place between TP3 and TA4, measure voltage from TP6 to TP6, Adjust "Sel 2" until voltage is zero. Remove jumper. The Period Amulator may be zeroed any time the input is not changing by adjusting "Sel 3" until front panel period meter indicates "0"

![](images/a58e04e2f8ba674717864f80d3526b5840620970451227449defd3ba4e976a22.jpg)  
CN3609

![](images/5e99a46ff9dd0579c6b8989e897af5e8206b8e189a81661e8f530279845e767e.jpg)  
Fig. 2.5.10. Period Safety Circuit.

A00-3

<table><tr><td>NO.</td><td colspan="3">REVISIONS</td><td>DATE</td><td>APPD</td><td>APPD</td></tr><tr><td>C.E.M.A.PROGRESS</td><td>PART P-4.5</td><td>ENQ</td><td>PART</td><td>APPD</td><td></td><td></td></tr><tr><td>6 in PRAP</td><td>PART 4.3-4.5</td><td></td><td>PART</td><td>APPD</td><td></td><td></td></tr><tr><td>GRAPHS</td><td>PART</td><td>OFFLINE</td><td>PART</td><td>APPD</td><td></td><td></td></tr></table>

NoHo:

All resistors $1\%$ deposited carbon except as nofoe.

<table><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>DATE</td><td colspan="2">OREV. SEPIA DRAWING NO.</td><td>APPD. BY</td></tr><tr><td colspan="3">SEPLAS ISSUED FROM Q-2635-1</td><td></td></tr></table>

FOR INFORMATION ONLY

DO NOT USE FOR

MAINTENANCE OR

CONSTRUCTION

<table><tr><td>DETAILS</td><td>Q-2456-2</td></tr><tr><td>METALPHOTO PANEL</td><td>Q-2458-3</td></tr><tr><td>PRINTED CIRCUIT BOARD</td><td>Q-2458-4</td></tr><tr><td>ASSEMBLY</td><td>Q-2458-5</td></tr><tr><td>PARTS</td><td>Q-2458-6</td></tr><tr><td>REFERENCE DRAWINGS</td><td>DWG. NO.</td></tr><tr><td colspan="2">E.N.FRAY</td></tr><tr><td colspan="2">MODULAR REACTOR INSTRUMENTATION</td></tr><tr><td colspan="2">PERIOD SAFETY
CIRCUIT</td></tr><tr><td colspan="2">INTERVENTION AND CONTROLLED SEQUENCE
OAK RIDEE NATIONAL LABORATORY
UNCLASSIFIED ITEMS</td></tr><tr><td>Z.S.W.D.</td><td>Z.W.D.</td></tr><tr><td>###</td><td>Q-2635-1 ###</td></tr></table>

![](images/62160562c33d9c159bd0119fc9f63af1629789a4cfe199a07f5bd628e48411c0.jpg)  
C   
C   
C   
Fig. 2.5.11. Chamber High-Voltage Supply and Flux Amplifier Circuit.

![](images/4dc0910cf83c30236ac8fc0cc28b6fc7d5807dce6d2d5e3ee332c278018c152c.jpg)

![](images/5b9fc3e652a95ecc1e94f4249f434e56e2ee7648075afb51429726eb720b5f06.jpg)

![](images/f0eb0e5223711d22b4e09cfbde84bac72ea60567028f246264060dc9408e2859.jpg)  
Fig. 2.5.12. Output Voltage vs Load Current for Chamber High-Voltage Supply, Q-2602.

ORNL-DWG 67-6437

![](images/326ae2e25033c6437afe13f3c327aaaef06ec2413a31265ee172526c949d7603.jpg)  
Fig. 2.5.13. Amplifier Feedback Circuit.

![](images/3a9ccc563b6ff33b802744db94727f65d54d78a6b396208de2c6380c56150d50.jpg)

C

ORNL-DWG67-6436

![](images/dc86d4d88158860737074ab7c72891584500e6117a39cdc2ac3f448606466ef2.jpg)  
Fig. 2.5.14. Amplifier Gain-Adjusting Circuit.

C

![](images/46faf1fc191e39521deca1c08dae2018c3157d2fc8e5a9ceaa70f8aa6997ffff.jpg)  
Fig. 2.5.15. MSRE Test Module Circuit.

#

#

#

![](images/1b207edbfe0e2123c973f004c1c50f9009cd53ad808fa5f09ee2e572654eab22.jpg)

![](images/04a4b23111980a82a97329f705371fbad8542681084631640151927e07595edd.jpg)  
C

![](images/1b8873967a653484aa7fd08dd70de0554ac983c751248453a74275d696018280.jpg)  
Fig. 2.5.16. Fast-Trip Comparator Circuit.

<table><tr><td colspan="2">PARTS LIST</td><td>0-2605-6</td></tr><tr><td colspan="2">ASSEMBLY</td><td>0-2604-5</td></tr><tr><td colspan="2">PRINTED C/T. BD.</td><td>0-2603-4</td></tr><tr><td colspan="2">METALPHOTO PANEL</td><td>0-2603-3</td></tr><tr><td colspan="2">DETAILS</td><td>0-2603-2</td></tr><tr><td colspan="2">REFERENCE DRAWINGS</td><td>DWG. NO.</td></tr><tr><td colspan="3">J.L.ANDERSON</td></tr><tr><td colspan="3">MODULAR REACTOR INSTRUMENTATION</td></tr><tr><td colspan="3">FAST TRIP COMPARATOR
CIRCUIT</td></tr><tr><td colspan="3">INSTRUMENTATION AND CONTROLS DIVISION
OAK RIDGE NATIONAL LABORATORY
ONCOMICS OR
UNION CARBIDE NUCLEAR COMPANY</td></tr><tr><td>###</td><td>###</td><td>###</td></tr><tr><td></td><td>Q-2609-1</td><td>###</td></tr></table>

![](images/ead97e0c5c13e99b0a07a53bfebeee4ca5c9ceb45868090f045dbdb49a7dbdf9.jpg)  
Fig. 2.5.17. MSRE Coincidence Matrix Monitor.

# 2.6 SHIM AND REGULATING ROD CONTROL SYSTEM

# 2.6.1 Introduction

This section is concerned with the circuitry and circuit components which are used routinely for operational control of the reactor. The rod control system should be considered as a separate system from the rod safety system described in Sect. 2.5. It is true that there is weak coupling between the systems, but only to the extent that certain interlocks in the control system depend on information received from safety systems channels. Reverse coupling is not designed into the system; that is, the rod control system circuits and components do not perform any safety functions, either as input or output elements.

The design of the control rods and the drive units is described in Sect. 2.7. The location of the rods with respect to the core, their mounting and installation, rod worths, etc., are discussed in Sect. 2.7 and in refs. 1-4.

# 2.6.2 Rod Control Circuits

Figures 2.6.1 to 2.6.4 are block and elementary diagrams that provide the basic criteria for the design of the rod control system. Table 2.6.1 lists the interlocks, safety actions, prohibitions, and permitted actions governing control rod action.<sup>1,5</sup>

The reactor system is designed so that rod manipulation is either a $100\%$ manual operation or, optionally, an automatic rod control servo-mechanism is used to maintain either constant flux or constant core outlet temperature, depending on the power being generated in the core. The rod servo is used to control one rod only; this rod is arbitrarily designated "control rod 1" on MSRE design drawings and in the text and figures in this report. The rod drive units (see Sect. 2.7) are interchangeable, and individual rod worths (ref. 3, p. 58) do not differ widely from thimble to thimble. Therefore, the control system is designed so that any one of the three rods may be selected as the servo-controlled rod (rod 1). From this it can be seen that, without supplementary information, the rod numbers used in design drawings, reports, etc., cannot be used as the only information required to designate thimble

Table 2.6.1. Control Rod Operation   

<table><tr><td colspan="2">Operational Mode</td><td>Conditions of Operation - Interlocks, Permissive Actions, Prohibitions, Automatic Actions</td><td>References and Notes</td></tr><tr><td>1.</td><td>Manual scram</td><td>1. No restrictions; at discretion of operator at control console</td><td>The manual switch contacts are not sealed</td></tr><tr><td>2.</td><td>Automatic scram</td><td>2. When any two of the three rod scram safety channels calls for &quot;Scram.&quot; Each channel requests &quot;Scram&quot; for inputs as follows: 
a) Flux (reactor power) greater than 11.25 Mw; see b below 
b) Flux (reactor power) greater than 11.25 kw when fuel salt pump motor three-phase currents are less than 35 amp 
c) Positive reactor period is less than 1.0 sec 
d) Reactor outlet temperature greater than 1300°F 
e) Channel integrity monitor shows a malfunction</td><td>See ref. 1, sect. 2.2.1, p. 58</td></tr><tr><td>3.</td><td>Individual insert (manual)</td><td>3. No restrictions other than lower limit</td><td></td></tr><tr><td>4.</td><td>Group insert (manual &quot;Reverse&quot;)</td><td>4. No restrictions other than lower limit</td><td></td></tr><tr><td>5.</td><td>Group insert</td><td>5. Automatically takes place when: 
a) Any two of three fuel salt outlet temperature measurement channels indicates greater than 1275°F 
b) Fuel salt level in the pump bowl exceeds 75% 
c) Any two of three flux measurement channels indicate reactor power greater than 9.0 Mw 
d) Any two of three flux measurement channels indicate reactor power greater than 9.0 kw, and the fuel pump motor is drawing less than 35 amp 
e) When reactor power (flux) exceeds 1.50 Mw and control system is in Operate-Start mode 
f) When positive reactor period is less than 5 sec and control system is in Operate-Start mode 
g) Rod &quot;Scram&quot; takes place</td><td>See 2b, this table</td></tr><tr><td></td><td></td><td></td><td>Power and period information used to initiate 5e and 5f comes from either of the two wide-range counting channels; see Sect. 2.3, ref. 1, Sect. 2.8, and Sect. 1.4</td></tr><tr><td></td><td></td><td></td><td>Applies motor torque in addition to gravity to initiate scram. If a rod will not fall under action of gravity the motor will drive rod in</td></tr></table>

Table 2.6.1. (continued)   

<table><tr><td>Operational Mode</td><td>Conditions of Operation - Interlocks, Permissive Actions, Prohibitions, Automatic Actions</td><td>References and Notes</td></tr><tr><td>6. Individual rod with-drawal</td><td>6. a) Prohibited, with two exceptions, if the control system calls for "Insert." All manual switches and relays are cross-interlocked so that "Insert" mode (see preceding Nos. 3, 4, 5, this table) takes precedence over "Withdraw" mode. The ex- ceptions are:1. The servo can withdraw rod 1 within the span of the regulating rod limit switch, approximately 6 in., while rods 2 and 3 are being inserted2. By manually actuating two switches simulta-neously, two rods can be withdrawn while the third is being insertedb) Prohibited during Operate-Start control system mode unless one of the following conditions is met:1) "Confidence" is established in one or more wide-range counting channels and the re- actor period in the channel(s) providing "Confidence" is greater than +25 sec2) Confidence is established in the \(BF_3\) count-ing channel and the reactor vessel is less than half full of fuel salt3) Confidence is established in \(BF_3\) counting channel and the drain tank selector switch S6 (Fill) is in the FFT position; i.e., when using flush salt in the reactor vessel, the "half-full" requirement (see preceding Par. 2) is bypassedc) Permitted in Operate-Run mode without having "Confidence" (see bl above) providing no "In-sert" request exists. However, if "Confidence" exists in one, or both channels, the reactor period in channel(s) with "Confidence" must be greater than +25 secd) Prohibited in Pre-Fill unless conditions per b above are met</td><td>Discussed in Sect. 2.6.2 and in ref. 5, p. 44</td></tr><tr><td>7. Group withdrawal</td><td>7. a) Prohibited if, for any reason, the control system calls for "Insert" as in 6a aboveb) Prohibited unless control system is in Start sub-mode</td><td></td></tr><tr><td></td><td>1) Control system must be in Operate-Start mode</td><td>"Start" is a submode of the "Operate" mode 
(Sect. 1.4); Start and Run are mutually ex- 
clusive</td></tr><tr><td></td><td>2) Reactor drain valve (FV-103) must be frozen</td><td></td></tr><tr><td></td><td>3) Pump bowl must be filled</td><td></td></tr><tr><td colspan="3">NOTE: Group withdrawal is only intended for use during startup and at powers less than 500 kw. Power limitation is by means 
of a circuit interlock in the radiator door control circuitry which requires that the reactor control system be in the "Operate- 
Run" mode in order to raise the doors and thus demand power levels above 500 kw.</td></tr></table>

locations in the core. The selection of "control rod 1" as the servo-operated regulating rod is administrative and is accomplished by making the appropriate interconnections between the rod drive units and the control and servo system circuits. These interconnections are made in junction box 120, located in the north electrical service area. Control rods 2 and 3, designated as shim rods, are always manually controlled. Figures 2.6.5 to 2.6.7 show the contacts and relays which directly govern control rod operation. Figures 2.6.5 and 2.6.6 are concerned only with the control of rod 1, the regulating rod. The dynamic brake (Fig. 2.6.6) is an addition to the design (see ref. 5, pp. 41-42), and while it does not appear on Fig. 2.6.5, it is always used in the circuit controlling rod 1. Because it is the servo-controlled rod, the circuitry is more complex than that required by the manually operated shim rods 2 and 3. The automatic rod control servo and the principles governing its design and operation are described in Sect. 2.6.3.

Certain interlocks are common to all control rod "Withdraw" circuits. The contact arrangement of these interlocks is shown in the upper left corner of Fig. 2.6.5. These interlocks are shown in block diagram form in Fig. 2.6.8. The "Confidence," "No Confidence," and "Reactor Period" interlocks originate in the $\mathrm{BF}_3$ counting channel and the wide-range counting channels described in Sects. 2.2 and 2.3 of this report.

The "Automatic Reverse" (group insertion of all rods) has been outlined in detail in Table 2.6.1, and the circuitry is diagrammed in Fig. 2.6.9. The reactor operating modes are discussed in Sect. 1.4.

The interlocks diagrammed in Figs. 2.6.5 and 2.6.8 meet the following criteria:

1. Control rod withdrawal, during reactor start and at low powers ("Start" mode), is prevented unless at least one channel of the low-level flux instrumentation is complete, is operating correctly, and is on scale. This defines "Confidence." "Confidence" is established by a wide-range channel when all the following conditions are met:

a) the indicated count rate is not less than 2 cps and not greater than 50,000 cps,   
b) the selector switch on the model Q-2614 pulse amplifier and logarithmic count rate meter module is in the "Operate" position,   
c) all the Q-2609 fast-trip comparators (a total of eight - see Fig. 2.3.3, Sect. 2.3) are plugged into their cabinet drawers and the channel is selected by the operator.

"Confidence" is established by the $\mathbf{BF}_3$ counting channel when these requirements are met:

d) the indicated count rate is not less than 10 cps and not greater than 10,000 cps,   
e) the "Use-Calibrate" switch on the count rate meter is in the "Use" position.

2. Control rod withdrawal during the "Start" mode is prevented if the reactor period, measured by either or both of the wide-range counting channels in which there is "Confidence," is less than 25 sec.

3. Control rod withdrawal, either by the operator or by the servo controller, is prevented if an automatic "Reverse" is in force.   
4. Simultaneous withdrawal (group withdrawal) of all rods is desirable only during reactor start and at low powers and should be prohibited as a means of shimming when the reactor is in the power range (the Run mode).   
5. Once the reactor is in the power region (the Run mode) and developing more than 1 Mw, the wide-range counting channel "Confidence" interlocks in the Run mode circuitry (see Sect. 1.4) are bypassed so that a loss of "Confidence" will not require a return to the Start mode and consequent reduction in reactor power. This bypassing requires that two of the three safety channels be in operation. This bypassing is accomplished by control signals from the model Q-2609 fast-trip comparators in the control rod safety system (see Fig. 2.5.1, Sect. 2.5) and a seal contact on the Run mode relay. This is done to permit long, sustained runs at power uninterrupted by mal-functions in, or maintenance of, the wide-range counting channels.

The block diagram in Fig. 2.6.8 may be difficult to interpret at first glance. It may be instructive to list and comment on the different conditions which produce continuity to point A in the diagram. The combinations listed in Table 2.6.2 are consistent with the design criteria and the characteristics of the instruments involved. Note that if either one of the wide-range counting channel log count rate meters is functioning correctly as defined by "confidence," but if the reactor period is less than +25 sec, rod withdrawal is prevented regardless of whether the reactor system is in Start or Run mode. This may appear inconsistent with the criteria in paragraph 5 above and condition 4 in Table 2.6.2. This arrangement recognizes that it is highly desirable to have at least one wide-range channel in service at all levels of reactor power and that when they are in service the interlocks which they provide will be in force. For example, suppose that the MSRE was in the middle of a long, sustained power run at, say, 5 Mw and that wide-range counting channel 2 was out of service for routine maintenance. This is condition 2 in Table 2.6.2. Now, suppose that a malfunction develops in the LCRM in the remaining wide-range counting channel 1, resulting in a loss of "Confidence" in this remaining channel. This is condition 4; reactor operation may continue unaffected by the loss of the remaining wide-range channel as long as power is above 1 Mw. Again, suppose that a malfunction not in the LCRM develops which produces a spurious, short (less than 25 sec) reactor period signal. This inhibits rod withdrawal, and the indication that a trip has taken place appears on the panel of the Q-2609 fast-trip comparator (see Fig. 2.3.3, Sect. 2.3). If a thorough check shows conclusively that the period indication is spurious, operation can be restored by manual selection of the other channel with the switch on the console or by putting the switch on the Q-2614 LCRM in the "Calibrate" position, thus going into "No Confidence" on the offending channel and establishing a signal path per condition 4. Similarly, if it develops that, in this remaining channel, one of the Q-2609 fast-trip comparators requires removal for servicing, the loss of "Confidence" so produced will not inhibit reactor operation if power is above 1 Mw.

Table 2.6.2   
T = True; F = False; NA = Not Applicable   

<table><tr><td>Situation or Condition No.</td><td>&quot;No Confidence in WRCC No. 1</td><td>&quot;No Confidence&quot; in WRCC No. 2</td><td>Reactor Period &gt;+25 Sec (WRCC No. 1)</td><td>Reactor Period &gt;+25 Sec (WRCC No. 2)</td><td>&quot;Confidence&quot; in WRCC No. 1</td><td>&quot;Confidence&quot; in WRCC No. 2</td><td>Control System in &quot;Run&quot;</td><td>Reactor Vessel Less than Half Full</td><td>&quot;Confidence&quot; in EF3 Channel</td><td>Drain Tank Selector in FFT Position</td><td>Notes</td></tr><tr><td>1</td><td>F</td><td>F</td><td>T</td><td>T</td><td>T</td><td>T</td><td>T or F</td><td>F</td><td>NA</td><td>NA</td><td>This is normal situation with the reactor filled with fuel salt above &quot;BF3 Confidence&quot; level and with both wide-range counting channels in operation</td></tr><tr><td>2</td><td>T</td><td>F</td><td>T or F</td><td>T</td><td>F</td><td>T</td><td>T or F</td><td>F</td><td>NA</td><td>NA</td><td>Reactor situation same as 1 but only one wide-range counting channel in operation</td></tr><tr><td>3</td><td>F</td><td>T</td><td>T</td><td>T or F</td><td>T</td><td>F</td><td>T or F</td><td>F</td><td>NA</td><td>NA</td><td>Reactor situation same as 1 but only one wide-range counting channel in operation</td></tr><tr><td>4</td><td>T</td><td>T</td><td>T or F</td><td>T or F</td><td>F</td><td>F</td><td>T</td><td>F</td><td>NA</td><td>NA</td><td>Reactor is operating at power (flux) greater than 1 Mw and neither wide-range counting channel is operating; note that getting into &quot;Run&quot; mode can only be accomplished via condition 1 or 2</td></tr><tr><td>5</td><td>T</td><td>T</td><td>T or F</td><td>T or F</td><td>F</td><td>F</td><td>F</td><td>T</td><td>T</td><td>F</td><td>This situation obtains during early part of a &quot;Reactor Fill&quot; with fuel salt and before flux is sufficiently high to produce 2 cps in the wide-range counting channels</td></tr><tr><td>6</td><td>T</td><td>T</td><td>T or F</td><td>T or F</td><td>F</td><td>F</td><td>F</td><td>F</td><td>T</td><td>T</td><td>Reactor being filled from the flush salt tank (FFT); selection of FFT eliminates the requirements for &quot;Confidence&quot; in either the BF3 or the wide-range counting channels</td></tr></table>

"Reverse" is the insertion, in group, of all control rods. It takes place when the instruments indicate that system conditions have exceeded operating limits to the extent that rod insertion is the prudent action to be taken. The conditions or situations producing "Reverse" are listed in Table 2.6.1, and the circuitry which actuates the "Reverse" relay is depicted in Fig. 2.6.9.

# 2.6.3 The Automatic Rod Controller

The linear power channels (refer to Sect. 2.4) and automatic rod controller of the MSRE are shown in block diagram in Fig. 2.6.10. The purpose of this system is to provide automatic control of the reactor by the movement of one of the three shim rods in either of two controller modes (refer to Sect. 1.4). There is also a provision for disabling, through the servo "on-off" switch, the automatic controller in either mode to permit manual operation of the rod by the operator. The other two shim rods are always operated manually, as pointed out above.

One of the two automatic modes is called the flux mode and provides automatic control of neutron flux at a level selected by the operator when the reactor is in its "Start" mode of operation. The power range in which this mode is used extends from about 10 w to 1 Mw. The second mode is used to control the temperature of the fuel salt leaving the core and is called the temperature mode. This mode is used when the reactor is in the "Run" mode and is capable of adjusting the neutron flux to maintain the reactor outlet temperature at a set point established by the operator. In this mode the steady-state reactor power is a function only of the thermal load, which may be varied from about 1 to 10 Mw. The instantaneous power levels depend upon the thermal load and any changes in system temperatures required to achieve the desired outlet temperature. Switching between these two modes of controller operation is automatically accomplished when the reactor operating mode is changed. Reference 1, pages 104 to 108, is suggested for additional reading to augment this paragraph.

Significant features of the controller and its auxiliaries will be described below by referring to Fig. 2.6.10. The actual circuit diagram is shown in Fig. 2.6.11.

# 2.6.3.1 Basic Rod Control Circuit

The output element of the rod controller (Fig. 2.6.10) is a pair of pilot relays which operate as simple "on-off" switches to actuate the "Insert" and "Withdraw" relays in the rod drive motor circuit of control rod 1. These "Insert" and "Withdraw" relays must always be actuated to produce controlled rod movement regardless of whether the reactor is being operated manually or automatically. The pilot relay contacts are identified in Fig. 2.6.5 as contacts $R_{X}SS$ -NARC-A1 and A2 for "Withdraw" and "Insert" respectively. The power contactors which they control are relays K183 and K176, whose contacts are in the power leads to the servo motor in the control rod drive selected as "control rod 1." Amplifier 8 acts as a comparator with three inputs: (1) measured neutron flux, (2) flux demand, and (3) a signal proportional to rod speed. The model Q-2627 synchronous demodulator<sup>4</sup> is used to convert

the ac signal from the tachometer to a dc voltage with an amplitude proportional to rod speed and a polarity that depends upon the direction of rotation of the rod drive motor. This dc signal provides negative feedback to optimize the response of the servo mechanism.

When the controller is in the "flux" mode of operation, the operator chooses the flux at which the reactor is to operate and at which the controller output is zero by adjusting the demand potentiometer and the range of the picoammeter in the channel selected as the control input channel. This demand signal is identified as " $\Phi$ demand" in Fig. 2.6.10 and originates with the operator at the console. The " $\Phi$ demand" setting determines the voltage from the picoammeter that is required to bring the output of the comparator to zero (assuming no tachometer signal) and, with the range selection, determines the value of neutron flux required to produce that voltage. As indicated in Fig. 2.6.10, the range and the output voltage level of the picoammeters are recorded by the data logger. In addition, the range setting and level of the selected channel are recorded on a strip-chart power recorder located on the main control board. Although not shown in Fig. 2.6.10, there is an illuminated indicator on the main board immediately above the recorder, which displays the range of the selected channel.

In the "temperature control" mode the demand voltage is generated by the rod controller complex, and the range of the picoammeters is fixed. The way in which this is accomplished is described in the next section.

# 2.6.3.2 Temperature Control

The control of reactor outlet temperature is achieved by continuously computing a flux set point so that the temperature rise of the fuel salt through the core is just equal to the difference between the outlet temperature set point $\left[\mathrm{T}_{\mathrm{o}}\right]_{\mathrm{sp}}$ and the measured reactor inlet temperature $\mathrm{T}_{\mathrm{i}}$ . Figure 2.6.12 is a diagram of the array of Q-2605 operational amplifiers that accomplish this computation.

The system is best explained by neglecting, for the moment, amplifier 5 and its connection to amplifier 6. Considering the other two inputs to the summing amplifier 6, we note that, by proper choice of polarity, the algebraic sum of these two inputs is equal to the difference between the desired outlet temperature $\left[\mathbb{T}_{\mathrm{o}}\right]_{\mathrm{sp}}$ (selected by the operator through the model Q-2628 temperature servo demand drive unit) and the measured inlet temperature $\mathbf{T}_{\perp}$ . The output of amplifier 6 is (still neglecting the third input) proportional to the desired temperature rise through the core and, at constant flow, is a measure of the nuclear power required to achieve the desired outlet temperature. This output, through a sign-changing amplifier 7 and limiting circuits not included on Fig. 2.6.l2, becomes the flux demand or set-point signal to amplifier 8. Because of the varying conditions, both in the relationship of neutron flux to total heat generation and possible sensor errors, it is necessary to modify this set point if the measured outlet temperature is to be truly equal to the desired set-point value. The modification of the set point is accomplished by use of amplifier 5, the reset

amplifier, to generate a correction term. The reset amplifier is an integrator which continuously compares the measured flux $\phi$ , the measured core differential temperature $(T_{0} - T_{1})$ , and a correction term whose value is a function of the sum of the other three inputs and slowly alters the value of the correction term until the sum of the four inputs is zero, with the proper algebraic signs of the inputs considered. Since the correction term, the output of amplifier 5, is forced by this integration to be numerically equal to any discrepancy between measured flux and measured differential temperature, applying this same correction term with the proper polarity alters the flux demand as required to assure that the steady-state value of the measured outlet temperature is exactly equal to the set point. The response of the integrator is purposely adjusted to be considerably slower than the response of the other amplifiers on this computing system. Therefore, if either the reactor flux or inlet temperature, or both, experience a rapid change caused, for example, by a load transient or high rate of manual shimming, the error signal computation will initially proceed as if the integrator were not present. The controller will respond immediately to the transient, as explained in the first part of this paragraph.

Because of the rapid response of flux demand, and therefore flux, to a change in inlet temperature or outlet temperature set point, it is desirable that neither of these be permitted to change rapidly under normal operating conditions. Inlet temperature changes, assuming control of outlet temperature at a constant set point, are caused by load changes. These load changes are not normally permitted at a rate that exceeds the capability of the rod controller to hold the outlet temperature constant. The rate of change of outlet temperature set point is limited by using a motor-driven potentiometer to determine the reference voltage. This rate is necessarily very slow to prevent undesirable thermal gradients in the system when the controller is operating in the temperature mode, and, since it is desirable to match the outlet temperature set point to the actual outlet temperature prior to changing from manual to automatic control, a faster rate of altering the set point is available to the operator when the temperature is not being automatically controlled.

# 2.6.3.3 Flux Demand Limiting

Because components and devices do occasionally fail or malfunction and may thereby cause an unscheduled increase or decrease in flux demand in the temperature mode, a limiting circuit, block diagrammed in Figs. 2.6.10 and 2.6.11, has been provided which prevents the flux demand signal from departing appreciably outside its normal range. This feature is also useful to mitigate the consequences of an operator error such as turning on the controller when the outlet temperature set point is grossly different from the measured value.

In addition, a Q-2609 fast-trip comparator, shown in Fig. 2.6.10, is used to provide an interlock (see Sect. 2.5, Fig. 2.5.8) to prevent initiation of the Run mode of reactor operation while under automatic control unless the computed flux demand is less than about $1 \, \text{Mw}$ . Since the transfer from Start to Run must be made (by circuits not related to the automatic rod controller) at a power level of about $1 \, \text{Mw}$ , this comparator assures that no significant power excursion will occur.

# 2.6.4 Regulating Rod Limit Switch Assembly, Q-2586

It is good practice to limit the reactivity change that can be produced by the automatic controller to an amount equal to or slightly less than the effective delayed neutron fraction $\beta_{\mathrm{eff}}$ . Since each rod in the MSRE has a total full-stroke worth of approximately $2.2\%$ in $\Delta \mathbf{k} / \mathbf{k}$ (ref. 3, Sect. 4.3, Table 4.1, p. 58), the regulating rod limit switch assembly, hereinafter referred to as RRLSA, is provided to limit the stroke of No. 1 control rod to 6 in. when the automatic controller is in use.

Figure 2.6.13 is a simplified functional diagram of the RRLSA. This diagram does not depict the actual configuration of the system. The rod drive unit does not actually contain any intermediate movable limit switches as implied by the diagram. The actual short stroke limit switching takes place in the control room, and the mechanism which accomplishes this is shown in Figs. 2.6.14 to 2.6.17. Figure 2.6.18 is a mechanical diagram of the drive train, and Fig. 2.6.19 is a detailed block diagram of the assembly.

An ac servomechanism is used to position the limit switch cam when the automatic reactor controller is operating. This follows typical positioning servo practice when a synchro control transformer is used as the position error sensor. The servo loop (Figs. 2.6.18 and 2.6.19) consists of a size 15 control transformer whose output goes to an ac amplifier (Fig. 2.6.20), which drives the positioning servo motor. The control transformer is mechanically coupled to the positioning servo motor and is driven in a direction which reduces the error signal toward zero. When the rod controller is "on," the electromechanic clutch is engaged (the brake is off) and the cam is also connected, through speed changing gears and the differential gear set, to the ac servo motor. The shim-locating motor is also directly connected to the limit switch cam by gears and through the other input of the mechanical differential. Because the differential gear set is included in the drive train, both the ac servo motor and the shim-locating motor may be used independently and simultaneously to obtain cam motion. The net cam rotation is proportional to the algebraic sum of these two input rotations. The electromechanical clutch-brake in the output gear train between the shim-locating motor and the differential (see Figs. 2.6.18 and 2.6.19) is a design modification which does not appear in the photographs. It was added to eliminate the undesirable effects of cooldown of the shim-locating motor and of backlash in the motor's built-in gear reducer. Table 2.6.3 gives the rotational characteristics of the various components in the system when the reactor is in the automatically controlled mode and with the gear ratios in accordance with Fig. 2.6.18.

When the reactor is in the "Manual Control" mode, the control circuitry (Fig. 2.6.5) causes the electromechanical clutch-brake to become deenergized; the mechanical drive connection from the ac servo motor to the cam is broken and the brake is applied. Control circuit interlocks also prevent applying power to the shim-locating motor. Because of the very high built-in reduction gearing (2400 to 1) in this motor, it is not susceptible to being driven by torque applied to the output shaft. The brake prevents rotation of the other input to the differential. Therefore, both inputs to the differential are locked, and the limit switch cam is not free to rotate when torqued externally.

Table 2.6.3   

<table><tr><td colspan="2">Input Conditions</td><td colspan="4">RPM Outputs (Component Rotations in Q-2586, Regulating Rod Limit Switch Assembly)</td></tr><tr><td>Regulating Rod (Rod 1)</td><td>Limit Switch Span</td><td>Size 15 Control Transformer</td><td>AC Servo Motor</td><td>Limit Switch Cam and Size 31 Position Transmitter</td><td>Shim-Locating Motor</td></tr><tr><td>1.</td><td>Withdrawing at 0.5 in./sec</td><td>Stationary</td><td>+0.42</td><td>+5.0</td><td>+2.50</td></tr><tr><td>2.</td><td>Inserting at 0.5 in./sec</td><td>Stationary</td><td>-0.42</td><td>-5.0</td><td>-2.50</td></tr><tr><td>3.</td><td>Stationary</td><td>Withdrawing</td><td>Zero</td><td>Zero</td><td>-2.25</td></tr><tr><td>4.</td><td>Stationary</td><td>Inserting</td><td>Zero</td><td>Zero</td><td>+2.25</td></tr><tr><td>5.</td><td>Withdrawing at 0.5 in./sec</td><td>Withdrawing</td><td>+0.42</td><td>+5.0</td><td>+0.25</td></tr><tr><td>6.</td><td>Withdrawing at 0.5 in./sec</td><td>Inserting</td><td>+0.42</td><td>+5.0</td><td>+4.75</td></tr><tr><td>7.</td><td>Inserting at 0.5 in./sec</td><td>Withdrawing</td><td>-0.42</td><td>-5.0</td><td>-4.75</td></tr><tr><td>8.</td><td>Inserting at 0.5 in./sec</td><td>Inserting</td><td>-0.42</td><td>-5.0</td><td>-0.25</td></tr></table>

From Table 2.6.3 it is seen that the cam speed resulting from relocating the span of the limit switches with the shim-relocating motor is slightly less than the cam speed produced by control rod motion. With the gear ratios shown in Fig. 2.6.18, these speeds are 2.25 and 2.50 rpm respectively (see Table 2.6.3). The cam is cut for a maximum of $180^{\circ}$ rotation between limits, which is equivalent to 6 in. rod motion. The position of the limit switches is adjustable; hence, the effective span $\Delta y_{1}$ (Fig. 2.6.13) of the regulating rod may be adjusted within this maximum of 6 in. From Fig. 2.6.14, it can be seen that the gearing, clutch, motors, etc., are supported on movable mounts and bearing hangers. Therefore, it is simple and inexpensive to change the cam speeds and the span. A detailed description of the major components used in this unit is given in Sect. 2.6.5.

As noted above (see also Figs. 2.6.5 and 2.6.19), the net rotation of the limit switch cam is the resultant of two components: (1) the rotation produced by the balance motor and (2) the rotation of the shim-locating motor. When the reactor is in the servo control mode and if the operator is not relocating the position of the regulating rod span, the balance motor, driving through the clutch (the brake is disengaged) and the differential, rotates the limit switch cam through an angle that is directly proportional to the linear motion of the servo-controlled rod. Assume, for the sake of discussion, that the reactor is being operated in steady state and that no fuel is being added. Burnup and poisoning will cause slow withdrawal of rod 1, the servo-controlled rod, unless the reactor is manually shimmied by the other two rods. If no shimming takes place, the limit switch cam will continue to rotate clockwise (see Fig. 2.6.5), and, unless the shim-locating motor is actuated to produce counterclockwise cam rotation, the upper shim regulating rod limit switch will be opened, its associated relay K240 will drop out, and contact K240F will open. This will prevent the servo system "Withdraw" relay contact $\mathbb{R}_{\mathbb{X}}$ SS-NARC-Al from transmitting power to the rod withdraw relay K176. Note that the servo system is not turned off and that it continues to exert control in the "Rod Insert" direction; that is, if for any reason the servo calls for the insertion of negative reactivity with the servo rod at the upper limit of the regulating rod span, the rod insert requirement will be transmitted to relay K183, which causes the rod drive motor to insert the rod. This rod 1 insert relay, K183, cross-interlocks the rod withdraw relay K176 so that an "Insert" request from any source overrides all "Withdraw" requests. This cross interlock is included in all rod drive circuits. The operator must now shim the reactor. If he chooses to shim by using rod 1, the servo-controlled rod, he does so by means of the individual rod control switch, S19, used for manual operation. This closes contact S19A and energizes K175, the relay which causes the shim-locating motor to turn the cam counterclockwise. The limit switch closes, contact K240F closes, and the servo is in command of rod 1. The servo now withdraws rod 1 until the upper limit is again reached or until shimming requirements are met. The shim-relocating motor moves the cam at a slightly lower speed than does the balance motor, and the actual withdrawal of rod 1 in these circumstances is a series of start and stop movements until the span of the regulating rod is relocated. The alternate method of shimming is to withdraw either or both of the manually controlled rods 2 and 3 until the servo automatically returns rod 1 to a suitable place within the regulating rod span.

Should the servo controller malfunction and ask for a continuous out-of-control withdrawal of rod 1, the withdrawal will only persist until the upper regulating rod limit is reached. The "on-off" power amplifier relays in the servo controller do not exert direct control of the rod drive motors (see Fig. 2.6.5); instead they control the "Withdraw" and "Insert" relays K176 and K183, and a servo malfunction has to be accompanied by failure of other control-grade interlocks to become of consequence.

Should the regulating rod limit switch mechanism misoperate in conjunction with a servo controller malfunction so that the cam fails to rotate as the rod is being withdrawn by the servo, the control system interlocks may call for a "Reverse" (group insertion of all three rods) if the failure produces any of the situations listed in Table 2.6.1. "Reverse" by the control system is independent of the condition of the servo controller and may also be invoked should the operator inadvertently withdraw either shim rod so as to produce any of the listed conditions.

If one of the shim regulating rod limit switches remains actuated or if the cam fails to move off the mechanical stop, rod 1 is inhibited from further motion in one direction only. The operator can provide control with rods 2 and 3 and can switch over to manual control until the trouble is cleared.

A detailed step-by-step breakdown of the circuit and RRLSA responses to various situations is included in Sect. 2.6.6.

# 2.6.4.1 Range Switching

The range switching circuits of the flux channels are extensive because of the large number of operating conditions possible. Figure 2.6.21 shows these circuits, as well as those associated with the various reactor and rod controller modes.

The first two stages of the operator's range switches are used to connect the proper feedback resistors by energizing appropriate relays in the picoammeters. Contacts K204A and K204B (Fig. 2.6.21) are used to disconnect the range selector switches and to automatically connect a feedback resistor corresponding to a full-scale range of $15\mathrm{Mw}$ when a "range seal" condition exists. The "range seal" is described below.

Stages 3 and 4 of the range switch are used for proper switching of the inputs to the range indicator light assembly. This range indicator displays, in exponential form, the nominal full-scale range of the selected channel in watts. The range switching is by alternate steps of factors of 3 and $3 - 1 / 3$ . Stage 3 monitors the position of the range switches and the console channel selector switch and causes one of two multiplying factors (1.5 and 0.5) to be illuminated. In the event that K205 (another "range seal" relay) is energized, the 1.5 light is operated regardless of the position of either range switch. Stage 4 causes illumination of the proper exponent in the range indicator, thereby completing the identification of the range. The range seal condition causes a 7 to appear in the exponent position, indicating a range of $1.5 \times 10^{7}$ , or $15\mathrm{Mw}$ , when the range seal condition exists.

Stage 5 is a voltage divider used to provide range information to the data logger and range recorder. K208B contacts are used to switch the range recorder input to the selected channel range switch. Again K205 contacts disconnect the range selector switches and insert signals corresponding to the 15-Mw condition when the range seal is energized.

Stage 6 is a permissive switch used to enforce the 1.5-Mw range required to switch the operating mode of the reactor from Start to Run.

Stage 7 is used for the range seal function, which will now be described.

# 2.6.4.2 Range Seal

The transfer from Start to Run or Run to Start in reactor operation involves a number of distinct, but related, operations. To assure that all these are performed and that no severe transients are introduced as a result of such transfer, the range seal circuits have been developed.

The range seal, as the name may imply, is an electrical latching circuit which is energized whenever the reactor operating mode is switched by the operator from Start to Run. This transfer is restricted to power levels in the vicinity of 1 Mw. Energizing the range seal, represented in Fig. 2.6.21 by relays K203, K204, and K205, disconnects the range selector switches and causes the range of each picoammeter to become 15 Mw, as described above. Inasmuch as the range selector switches are now totally ineffective, it is reasonable to assume that they may be in any position during subsequent operations in the Run mode. It should be noted that the Run mode may be terminated automatically under certain conditions. Should this occur, the range seal circuits are used to automatically force the rod controller flux set point to about 1 Mw. The operator can then assume control of flux set point by putting both range selector switches in the 1.5-Mw position, at which time the flux set point becomes 1.5 Mw multiplied by the setting of the flux demand potentiometer.

The above features are shown in Fig. 2.6.21 at the bottom of the sheet. Relays K203 through K208 are operated in the following manner: A contact from the Run relay in the rod control system operates K206, called a run auxiliary relay. This relay in turn energizes K203, K204, and 205. If either of the range selector switches is turned from its 1.5-Mw position, the relays are sealed in their energized condition through S1 or S2 and K203A. Relay K207 is the relay which defines, for the controller and for the reset of the control system, the temperature mode of operation. Although it is clear that K204 should always be energized when K206 is energized, the interposition of K204C between K206 and K207 has a purpose. Inasmuch as the temperature control system cannot function properly unless the picoammeter range is 15 Mw, it was decided to initiate the temperature mode by the operation of the same relay, K204, that switches range. K208 is the relay which selects either channel 1 or channel 2 signals to be the input to the controller at the request of the operator.

At the bottom of Fig. 2.6.21 is also shown the switching circuit for the servo amplifier demand input. As described earlier, in the temperature mode the computed flux demand serves as a reference to be compared with the measured flux level. K207A, normally open, serves

this function. If K207 is deenergized, as it will be whenever the "run" relay is deenergized, the controller will be in the flux mode, and a flux demand voltage is supplied through a K203, or range seal, contact. If K203 is energized, the picoammeters are on their 15-Mw ranges, and the setting of the operator's demand potentiometer is in terms of percent of full scale and could represent as much as 15 Mw if used as a reference to the controller. Therefore, K203 is used to introduce a demand of 1 Mw, based on a 15-Mw range, whenever the range seal is energized and the run relay deenergized, as described earlier.

The temperature reset amplifier, described earlier, compares flux and temperatures to compute a correction term so that the reactor outlet temperature is equal to its set point in steady state. Since the flux signal into the controller depends upon the range of the picoammeter and the temperature signal does not, the reset mechanism would be saturated during most operations at low power. To provide a means for minimizing the error in the correction term at the time of transfer from Start to Run, a fictitious signal representing a 1-Mw flux level has been introduced whenever the range seal is deenergized. Since 1 Mw corresponds to a differential temperature of $5^{\circ}$ , the correction term will at most be $5^{\circ}$ , even if the power level is so low as to produce an unmeasurable differential temperature. As the reactor power approaches 1 Mw, prior to initiating the Run mode, the reset amplifier begins to operate properly. If the flux level is held actually at 1 Mw for a few minutes prior to transfer to the Run mode, there should be no appreciable change after transfer, since energizing K204 transfers the input to the reset amplifier from a fictitious 1-Mw signal to a real 1-Mw signal coming from the selected picoammeter.

# 2.6.5 Component Descriptions

# 2.6.5.1 Servo Motor

This is a two-phase, 60-hertz ac motor primarily designed to be the balancing pen drive motor in Minneapolis-Honeywell Company self-balancing potentiometer-type strip-chart recorders. It contains integral gear reduction such that it has a maximum no-load speed of $27\mathrm{rpm}$ . It is capable of operating at stalled torque continuously without damage. Its electrical characteristics provide a good match to the amplifier described below. The motor is designated by Minneapolis-Honeywell as their part No. 76750-3.

# 2.6.5.2 Amplifier

This is a general-purpose instrument servo amplifier designed to accept 60-hertz input signals in the millivolt range and to amplify them to a power level capable of driving the servo motor described above. This amplifier (Fig. 2.6.20) is manufactured by Minneapolis-Honeywell and modified in accordance with ORNL Instrumentation and Controls Division Drawing No. RC-2-10-12.

# 2.6.5.3 Clutch-Brake

The clutch-brake is manufactured by Autotronics, Inc., Florissant, Missouri, and is identified as part No. MB-34-2. [Refer to UCNC (ORNL) Requisition No. R-7674, April 4, 1963, and Purchase Order 63X47734.] Its performance characteristics are outlined below.

Operating voltage

Coil resistance, ±10%

Clutch torque, min

Brake torque, min

Response time to energize at 28 v dc

Maximum no-load torque (drag)

When energized  
When deenergized

Operating mode

24 to 28 v dc

138 ohms

80.0 oz-in.

100.0 oz-in.

0.020 sec

0.20 oz-in.

0.50 oz-in.

With coil energized the input gear flange is free to rotate and the output is braked to the housing

# 2.6.5.4 Shim-Locating Motor

The shim-locating motor is a synchronous capacitor type with integral gear reducer. It is manufactured by Bodine Electric Company, 2504 West Bradley Place, Chicago, Illinois, and is identified by catalog No. B8122E-1200C, frame KYCC22RC with K-45 capacitor. (Refer to UCNC Purchase Order 63X-50673, June 10, 1963.) Its performance characteristics are outlined below.

Input

115-v, 60-hertz, single-phase

Output speed

1.5 rpm

Output torque

105 oz-in.

Capacitor

0.35 μf

# 2.6.5.5 Mechanical Differential

The mechanical differential is a bevel gear type supplied by Reeves Instrument Corporation, Roosevelt Field, Garden City, New York.

# 2.6.5.6 Size 15 Control Transformer

This transformer (U.S. Government type 15CT6b, Mil. Spec. S-20708) is manufactured by the Bendix Corporation, Montrose Division, South Montrose, Pennsylvania, and is identified by Bendix Catalog No. AY1501B-11-B2, Dwg.1501B-0, or equal. (Refer to UCNC Purchase Order 63X-47764, April 29, 1963.) Specifications are given below.

<table><tr><td>Voltage, primary/secondary</td><td>90/57.3, 60 hertz</td></tr><tr><td>Current, max (typical)</td><td>0.011 amp</td></tr><tr><td>Power, primary (typical)</td><td>0.13 w</td></tr><tr><td>Total voltage at null</td><td>90 mv</td></tr><tr><td>Fundamental voltage at null</td><td>60 mv</td></tr><tr><td>Electrical accuracy</td><td>6 min</td></tr><tr><td>Phase shift</td><td>20° lead</td></tr></table>

# 2.6.5.7 Size 31 Torque Transmitter

The size 31 torque transmitter (U.S. Government type 31TX6b, Mil. Spec. S-20709) is manufactured by the Bendix Corporation, Montrose Division, Montrose, Pennsylvania, and is identified by Bendix catalog No. AY-3101B-12-E2, Bendix Dwg. 301OB-0, or equal. (Refer to UCNC Purchase Order 63X-47764, April 29, 1963.) Specifications are given below.

<table><tr><td>Voltage, primary/secondary</td><td>115/90, 60 hertz</td></tr><tr><td>Current, primary (typical)</td><td>0.395 amp</td></tr><tr><td>Power, primary (typical)</td><td>4.75 w</td></tr><tr><td>Electrical accuracy</td><td>10 min</td></tr><tr><td>Max total signal at null</td><td>125 mv</td></tr><tr><td>Max total signal, funda-mental at null</td><td>35 mv</td></tr><tr><td>Phase shift</td><td>6.5° lead</td></tr><tr><td>Torque gradient</td><td>0.40 oz-in./deg</td></tr></table>

2.6.6 Operational Situations Involving the Regulating Rod Limit Switch and the Regulating Rod Servo (Refer to Figs. 2.6.5, 2.6.7, and 2.6.9)

I. Servo withdraws rod to upper limit of the RRLSA

A. This moves cam clockwise to upper limit switch; this actuates (deenergizes) K240.   
B. The active contact chain during "Withdraw," in servo, is:

1. $\mathrm{R}_{\mathbf{x}}\mathrm{SS}\text{-NARC} \rightarrow \mathrm{Al} \rightarrow \mathrm{K24OF} \rightarrow \mathrm{KAl7OD} \rightarrow \mathrm{K228A} \rightarrow \mathrm{K229A} \rightarrow \mathrm{Kl83C} \rightarrow \mathrm{relay}$ K176.   
2. K24OF opens and prevents further withdrawal by the servo.

II. Regulating rod at upper limit of the RRLSA; operator acts to let servo continue rod withdrawal

A. This requires that the circuit to relay K176 be restored to energize relay K240 (see A above).   
B. This is permitted if the RRLSA is withdrawn so that its upper limit switch is not actuated. This is accomplished by manual operation of S19A to energize relay K175. The contact chain in circuit 175 is: S19A $\rightarrow$ S2OB $\rightarrow$ S21B $\rightarrow$ K170H $\rightarrow$ K241A $\rightarrow$ relay 175 energized.

C. When relay 175 is energized, the RRLSA cam moves off the upper limit and these actions follow:

1. K240F closes.   
2. Kl76 is energized since, by hypothesis, the servo error signal requesting withdraw rod 1 still exists and servo relay contact R SS-NARC-Al is still closed. The RRLSA cam is now receiving motion from two sources:

a) Clockwise rotation produced by the actual withdrawal of rod 1, which rotates the position synchro in the RRLSA.   
b) Counterclockwise rotation produced by the operator's closure of the manual shim switch (S19), which operates the shim-locating motor in the RRLSA.   
c) Since the cam speed produced by withdrawing rod 1 is slightly faster than the speed in the opposite direction produced by the shim-locating motor, the net rotation of the cam tends to be clockwise. Therefore, the motion of rod 1 will tend to keep the cam at its upper limit, while at the same time the operator is continuing to reverse the cam. Rod 1 will move up in steps as long as the servo requests withdrawal.   
d) When the servo error signal becomes zero:

1) $R_{\nu}SS$ -NARC-Al opens and relay K176 is deenergized.   
2) If the operator continues to request withdrawal of rod 1 by actuating S19A and energizing relay K175, the cam continues to move counterclockwise. Presumably the operator will stop the cam so that it is midway between limits. If the cam reaches the lower limit and energizes relay K241, rod 1 is prevented from responding to a servo error signal calling for rod insertion.

III. Servo inserts regulating rod to lower limit of the RRLSA

Control system response is same as in I, but in opposite directions.

IV. Regulating rod at lower limit of the RRLSA; operator acts to let servo continue rod insertion

Control system response is same as in II, but in opposite directions.

V. Manual insert of rod 1 (regulating rod) or manual or automatic reverse of all rods is requested

A. Any one of contacts S22B, S19D, or K186F is closed.   
B. Assume that rod 1 is between limits of the RRLSA; then the pertinent contact chain becomes: (S22B, S19D, or K186F) → KA170E → K240A → relay K182.   
C. The shim-locating motor rotates cam in the "Insert" direction. Note: Rod 1 does not move during this step as the cam approaches the upper limit switch in the RRLSA.   
D. The upper limit switch is actuated by the cam and relay K240 is deenergized.

1. Contact K240A opens and stops the shim-locating motor.   
2. Contact K24OC closes and the relevant contact chain becomes: (S22B, S19D, or K186F) $\rightarrow$ KA170E $\rightarrow$ KA24OC $\rightarrow$ K230A $\rightarrow$ K231A $\rightarrow$ relay K183.

E. Relay contact K183A closes, causing the drive motor for rod 1 to insert the rod. The cam will be rotated opposite in direc-

tion to its original rotation per VC above, and this action will continue until it is backed away from the upper limit switch in the RRLSA. Relay K240 is energized, and the cycle, starting with VB above, is repeated. The action is similar to that described above in IIB.

F. Once rod 1 has reached either of the limit switches in the RRLSA, its speed is limited by the speed with which the position of the RRLSA can be changed. This is approximately $10\%$ less than that of rod 1.

G. If, during a request for "insert" per VA above, the servo also requests rod l insert, the resulting action is to immediately insert rod l until the lower cam limit switch in RRLSA is reached. During this time the rotational speed of the cam will be the absolute difference of two speeds; namely:

1. The speed, counterclockwise, of rod 1 reproduced by the rod position synchro which drives the cam.   
2. The speed, clockwise, of the RRLSA produced by the shim-locating motor.

The shim-locating motor moves the cam at a slightly lower rate (approximately $10\%$ less) than the position-transmitting synchro. The net speed is the algebraic sum (absolute difference) of the two, thus (refer also to Sect. 2.6.4 and Table 2.6.3):

Cam speed = + (speed produced by shim-locating motor)

$$
\begin{array}{l} - \text {(s p e e d p r o d u c e d b y r o d l m o t i o n)} \\ = + 0. 9 (\text {r o d s p e e d}) - (\text {r o d s p e e d}) \\ = - 0. 1 \text {r o d s p e e d .} \\ \end{array}
$$

Therefore, in these circumstances, the cam will be turning, slowly in a counterclockwise direction until the lower limit switch in the RRLSA is actuated. As long as the servo is calling for rod 1 to insert, the rod will be nudging the lower limit switch in the same manner as described at the upper limit (see IIB).

H. If, during a reverse, the servo is requesting withdrawal of rod 1, the reverse relay contact K186A (see Fig. 2.6.9) is open and prevents energizing relays K174, K175, and K176. This, in turn, prevents group withdraw of all rods, withdraw RRISA, and individual withdraw of rod 1.

J. If the operator requests "insert rod l" while the servo is requesting "withdraw," the result is, in terms of pertinent contacts:

1. $\mathbb{R}_{\mathbf{x}}\mathbb{S}\mathbb{S}$ -NARC-Al $\rightarrow$ K24OF $\rightarrow$ KA17OD $\rightarrow$ D228A $\rightarrow$ K229A $\rightarrow$ K183C $\rightarrow$ energize relay K176 $\rightarrow$ (withdraw, rod 1). Rod 1 withdraws, and the position transmitter rotates the cam clockwise toward the upper limit of the RRLSA.   
2. S19D → KAl70E → K240A → energize relay K182. The shim-locating motor rotates the cam clockwise toward the upper limit RRLS.   
3. The net result of 1 and 2 above is to make the RRLSA cam approach its upper limit switch at a rate nearly twice as fast as normal; that is, net speed, the absolute sum of the

two speed components, instead of the difference as described in VG.

4. When the upper limit switch of the RRLSA is actuated, the closed circuit, per 2 above, is broken because contacts K24OA, K24OF, and KA24OC change their aspect. This energizes relay K183 and deenergizes K176, thus:

a) S19D → KAl7OE → KA24OC → K230A → K231A → energize K183. This calls for "insert rod 1." Note that K176 becomes deenergized for either of two reasons: 1) Energizing K183 opens K183C (see J1 above) 2) K24OF opens.   
In addition, contacts K183A and K183D appear in both "insert" and "withdraw" power leads to the motor in rod drive 1, so that "insert" overrides "withdraw." Note that, when the servo is controlling, this overriding interlock is not in effect until the upper limit switch in the RRLSA has been actuated.   
b) Rod 1 is inserted, and the RRLSA cam is rotated counterclockwise and away from the upper limit of the RRLSA.   
c) Insertion of rod 1 continues momentarily until the RRLSA cam leaves its upper limit switch.   
1) KA240C opens.   
2) Relay K183 is deenergized.   
3) Rod 1 stops inserting.   
4) K240A closes and the shim-locating motor drives the cam clockwise toward the RRLSA upper limit.   
5) K24OF closes, K183 closes, and relay K176 is energized, causing rod 1 to withdraw.   
6) The RRLSA cam is also now being driven toward its upper limit by the position transmitter.   
d) This condition (4, 5, and 6 above) is the same as that originally postulated, assuming that the servo is still requesting rod 1 withdraw and the operator is manually calling for "insert."

![](images/9f65dd878449cd5537061216f038c3dea3ef50f5d601fb200f3ff936845f40ea.jpg)  
Fig. 2.6.1. MSRE Rod Control Block Diagram.

120794RH 509D.2

![](images/55ef4fe0f2b69067b9017cc550b273997142c28b1ccc223400bd13db5ae6083b.jpg)  
120794RH 50ID-5   
Fig. 2.6.2. MSRE Rod Control Circuits.

![](images/ea62879cca717b249670914a905670cfe2454f48818dd4c6418cbe0e34457eaa.jpg)  
Fig. 2.6.3. MSRE Control Rod Block Diagram.

I20794RH 510D3

![](images/8d31de9080fbb6be3103b9d66846b54ea747ff426304d6339f2b599d863e1483.jpg)  
120794RH 502D 4   
Fig. 2.6.4. MSRE Rod Control Circuits.

![](images/823bc4923e22ee0493c85093820ab122094230a50debe676b2881d41e4722050.jpg)  
246   
Fig. 2.6.5. MSRE Shim Regulating Rod Control Circuits.

![](images/974779afa2db8a48d475c4147be94753d86ccc5f7bae148cc4ec8a6457e6a75d.jpg)

![](images/cdbd9e1bedbe8373467ac39120ffa4c09415fafe5b5fb241a6fcabbf2080c63c.jpg)

![](images/9a279184858c373c801d19e209bc1194295d6957294800602412391b221040a4.jpg)

![](images/5710af5cd4cf32392ac9b37b450b5f3c5798932410f7f8fe1fc5162a8b9ba52a.jpg)  
Fig. 2.6.6. Circuit Diagram for Regulating Rod Dynamic Brake.

![](images/0b28f91e90fc1a9a4bd2f8bbd410e7554197a09a2ad4889f6b0579a655d22aa2.jpg)  
Fig. 2.6.7. MSRE Control Rods 2 and 3 Circuits.

<table><tr><td colspan="5">INDIVIDUAL SHIM ROD ACTUATOR SWITCHES NO. S19, S20 AND S21. MANUAL, ON CONSOLE</td></tr><tr><td rowspan="2">CONTACT NUMBERS</td><td colspan="3">POSITION</td><td rowspan="2"></td></tr><tr><td>INSERT</td><td>&quot;OFF&quot;</td><td>WITHDRAW</td></tr><tr><td>S19A, S20A, S21A</td><td>O</td><td>O</td><td>X</td><td></td></tr><tr><td>S19B, S20B, S21B</td><td>O</td><td>X</td><td>O</td><td></td></tr><tr><td>S19C, S20C, S21C</td><td>O</td><td>X</td><td>O</td><td></td></tr><tr><td>S19D, S20D, S21D</td><td>X</td><td>O</td><td>O</td><td></td></tr></table>

<table><tr><td colspan="5">GROUP SHIM ROD ACTUATOR SWITCH S22</td></tr><tr><td rowspan="2">CONTACT NO.</td><td colspan="3">POSITION</td><td rowspan="2">CIRCUIT NO.</td></tr><tr><td>REVERSE(INSERT)</td><td>HOLD</td><td>WITHDRAW</td></tr><tr><td>S 22 A</td><td>0</td><td>0</td><td>X</td><td></td></tr><tr><td>S 22 B</td><td>X</td><td>0</td><td>0</td><td></td></tr><tr><td>S 22 C</td><td>X</td><td>0</td><td>0</td><td></td></tr><tr><td>S 22 D</td><td>X</td><td>0</td><td>0</td><td></td></tr></table>

ORNL-DWG 66-9074

![](images/dfd6cdab2036e6dcfa1332c8f3142c86a115f705cc60447fa2f1ba6dc7536ac0.jpg)

![](images/f19612e9450dd2441ec7e601cabf244d0775457e65c5b4cc378890da9a639d99.jpg)  
CONFIDENCE CIRCUITS   
Fig. 2.6.8. MSRE Control System Confidence Circuits.

![](images/f3e215fa70e0a16da66296bd70a6d61bb1cc2b4b560b8cb9ae48cf38f2804656.jpg)  
ORNL-DWG 68-9216

![](images/e8f827abe6b4bb1e276a2790dc9f2e9fc51766b8c5e16c8ae1bd22786a52e416.jpg)  
5   
Fig. 2.6.9. MSRE Control Rod "Reverse" Circuits.

C

![](images/f500905f70c06cf14e765fa14c4b76b33d88bb8aa27b6e634e26bf89a2ac59ec.jpg)  
Fig. 2.6.10. Linear Power Channels and Automatic Rod Controller.

C

![](images/8fecc2941defd6b398471da331d262674e4908f7db33113eee118770aacebb75.jpg)  
Fig. 2.6.11. MSRE Automatic Rod Controller Circuit Diagram.

![](images/ea6ed112b1015074b32ddf00a36c2cfc4109103e10fb4e713b82926a81dc8d37.jpg)  
Fig. 2.6.12. Diagram of Regulating Rod Servo Controller.

![](images/25eac910e0d5da9d0c0b74202b8a400f607275a0fb5fabfd66670d80d6897293.jpg)  
Fig. 2.6.13. Regulating Rod Limit Switching - Operational Diagram.

![](images/c91a476003795ef83f0f8bcdb182daffe2ad707a17fc76b4a9398529c40c4755.jpg)  
Fig. 2.6.14. Regulating Rod Limit Switch Assembly - Top View.

![](images/d75f46ce21831eced2343d1887824cc28a7362a77eb9ec752691c00ca63d4548.jpg)  
Fig. 2.6.15. Regulating Rod Limit Switch Assembly - Side View.

![](images/643c3b2bb6a737affc181eec2b1b53119225a135dfabf9c57742d8ccf7f4596f.jpg)  
Fig. 2.6.16. Regulating Rod Limit Switch Assembly - End View.

PHOTO 62305A

![](images/2b96ea1604507b21eacdb328200f971f68ccd7c1d088d7c002a6a6ee5d138858.jpg)  
Fig. 2.6.17. Regulating Rod Limit Switch Assembly - Underside View.

ORNL-DWG66-4105R

![](images/ca45e97abec5f179b82c72fcb79092f3fda9fdea5f10b9f19de007de84072b1e.jpg)  
Fig. 2.6.18. MSRE Regulating Rod Limit Switch Assembly, Drive Train Diagram.

![](images/ef468910af42cd170c79b6189e37905b29640d0ad5c724ee3b39a82cc7885c06.jpg)  
Fig. 2.6.19. MSRE Regulating Rod Limit Switch Assembly, Block Diagram.

![](images/5be0e7ce9554fe02d0816720c258ce2ce7bdc60c36451123f11f59833b33f2d5.jpg)

Fig. 2.6.20. Modified Brown Amplifier (Unused Wiring not Shown).   
![](images/b4eeacf82fe6b802f235e9bc234b55845c478b48f4397b8bf2e2b9bb2e9cc4d8.jpg)  
NOTE THAT FIRST STAGE IS BY-PASSED.

![](images/dd7f52689477edec805b53751874c3c2515edbab1805fff3675e1cd1db7b7658.jpg)  
Fig. 2.6.21. Automatic Rod Control | r Range Switching and Range Seal Circuits.

# 2.7 CONTROL RODS AND ROD DRIVES

# 2.7.1 General Arrangement

The control rod drive unit and its housing are shown in Figs. 2.7.1 to 2.7.3. Figure 2.7.4 is a simplified electromechanical diagram which shows the functional location of the essential elements which comprise the drive train. The gearing and the clutches are inside a cast-aluminum gear box. The drive motor, the two position-transmitting synchros, and the position-indicating potentiometer are mounted on and outside the gear box with their shafts carrying their drive gears projecting inside the box so as to mesh with the appropriate gears in the drive train (Fig. 2.7.2).

The gear box subassembly, which includes the position transmitters and the clutches, is located at the upper end of the drive unit in an effort to keep the radiation-sensitive components (electrical insulation and lubricant) as far from the reactor as feasible. Figure 2.7.5 is a diagram of the gear train and the clutches. The worm and gear set is of somewhat unorthodox design, if compared with typical standard practice for this type of gearing (see Sect. 2.7.9.10). The other gears are conventional.

The rod is scrambled by interrupting current to the electromechanical clutch. During scram, the driven element of the overrunning clutch is free to rotate and, except for a small amount of friction and inertia, does not interfere with rotation of the output sprocket in the "rod insert" direction.

The electromechanical clutch and the overrunning clutch provide parallel power transmission paths between the motor and the output sprocket. The arrangement is such that the overrunning clutch transmits motor torque in the "rod insert" direction only and can be used to apply motor torque to the drive sprocket in the event that a rod sticks or binds following a scream. If external torque is applied to the output sprocket in the "rod withdraw" direction of rotation, the overrunning clutch provides a solid mechanical coupling between the drive sprocket and the input side of the drive train. The worm and gear set are inherently self-locking with respect to torque in either direction originating at the output sprocket. This combination of overrunning clutch and worm and gear set prevents rod withdrawals by upward forces applied to the control rod or by a torque applied to the drive sprocket.

The drive unit housing, with the drive unit secured thereto, is attached to the control rod thimble by means of a flange welded to the bottom of the housing. Figure 2.7.6 is a photograph of the rod thimble, which extends into the core vessel, and shows the mating flange. The radial slots in the rim of the thimble flange mate with pins in the housing flange and are required to ease the problem of orientation during remote maintenance operations. The milled slot in the face of the flange accepts the T-shaped flange fitting, which is cap-screwed to the rod drive tow block (see Figs. 2.7.19, 2.7.20 and 2.7.14). It prevents the rod from twisting when it is being detached from the tow block during remote maintenance. Figure 2.7.7 is a photograph of the subassembly formed by the thimbles and the graphite sampler taken before installation

on the reactor vessel. This illustration also affords a good view of the lower, stationary halves of typical thermocouple disconnects designed for remote handling. Figure 2.7.8 shows this subassembly mounted on the reactor vessel; Fig. 2.7.9 is a line drawing of the control rod drives and rod thimbles on the reactor vessel. The rod drives are offset radially to make room for the graphite sampler tube (not shown on this sketch), which occupies space on the vertical center line through the core vessel. Figure 2.7.10 shows the top of the control rod drives installed on the reactor. This picture was taken looking down through the access hole in the top of the secondary containment cell. The electrical jumper cables and cooling air hoses with their disconnects are visible in this picture. Electrical interconnections between drive units and junction boxes on the wall of the reactor cell are made with flexible jumper cables. Each drive unit has its individual cable assembly, which is designed for remote handling. The wires making up the cable are designed for high temperatures and use radiation-resistant insulation (see Sect. 2.7.9). The wires are tightly bundled by means of heat-shrinkable plastic tubing. This wire bundle is sheathed in a loose-fitting, spirally wound stainless steel hose to give mechanical protection. The fittings at each end use ceramic pin and socket inserts of standard pattern in shells and receptacles which have been designed to meet remote handling requirements. The interconnection cabling and junction boxes are described in Sect. 2.1.

# 2.7.2 Position Indication

Continuous indication of rod position is provided by two synchro torque transmitter-receiver pairs, one "fine" and one "coarse." The location of the transmitters on the gear box is shown in Fig. 2.7.2.

The "coarse" rod position transmitter rotates $5^{\circ}$ per inch of rod travel. Since this is less than one full turn for the maximum rod travel of 60 in., the indication is unambiguous. The "coarse" position receivers, one for each rod, are located on the main control board. The "coarse" transmitter also supplies the ac error signal to the synchro control transformer in the torque amplifying rod position follower. This unit (see Fig. 2.6.20) drives the potentiometer which provides the rod position input signal to the logger. On rod 1, the same ac signal is used as the input to the Honeywell servo amplifier in the Instrumentation and Controls drawing Q-2586 shim regulating rod limit switch assembly. This device is discussed in Sect. 2.6. The "fine" transmitter rotates $60^{\circ}$ per inch of rod travel and is expected to be capable of resolving incremental sprocket chain motions to within $\pm 0.050$ in.

Since both the "coarse" and "fine" synchro transmitters are geared to the sprocket shaft, they indicate sprocket shaft rotation and do not take into account changes in rod length caused by thermal expansion, stretching, etc. In order to locate the control rod as accurately as possible with respect to the reactor core, a single-point, pneumatically operated, position device is employed. The position sensor consists of an air nozzle at the bottom of the control rod which carries the flow of rod cooling air from the hollow inside of the rod to the thimble. When the rod is at the bottom of its normal stroke the nozzle is op-

pose it a flow restrictor built into the thimble. The increase in pressure drop caused by the restriction is the position indication. The nozzle and restrictor are shown in Fig. 2.7.11, and the schematic diagram of the pressure measuring instrumentation is shown in Fig. 2.7.12. This device is manually operated and is used to check the zero readings of the position-indicating synchros and, inferentially, provides information on how temperatures and stresses produce small changes in the relative position of the rod with respect to the thimble.

# 2.7.3 Shock Absorber

The shock absorber is a development of the Yard Division of Royal Industries, who built the drive units. It uses the general principle of a typical hydraulic shock absorber but differs in that the working "fluid" consists of 3/32-in.-diam steel balls. Figure 2.7.13 is a vertical cross-section view of the shock absorber installed in the drive unit. Referring to this figure, the piston is the knob, which is an integral part of the plunger. The latter is a tubular rod which is threaded into the carriage and which connects the control rod tow block to the carriage. The closed cylinder, partially filled with steel balls, travels with the carriage and is positioned relative to the carriage (and the plunger) by the buffer return spring. At the end of a scram the bottom face of the cylinder strikes the stationary steel blocks which are bolted to the housing flange. The plunger continues to move downward and is decelerated by the forces developed by the springs and by the flow of the steel balls around the knob on the plunger.

Shock-absorbing characteristics are adjusted by changing either the spring constants or the preloading of the buffer return and ball reset springs, or both, by changing the quantity and size of the steel balls, and by sizing the knob on the plunger. A stroke of from 2.75 to 4.00 in. is considered satisfactory. During tests<sup>1</sup> of the prototype, the shock absorber performed consistently and provided a stroke of $3.4 \pm 0.2$ in. following rod scrams from a height of 5l in. This produced an average deceleration of $6.2\ g$ .

# 2.7.4 Cooling Air Flow and Temperature Monitoring

The drive is provided with two separate flows of cooling air. The first is conducted into the thimble by means of a thin-walled tube that projects into the stainless steel hose which supports the poison elements of the rod. This flow of air exits through the nozzle at the lower end of the rod (see Fig. 2.7.11) and returns up through the annulus formed by the outside of the rod and the inside of the thimble. The second air stream is admitted at the top of the rod drive housing and flows downward within the housing. This air flow is counter to the first flow and prevents heated air from the thimble from rising into the drive unit. Both streams are discharged into the reactor cell at the upper end of the thimble.

Two bimetallic thermostatic switches are mounted on the support column of the drive unit approximately 8 in. above the lower sprocket.

Their contacts are in series for redundancy and are set to open at $200^{\circ}\mathrm{F}$ . Switch actuation is annunciated in the control room; no control action results.

These switches (Fig. 2.7.14) were added to the drive units after they had seen service during the initial critical tests and low-power runs of the reactor; hence they do not appear in the photographs of the drive unit assembly. Their purpose is to signal the control room that the drive unit is in danger of being subjected to damaging temperatures, a condition which could result from loss of air flow into the housing, excessive thimble temperatures, stoppage of the exhaust line, or excessively high ambient cell atmosphere temperature. The switches are described in Sect. 2.7.9.

A second, or backup, method of checking temperatures within the rod drive is shown in Fig. 2.7.15. This method uses the temperature coefficient of resistance of the cooling fan motor windings (part of the rod drive motor assembly) to measure the temperature within the rod drive unit housings. The fan motor field windings typically have room-temperature resistances of 520 ohms. Copper has a temperature coefficient of resistance of $2.18 \times 10^{-3}$ ohm/ohm- $^{\circ}$ F over the temperature range of interest. The slightly more than $10\%$ change in resistance for a $50^{\circ}$ F change in winding temperature provides more than ample sensitivity. Periodic measurements made during reactor operation showed that the dc resistance of these windings gave a good linear correlation in following in-cell air temperature. The duty cycle of the rod drive motors is exceedingly light; for example, the servo motor was "on" for a total of 51 sec in a 2-1/2-hr period with the reactor at an intermediate power level and in servo control of the outlet temperatures. Manual shimming is an infrequent operation and requires only a few seconds to accomplish. In addition, the servo motors operate at a fraction of their rated capacity. The light load and duty cycle permit shutting off the fan long enough to measure the dc resistance of one of the fan motor field windings. It is likely that the motor cooling fans are not needed in the MSRE. As can be seen from Fig. 2.7.15, the fan motor being checked for temperature is turned off temporarily by energizing the selector-switched relays, and the temperature is indicated on the meter in the output circuit of the regulated voltage supply. The diodes across the motor windings prevent insulation damage by preventing high-voltage switching transients caused by opening the highly inductive field winding.

# 2.7.5 Limit Switches

Limit switches and their actuators are a frequent problem area in devices of this type. The MSRE rod drive unit was no exception; during the first critical tests, the actuator became stuck at the lower limit. This was caused by excessive wear and galling of soft steel sliding bearing surfaces in the switch actuator guide. The design was altered by providing hardened-steel, spring-loaded, floating bearing pads to replace the galled bearing surfaces. The revised design is shown in Fig. 2.7.16. The slide assembly is lubricated with Neolube (see Sect. 2.7.3.8). Figures 2.7.17 and 2.7.18 are photographs of the limit switches and actuators installed on the drive unit.

# 2.7.6 Control Rods

Figure 2.7.19 is a photograph of the upper end of a display model of the MSRE control rod with the poison elements<sup>2</sup> removed. The poison elements<sup>2</sup> are shown in Fig. 2.7.11. There are three control rods, which are identical in construction, each weighing approximately 11.2 lb. The rod lengths are slightly different because of the required offset of the control rod thimbles. The rod lengths are: rod 1, 11 ft 9-7/16 in.; rod 2, 11 ft 9 in.; and rod 3, 11 ft 7-3/16 in.

The control rod is attached to the control rod drive by means of a two-bolt (3/8 in. × 16 thread) flange or tow block made of 304 stainless steel. The drive mechanism contains a matching flange containing the captive bolts. The assembly is designed to permit attachment of the control rod drive flange to the control rod flange through an access hatch in the drive unit case using a remote, manually operated extension wrench.

The upper hose consists of a length ( $\sim$ 6-1/2 ft) of 0.850-in.-OD by 1/2 in.-ID annularly corrugated, 321 stainless steel, flexible metal hose with a single exterior layer of wire braid. The corrugated hose provides a leaktight passage for the low-pressure ( $\sim$ 8 psig, $\sim$ 5 scfm) rod cooling air to reach the poison elements. The wire mesh serves the purpose of protecting the hose from abrasion, minimizes stretching of the hose, and acts as an emergency retainer in the event of hose failure. The 1/2-in. inside diameter of the hose permits passage of the 7/16-in.-OD stationary cooling air tube which is attached to the upper drive mechanism. When the rod is in motion, the corrugated hose and tow block move up and down over the air tube.

The weld adapter serves to align the two types of metal hose used in the rod construction. It also serves as the upper anchor point for a 1/8-in.-OD INOR-8 retaining rod, which is located inside the lower hose.

The lower hose is 5 ft 2 in. long, Inconel 600, fully interlocked, unpacked, strip-wound flexible metal hose 47/64 in. OD and 5/8 in. ID. The 38 Inconel-clad poison elements, detailed in Fig. 2.7.11, are beaded over the strip-wound hose, as shown in Fig. 2.7.20.

The lower end of the strip-wound hose is welded to the air exhaust nozzle, which acts as the element retainer and lower anchor point for the 1/8-in. retaining rod. The rod supports a portion of the weight of the poison elements, contains the stretching of the strip-wound hose, and acts as safety retainer in the event of hose failure.

During the two years of rod testing, there have been three incidents of rod failure. Two failures were due to misoperation of the equipment, and one incident was due to misalignment of 7/16-in.-OD air tube in the corrugated upper hose. The upper hose was worn by the air tube rubbing the inside surface of the hose so that when the rod was

released in scorn, the hose broke away from the tow block when it hit the mechanical stop in the shock absorber mechanism.

A bronze bushing was installed in the tow block to assure alignment of the air tube and hose. Subsequent examination revealed only minor wear at this point.

# 2.7.7 Rod Drop Timer

Routine operation of the $\mathbf{MSRE}^3$ requires that the drop time for each rod be checked each time before filling the reactor with fuel salt. Figure 2.7.21 diagrams the timing circuitry used to measure drop times. The timer consists of a continuously running synchronous motor connected, via gearing, to a fast-acting electromechanical clutch-brake whose output shaft drives an indicating pointer. The elapsed time indicated by the pointer, therefore, is the time during which the clutch is engaged. The drop time is easily measured. The rod is scrambled using the manual scram switch on the console. This closes relay contact K29A, and the timer clutch is engaged and remains engaged until a lower rod limit switch is actuated by the rod at the end of the drop.

# 2.7.8 Performance Characteristics

This list of performance characteristics is derived from prototype test data:

1. Rod speed with either 25- or 10-w motor running continuously at rated voltage (115 v ac, 60 cps), 0.53 in./sec. Note: The change in speed in going from "Up" to "Down" is approximately $1\%$ .   
2. Rod speed with the 25-w motor in "inching" mode (1/2 sec "On," 1/2 sec "Off," etc.), motor at rated voltage, 0.22 in./sec.   
3. Motor speed as a function of applied voltage, see Fig. 2.7.22. Note: Rod speed (in./sec) = 1.53 × 10⁻⁴ × rpm of motor.

4. Scram performance

a) Elapsed time to drop 51 in., 0.80 sec (see Fig. 2.7.23).   
b) Average acceleration during scram for a 5l-in. drop, 13.2 ft/sec² = 0.4lg.   
c) Clutch release time, inferred from a curve of the square root of distance vs elapsed time (see Fig. 2.7.24), 0.012 sec.   
d) Figure 2.7.25 compares actual and required reactivity insertions during scram. These curves are calculated from curves "A" and "B" on Fig. 2.7.23 and the calculated percent of total rod worth vs distance curve, Fig. 1.19, p 59, ref. 2, and a total worth of $4.1\% \Delta k / k$ . This value of total worth approximates the total reactivity inserted by scrambling any two of the three rods. The initial height prior to scram was taken as 51 in.

# 2.7.9 Component Descriptions and Specifications

# 2.7.9.1 Rod Drive Motor Assembly

# General Description

The drive motor is a 115-v ac, 60-hertz, two-pole, two-phase servo motor rated at 25 w maximum output. As used in the MSRE, the input power is single-phase 115-v ac, and phase splitting is obtained with a 10-to 12-μf capacitor in series with one of the field windings. An actachometer is mounted integrally on the motor shaft. The tachometer output is used as a feedback signal to stabilize the servo controller. Tachometer output is 6 v per 1000 rpm. A small blower is included as part of the assembly. The blower is powered by a separate, capacitor-type two-phase motor and runs continuously whether the servo motor is on or off. These three units (motor, tachometer, and blower) are incorporated into a single unit supplied by the Diehl Electrical Division of the Singer Manufacturing Company. The unit specified for the MSRE is similar in shape, size, and performance to a standard Diehl 25-w motor No. FPF 49-91-1. They are special in that they call for class H radiation-resistant electrical insulation and use radiation-resistant grease. Performance data are given in Figs. 2.7.26 and 2.7.27.

# Procurement Information

Procurement specifications are contained in Yard Specification No. 114096, modified by ORNL, and dated April 12, 1964, and in ORNL Purchase Order No. 63Y-76819.

# 2.7.9.2 Electromechanical Clutch

This clutch is of the single-disk type with a stationary field coil. It is supplied by the Electroid Corporation, Union, New Jersey, their Drawing 2EC-6CC-8-8. Characteristics and specifications are as follows:

Rated static torque 75 in.-1b

Rated coil voltage 32 dc

Coil current at 32 v dc 0.24 amp

Nominal size (clutch disk diam) 2-5/8 in.

Engagement time<sup>a</sup> 0.0075 sec or less

Release time Not available

Electrical insulation Class H

Friction torque (max) 0.5 in.-oz

This number from Electroid catalog for this size clutch with both 24- and 90-v dc coils.

Detailed procurement information is on Vard Corporation Drawing No. 114701.

# 2.7.9.3 Overrunning Clutch

The overrunning clutch is a standard, commercially available device manufactured by the Formsprag Company, 23601 Hoover Road, Warren, Michigan. It is a Formsprag model FS-05 in which the Oilite sintered bronze bushing normally used has been replaced with a bronze bushing and which has been packed with California Research Corporation type NRRG-159 or Shell type AFL grease. The manufacturer states it meets performance requirements as follows: normal running torque, 3 lb-ft at 8 rpm; and stall torque, 20 lb-ft at 8 rpm. Additional specification-type information is contained in a letter dated February 1, 1963, from W. T. Cherry, Formsprag Company, 609 West Lincoln Avenue, Anaheim, California, to P. Butkys, Yard Division of Royal Industries.

# 2.7.9.4 Position-Indicating Synchros

The synchro torque transmitters, both "Fine" (size 18) and "Coarse" (size 31), meet military standard (Mil. S-20708) design requirements with respect to size, shape, mounting dimensions, and performance characteristics. They are nonstandard in that the electrical insulation and lubricant are for a high-radiation environment. The torque transmitters in the prototype rod drive unit were supplied by the Vernitron Corporation, 1742 Crenshaw Boulevard, Torrance, California. Additional specification data for these transmitters are as follows:

<table><tr><td>Item</td><td>Size 31a</td><td>Size 18b</td></tr><tr><td>Primary winding</td><td>Rotor</td><td>Rotor</td></tr><tr><td>Primary voltage, nominal</td><td>115</td><td>115</td></tr><tr><td>Frequency</td><td>60 cps</td><td>60 cps</td></tr><tr><td>Input current, max</td><td>462 ma</td><td>105 ma</td></tr><tr><td>Input power, max</td><td>6.6 w</td><td>4.0 w</td></tr><tr><td>Transformation ratio</td><td>0.783 ± 2%</td><td>0.783 ± 2%</td></tr><tr><td>Phase shift, max</td><td>6.5° lead</td><td>18.0°</td></tr><tr><td>Electrical error, max</td><td>10 min</td><td>6 min</td></tr><tr><td>Torque gradient</td><td>0.40 oz-in./deg.</td><td>0.05 oz-in./deg.</td></tr><tr><td>Null voltage (total), max</td><td>125 mv</td><td></td></tr><tr><td>Null voltage (fundamental), max</td><td>35 mv</td><td></td></tr></table>

aVernitron Corp. No. VTX31-6Rl, Vernitron Dwg. OD10581.   
bVernitron Corp. No. VTX18-6Rl, Vernitron Dwg. OD10582.

# 2.7.9.5 Position-Indicating Potentiometer

The specifications for the position-indicating potentiometer, a Beckman Company type 6200 series potentiometer with ball bearings lubricated as described in Sect. 2.7.9.8, are as follows:

Type

Infinite resolution, cermet resistance element, continuous rotation with no stops, metal housing, 1-1/16 in. diam $\times$ 5/8 in. long with standard servo mounting dimensions, ball bearings

Resistance

1000 ohms ± 5% at $150^{\circ}\mathrm{F}$

Linearity

0.5%

Electrical rotation

$350 \pm 5^{\circ}$

Power rating

5 w at $185^{\circ}\mathrm{F}$ derated to zero at $300^{\circ}\mathrm{F}$

Refer to UCNC Purchase Order 56S1446, Item 1 (Requisition L-8824), January 29, 1965.

# 2.7.9.6 Limit Switches

Limit switches are Micro Switch type V3-1301, a high-temperature nuclear-radiation-resistant design, manufactured by Micro Switch Division, Minneapolis-Honeywell Regulator Company, Freeport, Illinois. Catalog information describing this switch is supplemented by two letters written by V. J. Brown, Los Angeles 22, California, to Povilas Butkys, Ward Corporation. The letters are dated December 20, 1962, and January 9, 1963.

# 2.7.9.7 Electrical Wiring

Internal wiring within the rod drive unit from the terminals on the disconnect to the various components is of high-temperature, radiation-resistant hookup wire. The prototype used Supertemp type MGT, manufactured by American Super-Temperature Wires, Inc., 50 West Canal Street, Winooski, Vermont.

Micatemp, a similar type of wire manufactured by Rockbestos Wire and Cable Company, Division of Aero Corporation, Nicoll and Conner Streets, New Haven, Connecticut, is equally acceptable.

# 2.7.9.8 Lubrication

The gears, overrunning clutch, and the bearings in the gearbox, motor, synchros, etc., are lubricated with a nuclear-radiation-resistant grease: Shell Corporation type APL or California Research Corporation type NRRG-159. This latter grease<sup>5,6</sup> is composed of "C<sub>16-18</sub>-alkylbi-

phenyl fluid inhibited with didodecyl selenide and gelled with a sodium terephthalamate." The sprocket chain and the limit switch actuator are coated with Neolube, a film of colloidal graphite deposited as a dispersion of graphite in a volatile carrier (isopropanol). Neolube is manufactured by Huron Industries, Post Office Box 104, Port Huron, Michigan.

# 2.7.9.9 Thermostatic Switches

The thermostats are small bimetal-type units with the bimetal mounted in a ceramic tube. Sample switches were tested well beyond destruction by heating to over $1200^{\circ}\mathrm{F}$ , and no release of solder or other low-temperature melting point material was observed.

Technical data on these switches, based on the seller's catalog, are as follows:

Electrical rating

50 w at 115 to 230 v ac, non-inductive load

Operating temperature range

Adjustable, by means of a screw, to $300^{\circ}\mathbf{F}$

Physical appearance

1/4 in. diam, 1-1/8 in. long; terminal at each end with a 2-56 tapped hole for making electrical connection

Contact operation

To open on rising temperature

aThe range specified for the MSRE was 150 to $200^{\circ}\mathbf{F}$

The thermostats were purchased from the George Ulanet Company, 413-415 Market Street, Newark, New Jersey, their model No. 17-L3. Refer to UCNC Purchase Order 59Y-17341, Requisition No. L-9682 dated August 10, 1965.

# 2.7.9.10 Gears

All gears are of carbon steel or stainless steel. The 24 diametral-pitch gears in the power train between the motor and the output sprocket are of steel and designed particularly for the drive unit. The 32 diametral-pitch gears which drive the synchros and the position potentiometer are commercially available components with minor modifications where required for mounting, etc.

The worm and gear set is the end product of test stand experience with the prototype unit. The original design specified an aluminum bronze worm wheel mating with a steel worm. The worm had a hardness of 38 to 42 on the Rockwell C scale and a surface finish of $64\mu \mathrm{in}$ . maximum roughness. These gears failed at a rapid rate by abrasive wear. The final design of this gear pair, based on additional test stand experimentation and life testing with the prototype unit specified type 440C stainless steel, hardened to Rc 55 or better, for both the worm and gear. The worm thread was ground and had a surface finish of ap-

proximately $20\mu \mathrm{in}$ . The gears were lapped to form selectively fitted pairs. Gear sets of other hardenable steels were tried in the prototype, and it was concluded that the determining factor for the steels used in this service is probably surface hardness and finish, not any particular type or alloy.

![](images/7f1d4fae22255f6232f35bfc7c6195ef1112ad26df59424c8248cc3b29ab2f47.jpg)  
Fig. 2.7.1. MSRE Control Rod Drive Unit and Housing.

![](images/4febeb226bb07979e6a5293237bd4796459b79736f582f22999579330f7b0eb4.jpg)  
Fig. 2.7.2. MSRE Control Rod Drive Unit - Upper End Showing Gear Box and Servo Motor.

![](images/5394605643b1472ce22f1b3618b84d137fa340d9b2cd159ed5e4a6aacb7905d9.jpg)  
UPPER AND LOWER LIMIT SWITCHES   
Fig. 2.7.3. MSRE Control Rod Drive Unit - Upper End Showing Location of Limit Switches.

ORNL-DWG63-839r

![](images/c68a8d41858f0d0b6a029263c3650d926cd5f6b661c77817cf7f9fad9fc89d4c.jpg)  
Fig. 2.7.4. Electromechanical Diagram of Control Rod Drive Train.

![](images/ca9a72fd6bbc3efc34f752479cab6a4f516a4745d441072c6414afc7e5414f21.jpg)  
Fig. 2.7.5. MSRE Control Rod Drive Unit Power Transmission Diagram.

![](images/fdf90096f424c8b7acd7e17811710279f5280514b7dd68b666e40ac34677954e.jpg)  
Fig. 2.7.6. MSRE Control Rod Thimble.

PHOTO 7111A

![](images/46b884574d3668f4ee961b4aed64ff914346264c405ebbbbd75a984b478f4151.jpg)  
Fig. 2.7.7. MSRE Subassembly of Control Rod Thimbles and Graphite Sample Tube.

![](images/87761e07ea59496ab9dd235775218557aa9ddefc5b0717438961b6c752b5d0f2.jpg)  
Fig. 2.7.8. Subassembly (Fig. 2.7.7) Mounted on Reactor Vessel.

ORNL-DWG 64-6083

![](images/08945bc797dd8b8abd3cf2a817b2e03bdeeb7f65f65aa2e5f8bf755890c9f4ae.jpg)  
Fig. 2.7.9. Diagram of Control Rods, as Installed.

![](images/ef29a7a0bf1101112f10c3c3f747f09b2e564d2de1a0da0c8c60b48ea50c42cc.jpg)  
Fig. 2.7.10. MSRE View Looking Down Through Access Opening in Secondary Containment Cell Showing Control Rod Drives as Installed.

![](images/578ee27f263eabee489716fe7709fd71b4dc2638ce5290c115c4000a1748d788.jpg)  
ORNL-DWG63-8394R3

![](images/4d44a55d7af73326882256eba6447e753850e4607cd3964cde1190fcc148f8f0.jpg)  
Fig. 2.7.11. MSRE Lower End of Control Rod.

![](images/f2a32f584e3bfe7cfc36e6ddadda9ff0adefe43d59865a14b7071192eb93f2ff.jpg)

Fig. 2.7.12. Diagram of Instrumentation Used to Locate Rods at Fiducial Zero Position.   
![](images/bcd26b8889dbb1df35906bfdc5c4307c410a3ea50e4688b2ac2e71bd0e443fbf.jpg)  
NOTE:   
4. THIS VALVE IS ALSO A SAFETY SYSTEM BLOCK VALVE. Closes IF RM 565 B OR C INDICATES EXCESS RADIOACTIVITY.

![](images/2d34472ad6eaff8e6c24f0bd54048bff5f1ae47afeb51e3ef8a73b1431cdd7f9.jpg)  
Fig. 2.7.13. Cross Section of MSRE Control Rod Drive Shock Absorber.

PHOTO-73175A

![](images/cb2c4f6f53e1aa1e3777e03a9d4880add399de8c9070442236a21ad728aa8bc7.jpg)  
Fig. 2.7.14. MSRE Shock Absorber and Thermostatic Temperature Switches.

Fig. 2.7.15. MSRE Rod Drive Temperature Indicator.   
![](images/fa7caabf6b8fd6d2accb513675211322a9765ff0a4ff7752d58cacd5bef7e5c9.jpg)  
NOTE: REGULATED SUPPLY IS ZENER DIODE TYPE DESIGNED TO REPLACE STANDARD CELLS IN POTentiometers

![](images/53e4856abb729c3eb628b8541361e26a6231deae19882e5714bcd253a20ae48a.jpg)  
Fig. 2.7.16. MSRE Rod Drive Unit, Switch Actuator-Guide Bearing Assembly.

![](images/fbeae423e7cd85f7381fe2611a3626626868dbbb842f6cc06955697f15f3a3ff.jpg)  
Fig. 2.7.17. Upper End of Rod Drive Unit, Showing Inlet Air Tube for Control Rod Cooling Air and Side View of Upper and Lower Position Limit Switches.

![](images/e2b8abce2bb55baf4eb88542b1a953917714f296d3ff07726c5f311c83da1934.jpg)  
Fig. 2.7.18. Upper End of Rod Drive Unit, Showing Position Limit Switches.

![](images/6d2794858029b90bcdf52f754458936a58291f00c2b5a86731b34b2d805860c8.jpg)  
Fig. 2.7.19. MSRE Control Rod with Poison Elements Shown Removed from Supporting Structure.

![](images/b1220103a86df8c4277e889b8ac8383d4846ae998694e156ef1199ebf4badf4b.jpg)  
Fig. 2.7.20. MSRE Control Rods, Assembled.

![](images/72d49a199b8a20f449c182097fe85d11356d77beb6685e53ea52f8bcdf33192d.jpg)  
Fig. 2.7.21. MSRE Rod Drop Timer Circuitry.

![](images/58cdb01fbc6306a904f4754657b8810289ec4f63b4ee5d8315d26cf3c8288ff6.jpg)

![](images/ee7a2a63886252f23c1372c420cfb29fa09db35b0939e13cfd1a365a8ddc4637.jpg)  
Fig. 2.7.22. MSRE Control Rod Drive Motor Speed vs Voltage.

![](images/789153062f73d0f506ede628745c38f9bcb8e15aab5054e92f48b70bf9ca9aba.jpg)  
CURVE A-REFERENCE CURVE OF SATISFACTORY SCRAM PERFORMANCE; BASED ON ACCELERATION OF 5 ft/sec² AND RELEASE TIME OF O.400 sec  
CURVE B-SCRAM PERFORMANCE FROM TESTS OF JAN. 27-28, 1964   
Fig. 2.7.23. MSRE Control Rod Height vs Time During Scram.

![](images/7155ccc1458fef60282e4d15f0ec24543e9a7475c1841fa305177211bd7cb719.jpg)  
Fig. 2.7.24. MSRE Scran Performance Tests (Jan. 27-28, 1964).

![](images/8a2f6981b99058bc28e1aecae0dc761e0249707018b2b8cd266acac01e373661.jpg)  
Fig. 2.7.25. MSRE Control Rod Performance During Scram.

![](images/379f8bb4752ce294a99800e73c5cf359436622478f36f8ea6716f91d22c8cc52.jpg)  
Fig. 2.7.26. Performance Curves, 25-w Servo Motor.

ORNL DWG. 67-2414   

<table><tr><td colspan="3">TACHOMETER ELECTRICAL DATA 60 CYC.†</td></tr><tr><td>PHASE</td><td colspan="2">1</td></tr><tr><td>POLES</td><td colspan="2">2</td></tr><tr><td>EXCITATION</td><td>INPUT CURRENT (MA.)</td><td>50</td></tr><tr><td>PHASE (115v.)</td><td>INPUT POWER (WATTS)</td><td>5.0</td></tr><tr><td rowspan="3">OUTPUT PHASE</td><td>*OUTPUT VOLTAGE/1000 RPM</td><td>6</td></tr><tr><td>LINEARITY.% at 3000 RPM</td><td>1.0</td></tr><tr><td></td><td></td></tr><tr><td rowspan="2">RESIDUAL VOLTAGE</td><td>RMS (Mv.)</td><td>110</td></tr><tr><td>VARIATION (Mv.)</td><td>55</td></tr></table>

*May vary ±10%.   
Based on tach. load of 0.1 megohms.

MOTOR PERFORMANCE DATA

10 WATT MAX. OUTPUT·115/115 VOLTs·60 CYCLES·2 POLES·2 PHASE

![](images/41381aac273b1cd5f2039b34e78e89a5a5217707890cea9db6c12085ccd562de.jpg)  
Fig. 2.7.27. Performance Curves, 10-w Servo Motor.

# 2.8 LOAD CONTROL SYSTEM

The reactor loading system in the MSRE has been described in detail in ORNL-TM-728. Some design changes to improve the effectiveness of the air seals and the annulus cooling air flow have been made since the publication of TM-728, but the basic design remains unaltered. Briefly, the nuclear power generated by the reactor is finally dissipated by a coolant-salt-to-air radiator and discharged to the atmosphere via a stack 70 ft high and 10 ft in diameter. Air flow through the radiator is supplied by two large, 250-hp (nominal), axial flow fans. The radiator consists of a bundle of 120 thin-walled tubes (0.750 in. diam, 0.072-in. wall, 30 ft long) bent in the shape of a zee (Fig. 2.8.1). The radiator is enclosed by two vertically sliding doors which act, to a degree, as air flow control elements. Additional control of air flow is obtained with a bypass damper and by selecting either one or both fans. When the doors are fully lowered, cans on the guide roller track force the gasketed door against a flat sealing surface to prevent the entry of air to the radiator. Figure 2.8.2 shows the radiator, the doors and their drive mechanism, and the coolant salt pump as they are installed in the duct. Figure 2.8.3 is a simplified drawing of the door drive mechanism. Note the flywheel which reduces the door acceleration during a load scram when the clutch and brake are released. The flywheel is connected to the shaft by an overrunning clutch so that it continues to coast after the door reaches the lower limit.

The coolant salt experiences a calculated temperature drop (subject to small changes caused by slight variations in flow) in the radiator of $56^{\circ}\mathrm{F}$ at full power of 7.5 Mw. When ambient inlet air temperature is in the $40^{\circ}\mathrm{F}$ region, typical operating parameters at the radiator are as follows:

Coolant salt inlet temperature 1015°F

Coolant salt outlet temperature 1073°F

Air inlet temperature 42°F

Air outlet temperature 151°F

Air flow 200,000 cfm

Coolant salt freezes at $850^{\circ}\mathrm{F}$ , and the operating margin above the freezing point is therefore $165^{\circ}\mathrm{F}$ . This margin will be less on cold days, when the ambient temperature is reduced.

The remainder of this section is concerned with the instrumentation, control, and protection of the complex of equipment that is used to reject the reactor's energy output to the atmosphere.

It has been pointed out in ref. 2 (pp. 107 and 140) that the MSRE is a load-following reactor and is inherently self-regulating when developing any appreciable power. In any realistic power reactor system,

the operators have little or no direct control over the public's demand for power. There was, therefore, no incentive to control closely the load on the reactor. The only requirement in the MSRE is that the operators be able to establish and adjust the load about a point in any region within the operating range, up to 7.5 Mw, of the reactor and to do so in an orderly fashion. It can be seen from Fig. 2.8.4 that the reactor load (the heat rejection at the radiator) is determined by five independently variable elements, namely: (1) inlet radiator door, (2) outlet radiator door, (3) main blower 1, (4) main blower 3, and (5) bypass damper. Over a considerable portion of the range, the same value of load can be obtained by two or more different operating configurations of the above equipment. It follows that load changing and adjusting, if done strictly by manually manipulating these five different components, may add considerably to the duties of the operator at a time when he least needs such additional responsibility and, in addition, may produce unnecessarily high thermal shocks with accompanying high stresses.

In view of the foregoing, the adjustment of the thermal load of the reactor has been designed for either manual or programmed control. With programmed control, load changes are accomplished by means of a single control at the console (Fig. 2.8.5) when the selector switch (S-23) is in the "Auto" position.

# 2.8.1 Blower Operation

The main blowers, 1 and 3, are axial flow propeller-type fans. They are driven by direct-connected, 250-hp, 1750-rpm, three-phase, 440-v ac wound rotor induction motors. High rotor resistance starting is incorporated in the power circuits to limit starting currents to acceptable values. During start, the motor windings are connected in series to external resistances. As the motor accelerates, the external resistance in each winding is successively reduced by timer-controlled switching. This requires approximately 30 sec. After attaining full speed, when all external resistances have been disconnected, the motors operate as typical squirrel-cage induction motors. This startup circuitry operates automatically when a motor circuit breaker is closed to start a blower and, in the following discussion, is not included as a part of the reactor control system. The control system relays control the blowers by operating the "Close" and "Trip" coils in these circuit breakers.

# 2.8.2 Door Operation

Figure 2.8.6 is a diagram of the door drives. A single gear-reduced motor provides power to raise both doors; individual door control is obtained by means of clutches and brakes located on the separate sheave drive shafts. Operating conditions of the elements governing door movement in different situations are shown in Table 2.8.1.

Table 2.8.1   

<table><tr><td></td><td>Situation</td><td>Motor</td><td>Clutch, 
Inlet Door</td><td>Brake, 
Inlet 
Door</td><td>Clutch, 
Outlet Door</td><td>Brake, 
Outlet 
Door</td></tr><tr><td>1.</td><td>Normal, raise or lower both doors simultaneously</td><td>On</td><td>Engaged</td><td>Off</td><td>Engaged</td><td>Off</td></tr><tr><td>2.</td><td>Normal, raise or lower in-let door only</td><td>On</td><td>Engaged</td><td>Off</td><td>Disengaged</td><td>On</td></tr><tr><td>3.</td><td>Normal, raise or lower out-let door only</td><td>On</td><td>Disengaged</td><td>On</td><td>Engaged</td><td>Off</td></tr><tr><td>4.</td><td>Load scram</td><td>On or Off</td><td>Disengaged</td><td>Off</td><td>Disengaged</td><td>Off</td></tr></table>

Door position is indicated on the control console (Fig. 2.8.5) by synchro position receivers driven by synchro transmitters. The transmitters are mechanically connected, through gear reducers, to the sheave drive shafts. The intermediate limit switches (Fig. 2.8.7), used as control interlocks, are actuated by cams on the transmitting synchro drives. The position of these switches is adjustable over a wide range. The upper and lower limit switches are in redundant pairs and are actuated directly by the doors. These limit switches are an integral part of the control system used during normal operation. Additional switches used solely to protect the doors and the drive mechanism from overtravel and overload are provided. These are described in Sect. 2.8.6.

The bypass damper is positioned by an air cylinder with a built-in positioner, as diagrammed in Fig. 2.8.6. Cylinder position, directly proportional to cylinder pressure, is controlled either directly and manually or with a pneumatic servo. The servo positions the bypass damper to maintain the differential pressure drop $\Delta P$ across the damper equal to the set-point value $\Delta P_{\mathrm{sp}}$ .

Direct manual control of damper position may be obtained by manually adjusting the inlet pressure to the air cylinder with a pressure regulator in the manual control station mounted on the main control board. A three-way valve transfers cylinder air supply from the servo to the pressure regulator.

Assuming that one or both blowers are on, servo control of $\Delta P$ across the damper is accomplished from the console by operator adjustment of $\Delta P_{\mathrm{sp}}$ with the switch labeled DP Demand (see Figs. 2.8.5 and 2.8.6). This switch operates an electric-motor-driven pressure regulator, $P_{d}X-AD2-A1$ , whose output $\Delta P_{\mathrm{sp}}$ goes to the pneumatic servo. If the condition of other elements in the system (doors and blowers) is not

altered, a request for an increase (decrease) in $\Delta P_{\mathfrak{sp}}$ will cause the bypass damper to close (open). If, however, the doors are moved or blowers are turned on or off, the damper will also respond to maintain $\Delta P$ equal to $\Delta P_{\mathfrak{sp}}$ .

When load control is being automatically programmed, the adjustment of $\Delta P_{\mathfrak{sp}}$ is included in the program and is not directly manipulated by the operator. In either control mode the values of $\Delta P$ and $\Delta P_{\mathfrak{sp}}$ and the damper position are indicated on the console.

# 2.8.3 Automatic Load Programming

As the reactor system is brought from zero to full power, the various elements (as stated previously) governing reactor load are programmed in accordance with Fig. 2.8.8. This diagram is based on tests conducted on January 31, 1967. The dashed portion of the door position curve merely connects the end-point values of power obtained by moving the doors from the fully closed to fully open positions. The curves will shift slightly with changes in ambient temperature.

The programmed control system was designed with these fairly obvious assumptions:

1. When the radiator is presenting a constant frontal area to the air stream, heat transfer therefrom is closely related to static pressure drop across the radiator.<sup>3</sup>   
2. Heat transfer from the radiator increases as the doors are raised as long as the operating condition of the other flow elements (blowers and bypass damper) remains unaltered. The tests referred to above and in Fig. 2.8.8 indicate that the last 2 or 3 ft of door travel exerts little influence on the load; that is, the doors are most effective during the early stages of their movement.   
3. The static pressure drop measured across the bypass damper (see Fig. 2.8.6) differs only slightly from the static pressure across the radiator; that is, the pressure drop in the branching ducts to and from the radiator doors and the bypass damper, respectively, is small compared with the pressure drop across the radiator tubes.

The programming control system diagrammed in Fig. 2.8.6 uses the air flow differential pressure $\Delta P$ across the bypass damper and the limit switches (Fig. 2.8.7) to program the sequence in which the doors are raised, the blowers are turned on, and the bypass damper is opened or closed. Control system pressure and limit switches also provide restrictive and permissive interlock signals. Figures 2.8.9 to 2.8.11 are, respectively, the block diagram and the relay circuits which implement the block diagram. The operation of the load control system when the programmed load control ("Auto" control) is in use is best explained by tracing the sequence of events and operations which take place as a particular power level is established following a reactor start.

Suppose that operation at 7.5 Mw is required and the operator will establish this value of reactor load using the programmed or automatic load control mode of operation. Procedure and system actions are outlined below (refer to Figs. 2.8.5 to 2.8.11 in following the discussion):

Actuate the load control selector S23 to the "Auto" position. This switch is spring-returned to the "Hold," or center, position; but, if the conditions required to establish automatic operation have been met, automatic load control is in force. These conditions are (see circuit 150, Fig. 2.8.10):4

1. reactor system in "Operate" mode, contact KAL36F closed (see Sect. 1.4);   
2. salt level in the fuel-pump bowl above $43\%$ of full-scale level, contact K97C closed;   
3. fuel-salt pump speed greater than 1000 rpm, contact K96D closed;   
4. coolant-salt pump speed greater than 1400 rpm, contact K1OE closed;   
5. drain valve FV-103 frozen, contact K659D closed;   
6. static air pressure drop $\Delta P$ across the radiator equal to the operator-established set point $\Delta P_{\mathfrak{sp}}$ in the bypass damper controller (Fig. 2.8.6), contact K211A closed.

Alternate conditions to 6 above are:

7. system not in Run, contact KAl39C closed;   
8. bypass damper $100\%$ "Open," contact K2l4A closed;   
9. operator-established set-point signal $\Delta P_{sp}$ to the bypass damper controller set at zero.

With the automatic load control mode established and, in the case under discussion, the conditions listed above obtaining, reactor power is increased from near zero to approximately 1.0 Mw by the operator turning on main blower 1 or 3 and requesting the load increase with the load demand switch S24. Assume that it is decided to begin the ascent to $100\%$ power (7.5 Mw) using main blower 1. The operator will actuate the main blower 1 Start switch S29, and, if system conditions are not producing preventive interlocks, the following conditions prevail (refer to the block diagram in Fig. 2.8.9 and the circuits in Figs. 2.8.10 and 2.8.11):

1. The bypass damper is being held $100\%$ open $(\Delta P_{sp} = 0)$ ,   
2. both radiator doors are closed,   
3. main blower 1 is "On,"   
4. main blower 3 is "Off,"

5. main blower 3 has been selected to turn on automatically when the load demand cannot be met by a single blower. Had the operator elected to start with main blower 3, he would then have selected main blower 1 to turn on automatically when the load demand requires both blowers.

After main blower 1 is turned "On," the operator starts to load the reactor by actuating load demand switch S24. This causes the radiator doors to start opening and, as long as S24 is actuated, they will continue to do so without restriction until the lower intermediate limit is reached. The operator follows the course of reactor power by observing either the linear power recorder on the main control board or the two indicators, RI-NLCl-A1 and RI-NLC2-A2, on the console. The doors will continue to rise until the lower intermediate limit is reached and the system power level is approximately 1 Mw. The doors may be stopped at any point before this if it is desired to operate at powers less than 1 Mw.

When the doors have been raised to the lower intermediate limit, system conditions are:

1. main blower 1 is "On,"   
2. bypass damper is being held $100\%$ open $(\Delta P_{sp} = 0)$ ,   
3. reactor power is approximately 1 Mw.

The l-Mw level is the transition point from "Operate-Start" mode to "Operate-Run," and further increases in power level require that the Run mode of system operation be established. This has been discussed in Sects. 1.4 and 4.2.

Once the system is in "Run" mode the operator can again request additional load, using S24 as before. This can be seen by referring to circuits 162 and 164, in which "Run" relay contacts KAl39G and KBl39D bypass the intermediate limit relay contacts K219A and K223A respectively. Note that if the automatic rod controller has been used during the preceding operations, it has been in the "Flux" control mode during "Start." Going from "Start" to "Run" automatically puts the automatic controller into the "Outlet Temperature" mode (see Sects. 1.4 and 2.6). As the operator continues to request more load, the doors continue to rise until fully open. As the doors are going from the partially raised, intermediate limit, position to the upper limit position, the bypass damper remains fully open since the control system, by means of contact S24A in circuit 151, Fig. 2.8.10, is keeping $\Delta P_{sp} = 0$ . The load is increasing because of the increasing exposure of the radiator to the flowing air stream. Once both doors reach their upper limits, the bypass damper must start closing to divert more air through the radiator and thus increase heat rejection. This is accomplished in circuit 153, Fig. 2.8.10, by switch contact S24C. Closure of this contact turns on the motor which drives the $\Delta P_{sp}$ device, $P_{d}$ AD2-A1, in Fig. 2.8.6;

$\Delta P_{sp}$ is increased, and the bypass damper controller $P_{d}C$ -AD2-A closes the damper to satisfy the requirement for increased $\Delta P$ ; more air is diverted

through the fully exposed radiator and more heat is extracted from the system. Reactor power rises to meet this increased load. As before, the operator continues to request increased load with S24 and to follow the power by watching the linear channel instruments on the console and the main board. Any power level in this region can be established by the operator. This type of system response continues until the bypass damper is fully closed and the entire output of main blower 1 is flowing through the radiator. A summary of system conditions is:

1. main blower 1 "On,"   
2. main blower 3 "Off,"   
3. bypass damper $100\%$ closed,   
4. $\Delta P_{\mathfrak{sp}}$ at intermediate value,   
5. power level at approximately 5 Mw.

The only way now remaining to increase heat rejection (load) by the radiator is to turn on the second blower, main blower 3 in this discussion. Note, in Fig. 2.8.10, circuits 153 and 154, that when the bypass damper is fully closed, the following circuit actions take place: (1) contact K215A in circuit 153 opens, preventing further increases in $\Delta P_{sp}$ , and (2) contact K215F in circuit 154 closes and permits energizing of relay 154, which will turn on the second main blower. At this point, the value of $\Delta P_{sp}$ is established and is equal to or greater than the actual $\Delta P$ across the radiator. With the radiator presenting a constant frontal area to the air stream, as it will when the doors are fixed at their upper limits, the heat rejection is related to the $\Delta P$ across the radiator. Now, when the operator asks for more load via the Load Demand switch, S24, the circuitry (see action 2 above) is such that relay K154 is energized; this initiates the start of main blower 3. As this blower picks up speed, it delivers additional air through the radiator, thus raising $\Delta P$ above $\Delta P_{sp}$ , and the bypass damper will open an amount sufficient to bypass some or all of the additional air flow produced by main blower 3, depending on whether or not $\Delta P$ and $\Delta P_{sp}$ were or were not exactly equal when main blower 3 was turned on. The load may change slightly when main blower 3 is turned on. This is attributed to the large duct and the nonuniform shape of the radiator, which permits slight changes in air flow which are not measured by the single probe in the center of the duct.

After the second main blower (3) is turned on, the bypass damper is open, and the control circuit configuration (circuits 153 and 154) is as it was just before the damper was completely closed with only one blower running; that is, (1) contact K215A in circuit 153 (Fig. 2.8.10) is closed, permitting changes in $\Delta P_{\mathrm{sp}}$ by energizing relay 153, and (2) contact K215F is open, and main blower 3, once "On," is sealed and is no longer controlled by relay 154.

With both blowers "On" and with the bypass damper partially open, the heat rejection (load) is increased, as before, by actuating Load

Demand switch S24. This causes $\Delta P_{\mathrm{sp}}$ to increase, and the automatic damper controller (Fig. 2.8.6) closes the bypass damper to divert more air through the radiator. This mode of operation continues until the bypass damper is from 75 to $100\%$ closed and the load, somewhat dependent on ambient temperature, is in the 7- to 8-Mw region.

Reduction in load under automatic load control proceeds in the reverse direction.

# 2.8.4 Manual Control

When the reactor load is in the Manual Control mode, the separate components governing heat rejection (see earlier part of this section) are treated as independent units and are controlled separately. Referring to Figs. 2.8.5, 2.8.10, and 2.8.11, it can be noted that each door, Inlet and Outlet, has its own "Raise" and "Lower" switch and that bypass damper position is controlled by a $\Delta P$ demand switch. The blowers are not cross-interlocked with each other or controlled by door position as they are during Automatic Load Control. The selection of a particular operating configuration of these components and the operational path required to arrive at the desired configuration are entirely at the operator's discretion.

# 2.8.5 Interlocks

In either control mode the reactor loading system is subject to a number of interlocks and control actions whose primary purpose is to prevent or reduce the possibility that the coolant salt will freeze in the radiator. These interlocks and control actions and their purpose are listed and described in Table 2.8.2 and, in some cases, amplified in subsequent paragraphs of this section.

# 2.8.6 Load Scram

Load scram (or emergency closure of the radiator doors) is provided to prevent freezing of coolant salt in the radiator tubes. A pessimistic, worst case, calculation showed that salt freezing can take place is less than a minute. Operating experience tends to confirm this calculation.

Figure 2.8.12 is a diagram of the instrument system used to provide load scram, and Figs. 2.8.13 and 2.8.14 are elementary diagrams of the associated control circuits. The primary input information is coolant salt temperature at the radiator outlet. Three independent temperature measuring channels are used so that if any two of the three indicate an abnormally low temperature, the clutches and brakes in the door drive mechanism are automatically deenergized and the doors drop to the closed position.

Table 2.8.2. Load Control System Protective Interlocks   

<table><tr><td>Interlock or Control Action</td><td>System Response</td><td>Initiating Condition(s) orSituation(s)</td><td>Supplemental and Explanatory Notes</td></tr><tr><td rowspan="4">I. Load scream</td><td>1. Radiator doors are dropped to closed position</td><td>1. Abnormally low (980°F)a coolant salt temperature in radiator outlet pipe, line 202</td><td>1. Low salt temperature is the primary indi-cation that freezing is imminent</td></tr><tr><td rowspan="3">2. Both main blowers, MB-1 and MB-3, are shut down</td><td>2. Abnormally low (less than 700 gpm) flow rate of coolant salt</td><td rowspan="2">2 and 3. A loss or substantial reduction of salt flow through the radiator is the pre-lude to a freeze; particularly true when system is developing full power</td></tr><tr><td>3. Abnormally low speed of coolant salt pump</td></tr><tr><td>4. Control rod scream</td><td>4. Power generation ceases with a rod scream. Unless heat rejection by the radiator is reduced, a freeze is inevitable. Note (refer to Sect. 2.5) that when the reactor is developing power, a rod scream will be produced by an electrical power system failure, a loss of fuel salt level in the pump bowl, or any other condition which reduces input current to the fuel salt pump motorThese are safety-grade interlocks with addi-tional description in Sect. 2.8.6.</td></tr><tr><td>II. First upper limits</td><td>Prevents doors from being raised</td><td>Door(s) at normal, fully open, position actuate limit switches, two each per door</td><td>1. These are typical limit-switching controls of the type usually associated with mechanisms having limited motion. They are not the final limits whose sole purpose is to prevent damage to the system (see inter-lock No. III)2. Redundancy: a) Two switches per door. Actuation of either switch is capable of releasing the door drive clutch and applying the brakeb) When doors are being raised one at a time (manual control), limit switch actuation opens the "Raise" circuit in the door drive motor starter</td></tr><tr><td rowspan="2">III. Final (maximum) upper limits</td><td rowspan="2">1. Shuts off door drive motor 2. Disengages door drive clutches 3. Applies brakes in door drive mechanism</td><td rowspan="2">Door(s) raised above normal fully open position by approximately 8 in.</td><td>3. For details refer to: 
a) Limit switch circuits 216, 220, 224, and 225, Fig. 2.8.7 
b) "Raise" circuits 162 and 164, Fig. 2.8.11 
c) Clutch and brake circuits 13 to 16, Fig. 2.8.13 
d) Motor starter circuit 568, Fig. 2.8.16 
4. These switches also used in the automatic load control circuits</td></tr><tr><td>1. Actuation of these limit switches indicates an abnormal situation which, if continued, will damage the drive mechanism or the doors. If the damage includes a jammed door or snarled cable, it may prevent lowering the doors, either normally or by a load scream, and hence cause a radiator freeze 
2. Reliability: 
a) Two switches per door 
b) Two independent relay circuits with both relays actuated if either door at the final limit 
c) Either channel (relay circuit) will produce the actions tabulated in the "System Response" column 
d) Interconnection wiring carried in separate, individual conduits to control room 
In general, safety system criteria (Sect. 1.5) were used wherever possible in design of this interlock 
3. For details, refer to: 
a) Limit switch circuits 255 and 256, Fig. 2.8.7 
b) Clutch and brake circuits 13 to 16, Fig. 2.8.13 
c) Motor starter circuit 568, Fig. 2.8.16</td></tr><tr><td>IV. Motor overload</td><td>Same as III above</td><td>Motor current in one phase indicates that door drive motor is overloaded</td><td>1. This augments III above. Except that only one excess current relay is used, it has same degree of reliability and redundancy. The excess current relay has its contacts in series with the final upper limit switches and hence the output actions are identical</td></tr><tr><td>V. Manual emergency bypass of coolant pump control circuit</td><td>Maintains forced circulation of coolant salt</td><td>Variable and at discretion of re-actor operator</td><td>1. This consists of a manually operated switch with contacts in the control power circuits of breaker K. This circuit breaker controls ac power to the coolant salt pump2. This switch bypasses all the interlocks in circuit 142, which controls the coolant salt pump (refer to Sects. 3.3 and 4.2.3). It is used only for short periods, when it is absolutely mandatory, regardless of other considerations, that the coolant pump be operated to prevent a radiator freeze.a This switch does not bypass the overcurrent protection which is built into the circuit breaker. Coolant pump operation by this switch is announced3. Refer to Fig. 2.8.17 for circuit details</td></tr><tr><td>VI. Lower limits</td><td>Drops door(s)</td><td>1. Door(s) being lowered and 2. At "lower limit" position (see Fig. 2.8.7)</td><td>1. This is not a true lower limit (Sect. VII, this table). These switches are actuated approximately 8 in. above the fully closed, or sealed, position. The doors then fall freely as in load scream and acquire sufficient velocity to ensure an effective seal against leakage air flow across the radiator (door sealing is described in ref. 1, p. 298)2. Redundancy: Two switches for each door with contacts in series connected to one relay3. For details refer to: a) Limit switch circuits 217 and 221, Fig. 2.8.7b) "Lower" door(s) circuits 163 and 165, Fig. 2.8.11c) Door clutch and brake circuits 13 to 16, Fig. 2.8.13</td></tr><tr><td>VII. "Seal" limits</td><td>1. Stops doors at fully sealed (fully closed) position</td><td>1. Door(s) at fully closed position actuate limit switches</td><td>1. The seal limit is the true lower limit door position. At this location the door(s) has been self-cammed by its own weight against the sealing gaskets which prevent excessive air leakage across the radiator</td></tr><tr><td></td><td>a) Disengages clutch(es) if not disengaged by VI</td><td></td><td></td></tr><tr><td></td><td>b) Applies brake(s), providing door(s) are being lowered</td><td></td><td>2. Reliability: a) Two switches per door b) Any one of following outputs based on switch actuation will stop door(s):</td></tr><tr><td></td><td>c) Shuts off door drive motor</td><td></td><td>1) Clutch disengagement via either of limit switch contacts in each clutch circuit; refer to circuits 13 and 15 Fig. 2.8.13</td></tr><tr><td></td><td></td><td></td><td>2) Clutch disengagement by either of two limit switch contacts which de-energize "lower door" relay(s). Refer to circuits 163 and 165, Fig. 2.8.11</td></tr><tr><td></td><td></td><td></td><td>3) Drive motor shutdown by either of two limit switch contacts which de-energize "lower" contactor in the motor starter. Refer to circuit 568, Fig. 2.8.13</td></tr><tr><td></td><td></td><td></td><td>4) Drive motor shutdown by contact on "lower door" relay, which de-energizes the "lower" contactor in the motor starter. Refer to circuit 568, Fig. 2.8.16</td></tr><tr><td></td><td></td><td></td><td>5) Brake actuation by either of two limit switch contacts in circuits 14 and 16 (refer to Fig. 2.8.13)</td></tr><tr><td></td><td></td><td></td><td>6) If, because of malfunction, drive motor is "On" when a door (or doors is sealed and brake is engaged, the excess motor current relay (see IV, this table) will shut motor off</td></tr></table>

Figure 2.8.15 depicts a typical temperature input signal channel. Note that this is virtually identical to the temperature instrumentation used to provide rod scram (Sect. 2.5) except that the polarity of the thermocouple in the test assembly<sup>7</sup> is reversed; therefore, the application of heat and the resulting temperature increase of this test thermocouple appear as a reduction in temperature to the rest of the instruments. Each temperature input channel can be tested by turning on the heater in the test assembly and observing the response of the relays, which are controlled by the Foxboro temperature switches. The equivalent drop in temperature produced during the test procedure can be observed on a meter by the person conducting the test.

A loss of coolant salt flow will inevitably produce freezing if the doors are open and there is any appreciable air flow through the radiator. Therefore, the doors are also closed automatically by combinations of signals from the flowmeters on the radiator outlet line and from the coolant salt pump speed monitors. These signal combinations are tabulated in Fig. 2.8.12.

The pump speed measuring instrumentation is discussed in Sect. 6. A "loss of speed" input signal to one of the speed monitors is simulated, for testing purposes, by means of the calibration switch built into the speed monitor. Output relay action indicates whether or not the system is responding properly.

The instrumentation used to measure coolant salt flow rate is described in Sect. 6. For test purposes, a simulated loss of flow signal may be produced in each channel by shunting a leg of the resistance bridge in the differential pressure cell. Observation of the output relays gives an indication of input channel response.

Redundant door travel limit switches (Fig. 2.8.16) are employed to protect the ability of the doors to drop when the safety system calls for a load scram. Door limit switching has been described in Table 2.8.2, but it is worth while to emphasize here that the primary purpose of this redundancy is to prevent jamming of the doors or the drive mechanism which, in turn, is likely to compromise their ability to drop. An excess current relay in the motor circuit (Fig. 2.8.16) is used to detect an overload caused by a jammed door, snarled cable, or similar malfunction if it occurs either in the normal motion span of the doors or at the limits. The action of both of these limiting circuits is to stop the drive motor by deenergizing the relays in the motor starter. Manual reset (refer to circuits 255 and 256, Fig. 2.8.16) is required before restarting the drive motor.

Insofar as possible the limit switch design and installation follow the recommended safety-system practices outlined in Sect. 1.5.

The predominant requirement in controlling and operating the load control system is to prevent a frozen radiator. To this end the circuitry diagrammed in Fig. 2.8.17 was added. The time required to freeze the salt in the radiator is extended if circulation is maintained with

the coolant pump. The coolant pump control circuit (see Sect. 4) contains interlocks which stop the pump if it experiences a loss of motor-cooling water or lube oil. The salt pumps cannot run for any appreciable length of time without oil or cooling water, but no harm will come to either pump or motor during the first minute or so following a loss of either. The manual switch, S127, located on the main control board, overrides these interlocks which are capable of stopping the coolant pump. It does not bypass the overload protection in the coolant pump circuit breaker. Use of this overriding switch is controlled administratively and is only permitted if the pump stops and a frozen radiator is imminent.

![](images/4d645a90e7dfa8b65d0337bcb8cd0815214c2c9d666a907e45d2d5a1a2937782.jpg)  
Fig. 2.8.1. Radiator Coil Configuration.

![](images/a5e42782678dd006658a42f2b2fcee34437779f5ee8fe9e51625beddfab486d9.jpg)  
Fig. 2.8.2. Radiator Coil and Enclosure.

![](images/eae7ae7944c96445c5c57022ecaf7293b38067d0a25e71bc150e5a453a215c2e.jpg)  
Fig. 2.8.3. Diagram of Radiator Door Drive.

![](images/d3fbd797f813506f3c65618d02474381c3991fafb5c7f6c264ed50c8f38c47c1.jpg)  
Fig. 2.8.4. Diagram of Radiator Air Flow System.

![](images/14f2fc87635e539e1c27c46edb02992e0d107acadea711f3bd4a8fa4c9b9794e.jpg)  
Fig. 2.8.5. Load Controls Located on Operator's Console.

ORNL-DWG 66-11719

![](images/4ec90e67080e27e9032892dd90e427418010f94e56de436a78aef7b02233c54e.jpg)  
Fig. 2.8.6. Load Control System Bypass Damper Servo.

![](images/bb1d3e0fe3dcfb5a61790afb02686a684df905b5eafc356e992053f56cda25d8.jpg)  
RADIATOR DOOR LIMIT SWITCHES

AP SETPOINT LIMITS

B·PASSAMPER

![](images/8eb4190a91a1624e2e13be5a47dabf3a0aae6df508d699885d3ccdaee9081182.jpg)  
POSITION

![](images/0bd8f282dce2e9d29a65e6cf8c0227eb37da788520f14abfae98ccf53eb2241b.jpg)  
RADIATOR DOOR LIMIT SWITCHES

![](images/8477e00a045b1cd8052a0f159aa9a36f51528588680c2156d633ffe58ded0077.jpg)  
THESE SWITCHES OPERATED  
By CAMION SYNCHRO   
TRANSMITTER DRIVE AND   
ARE CAPABLE OF WIRE   
ADJUSTMENT   
A3021   
Fig. 2.8.7. Radiator Door Control System Limit Switches.

![](images/6b82535b56eed24831c58a89a5f140cb4725293eb081d0ffc5711fce6f2b3e92.jpg)

![](images/319f441acd4fbc9a0f287fcceec061ece0c1b0bb4716278d7dfc1c8270cd0977.jpg)

![](images/66af5938b95135d5e00c85df784c6155908dd6966da1d8eb78b04bbdcc760c34.jpg)

![](images/844fb621d67684f7ec728e2f4956957ff6ccdb40b60ec6078c7d4f91cc6b4311.jpg)

![](images/4d2a5dac465e27baef83324fe014f63398c3ac9f1b156d4b809dd0a073931674.jpg)  
Fig. 2.8.8. Program of Reactor Power Loading.

![](images/855d50fb8a9bc550e1234efec42f7f187fb976c7dec6d960b4cd0c1c9c974d95.jpg)  
Fig. 2.8.9. Radiator|Load Control System, Block Diagram.

![](images/aaeb5ac84a4965eafc12b94ea44a18d46536000adf5f77c94d5150e884c2bd26.jpg)

![](images/e752f9a4b4e08a7f40556556dfce70771bdc171ee89a1f560d640ab64dab94d7.jpg)

![](images/7195a8a8d7ed04b146cb3ab4c4d06084d439e3dd0877513b066ba351c6d40d45.jpg)

<table><tr><td colspan="5">LOAD CONTROL MODE SELECTOR SWITCH</td></tr><tr><td rowspan="3">CONTACTS
HANDLE WND</td><td colspan="3">POSITION (FRETOUT VIEW)</td><td rowspan="3">LOCATION
(CNTN.WB)</td></tr><tr><td>MANUAL</td><td>HOLD</td><td>AUTOMATIC</td></tr><tr><td>0-</td><td>3R-</td><td>0</td></tr><tr><td>A(1)</td><td></td><td></td><td>X</td><td>150</td></tr><tr><td>B(2)</td><td></td><td>X</td><td>X</td><td>150</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

A. DNOTES CLOSED CONTACTS   

<table><tr><td colspan="6">324
LOAD
DEMAND
SELECTOR
SWITCH</td></tr><tr><td rowspan="3" colspan="2">CONTACTS
HANDLE BWD</td><td colspan="3">POSITION (REONT VIEW)</td><td rowspan="3">LOCATION
(CNT, WE)</td></tr><tr><td>DECREASE</td><td>HOLD</td><td>INCREASE</td></tr><tr><td>0</td><td>-2K-</td><td>0</td></tr><tr><td colspan="2">A (1)</td><td></td><td></td><td>X</td><td>151</td></tr><tr><td colspan="2">B (2)</td><td>X</td><td></td><td></td><td>151</td></tr><tr><td colspan="2">C (3)</td><td></td><td></td><td>X</td><td>153</td></tr><tr><td colspan="2">D (4)</td><td></td><td>X</td><td>X</td><td>153</td></tr><tr><td colspan="2">E (5)</td><td></td><td>X</td><td>X</td><td>153</td></tr><tr><td colspan="2">F (6)</td><td></td><td></td><td>X</td><td>162</td></tr><tr><td colspan="2">G (7)</td><td></td><td></td><td>X</td><td>164</td></tr><tr><td colspan="2">H (8)</td><td>X</td><td></td><td></td><td>163</td></tr><tr><td colspan="2">J (9)</td><td>X</td><td></td><td></td><td>163</td></tr></table>

<table><tr><td colspan="12">227
RADIATOR AP SETPOINT NOJUSTING SWITCH</td></tr><tr><td>4</td><td colspan="3">D.C.N. = 3240</td><td>18-166G</td><td>98H</td><td>DATE</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td colspan="3">D.C.N. = 3197</td><td>11-186G</td><td>100H</td><td>DATE</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>B</td><td colspan="3">D.C.N. = 3182</td><td>9-16-65</td><td>100H</td><td>DATE</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A</td><td colspan="3">CHANGES NOTICE = 2422</td><td>9-164</td><td>100H</td><td>DATE</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>NO.</td><td colspan="3">REVISIONS</td><td>DATE</td><td>APPD</td><td>APPD</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">DRAWN
###</td><td rowspan="2">DATE
###</td><td rowspan="2">SUBMITTED</td><td rowspan="2">DATE</td><td rowspan="2">APPROVED</td><td rowspan="2">DATE</td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DEMOVED</td><td>DATE
###</td><td>APPROVED</td><td>DATE
###</td><td>APPROVED</td><td>DATE</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CHECKED</td><td>DATE
###</td><td>APPROVED</td><td>DATE</td><td>APPROVED</td><td>DATE</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

FOR INFORMATION ONLY

DO NOT USE FOR

MAINTENANCE OR

CONSTRUCTION

<table><tr><td colspan="3">####KES D.E.M.K.P.G AUS. CONTROL RELAYS</td><td>D.W.C-61196</td></tr><tr><td colspan="3">WIEIGING DIAGRAM TVA PUB E.PAG</td><td>D.WE.C-41191</td></tr><tr><td colspan="3">ENG.ELEK.CONTROLS INTERLOCK CICCUITS-SN.2-042</td><td>D.W.W.B-57327</td></tr><tr><td colspan="3">ENG.ELEK.ENDRATOR LOAD CONTROL SYSTEM-SN.2-042</td><td>D.W.H.-57325</td></tr><tr><td colspan="3">REFERENCE DRAWINGS</td><td>NO.</td></tr><tr><td colspan="4">OAK RIDGE NATIONAL LABORATORY
OPERATED BY
UNION CARBIDE NUCLEAR COMPANY
DIVISION OF UNION CARBIDE CORPORATION
OAK RIDGE, TENWENDEE</td></tr><tr><td colspan="4">MOLTEK SALT REACTOR EXPERIMENTAL NO. 7503</td></tr><tr><td colspan="4">ENGINEERING ELEMENTARY
RADIATOR LOAD CONTROL SYSTEM
SHEET 1 of 2</td></tr><tr><td colspan="2">SUBMITTED
X Y Z A B C D E F G H I J K L</td><td colspan="2">APPROVED
D.HH B 57522 D RMY I J</td></tr></table>

![](images/0f0e808ba55ab8d3e0aaf20673d0bb7572b7aaf85d48f6deec53e34b67e13a10.jpg)  
Fig. 2.8.10. Radiator Load Control System.

![](images/042ed37e66822095f2a435c44927a1b5e0d800739700431a2e497dca381f9a71.jpg)  
Fig. 2.8.11. Radiator Load Control System.

0

#

#

![](images/eb9919d24d799d3f4bf67dc63365d881742e3cd13c0fa1aeda44f893578324f4.jpg)  
Fig. 2.8.12. Diagram of Load Scram System.

![](images/18af38c7e7aed6012be7fb722888296af1788469e8069eee8eccf040b280de68.jpg)  
Fig. 2.8.13. Load Scram Output Circuits.

![](images/acde6a6b50a25ccbdcd09009a307c06d58701b0e8b241a94748b7aef77f712b8.jpg)

Fig. 2.8.14. Load Scram Input Circuits.   
![](images/cfbd8481deae460fa6ece608af9022abf3e84f7d1b736a9671c34c4cfad2636d.jpg)  
ORNL-DWG 67-912

![](images/b3f859c90769a711d5078f0b6b1ffd5b4587e87a38d70d618eedc5bdf8d886ca.jpg)  
Fig. 2.8.15. Temperature Measuring Equipment Used to Provide Load Scram.

![](images/6e397b29c293f9fcdf64e209f68fcf81b33c2b0ddf4ff87a2554a5e4b181dddf.jpg)

![](images/56d39f83d0db6cef3d3100ec059f92c7662eaad4df98726a5e85116523979b6f.jpg)  
ORNL-DWG 67-91

![](images/811200d63b1d5ba5179383184d12e5b8e6d9cb928f52fb99fb34cfbe3f91e549.jpg)  
Fig. 2.8.16. Radiator Door Drive Motor Control Overtravel and Overload Interlocks.

![](images/b6dcd81f3bf2f15ea3776942ccbf4fda67092b65d14b7d362ff5aa333979b711.jpg)  
S127,EMERGENCY START SWITCH,LOCATED ON MAIN CONTROL BOARD

![](images/895318da2149384eb232028646a0c3e22af734c88eff2ea68809ab13ef74bb2d.jpg)  
Fig. 2.8.17. Normal and Emergency Control of Circuit Breaker "K" Which Operates Coolant Pump Motor.

REFER TO IV-9.7 FOR TYPICAL MOTOR CONTROL CIRCUITS

CONTACT DEVELOPMENT   

<table><tr><td rowspan="2">CONTACT NO.</td><td colspan="4">POSITION</td></tr><tr><td>STOP</td><td>NORM</td><td>RUN</td><td>START</td></tr><tr><td>S127 A</td><td></td><td></td><td></td><td>X</td></tr><tr><td>S127 B</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td>S127 C</td><td>X</td><td></td><td></td><td></td></tr><tr><td>S127 D</td><td></td><td>X</td><td></td><td></td></tr><tr><td>S127 E*</td><td></td><td>X</td><td></td><td></td></tr><tr><td>S127 F*</td><td></td><td>X</td><td></td><td></td></tr></table>

* ANNUNCIATOR CONTACTS

SPRINGRETURN

# 2.9 HEALTH PHYSICS MONITORING

# 2.9.1 Introduction

The purpose of the Health Physics Monitoring System<sup>1</sup> is to provide personnel protection at the reactor site from radiation hazards due to airborne and fixed source activity. The monitors composing this system are placed at strategically located points throughout the reactor building. Those monitors which measure area activity and airborne activity make up the Facility Radiation and Contamination System<sup>1-3</sup> and produce signals which are transmitted to a central annunciator panel located in the reactor auxiliary control room and to the Laboratory Emergency Control Center in Building 2500. The Facility Radiation and Contamination System also produces a building evacuation signal based upon finding a coincidence of at least two monitors in an alarmed state. The other monitors composing the general system are mainly for personal survey and include such items as beta-gamma survey meters, a hand-and-foot counter, and smear counters for use by Health Physics personnel.

# 2.9.2 Facility Radiation and Contamination System

# 2.9.2.1 Introduction

A Facility Radiation and Contamination System was installed in the Molten-Salt Reactor Experiment Building 7503 to continuously and automatically monitor gamma radiation (by seven gamma monitrons) and air contamination (by seven beta-gamma air monitors) in the entire facility. These instruments and other components in the network provide health physics monitoring information, sound local alarms when abnormal conditions occur, and indicate the abnormal conditions on a central panel board and at the Laboratory Emergency Control Center in Building 2500.

Operating personnel are first given warning when a "caution level" of 7.5 mr/hr or 1000 counts/min is detected by a monitron or beta-gamma air monitor respectively. A second warning is given when a "high level" is detected, that is, 23 mr/hr by a monitron or 4000 counts/min by a beta-gamma air monitor.

The building evacuation system operates automatically when two or more monitors or two or more air monitors from a specific group of instruments detect a "high level" of radiation or air contamination. An

audible alarm in the building will be actuated, warning lights outside the building will flash, and an alarm signal will be transmitted to the Laboratory Emergency Control Center, Building 2500.

# 2.9.2.2 System Description

The gamma radiation level is monitored by seven monitrons located throughout the building (Table 2.9.1). Air is monitored for beta-gamma-emitting particles by seven constant air monitors located throughout the building. See Figs. 2.9.1 and 2.9.2 for the location of all the instruments.

Table 2.9.1. Radiation and Contamination Monitors Installed in Building 7503   

<table><tr><td>Location</td><td>Monitor No.</td></tr><tr><td>1. Facility radiation monitorsa,b</td><td></td></tr><tr><td>Control room</td><td>1 RE-7011</td></tr><tr><td>High bay, south</td><td>2 RE-7012</td></tr><tr><td>High bay, west</td><td>3 RE-7013</td></tr><tr><td>Basement, north</td><td>4 RE-7014</td></tr><tr><td>Transmitter room</td><td>5 RE-7015</td></tr><tr><td>Basement center</td><td>6 RE-7016</td></tr><tr><td>2. Radiation monitors with control room alarm onlya</td><td></td></tr><tr><td>Service tunnel</td><td>7 RE-7017</td></tr><tr><td>3. Facility contamination monitorsb,c</td><td></td></tr><tr><td>Offices</td><td>3 RE-7002</td></tr><tr><td>Basement, north</td><td>4 RE-7003</td></tr><tr><td>Transmitter room</td><td>5 RE-7004</td></tr><tr><td>Service tunnel</td><td>6 RE-7005</td></tr><tr><td>4. Contamination monitors with control room alarm onlyc</td><td></td></tr><tr><td>High bay, west</td><td>1 RE-7000</td></tr><tr><td>High bay, south</td><td>2 RE-7001</td></tr><tr><td>5. Mobile air monitor</td><td>7 RE-7006</td></tr></table>

aAll monitrons are Q-1154B-13.   
b. Coincidence of any two high-level alarms in the group causes automatic evacuation.   
c ORNL model Q-2240B-4 constant air monitor.

Since none of the health physics functions originally designed into the monitrons and air monitors were altered, each instrument is an independent unit that retains all its local alarm features. Each instrument, however, is connected to an individual indicator module on the monitoring panel located in the Auxiliary Control Room, Nuclear Board 5. By means of three colored lamps, which normally give a dim light, an indicator module indicates the condition of the instrument to which it is connected; that is, a white lamp burns at full intensity if the instrument is inoperative, an amber lamp burns at full intensity if the "caution alarm level" (7.5 mr/hr for a monitron and 1000 counts/min for a beta-gamma air monitor) is reached, and a red lamp burns at full intensity if the "high level" (23 mr/hr for a monitron and 4000 counts/min for a beta-gamma air monitor) is reached (Table 2.9.2). Any change in the intensity of any lamp, that is, from dim to bright, is announced by the sounding of a buzzer at the monitoring panel and by annunciation on the main board.

The high-level alarm outputs of six selected monitron indicator modules are connected to a coincidence module, and the high-level alarm outputs of four selected constant air monitors are connected to a coincidence module. If a coincidence module receives a high-level alarm signal from any two or more constant air monitors or monitrons in a group, the building evacuation system is actuated (see Table 2.9.1). See Fig. 2.9.3 for a block diagram of the system and Fig. 2.9.4 for the control schematic.

Table 2.9.2. Central Control Panel Alarm Indications for Monitrons and Air Monitors   

<table><tr><td rowspan="2">Instrument Condition</td><td colspan="3">Lamp Intensity</td></tr><tr><td>Red</td><td>Amber</td><td>White</td></tr><tr><td>Normal operation</td><td>Dim</td><td>Dim</td><td>Dim</td></tr><tr><td>Caution levela</td><td>Dim</td><td>Bright</td><td>Dim</td></tr><tr><td>High levelb</td><td>Bright</td><td>Bright</td><td>Dim</td></tr><tr><td>Instrument inoperative</td><td>Dim</td><td>Dim</td><td>Bright</td></tr><tr><td>Instrument removedc</td><td>Bright</td><td>Bright</td><td>Bright</td></tr></table>

<sup>a</sup>Caution level for a beta-gamma air monitor is 1000 counts/min and for a monitron is 7.5 mr/hr. No caution level alarms are available on constant alpha air monitors.   
bHigh level for a beta-gamma air monitor is 4000 counts/min and for a monitron is $23\mathrm{mr / hr}$   
Lamp intensities remain bright until a maintenance connection is made giving "inoperative" indication.

# 2.9.2.3 Components

# Panelboard

The central panelboard for the entire system, located in the Auxiliary Control Room on Nuclear Panel 5, consists of two 12-module racks, one central control chassis, and one dc power supply (Fig. 2.9.2). The 12-module racks contain one indicating module for each instrument, coincidence modules for the beta-gamma radiation alarm system and the contamination alarm system, a remote alarm module, a buzzer module, and a manual evacuation module. The remote alarm module transmits a signal to a single annunciator on the main control panel. The racks and modules are made of anodized aluminum. The modules have anodized Metalphoto front panels. A Metalphoto text strip is provided at the top of each rack for instrument identification. The central control chassis contains manual switches, timers, relays, and monitoring equipment which are parts of the system but not located in modules. For circuit details on the central control chassis, see Fig. 2.9.5.

# Monitron

The remote monitron (ORNL model Q-1154B) is an ac-powered, null-type radiation detection instrument for monitoring gamma radiation. The monitron consists of two basic units: (1) a control chassis, which contains the power supply, the main amplifier, a radiation-level indicating meter, and the controls; and (2) a preamplifier and ion-chamber detector assembly. The detector assembly can be located remotely 50 ft or more from the control chassis. A 0-to-10-mv recorder or a 0-to-1-ma meter can be connected to the monitron. The range of the meter is 0 to 25 mr/hr, and the calibrated accuracy of the meter is within $3\%$ for gamma radiation. The zero setting may be checked by means of a push button.

When the set point of an alarm circuit in the main chassis is exceeded, a bell is rung and a red lamp on the instrument is lighted. A connection on the instrument for an external alarm is used to operate the caution-level alarm for the system. In addition to these standard features, the monitrons installed in Building 7503 have two other features: (1) warmup time delay relays installed on the main chassis and (2) a high-level alarm meter relay installed on an accessory chassis. The instrument and alarms operate as follows:

1. A power failure or a disconnected power cord will cause the white lamp on the central control panel to burn brightly. After power is restored and a 1-min delay for warmup, the white lamp resets itself. During this 1-min delay, caution and high-level alarms at the instrument might sound, but the same alarms on the central panel are locked out and will not sound.   
2. If the caution level of $7.5 \, \text{mr/hr}$ is exceeded, an electronic alarm circuit causes the yellow lamp on the central panel to burn brightly and the bell at the instrument to ring. The alarms are automatically reset at the instrument when the radiation level decreases below 7.5 $\text{mr/hr}$ , but they must be reset manually at the central panel.   
3. The 0-to-1-ma meter output terminals are connected to the accessory meter relay, which is set to operate when the $23\mathrm{mr/hr}$ (high-level)

alarm set point is exceeded. At $23\mathrm{mr/hr}$ the bell at the instrument will be ringing, since it started at $7.5\mathrm{mr/hr}$ , and the red lamp on the central panel will burn brightly. When the radiation level decreases to less than $23\mathrm{mr/hr}$ , the high-level alarm at the instrument is automatically reset by a signal interrupter (allows a reset every 30 sec) from the central panel. The central panel alarm is reset manually.

# Beta-Gamma Constant Air Monitor

This monitor consists of an aspirating system, a paper-tape filter, a halogen-type Geiger-Mueller tube detector, a linear count-rate meter, a recorder, and visible and audible alarms. Air is drawn through the filter by a Roots blower. A sample containing beta-gamma-emitting particles is collected on the paper-tape filter (collected sample size of $1 \times 2 - 1/2$ in.). The sample tape is advanced automatically every $24\mathrm{hr}$ . The tape may be advanced manually at any time by the operator. The detector counts the sample as it is being collected. The count-rate meter is a linear duty-cycle type utilizing a single range and having an internal high-voltage supply. The normal range is 0 to 5000 counts/min, and ranges of 0 to 250, 0 to 1000, 0 to 10,000, and 0 to 25,000 counts/min at full scale may be obtained by various interconnections of two jumper wires under the chassis. The input voltage sensitivity of the rate meter is $200\mathrm{mv}$ . The overall accuracy of the rate meter, including the effect of long-term drift, is within $5\%$ . The corona-regulated high-voltage supply is nominally $900\mathrm{v}$ with $\pm 150\mathrm{v}$ adjustment. The maximum load current is $20\mu\mathrm{a}$ .

The rate meter has adjustable high-level and caution alarms and puts out a 1-ma full-scale signal to drive an integrally mounted Rustrack recorder. The caution alarm is adjustable over the range of approximately 2 to $58\%$ of full scale, and the high-level alarm is adjustable from the caution-alarm set point to full scale. The caution alarm is an electronic circuit which employs a dual triode and plate relay with potentiometer adjustment. The relay is energized below the trip point and is deenergized by current transfer from one triode to the other by a diode that couples the cathode circuits. Hysteresis is approximately $4\%$ of full scale. The high-level trip is accomplished by the high contact on a contact-making meter which energizes the high-level trip relay.

When the set point is reached, the meter contacts and relay are locked in; these are released by depressing the reset push button. A low-level pointer on the panel meter has no contacts and is used only as a visual indicator. The pointer should be set at the level corresponding to the caution-alarm set point.

The instrument has an alarm panel with four lights, a bell, and a buzzer. When the caution set point is reached, an amber lamp is lighted and the buzzer is energized. There is no switch to silence the buzzer, and the operator is expected to advance the tape when this point is reached. When the high-level trip point is reached, a red lamp is lighted and the bell rings. The bell can be silenced by a toggle switch, and when this is done, an amber neon indicator is lighted.

When the filter tape breaks, a red neon indicator is energized and the caution circuit is energized through a flasher. The amber neon bulb

burns continuously, and the caution light and the buzzer come on intermittently. If a tape breaks and, the caution alarm sounds at this same time, the tape-break neon light, the caution light, and the buzzer will be on continuously. A test push button permits checking the alarm panel by simultaneously simulating tape break and high-level alarm signals.

In addition to these standard features, all air monitors at Building 7503 have an accessory "instrument-inoperative" chassis containing a meter relay. The instrument and alarms operate as follows:

1. An accessory meter relay connected to the 0-to-1-ma output of the count-rate meter will cause the white "inoperative" light on the central panel to burn brightly whenever the meter pointer drops to zero, indicating no signal from the instrument. After power is restored and a 60-sec delay, this alarm clears itself. During the 60-sec delay, local caution and high-level alarms do not sound since they are locked out.   
2. At the caution level of 1000 counts/min, an electronic alarm circuit will cause the yellow lamp in the control room to burn brightly. With an ORNL model Q-2240 air monitor, a buzzer will sound at the instrument. The alarm is automatically reset when the filter is changed.   
3. At the high level of 4000 counts/min, the panel meter relay on the instrument causes the red lamp in the control room to burn brightly. Also, the bell sounds. These alarms are reset by advancing the filter and by pressing the manual reset button on the monitor.

# Indicator Module

The indicator module (ORNL model Q-2563-1) consists of three independent transistorized channels, each operating an indicator lamp and providing a dc voltage shift signal for alarm or control purposes and a voltage pulse signal for operating the buzzer module. The three lamps and a push button are on the front panel. Each module is $35.8 \mathrm{~mm}$ wide, $120 \mathrm{~mm}$ high, and $125.8 \mathrm{~mm}$ deep. All connections are made on printed strip connections at the rear edge of the plug-in module.

When the instrument connected to an indicator module is operating normally, all lamps on that module are dim (Table 2.9.2). When the module receives a signal that the primary instrument is operating abnormally or that the caution or the high-level alarm values have been exceeded, the lamps burn at full intensity: white for inoperative instrument, yellow for caution level, and red for high level. A signal is also generated by the module which causes a buzzer to sound. The white lamp indication will remain until the condition causing the alarm is cleared, at which time the lamp will return to the dim condition. The red and amber lights will remain bright until they are manually reset by a push button on the indicator module. If the indicator module is reset when the alarm or abnormal condition still exists, the lamps will momentarily become dim when the reset button is depressed and then will become bright and the buzzer will sound again when the reset button is released.

All indicator modules are identical and can be interchanged or replaced without alteration (see Fig. 2.9.6 for circuit details).

# Coincidence Module

The coincidence module (ORNL model Q-2563-2) consists of one transistorized circuit which accepts a dc shift voltage alarm signal from as many as six indicator modules. The circuit can be adjusted by internal jumper connections to operate a relay for alarm or control purposes on any combination of one to six input signals. All coincidence modules at Building 7503 are arranged to operate the relay when there is a coincidence of any two alarms from a selected group of instruments. Each module is $35.8 \, \text{mm}$ wide, $120 \, \text{mm}$ high, and $125.8 \, \text{mm}$ deep. All connections are made on printed strip connections at the rear edge of the plug-in module.

Four selected air-monitor indicator modules are connected to a coincidence module. Six selected monitron indicator modules are connected to a separate coincidence module. When two or more monitron indicator modules or two or more air-monitor indicator modules receive high-level alarm signals, the associated coincidence module will actuate the building warning and evacuation equipment and will transmit a signal to the Emergency Control Center, Building 2500. A red lamp on the affected coincidence module will indicate which set of instruments has detected an abnormal condition.

When the indicator modules showing an abnormal condition are reset manually, the coincidence module will also be reset.

All coincidence modules are identical and can be interchanged or replaced without alteration, except for an internal jumper connection which determines the number of coincidental input signals required for an output signal (see Fig. 2.9.7 for the circuit schematic).

# Relay Module

To alert the reactor operator, a relay in the relay module operates an annunciator at the main control panel whenever the buzzer module operates; that is, any alarm at the auxiliary panel also annunciates at the operating position. The annunciator at the main control panel operates in the same manner as all other Tigerman annunciators at that point. To reset the annunciator, the operator must first silence the buzzer at the auxiliary control panel.

# Buzzer Module

The buzzer module (ORNL model Q-2563-4) consists of a transistorized trigger circuit that operates a silicon controlled rectifier to actuate a buzzer when a voltage shift pulse is received from an indicator module. The buzzer module is the same size as all other modules and is interchangeable with other buzzer modules (see Fig. 2.9.8 for the circuit schematic).

The buzzer module gives audible notice that an indicator module has received any one of three input signals. The buzzer module, which serves all indicator modules, is reset by a push button at the front of the module.

After being reset, the buzzer will sound again whenever an input signal is received by one of the indicator modules. For example, a change from a normal condition to a "caution alarm level" at some location will start the buzzer. After it is reset, a change to "high alarm level" or to "inoperative instrument" will start the buzzer again.

# Air Whistle and Beacon Lights

When a coincidence module has been energized by two or more monitrons or air monitors, four air whistles are activated by nitrogen gas bottles (one for each whistle) to notify the building occupants to leave the building. The air whistle, a "Clarion whistle" by Westinghouse Air Brake Company, will sound from 2 to 4 min on one filled gas bottle. A control box for each whistle contains a pressure valve, pressure switches which monitor tank and regulated pressures, and a solenoid valve that is opened by an electrical signal from the coincidence module. A momentary signal will open the solenoid valve, and the valve will remain open until it is closed manually by pressing the mushroom head of the valve stem inward. See Fig. 2.9.1 for the location of the whistles and Fig. 2.9.9 for the control circuit schematic.

The normal gas pressures for proper operation of the whistles are not less than 1000 psig tank pressure and 80 to 120 psig line pressure to the solenoid valve. Abnormal pressures are indicated by red lamps (labeled "horn trouble") on the central control panelboard, one lamp for each whistle. A dim lamp indicates normal pressures, and a bright lamp indicates abnormal pressures. Inspection of the gages will indicate whether the tank pressure or the line pressure is abnormal.

Federal Sign and Signal Corporation model 27S 110-v beacons with magenta-colored lenses are installed at 15 locations (Fig. 2.9.2) in and around the reactor building complex and the office building to warn personnel to evacuate the building. These beacons are actuated simultaneously with the air whistles by a signal from a coincidence module, and they are automatically stopped when the coincidence module has returned to a normal condition.

A key-operated switch, labeled "normal disable," on the central control panelboard may be used to disconnect the air whistles and beacons during maintenance or abnormal operation periods. Since the Emergency Control Center receives an alarm signal when the switch is moved to the "disable" position, the Control Center should be notified before the switch is set at this position.

A large red push button located on a module in the central control panel, labeled "manual evacuate," actuates the air whistles and beacons and transmits an alarm signal to the Emergency Control Center (if the Center has not already received an alarm). Remote manual evacuation switches are provided on the reactor control console and in the maintenance control room. If one of the manual evacuation push buttons has been used, the system may be restored to the normal condition by pressing the "reset" push button on the "manual evacuate" module.

# Power Supplies

The main power for the system is 120 v, 60 hertz, supplied from instrument power panel 5 in Building 7503 to the 24-v dc power supply and the monitoring instruments.

The 24-v dc transistorized power supply is a regulated voltage and current unit. A green "power on" lamp on the control chassis and a neon lamp on the power supply panel will be brightly lighted to indicate that the power supplies are operating. Also a "dc failure relay" is used which triggers an annunciator on the main control panel should the dc power supply fail.

# Drawings

The Facility Radiation and Contamination System is described in the following ORNL Instrumentation and Controls and Reactor Division drawings.

1. Q-2354-1 to -7, instrumentation location and wiring diagrams.   
2. Q-2563-1 to -4, and Q-2563-16B, -17, and -19B, plug-in modules.   
3. Q-2358-7, horn control box.   
4. Q-1154B-1 to -14, monitron.   
5. Q-2359-12, monitron high-level alarm.   
6. Q-2240-1 to -23, constant air monitor.   
7. Q-2311B, constant air monitor instrument failure box.   
8. D-HH-Z-40641, instrument placement plot.

# Operating Manual

See ORNL-TM-1127 (Revised)<sup>1</sup> for operating and checkout procedures.

# 2.9.3 General System

# 2.9.3.1 Introduction

This part of the Health Physics Monitoring System consists of all the instruments used for health physics purposes which are not included in the Facility Radiation and Contamination System. In general, these instruments are for use by the area health physicists and for operating personnel in conducting personal surveys of their bodies and clothes. Included in this system are seven beta-gamma survey-type monitors, a beta-gamma sample counter, an alpha sample counter, and a hand-and-foot monitor. See Fig. 2.9.1 for location of these instruments.

# 2.9.3.2 Beta-Gamma Monitors, Q-2091

The beta-gamma monitors are mostly placed in contamination-free areas to provide a means of personal survey of clothing and body. However, when not used for this purpose, they are left operating and serve as backup monitors for the monitrons. In four places (the cooling-water equipment room, the hallway between Buildings 7503 and 7509, the instrument shop, and the venthouse) their primary purpose is area monitoring. They are used instead of the monitron because of the lower unit cost and low area background expected. They provide a local aural alarm only and are not tied to any central alarm system.

The Q-2091 monitor consists of a G-M tube and a count-rate meter with integral power supply. The G-M tube has an adjustable beta shield and is attached to the rate meter by a 3-ft length of coax cable.

The count rate meter (Q-2091) is of the duty-cycle, linear-scale type. It includes an amplifier designed to accept the G-M beta-gamma tube input. A high-voltage power supply, a high-level alarm circuit, an aural monitor with volume control, and a 1-ma full-scale output for recorder or telemeter are included features. The unit weighs 19 lb and is enclosed in a cabinet approximately 8 in. wide, 9 in. high, and 12 in. deep. It operates from 115 v, 60 hertz ac.

# Performance Specifications

Performance specifications are given below.

Input sensitivity 200 mv

Circuit linearity 2.5%; overall accuracy, including drift, 5%

Amplifier gain control None

High voltage 900 ± 150 v, corona-regulated, 20 μa

Range selector 250, 1000, 2500, 10,000, and 25,000 counts/min

Integrator time constants 1, 11, and 21 sec

Alarm Adjustable, zero to full scale on any range for high level only, manual reset

0 to 1 ma output, 50,000-ohm impedance

Aural monitor Gated relaxation oscillator and power amplifier with volume control

# 2.9.3.3 Hand-and-Foot Beta-Gamma Monitor, Q-1939-B

The hand-and-foot monitor is located in an area which serves as the main entrance and exit from the reactor building (7503).

This instrument is an ac-powered four-channel monitor for beta-gamma radiation with a channel for each hand, a channel for the shoes (feet), and a channel with a movable probe. The probe is mounted approximately waist high in order to monitor the front of clothes when not used for special monitoring. Three channels are identical modular-constructed units, actuated by a halogen-quenched stainless-wall G-M tube. The counting rate is indicated by glow transfer scler tubes and electrical reset registers. The fourth channel, the survey probe, is an aural channel. The count in this channel is not totalized. Maximum counting rate in the probe channel is approximately 5000 counts/sec. To start the instrument, a manual push button is depressed which energizes a timer, after which the operation is automatic. The instrument resets itself, and there is a 5-sec waiting period before the counting cycle starts, to give the user

![](images/479b4ca32cf15c50f08309543fbab15b4d2c21a0722c24f095fa459a8676400c.jpg)

time to get both hands in position for monitoring. The actual counting period is 23 sec. The total cycle is 30 sec. The maximum count rate per channel is approximately 250 counts/sec, and the input resolving time per channel is approximately 200 μsec. The instrument is contained in a rack cabinet 68-3/8 in. high, 21-1/16 in. wide, and 220 in. deep. A detachable base, 4 in. high, 18 in. long, and 21 in. wide, contains the foot-monitoring assembly. The power requirements are $115 \pm 10$ v, 60 hertz, 75 w, 0.7 amp. Operating temperature limits are 0 to $135^{\circ}$ F.

# 2.9.3.4 Beta and Alpha Sample Counters

The beta and alpha sample counters are located in the health physics counting room at the north end of the reactor building.

# Beta Sample Counting System, Q-2344-1

The Q-2344 beta counting system includes a Tracerlab end-window G-M tube mounted in a vertical lead shield (ORNL-Q-2089). The lead shield also contains a card sample holder. Attached to the shield is a pre-amplifier and cable. The preamplifier signal is transmitted via this cable to a decadeScaler containing the high-voltage power supply (ORNL-Q-2188-1). A timer is also included in this unit. The complete assembly is usually mounted on a table or a laboratory bench.

# Alpha Scintillation Counting System, Q-2345-1

This system uses a scintillation detector composed of a $2 \times 2$ NaI crystal and a 2-in. photomultiplier tube (ORNI-Q-2287). The tube and crystal are mounted in a housing which is attached to a smear or slide sample holder. The system uses a preamplifier and the combined power supply unit used for the beta sample counter (Q-2188). This system, like the beta system, is mounted on a table or a laboratory bench.

![](images/a507571cbf2c51b3eade1cbb15f6ab62f635c7273428843cce6c730a02c6c142.jpg)

![](images/51844a7d6d968889190ef7204c8691f8b09608a84d8d29ca40eff43e9447882d.jpg)

# LEGEND

MOBILUNI-0-240-1-REQD   
AIRMONITOR-Q-2240- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
-0-MONITORON-Q-1154--7-REQD  
CRM (BETA GAMMA)-Q-2091--B-RsQ'D   
HANOFOOORMONITOR-Q-1939-1-880D   
EVACUATION HORN.   
ALARM BEACON LIGHT. 15-REQD

![](images/295cb027c0fe0b44b10e2c53306be8a5dcc4611f111e4412cacd60cf07178796.jpg)  
Fig. 2.9.1. Location of Fixed Health Physics Monitoring Instruments.

# NOTES:

1. CENTRAL CONTROL AND ANNUNCIATOR PANEL
2. CONTROL PANEL FOR AUXILIARY CONTROL ROOM
NUCLEAR PANEL.   
2. SINGLE AUNUNCIATOR FOR ALL ALARMS IN MAIN CONTROL ROOM  
3. OUR MODEL 02217 PATE METER AU ALPHA PROBE:LOCATED IN NOT CHANGE HOUSES   
4. FOR INSTRUMENT JUNCTION BOX LOCATIONS AND METHODS OF THE DISEASES: RAPID-SCAN 55115, 57114, RADIATION ALARM SYSTEM

<table><tr><td>MOLLEA CONTROL PAUSE S·LAYOUT</td><td>DWG-A152</td></tr><tr><td>MOLLEA COORDIATE PAPER S·WIRE CHARGE</td><td>D-WIRE-CHARGE</td></tr><tr><td>BOLD, 750Hz RADIATION (CONTINUING) OUTPUTS</td><td>Q-750-4-1-6</td></tr><tr><td>M.W. INST. CONDUIT ROUTING</td><td>DKC-53116</td></tr><tr><td>M.P. INST. CONDUIT ROUTING</td><td>DKC-53112</td></tr><tr><td>REFERENCE DRAWINGS</td><td>DWG. NO.</td></tr><tr><td colspan="2">MOLLEN SALT REACTOR EXPERIMENTAL
RADIATION MONITORING INSTRUMENTS NO. 1903</td></tr><tr><td colspan="2">INSTRUMENT PLACEMENT PLOT
FIXED HEALTH PHYSICS INSTRUMENTS
RADIATION MONITORING SYSTEM</td></tr></table>

120794RH 083D3   

<table><tr><td colspan="2">UNITS ON DETERMINES UNLESS
SPECIFICATIONS DESPIRATES</td><td rowspan="3" colspan="3">OAK RIDGE NATIONAL LABORATORY
OPERATIONS ON
UNION CARBIDE NUCLEAR COMPANY
MISCELLANEOUS
OAK RIDGE, TENNESSEE</td></tr><tr><td colspan="2">PROPERTIES ±</td></tr><tr><td colspan="2">REMARKS ±</td></tr><tr><td colspan="2">AMOUNTS ±</td><td>UNITED
Q2T100011-03</td><td colspan="2">APPROVED</td></tr><tr><td colspan="2">SCALE: % ± 1.0°</td><td></td><td>D-HH-Z-40641</td><td>REV</td></tr></table>

![](images/623c22b9023ae6d8ef1bb81deb13d029bea2e92c3bf64b8483c49d73ae093b4c.jpg)  
Fig. 2.9.2. Instrument Panel and Health Physics Instruments Locations.

![](images/a6e66d43d0155d8634919e71334aab1dde66fc26bf80d5bdddee5f967672fb0a.jpg)

ORNL-DWG67-7830

![](images/a8696d6f69cdbd50f9f1f0b443e9455660e24cb467b70c3e99e9f88291b6d4df.jpg)  
Fig. 2.9.3. Functional Block Diagram of MSRE Health Physics Monitoring System.

![](images/2243335828dada49db113dda4cb2cd35b1d9a23da3e0f6ec2b64ae9a8aa0341d.jpg)

![](images/b4ebe9a04a1d5ac46eb3a88406d78ff9e86eb94b8056c1b01861846247796fb3.jpg)

![](images/baf7aa5b45aecdf81c85568a087b63db4ff9e3b3e0acc6c9a98bd512c03f65e1.jpg)

![](images/ba3dc76cc0cd6bf1f7906623df88fc2e0764c2a7c6b578312f2f317607ae81a0.jpg)

![](images/b04c3916fbb64a8177441c5ce0ad18ea446bac23ee1cf9f88335c36817585743.jpg)

![](images/9a2b114900ebf88d13fc660c6e0b3be961cce8d30801362b26717348d91f8ba7.jpg)  
Fig. 2.9.4. Electrical Schematic Diagram of Health Physics Monitoring System.

<table><tr><td>REFERENCE DRAWINGS</td><td>DWG. NO.</td></tr><tr><td colspan="2">### J.A. Russell Jr.</td></tr><tr><td colspan="2">FACILITY RADIATION &amp; CONTAMINATION
WARNING SYSTEM</td></tr><tr><td colspan="2">ELECTRICAL CONTROL SCHEMAIC</td></tr><tr><td colspan="2">INSTRUMENTATION AND CONTROLS DIVISION
OAK RIDGE NATIONAL LABORATORY
OPERATED BY
UNION CARBIDE NUCLEAR COMPANY</td></tr></table>

<table><tr><td>5</td><td colspan="3">Add Pwir. Cat. nos.</td><td>1221-46</td><td>YNE</td><td></td></tr><tr><td>4.1</td><td colspan="3">YFA contact moved to pick up AK-1</td><td>629-66</td><td>AK-2</td><td></td></tr><tr><td>3.1</td><td colspan="3">As built</td><td>346-46</td><td>AK-3</td><td></td></tr><tr><td>2.1</td><td>Add D-C Fall Alarm Mod. b1 w/ 0.5 m/s</td><td colspan="2">NO. 85-46</td><td>14</td><td>AK-4</td><td></td></tr><tr><td>1.1</td><td colspan="3">Add 35 ft 80 Hare, add 70 Beacon</td><td>4-2-5</td><td>AK-5</td><td></td></tr><tr><td>THQ</td><td colspan="3">REVISIONS</td><td>DATE</td><td>APPD</td><td>APPD</td></tr><tr><td>###</td><td>###</td><td>###</td><td>###</td><td>APPROVED</td><td></td><td>DATE</td></tr><tr><td>1.1</td><td>###</td><td>###</td><td>APPROVED</td><td>APPROVED</td><td></td><td>DATE</td></tr><tr><td>1.2</td><td>###</td><td>###</td><td>APPROVED</td><td>APPROVED</td><td></td><td>DATE</td></tr></table>

ORNL DWG. 67-7843

![](images/160fe1f703d015d1cb68cc46c12187c47953d5c56c061e18b840618f7f6fb88c.jpg)  
Fig. 2.9.5. Central Alarm Panel Wiring Diagram.

![](images/30c9f59523ee6b0a7c4491dffb9dd1a00fd746b5ecc4115ed59854cf41a1269d.jpg)  
Fig. 2.9.6. Indicator Module.

![](images/f7e1be0911e94fab3f69d87b0c1369237f8c8c8102ec8233b9b7825d5fc669cd.jpg)

ORNL-DWG 67-7831

![](images/f46ea51052b2c1344dafa3ea5fdf86dd9493f10a6bee5c4f501b484a0fe5175a.jpg)  
Fig. 2.9.7. Coincidence Module Circuit Diagram.

ORNL DWG. 67-7832

![](images/b83701484991daa2fb024cd434567c460203cb75d7b0ef0f69ceb3b2704a15e8.jpg)  
Fig. 2.9.8. Buzzer Module Circuit Diagram.

![](images/8b688b6457816ce2057ad47a1cbe8d778ef721dd805a0cf0b36a330b19230aa7.jpg)  
Fig. 2.9.9. Air Whistle Schematic Diagram.

# 2.10 PROCESS RADIATION MONITORS

# 2.10.1 Introduction

The process radiation monitoring system monitors radioactivity levels in process pipelines, vessels, and operating components. This system is distinct from the Health Physics Monitoring System, Sect. 2.9, which is designed to warn personnel throughout the reactor area. Signals from the process monitoring system detectors located on or near pipes and components are used to produce alarm control signals and safety system input signals when activity levels indicate abnormal conditions. These monitors also provide information which indicates operating conditions of various parts of the reactor system.

# 2.10.2 System Description

Two kinds of detectors are used in the process monitors, ion chambers and Geiger-Mueller (G-M) tubes. The G-M tubes are used to monitor levels up to 100 mr/hr. Three types of ion chambers are used. One is a standard, commercial Reuter-Stokes chamber (Fig. 2.10.1) used to cover a range of 30 mr/hr to 300 r/hr. The second (Fig. 2.10.2) is an ORNL model Q-2818 and is used to cover a range of 100 mr/hr to $5 \times 10^{4} \mathrm{r/hr}$ . The third (Fig. 2.10.3) is a special high-level ion chamber used to cover a range of $10^{3}$ to $10^{7} \mathrm{r/hr}$ . This chamber is of special design to withstand the high radiation intensity and temperature present in the reactor and drain-tank cells during reactor power operation. It also has mineral-insulated cables sheathed with stainless steel to satisfy the cell containment requirements.

A typical G-M tube monitoring channel consists of an Anton 106C G-M tube supplying the input signal to an ORNL model Q-1916 logarithmic response gamma radiation monitor. This model Q-1916 instrument was developed to meet the requirements of most gamma radiation monitoring of reactors and in-pile loop systems. It has been in use at ORNL since 1958. The G-M tube (Fig. 2.10.4) is enclosed in a stainless steel housing less than 1 in. in diameter and 8 in. long, and it can be located up to 500 ft from the electronics. No preamplifier is used. The scale indication on the monitor is proportional to the logarithm of the radiation level over a three-decade span. Full-scale indication is normally 100 mr/hr, but it can be increased to 1 r/hr by use of a different G-M tube and by appropriate changes in the electronics. While the unit has a normal range of 100 mr/hr, it can handle levels in excess of 100 r/hr without impairing its alarm and control functions. The monitor provides an upscale electronic alarm. The alarm level may be set at any point over the readout range, and the alarm point may be read on the meter while the setting is being made without tripping the alarm circuit. A relay which is energized during normal in-limit operation provides the alarm and control signals.

Figure 2.10.5 is a block diagram of a typical Q-1916 monitor, with circuit details shown in Fig. 2.10.6. The G-M tube detector is operated at $900\mathrm{~V}$ , and the radiation level indicated is determined from the average current through the tube rather than from the pulse rate. Radiation intensity causes the tube to conduct. The voltage drop across a resistor in series with the G-M tube provides the input signal to the averaging filter. The filter's output, an analog signal, is fed to a dc amplifier having a logarithmic response. The amplifier is used to drive the alarm limit detector, panel meter, and recorder. The alarm limit detector drives a DPDT relay which is used for alarm and control signals.

The monitor is fabricated using modular construction; the Q-1916 monitor assembly contains three plug-in modules (Fig. 2.10.7), each of which is a complete monitor. A single power supply (Fig. 2.10.8) for all three modules is located along the back of the chassis. A single-channel unit with integral power supply is also available. The Q-1916 monitor was chosen because of its operating simplicity, availability, small detector size, ease of monitor replacement, fast response, and fail-safe features.

An E-H Research Laboratories model 202 electrometer is used to measure and indicate the signal produced by the ion chambers. This electrometer incorporates a 5889 low-leakage input tube and double feedback. Negative feedback reduces the effect of cable and source capacitance, thereby improving transient response; positive feedback reduces the input capacitance at low frequencies and further extends electrometer response. The seven input resistors from $10^{6}$ ohms to $3 \times 10^{12}$ ohms, selectable in seven steps, provide a wide operating range. The electrometer has an adjustable alarm set point on the front-panel meter. An alarm reset button is provided to reset the instrument after an alarmed condition has cleared. It contains a DPDT relay to provide alarm and control signals and it produces an output signal scaled to drive a 0-to-10-mv recorder. A 150-v power supply is provided for chamber polarization. Figures 2.10.9 and 2.10.10 are a front panel view of the electrometer and the circuit schematic respectively.

Excluding the Chemical Processing Plant a total of 16 G-M tube monitors and 12 ion chamber detectors are used for process monitoring at the MSRE. A list of these monitors, their function, and their location is shown in Table 2.10.1.

The column in Table 2.10.1 labeled "Number of Units and Type of Coincidence Circuit" describes the number of complete monitor channels at one location and how they are used to increase reliability. In a one-of-two circuit, either monitor reaching the alarm set point initiates the desired alarm or control action. If either monitor fails, the other unit is still available to monitor the system and produce the required action should it be required. With but one exception a failure of the monitor power supply produces control and alarm signals as does any other failure which causes the monitor response to appear like that caused by a high radioactive level (see sect. 1.5). The one-of-two system is used in those applications where the output control action can be tolerated during an on-line test.

In the two-out-of-three coincidence systems, two monitors are required to produce an alarm or control action. This arrangement allows

Table 2.10.1.   

<table><tr><td rowspan="2">Process or Component Monitored</td><td rowspan="2">Instrument No.</td><td rowspan="2">Detector</td><td rowspan="2">Detector Locationa</td><td colspan="2">Radiation Level</td><td rowspan="2">Number of Units and Type of Coincidence Circuit</td><td rowspan="2">Control or Alarm Functionb</td><td rowspan="2">Monitoring Function</td></tr><tr><td>Background</td><td>Alarm Set Point</td></tr><tr><td>Fuel pump bubbler inlet lines</td><td>RE-596A, B, C</td><td>G-M tube</td><td>East of transmitter room at 840-ft level</td><td>&lt; 7 mr/hr</td><td>20 mr/hr</td><td>3 Two of three</td><td>Alarm; close bubbler inlet valves</td><td>To prevent fission gas backup in fuel pump and pump over-flow tank bubbler helium supply lines and ensure containment validity</td></tr><tr><td>Coolant pump sweep gas</td><td>RE-528B, C</td><td>G-M tube</td><td>Vent house</td><td>&lt; 7 mr/hrc</td><td>20 mr/hr</td><td>2 One of two</td><td>Alarm; emergency fuel drain; fuel pump off</td><td>To monitor coolant salt for fuel in leakage through break in heat exchanger</td></tr><tr><td>Helium supply line</td><td>RE-500D</td><td>G-M tube</td><td>Water room</td><td>&lt; 5 mr/hr</td><td>20 mr/hr</td><td>1 One of one</td><td>Alarm only</td><td>To monitor for fission gas backup in helium supply header</td></tr><tr><td>Fuel sample box exhaust</td><td>RE-675A, B</td><td>G-M tube</td><td>High bay</td><td>&lt; 7 mr/hrc</td><td>10 mr/hr</td><td>2 One of two</td><td>Alarm; close valves in line to filter pit</td><td>To indicate and control amount of fission gas going to stack</td></tr><tr><td>Fuel pump oil tank</td><td>RE-OT1B</td><td>G-M tube</td><td>Service tunnel</td><td>&lt; 7 mr/hr</td><td>20 mr/hr</td><td>1 One of one</td><td>Alarm only</td><td>To indicate activity buildup in oil</td></tr><tr><td>Coolant pump oil tank</td><td>RE-OT2B</td><td>G-M tube</td><td>Service tunnel</td><td>&lt; 7 mr/hr</td><td>20 mr/hr</td><td>1 One of one</td><td>Alarm only</td><td>To indicate activity buildup in oil</td></tr><tr><td>Reactor cell containment air</td><td>RE-565B, C</td><td>G-M tube</td><td>Vent house</td><td>&lt; 7 mr/hrc</td><td>20 mr/hr</td><td>2 One of two</td><td>Alarm; emergency fuel drain; close valve HCV-565Al</td><td>To indicate fuel leak into containment area and prevent excessive amounts from discharging to stack</td></tr><tr><td>Off-gas sampler</td><td>RE-52A, 52B</td><td>G-M tube</td><td>Sampler box at vent house</td><td>&lt; 7 mr/hr</td><td>100 mr/hr</td><td>2 One of two</td><td>Alarm only</td><td>To indicate leaks in the off-gas sampler system</td></tr><tr><td>Charcoal bed discharge</td><td>RE-557A, B</td><td>G-M tube</td><td>Vent house</td><td>&lt; 7 mr/hrc</td><td>20 mr/hr</td><td>2 One of two</td><td>Alarm; close fuel and coolant system vent valves; close off-gas vent valve</td><td>To check operation of charcoal filters and prevent excess activity discharge to stack and pump lube oil systems</td></tr><tr><td>Fuel sampler vacuum line</td><td>RE-678C, D</td><td>Ion chamber</td><td>High bay</td><td>&lt; 7 mr/hrc</td><td>25 r/hr</td><td>2 One of two</td><td>Alarm only</td><td>To indicate when sample exchange area is free of fission gas</td></tr><tr><td>Reactor cell space coolers 1 and 2, drain-tank cell space cooler, and fuel pump coolant water return line header</td><td>RE-827A, B, C</td><td>Ion chamber</td><td>Blower house</td><td>&lt; 5 mr/hrc</td><td>50 mr/hr</td><td>3 Two of three</td><td>Alarm; close valves in water supply lines</td><td>To indicate break in the water lines in the cells and prevent activity from escaping the containment area</td></tr><tr><td>Reactor cell</td><td>RE-6000-1, 2, 3</td><td>Ion chamber</td><td>Reactor cell</td><td></td><td></td><td>3 No alarm circuit</td><td>Indication only</td><td>Indicate operating levels in the cell</td></tr><tr><td>Drain-tank cell</td><td>RE-6000-4, 5, 6</td><td>Ion chamber</td><td>Drain-tank cell</td><td></td><td></td><td>3 No alarm circuit</td><td>Indication only</td><td>Indicate operating levels in the cell</td></tr><tr><td>Radiator pit</td><td>RE-6010</td><td>Ion chamber</td><td>Radiator pit</td><td></td><td></td><td>1 No alarm circuit</td><td>Indication only</td><td>Indicate operating levels in the radiator pit</td></tr></table>

See Dwgs. E-HH-A-55588 and D-HH-B-41668.   
bSee instrument flow diagrams for controlled element.   
After shielding detector.

the monitors to be tested, channel by channel, without actuating the final alarm and control or safety circuits. Each monitoring channel can be tested completely up to and including the alarm light and the alarm and control relay in the module. The two-out-of-three coincidence arrangement is used where maintenance and on-line testing of any single channel must be accomplished without producing control action and where false output control action caused by a failure or malfunction of a single channel is highly undesirable.

All the detectors, except the high-level ones in the reactor and drain-tank cells and the radiator pit, are capable of being tested with a radiation source. A $^{60}\mathrm{Co}$ source is used to test each location.

In areas where substantial background radiation exists, the low-level detectors are provided with lead shields (Fig. 2.10.11). Shielding reduces the background and improves the signal-to-noise ratio, thus preventing spurious alarms from a rise in activity level at another location. These shields consist of lead sheet formed into the required shape or of concentric lead-filled pipes. The shields are designed<sup>2</sup> to facilitate the replacement of detectors and are built with access holes to accept a radiation source for calibrating and testing the monitors.

No shields or test sources are provided for the high-level ion chambers since their operating range is in the neighborhood of $10^{5}$ r/hr. The high-level chambers are mounted at selected locations in the reactor and drain-tank cells. Three chambers are located near the wall of the reactor cell, one at elevation 844.5 ft, one at elevation 838.5 ft, and one directly over the reactor to measure control rod drive dose. Two of the three chambers in the drain-tank cells are mounted on the walls, and a third is mounted between the two fuel tanks on the thermocouple tray.

The chambers are filled with nitrogen, employ alumina insulators, and are built with mineral-insulated signal and high-voltage cables. The chamber is 7-7/8 in. long and 1-1/16 in. in diameter. The chamber sensitivity is $4 \times 10^{-13}$ amp r $^{-1}$ hr; 98% saturation is obtained in a field of $10^{7}$ r/hr with 350 v applied.

Only one chamber is monitored at a time. This is done by using a single electrometer and a six-position selector switch. The selector switch connects the signal from any selected chamber to the electrometer. Two high-voltage power supplies are used, each supplying 350 v to three chambers.

All the process monitoring electronic instruments except those used with the sampler-enricher system and the pump lube oil tanks are mounted in nuclear boards 4 and 5. The other detectors are mounted in panels associated with their respective systems. To obtain the required reliability for the monitoring system, the ac input power to the monitors is obtained from the 25-kva emergency power system. In addition, in the

Process line detector shields, ORNL Reactor Division Drawings D-HH-B-41527, 41528, 40551, and 40552.

Nuclear control board panels 4 and 5 layout, ORNL Reactor Division Drawings D-HH-A-41532 and 41533.

one-out-of-two monitor system, each channel has its own separate power bus, providing added operating reliability.

With the exception of the six high-level, in-cell monitors, all monitor outputs are transmitted to the data system for alarm detection and logging. Each monitor is provided with an individual alarm indication. In addition, the alarm signal from each monitor station is transmitted to annihilators in the auxiliary control room. These annihilator signals are interconnected and transmitted to a single annihilator in the main control room, labeled "Process Radiation Monitors."

![](images/5a4fea86b8a8b9e9eb3756369e209ec87a96adcafb67c14bd194836cdd7bfa51.jpg)  
Fig. 2.10.1. Reuter-Stokes Standard Ion Chamber.

![](images/a48ca735bcd0985635b3da78d7e439801921a522923d89403ea5d8f898843e6e.jpg)  
Fig. 2.10.2. ORNL Model Q-2818 Ion Chamber.

![](images/3a4094575ed8fec215bb68689b148286bbd5bfa4d57d6a4bfbe6cf223781a671.jpg)  
Fig. 2.10.3. MSRE Special High-Level Gamma Ion Chamber.

![](images/a8260b1d3ebce73333e16f24f513016acf56521a25337b38cb912c07337a21b6.jpg)  
Fig. 2.10.4. G-M Tube Assembly.

Fig. 2.10.5. Block Diagram of Q-1916 Radiation Monitor.   
![](images/f97334da2cd41dafc86cefa44e51a6bf745c4496c4341ae86b9f4a34a6dd494f.jpg)  
ORNL-LR-DWG 31166AR

NOTES   
![](images/b729bd287d44e85e765f2013bd5d23172c57d7a3ce80a9b437a8837c1eb18003.jpg)  
(1) All resistors 1 with 100 mH resistor. All resistors $5^{\circ}$ are set as noted. Be denoted Steamp caten filn resistor. TI denotes Texr Instrument Co. carbof filn resistor.   
(2) After the following instructions, we are all satisfied by the sample, adjust the voltage on the upper end of the "volcanic" rod to 30 mV with respect to group. This means that we can use a capital or differential voltage meter   
(3) With the "Catalyst" control, 1), up to used, adjust the "Catalyst" set to: $0.5\mathrm{MPa} / \mathrm{HF}$ for t1, 100 MPa or 3.0 MPa for the 1000 MPa control.   
(4) For instruments, the input letter worked to 100 MPW/ft, apply a 3 cent. precision to the input and set the value equal yet. R20a to write a letter reading of 30 MPW/ft. For instruments, starting with 100 MPW, apply a 3 volt min. precision to the input and set the value equal yet. R20a to write a letter reading of 300 MPW/ft.   
(5) Rernt (3) 4.0

![](images/2c6290d2a679104e2f0f985e000b3615443c9ea6c4445348a3247cc2be440ea7.jpg)  
NOTE: This reproduced transparency of I & C Dwq.: Q-19/6-1 was made of Rev. 5 (Current as of April 65) For M.S.R.E.ONLY.

Poward Panel   
![](images/e90037c16e2d17a79e0c960fe675bde4c09795e370d2108e6175636e52ced3df.jpg)  
Material: Epoxy fiber gloss, MIL-14077 grove SEE, g'g drilled with #33 (1/3) holes spaced 2. Mount Q-900-151 def.  
split terminal lugs with slots at 90° with long axis of term. bd in all holes except those marked 8.  
@ Enlargge with #27 (144) drill and mount stubs Q900-142 def.

![](images/b42f3ef31e89b75ff4754c562f4435eb2ade382ab288162cd43cccdc9969a991.jpg)

![](images/fb315fc9e1a289e53f34a68da98d4df43aa77e8f5f8e2c02b239ef7fc6b4d892.jpg)  
Fig. 2.10.6. Radiation Monitor Single-Module Circuit.

![](images/f8df55ce685e7827da9409b7f7d219ea24510b3034be5dec1de90e1766078f35.jpg)  
Fig. 2.10.7. Three-Module Q-1916 Radiation Monitor.

![](images/5646bdc6013eed5c41addfb94026eaedbcd9a604c82f07ae930ea63f7d793f3f.jpg)  
C   
Fig. 2.10.8. Three-Module Radiation Monitor.

![](images/3d3fb167c588e6cfd78d322254665a486503600fe0e03698e9ed5b525f48a035.jpg)  
Fig. 2.10.9. E-H Research Laboratories Model 202 Electrometer.

![](images/5a460af8d9be58fcd96b0f1a108b5d83b30c0f30e7502d955602da66cbe26e9c.jpg)

![](images/fbc2c6cff25d7134625ccf39a2a78d6776abd8137bf5c6c25595ca0389eb48dc.jpg)  
C   
Fig. 2.10.10. Electrometer Model 202 Circuit.

![](images/972838360439efdca09d3d707c955a411d9e5885206b1e255306331ffe3c1554.jpg)  
Fig. 2.10.11. Typical Process Monitor Lead Shield.

# 2.11 STACK MONITORING SYSTEM

# 2.11.1 Introduction

The MSRE stack monitoring system monitors the MSRE off-gas for abnormally high radiation levels in the 100-ft-high off-gas stack. The level of activity of the gas emitted from the stack is recorded on instruments located in the reactor auxiliary control room and by the computer data logger. Abnormally high levels of activity generate an aural and visual alarm in the reactor control room and in the Laboratory Waste Monitoring Control Center located in Building 3105.

All hot-cell ventilation, some building ventilation, and all waste gas (off-gas from process vessels and experiments) at ORNL are monitored and discharged through one of several stacks. This section describes the principal features of the MSRE stack monitoring system. This stack is the main disposal facility for gaseous waste at the MSRE. Cell ventilation air (high flow, low contamination) makes up the bulk of the air flow; reactor off-gas (low flow, high contamination) is also disposed through this facility. Filtering equipment consisting of multilayer fiber glass roughing and absolute filters (see Fig. 1.5.10) is also located near the stack. These filters are, in general, a second line of defense, since all air and gas is cleaned near its source by the use of particle traps and charcoal beds before entering the roughing filters.

All continuous waste effluent monitoring systems at ORNL feed information to panelboards at the Waste Monitoring Control Center located in Building 3105.² The information is displayed by signal lights indicating alarm conditions or by records on single-point or multipoint strip-chart recorders.

# 2.11.2 System Description

The basic concept of stack monitoring installations divides the channels of information into two functional parts. One part provides day-to-day information necessary to arrive at monthly and quarterly inventories of radionuclides emitted from the stack. The other part provides a continuous surveillance of the minute-to-minute condition of the stack inventory in order to sound an alarm if an unusual burst of activity occurs.

The function of this second part of the system, in addition to providing an early warning of unusual conditions, is to provide gross information about the incident useful in locating the source and in assisting all emergency groups involved to evaluate the extent of the incident. At present there are five channels of information available from the MSRE stack to meet these requirements. All the primary instrumentation for

these channels is located on a balcony 40 ft up the stack, with the indicating instruments located in the reactor building (Fig. 2.11.1). These information channels are given below.

# 2.11.2.1 Flow Channel FT-S1

A Pitot tube in the stack at the 40-ft level continuously measures the total flow of air in the stack (approximately 18,000 cfm). This measurement provides surveillance to detect unusual changes in air flow. The flow data are also required, to calculate the average concentrations of material passing through the stack. The stack flow rate is recorded by the data-logger and printed on the hourly log.

# 2.11.2.2 In-Stack Sampler

An in-stack sampler is located at the 40-ft level. This sampler collects a sample from the air stream by means of a cartridge with an integral filter and a charcoal trap (Fig. 2.11.2). Isokinetic sampling is attempted, and the cartridge is removed once a day routinely for counting room analysis and would be removed and replaced as often as necessary during an incident or any unusual situation.

# 2.11.2.3 Particulate Monitors

# Beta-Gamma Monitor, RE-S1A

A sample is continuously withdrawn from the stack stream at the 40-ft level and passed through a filter paper which is monitored by a G-M tube. The buildup of beta-gamma-emitting particulates provides the first clue as to the physical form and characteristic radiation of contamination. Exit gas from this monitor is sent to the $^{131}\mathrm{I}$ monitor (refer to 2.11.2.4 below).

# Alpha Monitor, RE-S1B

A similar device monitors the stack stream for alpha activity. Exit gas from the alpha monitor is returned to the stack.

# 2.11.2.4 Iodine Monitor, RE-S1C (Fig. 2.11.3)

After passing through the paper filter of the beta-gamma monitor (Sect. 2.11.2.3), the gaseous sample passes through a charcoal trap at ambient temperature; here it is monitored by G-M tubes. The charcoal bed receives the sample free of particulates and detects iodine and other materials, such as tellurium, in volatile gaseous form. These gases are poorly trapped by the preceding filter; $^{131}\mathrm{I}$ is the contaminant usually detected, thus explaining the name, iodine monitor. A second clue as to the physical form and identification of stack gas material is, therefore, provided by this channel.

A sample of stack air is constantly pumped through the beta-gamma monitor RE-SIA at 2 cfm by a Roots blower. A 2-1/2- by 1-in. section

of filter-paper tape catches better than $90\%$ of the particulate matter of greater than $0.3\mu$ size which passes, and any radiation of sufficient energy is detected by a G-M tube. The paper used is Whatman No. 4 and is in rolls 3 in. wide and 145 ft long. No regulation of air flow is provided. Since the filter is changed at least every 8 hr, the air flow remains reasonably constant at the blower-rated flow of 2 cfm. A pressure switch in the intake air line is held closed during operation and sounds an alarm in Building 3105 if there is a blower failure. The sample is collected inside a stainless steel shield that provides approximately 2 in. of metal in all directions except where an opening is necessary to admit air and tape. A mica end-window G-M tube (Lionel Electronic Laboratories type 21OT) is used as the detector. Window thickness is 1.4 to $2\mathrm{mg/cm}^2$ nominal and will pass beta particles of energies down to 35 kev. Since stack gas may contain practically any isotope, good energy sensitivity is required.

Details of the assembled filter, detector, and shield are on Instrumentation and Controls Division Dwg. Q-2325-5. The design of this assembly allows the filter tape to be advanced by a 24-v dc signal from the control center in Building 3105 and also includes broken tape detection before and after the shield. If the filter-paper tape breaks or runs out, it cannot be advanced, and an alarm signal is sounded in Building 3105. A method of calibration is described in ref. 3. The tape assembly is based on the ORNL Q-2118 design used in the standard Q-2240 constant air monitors except that the intake portion has been altered to allow easier disassembly for decontamination (see Instrumentation and Controls Division Dwg. Q-2218-1 for details). Also, the air intake diameter has been altered to match the sample probe and to reduce the number of diameter changes in the sampling line.

At the time of installation, isokinetic sampling conditions were approximated by estimating the flow, assuming 2-cfm sample volume and sizing the sample pipe accordingly. In addition, the end of the pipe was sharpened, placed close to the center of the stack, and headed into the air stream. The number of degrees of turn between the pipe entry and the filter were minimized, and all pipe bends were at the maximum allowable radius. All piping is of stainless steel except for a small section of plastic tubing where flexibility is needed. The sample is taken approximately ten diameters downstream from the input to the stack.

The G-M tube is connected with RG59/U coaxial directly to the indicating instrument located in Building 7503. The cable runs are in conduit, and lengths are typically 100 to 250 ft. The indicating instrument (RI-SIA) is a Q-2313 count rate meter with a current-sensitive input and is located in nuclear panel board 5 (NB5) in the auxiliary control room. The current-sensitive input allows the signal and high voltage for the G-M tube to be put on the coaxial cable without using preamplifier at the G-M tube. The count-rate meter chassis also holds the +HV supply, an audio output, a Rustrak recorder, and a panel meter. Range and time constant switchings are manual. The count-rate meter ranges are 0-250,

0-500, 0-10,000, and 0-25,000 counts/min. Damping time constants are 1, 11, and 22 sec. In addition to display by the rate meter and recorder, the beta-gamma level is also checked for alarms recorded by the computer-logger and output once a shift on the 8-hr log. The signal to the logger is 0 to 10 mv and is obtained from the output of the ratemeter.

The alpha monitor (RI-S1B) is similar to the beta-gamma particulate monitor. The stack-gas sample is withdrawn by means of a separate sample pipe at the 40-ft level. The 2-cfm sample is drawn through a filter tape deck, as with the beta-gamma monitor, by a Roots blower. In this monitor, however, the radiation detector is a thallium-actuated zinc sulfide screen (see Instrumentation and Controls Division Dwg. Q-2218-5 for details). The area viewed is 1-5/8-in. in diameter (2 in.²), and the detector is on the top (intake) side of the filter tape to avoid absorption of alpha particles by the filter paper. No shielding is necessary owing to the low sensitivity of the screen to beta-gamma radiation. The indicating instrument, a Q-2313 count rate meter labeled RE-S1B, is located in the same panel as the beta-gamma rate meter. The alpha level is also monitored for alarm condition, recorded by the logger-computer, and output on the 8-hr log.

After leaving the beta-gamma particulate monitor, the gas is passed through the model Q-2725 iodine monitor detector RE-S1C (Fig. 2.11.3) and returned to the stack. A charcoal trap, made of a disposable plastic bottle and containing 6-l4 mesh coconut charcoal about 3 in. in depth, is used to trap $^{131}\mathrm{I}$ (and other materials such as tellurium that adsorb on charcoal). The trap, placed within a standard 2-in.-thick lead shield (Q-1907-15), is monitored by four Lionel 106C G-M tubes. The air flow is 2 cfm, and the measured cross-sectional flow area of the charcoal bed is 5.41 in. $^{2}$ . From curves given in ORNL-2872, the pressure drop is approximated at 2 in. $\mathrm{H}_2\mathrm{O}$ or less, and the air velocity is 55 bpm. The decontamination factor is estimated from the above report to be $10^{3}$ or better. As a rough rule of thumb, 6-l4 mesh charcoal will collect $90\%$ of $^{131}\mathrm{I}$ per inch, so that the high concentration is at the upstream face of the charcoal. Data presented in the report are for velocities of 200 bpm and less. Actually the charcoal is easily recoverable and can be used for analysis since the trap is easily replaced. When sensitivity is too great, the number of G-M tubes can be reduced. About 75 g of charcoal is used in each trap.

The output of the G-M tubes (operated in parallel) is connected by RG59/U coaxial cable to the input of a Q-2313 count-rate meter (RI-S1C) located in NB5 in the auxiliary control room. The 10-mv output of the rate meter is transmitted to the data-logger, which prints out the iodine level on the 8-hr log.

The collected material is monitored by a halogen-filled G-M tube (Lionel 106C) which has a $30\mathrm{-mg/cm^2}$ wall that excludes all beta energies below about 300 kev. The G-M tube also sees inert and volatile gases which are not collected by the filter paper. These show as only a rise in count rate on the recorder for the time of their passage through the monitor. Iodine-13l will collect on the filter paper but with very low efficiency, depending on the stack conditions and the physical form of the iodine.

Inert gas such as $^{85}\mathrm{Kr}$ will be seen in both the particulate and $^{131}\mathrm{I}$ channels for the duration of its presence in the stack flow. It

will not collect to any extent on the filter or the charcoal. While some adsorption on the charcoal has been noted, collection and retention are very poor at ambient temperatures.

As can be seen, particulate matter is immediately identifiable since it is collected by the beta-gamma monitor filter before it reaches the iodine monitor.

Iodine-131 will cause a long-term (8-day half-life) buildup on the charcoal; inert gas can be identified since it shows on both channels in a transient rather than an integrated manner.

As stated previously, the indicating instruments for the stack monitors are located in NB5 in the auxiliary control room (Fig. 2.11.1). The indicating instruments consist of the three rate meters with the integral recorders for the three monitor channels, beta-gamma, alpha, and iodine, plus the alarm detection and display circuitry for the three channels. The alarm detection equipment provides a local annunciation of the alarm from any of the detection channels and transmits the alarm signal to the Waste Monitoring Control Center in Building 3105. Figure 2.11.4 is the functional block diagram of the system.

The alarm-detection equipment consists of three transistorized switches which operate two alarm relays, a buzzer, and a lamp, all powered by a 24-v dc power supply. The equipment, except for the power supply, is mounted on modular cards located in an integral panel (Fig. 2.11.5). The modular card panels are slightly modified, but the circuits are identical with those used in the Health Physics Monitoring System (Sect. 2.9). The three alarm switches are actuated from signals derived from the three rate meters. See Fig. 2.9.6, Sect. 2.9, for a schematic of the switch circuit. Any channel in an alarmed condition will cause the appropriate alarm switch to trip, which turns the alarm lamp "On" on the switch, turns on a local buzzer (Fig. 2.9.8, Sect. 2.9), actuates a local annunciator, turns on a local alarm lamp, and actuates a relay all through the action of the alarm module (Fig. 2.9.7, Sect. 2.9), which also trips the stack monitor alarm in the Waste Monitoring Control Center also. The alarm for each channel is set by the contact meter on each rate meter. Once a channel is in the alarmed state, the alarm will continue until the signal has decreased below the alarm set point, the individual alarm switch is reset, and the common buzzer is reset. There is an additional module, called the remote alarm relay module (Fig. 2.11.5), which trips an annunciator in the main control room should the 24-v dc power supply fail. See the ORNL Q-2563 series of drawings listed in Sect. 2.11.3 for details on the transistorized alarm circuitry. See Fig. 2.11.6 for the operational schematic and elementary diagram of the beta-gamma, alpha, and iodine monitors.

2.11.3 ORNL Drawing List for the MSRE Stack Monitoring System

Q-2370-1 - Stack Sampler Location and Control Alarm Panel Assembly

Q-2370-2 - Functional Block Diagram

Q-2370-3 - Operational Block Diagram

Q-2370-4 - Power Wiring at Stack

Q-2370-5 - Interconnection Diagram

Q-2370-6 - Alarm Panels Rear View Wiring

Q-2370-7 - Beta-Gamma Monitor, Operational Schematic and Elementary Diagram

Q-2370-8 - In-Stack Sampler Assembly

Q-2370-9 - In-Stack Sampler Details

Q-2370-10 - In-Stack Sampler Probe Details

Q-2370-13 - Tape Deck Cabinet Assembly and Details

Q-2370-14 - Sampling Cabinet Assembly and Details

Q-2563-lA - Hi-Level Module, Schematic

Q-2563-2A - Alarm Module, Schematic

Q-2563-4C - Reset Module, Schematic

Q-2563-19B - Remote Alarm Relay, Schematic

Q-2328-13 - Alpha Monitor

Q-2325-5 - Filter and Shield

Q-2313-15 - Countrate Meter Schematic

Q-2218-5 - Iodine Detector

Q-2118 - Tape Assembly

![](images/13d65745c4c41a86764c16c352dff013d9099e19bf12cbb3ae54c88ad1df40f8.jpg)

![](images/f743b74858ceee072475bb2c89749080c169f23780334a8f90341ae0942e9d0f.jpg)

![](images/3fd3a911cfb5cbdc23a03ca7d9555e09651e4fa4c3f2e7d181eb0965ccb1cb05.jpg)

![](images/7be87adedd684b281e15b2dcc5b6a2321fae7a1f8bf39ad9588f3b4d6ac498bd.jpg)

<table><tr><td>c</td><td colspan="4">Add 24V Power Failure Mod 1-10</td><td>63-64</td><td>116</td><td></td></tr><tr><td>1</td><td colspan="4">As built</td><td>3-4-67</td><td>118</td><td></td></tr><tr><td>NO.</td><td colspan="4">REVISIONS</td><td>DATE</td><td>APPD</td><td>APPD</td></tr><tr><td>N.F.C.
####</td><td colspan="2">9-15-64</td><td>#########</td><td>####</td><td>#########</td><td></td><td>###</td></tr><tr><td>J.H.H</td><td colspan="2">####</td><td>#########</td><td>####</td><td>#########</td><td></td><td>###</td></tr><tr><td>J.H.H</td><td colspan="2">9-23-67</td><td>#########</td><td>####</td><td>#########</td><td></td><td>###</td></tr></table>

1.10V Nema W.P Pecap..Duples   
2.3 way switch   
3. Condulat " T   
4 - 115V. Lamp with globa guard   
3. CONDUT   
23704 for Wiring

![](images/84a888419b3775ed91eef5100cca027837ddec0692a31bcd392d61794e870a7d.jpg)

![](images/d6d3836e4852232288a1b4e93633147b1aa0fb46cb098d14ad276f20d56397f0.jpg)

![](images/0e408e2bc427ff7b383bc820fc9788ae23aee2df9ad590153f985dc2e66dba65.jpg)  
Fig. 2.11.1. MSRE Stack Monitoring System, Showing Stack Sampler Location and Central Alarm Panel Assembly.

Panel Cutouts for Bldg. 7503

Panel 58-01378-27 R4 1fum 3   
Pare 5D·Q1378-27 R4·1tem 20

<table><tr><td colspan="2">Nuclear Control Panel &quot;S- Datalayout&quot;</td><td>DHA-4135</td></tr><tr><td colspan="2">REFERENCE DRAWINGS</td><td>DWG NO.</td></tr><tr><td colspan="3">V.H. Halladay</td></tr><tr><td colspan="3">MSRE STACK MONITORING SYSTEM</td></tr><tr><td colspan="3">STACK SAMPLER LOCATION OF
CENTRAL ALARM PANEL ASSY.</td></tr><tr><td colspan="3">INSTRUMENTATION AND CONTROLS DIVISION
OAK RIDGE NATIONAL LABORATORY
OBSERVED BY
UNION CARBIDE NUCLEAR COMPANY</td></tr><tr><td>###</td><td>###</td><td>###</td></tr></table>

ORNL-DWG 67-696

![](images/73dc5bc1d448816c420f95f5a59d89ae0da2b232179174357589fe163214c378.jpg)

![](images/2917e42f536a5638442b1b68c6cac196679e7c5f9d588f3b7303b60c0d41a29e.jpg)

![](images/bde8dc5df0f42cfa95025eb85f7009d63f859a23b6e06c00bd3f4c171bbd349f.jpg)

![](images/66f201d5b2b3eaf77cd5e3c4abfc63961d5f13dd2c8f52a010b9ed4c9580ab84.jpg)

![](images/4edb05fd36dddae24f2779f0fe3b88c9e90fb089fbb56c4665d7243ee4981e1d.jpg)  
END PLUG

MAT'L. CUT TO PROPER WIDTH FROM 1-oz POLYETHYLENE BOTTLE, ORNL STORES ITEM NO.15-014-9602 2 REQ'D.

![](images/f78a34fe43699a8e0cabafac5938eb8c83b7ceab45bee28e19eb14432f0906f6.jpg)  
HOUSING

MATL. CELLULOID-MAKE FROM 32-mm O.D. CENTRIFuge TUBE ORNL STORES ITEM NO 15-242-2483 1REQ'D

![](images/6904d98d5a1e5a8f87564ff01f6d2fd3b295e7340621e29bbb5741cccd94e357.jpg)  
Fig. 2.11.2. Charcoal Cartridge for In-Stack Sampler.

STRAJNER

MAT'L 40-mesh SST SCREEN WIRE 2 REQ'D.

![](images/396862c22143e1b19c464bf44d3ce730850e8a89932f40d4b3a538ead9c29461.jpg)  
Fig. 2.11.3. Iodine Monitor Detector.

![](images/98e819f69cf26931939ff5afadcf8844e07be61ff2f868a277a1e41b5125a9be.jpg)  
Fig. 2.11.4. Functional Block Diagram of MSRE Stack Monitoring System.

0

#

#

![](images/62184d77ab285db9eb629bedb85bbb62ae932e69d0a81941742ccede83fd0ae8.jpg)

![](images/056a0017b7ec105b1787f2e40bff3996265702efec598855fe5a3950633175d8.jpg)  
C

![](images/3f95b3f9943117a59c2251725b0b59a1236ac9a22ff5cb8ad1fc4e745f3a7fdd.jpg)  
Etched Board - 19B Q2563-16C   
Fig. 2.11.5. Remote Alarm Relay Schematic.

![](images/c11a696021cf1adb2b920d00d97409932ef22947361607077360c391b3b17086.jpg)  
Fig. 2.11.6. Pump, Filter Tape Drive Control, and Alarm Panel Circuits.

# 2.12.1 Introduction

A digital data collecting and computing system is used on the MSRE to augment the conventional instrumentation system (Figs. 2.12.1 and 2.12.2). It is designed to collect and process 350 analog and 112 on-off contact signals (at present it processes only 291 analog signals). The remaining signals can be added by merely wiring in the signal leads and altering the system program. Signal processing includes conversion of the analog signals to digital values in engineering units; alarm monitoring by comparing the signals against preset upper and lower alarm limits; and calculations to provide heat balances, total power, reactivity, and other operational and analytical information. These digital values may be logged on typewriters, displayed by a digital lamp unit, or recorded on magnetic tape, at the system operator's option.

# 2.12.2 Basic System Equipment Description

The system consists of a Bunker-Ramo model 340 digital computer, operating console, analog and digital input-output cabinets, typewriters, x-y plotter, digital display lamp bank, and two magnetic tape units<sup>1</sup> (Fig. 2.12.3).

The analog input-output equipment is housed in three 23- by 84-in. cabinets (Fig. 2.12.4). These cabinets contain four dc amplifiers, an input signal multiplexer composed of mercury wetted contact relays, an analog-to-digital converter, a thermocouple reference unit, power supplies, and the input-output terminals with associated filters and signal conditioning circuits. The dc amplifiers and the converter were manufactured by the Redcor Corporation, Canoga Park, California. The analog signals from the process instruments are transmitted by signal leads to the first two cabinets, where they are scanned by the multiplexer, then amplified, digitized, and transmitted to the computer memory.

The analog input system is designed to handle analog input signals ranging from millivolts dc to 220 v dc or ac. The lower-level signals are amplified to 10 v dc, while the higher-level dc signals are attenuated to the 10-v range and ac signals are rectified before attenuation.

The analog input signals are transmitted to the input terminals and then through 60-cycle noise filters before reaching the input

multiplexer. These filters have a manually set variable 60-cycle rejection of from 6 to 50 db. They are mounted on plug-in cards in the two analog input cabinets. In addition, digital filtering (integration) is applied to selected input signals, most of which are thermocouple signals used in precise calculations. The analog-to-digital converter operates on a 0- to 10-v dc range. All analog signals are converted to digital values on this basis, with the proper scaling done under program control. Digital signals are compared with preset alarm limits and can be selectively transmitted to digital-to-analog converters to produce up to 36 analog signals for recorders, oscillographs, an x-y plotter, or for control.

Three cabinets, indicated as I/O Nos. 1 to 3 in Fig. 2.l2.4, house the digital input/output equipment. This equipment handles the contact input signals from relays, typewriters, and the input keyboard and contains the control units for all the output devices. The contact input signals are transmitted to the arithmetic and control unit of the computer to perform operations under computer program control. The digital output signals from the arithmetic and control unit are transmitted through the digital input-output unit to operate relays, typewriters, and the digital lamp display unit.

The computer consists of the basic digital computer, the master input/output control unit, and the memory units. The computer containing the basic electronics is housed in three labeled cabinets, central processor, core memory, and drum memory (Fig. 2.12.4). Input/output is housed in one cabinet labeled Master I/O.

The basic 340 computer has all-solid-state circuitry with the following specifications.

Core memory

12,288 words, expandable to 16,384, in blocks of 2048

Drum memory

28,672 words, expandable to 49,152, in blocks of 4096

Machine cycle time

6.0 msec

Data word length

28 bits including sign plus one parity bit on all memory operations

Instruction format

Two fields: a 14-bit operation field and a 14-bit operand field

Addressing

Direct addressing of up to 16,384 words, single level indirect, and immediate operand and addressing

Number system

2's complement binary

Operation

Arithmetic, control, and core memory circuits: parallel; magnetic drum memory circuits: serial

Clock frequency

Arithmetic, control, and core memory circuits: 478 kc; magnetic drum memory circuits: 239 kc

<table><tr><td>Registers</td><td>Three major arithmetic registers, three index registers, and additional registers for peripheral equipment</td></tr><tr><td>Environmental conditions</td><td>Standard operation to 85°F cabinet temperature. The power consumption at 115-v single-phase, 60-hertz is 2000 w. The total system power consumption is approximately 7000 w, including the two tape drives which operate on 208 v, three phase</td></tr><tr><td>Software</td><td>An integrated package designed for process control; includes real time executive, utility package, assembler, and FORTRAN II compiler, and library of subroutines</td></tr><tr><td>Input-output subsystems</td><td>350 analog inputs, expandable to over 2000; 32 digital outputs, expandable to over 1000</td></tr><tr><td>Priority interrupt</td><td>Handles over 100 levels of program priority (program operating time schedule)</td></tr></table>

# 2.12.3 Peripheral Equipment Description

Aside from the computer itself and the analog input and output subsystems, there are a number of peripheral devices which provide communication between the operators and the machine. The devices are listed below and can be seen in Fig. 2.12.1.

<table><tr><td>Four typewriters: two with 30-in. carriage
    and two with 16-in. carriage</td></tr><tr><td>Two magnetic-tape units</td></tr><tr><td>Paper-tape punch, reader</td></tr><tr><td>Input keyboard</td></tr><tr><td>x-y plotter</td></tr><tr><td>Console: function matrix and digital displ.</td></tr></table>

In normal operation, four IBM typewriters are used to provide hard-copy records of reactor data (see Fig. 2.l2.4 for location of the typewriters). Two 30-in.-carriage typewriters are used to record essentially all logs and calculation results. The periodically appearing results are all typed on one device on preprinted forms; results of demanded operations are typed on the second typewriter. One of the two 16-in.-carriage typewriters is installed in the reactor control room to

record alarm conditions associated with analog signals and calculation results. The second 16-in. typewriter (console) records all operations performed at the computer console.

The principal depository for reactor data is magnetic tape. The values of all the analog signals are stored on magnetic tape every 5 min. In addition, all intermediate and final calculation results are stored on tape. (The typeout of calculation results is generally less frequent and more limited in extent.) Two tape drives (IBM model 729-2) are available, with the second unit normally in standby. However, the second unit can be used for off-line functions such as data processing or program development while the first unit is on line.

The paper-tape punch and reader (Teletype model BPRE-2 and Digi-tronics model 2500 respectively) are used primarily in connection with programming functions, for example, assembly and compiling. There is normally no input or output of reactor information through these devices.

The input keyboard (Invac model PK-164) operates in conjunction with the on-line program development package (OLPD) in the computer. From the standpoint of reactor operation, it is the means of entering data for the trend logging and plotting functions.

The x-y plotter (Moseley type 2D2) is capable of plotting any input variable as a function of time or of any other input variable. Parameters for both coordinate axes must be entered by the operator.

The computer console is the focal point for use of the computer by the reactor operators. It contains the function matrix as well as the digital switches for the selection of the various request functions. The console also houses the panel for digital display of signal values (Fig. 2.12.5).

# 2.12.4 System Operation

2.12.4.1 Collection and Processing of Analog and Digital Input Signals

At the present time there are 291 analog signals from the reactor system connected to the computer. The types and numbers of signals are summarized in Table 2.12.1.<sup>3,4</sup> See Fig. 2.12.6 for a complete list of all input signals. These signals are arranged in a scan table that contains 350 entries. Under normal conditions the raw analog signals for all 350 points are scanned, compared with high and low alarm limits, and stored in core once each 5 sec.

In order to provide a more frequent look at selected variables, some analog signals appear at several points in the table. For instance, the outputs of the three neutron safety channels are arranged so that one of the signals is read every 200 msec. Another reason for multiple entry in the scan table is to permit integration (digital filtering

Table 2.12.1. Analog Input Signals   

<table><tr><td>Type</td><td>Number of Signals</td></tr><tr><td>Thermocouple</td><td></td></tr><tr><td>Conventional</td><td>169</td></tr><tr><td>Integrated</td><td>17</td></tr><tr><td>Pressure</td><td>20</td></tr><tr><td>Flow</td><td>13</td></tr><tr><td>Amplifier gain</td><td>4</td></tr><tr><td>Weight</td><td>5</td></tr><tr><td>Power and voltage</td><td>4</td></tr><tr><td>Liquid level</td><td>11</td></tr><tr><td>Pump speed and tachometer</td><td>6</td></tr><tr><td>Position</td><td>7</td></tr><tr><td>Nuclear</td><td>13</td></tr><tr><td>Process radiation</td><td>23</td></tr><tr><td>Total</td><td>292</td></tr></table>

over 1/60 sec) of the signal for greater accuracy and resolution. Temperatures that are used in calculations are integrated and converted to the nearest $0.1^{\circ}\mathrm{F}$ in the range from 900 to $1300^{\circ}\mathrm{F}$ . Thus, the signal must appear a second time, unintegrated, to provide information over the entire operating range. As a result of these multiple appearing signals, the 350-entry scan table contains 346 actual analog signals with four spare locations.

Realistic high and/or low process limits are imposed on most of the analog signals. In the remaining cases the limits are set at the instrument extremes. The normal computer response to an out-of-limits condition is to actuate the logger annunciator in the main control room and to print a message on the control-room typewriter identifying the variable, its value, and the time. Such a message is typed in red when the variable first goes out of limits and in black when it returns within limits. No other information (except for a 4-hr out-of-limits log) is typed while the signal is either out of or within limits.

There is one group of 65 analog signals (type 2) that is recorded on magnetic tape, in engineering units, each 5 sec while any one of the signals is out of limits. The typed messages for this group of variables are similar to those for the other signals. The recording function can be inhibited by operator request on any or all of the signals that will produce this action.

An out-of-limits condition on any one of another group of 22 analog signals (for instance, neutron flux) switches the computer to a "fast scan" mode of operation. In this mode the scan table is reduced to 64

important variables and all 64 are scanned, converted to engineering units, and stored on magnetic tape once each $1/4$ sec. This mode of operation continues for 1 min, without limit checking, after its initiation. At the end of that minute the normal scan is resumed until another signal to start "fast scan" is detected. The "fast scan" mode of operation can also be inhibited by operator request on any or all of the signals that will produce it.

Once each 5 min, regardless of the scanning mode, all 350 signals are read, converted to engineering units, and stored on magnetic tape.

# 2.12.4.2 Logging Functions

The computer generates and types out a number of periodic logs, which are tabulated below:

1-hr log (54 analog signals)

8-hr log (175 analog signals)

Daily report (21 parameters)

Out-of-limits log (once every 4 hr)

Calculation results

The 1- and 8-hr logs simply present the values of selected analog signals to record the status of the system. In both cases the values that are printed are the same as those that were recorded on magnetic tape during the last 5-min taping operation. The daily report summarizes a number of operating parameters such as integrated power, time at temperature, and numbers of thermal cycles on important components. The out-of-limits log is an hourly summary of all analog signals (up to 40) that are out of limits at that time along with their current values. Selected results of some calculations, such as the average reactor inlet and outlet temperature, are also typed on the log sheet periodically.

# 2.12.4.3 Calculations

Aside from the routine functions, such as units conversion, the computer performs a number of on-line calculations using current reactor data. Many of these calculations include alarm functions to call attention to abnormal conditions. The calculations are normally performed on a periodic basis with the results being printed usually less frequently. Many of the calculations can be performed at nonscheduled times on operator demand; results of nonscheduled calculations are always printed.

Table 2.12.2 summarizes the schedule for some of the major calculations.

Table 2.12.2. Major Routine Calculations   

<table><tr><td>Calculation</td><td>Normal Interval</td><td>Printout Interval</td><td>Demandable?</td></tr><tr><td>Reactivity balance</td><td>5 min</td><td>1 hr</td><td>Yes</td></tr><tr><td>Average reactor inlet and outlet temperature</td><td>1 hr</td><td>1 hr</td><td>Yes</td></tr><tr><td>Reactor-vessel temperature difference</td><td>10 min</td><td>1 hr</td><td>No</td></tr><tr><td>Cell-atmosphere average temperature</td><td>1 hr</td><td>8 hr</td><td>Yes</td></tr><tr><td>Heat balance</td><td>4 hr</td><td>4 hr</td><td>Yes</td></tr><tr><td>Salt inventory</td><td>8 hr</td><td>8 hr</td><td>Yes</td></tr></table>

# 2.12.4.4 Miscellaneous Functions

Some of the miscellaneous functions that are, or can be, performed by the computer are listed below.

Trend log (up to 26 variables)

Trend plot

Digital display

Contact and analog outputs

On-line program development (OLPD)

Data retrieval and processing

General-purpose computing

The first three items, trend log, trend plot, and digital display, are means of providing visual information for operator guidance. The variables to which these functions are applied can be selected at will by the operators. The last three items in this list are all related in that they are nominally off-line functions that can be performed with the computer on line. The system program requires only about $30\%$ of the capability of the computer under normal circumstances; this utilization increases to about $40\%$ in the "fast scan" mode of operation. In addition, the system program requires only about two-thirds of the core memory. Thus, there is ample capability for background processing of off-line material.

The purpose of the computer is to provide close surveillance, rapid processing, and compact storage of large amounts of reactor data. Since it is associated with a reactor experiment, it is not possible to define all the data and calculations that are required for a complete analysis of the system. Therefore a great deal of data are being collected which may be used much later or which may never be used.

# 2.12.5 References and ORNL Drawings

For more details on all parts of the system, refer to the documents and drawings listed. For details on the operation of the system from the reactor operator's viewpoint, refer to item ll in the Reference List, Computer Manual for MSRE Operators.

<sup>1</sup>Interim Report to Oak Ridge National Laboratory Relating to a Digital Data Acquisition System for Use with the Homogeneous Reactor Test Facility, CF-60-3-159, R. K. Adams et al. (Mar. 29, 1960).   
2Final Report to Oak Ridge National Laboratory Relating to a Digital Data Collecting and Computing System for the EGCR Test Loop Facility, R. K. Adams et al. (June 22, 1960).   
3MSRE Data Collecting and Handling Requirements, A Study Report, MSR-61-112, G. H. Burger (Aug. 15, 1961).   
4Specification for a Digital Data Collecting and Computing System for the Molten Salt Reactor Experiment Located at Oak Ridge National Laboratory, Oak Ridge, Tennessee, JS-81-170 (May 1, 1962).   
5Use of On-Line Computer in MSRE Operation, CF-62-3-26, P. N. Haubenreich and J. R. Engel (Mar. 6, 1962).   
$^{6}$ Toward Closed Loop Control in Nuclear Plants, Nucleonics, 71 (June 1962).   
7High Speed Monitor for Closed Loop Control, Colin G. Lennox and Albert Pearson, Nucleonics, 73 (June 1962).   
<sup>8</sup>Input Signal Functional Tabulation, SC-I&C-EGM-6230.   
9MSRE Digital Data Collecting and Computer System Calculations, May 17, 1963.   
10TRWC Proposal for a TRW-340 Digital Data Collecting and Computing System, TRWC-63 157.   
11Computer Manual for MSRE Operators.   
12Cross Reference Listing of MSRE Instrumentation and Control System Drawings, CF-63-2-2, R. L. Moore.   
13MSRE Data Logger Signal Interconnection Wiring, ORNL Drawings D-HH-B-57456, 57457, 57458, 57459, 57460, and 57461.

![](images/57c3358ba66878b6095693f2e79a7a421fea947d1ea083fbd2ba2baa814675e2.jpg)  
Fig. 2.12.1. Bunker-Ramo 340 Computer Input-Output Equipment.

![](images/6d81d05be0b92f8750fdbe84ca76ab3fd3124f9e76ad47500456b9c9c80e5df0.jpg)  
Fig. 2.12.2. Bunker-Ramo 340 Computer Central Processor.

ORNL-DWG 64-64E1AR

![](images/59a2e09cccc4e86b402a5b72fd1fbdfb8807c3739ea949c9830a3ec3a9cbb382.jpg)  
Fig. 2.12.3. Block Diagram of MSRE Digital Data Collecting and Computer System.

![](images/46004f640ea37f07615d4d80136916f2faad87bfc59b8ea38447e15e67156c9c.jpg)  
Fig. 2.12.4. Layout of Data Room.

![](images/7854f80dd199b7c0fcb4f766ec0dfee23ebd09f148032dff7feb51a7fe70baf4.jpg)  
Fig. 2.12.5. Computer Operator Console.

Fig. 2.12.6. Data Logger Signal Interconnection Wiring Signal Assignment Tabulation.   

<table><tr><td colspan="4">REACTOR SYSTEM</td><td colspan="101">DATA LOGGER</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="4">REACTOR SYSTEM</td><td colspan="88">DATA LOGGER</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>LOGMAR</td><td>TYPE</td><td>GENOM</td><td>COMMITED</td><td>DATE</td><td>APPROVED</td><td>APPD</td><td>DATE</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUTF</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONM UT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUB</td><td>CONMUT</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMIB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUMB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMMB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUMB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMAB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMub</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMDB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMLOB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONM UB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUEB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBUB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td><td>CONMUB</td><td>CONCUBIB</td></tr></table>

# 2.13 MSRE Beryllium Monitoring System<sup>1</sup>

Atmospheric beryllium concentration is monitored by 15 air sampling stations located at strategic places throughout the reactor building. The beryllium content of the air is monitored by drawing air through filter papers which are then collected and analyzed for beryllium content.

The radiator air stack air is monitored by an arc spectrograph. Air is drawn through the spectrograph for a set period and then analyzed by the light spectrographic method. The result of the analysis is printed on a recorder located in the spectrograph cabinet.

The spectrograph is equipped with a manual switch so that the coolant cell can be monitored during reactor maintenance operations.

$^{1}$ N. E. Bolton and T. C. Whitson, Revised Beryllium Control Program for MSRE, ORNL-CF-63-11-44. (Supersedes ORNL CF-63-7-63.)

![](images/a53849feb8f18a97366a0ebd9d1ce37936e702d35b3d06dc1e5ce669c8fc1406.jpg)

# INTERNAL DISTRIBUTION

1. R. K. Abele   
2. R. K. Adams   
3. G. M. Adamson   
4. R. G. Affel   
5. L. G. Alexander   
6. G. W. Allin   
7. A. H. Anderson   
8. J. L. Anderson   
9. R. F. Apple   
10. C. F. Baes   
ll. J. M. Baker   
12. S. J. Ball   
13. C. J. Barton   
14. A. E. G. Bates   
15. H. F. Bauman   
16. S. E. Beall   
17. R. L. Beatty   
18. M. Bender   
19. C. E. Bettis   
20. E. S. Bettis   
21. R. E. Blanco   
22. F. F. Blankenship   
23. J. O. Blomeke   
24. R. Blumberg   
25. E. G. Bohlmann   
26. C. J. Borkowski   
27. G. E. Boyd   
28. H. R. Brashear   
29. J. Braunstein   
30. M. A. Bredig   
31. R. B. Briggs   
32. H. R. Bronstein   
33. F. R. Bruce   
34. G. D. Brunton   
35. J. B. Bullock   
36. O. W. Burke   
37. D. A. Canonico   
38. S. Cantor   
39. W. L. Carter   
40. T. M. Cate   
41. G. I. Cathers   
42. O. B. Cavin   
43. A. Cepolino   
44. J. M. Chandler   
45. C. W. Collins   
46. E. L. Compere   
47. K. V. Cook

48. W. H. Cook   
49. L. T. Corbin   
50. J. L. Crowley   
51. F. L. Culler   
52. J. M. Dale   
53. D. G. Davis   
54. R. J. DeBakker   
55. S. J. Ditto   
56. A. S. Dworkin   
57. D. A. Dyslin   
58. W. P. Eatherly   
59. J. R. Engel   
60. E. P. Epler   
61. D. E. Ferguson   
62. L. M. Ferris   
63. A. P. Fraas   
64. H. A. Friedman   
65. D. N. Fry   
66. J. H Frye, Jr.   
67. C. H. Gabbard   
68. R. B. Gallaher   
69. H. E. Goeller   
70. W. R. Grimes   
71. A. G. Grindell   
72. R. H. Guymon   
73. J. P. Hammond   
74. B. A. Hannaford   
75. P. H. Harley   
76. D. G. Harman   
77. W. O. Harms   
78. C. S. Harrill   
79. P. N. Haubenreich   
80. F. A. Heddleson   
81. P. G. Herndon   
82. J. R. Hightower   
83.M.R.Hill   
84. H. W. Hoffman   
85. D. K. Holmes   
86. R. W. Horton   
87. T. L. Hudson   
88. T. M. Hungerford   
89. H. Inouye   
90. W. H. Jordan   
91. P. R. Kasten   
92. R. J. Kedl   
93. M. T. Kelley   
94. M. J. Kelly

95. C. R. Kennedy

96-97. H. T. Kerr

98. S. S. Kirslis

99. D. J. Knowles

100. J. W. Koger

101. A. I. Krakiovak

102. J. W. Krewson

103. R. C. Kryter

104. C. E. Lamb

105. J. A. Lane

106. M. S. Lin

107. R. B. Lindauer

108. A. P. Litman

109. G. H. Llewellyn

110. E. L. Long

111. M. I. Lundin

112. R. N. Lyon

113. H. G. MacPherson

114. R. E. MacPherson

115. D. L. Manning

116. C. D. Martin

117. T. H. Mauney

118. H. McClain

119. R. W. McClung

120. H. E. McCoy

121. H. F. McDuffie

122. C. K. McGlothlan

123. C. J. McHargue

124. J. R. McWherter

125. L. E. McNeese

126. H. J. Metz

127. A. S. Meyer

128. R. R. Minue

129-132. R. L. Moore

133. C. A. Mossman

134. H. A. Nelms

135. P. D. Neumann

136. J. P. Nichols

137. E. L. Nicholson

138. L. C. Oakes

139. R. B. Parker

140. C. L. Partain

141. P. Patriarca

142. A. M. Perry

143. T. W. Pickel

144. H. B. Piper

145. J. F. Potts

146. B. E. Prince

147. G. L. Ragan

148-149. J. L. Redford

150. M. Richardson

151. G. O. Robbins

152. R. C. Robertson

153. W. C. Robinson

154. H. C. Roller

155. M. W. Rosenthal

156. D. P. Roux

157. P. Rubel

158. J. A. Russell

159. H. C. Savage

160. W. F. Schaffer

161. C. E. Schilling

162. Dunlap Scott

163. J. L. Scott

164. H. E. Seagren

165. C. E. Sessions

166. J. H. Shaffer

167. D. T. Simpson

168. M. J. Skinner

169. G. M. Slaughter

170. T. F. Sliski

171. A. N. Smith

172. F. J. Smith

173. G. P. Smith

174. O. L. Smith

175. P. G. Smith

176. W. F. Spencer

177. I. Spiewak

178. B. Squires

179. R. C. Steffy

180. W. C. Stoddart

181. H. H. Stone

182. R. S. Stone

183. R. A. Strehlow

184. H. J. Stripling

185. R. F. Sweet

186-191. J. R. Tallackson

192. E. H. Taylor

193. W. Terry

194. R. E. Thoma

195. L. M. Toth

196. D. B. Trauger

197. R. W. Tucker

198. W. C. Ulrich

199. C. S. Walker

200. J. S. Watson

201. H. L. Watts

202. C. F. Weaver

203. B. H. Webster

204. A. M. Weinberg

205. J. R. Weir

206. W. J. Werner

207. K. W. West   
208. M. E. Whatley   
209. J. C. White   
210. H. D. Wills   
211. L. V. Wilson   
212. G. Young   
213. H. C. Young

214. J. P. Young   
215. E. L. Youngblood   
216. F. C. Zapp

217-218. Central Research Library   
219-220. Document Reference Section   
221-230. Laboratory Records Department   
231. Laboratory Records, ORNL R.C.

# EXTERNAL DISTRIBUTION

232-233. D. F. Cope, RDT Site Office, ORNL   
234. A. Giambusso, Atomic Energy Commission, Washington   
235. W. J. Larkin, Atomic Energy Commission, Oak Ridge   
236-237. T. W. McIntosh, Atomic Energy Commission, Washington   
238. H. M. Roth, Atomic Energy Commission, Oak Ridge   
239. M. Shaw, Atomic Energy Commission, Washington   
240. W. L. Smalley, Atomic Energy Commission, Oak Ridge   
241. G. H. Burger, Mining and Metals Division, Union Carbide Corporation, Niagara Falls, N.Y.   
242. E. N. Fray, General Electric Company, San Jose, California   
243. S. H. Hanauer, University of Tennessee, Knoxville, Tenn.   
244. T. W. Kerlin, University of Tennessee, Knoxville, Tenn.   
245. C. L. Matthews, Atomic Energy Commission, Oak Ridge   
246. J. A. H. Kersten, P/A Kema, Utrechtsweg 310, Arnhem, The Netherlands   
247. K. A. Warschauer, Jacob Marislaan 48, Arnhem, The Netherlands   
248. William Kerr, Director, Michigan Memorial, Phoenix Project, Ann Arbor, Michigan

249-263. Division of Technical Information Extension   
264. Laboratory and University Division, AEC, ORO