![](images/bf6b765dcde8655ab98c9773a0ef76b278184e6e491e3c65859aae14bfb70462.jpg)

# OAK RIDGE NATIONAL LABORATORY. operated by

# UNION CARBIDE CORPORATION

# NUCLEAR DIVISION

![](images/10ee99198c5c288b5ff320747c41640e492b1722fe3993c3c5dbbd59efbc1a37.jpg)

for the

U.S. ATOMIC ENERGY COMMISSION

ORNL-TM-3718

MASS TRANSFER BETWEEN SMALL BUBBLES AND LIQUIDS IN

COCURRENT TURBULENT PIPELINE FLOW

(Thesis)

T. S. Kress

This report was prepared as an account of work sponsored by the United States Government. Neither the United States nor the United States Atomic Energy Commission, nor any of their employees, nor any of their contractors, subcontractors, or their employees, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness or usefulness of any information, apparatus, product or process disclosed, or represents that its use would not infringe privately owned rights.

Contract No. W-7405-eng-26

MASS TRANSFER BETWEEN SMALL BUBBLES AND LIQUIDS IN COCURRENT TURBULENT PIPELINE FLOW

T. S. Kress

Submitted as a dissertation to the Graduate Council of The University of Tennessee in partial fulfillment of the requirements for the degree Doctor of Philosophy.

APRIL 1972

# NOTICE

This report was prepared as an account of work sponsored by the United States Government. Neither the United States nor the United States Atomic Energy Commission, nor any of their employees, nor any of their contractors, subcontractors, or their employees, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness or usefulness of any information, apparatus, product or process disclosed, or represents that its use would not infringe privately owned rights.

OAK RIDGE NATIONAL LABORATORY

Oak Ridge, Tennessee 37830

operated by

UNION CARBIDE CORPORATION

for the

U. S. ATOMIC ENERGY COMMISSION

# ACKNOWLEDGMENTS

This investigation was performed at the Oak Ridge National Laboratory operated by the Union Carbide Corporation for the U. S. Atomic Energy Commission. The author is particularly grateful for the helpful discussions, guidance, and direction given the research by the major advisor, Dr. J. J. Keyes, and the support of Dr. H. W. Hoffman, Head of the Heat Transfer-Fluid Dynamics Department of the Reactor Division.

Dunlap Scott of the Molten-Salt Reactor Program suggested the problem and provided initial funding under the MSR Program. Dr. F. N. Peebles, Dean of Engineering, The University of Tennessee, suggested the use of the oxygen-glycerine-water system and carried out the original analysis of the applicability to xenon-molten salt systems.

The contributions of the following ORNL staff members are also gratefully acknowledged: R. J. Kedl for his bubble generator development work drawn upon here; Dr. C. W. Nestor for computer solution of the analytical model; and Frances Burkhalter for preparation of the figures.

Special thanks are given to Margie Adair for her skillful and cheerful preparation of the preliminary and final manuscripts, and, of course, to my wife, Dee, for her forbearance.

# ABSTRACT

Liquid-phase-controlled mobile-interface mass-transfer coefficients were measured for transfer of dissolved oxygen into small helium bubbles in cocurrent turbulent pipeline flow for five different mixtures of glycerine and water. These coefficients were determined by transient response experiments in which the dissolved oxygen was measured at only one position in a closed recirculating loop and recorded as a function of time. Using an independent photographic determination of the interfacial areas, the mass-transfer coefficients were extracted from these measured transients and determined as functions of pipe Reynolds number, Schmidt number, bubble Sauter-mean diameter, and gravitational orientation of the flow.

Two general types of behavior were observed:

(1) Above pipe Reynolds numbers for which turbulent inertia forces dominate over gravitational forces, horizontal and vertical flow mass-transfer coefficients were identical and varied according to the regression equation

$$
\mathrm {S h} / \mathrm {S c} ^ {1 / 2} = 0. 3 4 \mathrm {R e} ^ {0. 9 4} \left(\mathrm {d} _ {\mathrm {v s}} / \mathrm {D}\right) ^ {1. 0}.
$$

The observed Reynolds number exponent agreed generally with other literature data for cocurrent pipeline flow but did not agree with expectation based on equivalent power dissipation comparisons with agitated vessel data.

(2) Below the Reynolds numbers that marked the equivalence of horizontal and vertical flow coefficients, the horizontal-flow coefficients continued to vary according to the above equation until, at low flows,

severe stratification of the bubbles made operation impractical. The vertical-flow coefficients at these lower Reynolds numbers underwent a transition to approach constant asymptotes characteristic of the bubbles rising through the quiescent liquid. For small bubbles in the most viscous mixture tested, both horizontal and vertical-flow coefficients underwent this transition.

An expression was developed for the relative importance of turbulent inertial forces compared to gravitational forces, $\frac{F_i}{F_g}$ . This ratio served as a good criterion for establishing the pipe Reynolds numbers above which horizontal and vertical-flow mass-transfer coefficients were identical. In addition, it proved to be a useful linear scaling factor for calculating the vertical-flow coefficients in the above mentioned transition region.

A seemingly anomalous behavior was observed in data for water (plus about 200 ppm N-butyl alcohol) which exhibited a significantly smaller Reynolds number exponent than did data for the other fluid mixtures. To explain this behavior, a two-regime "turbulence interaction" model was formulated by balancing turbulent inertial forces with drag forces. The relationship of the drag forces to the bubble relative-flow Reynolds number gave rise to the two regimes with the division being at $\mathrm{Re_b} = 2$ . The resulting bubble mean velocities for each regime were then substituted into Frössling-type equations to determine the mass-transfer behavior. The resulting Reynolds number exponent for one of the regimes $(\mathrm{Re_b} \leq 2)$ agreed well with the observed data but the predicted exponent for the effect of the ratio of bubble mean diameter to conduit diameter, $d_{\mathrm{vs}} / D$ , was less than that observed. The mass-transfer equations

V

resulting from the other regime $(\mathrm{Re}_{\mathrm{b}} > 2)$ agreed well with data for particles in agitated vessels and also compared favorably with the water data mentioned above.

For comparison, a second analytical model was developed based on surface renewal concepts and an eddy diffusivity that varied with Reynolds number, Schmidt number, bubble diameter, interfacial condition, and position away from an interface. Using a digital computer, a tentative numerical solution was obtained which treated a dimensionless renewal period, $\mathbf{T}_{*}$ , as a parameter. This renewal period was interpreted as being a measure of the rigidity of the interface, $\mathbf{T}_{*} \rightarrow 0$ corresponding to fully mobile and $\mathbf{T}_{*} \rightarrow$ approximately 2.7 (in this case) to fully rigid interfaces.

# TABLE OF CONTENTS

# CHAPTER

PAGE

I. INTRODUCTION 1

II. LITERATURE REVIEW 5

Experimental-Cocurrent Flow 5

Experimental-Agitated Vessels 7

Discussion of Available Experimental Data 9

Theoretical 11

Surface Renewal Models 11

Modeling of the Eddy Structure 14

Turbulence Interactions 15

Dimensional Analysis (Empiricism) 16

Discussion 17

III. DESCRIPTION OF EXPERIMENT 19

Transient Response Technique 19

Apparatus 23

Pump 23

Liquid Flow Measurement 26

Temperature Stabilization 27

Gas Flow Measurement 27

Dissolved Oxygen Measurement 28

Bubble Generation 29

Bubble Separation 34

Test Section 37

Bubble Surface Area Determination - Photographic

System 38

End Effect 47

Summary of Experimental Procedure 49

# IV. EXPERIMENTAL RESULTS 55

Unadjusted Results 55

Equivalence of Horizontal and Vertical Flow

Mass Transfer 56

Vertical Orientation Low-Flow Asymptotes 60

Mass Transfer Coefficients 60

Calculating Vertical Flow Mass-Transfer Coefficients

for $\mathbf{F}_{\mathrm{i}} / \mathbf{F}_{\mathrm{g}}$ Less Than 1.5 67

Comparison with Agitated Vessels 69

Recommended Correlations 71

# V. THEORETICAL CONSIDERATIONS 76

Turbulence Interaction Model 76

Surface Renewal Model 81

# VI. SUMMARY AND CONCLUSIONS 94

# VII. RECOMMENDATIONS FOR FURTHER STUDY 100

Experimental 100

Theoretical 102

# LIST OF REFERENCES 105

# APPENDICES 111

# A PHYSICAL PROPERTIES OF AQUEOUS-GLYCEROL MIXTURES 111

# CHAPTER

PAGE

B DERIVATION OF EQUATIONS FOR CONCENTRATION CHANGES

ACROSS A GAS-LIQUID CONTACTOR 117

C INSTRUMENT APPLICATION DRAWING 121

D INSTRUMENT CALIBRATIONS 123

E EVALUATION OF EFFECT OF OXYGEN SENSOR RESPONSE SPEED ON

THE MEASURED TRANSIENT RESPONSE OF THE SYSTEM 129

F MASS BALANCES FOR THE SURFACE RENEWAL MODEL 131

ESTIMATE OF ERROR DUE TO END-EFFECT ADJUSTMENTS 134

H MASS TRANSFER DATA 137

LIST OF SYMBOLS 163

# LIST OF TABLES

# TABLE FAGE

I. Ranges of Independent Variables Covered 3   
II. Categories of Data Correlation for Mass Transfer from

a Turbulent Liquid to Gas Bubbles 12

III. Physical Properties of Aqueous-Glycerol Mixtures $(25^{\circ}C)$

Data of Jordan, Ackerman, and Berger 20

IV. Experimental Conditions for Runs Used to Validate

Surface Area Determination Method for Vertical

4

V. Experimental Conditions for Runs Shown on Horizontal

Flow Volume Fraction Correlation 45

VI. Conditions at Which Horizontal and Vertical Flow

Mass-Transfer Coefficients Become Equal

(Lamont's Data)11 59

# LIST OF FIGURES

# FIGURE

1. Photograph of the Mass Transfer Facility 24   
2. Schematic Diagram of the Main Circuit of the Experimental Apparatus 25   
3. Diagram of the Bubble Generator 31   
4. Comparison of Measured Bubble Sizes with the Distribution Function 33   
5. Diagram of the Bubble Separator 36   
6. Comparison of Interfacial Areas Per Unit Volume Measured Directly from Photographs with Those Established Through the Distribution Function. Vertical Flow 43   
7. Correlation of Horizontal Flow Volume Fraction 46   
8. Comparison of Measured and Calculated Interfacial Areas Per Unit Volume. Horizontal Flow 48   
9. Typical Experimental Concentration Transient Illustrating Straight-Line Behavior on Semi-Log Coordinants 53   
10. Typical Examples of Bubble Photographs: a. Inlet b. Exit Vertical Flow, $37.5\%$ Glycerine- $62.5\%$ Water, $Q_{\ell} = 20$ gpm, $Q_{g} / Q_{\ell} = 0.3\%$ , $D = 2$ inches, and $d_{vs} = 0.023$ inches   
11. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. Water Plus $\sim 200$ ppm N-Butyl Alcohol. Horizontal and Vertical Flow in a 2-inch Diameter Conduit 62

# FIGURE

# PAGE

12. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. 12.5% Glycerine-87.5% Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit 63   
13. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $25\%$ Glycerine- $75\%$ Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
14. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. 37.5% Glycerine-62.5% Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit 65   
15. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $50\%$ Glycerine- $50\%$ Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit 66   
16. Observed Types of Horizontal Flow Behavior. $\mathrm{d}_{\mathrm{VS}} = 0.02$ inches and D = 2 inches 68   
17. Equivalent Power Dissipation Comparison of Results with Agitated Vessel Data 70   
18. Equivalent Power Dissipation Comparison of Gravity Dominated Results with Agitated Vessel Data 72   
19. Correlation of Horizontal Flow Data 74   
20. Dimensionless Variation of Eddy Diffusivity with Distance from an Interface. Effect of Surface Condition 88

# FIGURE

21. Variation of Eddy Diffusivity with Distance from an Interface. Comparison of Calculated Values with Data of Sleicher 90   
22. Numerical Results of the Surface Renewal Model. Plots of a, b, and c (Exponents on Re, Sc, and d/D, Respectively) as Functions of the Dimensionless Period, $\mathbf{T}_{\star}$ 92   
23. Schmidt Numbers of Glycerine-Water Mixtures 112   
24. Henry's Law Constant for Oxygen Solubility in Glycerine-Water Mixtures 113   
25. Molecular Diffusion Coefficients for Oxygen in Glycerine-Water Mixtures. Data of Jordan, Ackerman, and Berger 114   
26. Densities of Glycerine-Water Mixtures 115   
27. Viscosities of Glycerine-Water Mixtures 116   
28. Instrument Application Drawing of the Experiment Facility 121   
29. Bubble Size Range Produced by the Bubble Generator 123   
30. Calibration of Rotameter No. 1 (100 gpm) 124   
31. Calibration of Rotameter No. 2 (40 gpm) 125   
32. Calibration of Rotameter No. 3 (8 gpm) 126   
33. Calibration of Gas-Flow Meter at 50 psig 127   
34. Calibration of Oxygen Sensors in two Mixtures of Glycerine and Water 128

FIGURE PAGE

35. Unadjusted Mass Transfer Data. Water Plus $\sim 200$ ppm N-Butyl Alcohol. Vertical Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
36. Unadjusted Mass Transfer Data. Water Plus $\sim 200$ ppm N-Butyl Alcohol. Horizontal Flow 139   
37. Unadjusted Mass Transfer Data. 12.5% Glycerine-87.5% Water. Vertical Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
38. Unadjusted Mass Transfer Data. 12.5% Glycerine-87.5% Water. Horizontal Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
39. Unadjusted Mass Transfer Data. $25\%$ Glycerine- $75\%$ Water. Vertical Flow 142   
40. Unadjusted Mass Transfer Data. $25\%$ Glycerine- $75\%$ Water. Horizontal Flow . . . . . . . . . . . . . . . 143   
41. Unadjusted Mass Transfer Data. 37.5% Glycerine-62.5% Water. Vertical Flow . . . . . . . . . . . . . . . . 144   
42. Unadjusted Mass Transfer Data. 37.5% Glycerine-62.5% Water. Horizontal Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
43. Unadjusted Mass Transfer Data. 50% Glycerine-50% Water. Vertical Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
44. Unadjusted Mass Transfer Data. 50% Glycerine-50% Water. Horizontal Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   
45. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. Water Plus $\sim 200$ ppm N-Butyl Alcohol. Horizontal and Vertical Flow 148

# FIGURE

PAGE

46. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. 12.5% Glycerine 87.5% Water. Horizontal and Vertical Flow 149   
47. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $25\%$ Glycerine- $75\%$ Water. Horizontal and Vertical Flow 150   
48. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. 37.5% Glycerine-62.5% Water. Horizontal and Vertical Flow 151   
49. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $50\%$ Glycerine- $50\%$ Water. Horizontal and Vertical Flow 152   
50. Mass Transfer Data Adjusted for End-Effect. Water Plus \~200 ppm N-Butyl Alcohol. Vertical Flow 153   
51. Mass Transfer Data Adjusted for End-Effect. Water Plus \~200 ppm N-Butyl Alcohol. Horizontal Flow 154   
52. Mass Transfer Data Adjusted for End-Effect. 12.5%  
Glycerine-87.5% Water. Vertical Flow . . . . . . . . . 155   
53. Mass Transfer Data Adjusted for End-Effect. 12.5%  
Glycerine-87.5% Water. Horizontal Flow . . . . . . . . . 156

# XVI

# FIGURE

54. Mass Transfer Data Adjusted for End-Effect. 25%  
Glycerine-75% Water. Vertical Flow 157   
55. Mass Transfer Data Adjusted for End-Effect. 25%  
Glycerine-75% Water. Horizontal Flow 158   
56. Mass Transfer Data Adjusted for End-Effect. 37.5%  
Glycerine-62.5% Water. Horizontal Flow 159   
57. Mass Transfer Data Adjusted for End-Effect. 50%  
Glycerine-50% Water. Vertical Flow 160   
58. Mass Transfer Data Adjusted for End-Effect. 50%  
Glycerine-50% Water. Horizontal Flow 161

# CHAPTER I

# INTRODUCTION

When gas bubbles are dispersed in a continuous liquid phase, dissolved constituents of sufficient volatility will be exchanged between the liquid and the bubbles, effectively redistributing any concentration imbalances that exist. Common practices involve contacting gas bubbles with an agitated liquid in such a manner that a relatively large interfacial area is available. Techniques such as passing gas bubbles up through a liquid column or mechanically stirring a gas-liquid mixture in a tank have been studied extensively and the design technology for these is relatively firm. However, one method, cocurrent turbulent flow in a pipeline, has not been given a great deal of attention. A review of the literature has shown that the available data are insufficient to allow confident determination of the mass-transfer rates in such a system. This research, then, was undertaken to provide additional information that will aid in determining liquid phase controlled mass-transfer rates for cocurrent turbulent flow of small bubbles and liquids in a pipeline.

The impetus for this work was provided by the Molten Salt Breeder Reactor (MSBR) Program of the Oak Ridge National Laboratory where recent remarkably successful operation of a molten salt fueled nuclear reactor<sup>1</sup> has convincingly demonstrated the feasibility of this power system. The economic competitiveness of an MSBR, however, depends to a significant extent on the breeding ratio obtainable. The production within the liquid fuel of fission-product poisons, principally xenon-135, exerts

a strong influence on the neutron economy of the reactor and consequently on the breeding ratio itself.

One method proposed for removing the xenon would require injecting small helium bubbles into the turbulently flowing regions of the fuel-coolant stream and allowing them to circulate with the fuel. Since such bubbles would be deficient in xenon compared to the nearby bulk stream, the dissolved xenon would be transferred by turbulent diffusion across the concentration potential gradient. By continuous injection and removal of the helium bubbles the equilibrium xenon poisoning can be significantly reduced. Since a large amount of gas in the fuel could influence the reactivity of the core, this system would be limited to low volume fractions.

Peebles² showed that removal of dissolved oxygen from a given mixture of glycerine and water by small helium bubbles could closely match the hydrodynamic and mass-transfer conditions in an MSBR and suggested using such a system in a similitude experiment from which the actual MSBR behavior might be inferred. Other desirable features of such a system include: (1) convenient variation of the Schmidt number by using different percentages of glycerine in water, (2) operation at room temperature using glass hardware that allows photographic measurements through an optically clear system, and (3) easy measurement of the dissolved oxygen content by commercially available instruments. Therefore an oxygen-glycerine-water system was chosen for this study.

The objective of the program was to measure liquid phase controlled axially averaged mass-transfer coefficients, $\mathbf{k}$ , defined by

$$
k \equiv \frac {\int_ {0} ^ {L} k _ {x} d x}{L}.
$$

The local mass-transfer coefficients, $\mathbf{k}_{\mathbf{x}}$ are defined by

$$
J \equiv k _ {x} a [ C _ {\text {a v g}} - C _ {s} ],
$$

where $J$ is the mass transferred from the liquid to the bubbles per unit time per unit volume of liquid, $a$ is the interfacial area per unit volume of liquid, $C_{avg}$ is the bulk average concentration, and $C_s$ is the interfacial concentration.

These coefficients need to be established as a function of Schmidt number, Reynolds number, bubble size, conduit diameter, gravitational orientation of the flow (vertical or horizontal), interfacial condition (absence or presence of a surface active agent), and the volume fraction of the bubbles. The scope of this thesis is limited to the ranges of variables listed in Table I, below, which for the most part represent limits of the experimental apparatus. Extensions of this program, however, are projected to include different conduit diameters and different interfacial conditions.

Table I. Ranges of Independent Variables Covered   

<table><tr><td>Variable</td><td>Range</td></tr><tr><td>Schmidt Number (weight percent of glycerine)</td><td>370 - 3446(0, 12.5, 25, 37.5, 50)</td></tr><tr><td>Pipe Reynolds Number</td><td>8 x 103- 1.8 x 105</td></tr><tr><td>Bubble Sauter Mean Diameter</td><td>0.01 to 0.05 inches</td></tr><tr><td>Gas to Liquid Volumetric Flow Ratio</td><td>0.3 and 0.5 percent</td></tr><tr><td>Gravitational Orientation of Flow</td><td>Vertical and Horizontal</td></tr><tr><td>Conduit Diameter</td><td>2 inches</td></tr></table>

The mass-transfer coefficients were extracted from measurements of the coefficient-area products, ka, and independent photographic measurements of the interfacial areas per unit volume, a. The products, ka,

were established by means of a unique transient response technique in which the changes in liquid phase concentration were measured as a function of time at only one position in a closed liquid recirculating system while helium bubbles were injected at the test section entrance and removed richer in oxygen at the exit. The apparatus for generating these small bubbles (with an independent control of their mean size) and effectively separating a high percentage from the flowing mixture had to be developed prior to the start of this research. These are described in Chapter III along with the photographic equipment and technique for establishing the interfacial areas.

The results of this study are expected to be of immediate benefit to the MSBR Program and should also prove useful to workers in the general chemical industry. Application may extend to such diverse areas as general extraction of radioactive elements from reactor effluents, bubble lifetimes in the coolant of liquid metal fast breeder reactors, and oxygen treatment of sewage effluents. In addition, benefits of a fundamental nature may be derived in that the research concerns transfer of a scalar in a turbulent shear flow field in which the fluid velocity field effectively seen by the bubbles is primarily due to the turbulent fluctuations. The characteristics of mass transfer between dispersed bubbles and a continuous liquid phase in turbulent flow are thus seen to be of immediate scientific and practical importance.

# CHAPTER II

# LITERATURE REVIEW

A comprehensive survey was made of literature related to mass transfer between small bubbles and liquids in cocurrent turbulent flow. An exhaustive review of all this literature would be lengthy and somewhat pointless. Consequently, only those works that are considered representative of the field (not necessarily of most significance) are included in this chapter and the author intends no derogation or slighting by the omission of any work. No significance should be attached to the order in which references appear. For a fairly complete documentation of work related to this subject, the reader is referred to several excellent review articles.[3-8]

# Experimental-Cocurrent Flow

There have been very few direct measurements of mass-transfer coefficients for cocurrent turbulent flow of small gas bubbles and liquids, perhaps because substantial special apparatus seems to be required for these measurements. Recently Jepsen<sup>9</sup> measured the liquid phase controlled product of mass-transfer coefficient, k, and interfacial surface area per unit volume, a, for air/water flow in horizontal pipes with and without spiral turbulence promoters. For straight tubes without turbulence promoters he correlated his data by the equation,

$$
k a \cdot 8 ^ {- 1 / 2} \sigma^ {- 1 / 2} \mu^ {0 \cdot 0 6} D ^ {0 \cdot 6 8} = 3. 4 7 \varepsilon_ {V} ^ {0 \cdot 4}.
$$

As shown in Chapter IV, page 58, the energy dissipation per unit volume, $\epsilon_{\mathrm{v}}$ , can be represented as

$$
\varepsilon_ {v} = \left(\frac {0 . 3 1 6}{2 g _ {c}}\right) \frac {\mu^ {3}}{D ^ {4} \rho^ {2}} R e ^ {1 1 / 4}. \tag {1}
$$

Therefore, Jepsen's correlation reveals that

$$
\mathrm {S h} \sim \mathrm {R e} ^ {1 \cdot 1 / \mathfrak {g} ^ {1 / 2}} a.
$$

Care must be taken in interpreting the influence of Reynolds number on $k$ when the product, $ka$ , is reported because the interfacial area itself may depend on the Reynolds number. No attempt was made by Jepsen to separate the area from the product.

Scott and Hayduk, $^{10}$ in admittedly exploratory experiments, dissolved carbon dioxide and helium into water, ethanol, and ethylene glycol in horizontal flow pipelines. Thus they did vary the diffusivity but, like Jepsen, did not separate the ka product.

Their results were correlated by the equation

$$
\mathrm {k a} = \frac {0 . 0 0 6 8 \mathrm {V} \Phi^ {0 . 7 4} \sigma^ {0 . 5 1} \mu^ {0 . 0 8} \mathcal {D} ^ {0 . 3 9}}{\mathrm {D} ^ {1 . 8 8}},
$$

from which may be inferred

$$
\mathrm {S h} \sim \mathrm {R e} / \mathfrak {g} ^ {0 \cdot 6 1} a.
$$

Lamont<sup>1</sup> and Lamont and Scott<sup>2</sup> dissolved, in single file fashion, relatively large $\mathrm{CO}_{2}$ bubbles into water under vertical and horizontal flow conditions. They did not vary bubble diameter or Schmidt number. At sufficiently large Reynolds numbers their horizontal and vertical results became identical. The data above these Reynolds numbers were correlated as

$$
k \sim R e ^ {0. 8 2}.
$$

Heuss, King, and Wilke<sup>13</sup> studied absorption into water of ammonia and oxygen in horizontal froth flow. The liquid phase coefficients were

controlling only in the oxygen runs and consequently they did not vary the Schmidt number and their results were also obtained as the product of ka. However, using estimates of surface area in froth flow, their data reveal

$$
\mathrm {S h} \sim \mathrm {R e} ^ {0 \cdot 9}.
$$

Hariott<sup>14</sup> reported mass-transfer coefficients for particles of boric acid and benzoic acid dissolving in water flowing cocurrently in a two-inch pipeline. A data correlation was not given but a line tangent to their data at the high flow end would indicate

$$
\mathrm {S h} \sim \mathrm {R e} ^ {0. 9 3}.
$$

Figueiredo and Charles<sup>15</sup> measured coefficients for dissolution of NaCl particles carried along as a "settling" suspension in water in horizontal flow. They correlated their data with mass-transfer coefficients previously measured for transfer between a liquid and the conduit itself. However, a line tangent to the high flow end of their data indicates

$$
\mathrm {S h} \sim \mathrm {R e} ^ {1 \cdot 1}.
$$

# Experimental-Agitated Vessels

Often the data for transfer to bubbles or particles in agitated vessels are correlated in terms of the power dissipated. Using Equation (1) we might relate these results to what would be expected for flow in conduits.

Calderbank and Moo-Young<sup>16</sup> correlated data for different particles and small bubbles dispersed in different liquids in agitated vessels. Their equation, determined partly through dimensional analysis, is

$$
k (S c) ^ {2 / 3} = 0. 1 3 \left[ \frac {\varepsilon_ {V} \mu}{\rho^ {2}} \right] ^ {1 / 4}.
$$

Using Equation (1) this would give for flow in conduits

$$
\mathrm {S h} = 0. 0 8 2 \mathrm {S c} ^ {1 / 3} \mathrm {R e} ^ {0 \cdot 6 9}. \tag {2}
$$

They also indicate that in the range of mean bubble diameters, 0.025 $\leq d_{\mathrm{VS}} \stackrel{\approx}{\leq} 0.1$ inches, the mass-transfer coefficients increase linearly, undergoing a transition from "small" bubble behavior where $\mathrm{Sh} \sim \mathrm{Sc}^{1/3}$ to "large" bubble behavior where $\mathrm{Sh} \sim \mathrm{Sc}^{1/2}$ . They conclude that this transition corresponds to a change in interfacial condition from rigid to mobile.

Sherwood and Brian $^{17}$ used dimensional analysis to correlate data for particles in different agitated liquids. Their correlation graphically related $\mathrm{Sh}_{\mathrm{b}} / \mathrm{Sc}^{1/3}$ to $(\epsilon_{\mathrm{m}} d^4 / \nu^3)^{1/3}$ . Using Equation (l) (with $\epsilon_{\mathrm{v}} / \rho = \epsilon_{\mathrm{m}}$ ) and drawing a line tangent to the high power dissipation end of their correlating curve gives

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 3} \operatorname {R e} ^ {0. 6 1} (d / D) ^ {- 0. 1 2}. \tag {3}
$$

Barker and Treybal<sup>18</sup> correlated mass-transfer coefficients for boric acid and benzoic acid particles dissolving in water and $45\%$ sucrose solutions with a stirrer Reynolds number, $\mathrm{Re}_{\mathrm{T}}$ , proportional to the speed of rotation. They reported

$$
k \sim R e _ {T} ^ {0. 8 3} S c ^ {1 / 2} \vartheta .
$$

If the power dissipation is assumed proportional to the cube of the rotation speed, then

$$
k \sim \operatorname {R e} ^ {0. 7 6} \operatorname {S c} ^ {1 / 2} \mathscr {Q}.
$$

The effect of Schmidt number is not as would be inferred from the above because $\mathfrak{D}$ was reported to be essentially proportional to $\mathrm{Sc}^{-1/2}$ in their experiments.

The preceding are representative of data available that may have direct applicability to cocurrent flow in conduits. Some other works that may be of indirect interest include cocurrent turbulent flow of dispersed liquid drops in a continuous liquid phase, $^{19-22}$ mass transfer from a turbulent liquid to a free interface, $^{23-25}$ and innumerable studies of the motions of, and mass transfer from, individual bubbles or particles under steady relative flow conditions (e.g., References 26-30).

For systems in which bubbles move steadily through a fluid, some relevant findings include the fact that, depending on bubble size and liquid properties, the bubble motion in a gravity field may vary from creeping flow to flow characterized by a turbulent boundary layer. Irrespective of this, the mass-transfer correlations usually take two basic "Frössling" forms (neglecting the constant term) depending on whether there is a rigid interface (no slip condition) or a completely mobile interface with internal circulation of the fluid within the bubble (or drop). In substantial agreement with theoretical treatments, the former data are correlated with

$$
\mathrm {S h} _ {\mathrm {b}} \sim \mathrm {R e} _ {\mathrm {b}} ^ {1 / 2} \mathrm {S c} ^ {1 / 3},
$$

and the latter

$$
\mathrm {S h} _ {\mathrm {b}} \sim \mathrm {R e} _ {\mathrm {b}} ^ {1 / 2} \mathrm {S c} ^ {1 / 2} \equiv \mathrm {P e} _ {\mathrm {b}} ^ {1 / 2}.
$$

Good accounts of these relative flow equations and their derivations are given by Lochiel and Calderbank<sup>31</sup> and by Sideman.<sup>22</sup>

# Discussion of Available Experimental Data

It is seen that there have been very few direct measurements of mass transfer to small cocirculating bubbles in a turbulent field and

none that are complete in terms of all the independent variables. The product, ka, is often not separated, because of the difficulty in establishing the interfacial area. This makes some of the available data difficult to interpret and of limited value for application at different conditions.

Not enough experimental information is available to assess the influence of Schmidt number on Sherwood number although the Schmidt number exponent most often appears to vary between $1/3$ and $1/2$ - apparently determined by the interfacial condition (the Schmidt number exponent may even be greater than $1/2$ , e.g., Reference 10).

The effects of bubble mean diameter and pipe size have received less attention than the Schmidt number and, as yet, no systematic effect can be confidently cited. Calderbank and Moo-Young, however, observed a linear dependence over a limited range of bubble diameters in agitated vessels.

The influence of Reynolds number has been the most studied. From References 9-15, it would appear that Sherwood number for gas-liquid flow in conduits may vary with pipe Reynolds number to a power between 0.9 and 1.1 (although Lamont<sup>11</sup> found it to be 0.52). In contrast, the effect of Reynolds number (turbulence level) in stirred vessels (References 16-18) would appear to yield a power between 0.6 and 0.8. This apparent difference between agitated vessels and flow in conduits is surprising because one would think that flowing through a closed conduit is just another way to stir the liquid. There should be little fundamental difference in the effect of the turbulence produced.

# Theoretical

It is convenient to identify four different analytical approaches designed to provide a description of mass transfer to bubbles from a turbulent liquid that may be applicable to cocurrent flow. The author has chosen to name these (1) Surface Renewal, (2) Turbulence Interactions, (3) Modeling of the Eddy Structure, and (4) Dimensional Analysis (Empiricism). These do not necessarily encompass all approaches and there may be considerable overlapping among areas (for example, a certain degree of empiricism is evident in each). There may be only an indirect equivalence among those within a given category.

Some representative works have been categorized according to their approach and listed in Table II. A brief discussion of each category is given below.

# Surface Renewal Models

This category is of considerable historical interest especially the original contributions of Higbie $^{32}$ and Danckwerts. $^{33}$

The so-called surface renewal models can be envisioned by imagining the interface as being adjacent to a semi-infinite fluid through which turbulent eddies having uniform concentrations characteristic of the continuous phase, periodically penetrate to "renew" the surface. The mass transfer then depends on the rate and depth of eddy penetration and the eddy residence time near the surface (or the distribution of eddy ages). For a given eddy, the original models are essentially solutions of the diffusion equation

$$
\frac {\partial \mathrm {C}}{\partial t} = \vartheta \frac {\partial^ {2} \mathrm {C}}{\partial y ^ {2}}. \tag {4}
$$

Table II. Categories of Data Correlation for Mass Transfer from a Turbulent Liquid to Gas Bubbles   

<table><tr><td>1. Surface Renewal</td><td>2. Turbulence Interactions</td></tr><tr><td>Brian and Beaverstock (40)a</td><td>Boyadzhiev and Elenkov (19)</td></tr><tr><td>Danckwerts (33)</td><td>Harriot (50)</td></tr><tr><td>Davies, Kilner, and Ratcliff (41)</td><td>Kozinski and King (24)</td></tr><tr><td>Gal-Or, Hauck, and Hoelscher (42)</td><td>Levich (36)</td></tr><tr><td>Gal-Or and Resnick (43)</td><td>Peebles (2)</td></tr><tr><td>Harriot (44)</td><td>Porter, Goren, and Wilke (20)</td></tr><tr><td>Higbie (32)</td><td>Sideman and Barsky (21)</td></tr><tr><td>King (25)</td><td></td></tr><tr><td>Koppel, Patel, and Holmes (45)</td><td></td></tr><tr><td>Kovasy (46)</td><td></td></tr><tr><td>Lamont and Scott (12)</td><td rowspan="3">4. Dimensional Analysis (Empiricism)</td></tr><tr><td>Perlmutter (47)</td></tr><tr><td>Ruckenstein (48)</td></tr><tr><td>Sideman (49)</td><td>Barker and Treybal (52)</td></tr><tr><td>Toor and Marchello (34)</td><td>Calderbank and Moo-Young (16)</td></tr><tr><td></td><td>Figueiredo and Charles (15)</td></tr><tr><td>3. Modeling of the Eddy Structure</td><td>Galloway and Sage (53)</td></tr><tr><td></td><td>Heuss, King, and Wilke (13)</td></tr><tr><td></td><td>Hughmark (54)</td></tr><tr><td>Banerjie, Scott, and Rhodes (51)</td><td>Middleman (38)</td></tr><tr><td>Fortescue and Pearson (23)</td><td>Scott and Hayduk (10)</td></tr><tr><td>Lamont (11)</td><td>Sherwood and Brian (17)</td></tr></table>

$^{\mathrm{a}}$ Reference number.

As shown by Toor and Marchello, $^{34}$ the "film" model first introduced by Whitman $^{35}$ corresponds to the asymptotic solution of this equation at long times (no surface renewal) where $k$ would be proportional to $\mathfrak{D}$ and Sherwood number would be independent of Schmidt number. The "penetration" model first introduced by Higbie $^{32}$ and later extended by Danckwerts $^{33}$ corresponds to the asymptotic solution at short times where $k$ would be proportional to $\mathfrak{S}^{1/2}$ or Sh $\sim$ $\mathrm{Sc}^{1/2}$ . Depending on the distribution of contact times between the eddies and the surface, the transfer may take on characteristics of either or both of the above.

King $^{25}$ generalized this approach to include turbulence effects by replacing Equation (4) with

$$
\frac {\partial C}{\partial t} = \frac {\partial}{\partial y} \left[ (\vartheta + \mu_ {e}) \frac {\partial C}{\partial y} \right],
$$

where $\mu_{\mathrm{e}}$ is an eddy diffusivity which he arbitrarily let vary with distance from the surface as

$$
\mu_ {e} \sim y ^ {b}.
$$

This model approaches the same asymptote (Sh $\sim$ Sc $^{1/2}$ ) at short times but different asymptotes at long times depending on the value of b (with b = 3, Sh $\sim$ Sc $^{0.35}$ ; with b = 4, Sh $\sim$ Sc $^{0.25}$ ).

To establish an overall mass-transfer rate, it is necessary to assign a frequency with which the surfaces are "renewed" (or the distribution of eddy ages). The different extensions and modifications of this model mostly involve the choice of different functions to describe the randomness of the eddy penetrations. None of these models give significant information as to the effect of bubble size, conduit size, or Reynolds number. They are mechanistically unsatisfactory because the

# 14

hydrodynamic effects are often ignored or included by relating the eddy age distribution in some way to the flow field. For example, Lamont and Scott<sup>12</sup> assumed that the fractional rate of surface renewal, s, $(k \sim \sqrt{\delta s})$ is given by

$$
s \sim \operatorname {R e} \sqrt {f}.
$$

There is really no clear-cut way to establish a relationship between the rate of surface renewal and the hydrodynamics and, consequently, there is a heavy reliance on empiricism. The original intent of these models was to describe transfer to a surface (bubble) that has a distinct steady flow relative to the liquid.

# Modeling of the Eddy Structure

If the fluid velocity field in the vicinity of the interface could be completely described, then the computation of transfer rates, in principal, would be straightforward. However, at the present time, there are no satisfactory descriptions of the details of a turbulent velocity field and even if such were available, the mathematical accounting of the differential transfer processes might become intractable. Consequently, there have been idealizations of the eddy structure with, admittedly, unrealistic fields and mass-transfer behavior has been computed based on these idealizations.

Lamont's work<sup>1</sup> provides an excellent example of this approach. He modeled the eddy structure by considering individual eddy cells that have a sinusoidal form at a sufficient distance away from the interface (corresponding perhaps to an individual component of a Fourier decomposition of the turbulent field). As the interface is approached, viscous forces dampen the eddy cell velocities by an amount that depends on the

interfacial condition (mobile or rigid). Lamont calculated the mass-transfer coefficient for an individual eddy cell as a function of the damping condition, fluid properties, the wave properties, and the eddy energy. He then used a Kovasznay distribution function for the energy spectrum and summed over a range of wave numbers to obtain the overall coefficient. The results of this procedure were

$$
k \sim (\mathrm {S c}) ^ {- 1 / 2} \left(\epsilon_ {\mathrm {m}} v\right) ^ {1 / 4}
$$

for a mobile interface and

$$
k \sim (\mathrm {S c}) ^ {- 2 / 3} \left(\epsilon_ {\mathrm {m}} v\right) ^ {1 / 4}
$$

for a rigid interface.

Using Equation (1), these give

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 2} \mathrm {R e} ^ {0 \cdot 6 9}
$$

and

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 3} \mathrm {R e} ^ {0. 6 9},
$$

respectively.

The present writer feels that this approach may represent a bridge between surface renewal models and turbulence theory and as such deserves particular mention.

# Turbulence Interactions

Some authors have attempted to analyze the forces and interactions between spheres and fluid elements in a turbulent field to arrive at equations for the fluctuating motion of the spheres. These equations are solved to obtain a "mean" relative velocity between the bubble and the fluid which is then substituted into a steady-flow equation (usually of the Frössling type) to establish the mass-transfer coefficients. The work of Levich<sup>36</sup> is of this nature and Peebles<sup>2</sup> used this approach in

his document. For example, Peebles used the result of $\mathrm{Hinze}^{37}$ for small gas bubbles

$$
\sqrt {v _ {g}} ^ {2} \cong 3 \sqrt {v _ {\ell}} ^ {2}
$$

which essentially comes from an integration of the equation

$$
\frac {\pi d ^ {3}}{6} \left(\rho_ {g} + W \rho\right) \frac {d v _ {g}}{d t} = \frac {\pi d ^ {3}}{6} \rho (1 + W) \frac {d v _ {\ell}}{d t},
$$

where $W$ is an added mass coefficient for an accelerating spherical bubble. The relative velocity is then

$$
v _ {b} = \sqrt {v _ {g} ^ {2}} - \sqrt {v _ {\ell} ^ {2}} = 2 \sqrt {v _ {\ell} ^ {2}}.
$$

Peebles used the approximations

$$
\sqrt {v _ {\ell} ^ {2}} \sim V \sqrt {f / 2} a n d f \sim R e ^ {- 1 / 5}
$$

in the above which were then substituted into Frössling type equations to obtain $\mathrm{Sh} \sim \mathrm{Re}^{0.45} \, \mathrm{Sc}^{1/2} (\mathrm{d}/\mathrm{D})^{-1/2}$ for a mobile interface and $\mathrm{Sh} \sim \mathrm{Re}^{0.45} \, \mathrm{Sc}^{1/3} (\mathrm{d}/\mathrm{D})^{-1/2}$ for a rigid interface.

In a similar computation which included Stokes law to describe the drag experienced by the bubble, Levich<sup>36</sup> obtained for a mobile interface

$$
\mathrm {S h} \sim \mathrm {R e} ^ {3 / 4} \mathrm {S c} ^ {1 / 2}.
$$

# Dimensional Analysis (Empiricism)

Some workers have chosen to postulate the physical variables that may be controlling and have used standard dimensional analysis techniques for ordering the experimental data. The paper by Middleman<sup>38</sup> is a splendid example of this approach as applied to agitated vessels. Also for agitated vessels, Calderbank and Moo-Young<sup>16</sup> used dimensional analysis to obtain Equation (2) and Sherwood and Brian<sup>17</sup> dimensionally related $\mathrm{Sh}_{\mathrm{b}} / \mathrm{Sc}^{1/3}$ to $[\varepsilon_{\mathrm{m}} \mathrm{d}^4 / \mathrm{v}^3]^{1/3}$ .

Also included under this category is a most interesting correlation by Figueiredo and Charles<sup>15</sup> for a heterogeneous pipeline flow of settling particles. They used an expression for the ratio of pressure gradient for flow of the suspension to the pressure gradient for flow of the liquid alone and assumed that, if altered by the ratio $\frac{d}{D}$ , it could also represent the ratio of mass-transfer coefficients for the particles to those for transfer from the liquid to the pipe wall. They found that they could, indeed, use this ratio to correlate their data for a settling suspension with the data of Harriot and Hamilton.<sup>39</sup>

# Discussion

It is seen that the theoretical description of mass transfer to bubbles in cocurrent turbulent flow has by no means been standardized. There seems to be somewhat general agreement as to the effect of Schmidt number. The Sherwood numbers for cases of completely rigid interfaces with zero tangential velocity at the surface (no slip) applicable to solid spheres, very small bubbles, and bubbles with surfactant contamination in the interface are generally predicted to vary with Schmidt number to the one-third power. Completely mobile interfaces (negligible tangential stress with non-zero interfacial velocity) are generally predicted to yield a $\mathrm{Sc}^{1/2}$ variation of Sh.

There is only scant and inconsistent information predicting the effects of bubble and conduit diameter. For example, Levich predicts no effect of d/D while Peebles predicts Sh $\sim$ (d/D) $^{-1/2}$ .

There is general disagreement as to the effect of Reynolds number as evidenced by the fact that exponents have been predicted that range

from 0.45 to $>1$ . These different exponents may not be mutually exclusive, however because an inspection of the experimental data shows disagreement in the measured exponents also. It may be that the proper application of these equations depends on suitable evaluation of the conditions of the experiment.

# CHAPTER III

# DESCRIPTION OF EXPERIMENT

This experiment was designed to measure liquid phase controlled mass-transfer coefficients for cocurrent pipeline flow of turbulent liquids with up to $1\%$ volume fraction of small helium bubbles having mean diameters from 0.01 to 0.05 inches. The liquids chosen were five mixtures of glycerine and water (0, 12.5, 25, 37.5, and $50\%$ by weight of glycerine) each of which represent a different Schmidt number. The physical properties of these mixtures, obtained from the literature,[55] are shown graphically in Appendix A and the values used in this study for the given mixtures are listed in Table III.

# Transient Response Technique

A closed recirculating system was used in which helium bubbles were introduced (generated) at the entrance of a well-defined test section and removed richer in oxygen at the exit, allowing only the bubble-free liquid to recirculate.

The products of mass-transfer coefficients and interfacial areas were measured by a transient response technique in which the system was initially charged with dissolved oxygen. The oxygen was then progressively removed by transfer to the helium bubbles while the oxygen concentration was continuously monitored as a function of time at a single position in the system.

For a test section of length, L, and cross-sectional area, A, it can be shown (Appendix B) that the ratio of exit concentration to inlet

Table III. Physical Properties of Aqueous-Glycerol Mixtures (25°C) Data of Jordan, Ackerman and Berger   

<table><tr><td>Glycerol 
Content 
(wt %)</td><td>Density, ρ 
(lb/ft3)</td><td>Viscosity, μ 
(lb/ft·hr)</td><td>Henry&#x27;s Law 
Constant, H 
(atm·liters/mole)</td><td>Molecular 
Diffusivity of 
Oxygen, Ω × 105(ft2/hr)</td><td>Schmidt 
Modulus, Sc 
(Dimensionless)</td></tr><tr><td>0</td><td>62.43</td><td>2.15</td><td>795.4</td><td>8.215</td><td>419</td></tr><tr><td>12.5</td><td>64.43</td><td>3.07</td><td>1127.6</td><td>12.865</td><td>370</td></tr><tr><td>25</td><td>66.49</td><td>4.62</td><td>1421.0</td><td>9.261</td><td>750</td></tr><tr><td>37.5</td><td>67.67</td><td>6.34</td><td>1621.8</td><td>4.650</td><td>2015</td></tr><tr><td>50</td><td>69.86</td><td>10.82</td><td>2011.1</td><td>4.495</td><td>3446</td></tr></table>

concentration, $\mathrm{C_e / C_i}$ , is a constant, K, given by

$$
K \equiv C _ {e} / C _ {i} = \frac {\gamma + e ^ {- 3}}{1 + \gamma}, \tag {5a}
$$

where

$$
\gamma = \frac {\mathrm {R T Q} _ {\ell}}{\mathrm {H Q} _ {\mathrm {g}}} \text {a n d} \theta = \frac {\operatorname {k a A L} (1 + \gamma)}{Q _ {\ell}}. \tag {5b}
$$

In the absence of axial smearing, each time the fluid makes a complete passage around the closed circuit (loop transit time, $\tau$ , $\equiv V_{s} / Q_{l}$ ) the concentration at the measuring position would (ideally) decrease instantaneously from its value, $C$ , to a value equal to KC. Therefore, in actuality, the ratio, $C / C_{o}$ , of the concentration at any time to that at an initial reference time (set equal to zero) would be given by

$$
C / C _ {o} = \operatorname {E x p} \left[ - \frac {\left(\varrho n K\right) t}{T} \right] = \operatorname {E x p} \left[ - \frac {\left(\varrho n K\right) Q _ {e} t}{V _ {s}} \right].
$$

Therefore a plot of $\frac{\partial n}{\partial C_{0}}$ versus time would be a straight line of slope $-\left(\frac{\partial n}{\partial K}\right) Q_{2} / V_{s}$ . Note that the absolute value need not be measured because a signal that is merely proportional to the oxygen concentration would have the same slope. If the system volume, $V_{s}$ , and the liquid volumetric flow rate, $Q_{2}$ , have been measured, the constant $K$ can be extracted from the slope of the measured transient. Having a measure also of gas volumetric flow, $Q_{g}$ , and the system absolute temperature, $T$ , and knowing $R$ , $H$ , $A$ , and $L$ , the product, $ka$ , can be obtained from $K$ through Equations (5). If an independent measure is also made of "a," then the mass-transfer coefficients are fully determinable.

This technique was selected as being superior to a once-through test that requires an independent measurement of the oxygen concentration at both ends of the test section for reasons illustrated by the following comparison.

In a once-through system with a $37.5\%$ mixture and conservative values of $\mathsf{Q}_{\mathsf{g}} / \mathsf{Q}_{\mathsf{\ell}} = 1\%$ , bubble mean diameter $= 0.01$ inches, Reynolds number $= 6 \times 10^{4}$ , and a mass-transfer coefficient of 0.7 ft/hr, a test section length of $\sim 100$ feet would be required to obtain a concentration change across the test section of only

$$
C _ {e} / C _ {i} = 0. 9 \quad .
$$

At this level a small error in the concentration measurement would be magnified in the determination of ka. In contrast, the same conditions in a transient test with only a 25-ft-long test section would give a concentration change of $\mathrm{C} / \mathrm{C}_0 \sim 0.1$ in only about seven minutes - greatly reducing the error magnification in ka. In return for this benefit, the values of total system volume, $V_s$ , and the time coordinate, $t$ , need also to be measured. These, however, are parameters that can be measured very precisely compared to the concentration measurement. Therefore, the transient tests should result in more reliable data.

On the other hand, the concentrations in once-through tests are measured at specific locations that bracket the region of interest and only the transport behavior within that region is important. Whereas in the transient tests all mass transfer occurring outside the test section is extraneous and represents an "end effect" contribution that must be independently measured and accounted for in determining the "ka" product. This "end effect," which would include mass transfer occurring in the

bubble generating and separating processes, represents the most serious disadvantage and error source in the transient measurements. The measurement and accounting for the "end effect" are discussed further on page 47.

# Apparatus

In constructing the main circulating systems of the experiment exclusive use was made of stainless steel or glass hardware and all gaskets were Teflon. This was part of careful measures taken to keep the system free of contamination. Figure 1 is a photograph of the facility with the test section mounted in the vertical orientation and Figure 2 is a diagram of the main circuit portion. Figure 28, page 121 (Appendix C) is an instrument application drawing of the system which includes an auxiliary flow circuit used for rotameter calibration and for special tests.

The main circuit consisted of a canned rotor centrifugal pump, three parallel rotameters, a heat exchanger, three dissolved oxygen measuring sensors, a helium flow and metering system, a bubble generator, the test section, a bubble separator, a photographic arrangement for determining the bubble interfacial areas and mean diameters, and a drain-and-fill tank equipped with scales for precise determination of the weight percent of glycerine in the mixture. Further descriptions of individual components are given below.

# Pump

The main circulator was a 20 HP Westinghouse "100-A" canned rotor constant speed centrifugal pump capable of delivering about 100 gpm at

![](images/7e66c2468801b24e79e074525559db6a6d0aca2fdd683710ab0566ee2c158edc.jpg)  
Figure 1. Photograph of the Mass Transfer Facility.

![](images/932aef38d1ddd75feca78d7d9bc75235419adb11d326bd3cf034398d9fff1e35.jpg)  
Figure 2. Schematic Diagram of the Main Circuit of the Experimental Apparatus.

about 180 feet of head. The motor cannings, housing, and impeller were stainless steel and the bearings were graphite - lubricated solely by the loop fluid. An auxiliary circuit required to cool the pump motor windings circulated transformer oil through the windings and through an external circuit containing an auxiliary oil pump, a filter, and a small water-cooled heat exchanger. The pump was safety instrumented to turn off on loss of pressure in the oil circuit or on high temperature of the motor housing.

# Liquid Flow Measurement

The liquid flow rate was controlled by three parallel stainless steel globe valves downstream of the pump at the entrances to the rotameters. Three parallel rotameters of different capacities (100, 40, and 8 gpm) were used for measuring liquid volumetric flow rates. By judicious use of the rotameter scales, parallel rotameters provide greater precision when measurements are required over a wide flow range. In each experiment, however, some flow was allowed to go through each rotameter to prevent having regions that might "lag" the rest of the loop during the transient tests and thereby become concentration "capacitance" volumes.

Because of the large differences in viscosities over the range of glycerine-water mixtures used, the rotameters were calibrated, in place, for both water and a $50\%$ mixture. These calibrations were obtained by the use of two identical 6-inch-diameter, 6-feet-long glass tanks in the auxiliary circuit valved together in such a way that, while one was being filled, the other was being drained. Changing the position of one lever reversed the process before the liquid could spill over the top.

The time required to fill (or empty) a known volume of either of these tanks was measured over the entire range of each rotameter. These calibrations are given in Appendix D.

Since there was only a small difference in the calibration between 0 to $50\%$ glycerine, the flow for in-between mixtures was determined by linearly interpolating between the two curves according to the viscosity.

# Temperature Stabilization

The fluid temperature was measured at the inlet and exit of the test section by standard stainless steel sheathed chromel-alumel thermocouples immersed in the fluid. The friction and pump heat were removed and the test section temperature held at $25^{\circ}\mathrm{C}$ for all tests by a stainless-steel, water-cooled, shell-and-tube heat exchanger.

# Gas Flow Measurement

Helium for generation of the bubbles was obtained from standard commercial cylinders metered through a pressure regulator, a safety relief valve, and a flow control needle valve. The rate of helium flow was determined by measuring both the exit pressure and the pressure drop across a 6-foot length of tubing of about 1/16-inch internal diameter. These measurements were made with a Bourden type pressure gage and a water-filled U-tube manometer, respectively.

Calibration at atmospheric conditions was obtained prior to operation by comparing with readings from a wet-test meter timed with a stop watch. The calibration at 50 psig exit pressure (normal operating condition) is given in Figure 33, page 127(Appendix D). The calibration

and the leak tightness of this system were checked periodically over the course of the experimental program.

# Dissolved Oxygen Measurement

Two identical commercially available "Polarographic" type instruments were used to measure the dissolved oxygen concentration (Magna Oxymeter Model 1070, Magna Corporation-Instrument Division, 11808 South Bloomfield Avenue, Santa Fe Springs, California). Two were used so that an automatic continuous check was provided by comparing the readings of one with the other. It was felt unlikely that both would use up their electrolyte or fail simultaneously. These instruments used polarographic type sensors inserted into the flowing liquid through penetrations in tees provided for that purpose. Electrical signals produced by the sensors were fed through recording adaptors and the resulting millivolt signals recorded on a Brown Multipoint recorder having a measured chart speed of 1.18 inches/sec.

Each sensor assembly consisted of an electrolytic cell made up of a cathode, anode, and an electrolyte mounted in a plastic cylindrical housing. The end of the housing, containing the cell, was encased in a thin oxygen-permeable Teflon membrane which also acted to contain the electrolyte. The dissolved oxygen is electrolytically reduced at the cathode causing a current to flow through the system from cathode to anode. The magnitude of this current is proportional to the oxygen concentration if sufficient liquid velocity exists ( $\sim$ 2 ft/sec) to prevent concentration polarization at the membrane.

The response times for these instruments are greater than $90\%$ in 30 seconds. An analysis showing that this response produces an acceptable error in the transient tests is given in Appendix E.

Since the transient response technique used in these tests requires a signal that is merely proportional to the oxygen concentration, an absolute calibration of these instruments was not necessary. Nevertheless calibration tests were made for two different mixtures of glycerine and water by bubbling air through the mixtures at different pressures until they became saturated. Knowing the solubility of oxygen in the mixtures, the meter reading could be set on the calculated concentration for an initial "set-point" pressure and subsequent readings at different pressures compared with calculated values (assuming a Henry's Law relationship). Calibrations obtained in this manner are shown on Figure 34, page 128 (Appendix D) which includes readings made with a third instrument similar to the Magna instruments but made by a different company. The response speed of this third sensor proved to be slow compared to the Magna sensors and consequently it was used only as an independent monitor on the operability of the Magna sensors throughout these experiments.

# Bubble Generation

Special apparatus was required that could generate a dispersion of small bubbles whose mean size could be controlled and varied over the range 0.01 to 0.05 inches independently of the particular liquid mixture being used and of the flow rates of gas and liquid. Two devices considered and discarded as being inadequate were (1) a fine porosity fritted glass disc through which the gas was blown into the liquid, and

(2) two parallel stainless steel discs, a rotor and a stator, each equipped with intermingling blades. The gas-liquid mixture flowed between the blades and the gas was broken into fine bubbles by the shearing action.

The bubble generator designed and developed for this project is shown diagrammatically on Figure 3. The liquid flowed through a converging diverging nozzle with a 1-inch-diameter throat and a 2-inch-diameter entrance and exit. The section downstream of the throat diverged at an angle of about 12 degrees. A central "plumb-bob" shaped probe of maximum cross-sectional diameter of $\sim0.812$ inches was movable and could be centrally positioned anywhere in the diverging section including the throat and exit. This probe was supported by a tube which carried the gas into the system. The tube, in turn, was supported by a "Swagelok" fitting penetrating a flange on the end of the straight leg of a tee connected to the nozzle entrance. Four small positioning rods near the throat centered the probe within the nozzle and helped support it. They also acted as holders for a section of "honey-comb" straightening vanes used to minimize the liquid swirl induced by the right angle turn at the tee entrance to the nozzle.

Gas entered the liquid through 48 holes (1/64-inch-diameter) around the probe periphery at its maximum thickness and exited as a series of parallel plumes which were broken into individual bubbles by the turbulence in the diverging section of the nozzle. The mean bubble size for a given flow and mixture was controlled by the position of the probe within the nozzle (the closer the probe was to the throat the smaller the mean bubble size produced).

![](images/f9d820c02c17c4e75ed4deb560913307517b7a0227f08378e344923e2d88d792.jpg)  
Figure 3. Diagram of the Bubble Generator.

Bubbles generated by this device were found to follow closely a size distribution function proposed by Bayens $^{56}$ and previously used to describe droplet sizes produced in spray nozzles.

The function, defined as $f(\delta) \mathrm{d}\delta \equiv$ that fraction of the total number of bubbles that have diameters, $\delta$ , lying in the range $\delta \pm 1/2$ dδ, is given by

$$
f (\delta) = 4 \left(\alpha^ {3} / \pi\right) ^ {1 / 2} \delta^ {2} \operatorname {E x p} (- \alpha \delta^ {2}) \tag {6}
$$

in which

$$
\alpha = [ 4 \sqrt {\pi} N / 6 \Phi ] ^ {2 / 3}.
$$

This function has been normalized so that

$$
\int_ {0} ^ {\infty} f (\delta) d \delta = 1.
$$

An indication of the suitability of this distribution function is given in Figure 4 where measured cumulative size distributions for bubble populations produced by the bubble generator are compared with the distributions calculated from the function at different liquid flows and different ratios of gas to liquid flows. The measured distributions were obtained by painstakingly scaling the sizes of a sufficient number of bubbles directly off photographs taken of the bubble swarms at each condition. These measured areas should be accurate within about $10\%$ .

The range of mean bubble sizes capable of being produced by this bubble generator were measured at a constant gas-to-liquid volumetric flow ratio, $\frac{Q_g}{Q_\ell}$ , of 0.3% at different liquid flow rates, different mixtures of glycerine and water, and different probe positions. The results are shown on Figure 29, page 123 (Appendix D). The mean

![](images/d4d5349ea1d7f4f37316ae73c669cd25b3168f749dcef0e863b4b0aaf14e1370.jpg)  
Figure 4. Comparison of Measured Bubble Sizes with the Distribution Function.

diameter used throughout this report is the "Sauter" mean defined by

$$
d _ {v s} \equiv \frac {\int_ {0} ^ {\infty} \delta^ {3} f (\delta) d \delta}{\int_ {0} ^ {\infty} \delta^ {2} f (\delta) d \delta}, \tag {7}
$$

which is the volume-to-surface weighted mean commonly used in mass-transfer operations.

# Bubble Separation

Since this project uses the transient mode of testing, bubbles that recirculate and extract dissolved oxygen from the liquid in regions outside the test section constitute an error source in the measurements. Consequently a high degree of separation is desirable for this method of testing. Some techniques considered were (1) gravitational separation in a tank, (2) centrifugal separation through the use of vanes to induce a strong vortex, and (3) separation by flowing through a porous metal which might act as a physical barrier to the bubbles. Each of these had shortcomings that prevented their use in this project. For example, with gravitational separation the tank size required for the viscous mixtures was ponderously large. This increases the system volume resulting in a "sluggish" loop and an accompanying increase in the measurement error.

With centrifugal separation there were problems in stabilizing the gaseous core of the vortex over a wide range of operating conditions. In addition, large by-pass of bubbles (inefficient separation) was observed and there was too much liquid carryover through the gas removal duct.

The porous physical barriers tested required large frontal areas or had prohibitive pressure drops, and the bubbles were observed to regularly penetrate these barriers.

A satisfactory separator was finally developed that combined features of each of the above. A diagram of this separator is shown on Figure 5. The liquid-bubble mixtures entered the bottom of a 6-inch-diameter pipe. A series of plexiglas vanes just beyond this entrance created a swirl flow within the tank which tended to force the bubbles to the middle. The spinning mixture flowed upward into a converging cone-shaped region with sides of 500-mesh stainless steel screen. When wetted by the liquid, the screen acted as a physical barrier to the bubbles but allowed the liquid to pass through. The liquid exited from the separator while the bubbles continued to rise through the truncated end of the conical screen to an interface where the gas was vented through a small exit line. The system pressure level was also controlled at this interface by providing an auxiliary sweep of helium through the exit line.

Good separation was achieved with this apparatus over the test conditions of this thesis. No bubbles could be detected in photographs taken downstream of the separator. However, with the use of a light beam, some bubbles that appeared to be smaller than the screen mesh size could be detected visually. After passing through the pump and entering a higher pressure region these bubbles apparently went into solution because they could no longer be visually detected downstream of that region. If indeed they did go into solution along with their small amount of extracted oxygen, they would have hardly constituted

![](images/d27ff757a0d215337e60764abefc19b9e3f73548171cf8c6514daca7783f5ae3.jpg)  
Figure 5. Diagram of the Bubble Separator.

a significant error in the mass-transfer measurements. Nevertheless, several "special" tests were made in which about $10\%$ of the normal gas flow was purposely introduced downstream of the separator and allowed to recirculate. The measured rates of change in loop concentration under these conditions were always less than $3\%$ of the normal rate and the effect of the apparently much smaller amounts of by-pass therefore were felt to be acceptable.

This separator was the major factor in limiting the ranges of Reynolds numbers that could be obtained in this system. For a given mixture, as flow was increased a flow rate was eventually reached at which there was an observed "breakthrough" of many large bubbles that would continue to recirculate. At this level of flow it was necessary to terminate the tests with the particular mixture.

In addition to the flow limiting aspect of the separator, an unexpected large amount of mass transfer occurred there - probably due to the energy dissipation of the swirl and the relatively large amount of contact time between the liquid and gas. Consequently a larger than anticipated "end effect" resulted that had to be accounted for in determining the mass-transfer coefficients applicable to the test section only. This correction resulted in decreased reliability of the results.

# Test Section

The test section was considered as that portion of conduit between the bubble generator exit and the entrance of an elbow leading into the separator entrance pipe (see Figure 1, page 24). It consisted of five sections of 2-inch-diameter conduit flanged together with Teflon gaskets. As encountered in the direction of flow these were a 4-foot-long section

of glass pipe, a 10-foot-long section of glass pipe, a 6 1/2-foot-long section of stainless steel "long-radius" U-bend, another 10-foot-long section of glass pipe, and a 5-foot-long section of glass pipe, for a total of 35 1/2 feet of length. The test section and bubble generator were connected to the rest of the loop piping through the bubble generator tee at the entrance and an elbow at the exit which served as pivot points to permit the test section to be mounted in any orientation from horizontal to vertical.

# Bubble Surface Area Determination - Photographic System

The mean sizes and interfacial areas per unit volume of the bubble dispersions were determined photographically using a Polaroid camera and two Strobolume flash units. To reduce distortion the photographs were taken through rectangular glass ports fitted around the cylindrical glass conduit and filled with a liquid having the same index of refraction as the glass. The port for "inlet" pictures was located about one foot downstream from the bubble generator exit and the "exit" port was located about two feet upstream from the test section exit.

The Polaroid camera was equipped with a specially made telescopic lens that permitted taking photographs in good focus across the entire cross section of the conduit. The camera was semi-permanently mounted onto the facility structure in such a manner that photographs could be taken at the "inlet" port and then the camera pivoted for taking a subsequent picture through the "exit" port. For vertical orientation of the test section, photographs were taken directly through the ports.

For horizontal tests, the camera remained in its "vertical orientation" position and the photographs were taken through high quality front surface mirrors.

With the camera focused along the axis of the conduit, bubbles closer to the camera appear larger and those further away appear smaller. To determine the magnitude of this possible error source, small wires of known diameter were mounted inside the conduit across the cross section. Photographs obtained after focusing on the central wire indicated less than one percent maximum error in the apparent diameter reading.

The Strobolum flash units (one for each port) produced pictures of best contrast when mounted to provide diffuse back lighting in which the lights were aimed directly into the camera lens from behind the photo ports. Semi-opaque "milky" plexiglas sheets between the lights and the photo ports served as the light diffusers.

Bubble diameters could have been scaled directly off the photographs for each run and used to establish the interfacial areas and mean diameters just as was done to validate the bubble size distribution function. However, this proved to be such an onerous and time-consuming procedure that it would have been prohibitive due to the large number of experimental runs and need for at least two photographs for each run. Consequently, the following use was made of the distribution function.

The interfacial area per unit volume is defined as

$$
a = \int_ {0} ^ {\infty} N \pi \delta^ {2} f (\delta) d \delta \tag {8}
$$

and the bubble volume fraction is given by

$$
\Phi \equiv \int_ {0} ^ {\infty} \frac {N \pi \delta^ {3}}{6} f (\delta) d \delta .
$$

Recalling the definition of the Sauter mean diameter, Equation (7), it is seen from the above that, regardless of the form of the distribution function, the interfacial area per unit volume can be expressed as

$$
a \equiv \frac {6 \Phi}{d _ {\text {v s}}} \tag {9}
$$

For the distribution function of Equation (6), Equation (8) may be integrated to give

$$
a = \frac {3}{2} \left(\frac {6 \pi}{4}\right) ^ {2 / 3} N ^ {1 / 3} \Phi^ {2 / 3} \cong 4. 2 2 N ^ {1 / 3} \Phi^ {2 / 3}. \tag {10}
$$

Therefore, by measuring the volume fraction, $\Phi$ , it was only necessary to count the number of bubbles per unit volume from the photographs and use Equation (10) to establish the areas. Equation (9) was then used to determine the mean bubble diameters. Counting the number of bubbles in a representative area of the photographs was a considerably easier task than measuring the actual sizes of each bubble. However, it was then necessary to have an independent determination of the volume fraction occupied by the bubbles.

Hughmark $^{54}$ presented a volume fraction correlation that graphically related a flow parameter, X, defined from

$$
\frac {\rho Q _ {\ell}}{\rho_ {g} Q _ {g}} = 1 - \frac {\rho}{\rho_ {g}} \left(1 - \frac {X}{\Phi}\right) \tag {11}
$$

to the parameter

$$
Z \equiv (\operatorname {R e}) ^ {1 / 6} (\operatorname {F r}) ^ {1 / 8} / Y ^ {1 / 4},
$$

where

$$
Y \equiv Q _ {\ell} / (Q _ {\ell} + Q _ {g})
$$

For $\rho >> \rho_{\mathrm{g}}$ , Equation (11) reduces to

$$
\Phi \cong X Q _ {g} / Q _ {\ell}. \tag {12}
$$

Hughmark's correlation for X at sufficiently large Z is nearly flat with X changing from 0.7 to 0.9 over a 10-fold change in Z. For the conditions of the experiments in this report, X was considered to be constant at an average value of 0.73.

When volume fractions were measured in the vertical flow tests, it was found that

$$
\Phi = 0. 7 3 \mathrm {Q} _ {\mathrm {g}} / \mathrm {Q} _ {\ell}
$$

gave a good measure of the mean value for a given test but that the volume fractions were sometimes considerably smaller than this in the riser leg of the test section and, at the same time, comparably larger in the downcomer. It was apparent that this difference was due to buoyancy driven relative flow between the bubbles and the liquid. Separate volume fractions were therefore determined for each leg based on a mass balance. This mass balance between the riser and downcomer sections in a constant area conduit takes the form

$$
\left(\mathrm {N V}\right) _ {\mathbf {r}} = \left(\mathrm {N V}\right) _ {\mathbf {d}}.
$$

Letting

$$
V _ {r} = V + V _ {b}
$$

and

$$
V _ {d} = V - V _ {b}
$$

then

$$
\Phi_ {d} / \Phi_ {r} \equiv N _ {d} / N _ {r} = \frac {V + V _ {b}}{V - V _ {b}}. \tag {13}
$$

The bubble terminal velocity, $V_{b}$ , depends on the bubble Reynolds number, $Re_{b}$ ( $\equiv V_{b} d_{vs} / v$ ).

If $\mathbf{Re}_{\mathfrak{b}} < 2$ , then Stokes law results in

$$
V _ {b} = \frac {d ^ {2} v s g (\rho - \rho_ {g})}{1 8 \mu}.
$$

If $\mathsf{Re}_{\mathsf{b}} > 2$ , then $\mathbf{V}_{\mathbf{b}}$ is determined from a balance between the drag force $[(C_{d} \rho V_{b}^{2} / 2g_{c})(\pi d_{vs}^{2} / 4)]$ and buoyancy $(\rho \pi d_{vs}^{3} g / g_{c}6)$ to be

$$
V _ {b} = \left[ \frac {4}{3} \frac {d _ {v s} g}{C _ {d}} \right] ^ {1 / 2},
$$

where the drag coefficient, $C_d$ , is given by

$$
C _ {d} = 1 8. 5 / R e _ {b} ^ {0 \cdot 6}.
$$

It was further assumed that the average of the riser and downcomer volume fractions could be calculated by

$$
\frac {\Phi_ {r} + \Phi_ {d}}{2} = 0. 7 3 Q _ {g} / Q _ {l}. \tag {14}
$$

Then with iterations to establish $\mathrm{d}_{\mathrm{vs}}$ , $\mathrm{V}_{\mathrm{b}}$ , and $\mathrm{Re}_{\mathrm{b}}$ , Equations (13) and (14) were solved to determine the individual leg vertical flow volume fractions, and Equation (10) was used to establish the interfacial areas per unit volume. The averages were used to extract the mass-transfer coefficients from the ka products.

As a further indication of the accuracy of the distribution function and the validity of this technique for establishing the vertical flow surface areas, Figure 6 compares some surface areas determined as outlined above with the areas measured directly from the photographs. The experimental conditions for the run numbers identifying each point are listed in Table IV.

In horizontal flows the volume fractions were the same in each leg but stratification of the bubbles near the top of the conduit, especially

![](images/db333406cf4a49da44f1270f3e4f6a8171937dc8496a5dc03641c1f249bb8bf8.jpg)  
$a_{c}$ , CALCULATED INTERFACIAL AREA PER UNIT VOLUME (in.1)   
Figure 6. Comparison of Interfacial Areas Per Unit Volume Measured Directly from Photographs with Those Established Through the Distribution Function. Vertical Flow.

Table IV. Experimental Conditions for Runs Used to Validate Surface Area Determination Method for Vertical Flows   

<table><tr><td>Run No.</td><td>Ql(gpm)</td><td>Qg/Ql(%)</td><td>Mixture
(% glycerine)</td></tr><tr><td>71</td><td>20</td><td>0.5</td><td>0</td></tr><tr><td>73</td><td>20</td><td>0.1</td><td>0</td></tr><tr><td>76</td><td>20</td><td>0.1</td><td>0</td></tr><tr><td>83</td><td>40</td><td>0.5</td><td>0</td></tr><tr><td>85</td><td>40</td><td>0.1</td><td>0</td></tr><tr><td>87</td><td>40</td><td>0.3</td><td>0</td></tr><tr><td>91</td><td>60</td><td>0.1</td><td>0</td></tr><tr><td>92</td><td>60</td><td>0.5</td><td>0</td></tr><tr><td>93</td><td>60</td><td>0.3</td><td>0</td></tr><tr><td>100</td><td>80</td><td>0.1</td><td>0</td></tr><tr><td>104</td><td>80</td><td>0.5</td><td>0</td></tr><tr><td>119</td><td>20</td><td>0.5</td><td>50</td></tr><tr><td>130</td><td>40</td><td>0.5</td><td>50</td></tr><tr><td>142</td><td>10</td><td>0.5</td><td>50</td></tr><tr><td>155</td><td>50</td><td>0.3</td><td>50</td></tr><tr><td>162</td><td>20</td><td>0.5</td><td>37.5</td></tr><tr><td>165</td><td>30</td><td>0.5</td><td>37.5</td></tr><tr><td>171</td><td>40</td><td>0.5</td><td>37.5</td></tr><tr><td>198</td><td>40</td><td>0.5</td><td>37.5</td></tr><tr><td>213</td><td>20</td><td>0.5</td><td>37.5</td></tr><tr><td>217</td><td>40</td><td>0.5</td><td>37.5</td></tr></table>

at low flows, invalidated the use of Equation (14). It was found possible however to correlate the horizontal flow volume fractions at $\mathsf{Q}_{\mathsf{g}} / \mathsf{Q}_{\mathsf{l}} = 0.3\%$ with the ratio, $\mathrm{V} / \mathrm{V}_{\mathrm{b}}$ , of the axial liquid velocity to the bubble terminal velocity in the liquid. This correlation is shown in Figure 7 with the identification of the randomly selected runs given in Table V.

Table V. Experimental Conditions for Runs Shown on Horizontal Flow Volume Fraction Correlation   

<table><tr><td>Run No.</td><td>Ql(gpm)</td><td>dvs(inches)</td><td>Mixture(% glycerine)</td></tr><tr><td>376</td><td>35</td><td>0.033</td><td>50</td></tr><tr><td>390</td><td>50</td><td>0.028</td><td>50</td></tr><tr><td>382</td><td>40</td><td>0.059</td><td>50</td></tr><tr><td>389</td><td>50</td><td>0.024</td><td>50</td></tr><tr><td>391</td><td>30</td><td>0.037</td><td>50</td></tr><tr><td>365</td><td>60</td><td>0.026</td><td>0</td></tr><tr><td>355</td><td>30</td><td>0.049</td><td>0</td></tr><tr><td>370</td><td>30</td><td>0.014</td><td>50</td></tr><tr><td>368</td><td>70</td><td>0.014</td><td>0</td></tr><tr><td>400</td><td>30</td><td>0.066</td><td>37.5</td></tr><tr><td>404</td><td>35</td><td>0.061</td><td>37.5</td></tr><tr><td>422</td><td>55</td><td>0.026</td><td>37.5</td></tr><tr><td>427</td><td>60</td><td>0.030</td><td>37.5</td></tr></table>

For $\mathrm{V} / \mathrm{V}_{\mathrm{b}}$ less than 30, a least squares line,

$$
\Phi = 0. 0 0 1 8 + 0. 0 2 1 / \left(\mathrm {V} / \mathrm {V} _ {\mathrm {b}}\right), \tag {15}
$$

was used while for $\mathrm{V} / \mathrm{V}_{\mathrm{b}}$ greater than 30 a constant value,

$$
\Phi = 0. 0 0 2 5,
$$

was used. Severe stratification prevented experimentation at values of $\mathrm{V} / \mathrm{V}_{\mathrm{b}}$ less than about 3.

![](images/f0ac7be9819a8cd7bae2df8db01933303f4576a2ca9c92fdc155fd731d8692cf.jpg)  
$\Phi$ , BUBBLE VOLUME FRACTION   
Figure 7. Correlation of Horizontal Flow Volume Fraction.

This horizontal flow volume fraction correlation in conjunction with Equation (10) was used to establish the horizontal flow interfacial areas per unit volume. An indication of the adequacy of this procedure is given in Figure 8 in which calculated and measured areas are compared for the runs identified in Table V.

# End Effect

In the transient response mode of operation all mass transfer occurring outside the test section (principally in the bubble separator and generator) must be independently measured and accounted for in establishing the ka products applicable only to the test section.

"End-effect" measurements were made after all other scheduled tests were completed by moving the bubble generator to a position at the test section exit which allowed the bubbles to flow directly from the generator into the separator - effectively by-passing the test section. All tests were then repeated duplicating as nearly as possible the original conditions. With the end-effect response so measured, the correction was determined as follows.

Consider three regions of mass transfer in series representing the bubble generator (Region 1), the test section (Region 2), and the bubble separator (Region 3). The original measurements, indicated here by a subscript "I," determined the ratio, $\mathrm{K_I}$ , of the outlet to inlet concentration across all three regions. Therefore

$$
\mathrm {K} _ {\text {工}} = \mathrm {K} _ {1} \quad \mathrm {K} _ {2} \quad \mathrm {K} _ {3},
$$

where $\mathbf{K}_1, \mathbf{K}_2$ , and $\mathbf{K}_3$ are the outlet and inlet concentration ratios across the individual regions.

$a_{c}$ , CALCULATED INTERFACIAL AREA PER UNIT VOLUME (in.1)   

<table><tr><td colspan="9">HORIZONTAL FLOW IN 2-in. DIAMETER CONDUCT</td></tr><tr><td colspan="9">an = MEASURED DIRECTLY FROM
PHOTOGRAPHS
ac = 4.22 N/3 Φ2/3 (FROM DISTRIBUTION
FUNCTION)
VOLUME FROM PHOTOS RAPHS
1.5
WHERE N = NUMBER OF BUBBLE PER UNIT
VOLUME FROM PHOTOS RAPHS
Φ = VOLUME FRACTION OCCUPIED BY
THE BUBBLE
RUN NUMBERS SHOWN ARE IDENTIFIED
EL SEWHERE
+20%
ELSEWHERE</td></tr><tr><td colspan="9">a, MEASURED INTERFACIAL AREA PER UNIT VOLUME (in-)
m, measured interfacial area per unit volume (in-)
m2</td></tr></table>

Figure 8. Comparison of Measured and Calculated Interfacial Areas Per Unit Volume. Horizontal Flow.

The second series of tests, subscripted "II," with only the bubble generator and separator regions entering into the mass transfer, determined the ratio

$$
\mathrm {K} _ {\text {I I}} = \mathrm {K} _ {1} \quad \mathrm {K} _ {3} \quad .
$$

Consequently the desired ratio, $\mathbf{K}_{2}$ , across the test section only, was determined from

$$
\mathrm {K} \equiv \mathrm {K} _ {\text {乙}} = \mathrm {K} _ {\mathrm {I}} / \mathrm {K} _ {\mathrm {I I}}.
$$

An estimate of the error involved in this procedure is given in Appendix G.

# Summary of Experimental Procedure

The mode of experimentation was transient with the independent variables being Schmidt number (depending on percent glycerine in glycerine-water mixtures), Reynolds number (liquid flow), bubble mean diameter (controlled by bubble generator probe position), and test section orientation (vertical or horizontal). Other parameters that were held constant for most of these tests include the test section conduit diameter $(D = 2$ inches), the ratio of gas to liquid volumetric flow $\left(Q_{g} / Q_{\ell} = 0.3\%\right)$ and the fluid temperature $(25^{\circ}C)$ .

It was found that the only effect of volume fraction up to $1\%$ was in the highly predictable change in surface area. No significant difference was detected in the mass-transfer coefficients themselves which are on a unit area basis. Consequently with the exception of some of the early runs most of the experiments were performed at a convenient volume fraction of $0.3\%$ . In addition it was found that for the distilled water runs (no glycerine) the rapid agglomeration of the

bubbles at the flows obtainable prevented meaningful interpretation of the data. Consequently all water tests were performed with the addition of about 200 ppm of normal butyl alcohol which effectively inhibited the agglomeration but may have resulted in a different surface condition compared to the other mixtures. The addition of this same amount of N-butyl alcohol to the glycerine-water mixtures made no significant difference.

For a given liquid mixture and orientation of the test section, the procedure followed to obtain a series of data is outlined in detail below:

1. The loop was first purged repeatedly with distilled water to remove residual liquid from previous experiments and the system allowed to dry by blowing air through it overnight.   
2. The mixture of glycerine and water to be used was precisely made up in the weigh tank and then thoroughly mixed by vigorous stirring produced by pumping the liquid from the bottom of the tank back into the top.   
3. The loop was filled using a small auxiliary pump and the system operating pressure was set at a nominal 40 psia by helium pressure over the interface in the bubble separator.   
4. Liquid flow was established by energizing the main loop circulator and the flow was set at the desired level by throttling through all three rotameters.   
5. The system was charged with oxygen to about seven or eight parts per million by passing oxygen bubbles through the bubble generator, the test section, and the bubble separator. The system was allowed to

run a sufficient time after the oxygen flow had been terminated to insure that the concentration readings were steady.

6. The bubble generator probe position was set to obtain the first desired mean bubble diameter for the given test conditions.   
7. The helium flow, having been preset to give $\frac{Q_g}{Q_\ell} = 0.3\%$ at the given liquid flow, was turned on initiating the transient experiment which was usually allowed to continue for 10 to 15 minutes.   
8. The oxygen concentration was continuously recorded and data sheet loggings were made of liquid flow through each rotameter, test section inlet pressure, test section pressure drop, helium pressure at the capillary tube exit, pressure drop across the capillary tube, loop temperature, bubble generator probe position, and atmospheric pressure.   
9. About midway through the transient for each test, a Polaroid picture of the bubbles was made through one of the photo ports (entrance or exit) and then the camera was pivoted and a picture taken through the other photo port.   
10. For the given liquid flow, the bubble generator probe position was varied to produce different mean diameters. Five values were desired and usually obtained. For each position the above procedure (5-9) was repeated. Occasionally to produce extra large bubbles, the gas was introduced through the test-section inlet pressure tap - bypassing the bubble generator itself.   
11. The liquid flow was varied over the desired range and the above procedure (5-10) was repeated for each flow setting.

Typical transient data of $\mathfrak{L}\mathfrak{n}\mathbb{C} / \mathbb{C}_{\circ}$ versus time taken directly from the oxygen concentration recording chart is shown on Figure 9 which illustrates the constancy of the slope $(-\mathfrak{L}\mathbb{K}_{\mathrm{I}}\mathbb{Q}_{\ell} / \mathbb{V}_{\mathrm{s}})$ .

The system volume had been previously measured to be $\sim 2.52\mathrm{ft}^3$ by filling the system completely with water which was then collected and weighed. Using this and the measured values of $Q_{\ell}$ , the constants $K_I$ were determined from the slopes of the curves.

After all vertical and horizontal tests were completed, "end effects" were measured by moving the bubble generator to the test section exit and repeating each experiment with the original conditions duplicated as nearly as possible.

The values of $\mathbf{K}_{\mathrm{II}}$ were then calculated from the slopes of the "end effect" curves and $\mathbf{K}$ 's were calculated from

$$
\mathrm {K} = \mathrm {K} _ {\mathrm {I}} / \mathrm {K} _ {\mathrm {I I}}.
$$

The products, ka, were extracted from K through Equations (5).

The bubble photographs were analyzed to obtain the interfacial areas per unit volume and the mean diameters. Typical examples of an inlet and exit photograph are shown on Figure 10. The outlined regions were used as the sample populations for counting the number of bubbles per unit volume, N.

The applicable volume fraction correlation [either Equations (13), (14), or (15)] was used to determine $\Phi$ and Equations (10) and (9) were used to calculate the interfacial areas per unit volume and the mean bubble diameters, respectively. Finally, the averages of the inlet and exit areas were used to extract $k$ from the ka products.

![](images/24a241452d5e6f117834716df897e4cb6a97121ce388fe14ec330114f863f744.jpg)  
Figure 9. Typical Experimental Concentration Transient Illustrating Straight-Line Behavior on Semi-Log Coordinants.

PHOTO 1854-71

![](images/04d88e8aea4a66301b4180045b4c2e6fd9bae3f85ae63bb636d86a9ce59603b0.jpg)

![](images/ce8130d7ae3177854650bf0f235535e822b3ce08d6b6a68ac124fdf907e3a455.jpg)  
Figure 10. Typical Examples of Bubble Photographs: a. Inlet b. Exit. Vertical Flow, $37.5\%$ Glycerine-62.5% Water, $Q_{\ell} = 20 \, \text{gpm}$ , $Q_{g} / Q_{\ell} = 0.3\%$ , $D = 2 \, \text{inches}$ , and $d_{VS} = 0.023 \, \text{inches}$ .

# CHAPTER IV

# EXPERIMENTAL RESULTS

The experimentally measured mass-transfer transients initially were converted into pseudo mass-transfer coefficients without any adjustment being made for mass-transfer occurring outside the test section. The results thus obtained are not the true mass-transfer coefficients because significant mass transfer occurred in the bubble generating and separating equipment. Nevertheless, considerable information can be gathered from this "unadjusted" data because of its presumed greater precision. The true mass-transfer coefficients with extraneous mass-transfer effects accounted for are presented later in this Chapter.

# Unadjusted Results

The "unadjusted" mass-transfer coefficients determined as outlined in Chapter III as functions of bubble mean diameter, Reynolds number, orientation of the test section, and Schmidt number are given in Appendix H (Figures 35-44, pages 138-147).

The "raw" data which consists of recorder charts of oxygen concentration versus time, innumerable photographs of bubble populations, and log book records of flows, probe settings, temperature, pressure and other conditions are on file in the Heat Transfer-Fluid Dynamics Department, Reactor Division of the Oak Ridge National Laboratory and are available upon request.

It is instructive to consider the crossplots (Figures 45-49, pages 148-152). Similar to Lamont's results, the horizontal and the vertical

flow values were identical above sufficiently high Reynolds numbers. As flows were decreased below these Reynolds numbers, however, the vertical flow coefficients were larger than the horizontal flow coefficients and seemed to asymptotically approach constant values. The horizontal flow data, on the other hand, continued along straight line variations (on log-log coordinates) until either the flow was too low to prevent concentration polarization at the oxygen sensors or in some cases severe stratification of the bubbles prevented further testing. The pertinent results to be considered, based on these unadjusted data, are the values of the Reynolds number at which vertical and horizontal flow results become identical and the apparent asymptotes approached by the vertical flow coefficients at low flows. Mass transfer occurring outside the test section should not affect either of these and their values should be the same as for the data presented later that represents the true mass-transfer coefficients.

# Equivalence of Horizontal and Vertical Flow Mass Transfer

It seems evident that gravitational forces (buoyancy) tend to establish a steady relative flow between the bubbles and the liquid if the bubbles are free to move in the vertical direction (as they would be in vertical orientations of the test sections) and are not restricted by physical boundaries (as they would be in horizontal orientations). The bubbles are also acted upon by inertial forces generated by the turbulent motions within the liquid. These turbulent inertial forces are randomly directed and thus tend, on the average, to counteract the gravitational forces. Therefore it would be reasonable to assume that if the magnitudes of the turbulent inertial forces, $F_{i}$ , were known

compared to the gravitational forces, $\mathbf{F}_{\mathrm{g}}$ , then their ratio, $\frac{\mathbf{F}_{\mathrm{i}}}{\mathbf{F}_{\mathrm{g}}}$ , would be a measure of the relative importance of these forces in establishing the mass-transfer coefficients. At sufficiently high values of $\frac{\mathbf{F}_{\mathrm{i}}}{\mathbf{F}_{\mathrm{g}}}$ one would expect the turbulent forces to dominate and there should then be no detectable difference in the horizontal and vertical flow results.

The gravitational force on a bubble of diameter, $d$ , is the weight of the displaced fluid

$$
F _ {g} = \frac {\rho \pi d ^ {3} g}{6 g _ {c}}. \tag {16}
$$

The turbulent inertial force exerted on a bubble essentially traveling at the local fluid velocity in a turbulent liquid is not so easily determined. Consequently, use was made of dimensional arguments.

In a turbulent fluid the mean variation in velocity, $\Delta V$ , over a distance, $\lambda$ , (greater than the microscale) is given dimensionally by

$$
\Delta V \sim \left(\frac {\varepsilon_ {v} \lambda g _ {c}}{\rho}\right) ^ {1 / 3},
$$

where $\mathsf{e}_{\mathsf{V}}$ is the power dissipation per unit volume. The 1/3 power on $\lambda$ agrees with the result of Hinze (Reference 37) for the variation in turbulent intensity required to result in the Kolmogoroff spectrum law. Similarly, the period, $\theta$ , for such velocity variations is given dimensionally by

$$
\theta \sim \left(\frac {\lambda^ {2} \rho}{g _ {c} \epsilon_ {v}}\right) ^ {1 / 3}.
$$

Following Levich, $^{36}$ it is postulated that the mean acceleration $a_{\lambda}$ undergone by a fluid element of size, $\lambda$ , is

$$
a _ {\lambda} \cong \frac {d \Delta V}{d t} \sim \left(\frac {\varepsilon_ {v} g _ {c}}{\rho}\right) ^ {2 / 3} / \lambda^ {1 / 3}.
$$

A spherical fluid element with this mean acceleration must have experienced a "mean" force given by

$$
F _ {\lambda} = \frac {M a _ {\lambda}}{g _ {c}} \sim \frac {\rho \pi \lambda^ {3}}{6 g _ {c}} \left(\frac {\epsilon_ {v} g _ {c}}{\rho}\right) ^ {2 / 3} / \lambda^ {1 / 3}.
$$

It is further postulated that a bubble of diameter, $d$ , in the turbulent liquid will be subjected to the same mean forces as those exerted on a fluid element of the same size. Therefore the mean turbulent inertial force on the bubble is given by

$$
F _ {i} \sim \frac {\rho \pi d ^ {3}}{6 g _ {c}} \left(\frac {e _ {v} g _ {c}}{\rho}\right) ^ {2 / 3} / d ^ {1 / 3}. \tag {17}
$$

Dividing by Equation (16) the ratio of inertial forces to gravitational forces is given by

$$
F _ {i} / F _ {g} \sim \left(\frac {\epsilon_ {v} g _ {c}}{\rho}\right) ^ {2 / 3} / d ^ {1 / 3} g. \tag {18}
$$

For flow in conduits, the power dissipation per unit volume can be expressed as

$$
\varepsilon_ {v} \equiv V \frac {d P}{d x} = (R e \mu / D _ {P}) \frac {d P}{d x}
$$

and the pressure gradient can be determined from the Blasius relationship,

$$
\frac {d P}{d x} = \frac {f}{D} \frac {\rho V ^ {2}}{2 g _ {c}} = \left(f \mu^ {2} / 2 g _ {c} D ^ {3} \rho\right) R e ^ {2}.
$$

Using the friction factor for smooth tubes,

$$
f = 0. 3 1 6 / (\mathrm {R e}) ^ {1 / 4},
$$

the power dissipation per unit volume is

$$
\varepsilon_ {V} = \left(\frac {0 . 3 1 6}{2 g _ {c}}\right) \frac {\mu^ {3}}{\rho^ {2} D ^ {4}} R e ^ {1 1 / 4}. \tag {19}
$$

Substitution into Equation (18) and replacing the bubble diameter by the Sauter mean gives

$$
F _ {i} / F _ {g} \sim \left[ \frac {0 . 3 1 6 \mu^ {3} R e ^ {1 1 / 4}}{2 \rho^ {3} D ^ {4}} \right] ^ {2 / 3} / d _ {\mathrm {v s}} ^ {1 / 3} g. \tag {20}
$$

Since Equation (20) was established on dimensional grounds, there exists a proportionality constant of unknown magnitude. To establish the value that the ratio should have to serve as a criterion for determining when horizontal and vertical flow mass-transfer coefficients become identical, use was made of the data of Lamont gathered from his report as listed in Table VI below.

Table VI. Conditions at Which Horizontal and Vertical Flow Mass Transfer Coefficients Become Equal (Lamont's Data) $^{11}$   

<table><tr><td></td><td>Case I</td><td>Case II</td></tr><tr><td>Conduit Diameter, D (inches)</td><td>5/16</td><td>5/8</td></tr><tr><td>Reynolds Modulus, Re</td><td>\( 10^4 \)</td><td>\( 3 \times 10^4 \)</td></tr><tr><td>Liquid Viscosity, μ (centipoise)</td><td>0.89</td><td>0.89</td></tr><tr><td>Liquid Density, o (g/cm3)</td><td>1.0</td><td>1.0</td></tr><tr><td>Bubble Diameter, d (inches)</td><td>~5/32</td><td>~5/32</td></tr></table>

Substitution of the data of Case I into Equation (20) gives

$$
F _ {i} / F _ {g} \cong 1. 5
$$

As a check the data of Case II are compared,

$$
\frac {\left(\mathrm {F} _ {\mathrm {i}} / \mathrm {F} _ {\mathrm {g}}\right) _ {\mathrm {I}}}{\left(\mathrm {F} _ {\mathrm {i}} / \mathrm {F} _ {\mathrm {g}}\right) _ {\mathrm {I I}}} = \left(\frac {1 0 ^ {4}}{3 \times 1 0 ^ {4}}\right) ^ {1 1 / 6} / \left(\frac {5 / 1 6}{5 / 8}\right) ^ {8 / 3} = \frac {0 . 8 2}{0 . 8 3} \sim 1.
$$

For the present investigation, the loci of points for $\mathbf{F}_i / \mathbf{F}_g = 1.5$ as calculated from Equation (20) are shown on Figures 45-49, pages 148-152.

It is seen that the ratio $\frac{F_i}{F_g}$ seems to be a good predictor for the equivalence of the horizontal and vertical results.

# Vertical Orientation Low-Flow Asymptotes

As liquid flow is reduced, the gravitational forces become more and more dominant over the turbulent inertial forces. Consequently, at low flows, the vertical flow mass-transfer coefficients approach the values that would be expected for the bubbles rising through a quiescent liquid.

The conditions of mass transfer for bubbles rising through a column of liquid have been extensively studied (e.g., References 26-30). Resnick and Gal-Or<sup>57</sup> have recommended for surfactant-free systems

$$
k _ {a} = 0. 1 0 9 \left[ \frac {\vartheta_ {p g}}{\mu} \right] ^ {1 / 2} \frac {1 - \Phi}{\left(1 - \Phi^ {5 / 3}\right) ^ {1 / 2}} \sqrt {d _ {v s}}
$$

They caution that this equation may give values slightly higher than the observed data in particular for lower concentrations of glycerol in water-glycerol systems.

In the present investigation, the volume fraction is low so that the above equation was approximated as

$$
k _ {a} \cong 0. 1 0 9 [ \delta \rho g / \mu ] ^ {1 / 2} \sqrt {d _ {v s}} \tag {21}
$$

and used to determine the "calculated asymptotes" for the vertical flow results as indicated on the various data plots.

# Mass-Transfer Coefficients

With the end-effect accounted for as outlined in Chapter III, the mass-transfer coefficients measured in this investigation are given in Figures 50-58, pages 153-161 (Appendix G). The more revealing crossplots

of mass-transfer coefficients versus Reynolds number are shown in Figures 11-15 which contain regression lines fitted to the horizontal flow data and calculated lines for the vertical flow cases. Vertical flow data are not shown for the $37.5\%$ mixture because the end effect adjustments were not satisfactory. Excessive vibration of the bubble generation probe that occurred during the $37.5\%$ experiments was eliminated by redesign of the probe before the horizontal data were obtained. Time did not permit a reorientation of the system to the vertical position to repeat the runs.

From these figures it is seen that the horizontal flow data for water (plus N-butyl alcohol) apparently have a lesser slope than that for the glycerine-water mixtures. Therefore a regression equation was determined for the water runs alone and a separate regression equation was determined for the combined data for the 12.5, 25, and $37.5\%$ glycerine mixtures. A third behavior was observed for the $50\%$ glycerine mixture (Figure 15). It is seen that all the data for this mixture were obtained at Reynolds numbers less than that required for $\mathrm{F_i / F_g} = 1.5$ . However, instead of a steady march of the horizontal flow data down a straight line as observed for the other mixtures, the small bubble horizontal flow mass-transfer coefficients tended to behave like those for vertical flows. This behavior implies that, if the liquid is viscous enough, small bubbles apparently can establish steady relative flow conditions in their rise across the conduit cross section. In these runs, the pipe wall apparently did not significantly inhibit the bubble rise rate during transit through the test section and, evidently, the bubbles behaved exactly as if they were rising through a vertical conduit.

![](images/99bb6fc72ecce6969c13fe954c4c4adf74fe97bd07c24a7d1c104821e24eba99.jpg)  
Figure 11. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. Water Plus $\sim 200$ ppm N-Butyl Alcohol. Horizontal and Vertical Flow in a 2-inch Diameter Conduit.

![](images/dd21a0f9b61277358a57d7df3f33f8cd275a599d67a484c1d1dc6c83a184fad0.jpg)  
Figure 12. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $12.5\%$ Glycerine- $87.5\%$ Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit.

![](images/9a1e56c6a54c073e8892738456882ab9be860e2247fa6a5a779fcffa1e9cb368.jpg)  
Figure 13. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $25\%$ Glycerine- $75\%$ Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit.

![](images/434d13371fabaab7817a72804347b052ce55400499a72a516ad640467b8a7ee5.jpg)  
Figure 14. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $37.5\%$ Glycerine- $62.5\%$ Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit.

![](images/f8bd781e0b96516f3bebcc5ad34d766aab0ddcf03ed50df409255e6fda507f25.jpg)  
Figure 15. Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $50\%$ Glycerine- $50\%$ Water. Horizontal and Vertical Flow in a 2-inch Diameter Conduit.

These three kinds of observed horizontal flow behavior are further illustrated on Figure 16 for 0.02-in. mean diameter bubbles. The regression slope of 0.94 for the glycerine-water mixtures agrees generally with the literature as discussed in Chapter II and the slope of 0.52 for the water plus N-butyl alcohol is, coincidentally, exactly what Lamont found. However, the combined regression slope (0.79) for all the water data which includes the other bubble mean diameters was greater than the value for the 0.02-in. bubbles by themselves.

# Calculating Vertical Flow Mass-Transfer Coefficients

for $\mathbf{F_i} / \mathbf{F_g}$ Less Than 1.5

Since the ratio of turbulent inertial forces to gravitational forces is seen to be a good predictor of the Reynolds number at which horizontal and vertical flow mass-transfer coefficients become identical, it is proposed that the varying ratio might also serve as a scaling factor at all Reynolds numbers to determine the relative importance of the purely turbulent coefficients $(\mathbf{F}_{\mathbf{i}} / \mathbf{F}_{\mathbf{g}} > 1.5)$ and the relative flow coefficients (vertical flow asymptotes). That is, if the values are known for the straight line variation at higher Reynolds numbers where vertical and horizontal coefficients are equal along with the vertical flow asymptotes, it is proposed that the intermediate vertical flow mass-transfer coefficients can be calculated by using $\mathbf{F}_{\mathbf{i}} / \mathbf{F}_{\mathbf{g}}$ as a linear scaling factor between the two. Since $\mathbf{F}_{\mathbf{i}} / \mathbf{F}_{\mathbf{g}} = 1.5$ appears to mark the Reynolds numbers at which turbulent inertial forces dominate over gravitational forces, the actual ratio of forces at that condition are assumed to be of the order of 10 to 1 for gravitational forces to begin

![](images/7c367a6408461539e745d4623b3e2c4176ec8b88f639e090e1b1bc3f7af78ce2.jpg)  
Figure 16. Observed Types of Horizontal Flow Behavior. $d_{\mathrm{VS}} = 0.02$ inches and $D = 2$ inches.

to be negligible. Consequently $10(\mathsf{F_i} / \mathsf{F_g}) / 1.5$ was chosen as an appropriate linear scaling factor and the vertical flow mass-transfer coefficients were calculated from

$$
k _ {v} = k _ {a} \left[ \frac {1}{1 + 1 0 \left(F _ {i} / F _ {g}\right) / 1 . 5} \right] + k _ {h} \left[ \frac {1 0 \left(F _ {i} / F _ {g}\right) / 1 . 5}{1 + 1 0 \left(F _ {i} / F _ {g}\right) / 1 . 5} \right], \tag {22}
$$

in which $\mathbf{k}_{\mathrm{a}}$ is the calculated asymptote given by Equation (21) and $\mathbf{k}_{\mathrm{h}}$ is the value at the given Reynolds number that would be obtained by extending the straight-line variation of the horizontal flow data.

Using separate regression lines for $k_h$ , the vertical flow mass-transfer coefficients calculated from Equation (22) are compared with the data on Figures 11-15, pages 62-66. Except for the $50\%$ mixture data, Equation (22) provides a relatively good description of the data.

# Comparison with Agitated Vessels

A comparison of the horizontal flow data with that of Sherwood and $\text{Brian}^{17}$ for particulates in agitated vessels is shown on Figure 17. Sherwood and Brian's coordinates are used by converting $\mathbf{e}_{\mathrm{m}} \left( \equiv \frac{\mathbf{e}_{\mathrm{v}}}{\rho} \right)$ through Equation (19) for flow in conduits. It is seen that, although the relative magnitudes of the coefficients are comparable on an equivalent power dissipation basis, there is a Schmidt number separation of this data indicating mobile interfacial behavior. In agreement with the findings of other investigations reported in Chapter II, the variation with Reynolds number for flow in conduits is much steeper than would have been expected from the agitated vessel data.

A possible explanation for this difference in slope observed between agitated vessels and flow in conduits may lie in the relative importance of the gravitational forces. For example, the data of this research for

![](images/18800a1a291bfe76d7c8c05036e9368b63cafb3ad5a11396671fbd9d8bb26e71.jpg)  
Figure 17. Equivalent Power Dissipation Comparison of Results with Agitated Vessel Data.

small bubbles in a $50 \%$ mixture of glycerine and water were obviously strongly gravitationally dominated as evidenced by the equality of the horizontal and vertical flow coefficients even at very low Reynolds numbers. A comparison of these "gravity- influenced" data with Sherwood and Brian's correlation shown on Figure 18 indicates a remarkable similarity. It may be that gravitational forces are generally less important for flow in conduits than for flow in agitated vessels where there may be a greater degree of anisotropy.

# Recommended Correlations

A regression line through all the horizontal flow data except the water and the $50\%$ mixtures has a Schmidt number exponent of 0.71 using the literature<sup>56</sup> values of $\&$ . These values of $\&$ (Figure 25, page 114, Appendix A) first increase with addition of glycerol, reach a maximum at about $12.5\%$ glycerol, and then decrease. This behavior represents a striking departure from the Stokes-Einstein behavior usually observed for aqueous mixtures. If, instead of using these values for $\&$ , a smooth monotonically decreasing line is drawn through the first, fourth, and fifth data points of Figure 25 and the values of $\&$ taken from that line, a regression analysis yields a Schmidt number exponent of 0.58 - not much different than the value of 0.5 expected for mobile interfaces.

A regression analysis of all the horizontal data for the glycerine-water mixtures (except for the $50\%$ mixture) using the original values of $\mathcal{S}$ (Table III, page 20) and forcing the Schmidt number to have an exponent of $1/2$ results in the equation,

$$
\mathrm {S h} = 0. 3 ^ {4} \mathrm {R e} ^ {0 \cdot 9 4} \mathrm {S c} ^ {1 / 2} \left(\mathrm {d} _ {\mathrm {v s}} / \mathrm {D}\right) ^ {1 \cdot 0}, \tag {23}
$$

![](images/bcd58da17daf17799a5264dad1db48d46e91553b9e30f436831e62b7e2bdbbcb.jpg)  
Figure 18. Equivalent Power Dissipation Comparison of Gravity Dominated Results with Agitated Vessel Data.

with a standard deviation in $\ell_{\pi}(\mathrm{Sh} / \mathrm{Sc}^{1/2})$ of 0.19 and an index of determination of 0.86. The comparison of the data with this equation is shown in Figure 19.

Since a Schmidt number exponent of $1/2$ is expected on theoretical grounds and since there is little loss of precision by using this exponent, it is recommended for design purposes that the horizontal flow mass-transfer coefficients, $k_h$ , be calculated from Equation (23) as long as $V / V_b$ is greater than about 3. Operation below $V / V_b = 3$ is not recommended because of severe stratification. Equation (23) can also be used to calculate the vertical flow coefficients, $k_v$ , as long as $F_i / F_g$ , as determined by Equation (20), is greater than 1.5. Otherwise, Equation (22) is recommended for the vertical flow coefficients with the asymptotic values, $k_a$ , to be calculated from Equation (21).

As evidenced by the observed high Schmidt number exponent, these recommendations are for contamination free systems only. For a contaminated system with rigid interfacial conditions, the Schmidt number exponent is expected to be $1/3$ and the coefficient multiplying the equation should also be different. In the absence of supporting experimental data, a tentative correlation for rigid interfacial conditions might be inferred from Equation (23) to be

$$
\mathrm {S h} = 0. 2 5 \mathrm {R e} ^ {0 \cdot 9 4} \mathrm {S c} ^ {1 / 3} \left(\mathrm {d} _ {\mathrm {v s}} / \mathrm {D}\right) ^ {1 \cdot 0}.
$$

The coefficient, 0.25, was obtained by multiplying 0.34 [the coefficient of Equation (23)] by the ratio of rigid-to-mobile coefficients of equations applicable to bubbles moving steadily through a liquid.[31] A similar transformation of Equation (21) would be required to obtain the rigid-interface values of the vertical flow asymptotes. The above

![](images/2dd476d63184c6452b7aa746b35f90a80f6eba750937de8bf8acb3aec12a78f6.jpg)  
Figure 19. Correlation of Horizontal Flow Data.

equation for rigid interfaces should be used with caution as it has not been validated by experimental data. In addition the experimentally observed linear variation with $(d_{\mathrm{vs}} / D)$ may have been caused by a transition from rigid-to-mobile interfacial condition. For strictly rigid interfaces no such transition would be expected to occur and the exponent on $(d_{\mathrm{vs}} / D)$ might then be less than 1.0.

# CHAPTER V

# THEORETICAL CONSIDERATIONS

Two different viewpoints were considered to describe mass transfer between small bubbles and liquids in cocurrent turbulent flow. In the first, a turbulence interaction approach, the bubbles were considered to be subjected to turbulence forces which impart random motions resulting in "mean" relative velocities between the bubbles and the fluid. These "mean" velocities were then considered as "steady" (albeit multi-directional) and as dictating the mass-transfer behavior.

In the second, a surface renewal approach, the bubbles were viewed as being associated with a spherical shell of liquid for an indefinite time during which mass exchange takes place by turbulent diffusion. This indefinite time was assumed to be related to the bubble size and the average relative velocity between the bubble and the liquid.

# Turbulence Interaction Model

A small bubble suspended in a turbulent field will be subjected to random inertial forces created by the turbulent fluctuations. Under the action of a given force, if sufficiently persistent, the bubble may achieve its terminal velocity and move at a steady pace through the liquid before being redirected by another force encounter within the random field. If the "average" value representing the bubble relative velocity in such a turbulent field could be determined, then a convenient formulation would be to use that velocity to determine an average bubble

Reynolds number and stay within the confines of the well-established relative-flow Frössling-type equations to determine the mass-transfer coefficients.

The movement of the bubbles through the liquid will be resisted primarily by viscous stresses. The drag force on a sphere moving steadily through a liquid is often expressed in terms of a drag coefficient, $C_d$ , by the equation,

$$
F _ {d} = \frac {C _ {d} A \rho v ^ {2} b}{2 g _ {c}} = \frac {C _ {d} \pi \mu^ {2} R e ^ {2} b}{8 g _ {c} \rho},
$$

in which the drag coefficient is itself a function of the bubble Reynolds number, $\mathsf{Re}_{\mathsf{b}}\left(\equiv v_{\mathsf{b}}\mathrm{d}\rho /\mu\right)$ . In relative flows, however, the drag coefficient-Reynolds number correlation depends on the particular Reynolds number range. Frequently, two regimes of flow are identified with the division occurring at $\mathsf{Re}_{\mathsf{b}}\cong 2$ . Common correlations for the drag coefficients in these two regimes are given below.

For $\mathbf{Re}_{\mathrm{b}} \leq 2$

$$
C _ {d} = 2 4 / R e _ {b} \text {a n d} F _ {d} = 3 \pi \mu^ {2} R e _ {b} / g _ {c} o. \tag {24-a}
$$

For $2 < \mathrm{Re}_{\mathrm{b}} \leq 200$

$$
C _ {d} = 1 8. 5 / R e _ {b} ^ {0 \cdot 6} a n d F _ {d} = 1 8. 5 \pi \mu^ {2} R e _ {b} ^ {1 \cdot 4} / 8 g _ {c} \rho . \tag {24-b}
$$

In Chapter IV, an expression was developed for the inertial forces experienced by a bubble in a turbulent fluid,

$$
F _ {i} \sim \frac {\mu^ {2}}{\rho g _ {c}} (d / D) ^ {8 / 3} (R e) ^ {1 1 / 6}. \tag {25}
$$

It might be reasonable to determine "mean" bubble velocities from a balance between the inertial forces and the drag forces for later substitution into the Frössling equations. If it is postulated that the

above two relative flow regimes also exist for bubbles in a turbulent field, then two different sets of equations describing the mass transfer will result. Since the inertial forces depend on the bubble size, a dispersion of bubbles with a distribution of sizes may have bubbles in either or both regimes simultaneously and the mass-transfer behavior may be described by either set of equations or take on characteristics of a combination of the two. The mass-transfer equations resulting for the two separate regimes are discussed below.

# Regime-1: $\mathbf{Re}_{\mathfrak{b}}\leq 2$

If the bubble motion were predominantly governed by the regime, $\mathsf{Re}_{\mathsf{b}} \leq 2$ , the drag forces would be given by Equation (24-a). A balance between the inertial and drag forces, $\mathbf{F}_{\dot{\mathbf{i}}} = \mathbf{F}_{\dot{\mathbf{d}}}$ , would then give for the bubble Reynolds number

$$
\mathrm {R e} _ {\mathrm {b}} \sim (\mathrm {d} / \mathrm {D}) ^ {8 / 3} \mathrm {R e} ^ {1 1 / 6}. \tag {26}
$$

By this formulation, the bubble relative flow Reynolds number depends only on the ratio, $\frac{d}{D}$ , and on the pipe Reynolds number which, for a given bubble size, establish the turbulence level. The Sherwood number for mass transfer can therefore be determined as a function of these variables by substitution of Equation (26) into mass-transfer equations that have been established as applicable to a sphere moving through a liquid. These are the Frössling-type equations which, for large Schmidt numbers, usually take the forms

$$
\mathrm {S h} _ {\mathrm {b}} \sim \mathrm {R e} _ {\mathrm {b}} ^ {1 / 2} \mathrm {S c} ^ {1 / 2}
$$

and

$$
\mathrm {S h} _ {\mathrm {b}} \sim \mathrm {R e} _ {\mathrm {b}} ^ {1 / 2} \mathrm {S c} ^ {1 / 3}
$$

for mobile and rigid interfaces, respectively. Making the conversion, $\mathrm{Sh} \equiv (\mathrm{D} / \mathrm{d}) \mathrm{Sh}_{\mathrm{b}}$ , and substituting Equation (26) gives for the mobile and rigid interface pipe Sherwood numbers applicable to cocurrent turbulent flow,

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 2} \operatorname {R e} ^ {\circ \cdot 3 2} (\mathrm {d} / \mathrm {D}) ^ {1 / 3} \tag {27}
$$

and

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 3} \operatorname {R e} ^ {0. 9 2} (d / D) ^ {1 / 3}, \tag {28}
$$

respectively.

Consequently, in this regime, the pipe Reynolds number exponent is 0.92. For comparison, the experimentally determined value for the water-glycerine mixtures in this investigation was 0.94. The theoretical bubble diameter dependence, $(\mathrm{d} / \mathrm{D})^{1/3}$ , however is less than the experimentally determined linear variation. Calderbank and Moo-Young<sup>16</sup> point out that the linear variation they observed for bubbles in this size range probably resulted from a transition from rigid to mobile interfacial conditions because small bubbles tend to universally behave as rigid spheres while larger bubbles require the presence of sufficient surface active ingredients to immobilize their surface.

If such a transition is the reason for the linear variation in this instance also, then the effect of conduit diameter will be different from that implied in Equation (23) which did not include actual variations in conduit diameter. Consequently, anticipated future experiments with variations in the conduit diameter should help clarify the influence of bubble mean diameter. In addition, exploratory experiments in this study indicated that the linear variation did not continue up to larger bubble sizes and may, therefore, be limited to the relatively narrow mean

diameter range of approximately 0.01 to 0.05 inches. At larger diameters, the dependence tended to lessen until above mean diameters of about 0.08 inches where the Sherwood number appeared to decrease with increasing bubble diameter. Since the bubble generator was not generally capable of producing larger bubbles, further investigation of the bubble size influence was not possible in this experiment.

# Regime-2: $\mathsf{Re}_{\mathsf{b}} > 2$

If the bubble motions were predominantly in the regime, $\mathbf{Re}_{\mathrm{b}} > 2$ , the drag forces would be given by Equation (24-b). The balance, $\mathbf{F}_{\mathrm{i}} = \mathbf{F}_{\mathrm{d}}$ , would then give

$$
\mathrm {R e} _ {\mathrm {b}} \sim (\mathrm {d} / \mathrm {D}) ^ {8 / 4 \cdot 2} \mathrm {R e} ^ {1 1 / 8 \cdot 4}. \tag {29}
$$

The relative-flow bubble Reynolds number in this regime still depends on the variables that establish the turbulence level but that dependence is different from that of Regime 1. When substituted into the Frössling equations for mobile and rigid interfaces, the results are

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 2} \mathrm {R e} ^ {0 \cdot 6 6} (\mathrm {d} / \mathrm {D}) ^ {- 0 \cdot 2 / 4 \cdot 2}
$$

and

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 3} \operatorname {R e} ^ {0 \cdot 6 6} (\mathrm {d} / \mathrm {D}) ^ {- 0 \cdot 2 / 4 \cdot 2}, \tag {30}
$$

respectively.

For this regime the Reynolds number exponent is 0.66. Consequently, if bubbles in cocurrent turbulent flow experience different flow regimes similar to bubbles in relative flow, a transition would be expected at higher pipe Reynolds numbers in which the Reynolds number exponent would tend to become smaller. In the present experiments, the data for water (plus $\sim$ 200 ppm N-butyl alcohol) with no glycerine added was obtained at

the highest range of Reynolds numbers covered. The experimentally measured Reynolds number exponent for the water runs was lower than for the glycerine-water mixtures and compared favorably with the above results. In addition, Equation (30) compares quite well with data for particles in agitated vessels [for example see Equation (3)].

It is felt that the possible existence of different flow regimes even in cocurrent turbulent flows is an important concept that, if further developed, could help explain some of the apparent discrepancies in the literature data. For example, this may explain the different slopes observed in this study and may be the reason for observed differences between mass transfer in agitated vessels and in conduits. It is more likely, however, that the latter difference is due to greater gravitational influence in agitated vessels.

# Surface Renewal Model

In this analysis each bubble is considered to be surrounded by, and exchanging mass with, a spherical shell of turbulent liquid in which the turbulence is isotropic.

A mass balance (Appendix F) in a spherical differential element of fluid results in the equation

$$
\frac {\partial C}{\partial t} = \mathfrak {A} \left[ \frac {\partial^ {2} C}{\partial r ^ {2}} + \frac {2}{r} \frac {\partial C}{\partial r} \right] + \frac {1}{r ^ {2}} \frac {\partial}{\partial r} (r ^ {2} U _ {r} C). \tag {31}
$$

Making Reynolds assumptions,

$$
\mathrm {C} \equiv \overline {{\mathrm {C}}} + \mathrm {C} ^ {\prime}
$$

$$
U _ {r} \equiv u ^ {\prime},
$$

and time averaging gives

$$
\frac {\partial \overline {{C}}}{\partial t} = \vartheta \left[ \frac {\partial^ {2} \overline {{C}}}{\partial r ^ {2}} + \frac {2}{r} \frac {\partial \overline {{C}}}{\partial r} \right] + \frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} \overline {{\mu^ {\prime} C ^ {\prime}}}\right). \tag {32}
$$

In turbulent scalar transfer, the "Reynolds" term $\overline{\mu^{\prime}C^{\prime}}$ , is often assumed to be expressible with an eddy diffusivity, $E$ , defined by

$$
\left. \overline {{u ^ {\prime} C ^ {\prime}}} \right| _ {y} \equiv E \frac {d \overline {{C}}}{d y}.
$$

However, it is more convenient here to use a recent eddy viscosity definition by Phillips, $^{58}$ for which an analogous definition for an eddy diffusivity in spherical coordinates would be

$$
\frac {\mathrm {d}}{\mathrm {d} r} \left(r ^ {2} \overline {{u ^ {\prime} C ^ {\prime}}}\right) \equiv \mu_ {\mathrm {e}} \frac {\mathrm {d}}{\mathrm {d} r} \left(r ^ {2} \frac {\mathrm {d} \overline {{C}}}{\mathrm {d} r}\right). \tag {33}
$$

Using this definition, Equation (32) is expressed more simply as

$$
\frac {\partial \overline {{c}}}{\partial t} = (\vartheta + \mu_ {e}) \left[ \frac {\partial^ {2} \overline {{c}}}{\partial r ^ {2}} + \frac {2}{r} \frac {\partial \overline {{c}}}{\partial r} \right] \quad . \tag {34}
$$

The view is now to be taken that, on the average, a bubble remains associated with a spherical shell of liquid for some indefinite time after which its surface is completely "renewed" - that is, associated with an entirely different spherical shell of liquid that has an initial uniform concentration characteristic of the bulk fluid. It is felt that the times of association between the bubble and a given region of liquid should be related to the magnitude of the turbulent inertial forces or alternatively to the mean relative velocity between the bubble and the liquid as established by the balance of the inertial and the viscous resisting forces.

Therefore a nondimensional time for comparison purposes is proposed to be

$$
t _ {*} \equiv \frac {t v _ {b}}{d}.
$$

Using this definition along with the following additional definitions of dimensionless quantities

$$
\begin{array}{l} \mathrm {C} _ {*} \equiv \overline {{\mathrm {C}}} / \mathrm {C} _ {\mathrm {O}} \\ \mathbf {r} _ {*} \equiv \mathbf {r} / d \\ \mathrm {R e} _ {\mathfrak {p}} \equiv v _ {\mathfrak {p}} d \rho / \mu \\ \mathrm {R e} \equiv \mathrm {V D} _ {\rho} / \mu \\ \mathrm {S c} \equiv \mu / \rho \mathcal {D}, \\ \end{array}
$$

Equation (34) can be expressed in nondimensional form as

$$
\frac {\partial \mathrm {C} _ {*}}{\partial \mathrm {t} _ {*}} = \frac {(1 + \mu_ {\mathrm {e}} / 2)}{\operatorname {R e} _ {\mathrm {b}} \operatorname {S c}} \left[ \frac {\partial^ {2} \mathrm {C} _ {*}}{\partial \mathrm {r} _ {*} ^ {2}} + \frac {2}{\mathrm {r} _ {*}} \frac {\partial \mathrm {C} _ {*}}{\partial \mathrm {r} _ {*}} \right]
$$

Assuming the bubble motion is predominantly in Stokes' regime, Equation (26) can be used to estimate $\mathsf{Re}_{\mathsf{b}}$ and substituted into the above equation to give

$$
\frac {\partial C _ {*}}{\partial t _ {*}} = \frac {(1 + \mu_ {e} / \vartheta)}{C _ {1} \operatorname {S c} (d / D) ^ {8 / 3} \operatorname {R e} ^ {1 1 / 6}} \left[ \frac {\partial^ {2} C _ {*}}{\partial r _ {*} ^ {2}} + \frac {2}{r _ {*}} \frac {\partial C _ {*}}{\partial r _ {*}} \right] \quad , \tag {35}
$$

where $C_1$ is a proportionality constant of unknown magnitude but assumed to be of the order $\sim 10^{-2}$ . A similar equation can be developed for Regime-2 of the previous model by using Equation (29) for $Re_b$ . Logical boundary conditions for Equation (35) would be

1. $C_{*}(0, r_{*}) = 1,$   
2. $C_{*}(t > 0,1 / 2) = 0,$ and   
3. $\frac{\partial C_{*}}{\partial r_{*}} = 0$ at $r_{*e} \equiv 1/2\Phi^{1/3}$

The third boundary condition above arises from equating the volume fraction with the ratio of bubble volume to equivalent sphere volume.

A solution of Equation (35) would give $C_*$ as a function of $r_*$ and $t_*$ . If a radial average, $\overline{C}_*$ , is defined as

$$
\overline {{c}} _ {*} \left(t _ {*}\right) \equiv \frac {\int_ {1 / 2} ^ {r _ {* e}} c _ {*} \left(r _ {*} , t _ {*}\right) r _ {*} ^ {2} d r _ {*}}{\int_ {1 / 2} ^ {r _ {* e}} r _ {*} ^ {2} d r _ {*}},
$$

then the Sherwood number as a function of time can be expressed as

$$
\operatorname {S h} \left(t _ {*}\right) \equiv \frac {\frac {\partial c _ {*}}{\partial r _ {*}} \mid r _ {*} = 1 / 2}{\left(\frac {d}{D}\right) \overline {{c}} _ {*}}.
$$

If a bubble is assumed to remain associated with a fluid element for some unspecified time, $T_*$ , then the average Sherwood number for that period is

$$
\overline {{\mathrm {S h}}} \equiv \frac {\int_ {0} ^ {\mathrm {T} _ {*}} \mathrm {S h} \left(\mathrm {t} _ {*}\right) \mathrm {d t} _ {*}}{\mathrm {T} _ {*}}. \tag {36}
$$

The above analysis is similar to normal surface renewal models in that the dimensionless time period $\mathbf{T}_{*}$ is analogous to a surface age. There is no real basis for being able to relate $\mathbf{T}_{*}$ to the flow hydrodynamics or the surface conditions; however, it could be treated as a parameter and the mass-transfer coefficients determined as a function of this parameter. "Surface age" distributions could then be established from the experimental data or specified arbitrarily just as they have been in other surface renewal models. For example, one common assumption has been that the surface is "renewed" each time the bubble travels (relative to the fluid) a distance equal to its diameter. With the formulation used here, this assumption would be particularly convenient because then $\mathbf{T}_{*} = 1$ .

Equation (35) along with its boundary conditions is considered as a surface renewal model. For a solution, a function,

$$
\mu_ {e} / \mathcal {D} (R e, S c, d / D, r _ {*}),
$$

must first be established to describe the variation in eddy diffusivity.

In arriving at his eddy viscosity definition, Phillips $^{58}$ used a Fourier decomposition of the turbulent field and, by an elegant analysis, determined the contributions to the local eddy viscosity due to each component "wave" making up the field.

Through a parallel analysis for mass transfer, it is inferred here that the individual component contributions to the eddy diffusivity are proportional to the energy of the transverse velocity fluctuations and inversely proportional to their wave number,

$$
\mu_ {e, n} \sim \overline {{u}} _ {n} ^ {2} / n. \tag {37}
$$

Defining $f(n) \mathrm{dn}$ as the fraction of eddies that have wave numbers in the range $n \pm 1/2 \mathrm{dn}$ , and summing the contributions over all wave numbers gives

$$
\mu_ {e} \sim \int_ {n} \frac {\bar {u} _ {n} ^ {2}}{n} f (n) d n. \tag {38}
$$

If Kolmogoroff's energy spectrum is used, the distribution function defined above can be assumed to be inversely proportional to the wavenumber,

$$
f (n) \sim 1 / n,
$$

and Equation (38) becomes

$$
\mu_ {e} \sim \int_ {n} \left(\bar {u} _ {n} ^ {2} / n ^ {2}\right) d n. \tag {39}
$$

To assess the effect of the interface, use was made of Lamont's analysis in which he idealized each component as a sinusoidal viscous

"eddy cell" in which the velocities are damped by viscous stresses as an interface is approached. His analysis gave for a spacial average (parallel to the interface),

$$
\bar {u} _ {n} \sim \xi (y) n ^ {- 1 / 3},
$$

where $y$ is a coordinate defined as $y \equiv r - d/2$ and $\xi(y)$ is a damping factor depending on the interfacial condition. Lamont's solution of the viscous "eddy-cell" equation gave for a rigid interface,

$$
\xi_ {r} = [ 0. 2 9 4 \mathrm {n y} \sinh \mathrm {n y} + 0. 3 8 8 \sinh \mathrm {n y} - 0. 3 8 8 \mathrm {n y} \cosh \mathrm {n y} ],
$$

and for a mobile interface,

$$
\bar {\xi} _ {m} = [ 0. 3 6 6 \sinh n y - 0. 0 8 9 n y \cosh n y ] \quad .
$$

In addition, it is assumed here that only the range of eddy sizes smaller than, or equal to, the bubble diameter interact with a bubble to produce eddy transfer to the bubble itself and that each of these eddies is effectively damped only if it is within a distance from the interface equal to the wave size. The eddy sizes assumed present range from a minimum given by the Kolmogoroff microscale for pipe flow,

$$
\lambda_ {\min } \equiv D / R e ^ {1 1 / 1 6},
$$

to an arbitrary maximum of one-half the pipe diameter,

$$
\lambda_ {\max } \equiv D / 2.
$$

Consequently, using Equation (39), the ratio of eddy diffusivity effective to the bubble at a position $y$ to the eddy diffusivity existing away from the interface, $\mu_{\mathrm{e}} / \mu_{\mathrm{o}}$ , is calculated from the following relations:

1. For $\pi / y > \pi / d$ ,

$$
^ {8 7}
$$

$$
\frac {\mu_ {e}}{\mu_ {o}} = \frac {\int_ {\pi / \lambda_ {\min }} ^ {\pi / y} n ^ {- 8 / 3} d n + \int_ {\pi / y} ^ {\pi / d} n ^ {- 8 / 3} \xi^ {2} d n}{\int_ {\pi / \lambda_ {\min }} ^ {\pi / \lambda_ {\max }} n ^ {- 8 / 3} d n}. \tag {40a}
$$

2. For $\pi / y < \pi / d$ (no damping),

$$
\frac {\mu_ {e}}{\mu_ {o}} = \frac {\int_ {\pi / \lambda_ {\min}} ^ {\pi / d} n ^ {- 8 / 3} d n}{\int_ {\pi / \lambda_ {\min}} ^ {\pi / \lambda} n ^ {- 8 / 3} d n}. \tag {40b}
$$

A numerical integration of Equation (40) with $\lambda_{\max} = d$ is shown on Figure 20 for both mobile and rigid damping.

The actual relative eddy diffusivity variation calculated from Equation (40) will not approach unity in midstream as in Figure 20 because the integration of the numerator is to include only eddies up to the size of the bubble diameter whereas the denominator is to be integrated over all wave sizes in the field.

Comparing the mobile and rigid interface curves on Figure 20 indicates that the two conditions would result in very little difference in mass-transfer behavior for an essentially passive bubble being acted upon simultaneously by many eddies - a result not too displeasing intuitively. A significant difference in behavior then, by this formulation, must come about by assigning a longer renewal period, $\mathbf{T}_{*}$ , to rigid interfaces than to mobile interfaces.

The variation of $\mu_{\mathrm{e}} / \mathfrak{S}$ required for a solution to Equation (35) can be obtained from the product

$$
\mu_ {e} / \mathfrak {Q} = \left(\frac {\mu_ {e}}{\mu_ {o}}\right) \left(\frac {\mu_ {o}}{\mathfrak {Q}}\right) \tag {41}
$$

if the values for eddy diffusivity in midstream, $\mu_{\circ}$ , are known.

![](images/1f5ee4ea0eb5d565e93c7a01aee38f59f258e3e3520c97b21a3f5e723a09b6ed.jpg)  
Figure 20. Dimensionless Variation of Eddy Diffusivity with Distance from an Interface. Effect of Surface Condition.

For the standard definition of eddy diffusivity, Groenhof<sup>59</sup> gives a correlation applicable to the midsection of a pipe,

$$
E = 0. 0 4 \sqrt {\tau_ {w} g _ {c} / \rho} D. \tag {42}
$$

Letting $\tau_{\mathrm{w}} = f \rho V^{2} / 8g_{c}$ and $f = 0.316 / \mathrm{Re}^{1 / 4}$ for smooth tubing, then E from Equation (42) is given by

$$
E / v = 0. 0 4 \sqrt {f / 8} R e = 0. 0 4 \sqrt {0 . 3 1 6 / 8} R e ^ {7 / 8}. \tag {143}
$$

Phillip's definition of eddy viscosity reduces to the standard definition in the midsection of a pipe. Consequently, it is acceptable to convert Equation (43) to

$$
\mu_ {0} / \Omega = 0. 0 4 \sqrt {0 . 3 1 6 / 8} \text {S c R e} ^ {7 / 8}, \tag {44}
$$

which along with Equation (4l) and Equations (40) fully determine a function

$$
\mu_ {o} / \mathscr {D} (R e, S c, d / D, r _ {*})
$$

for use in solving Equation (35).

It is realized that Phillip's analysis for eddy viscosity is not strictly applicable near an interface nor is the "eddy-cell" idealization a realistic picture of the turbulence. Nevertheless, the variation in eddy diffusivity based on these concepts was determined through Equations (43) and (40). It is felt that the behavior of a pseudo-turbulence such as this may be similar to a real turbulent field in that the essential features are retained and the trends predicted in this manner may be useful. For example, for the condition of turbulent transfer to a conduit wall itself there have been measurements of the standard eddy diffusivity distributions. Therefore, a comparison was made in Figure 21 of eddy diffusivities calculated in the above manner with Sleicher's

![](images/1709be77243311dbe690750797f8504fe872c17743d7c71efb27335de14100ad.jpg)  
Figure 21. Variation of Eddy Diffusivity with Distance from an Interface. Comparison of Calculated Values with Data of Sleicher.

data. $^{60}$ For this application of transfer to a conduit, the value of $d$ in Equation (40a) (the maximum eddy size in this case) was arbitrarily set equal to $1/2$ of the pipe radius, $r_o$ , and the coefficient in Equation (43) was adjusted slightly to require $\mu_e / \nu$ to coincide exactly with Sleicher's value in the pipe midsection at $Re = 14,500$ . Considering the difference in the eddy diffusivity definitions, the comparison is favorable and it appears that use of a pseudo-turbulence idealization such as this may provide a unique means of predicting eddy viscosity and eddy diffusivity variations. Since the determination of eddy diffusivities and their variation was not the primary concern of this thesis, further development of these concepts was not considered.

Equations (35), (36), (40), and (44), which represent the present surface renewal model were programmed on a digital computer and numerical solutions obtained using $\mathbf{T}_{*}$ as a parameter. Time did not permit a complete evaluation of this computer program and the results can only be presented here as tentative. Figure 22 illustrates the values of the exponents obtained for an equation of the form

$$
\mathrm {S h} _ {\mathrm {b}} \sim \mathrm {R e} ^ {\mathrm {a}} \mathrm {S c} ^ {\mathrm {b}} (\mathrm {d} / \mathrm {D}) ^ {\mathrm {c}}
$$

as a function of $\mathbf{T}_{*}$ . The value of $\mathbf{T}_{*}$ for which the Schmidt number exponent was 1/3 (corresponding to rigid interfaces) was approximately 2.7. At this value of $\mathbf{T}_{*}$ , the solution for the time-averaged pipe Sherwood number was essentially independent of the bubble diameter and varied according to

$$
\mathrm {S h} \sim \mathrm {R e} ^ {0. 8 5} \mathrm {S c} ^ {1 / 3}. \tag {45}
$$

The computer results as $\mathbf{T}_{*}$ approached zero appeared to approach the classical penetration solution of Equation (35) obtained for $\mu_{\mathrm{e}} / \mathfrak{Q} = 0$ ,

![](images/7863b32597318dcd1474d605d6d62abbd0cd9f3cc8066960e5d44a7225998981.jpg)  
Figure 22. Numerical Results of the Surface Renewal Model. Plots of a, b, and c (Exponents on Re, Sc, and d/D, Respectively) as Functions of the Dimensionless Period, $\mathbf{T}_{*}$ .

$$
\mathrm {S h} \sim \sqrt {\mathrm {S c} (d / D) ^ {8 / 3} \mathrm {R e} ^ {1 1 / 6}} / (d / D)
$$

or

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 2} \mathrm {R e} ^ {0. 9 2} (\mathrm {d} / \mathrm {D}) ^ {1 / 3},
$$

which is identical to Equation (27). Consequently, if the surface renewal period, $T_*$ , is interpreted as being a measure of the rigidity of the interface, $T_* \rightarrow 0$ being characteristic of mobile interfaces and $T_* \rightarrow \sim 2.7$ (in this case) being characteristic of rigid interfaces, then this surface renewal model may be useful.

Neither this model nor the preceding turbulence interaction model satisfactorily predict the observed variation of pipe Sherwood number with bubble diameter for this range of bubble sizes. Indirect support is therefore provided for the supposition that the observed linear variation may be the result of a transition from rigid to mobile behavior.

# CHAPTER VI

# SUMMARY AND CONCLUSIONS

Transient response experiments were performed using five different mixtures of glycerine and water. Liquid-phase-controlled mass-transfer coefficients were determined for transfer of dissolved oxygen into small helium bubbles in cocurrent turbulent gas-liquid flow. These coefficients were established as functions of Reynolds number, Schmidt number, bubble mean diameter, and gravitational orientation of the flow.

An analytical expression was obtained for the relative importance of turbulent inertial forces compared with gravitational forces, $\mathbf{F}_{\mathrm{i}} / \mathbf{F}_{\mathrm{g}}$ . For conditions in which this ratio was greater than $\sim 1.5$ , the variation in the observed mass-transfer coefficients with Reynolds numbers was linear on log-log coordinates with identical behavior for horizontal and vertical flows. Below $\mathbf{F}_{\mathrm{i}} / \mathbf{F}_{\mathrm{g}} = 1.5$ , the horizontal coefficient variation continued to be "linear" until the ratio of liquid axial velocity to bubble terminal velocity, $\mathbf{V} / \mathbf{V}_{\mathrm{b}}$ , decreased to about 3, where severe stratification made operation impractical. The vertical flow coefficients underwent a transition from the "linear" variation and approached constant asymptotes characteristic of bubbles rising through a quiescent liquid. The variable ratio of $\mathbf{F}_{\mathrm{i}} / \mathbf{F}_{\mathrm{g}}$ proved to be a useful linear scaling factor for describing the vertical flow coefficients in this transition region for which Equation (22) is the recommended correlation.

The Schmidt number exponent for the straight-line portions of the data was observed to be greater than $\frac{1}{2}$ based on physical property data for $\varnothing$ which may be suspect. Fitting the data with a Schmidt number

exponent of $1/2$ resulted in only slightly less precision than for the case in which the actual regression exponent was used, and a definitive choice could not be made between the two. Based on theoretical expectations, a Schmidt number exponent of $1/2$ would seem to be appropriate, and consequently, the recommended correlation is Equation (23).

The variation in mass-transfer coefficient with bubble mean diameter over the range covered was observed to be linear in agreement with the findings of Calderbank and Moo-Young $^{16}$ for agitated vessels. Some preliminary runs made with bubble mean diameters outside the range of this report indicated that the linear variation does not continue but that the coefficients level off at both smaller and larger diameters. Furthermore the coefficients tentatively appear to decrease slowly with increasing mean diameters above about 0.08 inches.

Consistent with findings of other investigations, the Reynolds number exponent was significantly greater than expected based on agitated vessel data compared on an equivalent power dissipation basis. One explanation is that there may exist greater gravitational influence in agitated vessels. Another is the postulated existence of different bubble relative flow regimes.

A seemingly anomalous behavior was observed for the Reynolds number variation in that the data for water (plus about 200 ppm N-butyl alcohol) exhibited significantly smaller Reynolds number exponents and a correspondingly smaller exponent for the ratio, $(\mathrm{d} / \mathrm{D})$ , than that for the glycerine-water mixtures. There may have been a difference in the interfacial conditions (the addition of the surfactant creates a "rigid"

interface while the glycerine-water mixtures apparently generally had "mobile" interfacial behavior). However, under steady relative flow conditions this would result in no difference in the Reynolds number exponent. Consequently, it was postulated that this difference resulted from the possible existence of different bubble relative flow regimes.

In support of the above contention, a two-regime "turbulence interaction" model was formulated by balancing turbulent inertial forces with drag forces that depend on the bubble relative flow Reynolds number. The resulting mean bubble velocities were substituted into "Frössling" equations to determine the mass-transfer behavior. The resulting Reynolds number exponent for one regime ( $\mathrm{Re}_{\mathrm{b}} < 2$ ) agreed very well with the experimental value for the glycerine-water mixtures and that for the other regime ( $\mathrm{Re}_{\mathrm{b}} > 2$ ) compared favorably with the water data and with agitated vessel data on an equivalent power dissipation basis.

The dependence of Sherwood number on the bubble-to-conduit diameter ratio, $\mathrm{d} / \mathrm{D}$ , predicted by the interaction model did not agree with the observed linear variation. Calderbank and Moo-Young<sup>16</sup> pointed out that the linear variation they observed in agitated vessels for bubbles of this size range probably resulted from a transition from "small" bubble to "large" bubble behavior. Such a transition could also explain the present observations, however, there was no satisfactory means for validating this.

For comparison, a second analytical model was developed based on surface renewal concepts which could also include different flow regimes. This model incorporated an eddy diffusivity that varied with Reynolds

number, Schmidt number, bubble diameter, interfacial condition, and position away from the interface. The variation of eddy diffusivity was established by using a pseudo-turbulent model in which the turbulence was simulated by superposed viscous eddy-cells damped by the bubble interface in a manner determined by Lamont.[11]

The surface renewal model assumed that the "renewal" period for the bubbles was related to the bubble "mean" velocity resulting from a balance between turbulent inertial forces and viscous resisting forces, thus allowing the casting of the equations into nondimensional form with the pipe Reynolds number, the Schmidt number, and $\mathrm{d} / \mathrm{D}$ as parameters. A closed solution of the equations was not obtained but a tentative numerical solution employing a digital computer indicated that, in the limit of small dimensionless renewal period, $\mathbf{T}_{\star}$ - interpreted as representing mobile interfacial behavior, the classical penetration solution of this particular form of the diffusion equation resulted.

As $\mathbf{T}_{\star}$ approached a value of approximately 2.7 (in this case), the computer solution was independent of $(d / D)$ and resulted in a Schmidt number exponent of $\sim 1 / 3$ . Therefore, this value of $\mathbf{T}_{\star}$ was interpreted as representing rigid interfacial behavior.

Explicit results based on the models described above along with a listing of the more significant observations of this study are given below:

1. Bubbles generated in a turbulent field are well characterized by the distribution function

$$
f (\delta) = 4 \left(\alpha^ {3} / \pi\right) ^ {1 / 2} \delta^ {2} \operatorname {E x p} (- \alpha \delta^ {2}),
$$

where

$$
\alpha \equiv [ 4 \sqrt {\pi} N / 6 \Phi ] ^ {2 / 3}.
$$

2. The average volume fractions occupied by gas in bubbly flow are approximated by Hughmark's correlation $^{54}$ only at higher flows. In horizontal flow, when the ratio of axial velocity of the liquid to the bubble terminal velocity is below $\sim 25$ , Hughmark's correlation predicts volume fractions lower than those observed. In vertical flow, while the volume fractions are higher in downcomer legs than in riser legs, they can be established by using Hughmark's correlation for the mean and accounting for the buoyant relative velocity of the bubbles in each leg.   
3. At low turbulent flows stratification of the bubbles in horizontal conduits prevented operation for ratios of axial velocity to bubble terminal velocity below $\sim 3$ .   
4. Even at Reynolds numbers well into the turbulent regime, horizontal and vertical flow mass-transfer coefficients differ. The Reynolds numbers above which they become equivalent are marked by the dominance of turbulent inertial forces over gravitational forces.   
5. As Reynolds numbers are reduced, vertical flow mass-transfer coefficients approach asymptotes characteristic of bubbles rising through a quiescent liquid. The ratio of turbulent inertial forces to gravitational forces serves as a useful linear scaling factor for estimating the mass-transfer coefficients at these lower Reynolds numbers.   
6. The effect of Reynolds number on Sherwood number for flow in conduits is not as would be expected based on comparison with agitated vessel data on an equivalent power dissipation basis. For example, the observed turbulence-dominated data are correlated by

$$
\mathrm {S h} / \mathrm {S c} ^ {1 / 2} = 0. 3 4 \mathrm {R e} ^ {0. 9 4} (\mathrm {d} / \mathrm {D}) ^ {1. 0} \tag {23}
$$

whereas one obtains from the agitated vessel data of Calderbank and Moo-Young<sup>16</sup> for small bubbles

$$
\mathrm {S h} / \mathrm {S c} ^ {1 / 3} = 0. 0 8 2 \mathrm {R e} ^ {0. 6 9}, \tag {2}
$$

and of Sherwood and Brian<sup>17</sup> for particulates

$$
\mathrm {S h} / \mathrm {S c} ^ {1 / 3} \sim \mathrm {R e} ^ {0. 6 1} (\mathrm {d} / \mathrm {D}) ^ {- 0. 1 2}. \tag {3}
$$

In this thesis the two-regime turbulence interaction model and the surface renewal model exhibit identical results for mobile interfaces in the "Stokes" regime $(\mathrm{Re}_{b} \leq 2)$ ,

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 2} \mathrm {R e} ^ {0. 9 2} (\mathrm {d} / \mathrm {D}) ^ {1 / 3},
$$

which compares well with the observations represented by Equation (23).

In the second regime $(\mathrm{Re}_{\mathrm{b}} > 2)$ , the turbulence interaction model for rigid interfaces results in

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 3} \mathrm {R e} ^ {0. 6 6} (\mathrm {d} / \mathrm {D}) ^ {- 0. 2 / 4. 2}
$$

and the rigid interface interpretation of the surface renewal model gives

$$
\mathrm {S h} \sim \mathrm {S c} ^ {1 / 3} \mathrm {R e} ^ {0. 8 5}
$$

as compared, for example, with Equations (2) and (3).

7. The observed linear variation of Sherwood number with bubble diameter was not predicted theoretically. Consequently, following Calderbank and Moo-Young, $^{16}$ it is conjectured that this variation results from a transition from rigid (small bubbles) to mobile (large bubbles) interfacial behavior for this size range.

8. Data of this study that were obviously gravitationally influenced compare favorably with data for particulates in agitated vessels, giving rise to the speculation that gravitational forces may be more influential in agitated vessels where there may exist a greater degree of anisotropy compared with flow in conduits.

# CHAPTER VII

# RECOMMENDATIONS FOR FURTHER STUDY

# Experimental

Time did not permit a complete investigation of the effects of all the independent variables. Consequently, projections of this study into the future include experiments involving variations of the conduit diameter and the interfacial condition. It is anticipated that these studies will help clarify the role of $\mathrm{d} / \mathrm{D}$ , in particular with regard to the observed linear variation of mass-transfer coefficient with bubble diameter. These projected studies will also attempt to extend the ranges of variables covered through improvements in the bubble generating and separating equipment. It is hoped that these improvements will reduce the magnitude of the "end-effect" and thereby provide greater precision to the data. Parenthetically, the high rates of mass transfer observed in the bubble separator may qualify it for further investigation as a possible efficient in-line gas-liquid contactor.

For practical purposes it is recommended that mass-transfer rates also be measured in regions of flow discontinuities such as elbows, tees, valves, venturis, and abrupt pipe size changes. An objective of these "discontinuity" studies would be to test Calderbank and Moo-Young's hypothesis that mass-transfer rates can be universally correlated with the power dissipation rates.

As a direct extension of the work of this thesis, others might consider use of different fluids to provide a more definitive variation of the Schmidt number and of the interfacial condition. The studies could

have the additional objective of demonstrating that surface tension is not an influential variable other than for its effect on the mobility of the interface. Experiments designed to look at the actual small-scale movements of bubbles in cocurrent turbulent flow and the eddy structure very close to the interface would help guide further theoretical descriptions and may help validate the dimensionally determined expression for the average turbulent inertial forces.

One contention of the present work, the possible existence of different flow regimes yielding different Reynolds number exponents, should be further tested. A substantially widened range of Reynolds number for a given bubble size in a viscous fluid might uncover a transition from one regime to another.

In practical applications, the interfacial area available for mass transfer is equally as important as the mass-transfer coefficient. Therefore, for systems in which relatively long term recirculation of the bubbles is anticipated, the bubble dynamic behavior becomes of interest. For example, more information is needed on bubble breakup and coalescence which tend to establish an equilibrium bubble size in a turbulent field. More important perhaps, is the effect of bubbles passing through regions with large changes in pressure (e.g., across a pump) where they may go into solution and, as the pressure is again reduced, renucleate and grow in size. The effects on mean bubble sizes and the interfacial areas available under such conditions are not well known and this particular aspect of bubble behavior could provide a fruitful field for further research.

# Theoretical

Two extreme viewpoints were taken in this report in which bubbles were considered as being either essentially passive in a turbulent field with the mass-transfer behavior being governed by the "sweeping" of the surface with random eddies or, alternatively, as moving through the turbulent liquid and establishing a boundary-layer type of behavior.

The "surface renewal" model developed in this report was only tentatively evaluated. Further development of the model is anticipated and additional solutions should demonstrate the technique by which surface renewal concepts can be applied to cocurrent turbulent flow.

A complete mechanistic description of mass transfer between bubbles and liquids in cocurrent turbulent flow would presumably include the transient effects of a developing boundary layer as a bubble is accelerated in first one direction and then the other by random inertial forces. Superimposed on this would be the effects of the surrounding eddy structure and the characteristics of the eddy penetrations through the developing boundary layer. Further efforts to theoretically describe these simultaneous effects should be considered with possible solutions on a digital computer.

The use of pseudo-turbulent fields (e.g., an eddy-cell structure) to determine the transport rates and to establish such properties as an eddy diffusivity should provide useful insights into the actual behavior in real fluids and should help predict data trends. For example, the multiple boundary layer structure established by Busse<sup>61</sup> for the vector field that maximizes momentum transport in a shear flow strongly resembles

an artificial eddy-cell structure. Starting with such a structure, one could work "backwards" to calculate eddy viscosities (for example) as a function of position away from a solid boundary.

#

# LIST OF REFERENCES

1. Oak Ridge National Laboratory, Molten Salt Reactor Program Semi-annual Progress Report for Period Ending February 29, 1968, USAEC Report ORNL-4254, August (1968).   
2. Peebles, F. N., "Removal of Xenon-135 from Circulating Fuel Salt of the MSBR by Mass Transfer to Helium Bubbles," USAEC Report ORNL-TM-2245, Oak Ridge National Laboratory, July (1968).   
3. Harriott, P., "A Review of Mass Transfer to Interfaces," The Can. Journal of Chem. Eng., April (1962).   
4. Calderbank, P. H., "Gas Absorption from Bubbles-Review Series No. 3., The Chemical Engineer, 209-233, October (1967).   
5. Gal-Or, B., G. E. Klinzing, and L. L. Tavlarides, "Bubble and Drop Phenomena," Ind. and Eng. Chem., 61(2): 21, February (1969).   
6. Tavlarides, L. L., et al., "Bubble and Drop Phenomena," Ind. and Eng. Chem., 62(11): 6, November (1970).   
7. Regan, T. M. and A. Gomezplata, "Mass Transfer," Ind. and Eng. Chem., 69(2): 41, February (1970).   
8. Regan, T. M. and A. Gomezplata, "Mass Transfer," Ind. and Eng. Chem., 62(12): 140, December (1970).   
9. Jepsen, J. C., "Mass Transfer in Two-Phase Flow in Horizontal Pipelines," AIChE Journal, 16(5): 705, September (1970).   
10. Scott, D. S. and W. Hayduk, "Gas Absorption in Horizontal Cocurrent Bubble Flow," Can. J. Chem. Eng., 44: 130 (1966).   
ll. Lamont, J. C., "Gas Absorption in Cocurrent Turbulent Bubble Flow," PhD Thesis, The University of British Columbia, August (1966).   
12. Lamont, J. C. and D. S. Scott, "Mass Transfer from Bubbles in Cocurrent Flow," Can. J. Chem. Eng., 201-208, August (1966).   
13. Heuss, J. M., C. J. King, and C. R. Wilke, "Gas-Liquid Mass Transfer in Cocurrent Froth Flow," AIChE Journal, 11(5): 866, September (1965).   
14. Marriott, P., "Mass Transfer to Particles: Part II. Suspended in a Pipeline," AIChE Journal, 8(1): 101, March (1962).   
15. Figueiredo, O. and M. E. Charles, "Pipeline Processing: Mass Transfer in the Horizontal Pipeline Flow of Solid-Liquid Mixtures," The Can. J. of Chem. Eng., 45: 12, February (1967).

16. Calderbank, P. H. and M. B. Moo-Young, "The Continuous Phase Heat and Mass-Transfer Properties of Dispersions," Chem. Eng. Sci., 16: 37 (1961).   
17. Sherwood, T. K. and P. L. T. Brian, "Heat and Mass Transfer to Particles Suspended in Agitated Liquids," U. S. Dept. of Interior Research and Development Progress Report No. 334, April (1968).   
18. Barker, J. J. and R. E. Treybal, "Mass Transfer Coefficients for Solids Suspended in Agitated Liquids," AIChE Journal, 6(2): 289-295, June (1960).   
19. Boyadzhiev, L. and D. Elenkov, "On the Mechanism of Liquid-Liquid Mass Transfer in a Turbulent Flow Field," Chem. Eng. Sci., 21: 955 (1966).   
20. Porter, J. W., S. L. Goren, and C. R. Wilke, "Direct Contact Heat Transfer Between Immiscible Liquids in Turbulent Pipe Flow," AICHe Journal, 14(1): 151, January (1968).   
21. Sideman, S. and Z. Barsky, "Turbulence Effect on Direct-Contact Heat Transfer with Change of Phase," AIChE Journal, 11(3): 539, May (1965).   
22. Sideman, S., "Direct Contact Heat Transfer Between Immiscible Liquids," Advances in Chemical Engineering, Vol. 6, pp. 207-286, Academic Press, New York (1966).   
23. Fortescue, G. E. and J. R. A. Pearson, "On Gas Absorption into a Turbulent Liquid," Chem. Eng. Sci., 22: 1163-1176 (1967).   
24. Kozinski, A. A. and C. J. King, "The Influence of Diffusivity on Liquid Phase Mass Transfer to the Free Interface in a Stirred Vessel, AIChE Journal, 12(1): 109-110, January (1966).   
25. King, C. J., "Turbulent Liquid Phase Mass Transfer at a Free Gas-Liquid Interface," Ind. Eng. Chem. Fund., 5(1): 1-8, February (1966).   
26. Peebles, F. N. and H. J. Garber, "Studies on the Motion of Gas Bubbles in Liquids, Chem. Eng. Progr., 49(2): 88-97, February (1953).   
27. Ruckenstein, E., "On Mass Transfer in the Continuous Phase from Spherical Bubbles or Drops," Chem. Eng. Sci., 19: 131-146 (1964).   
28. Griffith, R. M., "Mass Transfer from Drops and Bubbles," Chem. Eng. Sci., 12: 198-213 (1960).   
29. Redfield, J. A. and G. Houghton, "Mass Transfer and Drag Coefficients for Single Bubbles at Reynolds Numbers of 0.02-5000," Chem. Eng. Sci., 20: 131-139 (1965).

30. Chao, B. T., "Motion of Shperical Gas Bubbles in a Viscous Liquid at Large Reynolds Numbers," Phys. Fluids, 5(1): 69-79, January (1962).   
31. Lochiel, A. C. and P. H. Calderbank, "Mass Transfer in the Continuous Phase Around Axisymmetric Bodies of Revolution," Chem. Engr. Sci., 19: 475-484, Pergamon Press (1964).   
32. Higbie, R., "The Rate of Absorption of a Pure Gas Into a Still Liquid During Short Periods of Exposure," Presented at American Institute of Chemical Engineers Meeting, Wilmington, Delaware, May 13-15 (1935).   
33. Danckwerts, P. V., "Significance of Liquid-Film Coefficients in Gas Absorption," Ind. Eng. Chem., Engineering and Process Development, 43(6): 1460-1467, June (1951).   
34. Toor, H. L. and J. M. Marchello, "Film-Penetration Model for Mass and Heat Transfer," AIChE Journal, 4(1): 97-101, March (1958).   
35. Whitman, W. G., Chem. and Met. Eng., 29: 147 (1923).   
36. Levich, V. G., Physicochemical Hydrodynamics, Prentice-Hall, Inc., Englewoods Cliffs, N. J. (1962).   
37. Hinze, J. O., Turbulence, McGraw-Hill Book Co., Inc., New York (1959).   
38. Middleman, S., "Mass Transfer from Particles in Agitated Systems: Application of the Kolmogoroff Theory," AICHE Journal, 11(4): 750-761, July (1965).   
39. Harriott, P. and R. M. Hamilton, "Solid-Liquid Mass Transfer in Turbulent Pipe Flow," Chem. Eng. Sci., 20: 1073-1078 (1965).   
40. Brian, P. L. T. and M. C. Beaverstock, "Gas Absorption by a Two-Step Chemical Reaction," Chem. Eng. Sci., 20: 47-56 (1965).   
41. Davies, J. T., A. A. Kilner, and G. A. Ratcliff, "The Effect of Diffusivities and Surface Films on Rates of Gas Absorption," Chem. Eng. Sci., 19: 583-590 (1964).   
42. Gal-Or, B., J. P. Hauck, and H. E. Hoelscher, "A Transient Response Method for a Simple Evaluation of Mass Transfer in Liquids and Dispersions," Intern. J. Heat and Mass Transfer, 10: 1559-1570 (1967).   
43. Gal-Or, B. and W. Resnick, "Mass Transfer from Gas Bubbles in an Agitated Vessel with and without Simultaneous Chemical Reaction," Chem. Eng. Sci., 19: 653-663 (1964).   
44. Harriott, P., "A Random Eddy Modification of the Penetration Theory," Chem. Eng. Sci., 17: 149-154 (1962).

45. Koppel, L. B., R. D. Patel, and J. T. Holmes, "Statistical Models for Surface Renewal in Heat and Mass Transfer," AIChE Journal, 12(5): 941-955, September (1966).   
46. Kovásy, K., "Different Types of Distribution Functions to Describe a Random Eddy Surface Renewal Model," Chem. Eng. Sci., 23: 90-91 (1968).   
47. Perlmutter, D. D., "Surface-Renewal Models in Mass Transfer," Chem. Eng. Sci., 16: 287-296 (1961).   
48. Ruckenstein, E., "A Generalized Penetration Theory for Unsteady Convective Mass Transfer," Chem. Eng. Sci., 23: 363-371 (1968).   
49. Sideman, S., "The Equivalence of the Penetration and Potential Flow Theories," Ind. Eng. Chem., 58(2): 54-58, February (1966).   
50. Harriott, P., "Mass Transfer to Particles: Part I. Suspended in Agitated Tanks," AICHE Journal, 8(1): 93-101, March (1962).   
51. Banerjee, S., D. S. Scott, and E. Rhodes, "Mass Transfer to Falling Wavy Liquid Films in Turbulent Flow," Ind. Eng. Chem. Fund., 7(1): 22-26, February (1968).   
52. Barker, J. J. and R. E. Treybal, "Mass Transfer Coefficients for Solids Suspended in Agitated Liquids," AIChE Journal, 6(2): 289-295, June (1960).   
53. Galloway, T. R. and B. H. Sage, "Thermal and Material Transport from Spheres," Intern. J. Heat Mass Transfer, 10: 1195-1210 (1967).   
54. Hughmark, G. A., "Holdup and Mass Transfer in Bubble Columns," Ind. Eng. Chem., Process Design and Development, 6(2): 218-220, April (1967).   
55. Jordan, J., E. Ackerman, and R. L. Berger, "Polarographic Diffusion Coefficients of Oxygen Defined by Activity Gradients in Viscous Media," J. Am. Chem. Soc., 78: 2979, July (1956).   
56. Bayens, C., PhD Thesis, The Johns Hopkins University, Baltimore, Maryland (1967).   
57. Resnick, W. and B. Gal-Or, "Gas-Liquid Dispersions," Advances in Chemical Engineering, Academic Press, New York, Vol. 7, pp. 295-395 (1968).   
58. Phillips, O. M., "The Maintenance of Reynolds Stress in Turbulent Shear Flow," J. Fluid Mech., 27(1): 131-144 (1967).   
59. Groenhof, H. C., "Eddy Diffusion in the Central Region of Turbulent Flows in Pipes and Between Parallel Plates," Chem. Eng. Sci., 25: 1005-1014 (1970).

60. Sleicher, Jr., C. A., "Experimental Velocity and Temperature Profiles for Air in Turbulent Pipe Flow," Transactions of the ASME, 80: 693-704, April (1958).   
61. Busse, F. H., "Bounds for Turbulent Shear Flow," J. Fluid Mech., 41: 219-240 (1970).

![](images/ad2a2d0c951cb65068d0f51e2807d33763c7dda4aa03f3833db058ec375f8bde.jpg)

APPENDIX A

PHYSICAL PROPERTIES OF AQUEOUS-CLYCEROL MIXTURES

![](images/c79057e3a7fa65082d011124c2e208cfd601b4c8107a6d06985b32e07e88e6f0.jpg)  
Figure 23. Schmidt Numbers of Glycerine-Water Mixtures.

![](images/1dc1932a66efa776df970dcf90567da038197a899d70ac1f87fc977d334ca9f1.jpg)  
Figure 24. Henry's Law Constant for Oxygen Solubility in Glycerine-Water Mixtures.

![](images/d2ae20b60aed34b93a9045ca72bc62f3ed65f5f8289f7729eb1168c584767769.jpg)  
Figure 25. Molecular Diffusion Coefficients for Oxygen in Glycerine-Water Mixtures. Data of Jordan, Ackerman, and Berger.

![](images/4cdaeb94cf60e368076dce570e4dd86bf755b70d17f89852686c9d8fc36b3687.jpg)  
Figure 26. Densities of Glycerine-Water Mixtures.

![](images/3db6e2f440aa51394404852227645cd37877d987b22890c795c9eac68649bce1.jpg)  
Figure 27. Viscosities of Glycerine-Water Mixtures.

# APPENDIX B

# DERIVATION OF EQUATIONS FOR CONCENTRATION CHANGES

# ACROSS A GAS-LIQUID CONTACTOR

Consider the cocurrent flow of a gas and a liquid in a constant area pipeline of cross section $A_{c}$ and length $L$ . In a differential element of length $d\ell$ , a dissolved constituent of concentration $\overline{C}$ in the liquid is transferred into the gas as shown below.

$$
\begin{array}{l}Q _ {\ell} \overline {{C}} \rightarrow\\Q _ {g} \overline {{C}} g \rightarrow\\\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad\end{array}
$$

A mass balance for the dissolved constituent gives

$$
Q _ {\ell} d \overline {{C}} = - k a A _ {c} d \ell (\overline {{C}} - C _ {s}) \tag {B-1}
$$

$$
\mathrm {Q} _ {\mathrm {g}} \mathrm {d} \overline {{\mathrm {C}}} _ {\mathrm {g}} = + \mathrm {k a A} _ {\mathrm {c}} \mathrm {d} \ell (\overline {{\mathrm {C}}} - \mathrm {C} _ {\mathrm {s}}) \quad , \tag {B-2}
$$

where $\overline{C}$ is the liquid phase average concentration, $\overline{C}_{\mathrm{g}}$ is the gas phase concentration, and $C_{s}$ is the concentration existing at the gas-liquid interface.

Dividing Equation (B-2) by Equation (B-1) gives

$$
\frac {\mathrm {d} \overline {{\mathrm {C}}} _ {\mathrm {g}}}{\mathrm {d} \overline {{\mathrm {C}}}} = - \frac {\mathrm {Q} _ {\ell}}{\mathrm {Q} _ {\mathrm {g}}} \quad . \tag {B-3}
$$

Integrating Equation (B-3) and letting $\overline{C}_{\mathbf{g}} = 0$ when $\overline{C} = C_{i}$ gives

$$
\overline {{C}} _ {g} = \left(Q _ {2} / Q _ {g}\right) \left(C _ {i} - \overline {{C}}\right). \tag {B-4}
$$

If the interfacial concentration is assumed to be at "equilibrium" and the solubility of the dissolved constituent is expressible by Henry's

Law, then

$$
\mathrm {H C} _ {\mathrm {s}} = \overline {{\mathrm {C}}} _ {\mathrm {g}} \mathrm {R T}. \tag {B-5}
$$

Substituting Equation (B-4) into Equation (B-5) gives

$$
C _ {s} = \frac {R T}{H} \left(\frac {Q _ {\ell}}{Q _ {g}}\right) \left(C _ {i} - \bar {C}\right). \tag {B-6}
$$

Equation (B-6) can be substituted into Equation (B-1) to obtain

$$
\begin{array}{l} Q _ {\ell} d \overline {{C}} = - k a A _ {c} d \ell [ \overline {{C}} - (R T / H) (Q _ {\ell} / Q _ {g}) (C _ {i} - \overline {{C}}) ] \\ = - k a A _ {c} d \ell [ \overline {{C}} (1 + R T Q _ {\ell} / H Q _ {g}) - (R T Q _ {\ell} / H Q _ {g}) C _ {i} ] \quad . \tag {B-7} \\ \end{array}
$$

Expanding and dividing by $Q_{\ell} \mathrm{d}\ell$ gives

$$
\frac {\mathrm {d} \overline {{C}}}{\mathrm {d} \ell} + \beta \overline {{C}} = \frac {\text {k a A} _ {\mathrm {c}} \gamma \mathrm {C} _ {\mathrm {i}}}{\mathrm {Q} _ {\ell}} = \frac {\beta^ {\prime} \gamma}{(1 + \gamma)} \mathrm {C} _ {\mathrm {i}}, \tag {B-8}
$$

where $\beta^{\prime}\equiv kaA_{c}(1 + \gamma) / Q_{\ell}$ and $\gamma \equiv (\mathrm{RT} / \mathrm{H})(Q_{\ell} / Q_{g})$

Use of the integration factor $e^{\beta' \ell}$ permits the following solution

$$
\bar {C} = \left(\frac {\gamma}{1 + \gamma}\right) C _ {i} + (\text {c o n s t .}) e ^ {- \beta^ {\prime} l}. \tag {B-9}
$$

At $\ell = 0$ , $\overline{C} = C_{i}$ , therefore the constant of integration is

$$
(\text {c o n s t .}) = C _ {i} / (1 + \gamma)
$$

and

$$
\bar {C} = \left(\frac {\gamma}{1 + \gamma}\right) C _ {i} + \left(\frac {1}{1 + \gamma}\right) e ^ {- \theta^ {\prime} l} C _ {i}.
$$

Therefore the ratio of the exit $(\lambda = L)$ to inlet concentration, $C_{e} / C_{i}$ ,

is

$$
C _ {e} / C _ {i} = \frac {\gamma}{1 + \gamma} + \frac {1}{1 + \gamma} e ^ {- \beta^ {\prime} L},
$$

or defining $\beta \equiv \theta^{\prime}L,$

$$
C _ {e} / C _ {i} = \frac {\gamma + e ^ {- \beta}}{1 + \gamma},
$$

where

$$
\gamma \equiv (\mathrm {R T} / \mathrm {H}) \left(Q _ {\ell} / Q _ {\mathrm {g}}\right) \text {a n d} \beta = \frac {\mathrm {k a A} _ {\mathrm {c}} \mathrm {L} (1 + \gamma)}{Q _ {\ell}}.
$$

![](images/ff989edbcbc87eeefb4473bbec4bc42bf38a123e90e1c5e02144ddcb21c64a6e.jpg)

# APPENDIX C

# INSTRUMENT APPLICATION DRAWING

![](images/da57ddcb77e4ab8615cb06f8c676727cbdae87ab66ab869f72bee7c81260a92b.jpg)  
Figure 28. Instrument Application Drawing of the Experiment Facility.

__________

__________

__________

__________

__________

__________

__________

__________

![](images/4f466d1d852af3019a6c36ac9b3239152ff6430bcf702beacf7a1c5dc256cff2.jpg)  
Figure 29. Bubble Size Range Produced by the Bubble Generator.

![](images/0d8263b33b1adc1f7e3ccab40a286d56d99a1ef48f593ff88140b362716f3040.jpg)  
Figure 30. Calibration of Rotameter No. 1 (100 gpm).

![](images/ecf132c5f3182531c7b1de7e51302821f601537ca4cb5cddbf1791206d893b17.jpg)  
Figure 31. Calibration of Rotameter No. 2 (40 gpm).

![](images/91f6e6cfd909fc1b03bf31ebf8b13edfb6be5ed4c88c0833fab45fe1cc4be2b3.jpg)  
Figure 32. Calibration of Rotameter No. 3 (8 gpm).

![](images/f3193a5ed05878059f3f53d05458a9abc6e791dc649fa2cfd32871b263cbb327.jpg)  
$\triangle P$ , PRESSURE DROP ACROSS CAPILLARY TUBE (inches of water)   
Figure 33. Calibration of Gas-Flow Meter at 50 psig.

![](images/acf617fac0b0f85247b1c7732cf88a937544f6df33626078ea529de0bbbf0999.jpg)  
DISSOLVED OXYGEN READING (ppm)   
Figure 34. Calibration of Oxygen Sensors in two Mixtures of Glycerine and Water.

# APPENDIX E

# EVALUATION OF EFFECT OF OXYGEN SENSOR RESPONSE SPEED ON THE MEASURED TRANSIENT RESPONSE OF THE SYSTEM

Instrument responses are typically exponential in nature. Thus, if the sensor reading is defined as $C_r$ , and the actual loop concentration as $\overline{C}$ (both functions of time) it is safe to assume an instrument response equation of the form

$$
\frac {d C _ {r}}{d t} = K _ {r} \left(\bar {C} - C _ {r}\right), \tag {E-1}
$$

where $\mathbf{K}_r$ is an instrument response coefficient.

The transient response of the loop itself is given by an equation of the form

$$
\overline {{C}} = C _ {o} e ^ {- K L ^ {t}}.
$$

Therefore, Equation (E-1) can be expressed as

$$
\frac {\mathrm {d} \mathrm {C} _ {r}}{\mathrm {d} t} + \mathrm {K} _ {r} \mathrm {C} _ {r} = \mathrm {K} _ {r} \mathrm {C} _ {o} e ^ {- \mathrm {K} _ {L} t}. \tag {E-2}
$$

Integration of Equation (E-2) with the initial condition $C_{r} = C_{0}$ at $t = 0$ gives

$$
\begin{array}{l} C _ {r} / C _ {o} = \left[ 1 - K _ {r} / \left(K _ {r} - K _ {L}\right) \right] e ^ {- K _ {r} t} + \left[ K _ {r} / \left(K _ {r} - K _ {L}\right) \right] e ^ {- K _ {L} t} \\ = \mathrm {A e} ^ {- \mathrm {K} _ {\mathrm {r}} t} + \mathrm {B e} ^ {- \mathrm {K} _ {\mathrm {L}} t}. \tag {E-3} \\ \end{array}
$$

The manufacturers stated response time for the Magna oxygen sensors is $90\%$ in 30 seconds. This response results in a value of

$$
\mathrm {K} _ {\mathrm {r}} = 4. 6 1 \quad .
$$

The maximum observed rate of change of oxygen concentration in the transient experiments corresponded to

# 130

$$
\mathrm {K} _ {\mathrm {L}} = 0. 7 5 \quad .
$$

(On the average, the experiment transients resulted in $\mathrm{K_L} < 0.3$ .) Therefore, for this case, $A = -0.19$ , $B = 1.19$ and

$$
C _ {r} / C _ {o} = 1. 1 9 e ^ {- 0 \cdot 7 5 t} - 0. 1 9 e ^ {- 4 \cdot 6 1 t}. \tag {E-4}
$$

An examination of Equation (E-4) shows that as time progresses the second term becomes negligible compared to the first, and the measured slope approaches the actual transient slope of 0.75. For example, the measured slope for this "worse" case is 0.74 after only one minute of transient compared to the real value of 0.75. Therefore, to further minimize this possible error, the slopes of the measured transients were taken only from the final six minutes of the curve permitting an initial "response adjustment" time of several minutes. The error due to the instrument response, then, is assumed to be negligible.

# APPENDIX F

# MASS BALANCES FOR THE SURFACE RENEWAL MODEL

Consider a differential region in a spherical shell of fluid surrounding a bubble as shown below.

![](images/b0f888ae934d233071a574bc6f3810951a9539db280b17515cf048d349d2a5b5.jpg)

Mass balances for the concentration, C, of a dissolved constituent within the liquid are obtained as follows:

# Convection

$$
\text {i n :} \quad \mathrm {U} _ {\mathrm {r}} \mathrm {C} 4 \pi \mathrm {r} ^ {2}
$$

$$
\text {o u t :} \quad 4 _ {\pi} (r + d r) ^ {2} [ U _ {r} C + \frac {\partial (U _ {r} C)}{\partial r} d r
$$

$$
\text {n e t} = (\text {o u t - i n}) = \boxed {4 \pi r ^ {2} \frac {\partial (U _ {r} C)}{\partial r} d r + 8 \pi r d r (U _ {r} C)} \tag {F-1}
$$

# Diffusion

$$
\text {i n :} \quad \mathfrak {D} 4 \pi r ^ {2} \frac {\partial C}{\partial r}
$$

$$
\text {o u t :} \quad 4 \pi (r + d r) ^ {2} \left[ \frac {\partial c}{\partial r} + \frac {\partial^ {2} c}{\partial r ^ {2}} d r \right]
$$

$$
\text {n e t} = (\text {o u t - i n}) = \left[ \vartheta 4 \pi r ^ {2} \frac {\partial^ {2} C}{\partial r ^ {2}} d r + \vartheta 8 \pi r d r \frac {\partial C}{\partial r} \right] \tag {F-2}
$$

# Storage

$$
\begin{array}{l} \text {n e t} = \frac {2 4 \pi}{3} [ (r + d r) ^ {3} - r ^ {3} ] \frac {\partial C}{\partial t} \\ \cong \boxed {- 4 \pi r ^ {2} d r \frac {\partial C}{\partial t}} \tag {F-3} \\ \end{array}
$$

Summing the contributions (F-1) through (F-3) gives

$$
\begin{array}{l} - 4 \pi r ^ {2} d r \frac {\partial C}{\partial t} + 9 4 \pi r ^ {2} d r \left[ \frac {\partial^ {2} C}{\partial r ^ {2}} + \frac {2}{r} \frac {\partial C}{\partial r} \right] \\ + 4 \pi r ^ {2} d r \left[ \frac {\partial (U _ {r} C)}{\partial r} + \frac {2}{r} (U _ {r} C) \right] = 0. \\ \end{array}
$$

Dividing by $4\pi r^2$ dr gives

$$
\frac {\partial C}{\partial t} = \mathcal {D} \left[ \frac {\partial^ {2} C}{\partial r ^ {2}} + \frac {2}{r} \frac {\partial C}{\partial r} \right] + \frac {1}{r ^ {2}} \frac {\partial \left(r ^ {2} U _ {r} C\right)}{\partial r}. \tag {F-4}
$$

Making the Reynolds assumptions

$$
\begin{array}{l} \mathrm {C} \equiv \overline {{\mathrm {C}}} + \mathrm {C} ^ {\prime} \\ U _ {r} = u ^ {\prime}, \\ \end{array}
$$

substituting into Equation (F-4), expanding and collecting terms gives

$$
\begin{array}{l} \frac {\partial \overline {{C}}}{\partial t} + \frac {\partial C ^ {\prime}}{\partial t} = 0 \left[ \frac {\partial^ {2} \overline {{C}}}{\partial r ^ {2}} + \frac {\partial^ {2} C ^ {\prime}}{\partial r ^ {2}} + \frac {2}{r} \frac {\partial \overline {{C}}}{\partial r} + \frac {2}{r} \frac {\partial C ^ {\prime}}{\partial r} \right] \\ + \frac {\partial (u \overline {{c}})}{\partial r} + \frac {\partial (u ^ {\prime} c ^ {\prime})}{\partial r} + \frac {2}{r} (u \overline {{c}}) + \frac {2}{r} (u ^ {\prime} c ^ {\prime}). \tag {F-5} \\ \end{array}
$$

The time average of a quantity, C, is defined as

$$
\overline {{C}} \equiv \frac {\int t _ {1} ^ {t _ {2}} C d t}{(t _ {2} - t _ {1})}
$$

in which the time interval, $(t_2 - t_1)$ , is long enough for the time average of the fluctuating quantities in Reynolds assumption to be zero but short compared to the transient changes in $\overline{C}$ . Therefore, a time average of Equation (F-5) gives

$$
\frac {\partial \overline {{C}}}{\partial t} = \delta \left[ \frac {\partial^ {2} \overline {{C}}}{\partial r ^ {2}} + \frac {2}{r} \frac {\partial \overline {{C}}}{\partial r} \right] + \frac {1}{r ^ {2}} \frac {\partial}{\partial r} \left(r ^ {2} \overline {{u ^ {\prime} C ^ {\prime}}}\right). \tag {F-6}
$$

# ESTIMATE OF ERROR DUE TO END-EFFECT ADJUSTMENTS

The measured ratios of exit-to-inlet concentration, K, across a gas-liquid contacter were extracted from the measured slope, S, of the log-concentration versus time data by the relation

$$
K = e ^ {- S V _ {s} / Q _ {l}}.
$$

The error involved in measuring the various quantities used to establish $K$ are estimated to be

$$
\frac {\Delta S}{S} \sim 0. 0 1,
$$

$$
\frac {\Delta \mathrm {V} _ {\mathrm {S}}}{\mathrm {V} _ {\mathrm {S}}} \sim 0. 0 3,
$$

and

$$
\frac {\triangle Q _ {l}}{Q _ {l}} \sim 0. 0 3
$$

Consequently, the error in $\mathbf{K}$ can be estimated from

$$
\frac {\Delta \mathrm {K}}{\mathrm {K}} \sim \frac {\mathrm {K} _ {\max } - \mathrm {K} _ {\min }}{\mathrm {K}},
$$

where

$$
K _ {\max } = \exp \left[ - \frac {(s - \Delta S) (V _ {s} - \Delta V _ {s})}{(Q _ {l} + \Delta Q _ {l})} \right]
$$

and

$$
K _ {\min } = \operatorname {E x p} \left[ - \frac {(S + \Delta S) (V _ {s} + \Delta V _ {s})}{(Q _ {\ell} - \Delta Q _ {\ell})} \right]
$$

The minimum ratio measured for K was $\sim 0.9$ , therefore the maximum estimate of the error is

$$
\frac {\Delta \mathrm {K}}{\mathrm {K}} \sim \frac {0 . 9 ^ {\frac {(0 . 3 7) (0 . 9 3)}{(1 . 0 3)}} - 0 . 9 ^ {\frac {(1 . 0 1) (1 . 0 3)}{(0 . 9 7)}}}{0 . 9} \sim 0. 0 2.
$$

In Chapter III, the ratio, $\mathbf{K}_{\mathbf{a}}$ , applicable to the test section above was calculated from

$$
\mathrm {K} _ {2} = \mathrm {K} _ {\mathrm {I}} / \mathrm {K} _ {\mathrm {I I}},
$$

where $\mathbf{K}_{\mathrm{I}}$ was the measured ratio across the bubble generator, the test section, and the bubble separator together, and $\mathbf{K}_{\mathrm{II}}$ was that across just the bubble generator and bubble separator. Therefore, the maximum instrument-precision induced error in $\mathbf{K}_{\mathrm{g}}$ is estimated to be

$$
\begin{array}{l} \frac {\Delta \mathrm {K} _ {3}}{\mathrm {K} _ {2}} \sim \frac {\mathrm {K} _ {2 , \max } - \mathrm {K} _ {2 , \min }}{\mathrm {K} _ {2}} \\ \sim \frac {\mathrm {K} _ {\mathrm {I}} / \mathrm {K} _ {\mathrm {II}} \left(\frac {1 + 0 . 0 2}{1 - 0 . 0 2}\right) - \mathrm {K} _ {\mathrm {I}} / \mathrm {K} _ {\mathrm {II}} \left(\frac {1 - 0 . 0 2}{1 + 0 . 0 2}\right)}{\mathrm {K} _ {\mathrm {I}} / \mathrm {K} _ {\mathrm {II}}} <   10 \% \\ \end{array}
$$

In establishing $\mathbf{K}_{\mathrm{I}}$ and $\mathbf{K}_{\mathrm{II}}$ in separate tests, the inability to exactly duplicate conditions results in an error greater than the above. An estimate of the maximum magnitude of this error can be had by examining the data for the $75\%$ water- $25\%$ glycerine mixture (Figure 13, page 63). Before the end-effect adjustment, the calculated vertical and horizontal flow mass-transfer coefficients for the 0.02-inch mean diameter bubbles were essentially identical. However, after the adjustment they differed by $\sim 25\%$ . It is felt that this difference mostly arises from the inability to exactly recreate the vertical flow conditions as a result of alterations made in the bubble generator between the original test and

the end-effect test. Consequently the horizontal flow data are considered the more "exact" although they should still reflect the $\sim 10\%$ error estimated due to measurement precision.

APPENDIX H

MASS TRANSFER DATA

![](images/f92cffc70cce18b4dc8db873c89f7e08a57f240d38b78fa5bceccae2bb7da13b.jpg)  
k, UNADJUSTED MASS TRANSFER COEFFICIENT (ft/hr)   
Figure 35. Unadjusted Mass Transfer Data. Water Plus ~200 ppm N-Butyl Alcohol. Vertical Flow.

![](images/71e0f34e8295c94c94de1f985c2885045597c5a2c5776b4a0148a98ee0116833.jpg)  
k, UNADJUSTED MASS TRANSFER COEFFICIENT (ft/hr)   
Figure 36. Unadjusted Mass Transfer Data. Water Plus $\sim$ 200 ppm N-Butyl Alcohol. Horizontal Flow.

![](images/a587ebf672c457e367875d399bea457c2692c5231733627eb16a46f40ee85af5.jpg)  
Figure 37. Unadjusted Mass Transfer Data. $12.5\%$ Glycerine-87.5% Water. Vertical Flow.

![](images/1b18ffb3f8e6a1c2498448f5f7ae70a745e9bc43dfb857e9697f44bc5084d39d.jpg)  
Figure 38. Unadjusted Mass Transfer Data. $12.5\%$ Glycerine-87.5% Water. Horizontal Flow.

![](images/5d6881653dbad294ee18e92f9ced18abd58751c99d35ac99cf410ff15249be78.jpg)  
Figure 39. Unadjusted Mass Transfer Data. $25\%$ Glycerine- $75\%$ Water. Vertical Flow.

![](images/4daaa33ffe14800159313a371cca1a28f99d4bcdd61811087c5ed03757998fcc.jpg)  
Figure 40. Unadjusted Mass Transfer Data. $25\%$ Glycerine- $75\%$ Water. Horizontal Flow.

![](images/78b431f4de384684f39760ca90318dcf014e41e81628587c9c598c961bfa013b.jpg)  
Figure 41. Unadjusted Mass Transfer Data. $37.5\%$ Glycerine- $62.5\%$ Water. Vertical Flow.

![](images/a13fee66b128335fa1e06c7a4c163b1fcc133777bc9fd4933707c8f377b382b0.jpg)  
Figure 42. Unadjusted Mass Transfer Data. $37.5\%$ Glycerine- $62.5\%$ Water. Horizontal Flow.

![](images/19b15fc55f571ea2fc338076a01891abfcc239fb0f32a9fca47365a10fb5d2db.jpg)  
Figure 43. Unadjusted Mass Transfer Data. $50\%$ Glycerine- $50\%$ Water. Vertical Flow.

![](images/c5d8573b73c0d9737006e4356c73117ef261362285ed72901a775c4d9dd319b3.jpg)  
Figure 44. Unadjusted Mass Transfer Data. $50\%$ Glycerine- $50\%$ Water. Horizontal Flow.

![](images/13946799e5df78c933982874df91f6dd65118542335d6c90bcf1596296638c51.jpg)  
Figure 45. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. Water Plus $\sim$ 200 ppm N-Butyl Alcohol. Horizontal and Vertical Flow.

![](images/fc83d1267e80fe33549d3ced0f8d658b8dcd4f63ea3827507a3d01519a25cf73.jpg)  
Figure 46. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $12.5\%$ Glycerine-87.5% Water. Horizontal and Vertical Flow.

![](images/6d116f1fe8f061b3ee82287c26ff7f0ca24cf642707f91b4809057b35eefaf69.jpg)  
Figure 47. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $25\%$ Glycerine- $75\%$ Water. Horizontal and Vertical Flow.

![](images/a575ba4719c9fef7c831b243c3b1534d522270563cbeb57d98728d599fc91680.jpg)  
Figure 48. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $37.5\%$ Glycerine- $62.5\%$ Water. Horizontal and Vertical Flow.

![](images/b466b5a87c7bef602af7974b724d3a34699a1dda889a15c1192343e84af080fe.jpg)  
Figure 49. Unadjusted Mass Transfer Coefficients Versus Pipe Reynolds Number as a Function of Bubble Sauter-Mean Diameter. $50\%$ Glycerine- $50\%$ Water. Horizontal and Vertical Flow.

![](images/5bb1570c29521bdb2432bc553e32b51ecd506ff88d330bbfb78a5ae8e881d7a5.jpg)  
Figure 50. Mass Transfer Data Adjusted for End-Effect. Water Plus $\sim 200$ ppm N-Butyl Alcohol. Vertical Flow.

![](images/5ab54d73c9aea46c1bcc5b0b9ac5f6ec4ae98677a57052d13e61154c6dc1863d.jpg)  
Figure 51. Mass Transfer Data Adjusted for End-Effect. Water Plus $\sim 200$ ppm N-Butyl Alcohol. Horizontal Flow.

![](images/2e462742c652e5142ffe24ad7410b0ee3fb588344572d6376e05ab4a19b45d4a.jpg)  
k, MASS TRANSFER COEFFICIENT (ft/hr)   
Figure 52. Mass Transfer Data Adjusted for End-Effect. $12.5\%$ Glycerine-87.5% Water. Vertical Flow.

![](images/5f71ff620075719fcec2df637c18102381450ded9938235996e656234a315863.jpg)  
Figure 53. Mass Transfer Data Adjusted for End-Effect. $12.5\%$ Glycerine-87.5% Water. Horizontal Flow.

![](images/8dfb5804274879d31343f8928da47fcb6fd7bacc8ae80cf498726e8145b1964a.jpg)  
Figure 54. Mass Transfer Data Adjusted for End-Effect. $25\%$ Glycerine- $75\%$ Water. Vertical Flow.

![](images/7127cbc66c59ed1b8dc093dd622fca61a4f665c6d3381aa996affa00ac9ee476.jpg)  
Figure 55. Mass Transfer Data Adjusted for End-Effect. $25\%$ Glycerine- $75\%$ Water. Horizontal Flow.

ORNL-DWG 71-7981

![](images/497fb105c65b5fd3e0ada69e942ee1223d70a73d26e2f1f802a3ef90c1761f7a.jpg)  
Figure 56. Mass Transfer Data Adjusted for End-Effect. $37.5\%$ Glycerine- $62.5\%$ Water. Horizontal Flow.

![](images/d28cb51a4c2db5716b7140e05209c17ea6c54b794a4c93477e1ec87e703dc7bd.jpg)  
Figure 57. Mass Transfer Data Adjusted for End-Effect. $50\%$ Glycerine- $50\%$ Water. Vertical Flow.

![](images/0dbdb79031a436e56555717d269dae981edcf2607372754d8e05ee4c8014d228.jpg)  
Figure 58. Mass Transfer Data Adjusted for End-Effect. $50\%$ Glycerine- $50\%$ Water. Horizontal Flow.

# LIST OF SYMBOLS

a Bubble interfacial area per unit volume

a. Mean acceleration of a fluid element of size $\lambda$ in a turbulent field

A Conduit cross sectional area

$A_{b}$ Bubble projected cross sectional area

C Local concentration of a dissolved constituent in a liquid

Time averaged component of C

C' Turbulent fluctuating component of C

Cavg Bulk-average concentration of a dissolved constituent in a liquid

C $d$ Drag coefficient for a bubble moving through a liquid

C i Gas-liquid contactor inlet value of C avg

C e Gas-liquid contactor exit value of C avg

$\mathbf{C}_{\mathrm{o}}$ Initial value of $\mathbf{C}_{\mathrm{avg}}$

C s Interfacial value of C

d Bubble diameter

ds Sauter-mean diameter of a bubble dispersion

$$
[ \equiv \int_ {0} \delta^ {3} f (\delta) d \delta / \int_ {0} \delta^ {2} f (\delta) d \delta ]
$$

D Conduit diameter

Molecular diffusion coefficient

E Eddy viscosity

f Blasius friction coefficient

f(δ) Bubble size distribution function

f(n) Frequency distribution function for turbulent eddies of wave number n

$\mathbf{F}_{\mathrm{d}}$ Drag force on a bubble moving through a liquid

$\mathbf{F}_{\mathrm{j}}$ Mean inertial force on a bubble due to turbulent fluctuations

$\mathbf{F}_{\alpha}$ Gravitational force on a bubble (buoyancy)

g Gravitational acceleration

$\mathbf{g}_{c}$ Dimensional proportionality constant relating force to the

product of mass and acceleration

H Solubility constant in Henry's Law relations

J Mass transfer per unit time per unit volume of liquid

k Local mass-transfer coefficient

k Axially averaged mass-transfer coefficient

Horizontal flow values of k

$\mathbf{k}_{\mathrm{v}}$ Vertical flow values of k

ka Low flow asymptotic value of $\mathbf{k}_{\nu}$

K Ratio of test section exit-to-inlet concentration, $C_{e} / C_{i}$

$\mathbf{K}_{\mathrm{T}}$ Loop response coefficient

$\mathbf{K}_{\mathbf{r}}$ Oxygen sensor response coefficient

L Test section length

M Mass of a fluid element

n Wave number of a turbulence component

N Number of bubbles per unit volume of liquid

Local pressure in the conduit

$Q_{\mathrm{g}}$ Volumetric flow rate of gas bubbles

Q, Volumetric flow rate of liquid

R Universal gas constant

r Radial coordinate

Fractional rate of surface renewal

t Time coordinate

T Absolute temperature

$\mathbf{U}_{r}$ Radially directed velocity in spherical coordinates

$\mathbf{u}^{\prime}$ Fluctuating component of $\mathbf{U}_{\mathbf{r}}$

Contribution to u' of eddies of wave number n

V Liquid axial velocity

V. Bubble terminal velocity within a liquid in a gravity field

Mean fluctuating velocity of a bubble in a turbulent fluid

Mean fluctuating velocity of a fluid element in a turbulent field

$\mathbf{V}_{\mathfrak{b}}$ Relative mean fluctuating velocity between a bubble and the liquid

V. Bubble total velocity in the riser leg of a vertical test section

$\mathbf{V}_{\mathrm{d}}$ Bubble total velocity in the downcomer leg of a vertical test section

$\Delta V$ Mean variation in velocity over a given distance in a turbulent field

V s Volume of the closed recirculating experiment system

W Added mass coefficient for an accelerating spherical bubble

x Axial coordinate

X A flow parameter used by Hughmark in correlating volume fractions

Y Ratio of liquid-to-total volumetric flow $\left[\mathbb{Q}_{\ell} / \left(\mathbb{Q}_{\ell} + \mathbb{Q}_{\mathrm{g}}\right)\right]$

Z A flow parameter used by Hughmark in correlating volume fractions

$$
\left(\equiv \operatorname {R e} ^ {1 / 6} \operatorname {F r} ^ {1 / 8} / \Upsilon^ {1 / 4}\right)
$$

# Greek Symbols

$\alpha$ Parameter in bubble size distribution function

Gas-liquid contacter parameter $\left[\equiv$ ka AL $(1 + \gamma) / Q_{\ell}\right]$

Y Gas-liquid contact parameter $\left[\equiv\mathrm{RTQ}_{\mathfrak{L}} / \mathrm{HQ}_{\mathfrak{g}}\right]$

$\delta$ Bubble diameter used in distribution function (same as d) $\epsilon_{m}$ Energy dissipation per unit mass in a turbulent liquid $\epsilon_{v}$ Energy dissipation per unit volume in a turbulent liquid $\lambda$ Distance scale in a turbulent liquid $\lambda_{min}$ Minimum eddy size in a turbulent liquid $\lambda_{max}$ Maximum eddy size in a turbulent liquid $\mu$ Liquid viscosity $\mu_{e}$ Eddy diffusivity $\mu_{e,n}$ Contribution to $\mu_{e}$ from turbulent component of wave number n $\mu_{o}$ Undamped eddy diffusivity away from an interface $\nu$ Kinematic viscosity ( $\equiv \mu/\rho$ ) $\xi$ Interfacial damping function for viscous eddy cells $\xi_{r}$ Rigid interface form of $\xi$ $\xi_{m}$ Mobile interface form of $\xi$ $\rho$ Liquid density $\tau_{w}$ Wall shear stress $\Phi$ Bubble volume fraction $\Phi_{d}$ Bubble volume fraction in the downcomer leg of a vertical test section $\Phi_{r}$ Bubble volume fraction in the riser leg of a vertical test section

# Dimensionless Quantities

$\mathbf{C}_{*}$ Dimensionless concentration $(\overline{\mathbb{C}} /\mathbb{C}_0)$ $\overline{\mathbf{C}}_{*}$ Radial average of $C_*$ Fr Froude number $(\equiv V^{2} / gD)$ $\mathrm{Pe_b}$ Bubble Peclet number $(\equiv \mathrm{Re}_{\mathrm{b}}\mathrm{Sc})$

$\mathbf{r}_{*}$ Dimensionless radial coordinate $(\equiv r / d)$

$\mathbf{r}_{*e}$ Dimensionless radius of spherical shell of liquid surrounding a bubble $[\equiv 1/2 \Phi^{1/3}]$

Re Pipe Reynolds number $(\equiv \mathrm{VD}\rho /\mu)$

$\mathrm{Re}_{\mathrm{b}}$ Bubble Reynolds number $(\equiv v_{\mathrm{b}}d\rho /\mu)$

$\mathbf{Re}_{\mathbb{T}}$ Stirrer Reynolds number defined as the product of the stirrer rotation speed, square of the stirrer diameter, and $\pi$ divided by the kinematic viscosity

Sc Schmidt number $(\equiv \mu /\rho \mathfrak{D})$

Sh Pipe Sherwood number $(\equiv kD / \mathfrak{Q})$

Sh Time average of Sh

Sh Bubble Sherwood number $(\equiv \mathrm{kd} / \mathcal{Q})$

$\mathfrak{t}_{*}$ Dimensionless time coordinate $(\equiv \mathrm{tv}_{\mathrm{b}} / \mathrm{d})$

$\mathbf{T}_{*}$ Period for surface renewal

![](images/5906df0b5821b684db970c359b58f15d70cf8a8d6496ba0d03ef61f5f9952477.jpg)

# INTERNAL DISTRIBUTION

1. L. G. Alexander   
2. J. L. Anderson   
3. C. F. Baes   
4. H. F. Bauman   
5. S. E. Beall   
6. E. S. Bettis   
7. R. Blumberg   
8. E. G. Bohlmann   
9. H. I. Bowers

10. R. B. Briggs   
11. S. Cantor   
12. D. W. Cardwell   
13. C. J. Claffey   
14. H. D. Cockran   
15. C. W. Collins   
16. E. L. Compere   
17. J. W. Cooke   
18. L. T. Corbin   
19. W. B. Cottrell   
20. J. L. Crowley   
21. F. L. Culler   
22. J.H.DeVan   
23. J. R. DiStefano   
24. S. J. Ditto   
25. W. P. Eatherly   
26. D. M. Eissenberg   
27. J. R. Engel   
28. D. E. Ferguson   
29. L. M. Ferris   
30. M. H. Fontana   
31. A. P. Fraas   
32. J.H.Frye   
33. L. C. Fuller   
34. W. K. Furlong   
35. C. H. Gabbard   
36. W.R.Gambill   
37. W. R. Grimes   
38. A. G. Grindell   
39. R. H. Guymon   
40. R. L. Hammer   
41. T. H. Harley   
42. W. O. Harms   
43. P. N. Haubenreich   
44. R.E.Helms   
45. P. G. Herndon   
46. D. M. Hewett   
47. H. W. Hoffman   
48. W.R.Huntley   
49. H. Inouye

50. J. K. Jones (K-25)   
51. W. H. Jordan   
52. P. R. Kasten   
53. R.J.Kedl   
54. J. J. Keyes, Jr.   
55. S. S. Kreslis   
56. O. H. Klepper   
57. J. W. Koger   
58. A. I. Krakoviak

59-63. T. S. Kress   
64. J. A. Lane   
65. Kermit Laughon, AEC-OSR   
66. A. W. Longest   
67. M. I. Lundin   
68. R. N. Lyon   
69. H. G. MacPherson   
70. R. E. MacPherson   
71. C. L. Matthews, AEC-OSR   
72. H. E. McCoy   
73. H. C. McCurdy   
74. D. L. McElroy   
75. H. A. McLain   
76. L. E. McNeese   
77. J. R. McWherter   
78. A. P. Malinauskas   
79. A. S. Meyer   
80. A. J. Miller   
81. W.R.Mixon   
82. R. L. Moore   
83. J. W. Michel   
84. F. H. Neill   
85. E. L. Nicholson   
86. T. S. Noggle   
87. P. Patriarca   
88. A. M. Perry   
89. H. B. Piper   
90. D. M. Richardson   
91. R.C.Robertson   
-93. M. W. Rosenthal   
94. H. M. Roth, AEC-ORO   
95. W. K. Sartory   
96. Dunlap Scott   
97. R. L. Senn   
98. J.H.Shaffer   
99. Myrtleen Sheldon   
100. J. D. Sheppard   
101. M. D. Silverman   
102. M. J. Skinner   
103. G. M. Slaughter

104. A. N. Smith

105. G.P. Smith

106. I. Spiewak

107. R. A. Strehlow

108. D. A. Sundberg

109. J. R. Tallackson

110. O.K. Tallent

111. R.E.Thoma

112. D. G. Thomas

113. D. B. Trauger

114. W. E. Unger

115. J. L. Wantland

116. A. M. Weinberg

117. J. R. Weir

118. J.C. White

119. G. D. Whitman

120. R.P.Wichner

121. L. V. Wilson

122. M. M. Yarosh

123. Gale Young

124. H.C.Young

125. F.C.Zapp

126-127. Central Research Library

128. Y-12 Document Reference Section

129-131. Laboratory Records Department

132. Laboratory Records Department (RC)

# EXTERNAL DISTRIBUTION

133. Norton Haberman, AEC-Washington

134. Milton Shaw, AEC-Washington

135-136. Division of Technical Information Extension (DTIE)

137. Laboratory and University Division, ORO

138-140. Director, Division of Reactor Licensing

141-142. Director, Division of Reactor Standards

143-147. Executive Secretary, Advisory Committee on Reactor Safeguards