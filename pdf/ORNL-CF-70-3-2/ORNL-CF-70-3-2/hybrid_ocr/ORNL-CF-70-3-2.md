DATE: March 2, 1970

SUBJECT: Calculation of Stresses During a Thermal Transient in a MSBR Outlet Nozzle

TO: Distribution

FROM: J. L. Spoormaker*

# ABSTRACT

Information is given about the thermal stresses developed in the outlet nozzles of a reactor vessel for a 1000 Mw(e) Molten-Salt Breeder Reactor for several step changes in the salt temperature. Calculation of the temperature distributions, as well as of the stresses, was carried out by finite element computer programs. Step temperature changes of 1300 to $1400^{\circ}\mathrm{F}$ , 1300 to $1600^{\circ}\mathrm{F}$ , 1300 to $1800^{\circ}\mathrm{F}$ , 1300 to $1200^{\circ}\mathrm{F}$ , and 1300 to $1100^{\circ}\mathrm{F}$ were considered. For each step change the number of cycles to failure was estimated and an estimation of whether or not gross cyclic yielding would occur was made.

# CONTENTS

Page

ABSTRACT 1

LIST OF FIGURES 5

NOMENCLATURE 9

1. INTRODUCTION 11   
2.DESCRIPTION OF CONFIGURATION AND FINITE ELEMENT IDEALIZATION 12

2.1. Configuration 12   
2.2. Finite Element Mesh 12

3．TEMPERATURE DISTRIBUTION CALCULATIONS 13  
4. STRESS ANALYSIS 14

4.1. General Remarks 14   
4.2. Evaluation of Stresses 14

5. RESULTS OF STRESS COMPUTATIONS 17

5.1. Steady-State Condition 17   
5.2. Step Change 1300 - 1400°F 17   
5.3. Step Change 1300 - 1600°F 18   
5.4. Step Change 1300 - 1800°F 18   
5.5. Step Change 1300 - 1200°F 19   
5.6. Step Change 1300 - 1100°F 20

6. CONCLUSIONS 20   
7. REFERENCES 21   
8. ACKNOWLEDGEMENTS 22   
9. FIGURES 23

# LIST OF FIGURES

Fig. 1. MSBR Reactor Vessel Flow Schematic.   
Fig. 2. MSBR Reactor Vessel Simplified Outlet Configuration.   
Fig. 3. MSBR Reactor Vessel Simplified Outlet Nozzle Detail.   
Fig. 4. Plot of the Outline of the Configuration.   
Fig. 5. Subplot of the Element Idealization (Pipe Region).   
Fig. 6. Subplot of the Element Idealization (Intersection Region).   
Fig. 7. Subplot of the Element Idealization (Nozzle Wall Region).   
Fig. 8. Subplot of the Element Idealization (Flat Plate).   
Fig. 9. Design Fatigue Strength, $S_{a}$ , for Ni-Mo-Cr Alloy.   
Fig. 10. Various Criteria for the Determination of the Design Stresses for INOR-8.   
Fig. 11. Temperature Distribution Across Section A-A in the Steady-State Condition.   
Fig. 12. Temperature Distribution Across Section B-B in the Steady-State Condition.   
Fig. 13. Temperature Distribution Across Section C-C in the Steady-State Condition.   
Fig. 14. Temperature Distribution Across Section D-D in the Steady-State Condition.   
Fig. 15. Temperature Distribution Across Section E-E in the Steady-State Condition.   
Fig. 16. Temperature Distribution Across Section F-F in the Steady-State Condition.   
Fig. 17. Stress Distribution Across Section A-A in the Steady-State Condition.   
Fig. 18. Stress Distribution Across Section B-B in the Steady-State Condition.   
Fig. 19. Stress Distribution Across Section C-C in the Steady-State Condition.   
Fig. 20. Stress Distribution Across Section D-D in the Steady-State Condition.   
Fig. 21. Stress Distribution Across Section E-E in the Steady-State Condition.   
Fig. 22. Temperature Distribution Across Section A-A After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 23. Temperature Distribution Across Section B-B After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 24. Temperature Distribution Across Section C-C After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

Fig. 25. Temperature Distribution Across Section D-D After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 26. Temperature Distribution Across Section E-E After the Step Change $1300 - 1400^{\circ}\mathrm{F}$   
Fig. 27. Stress Distribution Across Section A-A After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 28. Stress Distribution Across Section B-B After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 29. Stress Distribution Across Section C-C After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 30. Stress Distribution Across Section D-D After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 31. Stress Distribution Across Section E-E After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .   
Fig. 32. Temperature Distribution Across Section A-A After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 33. Temperature Distribution Across Section B-B After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 34. Temperature Distribution Across Section C-C After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 35. Temperature Distribution Across Section D-D After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 36. Temperature Distribution Across Section E-E After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 37. Stress Distribution Across Section A-A After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 38. Stress Distribution Across Section B-B After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 39. Stress Distribution Across Section C-C After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 40. Stress Distribution Across Section D-D After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 41. Stress Distribution Across Section E-E After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .   
Fig. 42. Temperature Distribution Across Section A-A After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 43. Temperature Distribution Across Section B-B After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 44. Temperature Distribution Across Section C-C After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 45. Temperature Distribution Across Section D-D After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

Fig. 46. Temperature Distribution Across Section E-E After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 47. Stress Distribution Across Section A-A After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 48. Stress Distribution Across Section B-B After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 49. Stress Distribution Across Section C-C After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 50. Stress Distribution Across Section D-D After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 51. Stress Distribution Across Section E-E After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .   
Fig. 52. Temperature Distribution Across Section A-A After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 53. Temperature Distribution Across Section B-B After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 54. Temperature Distribution Across Section C-C After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 55. Temperature Distribution Across Section D-D After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 56. Temperature Distribution Across Section E-E After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 57. Stress Distribution Across Section A-A After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 58. Stress Distribution Across Section B-B After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 59. Stress Distribution Across Section C-C After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 60. Stress Distribution Across Section D-D After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 61. Stress Distribution Across Section E-E After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .   
Fig. 62. Temperature Distribution Across Section A-A After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .   
Fig. 63. Temperature Distribution Across Section B-B After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .   
Fig. 64. Temperature Distribution Across Section C-C After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .   
Fig. 65. Temperature Distribution Across Section D-D After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .   
Fig. 66. Temperature Distribution Across Section E-E After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

Fig. 67. Stress Distribution Across Section A-A After the Step Change $1300 - 1100^{\circ}\mathbf{F}$ .   
Fig. 68. Stress Distribution Across Section B-B After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .   
Fig. 69. Stress Distribution Across Section C-C After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .   
Fig. 70. Stress Distribution Across Section D-D After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .   
Fig. 71. Stress Distribution Across Section E-E After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

# NOMENCLATURE

E Modulus of elasticity  
B Biot's number $\mathbf{S}_{\mathrm{a}}$ Allowable elastically calculated stress amplitude $\mathbf{S}_{\mathrm{alt}}$ Amplitude of stress fluctuation $\mathbf{S}_{\mathrm{y}}$ Uniaxial yield strength $\alpha$ Coefficient of thermal expansion $\theta$ Temperature $\Delta \theta$ Temperature difference $\nu$ Poisson's ratio $\sigma_{\mathrm{r}}$ Radial stress $\sigma_{\theta}$ Circumferential stress $\sigma_{\mathrm{z}}$ Axial stress $\sigma_{\mathrm{rz}}$ Shear stress $\sigma_{\mathrm{min}}$ Minimum stress in meridional plane $\sigma_{\mathrm{max}}$ Maximum stress in meridional plane $\sigma_{\mathrm{s}}$ Surface stress

# 1. INTRODUCTION

In a MSBR of 1000 Mw(e) the salt enters at a temperature of $1050^{\circ}\mathrm{F}$ and will rise about $250^{\circ}\mathrm{F}$ as it passes the core. Under normal conditions it is assumed that the salt temperature in and around the outlet nozzle will be at $1300^{\circ}\mathrm{F}$ .

There are, however, circumstances in which the salt from the core changes rapidly in temperature. Shortly after such a change, high temperature gradients, and hence high thermal stresses, will occur near the inner surface of the outlet nozzle and the connected pipe. Because the heat dissipates through the structure, discontinuity stresses are also produced at the intersection of the pipe and the nozzle since the nozzle is relatively thick in comparison with the pipe.

Information about the structural damage produced by rapid changes in salt temperature is needed for the design of a MSBR. Consequently, the thermal stresses were computed after five different step changes in salt temperature. The step changes were:

# Downward

# Upward

1300-1200°F

1300-1400°F

1300 - 1100°F

1300 - 1600°F

1300 - 1800°F

It was assumed that these transients would not last longer than 10 seconds, since measures could be taken in that amount of time to bring the salt temperature back to normal. The time at which the highest surface and discontinuity stresses would occur was determined by a number of stress computations at different time points for the step change $1300 - 1600^{\circ}\mathrm{F}$ . From the results of these computations at 1, 3, 5, 7, and 9 seconds, it was learned that the highest surface stresses in the pipe occur at about 1 second, and in the nozzle wall they occur at about 9 seconds. The highest discontinuity stresses occur at about 9 seconds.

Since the temperature distributions were similar for all step changes, and since the differences between the stresses produced at 1 and 3 seconds and at 7 and 9 seconds were not large, computations were carried out only at 1 and 9 seconds for the remaining step changes.

With the results obtained from the stress computations, estimates were made of the number of cycles to failure for each condition. A judgement was also made regarding the likelihood of gross cyclic yielding at the intersection between the pipe and the nozzle.

# 2. DESCRIPTION OF CONFIGURATION AND FINITE ELEMENT IDEALIZATION

# 2.1. Configuration

The outlet nozzles are attached to a cylindrical vessel about 22 ft in diameter. The diameter of the outlet nozzles at the connection is 23 in. (Fig. 1). Most of the salt flows directly from the inlet through the core to the outlet nozzles, but some salt from the inlet flows through the gap between the cylindrical wall and the reflector (see Fig. 2).

Since the highest stresses expected are due to thermal loading, the nozzles were considered to be attached to a flat plate rather than to a cylindrical shell. With this simplification it was possible to consider an axisymmetric problem for the thermal loading. Since the vessel diameter to nozzle diameter ratio is about 12:1, the results were expected to be reasonably accurate.

The configuration, as shown in Fig. 3, was extended as far as possible in order to approximate the real situation. The flat plate was taken sufficiently large for the degree of restraint against thermal expansion to closely approximate that of the cylindrical wall. The criterion for the length of the connected pipe was that the discontinuity stresses should be damped out to $10\%$ at the end of the pipe.

# 2.2. Finite Element Mesh

The configuration shown in Fig. 3 was divided into a number of triangular ring elements. A fine mesh was taken in regions where high stresses were expected. Although for the calculation of the temperature distribution the mesh in some regions was finer than necessary, the same mesh was used as for the stress analysis.

Plots and subplots of the mesh are given in Figs. 4 through 8.

# 3. TEMPERATURE DISTRIBUTION CALCULATIONS

The determination of the temperature distribution was carried out by a finite element computer program. The program calculates the temperature of the nodal points situated at the vertices of the elements into which the body has been divided. The temperature of the centroid of an element is obtained by taking the average of the temperatures of the nodal points. The difference of the centroid temperature and a reference temperature is multiplied by the coefficient of thermal expansion, and the resulting numbers are the input data for the SAFE-PCRS stress analysis program.

The following simplifications were made for these calculations:

1. The problem is axisymmetric.   
2. Under normal conditions, the salt temperature is at $1300^{\circ}\mathrm{F}$ .   
3. The temperature of the salt in the gap between the wall and the reflector does not change.   
4. Except along boundaries where the configuration is in contact with the salt, it was assumed to be insulated.   
5. The material properties are temperature independent.

The material properties used are:

Conductivity coefficient: 12.7 Btu/hr-ft-F

Heat capacity: 75.8 Btu-ft³-F

The film coefficients are:

In the nozzle: 1600 Btu/hr- ft2-F

In the gap: 150 Btu/hr- ft2-F

The heat source strengths due to gamma radiation are:

Perpendicular to nozzle wall: 27.4 exp $(-0.818x)$ Btu/hr-in.3

Perpendicular to vessel wall: 30.2 exp $(-0.818x)$ Btu/hr-in. $^3$ ,

where $x$ is the distance, in inches, from the wall. Although the intensity of the gamma radiation changes during a transient, this effect was not taken into account, since the time considered was relatively short.

The steady-state temperature distribution was first calculated because it was not uniform due to the internal heat generation.

# 4.1. General Remarks

The stress computations were carried out by a stress analysis finite element computer program which determines the elastic stresses in an axisymmetric body. Where the value of the "stress" exceeds the yield strength, the results from these computations must be interpreted as strain times Young's modulus. Further discussion will be in terms of stress, since the fatigue curves and Section III of the ASME Boiler and Pressure Vessel Code are based on these elastically calculated stresses.

As already mentioned, in the first 10 seconds after the step change in the salt temperature, high local surface stresses and high bending stresses will occur. The surface stresses are high in the pipe and the nozzle wall, while the bending stresses are dominant in the intersection between the pipe and the nozzle. The stresses in these regions develop as follows:

1. The Pipe. This rather thin and flexible part of the structure changes rapidly in temperature. The highest surface stresses occur here in the first seconds after the step change. These stresses quickly decrease because of the dissipation of heat.   
2. The Nozzle Wall. This is a relatively thick and stiff part of the structure and thus does not change as rapidly in temperature as does the pipe. At 9 seconds after the step change, a region only 0.5 in. deep is at a significantly different temperature from that in the steady-state condition. The highest surface stresses occur at this time.   
3. The Intersection. Due to the difference in thermal expansion between the pipe and the nozzle wall, high bending stresses occur here. These stresses are classified as discontinuity stresses and can cause cyclic yielding. The stresses produced by the pressure loading are also of interest here.

# 4.2. Evaluation of Stresses

The stresses obtained by the finite element calculations were $\sigma_{r}$ , $\sigma_{z}$ , $\sigma_{\theta}$ , $\sigma_{rz}$ , $\sigma_{\min}$ , and $\sigma_{\max}$ in each element. These stresses are assumed

to be constant within each element. Especially where steep thermal gradients occur, the actual stresses vary significantly across an element and the type of element (constant stress) which was used will not give very accurate results unless a very fine mesh is employed. Higher order elements or a finer mesh near the inside surface of the nozzle would improve the results. For practical reasons these solutions were not applied. According to Zienkiewicz (page 35, Ref. 4) the calculated stresses should be assigned to the centroids of the elements.

For a section consisting of a row of elements, it is then possible to plot the stress components at the centroids against the radius of these centroids. The curve through these plotted points then gives a reasonable approximation of the stress distribution through the wall in that section.

An approximation expression given by $\text{Manson}^5$ enables us to check the highest surface stress in the pipe and the nozzle wall. This expression, which takes the Biot number into account, has the form

$$
\sigma_ {s} = \frac {E O \Delta \theta}{1 - v} \left[ \frac {1}{1 . 3 5 + \frac {3 . 2 5}{B} - 0 . 5 e ^ {- 1 6 / B}} \right],
$$

and gives the maximum surface stress due to a step change in fluid temperature on one side of a thin restrained flat plate. This case is essentially the same as a thin, infinitely long, cylindrical shell. Generally, there was good agreement when the stresses in the steady-state condition at the surface were taken into account.

For the evaluation of the stresses it was necessary to use a strength theory since a triaxial stress condition existed. Because of its accepted use in Section III of the ASME Code, the maximum shear theory was used. The stress intensity was thus determined by taking the largest algebraic difference between any of the two principal stresses at a point. Since the thickness of the pipe and the nozzle wall was small in comparison with the diameter of the nozzle, $\sigma_{r}$ was expected to be small. From the results of the stress computations it was found that $\sigma_{r}$ was small throughout the wall. Since $\sigma_{r}$ is equal to zero at the surface, it was set equal to zero everywhere. With this simplification the stress intensity was just the highest stress component in absolute value.

The high local surface stresses were considered to be peak stresses which could damage the surface by fatigue cracking. For the evaluation of these stresses the amplitude of the stress fluctuation must be determined. This amplitude was found by taking the algebraic difference between the highest occurring surface stress in the structure and the surface stress in the steady-state condition for the same spot. The amplitude of the stress fluctuation was then half the difference of the stresses. The mean stress and hold-time effects were not taken into account because they were of no significance for the cases considered. The number of cycles to failure for each step change was determined from the fatigue curves in Fig. 9.

The evaluation of the bending stresses in the intersection between the pipe and the nozzle was more complicated. In addition to the thermal loading, the pressure loading should be taken into account. The internal pressure in the nozzle was, however, low (14 psig), and hence the effect of this loading was not expected to be significant. In order to determine the order of magnitude of the stresses produced by the pressure loading, a simplified calculation was carried out. For this calculation it was assumed that the pressure in the pipe was 30 psig and that the radial stress at the edge of the plate was equal to the circumferential stress in the vessel wall for the same internal pressure. A higher pressure than 14 psig was taken since no end plate (causing an axial membrane stress in the nozzle) was added to the configuration. The end plate was neglected since the relatively thin flat plate behaves differently from a cylindrical shell. It was found, from this calculation, that the stress intensity in nearly the entire intersection was lower than 1 ksi. The error in the determination of the thermal stresses was several times larger than this, and hence the stresses produced by the pressure loading were neglected.

In order to estimate whether or not serious cyclic yielding would occur in the intersection, it was determined over what percentage of the section a higher stress intensity than $2S_y$ occurs, where $S_y$ is the yield strength and is given in Fig. 10 as a function of temperature.

# 5. RESULTS OF STRESS COMPUTATIONS

In this chapter the results of the stress computations for different conditions are presented. From these results estimates of the number of cycles to failure have been made, and also it has been determined, for each condition, whether or not gross cyclic yielding might occur.

The temperature distributions presented have been obtained by plotting the nodal point values against the distance from the centerline. The procedure by which the stress distributions were obtained was described in Chapter 4. The stress component presented for each section is the highest component occurring there, and since $\sigma_{\mathbf{r}}$ has been set equal to zero this stress component is also the stress intensity.

# 5.1. Steady-State Condition

The temperature distributions through the wall at sections A-A, B-B, C-C, D-D, E-E, and F-F are presented in Figs. 11 through 16, respectively. The stress distributions through the wall in the first five sections are shown in Figs. 17 through 21.

These stress distributions are necessary to determine the amplitude of the stress fluctuation for the other conditions.

# 5.2. Step Change 1300 - 1400°F

The temperature distributions through the wall at sections A-A, B-B, C-C, D-D, and E-E are presented in Figs. 22 through 26, respectively. The stress distributions in the same sections are shown in Figs. 27 through 31.

The surface stress that gives the highest amplitude of stress fluctuation occurs in section D-D, and at this spot we have:

The circumferential stress: -21 ksi

The surface temperature: 1380°F

The circumferential stress in the 7 ksi

steady-state condition:

The amplitude of the stress fluctuation: 14 ksi

From the fatigue curves in Fig. 9 we find that fatigue cracking is unlikely for this condition.

For section B-B, where the highest discontinuity stresses occur, we have at 9 seconds after the step change:

The average temperature: 1350°F

The yield strength at $1350^{\circ}\mathrm{F}$ : 20 ksi

From the stress distribution in Fig. 28 we find that no yielding will occur.

# 5.3. Step Change 1300 - 1600°F

The temperature distributions through the wall in sections A-A, B-B, C-C, D-D, and E-E are presented in Figs. 32 through 36, respectively. The stress distributions in the same sections are shown in Figs. 37 through 41.

The surface stress that gives the highest amplitude of the stress fluctuation occurs in section D-D, and at this spot we have:

The circumferential stress: -70 ksi

The surface temperature: 1540°F

The circumferential stress in the 7 ksi

steady-state condition:

The amplitude of the stress fluctuation: 38.5 ksi

From the fatigue curves in Fig. 9 we find that the number of cycles to failure might be as low as 90.

For section B-B, where the highest discontinuity stresses occur, we have, at 9 seconds after the step change:

The average temperature: 1450°F

The yield strength at $1450^{\circ}\mathrm{F}$ 20 ksi

From the stress distribution in Fig. 38 we find that the stress intensity is higher than $2S_{y}$ in about $30\%$ of this section. It can thus be suspected that gross cyclic yielding might occur in this section.

# 5.4. Step Change 1300 - 1800°F

The temperature distributions through the wall in sections A-A, B-B, C-C, D-D, and E-E are presented in Figs. 42 through 46, respectively. The stress distributions in the same sections are shown in Figs. 47 through 51.

The surface stress that gives the highest amplitude of the stress fluctuation occurs in section D-D, and at this spot we have:

The circumferential stress: -118 ksi

The surface temperature: 1700°F

The circumferential stress in the 7 ksi

steady-state condition:

The amplitude of the stress fluctuation: 62.5 ksi

There are presently no fatigue data available for $1700^{\circ}\mathrm{F}$ , but since $\mathbf{S}_{\mathrm{alt}}$ is very high it is estimated that cracking might occur after only one or two cycles.

For section B-B, where the highest discontinuity stresses occur, we have, at 9 seconds after the step change:

The average temperature: 1550°F

The yield strength at $1550^{\circ}\mathrm{F}$ 20 ksi

From the stress distribution in Fig. 48 we find that the stress intensity is higher than $2S_y$ in about $55\%$ of this section. It can be concluded that gross cyclic yielding will occur for this condition.

# 5.5. Step Change 1300 - 1200°F

The temperature distributions through the wall in sections A-A, B-B, C-C, D-D, and E-E are presented in Figs. 52 through 56, respectively. The stress distributions in the same sections are shown in Figs. 57 through 61.

The surface stress that gives the highest amplitude of the stress fluctuation occurs in section D-D, and at this spot we have:

The circumferential stress: 34 ksi

The surface temperature: 1225°F

The circumferential stress in the 7 ksi

steady-state condition:

The amplitude of the stress fluctuation: 13.5 ksi

From the fatigue curves in Fig. 9 we find that fatigue cracking is unlikely for this condition.

For section B-B, where the highest discontinuity stresses occur, we have, at 9 seconds after the step change:

The average temperature: 1250°F

The yield strength at $1250^{\circ}\mathrm{F}$ 20 ksi

From the stress distribution in Fig. 58 we find that no yielding will occur at the intersection.

# 5.6. Step Change 1300 - 1100°F

The temperature distribution through the wall in sections A-A, B-B, C-C, D-D, and E-E are presented in Figs. 62 through 66, respectively. The stress distributions in the same sections are shown in Figs. 67 through 71.

The surface stress that gives the highest amplitude of the stress fluctuation occurs in section D-D, and at this spot we have:

The circumferential stress: 58 ksi

The surface temperature: 1145°F

The circumferential stress in the 7 ksi

steady-state condition: The amplitude of the stress fluctuation: 25.5 ksi

From the fatigue curves in Fig. 9 we find that the number of cycles to failure might be as low as $2 \times 10^{5}$ .

For section B-B, where the highest discontinuity stresses occur, we have, at 9 seconds after the step change:

The average temperature: 1220°F

The yield strength at $1220^{\circ}\mathrm{F}$ 20 ksi

From the stress distribution in Fig. 68 we find that the stress intensity is higher than $2S_y$ in about $10\%$ of this section. It can be concluded that no gross cyclic yielding will occur for this condition.

# 6. CONCLUSIONS

From the results of the stress calculations it was found that:

1. A step change of $100^{\circ}\mathrm{F}$ in the salt temperature upward or downward will not cause any damage to the configuration.   
2. The step change $1300 - 1100^{\circ}\mathrm{F}$ might possibly cause fatigue cracking after a large number of cycles, but no gross cyclic yielding would occur.   
3. A step change from $1300 - 1600^{\circ}\mathrm{F}$ would cause fatigue cracking after about 90 cycles and gross cyclic yielding might occur in the intersection between the pipe and the nozzle.   
4. The step change $1300 - 1800^{\circ}\mathrm{F}$ is likely to cause cracks after a very few cycles and gross cyclic yielding will occur in the intersection between the nozzle and the pipe.

# 7. REFERENCES

1. J. L. Spoormaker, "Application of the Finite Element Method to the Computation of Temperature Distributions in Axisymmetric Bodies," USAEC Report ORNL-TM-2894, Oak Ridge National Laboratory (to be published).   
2. Y. R. Rashid, "Finite Element Analysis of Axisymmetric Composite Structures," USAEC Report GA-6303, General Atomic, June 4, 1965.   
3. D. C. Cornell, "SAFE-PCRS - A Computer Program for the Stress Analysis of Composite Bodies of Revolution, Input Instructions," USAEC Report GA-6588, General Atomic, August 1, 1965.   
4. O. C. Zienkiewicz, The Finite Element Method in Structural and Continuum Mechanics, McGraw-Hill, 1967.   
5. D. J. Lewis, E. J. Chubb, and H. A. Money, "Factors Affecting Thermal Stress in a Power Plant," International Conference on Thermal Stresses and Thermal Fatigue, Berkeley Nuclear Laboratories, September 23-26, 1969.

# 8. ACKNOWLEDGEMENTS

The author wishes to express his appreciation to R. B. Briggs of the Director's Division for his overall direction and guidance. Members of the Reactor Division Design Department, including J. R. McWherter, C. W. Collins, W. K. Furlong, and H. A. McLain, supplied the necessary MSBR information and made helpful suggestions. Finally, the author acknowledges the help of J. M. Corum of the Reactor Division Applied Mechanics Section in performing the stress analyses and evaluating the results, and of W. G. Dodge of the Applied Mechanics Section in writing the heat conduction computer program.

# 9. FIGURES

ORNL-DWG 70-2354

![](images/5bf4f446bd466bb2463eca4fdfdccb030e029c774d0a0bba07bd8002bdcd637d.jpg)  
Fig. 1. MSBR Reactor Vessel Flow Schematic.

ORNL-DWG 70-2355

![](images/2e871f70b7e213f7bd1f49fb2255f22b58590b41e5b0a5124470797a6344c1fc.jpg)  
Fig. 2. MSBR Reactor Vessel Simplified Outlet Configuration.

ORNL-DWG 70-2356

![](images/7c1493fa24078d066c23d9befa4dd96fa48b99444a1143ab8e14047bf5f8e982.jpg)  
Fig. 3. MSBR Reactor Vessel Simplified Outlet Nozzle Detail.

![](images/2e16ca600c139a9640eb8d9c14c81ad355b1833544dda650dd2553b151e80259.jpg)  
MSBR OUTLET NOZZLE (SIMPLIFIED VERSION   
Fig. 4. Plot of the Outline of the Configuration.

![](images/72f2c41e9a9ad1def90e6a094952f69f288a999d17041b6f0d86a0fe716ec234.jpg)  
MSBR OUTLET NOZZLE (SIMPLIFIED VERSION)   
Fig. 5. Subplot of the Element Idealization (Pipe Region).

![](images/f9f9daaf7a6b351383fa236b4108d0c546657b1862b7922030c6cca62c5a1eed.jpg)  
MSER OUTLET NOZZLE (SIMPLIFIED VERSION)   
Fig. 6. Subplot of the Element Idealization (Intersection Region).

![](images/f22fcc5dbe29375b7a775e2fa4a95b0938aeff87fc418fb65a109c18315072ab.jpg)  
MSER OUTLET NOZZLE (SIMPLIFIED VERSION)   
Fig. 7. Subplot of the Element Idealization (Nozzle Wall Region).

![](images/84714dfff32f02c4eb5be504faff9923c0ed8bcf14566d3e28fe8ce7e4574a4b.jpg)  
Fig. 8. Subplot of the Element Idealization (Flat Plate).

ORNL-DWG 70-3301

![](images/af03654ca2ad04d46c300f94b5085c1426cd2e4fa3a1580cff6bde9b46604448.jpg)  
Fig. 9. Design Fatigue Strength, $S_{a}$ , for Ni-Mo-Cr Alloy.

![](images/22204a123679ab4fd5b31de0fea2285fa83b6cc486e4ceea2330a6cb921f49db.jpg)  
Various Criteria for the Determination of the Design Stresses for INOR-8.   
Fig. 10. Various Criteria for the Determination of the Design Stresses for INOR-8.

![](images/32bcbd49f220aa500c0c48bcd5d59c46008d25b75d6b9d7ffe3314db4018cf69.jpg)  
Fig. 11. Temperature Distribution Across Section A-A in the Steady-State Condition.

![](images/3164cc52b03cfd41612fc1a51b78832f295479fccfd0b8e4cd27e63d85fa0e86.jpg)  
Fig. 12. Temperature Distribution Across Section B-B in the Steady-State Condition.

![](images/1984ba366c2fae16e0b3f912c7f6ce2d32917e102d5f4937de045eccbd41e55a.jpg)  
Fig. 13. Temperature Distribution Across Section C-C in the Steady-State Condition.

ORNL-DWG 70-2366

![](images/8b49f0e6c3904d84c906848d1bfc7c24cd74ab6af915583c5431b00bb0369c74.jpg)  
Fig. 14. Temperature Distribution Across Section D-D in the Steady-State Condition.

![](images/5570489d2068ac2cdbadd1dd11563ae1dac213545fbbbe1130c768d8d35e065a.jpg)  
Fig. 15. Temperature Distribution Across Section E-E in the Steady-State Condition.

![](images/e89a69c8b99da463fde7ea6abefcebc1a4938462cd30b6ff7a58a4dec6f1c5ca.jpg)  
Fig. 16. Temperature Distribution Across Section F-F in the Steady-State Condition.

ORNL-DWG 70-2369

![](images/ecbdff9b639b42e1880b28242a4f807c0d4f43b8d645b94f6446ab2fd74f45d2.jpg)  
Fig. 17. Stress Distribution Across Section A-A in the Steady-State Condition.

![](images/50b8e987d534f6fe52234d3ed70ab15c53909f688bd5191704176715d0191d5e.jpg)  
Fig. 18. Stress Distribution Across Section B-B in the Steady-State Condition.

![](images/c0bd9078b828dc2b6e516c9dc0604c8f2bddb8dc708768daae4ff07ecede20ae.jpg)  
Fig. 19. Stress Distribution Across Section C-C in the Steady-State Condition.

![](images/539aa35a8b517ab4c2b00d5220cd494f674278e0378b9189b60b8ebe73904970.jpg)  
Fig. 20. Stress Distribution Across Section D-D in the Steady-State Condition.

![](images/5c1912f68885f018c21d8ee8e92a7bf339f6d16086f352e8e7fec57fcef6dbef.jpg)  
Fig. 21. Stress Distribution Across Section E-E in the Steady-State Condition.

![](images/10292a515cfb457f3faedb931eda97b07f7a2a0cb525344c3404e04728b5b0d4.jpg)  
Fig. 22. Temperature Distribution Across Section A-A After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

![](images/41a64f9a2531b2ed72f4a819ed2c66101ba219137aaa5222eed9c474c3539119.jpg)  
Fig. 23. Temperature Distribution Across Section B-B After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

![](images/137b89db7a11147085e665ab1c9c12ae4d1762cffbcd38a0f8e3f0f54e6e05b8.jpg)  
Fig. 24. Temperature Distribution Across Section C-C After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2377

![](images/1f0d2bdccb86e3758c5f3238d994ae64e9b514f1f8ecba55dd8290e319638618.jpg)  
Fig. 25. Temperature Distribution Across Section D-D After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2378

![](images/4a75b13ddbaea62f01c166c88ebafcb4ce96a21bd1222d428a12e81ebae9c720.jpg)  
Fig. 26. Temperature Distribution Across Section E-E After the Step Change $1300 - 1400^{\circ}\mathbf{F}$ .

ORNL-DWG 70-2379

CIRCUMFERENTIAL STRESS DISTRIBUTION THROUGH THE WALL IN SECTION A-A

![](images/e93abd484ffc3be0c801cbb4b2b8b5e952b2df1db0afd471400fe9215c6335d1.jpg)  
Fig. 27. Stress Distribution Across Section A-A After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2380

![](images/48ddb36bc213bc53de49c5f362452a92c18a8eb3a10165cc3ff28634ce9b6b32.jpg)  
Fig. 28. Stress Distribution Across Section B-B After the Step Change $1300 - 1400^{\circ}\mathbf{F}$ .

![](images/e5647b12fbaa00a02ed983dcdb7f8e009afc9d270e36b6caa056d3bac2d98890.jpg)  
ORNL-DWG 70-2381   
Fig. 29. Stress Distribution Across Section C-C After the Sept Change $1300 - 1400^{\circ}\mathrm{F}$ .

![](images/e221843d0d833d75760cf9ab7724e7df2998d7b2da56177ef226f5bedd46e540.jpg)  
Fig. 30. Stress Distribution Across Section D-D After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2383

![](images/041f6dbb4abaafc91d359dea6b7bfc96f110dde3eed3e1fa66184d5fbf0cf92e.jpg)  
Fig. 31. Stress Distribution Across Section E-E After the Step Change $1300 - 1400^{\circ}\mathrm{F}$ .

![](images/231023504a49150944ded47cf163705c6b41a0523402632fdd03c6bb8b69d17c.jpg)  
Fig. 32. Temperature Distribution Across Section A-A After the Step Change $1300 - 1600^{\circ}\mathbf{F}$ .

ORNL-DWG 70-2385

![](images/047c45357d0aef87d83c454b80fb8a6aa62176074bbc0a3f8dabd00881c6bf63.jpg)  
Fig. 33. Temperature Distribution Across Section B-B After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

![](images/6df1b13563069b5e3fc2b65ceb081cdb388e73a1b8042671e67e567fba489604.jpg)  
Fig. 34. Temperature Distribution Across Section C-C After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2387

![](images/b608f3fb33f6ce79c1a815de9905f0dcb8f3e4a45efdef9f0557ccce9ec43827.jpg)  
Fig. 35. Temperature Distribution Across Section D-D After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

![](images/9532843569621e1f6ae319ff7a9ccb1aedeaf3c1c0175cb5b3f4861e37113a1e.jpg)  
Fig. 36. Temperature Distribution Across Section E-E After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

![](images/5498e9ac72ab1135f5d1a542338748635130ef698113b42f77fc07208e11e081.jpg)  
Fig. 37. Stress Distribution Across Section A-A After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

![](images/bc80cc41c52bd75e8b653c1679c59e455f96884ef6dde5cbd635110db328fe81.jpg)  
Fig. 38. Stress Distribution Across Section B-B After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

![](images/c157ca8046fb3f0dcf5f27ce2a6f1183a20f059e13b9797d0f00aea53baa9170.jpg)  
Fig. 39. Stress Distribution Across Section C-C After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

# Circumferential Stress Distribution

# Through the Wall in Section D-D

![](images/3165b323284453a52d3d4fd83e6ee6dbaf43d0d20bfe0a99e4c59be9d426e824.jpg)  
Fig. 40. Stress Distribution Across Section D-D After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

![](images/8ef10e02917d7e0d24b4b24c3a6b5f7bfa58227c358ca786f8c1de3343fda229.jpg)  
Fig. 41. Stress Distribution Across Section E-E After the Step Change $1300 - 1600^{\circ}\mathrm{F}$ .

![](images/646e4429e2827ffd2e5e2d2ff42d670c55c434ebf191387a733747ad13dfbc11.jpg)  
Fig. 42. Temperature Distribution Across Section A-A After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

![](images/cc872b28a51d3d58a5e0a82a3f958bcc7a006144109004a8f531cbb60f44dfcf.jpg)  
Fig. 43. Temperature Distribution Across Section B-B After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

![](images/891cea720234a3a82b00b3e1d9362a43698a693016048dd70de1fa8110aa7afe.jpg)  
Fig. 44. Temperature Distribution Across Section C-C After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

![](images/0911c115f7074dbbb0f3616b50042683a7f63e35c5517d272a61daa8faf4917f.jpg)  
Fig. 45. Temperature Distribution Across Section D-D After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

![](images/b5a6fc57bce8b773dd9fbf282a3a3edf50ac95d79f97af3413e9eef49606e923.jpg)  
Fig. 46. Temperature Distribution Across Section E-E After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

CIRCUMFERENTIAL STRESS DISTRIBUTION THROUGH THE WALL IN SECTION A-A

![](images/ff6bcaafedebc5bc4c74c6174559cd85145c0f1617192c01a3c3d39f7f81202c.jpg)  
Fig. 47. Stress Distribution Across Section A-A After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

![](images/93eebd340531bf1342abbb5cd01135fdc177ac91c25c0dfd68a6a2b07057c595.jpg)  
Fig. 48. Stress Distribution Across Section B-B After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2401

![](images/84ab95bdbbd66eed7278873f25110550298a02f611c36ed2555c8e2cde6eb58c.jpg)  
Fig. 49. Stress Distribution Across Section C-C After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

![](images/77531042b3b1dc1f10e046ecae344cd6183892a0752189fbe631953f6171ec85.jpg)  
Fig. 50. Stress Distribution Across Section D-D After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

![](images/76ccdb2827367e312a9534d940dbf3f268000f5040d8fe28ea058c5dde99ba4c.jpg)  
Fig. 51. Stress Distribution Across Section E-E After the Step Change $1300 - 1800^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2404

![](images/456af8190f9254da91186e603ee102699787860a3bb3b7f2cdb68e765ef1dd25.jpg)  
Fig. 52. Temperature Distribution Across Section A-A After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

![](images/f49b34bc861419853b842d268e5c4a3196aeaaa34cee22b45226ebb7cccc21a9.jpg)  
Fig. 53. Temperature Distribution Across Section B-B After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

![](images/647fc171c374aab140066563094dc2a40bb0bcafd0272769a6cdc8f5425574f6.jpg)  
Fig. 54. Temperature Distribution Across Section C-C After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2407

![](images/74aafbe9abc16c5b44233eac9dce92150b06ec5236eee9f067e7808b47b0f5c1.jpg)  
Fig. 55. Temperature Distribution Across Section D-D After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

![](images/b44f08947b532f68ec9bd811cdde3f79fe9fb4be9b372d27dbbc9e7657e89e4f.jpg)  
Fig. 56. Temperature Distribution Across Section E-E After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2409

![](images/566ed164c3a50cdf22b33d0a7fb43dbf3dc32007097451de32b283ff23f91dfa.jpg)  
Fig. 57. Stress Distribution Across Section A-A After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2410

![](images/1519051cad321e0bec1c029cbd092f76c73a519946ab6049df535ec1c8e1a350.jpg)  
Fig. 58. Stress Distribution Across Section B-B After the Step Change $1300 - 1200^{\circ}\mathbf{F}$ .

![](images/29405166e3af2565ee3709e022096b5c9751f3964c884ac3a3bd8fdbc46aaf12.jpg)  
ORNL-DWG 70-2411   
Fig. 59. Stress Distribution Across Section C-C After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2412

![](images/fa7f21a299b66f4132e082ce41752456f8fe4d0453862b521622857d92761221.jpg)  
Fig. 60. Stress Distribution Across Section D-D After the Step Change $1300 - 1200^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2413

![](images/8a37833d06ed4a72fece7eaddfdf29623c79c2becf6fdcbe035b37d712d31e04.jpg)  
Fig. 61. Stress Distribution Across Section E-E After the Step Change $1300 - 1200^{\circ}\mathbf{F}$ .

![](images/fc6473795e68a036c8f795f8bd37d87ae8aae09b041a926ec9a402918b77de01.jpg)  
Fig. 62. Temperature Distribution Across Section A-A After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

![](images/e9f83f5e804e3fa33ddc1ab35f8edebf23a30801da231f152e275d74deacd6b5.jpg)  
Fig. 63. Temperature Distribution Across Section B-B After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

![](images/ec1d106d881a859eab1ad7d0a3286a8342dd0f2a876e33e2d64726515481d305.jpg)  
Fig. 64. Temperature Distribution Across Section C-C After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2417

![](images/ea72112984f074e3a9c793555643659452bb72324af82e01d2ba66bf55f33912.jpg)  
Fig. 65. Temperature Distribution Across Section D-D After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

![](images/8afcb1baa297a4dcb85f19373b965b62a8a5acb7bbf14e6eb587e218c43207ae.jpg)  
Fig. 66. Temperature Distribution Across Section E-E After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

![](images/2d0b372afc9d2af9b01b2c7cb2530c6cb80fc9fc8d8f6d12a79337b658159c38.jpg)  
Fig. 67. Stress Distribution Across Section A-A After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2420

![](images/893391d7a3c72850f6dd702ffaf072eb69e946a6e1cdb661acedd93f913e32ed.jpg)  
Fig. 68. Stress Distribution Across Section B-B After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

![](images/045949d92dcb2d059ba18613b867628f2885a9724698502ddd8fcc22f5e0f7e8.jpg)  
Fig. 69. Stress Distribution Across Section C-C After the Step Change $1300 - 1100^{\circ}\mathbf{F}$ .

![](images/ac0905d2da407cf42321892fd4138282f7e224e5a5490440b9a4354b4daafb25.jpg)  
Fig. 70. Stress Distribution Across Section D-D After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .

ORNL-DWG 70-2423

![](images/cf236844fed886f91f82e5a8a12a136f19e8d613af1dd1d4b60284ac445ab529.jpg)  
Fig. 71. Stress Distribution Across Section E-E After the Step Change $1300 - 1100^{\circ}\mathrm{F}$ .