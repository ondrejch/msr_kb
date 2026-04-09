DATE: March 3, 1965

SUBJECT: Comparison of Calculations and Uncertainties in the Temperature Coefficients of Reactivity in the MSRE

TO: Distribution

FROM: B. E. Prince

# ABSTRACT

Several calculated values for the MSRE temperature coefficients of reactivity have been reported in different sources. These values are compared and their bases discussed in this memorandum. Calculations based on new experimental data for the temperature coefficient of expansion of the fuel salt are also included. Ranges of uncertainty in the current "best values" of temperature coefficients of reactivity and critical concentration are suggested, and the implication of these uncertainties in the zero power critical experiments are discussed. It is concluded that, with presently planned procedures, the expected uncertainties will not reduce reactor safety below that previously reported in the MSRE safety report.

# NOTICE

This document contains information of a preliminary nature and was prepared primarily for internal use at the Oak Ridge National Laboratory. It is subject to revision or correction and therefore does not represent a final report. The information is not to be abstracted, reprinted or otherwise given public dissemination without the approval of the ORNL patent branch, Legal and Information Control Department.

# INTRODUCTION

In the course of obtaining estimates of basic nuclear design parameters for the MSRE, several values have been reported for the critical concentration and temperature coefficients of reactivity. One should first note that these calculations have had an evolutionary aspect, that is, the more recent calculations are generally considered to be "better", either in terms of the physical model or the basic nuclear data used in calculating the reported characteristic. In the case of the critical concentration, the most recent computations have been reported in Ref. 1 along with a discussion of the origin of differences from previous calculations. In this memorandum we shall try to achieve some clarification of the second case, that of the temperature coefficients of reactivity.

# DISCUSSION

The earliest reported calculations of the temperature coefficients for the final MSRE core design were those of Nestor.2 As indicated in Table 1, two-group bare reactor theory was used, together with the specific assumptions:

1. The neutron temperature and the graphite temperature are identical.   
2. The effects of changes in reactor size are negligible.   
3. The Fermi age is a function only of the graphite density.   
4. The resonance escape probability, fast effect, and $\overline{\eta}$ for $U^{235}$ were independent of temperature.

The fuel salt analyzed by Nestor contained $\sim 0.3$ mol $\%$ $\mathrm{UF}_4$ , $93\%$ enriched in $\mathrm{U}^{235}$ , in a carrier salt composition of $70/24/5/1$ mol $\%$ LiF/ $\mathrm{BeF}_2/\mathrm{ZrF}_4/\mathrm{ThF}_4$ . This salt is designated as Fuel A. Subsequent to Nestor's work, it was decided not to include thorium in the first MSRE fuel salt mixture, and to use instead a salt composed of $\sim 0.2$ mol $\%$ $\mathrm{UF}_4$ , $93\%$ enriched in $\mathrm{U}^{235}$ , in a carrier salt of $67/29/4$ mol $\%$ LiF/ $\mathrm{BeF}_2/\mathrm{ZrF}_4$ . This salt is designated as Fuel B. New calculations of the temperature coefficients were required, and this time use was made of two-group perturbation theory to check the validity of the one-region approximation. $^3$ The remaining assumptions used in the earlier calculations were retained. These results are given in

Table 1. Comparison of MSRE Temperature Coefficients of Reactivity   

<table><tr><td rowspan="2">Case</td><td rowspan="2">Fuel Salt Composition</td><td colspan="2">Temperature Coefficients of Reactivity (Δk/k/°F) x 10+5)</td><td colspan="2">Temperature Coefficients of Expansion (Δρ/ρ/°F) x 10+5)</td><td rowspan="2">Computational Model</td><td rowspan="2">Refer-ence</td></tr><tr><td>Fuel</td><td>Graphite</td><td>Fuel</td><td>Graphite</td></tr><tr><td rowspan="3">1</td><td rowspan="3">A</td><td rowspan="3">-2.8</td><td rowspan="3">-6.0</td><td rowspan="3">-12.6</td><td rowspan="3">-0.4</td><td>Mult. const. (ke): Two group, bare reactor theory.</td><td rowspan="3">2</td></tr><tr><td>Slowing down spectrum: Determined by Fermi age in graphite.</td></tr><tr><td>Thermal spectrum: Maxwell-Boltzmann approximation.</td></tr><tr><td rowspan="2">2</td><td rowspan="2">B</td><td rowspan="2">-4.5</td><td rowspan="2">-7.3</td><td rowspan="2">-12.6</td><td rowspan="2">-0.4</td><td>ke: Two-group perturbation theory.</td><td rowspan="2">3</td></tr><tr><td>Slowing down and thermal spectrum same as case 1.</td></tr><tr><td>3</td><td>A</td><td>-3.0</td><td>-3.4</td><td>-11.8</td><td>-1.0</td><td>ke: Same as case 1.</td><td rowspan="3">6</td></tr><tr><td>4</td><td>B</td><td>-5.0</td><td>-4.9</td><td>-11.8</td><td>-1.0</td><td>Slowing down spectrum: GAM-1 program calculations.</td></tr><tr><td>5</td><td>C</td><td>-3.3</td><td>-3.7</td><td>-11.8</td><td>-1.0</td><td>Thermal spectrum: THERMOS program calculations.</td></tr><tr><td rowspan="3">6</td><td rowspan="3">C</td><td rowspan="3">-5.6</td><td rowspan="3">-4.0</td><td rowspan="3">-18.6</td><td rowspan="3">-1.0</td><td>ke: Same as case 1.</td><td rowspan="3">This memo-randum</td></tr><tr><td>Slowing down spectrum: GAM-2 program calculations.</td></tr><tr><td>Thermal spectrum: THERMOS calculations.</td></tr></table>

line 2 of Table 1. Together with the perturbation theory calculations, estimates based on a one-region homogeneous model were also made for fuel B. The resulting coefficients were found to compare within 5 to $10\%$ , indicating that the detailed description of the external regions of the core (downcomer, top and bottom heads, etc.) did not significantly influence the reactivity coefficients. Note, however, that the magnitude of the temperature coefficients differs from the earlier calculations primarily because of the change in fuel salt composition. With fuel B the reactor neutron spectrum is more thermalized and the effect of salt density changes on the leakage factors is proportionally larger.

A further request was made to examine the possibility of increasing the total uranium content of the salt to the range of $0.8 - 0.9\mathrm{mol}\% \mathrm{UF}_4$ ( $\sim 35\%$ enriched for criticality, designated fuel C). About this same time, two new computer programs were acquired by use of which detailed calculations of the slowing down and thermal spectra could be made. Specifically, the GAM-1 program is based on consistent P-1 theory for calculation of the slowing down spectrum in finite, homogeneous mixtures. The THERMOS program numerically solves the Boltzmann equation for the thermal spectrum in a one-dimensional lattice cell, and thus allows the temperature of the fuel salt and graphite to be independently varied. A minor complication in the GAM-1 calculation for the MSRE spectrum was that the then-available version of the cross section library did not include Li, Li, and F. The other advantages of the GAM-1 calculation were considered sufficient, however, to warrant simulating the slowing down effect of the lithium and fluorine by an equivalent amount of oxygen, which was included in the GAM-1 cross section library. With these programs available, it was decided to recalculate the temperature reactivity coefficients for all three fuels under consideration, and to further examine the validity of some of the assumptions underlying previous calculations. The results are summarized in lines 3, 4, and 5 of Table 1. The major difference in these results and previously reported values is in the graphite temperature coefficient. This difference arises primarily in the temperature dependence of the thermal spectrum. For the MSRE lattice, (a) the thermal spectrum is not determined by the graphite temperature (assumption 1, above) but depends

on the temperature of the fuel channel as well, and (b) the Maxwell-Boltzmann approximation predicts too large a change in the thermal diffusion length as the temperature is varied.

Other differences are also reflected in the values given in lines 3, 4, and 5 of Table 1. These include the modified estimate of the graphite expansion coefficient, based on an average of longitudinal and transverse expansions, and changes due to explicit treatment of the temperature dependence of resonance absorption (assumption 4, above). In general, these differences were smaller than that due to the spectrum effect discussed above.

Very recently, new experimental data has become available for the density and temperature coefficient of expansion of fuel salt C. $^{7}$ These new data indicate that the expansion coefficient is nearly $60\%$ larger in magnitude than assumed in the preceding calculations. The previous values had been based on estimated temperature variations in the molar volumes of the salt constituents. $^{8}$

Also subsequent to the last reported calculations, acquisition was made of the GAM-2 program, an improved version of GAM-l, described above. By means of this new program, the slowing down effects in lithium and fluorine could be treated explicitly. The program has already been used to revise estimates of critical concentration and control rod worth, $^{9}$ and a set of temperature coefficients of reactivity for fuel C was also recalculated based on the new density data and the GAM-2 program. These results are summarized in line 6 of Table 1. As may be expected, the new expansion coefficient causes a significant increase in the fuel temperature coefficient of reactivity. Also, the explicit treatment of the slowing down by lithium and fluorine, particularly the inelastic scattering of fluorine, has the effect of further thermalizing the reactor spectrum. Hence both fuel and graphite reactivity coefficients are increased.

Most of the changes summarized in Table 1 have had the effect of making the fuel, or prompt temperature coefficient of reactivity more negative. In turn, the changes appear to improve the safety and stability margins for reactor operation.[10] The question still remains, however, as to the absolute uncertainties in these parameters. A method is

presently being investigated by which the uncertainty in the basic library of nuclear cross section data and densities can be related to the uncertainties in the nuclear design parameters (critical concentration, etc.). The basic notion is that of relating the standard deviation in the calculated parameter to the standard deviations in the cross sections and densities. This method would indicate the sensitivity in the parameters to uncertainties in all basic data used in calculation, and would be useful in later evaluation of results from the reactor critical experiments. This is not complete at the date of this writing and could not be included. However, since the validity of most of the main assumptions in the computation have been checked, it appears reasonable to assign a confidence interval of $\pm 10\%$ to the critical concentration and $\pm 25\%$ to the temperature coefficients of reactivity. Because of the "slope-like" nature of the latter quantity, it is expected to be the more sensitive of the two to errors in data and computational methods.

For all of the conceivable incidents previously analyzed which could result in significant additions of reactivity,[11] only the so-called cold slug accident would lead to a more severe transient if the fuel temperature coefficient of reactivity were more negative. This incident is not expected to lead to dangerous or damaging conditions, and in addition, precaution will be taken not to start fuel circulation unless the control rods are inserted in the core. Thus, safe operation should be insured for all values of the fuel reactivity coefficients indicated in Table 1.

The procedures of the initial critical experiments will be designed<sup>12</sup> to allow greater uncertainty in the clean critical concentration than the $10\%$ margin suggested above. The initial addition of uranium to the salt in the drain tanks will be $\sim 65\%$ of that predicted for criticality at zero power with all rods withdrawn from the core. The second addition is anticipated to be that amount to bring the salt within $87\%$ of the critical mass. From this point on, the amount in each addition will be determined by inverse count rate measurements. Even if the minimum critical mass were exceeded, this would only mean that criticality would be achieved with the rods slightly inserted and would not require other special procedures.

The uncertainty in the temperature coefficients of reactivity has no effect on procedures in the zero power critical experiments. The coefficients will be measured along with the rod calibration experiments, and any large discrepancy between measured and calculated coefficients will be taken into consideration in the planning and operation of experiments at higher power levels.

# REFERENCES

1. "MSRP Semiann. Prog. Rep. Jan. 31, 1964," USAEC Report ORNL-3626, p. 53-54.   
2. "MSRP Semiann. Prog. Rep. Aug. 31, 1961," USAEC Report ORNL-3215, p. 83.   
3. B. E. Prince and J. R. Engel, "Temperature and Reactivity Coefficient Averaging in the MSRE," USAEC Report ORNL-TM-379, Oak Ridge National Laboratory, October 15, 1962.   
4. G. D. Joanou and J. S. Dudek, "GAM-I: A Consistent P-1 Multi-group Code for the Calculation of Fast Neutron Spectra and Multigroup Constants," USAEC Report GA-1850, General Atomic, June 28, 1961.   
5. H. C. Honeck, "THERMOS: A Thermalization Transport Theory Code for Reactor Lattice Calculations," USAEC Report BNL-5826, Brookhaven National Laboratory, September 1961.   
6. P. N. Haubenreich, et al., "MSRE Design and Operations Report - Part III, Nuclear Analysis," USAEC Report ORNL-TM-730, p. 37-47, Feb. 3, 1964.   
7. B. J. Sturm, Reactor Chemistry Division (report in preparation).   
8. S. Cantor, "Reactor Chem. Div. Ann. Prog. Rep. Jan. 31, 1962," USAEC Report ORNL-3262, p. 38.   
9. "MSRP Semiann. Prog. Rep. July 31, 1964," USAEC Report ORNL-3708, p. 95-96.   
10. S. J. Ball and T. W. Kerlin, 'MSRE Stability Analysis, USAEC Report ORNL-TM-1070 (in preparation).   
11. S. E. Beall, et al., "MSRE Design and Operations Report - Part IV, Reactor Safety Analysis Report," USAEC Report ORNL-TM-732, Oak Ridge National Laboratory, p. 196-231, August 1964.   
12. P. N. Haubenreich, private communication (part of summary of test program, in preparation).

# INTERNAL DISTRIBUTION

1. MSRP Director's Office Rm. 219, 9204-1

2. S.J.Ball

3. H. F. Bauman

4. S. E. Beall

5. L. L. Bennett

6. E. S. Bettis

7. F. F. Blankenship

8. S. Cantor

9. R.S. Carlsmith

10. R. D. Cheverton

ll. H.C.Claiborne

12. C. W. Craven, Jr.

13. J.G.Delene

14. J.R. Engel

15. T. B. Fowler

16. C.H.Gabbard

17. J. J. Geist

18. E.H.Gift

19. W. R. Grimes

20. R. H. Guymon

21. P. N. Haubenreich

22. A. Houtzeel

23. L. Jung

24. T. W. Berlin

25. H.G.MacPherson

26. W. B. McDonald

27. H.F.McDuffie

28. R. L. Moore

29. E. A. Nephew

30. R.C. Olson

31. A.M.Perry

32. P. H. Pitkanen

33. C. M. Podeweltz

34. C. A. Preskitt

35-39. B. E. Prince

40. M. Richardson

41. M. W. Rosenthal

42. D. Scott

43. M. J. Skinner

44. O. L. Smith

45. J.R.Tallackson

46. R.E.Thoma

47. W. E. Thomas

48. M. L. Tobias

49. M. E. Tasgaris

50. R. Van Winkle

51. D. R. Vondy

52. F. G. Welfare

53. J. V. Wilson

54. K. J. Yost

55-56. Central Research Library

57-58. Document Reference Section

59-60. Reactor Division Library

61-63. Laboratory Records

64. ORNL-RC

# EXTERNAL DISTRIBUTION

65. S. K. Breslauer, AEC, Washington

66-67. D. F. Cope, Reactor Division, AEC, ORO   
68. R.W.Garrison,AEC,Washington   
69. H. M. Roth, Division of Research and Development, AEC, ORO   
70. W. L. Smalley, Reactor Division, AEC, ORO   
71. M. J. Whitman, AEC, Washington   
72. J. B. Lingerfelt, AEC, ORO