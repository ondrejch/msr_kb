# CHAPTER 19

# REACTOR PHYSICS FOR LIQUID METAL REACTOR DESIGN*

The flexibility of liquid metal fuel systems is such that they range over several different reactor categories. Liquid metal reactors may be designed as fast, intermediate, or thermal systems, with either circulating or static fuel systems. The reactor core components consist of a fuel carrier such as molten bismuth or lead, and a moderator such as graphite or beryllium, if the neutrons within the reactor core are to be thermalized. If the fuel is stationary, a second fluid is required as the reactor coolant.

In the simplest system, a high-temperature liquid-metal solution or slurry would be pumped through an externally moderated reactor core. For such a reactor, the neutron physics problems would be similar to those of aqueous homogeneous systems. The chief difference would lie in the neutron spectrum, which would be higher because of weaker moderation and higher operating temperatures.

The liquid-metal system that has received the greatest emphasis to date is of the heterogeneous, circulating fuel type. This reactor, known as the Liquid Metal Fuel Reactor (LMFR), has as its fuel a dilute solution of enriched uranium in liquid bismuth, and graphite is used as both moderator and reflector. With $\mathrm{U}^{233}$ as the fuel and $\mathrm{Th}^{232}$ as the fertile material, the reactor can be designed as a thermal breeder. Consideration is restricted here to this reactor type but, wherever possible, information of a general nature is included.

# 19-1. LMFR PARAMETERS

19-1.1 Cross sections. Most of the cross sections required for neutron physics studies of the LMFR can be obtained from BNL-325. The following exceptions should be noted. The $2200\mathrm{m / sec}$ value of the absorption cross section of graphite is given as $3.2\pm 0.2\mathrm{mb}$ . The best experimental value however is $3.6\mathrm{mb}$ after correcting for the presence of such impurities as B, $\mathrm{X}_2$ , etc. Graphite of density 1.65 to $1.70\mathrm{g} / \mathrm{cm}^3$ is obtainable with an absorption cross section of about $4\mathrm{mb}$ , including impurities. Graphite of density $1.8\mathrm{g} / \mathrm{cm}^3$ or higher is becoming available, but the purity of this high-density graphite has not been well established.

The $2200\mathrm{m / sec}$ value of the absorption cross section of $\mathrm{Bi}^{209}$ is $32\pm 2\mathrm{mb}$ . Two isomeric states of $\mathrm{Bi}^{210}$ are formed, one of which decays by $\beta$ -emission with a half-life of 5 days into $\mathrm{Po}^{210}$ .

TABLE 19-1 PARAMETERS OF $\mathbf{B}\mathbf{I}^{209}$ RESONANCES   

<table><tr><td>E0(ev)</td><td>σ0Γ, barn-ev</td><td>Γ, ev</td></tr><tr><td>810</td><td>9400</td><td>5.8 ± 0.3</td></tr><tr><td>2370</td><td>7660</td><td>17 ± 1.5</td></tr></table>

Bismuth has prominent resonances at 810 ev and 2370 ev, largely due to scattering. Breit-Wigner parameters obtained by Bollinger et al. at Argonne National Laboratory are listed in Table 19-1. To determine neutron capture within these resonances, it is necessary to estimate the value of the level width, $\Gamma_{\gamma}$ . One method is to use the value of $0.5\mathrm{b}$ obtained by Langsdorf (ANL-4342) for the resonance integral, which implies that $\Gamma_{\gamma}$ is about $150\mathrm{mv}$ . An analysis of Bollinger's data indicates that a more likely value is about $50\mathrm{mv}$ .

High-energy cross sections of bismuth and lead are of secondary interest in well-moderated liquid-metal reactors, but would become of prime interest in fast- or intermediate-energy reactors. On the basis of the known levels and spin assignments for bismuth and lead, Oleksa of Brookhaven National Laboratory has calculated cross sections that are in good agreement with experimental data. The (n, p) and (n, $\alpha$ ) cross sections are negligible. The threshold for the (n, 2n) cross section in bismuth is high, 7.5 Mev. At 1.0 and 4.3 Mev the transport cross sections of bismuth are calculated as 4.3 b and 4.2 b, respectively. The capture cross section at 1 Mev is 3.4 mb.

Inelastic scattering in bismuth is important in considering fission-energy neutrons. The results of Oleksa's studies are presented in Table 19-2. The lowest levels in $\mathrm{Bi}^{209}$ occur at 0.9, 1.6, 3.35 Mev, respectively. At energies up to 2.6 MeV, Oleksa finds that the cross sections for scattering into the individual levels are in good agreement with calculations based on the Hauser-Feshbach model.

In a U-fueled liquid-metal system, the cross sections of the higher isotopes or uranium are of considerable importance in determining equilibrium concentrations of these isotopes and the time required to approach their equilibrium. These equilibrium conditions require study because of solubility limitations in a liquid-metal fuel reactor. The chain starts with either $\mathrm{U}^{235}$ or $\mathrm{U}^{233}$ , depending on whether a converter or breeder reactor is under consideration, and ends with $\mathrm{U}^{237}$ because of its short half-life. In addition, some $\mathrm{U}^{238}$ may be present in the fuel. Thermal cross sections are given in BNL-325.

Other absorption cross sections of importance to high-power, high-fuel-burnup reactors are those of the long-lived fission products and, in a $\mathrm{U}^{233}$ breeder, that of $\mathrm{Pa}^{233}$ . Despite a number of comprehensive studies of these effects, accurate values may not be known until such reactors have been in operation for some time. Fuel-processing studies for the LMFR, however, indicate that the poisoning effect can economically be maintained at a few percent.

Although the LMFR is a heterogeneous reactor, the fuel and moderator arrangements that have been proposed yield a core which is nearly homogeneous from the neutron physics viewpoint. The preferred core is an impermeable graphite structure perforated with holes of about 2 in. diameter for passage of the liquid-metal fuel. The moderator volume is about equal to that of the liquid metal, bismuth, which contains about $0.1\mathrm{w / o}$ enriched uranium. Actually, the size of the fuel channels could be considerably increased without seriously increasing the flux disadvantage factor and, hence, the critical mass of the reactor core.

19-1.2 Neutron age and diffusion length. The following formulas, appropriate for mixtures, have been used to obtain the diffusion area, $L^2$ , and neutron age, $\tau$ , of graphite-bismuth LMFR cores:

$$
L ^ {2} = \frac {1}{3} \Sigma_ {a} \Sigma_ {\mathrm {t r}}, \tag {19-1}
$$

$$
\tau = \frac {\tau_ {\mathrm {C}} (1 + R) ^ {2}}{\left[ 1 + \frac {(\xi \Sigma_ {\mathrm {s}}) _ {\mathrm {B i}}}{(\xi \Sigma_ {\mathrm {s}}) _ {\mathrm {C}}} R \right] \left[ 1 + \frac {(\Sigma_ {\mathrm {t r}}) _ {\mathrm {B i}}}{(\Sigma_ {\mathrm {t r}}) _ {\mathrm {C}}} R \right]}, \tag {19-2}
$$

where $\xi$ is the logarithmic energy decrement,

$\Sigma_{s}$ is the macroscopic scattering cross section,   
$\Sigma_{a}$ is the macroscopic absorption cross section,   
$\Sigma_{\mathrm{tr}}$ is the macroscopic transport cross section,

the subscripts Bi and C indicate the macroscopic cross section for the respective materials, and $R$ is the bismuth-to-graphite volume ratio.

19-1.3 Reactivity effects. A problem unique to circulating fuel reactors is the loss of delayed neutrons in the external circuit. Since the time spent by the delayed-neutron emitters outside the reactor core is generally greater than that spent within the core, a considerable fraction of the delayed neutrons may be wasted. In addition, since most of the delayed-neutron emitters are produced as gases, they may be carried off during degassing operations. For $\mathrm{U}^{233}$ , the delayed neutron fraction in thermal fission is only $0.24\%$ . Thus prompt critical may, in some cases, be as little as $0.1\%$ excess reactivity.

TABLE 19-2 INELASTIC SCATTERING CROSS SECTION OF BI   

<table><tr><td>E, Mev</td><td>σinBi, barns</td></tr><tr><td>0.9</td><td>0</td></tr><tr><td>1.0</td><td>0.1</td></tr><tr><td>1.5</td><td>0.4</td></tr><tr><td>2.0</td><td>0.7</td></tr><tr><td>3.0</td><td>1.4</td></tr><tr><td>4.0</td><td>2.0</td></tr><tr><td>5.0</td><td>2.4</td></tr><tr><td>6.0</td><td>2.6</td></tr><tr><td>7.0</td><td>2.6</td></tr><tr><td>8.0</td><td>2.5</td></tr><tr><td>10.0</td><td>1.5</td></tr></table>

Coupled with this problem is the fact that the prompt temperature coefficient (due to liquid metal expansion) in the LMFR system under consideration is of the order of $-5 \times 10^{-5} / {}^{\circ}\mathrm{C}$ . Thus, ignoring temperature overshoots, which are discussed later, the magnitude of rapid reactivity changes must be limited to avoid large metal temperature changes. The total temperature coefficient of the LMFR runs about $-1.5 \times 10^{-4} / {}^{\circ}\mathrm{C}$ , the delayed coefficient resulting primarily from increased neutron leakage due to the heating of the graphite structure. While the slow response of the graphite to power changes thus limits the size of the prompt temperature coefficient, it aids in stabilizing the system against small oscillations at high power output.

19-1.4 Breeding. The LMFR can be operated as a breeder on the $\mathrm{U}^{233}\mathrm{-Th}^{232}$ cycle. The possible breeding gain is not large, since the value of $\eta$ for $\mathrm{U}^{233}$ is about 2.3. The theoretical gain is at most 0.3, but a value of 0.10 is about the maximum possible in a practical system. In fact, optimization based on economic considerations would probably reduce the gain to zero in any power breeder built in the near future. The gain is reduced by competitive neutron capture in the core and blanket, and by neutron leakage from the blanket and from the ends of the reactor core. A problem not yet solved is that of a leakproof, weakly absorbing container that will separate the core and blanket. It is hoped that beryllium or an impermeable graphite will provide such a container for the LMFR. Croloy steel or tantalum containers about 1/4-in thick appear satisfactory

from the mechanical and metallurgical standpoint but effectively wipe out the potential breeding gain because of their absorption cross section.

A number of studies of the so-called immoderation principle have been carried out in an attempt to reduce the neutron losses to the container. By removing the bulk of the moderator from a small region on both sides of the container wall the thermal neutron losses can be greatly reduced. Several feasible mechanical designs embodying this principle have been worked out by the Babcock & Wilcox Company.

# 19-2. LMFR STATICS

19-2.1 Core. The standard LMFR is predominantly thermal, nearly homogeneous, and moderated by graphite. Thus age-diffusion theory is applicable, and therefore the following formula can be used for a critical system:

$$
k _ {\infty} e ^ {- \tau B ^ {2}} = 1 + L ^ {2} B ^ {2}, \tag {19-3}
$$

where $B^2$ is the buckling of the system, and

$$
k _ {\infty} = \eta f, \tag {19-4}
$$

where $\eta$ is the number of fast neutrons produced per thermal neutron captured in the fuel, and $f$ is the thermal utilization factor. The product of the fast fission effect, $\epsilon$ , and resonance escape probability, $p$ , is assumed equal to unity.

In view of the uncertainty in the value of $\Gamma_{\gamma}$ for bismuth, the validity of neglecting resonance capture is still uncertain, and Monte Carlo studies are planned at BNL to obtain lower limits for $p$ as a function of channel size and lattice pitch. For small channels, the homogeneous formula for $f$ is adequate, since consideration of self-shielding of the fuel reduces $f$ in a typical core by about $2\%$ .

Studies have yielded for buckling the typical values given in Table 19-3[1] for both $\mathrm{U}^{233}$ and $\mathrm{U}^{235}$ as the fuel in a graphite moderator at an average core temperature of $475^{\circ}\mathrm{C}$ .

19-2.2 Reflector. In order to apply the above results to reflected reactors, it is necessary to determine the reflector savings, which can be obtained from conventional two-group theory. This method could also be used to estimate the critical size of the reactor but, for small cores, two-group theory underestimates the size of graphite-moderated reactors.

Two-group results obtained for typical reflectors are given in Table 19-4 [1] for a cylindrical reactor system surrounded by a large reflector.

TABLE 19-3   
BUCKLING OF GRAPHITE-MODERATED LMFR CORES   

<table><tr><td>VBi/Vc</td><td>NU/NBi=0.6×10-3</td><td>NU/NBi=1×10-3</td><td>NU/NBi=1.5×10-3</td></tr><tr><td colspan="4">U233 Fuel</td></tr><tr><td>0.25</td><td>6.64×10-4cm-2</td><td>9.51×10-4cm-2</td><td>11.85×10-4cm-2</td></tr><tr><td>0.50</td><td>8.20</td><td>10.70</td><td>12.50</td></tr><tr><td>1.00</td><td>8.09</td><td>9.82</td><td>10.95</td></tr><tr><td>1.50</td><td>7.33</td><td>8.60</td><td>9.43</td></tr><tr><td>2.00</td><td>6.59</td><td>7.60</td><td>8.22</td></tr><tr><td colspan="4">U235 Fuel</td></tr><tr><td>0.25</td><td>6.05</td><td>8.65</td><td>10.72</td></tr><tr><td>0.50</td><td>7.43</td><td>9.63</td><td>11.19</td></tr><tr><td>1.00</td><td>7.25</td><td>8.74</td><td>9.71</td></tr><tr><td>1.50</td><td>6.53</td><td>7.64</td><td>8.30</td></tr><tr><td>2.00</td><td>5.68</td><td>6.72</td><td>7.23</td></tr></table>

TABLE 19-4   
REFLECTOR SAVINGS OF U235-BI CORES MODERATED BY GRAPHITE   

<table><tr><td rowspan="2">Reflector</td><td colspan="5">Core</td></tr><tr><td>\(V_{\text{Bi}}/V_{\text{C}}=\)</td><td>1</td><td>2</td><td>1</td><td>2</td></tr><tr><td>Reflector</td><td>\(N_{\text{U}}/N_{\text{Bi}}=\)</td><td>\(0.6 \times 10^{-3}\)</td><td>\(0.6 \times 10^{-3}\)</td><td>\(1.5 \times 10^{-3}\)</td><td>\(1 \times 10^{-3}\)</td></tr><tr><td>Graphite</td><td></td><td>1.71 ft</td><td>2.10 ft</td><td>1.66 ft</td><td>2.10 ft</td></tr><tr><td>90%C-10% Void</td><td></td><td>1.62</td><td>2.00</td><td>1.63</td><td>2.01</td></tr><tr><td>\(V_{\text{C}}-V_{\text{Bi}}-V_{\text{Th}}:\)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>85-5-0</td><td></td><td>1.69</td><td>2.04</td><td>1.65</td><td>2.04</td></tr><tr><td>85-15-0</td><td></td><td>1.66</td><td>1.97</td><td>1.59</td><td>2.01</td></tr><tr><td>85-10-5</td><td></td><td>0.70</td><td>0.82</td><td>0.78</td><td>0.87</td></tr><tr><td>70-20-10</td><td></td><td>0.58</td><td>0.68</td><td>0.65</td><td>0.73</td></tr></table>

19-2.3 Critical mass. The results of age-diffusion theory are in good agreement with multigroup calculations for predominantly thermal LMFR reactors. At higher fuel concentrations, however, the age theory overestimates the critical mass, as shown in Table 19-5 [1]. The differences in critical mass estimates are large only for weakly moderated reactors.

TABLE 19-5   
CRITICAL MASS AND DIAMETER OF U235-FUELED LMFR SPHERES WITH A 90-CM GRAPHITE REFLECTOR   

<table><tr><td rowspan="2">NU/NBi</td><td rowspan="2">VBi-U/VC</td><td colspan="2">Age-Diffusion</td><td colspan="2">Multigroup</td></tr><tr><td>Diameter, ft</td><td>Mass, kg</td><td>Diameter, ft</td><td>Mass, kg</td></tr><tr><td colspan="6">Graphite-moderated</td></tr><tr><td rowspan="3">1×10-3</td><td>0.25</td><td>4.38</td><td>2.73</td><td>4.52</td><td>3.02</td></tr><tr><td>1.0</td><td>3.88</td><td>4.77</td><td>3.81</td><td>4.53</td></tr><tr><td>2.0</td><td>4.15</td><td>7.79</td><td>4.04</td><td>7.15</td></tr><tr><td rowspan="2">1×10-2</td><td>0.25</td><td>2.57</td><td>5.50</td><td>2.28</td><td>3.89</td></tr><tr><td>1.0</td><td>2.79</td><td>17.69</td><td>2.24</td><td>9.20</td></tr><tr><td colspan="6">Beryllium-moderated</td></tr><tr><td rowspan="3">1×10-3</td><td>0.25</td><td>3.86</td><td>1.87</td><td>3.88</td><td>1.92</td></tr><tr><td>1.0</td><td>3.08</td><td>2.37</td><td>2.94</td><td>2.07</td></tr><tr><td>2.0</td><td>3.29</td><td>3.86</td><td>3.04</td><td>3.05</td></tr><tr><td rowspan="3">1×10-2</td><td>0.25</td><td>1.90</td><td>2.22</td><td>1.66</td><td>1.49</td></tr><tr><td>1.0</td><td>2.11</td><td>7.70</td><td>1.73</td><td>4.19</td></tr><tr><td>2.0</td><td>2.43</td><td>15.55</td><td>1.94</td><td>7.87</td></tr></table>

19-2.4 Breeding. The conversion ratio obtainable in liquid metal systems depends on a number of variables, such as the fuel and fertile material concentrations, the fission-product processing methods, losses to the core container, etc. In a feasibility study of the LMFR conducted by the Babcock & Wilcox Company, currently practical reactor designs were reported (BAW-2) with conversion ratios ranging from 0.8 to 0.9, depending on whether an oxide slagging or fused salt method was used for nonvolatile fission-product processing. The U/Bi atomic ratio was low $(0.6 \times 10^{-3})$ and a $2\frac{1}{4}\%$ Cr-1% Mo steel core container was used, both

choices tending to reduce the possible breeding ratio. The estimates of the neutron balance are given in Table 19-6 [6].

TABLE 19-6   
NEUTRON BALANCE OF $\mathbf{TH}^{232}$ , U $^{233}$ BREEDER   

<table><tr><td>Production per U233absorption</td><td>Scheme A
Oxide slagging
2.31</td><td>Scheme B
Fused-salt process
2.31</td></tr><tr><td>Losses: Absorption in
U233</td><td>1.00</td><td>1.00</td></tr><tr><td>Bi</td><td>0.13</td><td>0.13</td></tr><tr><td>C</td><td>0.05</td><td>0.05</td></tr><tr><td>Fission products</td><td>0.12</td><td>0.03</td></tr><tr><td>Higher isotopes</td><td>0.02</td><td>0.02</td></tr><tr><td>Croloy structure</td><td>0.12</td><td>0.12</td></tr><tr><td>Th</td><td>0.80</td><td>0.89</td></tr><tr><td>Pa</td><td>0.02</td><td>0.02</td></tr><tr><td>Leakage</td><td>0.05</td><td>0.05</td></tr></table>

19-2.5 Control. Because of its prompt temperature coefficient, the LMFR is expected to be stable. Nevertheless, it represents a completely new and untested system. There are a number of ways in which the reactivity of the system can change, for example, with changes in inlet temperature, concentration, or velocity of the fuel, and changes in xenon concentration, delayed neutron emitter concentration, and blanket composition. Most of these changes are expected to be gradual, but they can be sufficiently large to require the use of control rods. Inherent stability has not been demonstrated in operating reactors except over a limited range in reactivity and power output. In a reactor with a high-velocity coolant there may occur sudden changes of reactivity which are too fast for conventional control. Thus both inherent stability against sudden reactivity changes and control rods for large but gradual reactivity changes are needed until considerable experience has been gained in operation of the reactor.

Studies have been carried out at BNL on control requirements for an LMFR experiment. The control requirements depend not only on the choice of operating temperatures, the possible xenon and fission-product poisoning, etc., but also on conceivable emergency situations such as errors in fuel concentration control. In a reactor with a full breeding blanket, the control requirements may have to include the effect of complete loss of the breeder fluid.

For a 5-mw experiment, control of $15\%$ reactivity appears to be ample and can be obtained with four $2\frac{1}{4}\% \mathrm{Cr - }1\%$ Mo steel rods of about 2-in. diameter. Blacker rods containing boron could, of course, be used to increase reactivity control. A study of various arrangements of identical rods in a ring around a central rod indicates that the optimum position of the ring occurs at about $1/4$ of the distance from the reactor center to the (extrapolated) radius of the reactor core.

It would be highly desirable to use sheaths for control rods in order to eliminate the problem of rod insertion through a heavy liquid metal. Steel sheaths are not satisfactory, since they reduce the breeding ratio in a liquid-metal power breeder and reduce the overall thermal flux in an experimental reactor. The solution to the problem may lie in the development of structurally sound beryllium sheaths.

19-2.6 Shielding. Shielding of an LMFR is complicated by the necessity of shielding an external circuit in which the delayed neutron emitters and fission products decay.

Calculations by K. Spinney at BNL indicate that even for a 5-Mw experimental reactor, about 5.5 ft of concrete are required as a neutron shield around the reactor cell. Gamma shielding of the cell requires about 8.5 ft of ordinary concrete or 4.5 ft of BNL concrete (70% Fe). For this reason, it has been proposed that heavy concrete be used as the shield for the 5-Mw reactor. For the rest of the circuit, including the degasser, pumps, heat exchanger, etc., the advantage of using BNL concrete is less evident.

# 19-3. LMFR KINETICS

A number of fundamental studies of the kinetics of circulating fuel reactors have been carried out at ORNL and by Babcock & Wilcox Company. A review of the subject has been given by Welton [2]. At low power, the equations governing the system are linear and complicated chiefly by the feedback of delayed neutrons. General results for the in-hour relation have been obtained by Fleck [3] for $\mathrm{U}^{233}$ and $\mathrm{U}^{235}$ -fueled reactors. At high power, the kinetics are much more complicated and there is a real question whether the response of a complex reactor can be accurately predicted in advance of its operation. Bethe [6] has strongly recommended the use of oscillator experiments to determine reactor transfer functions. Despite such experiments, however, the mechanism responsible for the resonances observed in EBR-I has, to date, not been satisfactorily explained.

There are two methods of treating the kinetics of a reactor. In the open-loop method, the inlet temperature is taken as constant. The justification for this procedure is that this condition generally prevails during rapid

transients, the feedback of information through the external system being slow by comparison. The method, however, suffers from the defect that it cannot reveal instabilities associated with the entire circuit. In the closed-loop method, the external system, or a reasonable facsimile, is coupled to the reactor system. The representation of the reactor, however, is generally oversimplified because of the complexity of the over-all system.

Although the set of kinetic equations that include temperature effects are nonlinear, the linearized equations are satisfactory for the investigation of stability and the qualitative transient behavior. A large subset of equations is required to properly treat the effect of the delayed neutron emitters. Again, however, lumping the delayed neutrons into a single group, or neglecting them altogether, always appears to lead to qualitatively, if not quantitatively, correct results.

A study of the temperature-dependent open-loop kinetics of the LMFR has been carried out by Fleck [4]. The effect of delayed neutrons and the delayed moderator temperature coefficient were neglected. Under these conditions, Fleck found that the reactor responded rapidly and with little overshoot in temperature when subjected to the largest permissible reactivity excursions.

Using a method developed at the Oak Ridge National Laboratory (ORNL-CF1-56-4-183) for homogeneous systems, the Babcock & Wilcox Company has studied the stability of the LMFR against small oscillations. The results show that the LMFR models under study are stable up to power densities 100 to 1000 times greater than the nominal design level.

Fleck has also examined the transient pressures in LMFR cores by treating the bismuth as a frictionless, compressible fluid. He found that the maximum pressures developed during conceivable transients were quite small. The assumption sometimes made, that the fluid external to the core can be represented as an incompressible slug, was found to overestimate the transient pressures.

In general, heterogeneous reactors possessing both a small prompt (positive or negative) fuel temperature coefficient and a large delayed negative moderator temperature coefficient can be expected to exhibit oscillatory instability at sufficiently high power. However, elementary models indicate that power levels high enough to cause such instability are not achievable in present reactors. Further study of the complex heat-transfer transients in reactor systems is still required before reactor stability can be assured.

# REFERENCES

1. J. CHERNICK, Small Liquid Metal Fueled Reactor Systems, Nuclear Sci. and Eng. 1(2), 135 (1956).   
2. T. A. Welton, Kinetics of Stationary Reactor Systems, in Proceedings of the International Conference on the Peaceful Uses of Atomic Energy, Vol. 5. New York: United Nations, 1956. (P/610, p. 377)   
3. J. A. FLECK, JR., Theory of Low Power Kinetics of Circulating Fuel Reactors with Several Groups of Delayed Neutrons, USAEC Report BNL-334, Brookhaven National Laboratory, April 1955.   
4. J. A. FLECK, Jr., The Temperature Dependent Kinetics of Circulating Fuel Reactors, USAEC Report BNL-357, Brookhaven National Laboratory, July 1955.   
5. G. T. TRAMMELL, Oak Ridge National Laboratory, 1955. ORNL-1893, 1955.   
6. BABCOCK & WILCOX Co., Liquid Metal Fuel Reactor; Technical Feasibility Report, USAEC Report BAW-2(Del.), June 30, 1955.