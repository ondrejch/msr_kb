![](images/59b8c80f2daf5da751a2206ae637d34906a847a2a9b7e7d24fe0f0d04600048b.jpg)

# LEGAL NOTICE

This report was prepared as an account of Government sponsored work. Neither the United States, nor the Commission, nor any person acting on behalf of the Commission:

A. Makes any warranty or representation, expressed or implied, with respect to the accuracy, completeness, or usefulness of the information contained in this report, or that the use of any information, apparatus, method, or process disclosed in this report may not infringe privately owned rights; or   
B. Assumes any liabilities with respect to the use of, or for damages resulting from the use of any information, apparatus, method, or process disclosed in this report.

As used in the above, "person acting on behalf of the Commission" includes any employee or contractor of the Commission, or employee of such contractor, to the extent that such employee or contractor of the Commission, or employee of such contractor prepares, disseminates, or provides access to, any information pursuant to his employment or contract with the Commission, or his employment with such contractor.

# CONTENTS

I Introduction. 1

II Description of the MSRE. 1

III Theoretical Predictions 4

A. Description of Mathematical Model.... 4

B. Results 4

IV Selection of Experimental Methods.. 6

A. Characteristics of the MSRE Regulating Rod. 6

B. Test Signals Used in the Experiments... 9

1. Pseudo-random Binary Test 9

2. Pulse Tests 10

3. Step Tests 12

V Experimental Procedures. 13

A. Implementation of Pseudo-random Binary Tests 13

B. Implementation of Pulse and Step Tests 13

VI Analysis Procedures. 13

A. Direct Analysis of PRBS Tests 13

B. Indirect Analysis of PRBS Tests 17

C. Step Response Test Analysis 21

D. Pulse Response Test Analysis 21

VII Results. 21

A. Transient Responses 22

B. Correlation Functions 22

C. Frequency Responses 32

VIII Interpretation of the Results. 32

IX References. 45

Appendix A. Potential Sources of Experimental Error Due to Equipment Limitations.... 47

Appendix B. The Direct Method for Cross-Power Spectrum Analysis...

LEGAL NOTICE

This report was prepared as an account of Government sponsored   
States, nor the Commission, nor any person acting on behalf of the Commission: A. Makes any warranty or representation, expressed or implied, with respect to the accu racy, completeness, or usefulness of the information contained in this report, or that the use privately owned rights; or B. Assumes any liabilities with respect to the use of, or for damages resulting from the   
As used in the above, "person acting on behalf of the Commission" includes any eme-   
ployee or contractor of the Commission, or employee of such contractor prepares,   
such employee or contractor of the Commission, or employee of such contractor prepares,   
disseminates, or provides access to, any information pursuant to his employment or contract   
with the Commission, or his employment with such contractor.

![](images/99971309f8ad1b4b269e31a1fad7c7954868cc44ab26c51ef60463d7b39a732a.jpg)

# I. INTRODUCTION

A series of experiments was performed on the Molten Salt Reactor Experiment (MSRE) to determine the frequency response of the uncontrolled reactor system. Tests were performed at eight different power levels ranging from zero to full power. Three different types of input disturbances were used to obtain the nuclear power to reactivity frequency response: the pseudo-random binary reactivity input, the pulse reactivity input, and the step reactivity input. Subsequent sections of this report will give a description of the system, a review of previously published theoretical predictions, a description of the testing procedures, and the experimental results.

# II. DESCRIPTION OF THE MSRE

The MSRE is a graphite-moderated, circulating-fuel reactor. The fuel is a mixture of the molten fluoride salts of uranium, lithium, beryllium, and zirconium.<sup>1</sup> The basic flow diagram is shown in Fig. 1. The flows and temperatures shown are nominal values which were calculated for operation at 10 MW, but heat transfer limitations at the radiator currently restrict maximum power operation to about 7.5 MW. The molten fuel-bearing salt enters the core matrix at the bottom and passes up through the core in channels machined out of unclad, 2-inch graphite blocks. The heat generated in the fuel and that transferred from the graphite raise the fuel temperature about $50^{\circ}\mathrm{F}$ . When the system operates at reduced power, the flow rate is the same as at full power and the temperature rise through the core is smaller. The heated fuel salt travels to the primary heat exchanger, where it transfers heat to a non-fueled secondary salt before reentering the core. The heated secondary salt travels to an air-cooled radiator before returning to the primary heat exchanger. The design parameters of major importance from the standpoint of dynamics are shown in Table 1. A detailed description of the MSRE appears in Ref. 1.

ORNL-LR-DWG 56870

![](images/e46fd024c31ab8ef5bdb00a638ca050008c62f67500ce703260f20470c1e043d.jpg)  
Fig. 1 MSRE Flow Diagram

Table 1. MSRE Design Data

# Nuclear

Temperature coefficient of reactivity of the fuel, $^\circ \mathrm{F} - 1$ -4.7 x 10-5

Temperature coefficient of reactivity of the graphite, °F-1 -2.6 x 10-5

Neutron lifetime, sec. 00024

Total delayed neutron fraction .00666

Reactivity loss due to fuel circulation, $\% \frac{\delta K}{K}$ -0.212

# Flow

Flow rate in the primary loop, gpm 1200

Flow rate in the secondary loop, gpm 830

Fuel transit time in the core, sec. 8.5

Fuel transit time in external primary loop, sec. 16.7

Total secondary loop transit time, sec. 24.2

# Heat Transfer

Fuel salt heat capacity, MW sec/°F 4.2

Graphite heat capacity, MW sec/°F 3.6

Heat exchanger heat capacity, MW sec/°F 4

Bulk graphite - fuel salt heat transfer coefficient, MW/°F 0.02

Fuel salt-heat exchanger metal heat transfer coefficient, MW/°F 0.36

Heat exchanger metal, secondary salt-heat transfer coefficient, MW/°F 0.17

Fraction of power generated in the fuel 0.93

# III. THEORETICAL PREDICTIONS

A. Description of Mathematical Model

Throughout the MSRE design effort, a wide variety of mathematical models was used to predict the dynamic behavior. We will limit our discussion here to the most up-to-date and detailed model reported, referred to in Ref. 2 as the "complete" model. The core fluid flow and heat transfer equations were represented by 18 fuel nodes and 9 graphite nodes. The nuclear power distribution and the nuclear importances for each node were derived from a 2-group neutron diffusion calculation. The flow rates and heat transfer coefficients for each node were determined from calculations based on full-scale hydraulic core mockup tests. The assumed flow mixing characteristics were verified by transient tests on the mockup.

The neutron kinetic behavior was described by the usual space-independent equations with six delayed-neutron groups, but with modifications to include the dynamic effects of the circulation of precursors around the primary loop. The thermal reactivity feedback was computed by using a weighted nuclear importance for each of the 27 fuel and graphite nodes. The xenon poisoning reactivity feedback included iodine production and decay into xenon, xenon decay and burnup, and xenon absorption into the graphite.

The transport of molten salt in the primary and secondary loop piping was described by a plug flow model, where heat transfer to the pipes was included. The primary heat exchanger and the salt-to-air heat exchanger were each represented by a 50-node model.

B. Results of Theoretical Analysis

Several different methods of solution were used on the various MSRE dynamics models, including analog and digital computer simulation (time response), frequency response analysis, and pole configuration analysis. The frequency response analyses can be directly compared to the experimental results, since the latter are readily cast in this form.

Fig. 2 shows the theoretical MSRE inherent frequency response

![](images/9593b93bfe05c9046a82dc21174beb9a4cce277ff061d116a20ffc5959f95929.jpg)

![](images/130ce104feaf0e721dd32b585ab3e644f4ebf072b6ca14afb424c9f3b058ce61.jpg)  
Fig.2 MSRE Theoretical Frequency Response

characteristics for normalized neutron level response to reactivity perturbations at several power levels. It can be seen that the system becomes more oscillatory at progressively lower frequencies as the nominal power level decreases, though it is stable for all power levels of interest. An explanation of the inherent stability characteristics is given in Ref. 2.

# IV. SELECTION OF EXPERIMENTAL METHODS

The selection of the experimental methods for the MSRE dynamic tests was based on the information required and on the capabilities of the available equipment. It may be seen from Fig. 2 that the most significant part of the frequency response is in the range 0.01 to 0.1 radians per second, since the amplitude peaks are in this frequency range for the operating power levels of interest. This frequency range corresponds to long periods of natural oscillation (10 min. to 1 min.). This emphasis on low frequency results fortunately made it possible to obtain the important part of the system frequency response using the standard MSRE control rods to introduce the input reactivity perturbations. In this section, we will examine the characteristics of the MSRE regulating rod and the properties of the test signals used.

# A. Characteristics of the MSRE Regulating Rod

The MSRE has three control rods, each with an active length of 59.4 inches. One rod is normally designated as the regulating rod and is used for fine control. The other two rods are shim rods used for coarse adjustments. The rods are actually flexible, stainless steel hoses on which are strung gadolinium oxide poison cylinders. The rods are mounted in thimbles which have two $30^{\circ}$ offsetting bends so that the rods can be centrally located even though there was no room for the control rod drive assemblies above the central axis of the core. The maximum rod speed is $\sim 0.5$ inches/second.

The three control rods are identical. Figures 3 and 4 show the control rod and drive assembly. The position indication for each rod is obtained from two synchros geared to the rod drive mechanism. Synchro number 1 is used for coarse position indication and has a

![](images/f4b638eaa1ca4dc22235d71cd65fb0a3d1d88f362589639d883a53cadbfaf780.jpg)  
Fig. 3 Control Rod Drive Assembly

ORNL-LR-DWG7808

![](images/f764ea4c9b3a2d466b222bf29396a21c0ba4a85876c03824e415d546395677c4.jpg)  
Fig. 4 Diagram of Control Rod Drive

sensitivity of $5^{\circ}$ per inch of rod motion. Synchro number 2 is used for fine position indication and has a sensitivity of $60^{\circ}$ per inch. The signal from the coarse position synchro is transmitted to a torque amplifier which drives a single-turn potentiometer feeding a d-c signal to the MSRE on-line computer.

After the system had operated for some time, it became difficult to obtain reproducible regulating rod position changes for a given time of insert or withdraw. This was due to the wearing of this rod and drive assembly caused by frequent use. For the dynamic tests, one of the rods normally used as a shim rod was used as the regulating rod. Since it is moved much less frequently than the normal regulating rod, it had experienced less wear and had much tighter response characteristics.

There are a number of factors which could adversely affect both the accurate positioning of the rods and the indications of effective rod position given by the instruments. Some of the potential sources of difficulty are listed in Appendix A.

These observations indicate that the MSRE control rods are hardly ideally suited for dynamic testing. However, since no provision was made for special control rods and since the main features of interest occur at low frequency, the testing program was carried out using the standard MSRE control rods. Fortunately, the rods performed far better than expected by their designers, and the final results were only slightly degraded by equipment problems.

# B. Test Signals Used in the Experiments

Three different types of test signals which were used to obtain the frequency response of the system are described in this section. 1) Pseudo-random Binary Test(4)

In this test, specially selected periodic series of positive and negative reactivity pulses called the pseudo-random binary sequence (PRBS) were introduced. The PRBS has the advantage that its frequency spectrum consists of a number of harmonics of approximately equal size. This means that the frequency response may be evaluated at a large number of frequencies in a single test. The spectrum of

the pseudo-random signal from one of the MSRE tests is shown in Fig. 5. We note that the signal strength is concentrated in discrete harmonic frequencies rather than distributed over a continuous spectrum as in the case of non-periodic (e.g. pulse and step) signals. This is helpful since it improves the effective signal-to-noise ratio at these frequencies.

A PRBS may be generated on-line at the test or may be pre-recorded in some fashion and played back as a control signal. On-line generation of the signal was used in these tests (see Section V). A PRBS is characterized by the number of bits in the sequence and the bit duration. A bit is defined as the minimum possible pulse duration in the sequence. All pulses in a PRBS are minimum width or integral multiples thereof. Numerous sequences may be generated, but they are restricted to certain specific numbers of bits. In the MSRE, PRBS tests were run with 19, 63, 127 and 511 bits. If the number of bits is Z and the bit duration is $\Delta t$ , then the PRBS has a period Z $\Delta t$ . The lowest harmonic radian frequency, $\omega_{0}$ , and the spacing of the harmonics, $\Delta \omega$ , is given by $\omega_{0} = \Delta \omega = \frac{2\pi}{Z\Delta t}$ . The PRBS tests which were run and analyzed are shown in Table 2. In each test, the rod motion was selected to give a reactivity change of $0.02\%$ to $0.03\%$ , peak to peak. The maximum reactivity perturbation was determined on the basis of keeping the resulting power level perturbations in the linear range, i.e. $\delta N / N_{0}$ maximum was kept below 0.1.

# 2) Pulse Tests(4)

In theory, it is possible to excite a system with a single pulse-type disturbance and obtain the frequency response by numerically determining the ratio of the Fourier transform of the output to the Fourier transform of the input. The frequency response can theoretically be evaluated at all frequencies since the input has a continuous frequency spectrum. In practice, the pulse test is often unsatisfactory because the available signal strength is distributed over all frequencies, resulting in a small amount of signal around the analysis frequency and thus poor effective signal to noise ratio.

![](images/4a5ffe17e388ec57188c96eae79cb778efe9c5eba57f325d1e260e2a15d4b80c.jpg)  
Fig. 5 Power Spectrum of the Input PRBS at 0.465 MW

Several tests using approximately square reactivity pulses of between 0.01 and $0.02\%$ were employed for the MSRE at zero power. Tests were carried out both with circulating fuel and with stationary fuel.

Table 2. Pseudo-Random Binary Sequence Tests   

<table><tr><td>Power Levels (MW)</td><td>Bits in Sequence</td><td>Bit Duration (sec)</td><td>Periodicity of the PRBS (sec)</td><td>Minimum Frequency (rad/sec)</td></tr><tr><td>0</td><td>19</td><td>6.58</td><td>125</td><td>.05</td></tr><tr><td>0</td><td>63</td><td>3.35</td><td>211</td><td>.03</td></tr><tr><td>.075</td><td>511</td><td>3.35</td><td>1711</td><td>.0037</td></tr><tr><td>.465</td><td>511</td><td>3.35</td><td>1712</td><td>.0037</td></tr><tr><td>1.0</td><td>511</td><td>3.35</td><td>1711</td><td>.0037</td></tr><tr><td>1.0</td><td>127</td><td>5.02</td><td>638</td><td>.0098</td></tr><tr><td>2.5</td><td>511</td><td>3.32</td><td>1699</td><td>.0037</td></tr><tr><td>2.5</td><td>127</td><td>4.97</td><td>631</td><td>.010</td></tr><tr><td>5.0</td><td>511</td><td>3.33</td><td>1701</td><td>.0037</td></tr><tr><td>5.0</td><td>127</td><td>4.97</td><td>631</td><td>.010</td></tr><tr><td>6.7</td><td>511</td><td>3.32</td><td>1698</td><td>.0037</td></tr><tr><td>7.5</td><td>511</td><td>3.33</td><td>1701</td><td>.0037</td></tr><tr><td>7.5</td><td>127</td><td>4.97</td><td>631</td><td>.010</td></tr></table>

# 3) Step Tests(5)

If the output eventually levels off to some constant value after a step disturbance, the frequency response may be obtained by a modified Fourier analysis of the output and the input. As with the pulse tests, the step input has a continuous spectrum, but is hampered by a low effective signal-to-noise ratio at any analysis frequency.

Step tests were used at power levels where the temperature feedback was adequate to cause the power to level off near the original power after the reactivity change. These tests used a reactivity perturbation of 0.01 to $0.02\%$ . Step tests were done at 2.5, 5.0, 6.7, and 7.5 MW.

# V. EXPERIMENTAL PROCEDURES

A. Implementation of Pseudo-random Binary Tests

The pseudo-random binary reactivity sequence required a very precisely controlled series of regulating rod insertions and withdrawals. Since the frequency range of interest was from about 0.002 to 1.0 radian/sec., the rod jogger was designed so that sequence with a bit time of 3 to 5 seconds could be run for as long as 1 hour. The rod jogger system, which required no special-purpose hardware, consisted of a hybrid computer controller shown schematically in Fig. 6. The portable EAI-TR-10 analog computer was used to control the bit time and the rod drive motor "on" times for the insert and withdraw commands. The MSRE digital computer was programmed to control the sequencing of the pulse train by means of a shift-register algorithm.(3) The number of bits in the sequence could be varied over a range between 3 and 33,554,431 bits.

The rod jogger system performed extremely well, as it was able to position the rod with an indicated positioning accuracy of about $\pm 0.01$ in. (corresponding to $\pm 0.0005\%$ $\delta \mathbf{k} / \mathbf{k}$ ) out of $1/2$ in. peak-to-peak rod travel for over a 500 insert-withdraw operations. A typical PRBS rod position signal is shown in Fig. 7 and a typical record of neutron flux changes during a PRBS test is shown in Fig. 8.

The analog computer was also used to amplify and filter the rod-position and power-level signals prior to digitizing. Throughout the dynamic tests the MSRE computer was used in the fast scan mode to digitize and store the data on magnetic tape. Each variable was sampled at the rate of 4 per second.

B. Implementation of Pulse and Step Tests

The same set up as described in (A) was used for the pulse and step tests with the PRBS generator omitted.

# VI. ANALYSIS PROCEDURES

A. Direct Analysis of PRBS Tests

The "direct" method of analysis uses a digital computer simulation of an analog filtering technique for obtaining cross-power spectral density functions. (6) A block diagram of the analyzer is shown in

ORNL-DWG 66-4763

![](images/b511b3086f848ec6e516a5e3e23d8f0eab9ab76bf6dda3813a066e7c606ac04a.jpg)  
Fig. 6 Block Diagram of MSRE Rod Jogging and Data Logging System

Low-Pass Filtered (Filter Transfer Function $= \frac{1}{\lambda + s}$ )

ORNL DWG. 66-11077

![](images/24c70dba5bd4099c0937dc410d4bf175107898a56749c6ecb458b3427d66d9f3.jpg)  
Fig. 7 Indicated Control Rod Position During a 5ll Bit PRBS Test

![](images/720f98a402d87fa1d187d8b296752b473b2e1ed514e5ee76493fe2502557e78d.jpg)  
Fig. 8 Measured Flux Signal During a 511 Bit PRBS Test

Fig. 9. The narrow band-pass filter $\dot{H} (s)$ has the characteristics of a quadratic lag and a transfer function

$$
\mathrm {H} (\mathrm {s}) = \frac {\mathrm {s}}{\omega_ {0} ^ {2} + 2 \xi \omega_ {0} \mathrm {s} + \mathrm {s} ^ {2}}
$$

where $\omega_{0}$ is the center frequency of the filter. Typically the damping factor $\xi$ is set equal to 0.05, giving a filter frequency response as shown in Fig. 10. This analyzer is similar to that described by Chang (7) and Van Deusen (8); the main difference is that it includes extra cross-multiplication terms resulting in higher accuracy. A mathematical description of the method is given in Appendix B.

# B. Indirect Analysis of PRBS Tests

The indirect analysis began with a calculation of the autocorrelation function of the input and the cross-correlation function of the input and the output

$$
C _ {1 1} (\tau) = \frac {1}{T ^ {*}} \int_ {0} ^ {T ^ {*}} I (t) I (t + \tau) d t
$$

$$
c _ {1 2} (\tau) = \frac {1}{T ^ {*}} \int_ {0} ^ {T ^ {*}} I (t) O (t + \tau) d t
$$

where

$$
\begin{array}{l} C _ {l l} (\tau) = \text {t h e a t u c o r r e l a t i o n f u n c t i o n} \\ C _ {1 2} (\tau) = \text {t h e c r o s s - c o r r e l a t i o n f u n c t i o n} \\ \tau = \text {t h e} \\ T ^ {*} = \text {t h e i n t e g r a t i o n t i m e (a m u l t i p l e o f t h e s i g n a l} \\ \end{array}
$$

$$
I (t) = \text {t h e i n p u t s i g n a l} \quad \text {p e r i o d i c i t y})
$$

$$
0 (t) = \text {t h e o u t p u t s i g n a l}
$$

$$
t = \text {t i m e}
$$

ORNL-DMG 68-10283

![](images/ea1e573d2efc201c00d8e19b39717541f923f6ef00d58ab079eebc2367f9857f.jpg)  
Fig. 9 Block Diagram of Cross-Power Spectral Density Analyzer

![](images/4aaa1cf16d0f727bcea5d325e3c2f24d2788e6637a3bdcee3a903a8357753180.jpg)

![](images/d0fc1e4c8bece1db80f554601f9dcd73f8d1657ddb1690c25537b67c40db8fa4.jpg)  
Fig. 10 Frequency Response of Filter Used in CPSD Analyzer

Subsequent Fourier analysis of $\mathbf{C}_{11}(\tau)$ and $\mathbf{C}_{12}(\tau)$ gave the input power spectrum and the cross power spectrum:

$$
\Phi_ {1 1} \left(\omega_ {k}\right) = \frac {1}{T} \int_ {0} ^ {T} C _ {1 1} (\tau) \cos \omega_ {k} \tau d \tau
$$

$$
\Phi_ {1 2} \left(\omega_ {k}\right) = \frac {1}{T} \int_ {0} ^ {T} C _ {1 2} (\tau) \cos \omega_ {k} \tau d \tau - j \frac {1}{T} \int_ {0} ^ {T} C _ {1 2} (\tau) \sin \omega_ {k} \tau d \tau
$$

where

$$
\Phi_ {1 1} \left(\omega_ {k}\right) = \text {i n p u t p o w e r s p e c t r u m a t f r e q u e n c y}, \omega_ {k}
$$

$$
\Phi_ {1 2} \left(\omega_ {k}\right) = \text {c r o s s p o w e r s p e c t r u m a t f r e q u e n c y}, \omega_ {k}
$$

$$
\omega_ {k} = \text {a n g u l a r f r e q u e n c y o f t h e k t h h a r m o n i c} \left(\omega_ {k} = \frac {2 k \pi}{T}\right)
$$

$$
\mathrm {T} = \text {p e r i o d i c i t y o f t h e t e s t s i g n a l}
$$

Note that the input power spectrum is a real quantity since $C_{11}(\tau)$ is always an even function of $\tau$ .

The frequency response, $G(j\omega_{k})$ , is given by

$$
\operatorname {R e} \left[ G \left(j \omega_ {k}\right) \right] = \frac {\frac {1}{T} \int_ {0} ^ {T} C _ {l 2} (\tau) \cos \omega_ {k} \tau d \tau}{\frac {1}{T} \int_ {0} ^ {T} C _ {l l} (\tau) \cos \omega_ {k} \tau d \tau}
$$

$$
\operatorname {I m} [ G (j \omega_ {k}) ] = - \frac {\frac {1}{T} \int_ {0} ^ {T} C _ {l 2} (\tau) \sin \omega_ {k} \tau d \tau}{\frac {1}{T} \int_ {0} ^ {T} C _ {l l} (\tau) \cos \omega_ {k} \tau d \tau}
$$

The magnitude ratio, MR, and the phase, $\theta$ , are given by:

$$
\operatorname {M R} \left(\omega_ {\mathrm {k}}\right) = \sqrt {\left\langle \operatorname {R e} \left[ G \left(j \omega_ {\mathrm {k}}\right) \right] \right\rangle^ {2} + \left\langle I _ {\mathrm {m}} \left[ G \left(j \omega_ {\mathrm {k}}\right) \right] \right\rangle^ {2}}
$$

$$
\Theta \left(\omega_ {k}\right) = \tan^ {- 1} \left\{\frac {\operatorname {I m} [ G (j \omega_ {k}) ]}{\operatorname {R e} [ G (j \omega_ {k}) ]} \right\}
$$

A Fortran computer code for the IBM-7090 or IBM-360 called CABS (9) was prepared to carry out these computations.

C. Step Response Test Analysis

The step response tests were analyzed using a digital computer code which implements Samulon's method. (5,10)

D. Pulse Response Test Analysis

Although pulse response tests were attempted at power levels of $\sim 0$ , 75 KW, 465 KW, and 1 MW, the only successful runs were the ones made at zero power. This was because the low frequency random fluctuations in heat load at low (but non-zero) powers drastically reduced the signal-to-noise ratio. At these powers, the radiator is cooled primarily by natural convection and radiation, and is consequently sensitive to atmospheric disturbances. At higher powers, where most of the cooling was due to forced convection, these fluctuations were not apparent.

The zero power tests required extremely accurate core temperature control and rod positioning in order to avoid drift of the flux level. Since a zero power reactor is an integrating system, a pulse reactivity input results in a change in steady-state flux output, and Fourier transforms are valid only if the response function eventually returns to its initial value. We got around this problem by first numerically filtering the output response data through a high-pass network HP(s) with a transfer function

$$
\mathrm {H P (s)} = \frac {5 0 \mathrm {s}}{5 0 \mathrm {s} + 1}
$$

then performing the numerical Fourier transform, and finally compensating the resulting frequency response for the high-pass filter characteristics.

The numerical Fourier transform calculations were done by a digital computer code using a novel method (11) which is mathematically equivalent to the standard technique of summing the products of $f(t) \cdot \cos \omega t$ and $f(t) \cdot \sin \omega t$ , but which reduces the computing time by a factor of 3.

# VII. RESULTS

The experimental data were analyzed to give correlation functions, input power spectra and cross power spectra, and frequency responses. These results are given in this section along with the directly observable

transient response to system disturbances.

# A. Transient Responses

At each power level, a transient was induced by inserting a reactivity pulse or step, or by simply allowing the system to seek equilibrium after the completion of some other test. These transient responses are informative in themselves since they demonstrate the damping and the natural frequency of oscillation of the system. Figure 11 shows the observed transient response. At 0.075 MW, it took over two hours for the flux to return to equilibrium.

# B. Correlation Functions

The pseudo-random binary tests were analyzed by the direct method and the indirect method. Autocorrelation functions of the input and cross correlation functions of the input and output were obtained as intermediate results by the indirect method. The correlation functions had the expected appearance in all tests until the 2-1/2 MW tests. In that test, spikes appeared in the correlation functions which have been present in all tests since then. The spikes always appeared at points 432 sec. from each end of a period in the 511 bit tests (~1700 sec. period), and 34 sec. from each end in the 127 bit tests (~630 sec. period). Figures 12 through 19 show typical autocorrelation functions and cross-correlation functions for tests before the 2-1/2 MW test and after the 2-1/2 MW test.

The reason for the appearance of the spikes is not yet known. The only significant difference noted in the input signal at 0.465 MW and at 2-1/2 MW was a change in effective pulse duration for positive and negative pulses. At 0.465 MW, the duration of a pulse above the midpoint was the same as the duration of a pulse below the midpoint. At 2-1/2 MW, the duration of pulses below the midpoint was longer than the duration of pulses above the midpoint. This was apparently due to changes in the coasting characteristics of the rod. Calculations were performed on pseudo-random binary sequences in which the pulse duration was changed for positive and negative pulses to determine whether this would cause spikes in the autocorrelation function. These calculations showed spikes for some sequence lengths but not for others. In particular, spikes were not found in these calculations for a 5ll bit sequence. The conflicting indications furnished by

![](images/cc32e4574965eabf145fdabee015ea35f995356decad32e3dec586427244b971.jpg)  
Fig. 11 MSRE Power Level Transients

![](images/e7011e6a14ba0ed3fd2454b4a0e6a2571b69b8170bae21d8135120a9025ee5f8.jpg)  
Fig. 12 Input Autocorrelation Function for a 5ll Bit PRES Test at 0.465 MW

![](images/bfe68b2694e93bf12dd47da6c5dae1429c2f9cc7a91f879be3b627fa9bd1c40e.jpg)  
Fig. 13 Cross-Correlation Function for a 511 Bit PRBS Test at 0.465 MW

ORNL DWG. 66-11080

Autocorrelation Function (Arbitrary Units)

![](images/ffa28c2b6ccabdd535fd7aae577da03ca8bc74dbd5cc30847c8da7f0bf83102a.jpg)  
Fig. 14 Input Autocorrelation Function for a 127 Bit PRBS Test at 1.0 MW

![](images/dbc4d3452c66e467541b4e4e6edeb8cd121f90b803dc81d43954ae78fa4f2742.jpg)  
Fig. 15 Cross-Correlation Function for a l27 Bit PRBS Test at 1.0 MW

ORNL DWG. 66-11082

Autocorrelation Function (Arbitrary Units)

![](images/2b8d9dbf8ca12faac03ca8902a6abbf3ab5543ec4e34dd7754ac11409ffa5177.jpg)  
Fig. 16 Input Autocorrelation Function for a 5ll Bit PRBS Test at 2.5 MW

![](images/47357cc85ff96f0d9d9acb16e316baa5e82b0dcd01b1543380571ec59aa20999.jpg)  
Fig. 17 Cross-Correlation Function for a 5ll Bit PRBS Test at 2.5 MW

Autocorrelation Function (Arbitrary Units)

![](images/eaa8611d4e6af1c74a95f4f22816386c88dfcaa728b070b9871598be57e436fd.jpg)  
Fig. 18 Input Autocorrelation Function for a 127 Bit PRBS Test at 2.5 MW

Cross-Correlation Function (Arbitrary Units)

ORNL DWG. 66-11085

![](images/80d775d5e58d2abccf4320b0da52d6d48743d20721bcc20f7c1e89c762399a4e.jpg)  
Correlation Time (sec)   
Fig. 19 Cross-Correlation Function for a 127 Bit PRBS Test at 2.5 MW

these calculations have not yet been resolved. However, we should note that this unexpected feature of the correlation functions does not invalidate the final result, the frequency response. It simply means that the spectral properties of the input and output are slightly different than anticipated, but that the ratio of cross power spectrum to input power spectrum still gives a valid frequency response.

# C. Frequency Responses

The results of the frequency response analyses are shown in Figures 20 through 28. The legend in each figure indicates the type of test and the analysis procedure. The theoretical curves were taken from previously published results $^{(2)}$ when the experimental power levels corresponded to available calculations. The curves for the other cases were obtained using the same procedures as were used to obtain the published results. Results obtained by Roux and Fry $^{(12)}$ by analyzing the random noise in the neutron flux signal are also shown with the zero-power results. These results were normalized to the theoretical results at 9 rad/sec. These points were obtained by taking the square root of the measured power spectral density (PSD) of the neutron flux signal after subtracting the background PSD. This gives a result which is proportional to the amplitude of the flux-to-reactivity frequency response, assuming that the observed noise is the result of a white noise reactivity input.

The natural period of oscillation of the system was determined either by direct observation of a transient or by location of the peak of the frequency response. These results, along with theoretical predictions, are shown in Fig. 29.

# VIII. INTERPRETATION OF THE RESULTS

The objectives of the dynamic testing program are twofold: 1) provide information on the stability and operability of the system; 2) provide information for checking procedures for making theoretical predictions so that future calculation on this and other similar systems will be improved. The results are interpreted in terms of these two objectives.

![](images/eb5a6a10a8550842e9ad12957ab91dbf5fefc9f6d0ddf65da8ddbc413becdef8.jpg)

![](images/ea535b5aa30705ad39972b1574c42bcab59c95cd2b55b1641a583c3edf932678.jpg)  
Fig. 20 Frequency Response of $\frac{\delta N / N_{\mathrm{o}}}{\delta K / K_{\mathrm{o}}}$ at Zero Power; Fuel Circulating

![](images/04c4aebb1652fdcbfb178d2c88da05c921e4f37b749175f1dafcef9ba2bf4f65.jpg)

![](images/3bca0359815264503ba366f87ce4bae2a8f1d201ec6e5435b287ac8e1511f012.jpg)  
Fig. 21 Frequency Response of $\frac{\delta N / N_{0}}{\delta K / K_{0}}$ at Zero Power; Fuel Static

![](images/de8c8d7d23f7cb682eb36152fb36ada5bcd05daf69209ad79d954504071efd74.jpg)

![](images/ffab40476a01ca268fd2a5355e8a90b54b428c7319d58a0dc0734e662c5f7b5e.jpg)  
Fig. 22 Frequency Response of $\frac{\delta N / N_{0}}{\delta K / K_{0}}$ ; Power = 0.075 MW

![](images/1ba73555d5e17a6cb886e2a04b9b7458f02044fb21223158299f28be6af0cc56.jpg)

![](images/6cb6d309f8bc5cd82d13affd90e0cfc7e33bf8ed1071be7dafa1f64dfa443c6b.jpg)  
Fig. 23 Frequency Response of $\frac{\delta N / N_{0}}{\delta K / K_{0}}$ ; Power = 0.465 MW

![](images/7fed00739bb7f06eade54d9b0faed207318d176b060964610276e3e6656b46df.jpg)

![](images/8302a67efbd8732ab4a853e2a358cb55299bc5199b72a07751c1f8d08ad1e53d.jpg)  
Fig. 24 Frequency Response of $\frac{\delta N / N_{0}}{\delta K / K_{0}}$ ; Power = 1.0 MW

![](images/9e1386ecfbd59dd93cc09021caf0d06c98cf53ea4f2343fff0334910304bfb82.jpg)

![](images/fae6865c718a8d344540344f71ca8e577caa122707fced0e34b0e7e5ad69c2d7.jpg)  
Fig. 25 Frequency Response of $\frac{\delta N / N_{\circ}}{\delta K / K_{\circ}}$ ; Power = 2.5 MW

![](images/f7b8c6c0ca6a056f050b55b3c5a63c5a292ff943b2104d05b47437075a22005c.jpg)

![](images/4943ed9cfce2ec61ee5cd742d9709ebb110a89ed360eb90df65d02b3af3a5304.jpg)  
Fig. 26 Frequency Response of $\frac{\delta N / N_{0}}{\delta K / K_{0}}$ ; Power = 5 MW

![](images/1f76ac6edbb26878a0953579a911c5b4ad5a74f5c543127f327fa79ca3635d70.jpg)

![](images/cc68f4ce59aaac42df8d17a64b4a498c245806692c00ace8f0547349ae3f8af7.jpg)  
Fig. 27 Frequency Response of $\frac{\delta N / N_{0}}{\delta K / K_{0}}$ ; Power = 6.7 MW

![](images/96b1cd53dde1501525f947293e33b1e2ae5bfd6f00a23132fb64ff9c713135e7.jpg)

![](images/5f76f0eebe2780f70dfc8aacd18521d3bad5f24862087cbfecd86d620702100d.jpg)  
Fig. 28 Frequency Response of $\frac{\delta\mathrm{N} / \mathrm{N}_0}{\delta\mathrm{K} / \mathrm{K}_0}$ ; Power = 7.5 MW

![](images/71b5775b463d8e1530bc2991e4f5b7c23405ceca32d5ffcd7300f8007bb85626.jpg)  
Fig. 29 MSRE Natural Periods of Oscillation

The linear stability of the system is certainly adequate. The frequency response shows a resonance which shifts to higher frequencies and lower amplitudes as power increases. This means that the transient response to a disturbance at low power will display a lightly damped, low frequency return to equilibrium (period greater than ten minutes for powers less than 500 KW). At higher power the system response is much more strongly damped and much faster. For instance, a disturbance at 7.5 MW causes a transient which is essentially completed in 1-1/2 minutes. These observations are in good agreement with prior predictions.

A detailed quantitative check of the theoretical predictions by experimental tests is much more difficult than a comparison of more general dynamic features such as stability, location of resonance peaks and the changes expected in these performance measures with power level. Early attempts to fit parameters in the theoretical model to give agreement in the absolute amplitude of the frequency response were abandoned because of uncertainties in the measured amplitudes caused by equipment limitations. While all of the tests at a given power level give results with the same shape, there is a difference in the absolute magnitude ratios. Figure 27 clearly shows this bias effect. Furthermore, the portion of the frequency response above 0.3 rad/sec should be the same for all power levels since feedback effects are small in this frequency range and the zero power frequency response should dominate. The experimental results for various power levels show the same shape in this frequency region, but different absolute amplitudes. This further indicates a bias problem. This bias problem is not surprising in view of the equipment characteristics discussed in Section IV.

In spite of the bias difficulties, one feature of the theoretical model is shown to be incorrect by experimental results. At high power (greater than 5 MW) the theoretical magnitude ratio curve has a dip at 0.2 rad/sec. This is due to the reappearance of a fuel salt temperature slug in the core after traveling around the primary loop. Since this dip was not observed experimentally, there must be

more mixing and heat transfer in the primary loop than was included in the theoretical model.

Because the predicted frequency response has the correct shape and location on the frequency axis, we feel that the model used for the MSRE dynamic analysis is a good representation of the system. The only discrepancy observed in predicted and observed shapes is the predicted dip at 0.2 rad/sec, just discussed. The apparent bias in the measured amplitude unfortunately prohibits detailed parameter fitting.

# REFERENCES

1. R. C. Robertson, MSRE Design and Operations Report, Part 1: Description of Reactor Design, USAEC Report ORNL-TM-728, Oak Ridge National Laboratory, January 1965.   
2. S. J. Ball and T. W. Kerlin, Stability Analysis of the Molten-Salt Reactor Experiment, USAEC Report ORNL-TM-1070, Oak Ridge National Laboratory, December 1965.   
3. T. W. Kerlin, The Pseudo-Random Signal for Frequency Response Testing, USAEC Report ORNL-TM-1662, Oak Ridge National Laboratory, September 1966.   
4. J. O. Hougen and P. A. Walsh, Pulse Testing Method, Chem. Eng. Prog., 57(3): 69-79 (March 1961).   
5. H. A. Samulon, Spectrum Analysis of Transient Response Curves, Proc. IRE, 39, 175-186 (1951).   
6. S. J. Ball, Instrumentation and Controls Div. Annual Progr. Rept. Sept. 1, 1965, USAEC Report ORNL-3875, pp. 126-7, Oak Ridge National Laboratory.   
7. S.S.L. Chang, Synthesis of Optimum Control Systems, Chap. 3, McGraw-Hill, New York, 1961.   
8. B. D. Van Deusen, Analysis of Vehicle Vibration, ISA Trans. 3, No. 2, 138-148, 1964.   
9. T. W. Kerlin and J. L. Lucius, CABS - A Fortran Computer Program for Calculating Correlation Functions, Power Spectra, and the Frequency Response from Experimental Data, USAEC Report ORNL-TM-1663, Oak Ridge National Laboratory, September 1966.   
10. E. M. Grabbe, S. Ramo, and D. E. Wooldridge (Editors), Handbook of Automation, Computation, and Control, Vol. 1, Chap. 22, J. Wiley and Sons, New York, 1958.   
11. S. J. Ball, A Digital Filtering Technique for Efficient Fourier Transform Calculations, USAEC ORNL-TM report (in preparation).   
12. D. P. Roux, and D. N. Fry, ORNL Instrumentation and Controls Division, personal communication.   
13. J. E. Gibson, Nonlinear Automatic Control, Chap. 1, McGraw-Hill, New York, 1963.

14. G. C. Newton, L. A. Gould, and J. F. Kaiser, Analytical Design of Linear Feedback Controls, pp. 366-381, J. Wiley and Sons, New York, 1957.   
15. C. T. Morrow, Averaging Time and Data-Reducing Time for Random Vibration Spectra, J. Acoust. Soc. Am., 30, 456 (1958).   
16. T. J. Karras, Equivalent Noise Bandwidth Analysis from Transfer Functions, NASA-TN-D2842, November 1965.   
17. L. D. Enochson, Frequency Response Functions and Coherence Functions for Multiple Input Linear Systems, NASA-CR-32, April 1964.   
18. H. M. Paynter and J. Suez, Automatic Digital Setup and Scaling of Analog Computers, Trans. ISA, 3, 55-64, January 1964.   
19. S. J. Ball and R. K. Adams, MATEXP, A General Purpose Digital Computer Program for Solving Nonlinear Ordinary Differential Equations by the Matrix Exponential Method, USAEC ORNL report (in preparation), Oak Ridge National Laboratory.

# APPENDIX A

# Potential Sources of Experimental Error Due to Equipment Limitations

As discussed in Section IV.A, there were a number of factors that could have had adverse effects on the experimental results, and they are listed below:

1) Friction in the bends in the thimbles. Rollers are mounted in the bends of the thimble, but there is still considerable friction. (Tests show that the rods fall with an acceleration of only about $0.4\mathrm{g}$ .) This suggests that part of the motion at the rod drive might go into bowing of the flexible hose rather than into motion of the bottom of the poison section.   
2) Bends in the hose. It was observed that an old MSRE control rod used for out-of-pile testing did not hang straight when suspended from the top. It had gradual bends that could be worked out by hand, but which were not pulled out by the weight of the rod (6 to 8 lb). If such bends exist in the MSRE rod used for the tests, then the motion of the bottom of the rod will not be the same as the motion at the top of the rod if a bend in the hose is passing over a roller in the bend of the thimble.   
3) Restricted twisting. The test rod showed a tendency to turn when inserted into a mockup of the MSRE thimble. This twisting is prevented in the reactor since the top of the rod is rigidly connected to the chain drive (see. Fig. 3). If a tendency to twist is prevented, the hose will bow and cause a difference in axial motion between upper and lower sections.   
4) Sprocket chain meshing. The action of the drive motor is transmitted to the drive chain by a sprocket. This sprocket has a diameter of 1.282 in. and the length of the links in the chain is $\frac{1}{4}$ in. The fact that the flat links cannot exactly follow the circular contour of the sprocket means that some of the sprocket motion is taken up by a lateral motion of the chain as well as the desired vertical motion.   
5) Sticking of poison beads. The control rod thimble contains

vanes for centering the control rod. The vanes are held in place by circular spacers located 4 in. apart. If the vanes became warped, they could touch links in the poison chain in certain sections without touching links in nearby sections. Since there is slack in the threading of the poison cylinders on the central hose, this friction could hold up the movement of certain poison elements.

6) Indicated position errors. It was necessary to use the coarse synchro signal (5 deg of turn per inch of rod motion) for logging on the MSRE computer and for subsequent data analysis. Since the 1/2-in. rod motion used in the tests corresponds to only 2.5 deg rotation of the synchro, sizeable percentage error could be caused by only a few tenths of a degree of deadband in the gears leading to the synchro. Periodic calibrations of the logged rod position against the fine synchro, however, indicated that the error is less than $\pm 5\%$ for a 1/2-in. rod travel. The maximum deadband in the logger signal corresponded to about $\pm 0.008$ in. of rod motion.

# APPENDIX B

# The Direct Method for Cross-Power Spectrum Analysis

Each of the terms used in the cross-power spectrum analysis is computed in the following manner:

![](images/28618c24886fc3b6aec37adb2c1e8c79a1f2274742d09b4d82b9a9ea6342dc8b.jpg)

where $\mathbf{H}_{1}$ and $\mathbf{H}_{2}$ are either $\mathrm{H(j\omega)}$ or $\frac{\omega_0}{j\omega}\mathrm{H(j\omega)}$ ; and $\mathbf{f}(\phi_{\mathbf{IO}})$ (depending on which combination of $\mathbf{H}_{1}$ and $\mathbf{H}_{2}$ are used) is related either to the real (COPOWER) or the imaginary (QUAD POWER) part of the cross-power spectral density (CPSD) $\phi_{\mathbf{IO}}$ . Four combinations of the basic computation shown above are used in the CPSD analysis as shown in Fig. 9.

To convert filtered time domain functions to frequency domain functions, we make use of Parseval's theorem, $^{13}$ which is

$$
\int_ {- \infty} ^ {\infty} a (t) b (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} B (j \omega) A (- j \omega) d \omega , \tag {1}
$$

where $\mathrm{B(j\omega)} =$ Fourier transform of $\mathrm{b(t)}$ , and $\mathrm{A(-j\omega)} =$ complex conjugate of the Fourier transform of $\mathrm{a(t)}$ .

Considering that only a finite integrating time $T$ is available to us:

$$
\int_ {0} ^ {T} a (t) b (t) d t \approx \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} B (j \omega) A (- j \omega) d \omega . \tag {2}
$$

Noting that

$$
A (j \omega) = H _ {1} (j \omega) I (j \omega), \tag {3}
$$

$$
B (j \omega) = H _ {2} (j \omega) O (j \omega), \tag {4}
$$

where

$$
I (j \omega) = F o u r i e r \text {t r a n s f o r m} \text {o f} \text {i t}, i (t),
$$

$$
0 (j \omega) = \text {F o u r i e r}
$$

From the definition of the complex conjugate, it can be shown that

$$
A (- j \omega) = H _ {1} (- j \omega) I (- j \omega), \tag {5}
$$

$$
B (- j \omega) = H _ {2} (- j \omega) O (- j \omega). \tag {6}
$$

Hence (2) can be rewritten in terms of the Fourier transforms of the input and output signals

$$
\int_ {0} ^ {\mathrm {T}} a (t) b (t) d t \approx \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} H _ {2} (j \omega) H _ {1} (- j \omega) I (- j \omega) O (j \omega) d \omega . \tag {7}
$$

Since the cross-power spectral density is defined as<sup>7</sup>

$$
\phi_ {I O} (j \omega) = \lim  _ {T \rightarrow \infty} \frac {1}{T} [ I (- j \omega) \quad O (j \omega) ] \tag {8}
$$

it behooves us to operate on (7) in order to be able to incorporate $\phi_{\mathrm{IO}}(\mathrm{j}\omega)$ . Taking the limit of both sides of (7) as $\mathbf{T} \to \infty$ and dividing by $\mathbf{T}$ , we get

$$
\lim  _ {T \rightarrow \infty} \frac {1}{T} \int_ {0} ^ {T} a (t) b (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} H _ {2} (j \omega) H _ {1} (- j \omega) \left\{\lim  _ {T \rightarrow \infty} \frac {1}{T} I (- j \omega) O (j \omega) \right\} d \omega . \tag {9}
$$

Substituting (8) into (9):

$$
\lim  _ {T \rightarrow \infty} \int_ {0} ^ {T} a (t) b (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} H _ {2} (j \omega) H _ {1} (- j \omega) \phi_ {I O} (j \omega) d \omega . \tag {10}
$$

# Case 1

For the case where

$$
\mathrm {H} _ {1} (\mathrm {j} \omega) = \mathrm {H} _ {2} (\mathrm {j} \omega) = \mathrm {H} (\mathrm {j} \omega)
$$

and defining

$$
\overline {{a (t) b (t)}} \equiv \lim  _ {T \rightarrow \infty} \frac {1}{T} \int_ {0} ^ {T} a (t) b (t) d t,
$$

Eq. (10) becomes

$$
\overline {{a (t) b (t)}} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} H (j \omega) H (- j \omega) \phi_ {I O} (j \omega) d \omega = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H (j \omega) | ^ {2} \phi_ {I O} (j \omega) d \omega . \tag {11}
$$

Since the input and output signals are filtered identically, it should be evident that this operation will yield information only about the in-phase relationship, or the real part of $\phi_{\mathrm{IO}}(\mathrm{j}\omega)$ . We can show this by noting that since

$$
\overline {{a (t) b (t)}} = \overline {{b (t) a (t)}}
$$

and

$$
\overline {{b (t) a (t)}} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H (j \omega) | ^ {2} \phi_ {O I} (j \omega) d \omega , \tag {12}
$$

the two integrals in Eqs. (11) and (12) must be equal; thus

$$
\frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H (j \omega) | ^ {2} \left(\phi_ {O I} (j \omega) - \phi_ {I O} (j \omega)\right) d \omega = 0. \tag {13}
$$

If we assume that $\phi_{\mathrm{IO}}(\mathrm{j}\omega)$ and $\phi_{\mathrm{OI}}(\mathrm{j}\omega)$ do not change much over the effective bandwidth of the filter, then $\phi_{\mathrm{IO}}(\mathrm{j}\omega)$ must equal $\phi_{\mathrm{OI}}(\mathrm{j}\omega)$ . But since

$$
\phi_ {I O} (j \omega) = \phi_ {O I} (- j \omega), \tag {14}
$$

this means that the imaginary part of $\phi_{\mathsf{IO}}(\mathsf{j}\omega)$ must be zero, or at least no information about $\operatorname{Im}[\phi_{\mathsf{IO}}(\mathsf{j}\omega)]$ is present in the output. For case 1, then

$$
\overline {{a (t) b (t)}} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H (j \omega) | ^ {2} \operatorname {R e} \left[ \phi_ {I O} (j \omega) \right] d \omega . \tag {15}
$$

If we assume that $\operatorname{Re}[\phi_{\mathsf{IO}}(\mathsf{j}\omega)]$ does not change much over the effective bandwidth of $\mathsf{H}(\mathsf{j}\omega)$ ,

$$
\overline {{a (t) b (t)}} \approx \left[ \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H (j \omega) | ^ {2} d \omega \right] \left[ R e [ \phi_ {I O} (j \omega) ] \right]. \tag {16}
$$

For the present study, we used a filter with the following transfer function:

$$
\mathrm {H} (\mathrm {j} \omega) = \frac {\mathrm {j} \omega}{\omega_ {\circ} ^ {2} + \mathrm {j} \omega 2 \zeta \omega_ {\circ} - \omega^ {2}}. \tag {17}
$$

The filter "area" term can be evaluated using a table of integrals<sup>14</sup>

$$
\frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | H (j \omega) | ^ {2} d \omega = \frac {1}{4 \zeta_ {0}} (\text {r a d / s e c}). \tag {18}
$$

Thus

$$
\operatorname {R e} \left[ \phi_ {\mathrm {I O}} (\mathrm {j} \omega) \right] \approx 4 \zeta \omega_ {\circ} \overline {{\mathrm {a} (\mathrm {t}) \mathrm {b} (\mathrm {t})}}. \tag {19}
$$

Case 2

For this case

$$
\mathrm {H} _ {\mathbf {l}} (\mathrm {j} \omega) = \frac {\omega}{\mathrm {j} \omega} \mathrm {H} (\mathrm {j} \omega) \tag {20}
$$

and

$$
\mathrm {H} _ {2} (\mathrm {j} \omega) = \mathrm {H} (\mathrm {j} \omega).
$$

Since

$$
\mathrm {H} _ {1} (- \mathrm {j} \omega) = \frac {\omega_ {\circ} \mathrm {H} (- \mathrm {j} \omega)}{- \mathrm {j} \omega}, \tag {21}
$$

Eq. (10) becomes

$$
\overline {{a (t) b (t)}} = \frac {\omega_ {0}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {\mathrm {H} (\mathrm {j} \omega) \mathrm {H} (- \mathrm {j} \omega) \phi_ {\mathrm {I O}} (\mathrm {j} \omega)}{- \mathrm {j} \omega} d \omega \tag {22}
$$

Since the input signal's filter has 90 deg more phase lag than the output signal's filter, we should expect that this operation will yield information only about the quadrature relationship, or the imaginary part of $\phi_{IO}(j\omega)$ . We can show this as follows:

In this case, revising the order of integration of the inputs makes a difference, i.e., from (2)

$$
\int_ {0} ^ {T} b (t) a (t) d t \approx \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} A (j \omega) B (- j \omega) d \omega \tag {23}
$$

we can use (3), (6), (19), and (23) to get

$$
\overline {{b (t) a (t)}} = \frac {\omega_ {0}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {H (j \omega) H (- j \omega)}{j \omega} I (j \omega) O (- j \omega) d \omega . \tag {24}
$$

Again, since $\overline{a(t)b(t)} = \overline{b(t)a(t)}$ , from (22) and (24) we can conclude that

$$
\frac {\phi_ {I O} (j \omega)}{- j \omega} = \frac {\phi_ {O I} (j \omega)}{j \omega} \tag {25}
$$

if we use the same argument as we did for case 1. Thus

$$
\phi_ {I O} (j \omega) = - \phi_ {O I} (j \omega) = - \phi_ {I O} (- j \omega) \tag {26}
$$

which is true only if the real part of $\phi_{\mathsf{IO}} = 0$ , or at least if no information about $\operatorname{Re}[\phi_{\mathsf{IO}}(\mathsf{j}\omega)]$ is present in the output. Hence, we can substitute $\mathsf{jIm}[\phi_{\mathsf{IO}}(\mathsf{j}\omega)]$ in for $\phi_{\mathsf{IO}}(\mathsf{j}\omega)$ in Eq. (22). For case 2, then

$$
\overline {{a (t) b (t)}} = - \frac {\omega_ {0}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {\left| H (j \omega) \right| ^ {2}}{\omega} \operatorname {I m} \left[ \phi_ {I O} (j \omega) \right] d \omega . \tag {27}
$$

If we assume that $\operatorname{Im}[\phi_{\mathsf{IO}}(\mathrm{j}\omega)]$ does not change much over the effective bandwidth of either $\mathsf{H}(\mathsf{j}\omega)$ or $\frac{\omega_0}{\mathsf{j}\omega}\mathsf{H}(\mathsf{j}\omega)$ , then

$$
- 5 4
$$

$$
\overline {{a (t) b (t)}} \approx \left[ - \frac {\omega_ {0}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {\left| H (j \omega) \right| ^ {2}}{\omega} d \omega \right] \left[ I m [ \phi_ {I O} (j \omega) ] \right]. \tag {28}
$$

For the particular filter used (Eq. 17):

$$
\frac {\omega_ {0}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {\left| H (j \omega) \right| ^ {2}}{\omega} d \omega = \frac {1}{4 \zeta \omega_ {0}}. \tag {29}
$$

Thus

$$
\operatorname {I m} \left[ \phi_ {\mathrm {I O}} (\mathrm {j} \omega) \right] \approx - 4 5 \omega_ {\mathrm {o}} \overline {{a (t) b (t)}}. \tag {30}
$$

Case 3

The case where

$$
\mathrm {H} _ {1} (\mathrm {j} \omega) = \mathrm {H} _ {2} (\mathrm {j} \omega) = \frac {\omega_ {\mathrm {O}}}{\mathrm {j} \omega} \mathrm {H} (\mathrm {j} \omega) \tag {31}
$$

can be developed similarly to case 1 as far as Eq. (16), since we could redefine $H(j\omega)$ as being equal to the expression in (31).

The integral to be evaluated is

$$
\frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} H _ {2} (j \omega) H _ {1} (- j \omega) d \omega = \frac {\omega^ {2}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {H (j \omega)}{j \omega} \frac {H (- j \omega)}{- j \omega} d \omega = \frac {\omega^ {2}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {\left| H (j \omega) \right| ^ {2}}{\omega^ {2}} d \omega . \tag {32}
$$

For the filter of Eq. (17), this integral is again equal to $\frac{1}{4\zeta\omega_0}$ , so

$$
\operatorname {R e} \left[ \phi_ {\mathrm {I O}} (\mathrm {j} \omega) \right] \approx 4 \zeta \omega_ {\circ} \overline {{a (t) b (t)}} \tag {33}
$$

assuming in this case, however, that $\operatorname{Re}[\phi_{\mathrm{IO}}(\mathrm{j}\omega)]$ does not change much over the effective bandwidth of $\frac{\omega_0}{\mathrm{j}\omega}\mathrm{H}(\mathrm{j}\omega)$ .

Case 4

The case where

$$
\mathrm {H} _ {1} (\mathrm {j} \omega) = \mathrm {H} (\mathrm {j} \omega), \tag {34}
$$

$$
\mathrm {H} _ {2} (\mathrm {j} \omega) = \frac {\omega_ {\mathrm {O}}}{\mathrm {j} \omega} \mathrm {H} (\mathrm {j} \omega) \tag {35}
$$

can be developed similarly to case 2. Equation (10) becomes

$$
\overline {{a (t) b (t)}} = \frac {\omega_ {0}}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {H (j \omega) H (- j \omega)}{j \omega} \phi_ {I O} (j \omega) d \omega . \tag {36}
$$

The expression on the right hand side is the negative of that for Eq. (22), case 2; hence for case 4, we get the expression corresponding to Eq. (3) when the filter of Eq. (17) is used:

$$
\operatorname {I m} \left[ \phi_ {\mathrm {I O}} (\mathrm {j} \omega) \right] \approx 4 \zeta \omega_ {\circ} \overline {{a (t) b (t)}} \tag {37}
$$

assuming again that $\operatorname{Im}[\phi_{\mathrm{IO}}(\mathrm{j}\omega)]$ does not change much in the effective bandwidths of either $\mathrm{H(j\omega)}$ or $\frac{\omega_0}{\mathrm{j}\omega}\mathrm{H(j\omega)}$ .

The power spectral density (PSD) of the input function is required for calculating the system transfer function $G(j\omega)$ . This is obtained by squaring the outputs of both the in-phase and quadrature filters and integrating the sum of the squares. In both cases, for the filter of Eq. (17):

$$
\phi_ {I I} (j \omega) \approx 4 \zeta \omega_ {0} \overline {{a (t) ^ {2}}} \tag {38}
$$

assuming that $\phi_{\mathrm{II}}(\mathrm{j}\omega)$ does not change much in the effective pass bands of $\mathrm{H}(\mathrm{j}\omega)$ and $\omega_{\circ}\mathrm{H}(\mathrm{j}\omega) / \mathrm{j}\omega$

The system transfer function $G(j\omega)$ is then computed from

$$
G (j \omega) \approx \frac {\operatorname {R e} [ \phi_ {I O} (j \omega) ] + j I m [ \phi_ {I O} (j \omega) ]}{\phi_ {I I} (j \omega)}, \tag {39}
$$

where each of the three terms on the right hand side of (39) are computed using the sum of two estimates. (Note that all terms have the same gain factor, $4\zeta \omega_{0}$ .) The reason for the better accuracy of this method as compared to using a single estimate of each term lies in the fact that since the effective pass-bands of the in-phase and quadrature filters are different, there is a bias in each of the quadrature, or imaginary term, estimates. Since the two imaginary term estimates are of different sign, this bias tends to be cancelled out.

Calculations of the percent standard deviations of both input and output (PSD) estimates are made using (40):15

$$
\% \mathrm{SD} = \frac{100\sigma}{\overline{\mathrm{x}^{2}}} = \frac{100}{\sqrt{\mathrm{BT}}}, \tag{40}
$$

where

$$
\sigma = \text {s t a n d a r d}
$$

$$
\overline {{x ^ {2}}} = \text {m e a n s q u a r e v a l u e},
$$

$$
B = \text {e q u i v a l e n t}
$$

$$
\mathrm {T} = \text {i n t e g r a t i o n}
$$

The equivalent noise bandwidth<sup>16</sup> for the H(jω) filter used in this study is

$$
B = \pi_ {0} ^ {\prime} \omega_ {0}, \text {r a d / s e c .} \tag {41}
$$

The coherence function $\gamma^2$ is also computed:

$$
\gamma^ {2} \equiv \frac {\left| \phi_ {\mathrm {I O}} \right| ^ {2}}{\phi_ {\mathrm {I I}} \phi_ {\mathrm {O O}}} . \tag {42}
$$

The coherence function is useful for estimating expected errors in transfer function calculations when the input and output signals are random.[17] For periodic signals, however, such as the PRBS, the expressions for error estimates in the literature have been found to be wildly pessimistic.

The calculation of the response of the digital filters is based on Paynter's matrix exponential method, $^{18,19}$ and gives virtually exact time-response solutions very efficiently.

# Internal Distribution

1. R. K. Adams   
2. G.M. Adamson   
3. R.G.Affel   
4. L. G. Alexander   
5. R.F.Apple   
6. C. F. Baes   
7. J. M. Baker   
8. M. A. Baker

9-18. S.J.Ball   
19. S. E. Beall   
20. E. S. Bettis   
21. F. F. Blankenship   
22. R. Blumberg   
23. E. G. Bohlmann   
24. C. J. Borkowski   
25. J. B. Bullock   
26. G.H.Burger   
27. 0. W. Burke   
28. S. Cantor   
29. W. L. Carter   
30. G.I.Cathers   
31. E. L. Compere   
32. J. A. Conlin   
33. W.H.Cook   
34. L. T. Corbin   
35. G. A. Cristy   
36. J. L. Crowley   
37. F. L. Culler   
38. R. A. Dandl   
39. H.P.Danforth   
40. D. G. Davis   
41. S. J. Ditto   
42. R. G. Donnelly   
43. F. A. Doss   
44. N. E. Dunwoody   
45. J.R.Engel   
46. E.P.Epler   
47. W. K. Ergen   
48. D. E. Ferguson   
49. A. P. Fraas   
50. H. A. Friedman   
51. D.N.Fry   
52. J. H. Frye, Jr.   
53. C. H. Gabbard   
54. R. B. Gallaher   
55. W. R. Grimes   
56. A. G. Grindell

57. R. H. Guymon   
58. E. W. Hagen   
59. P.H.Harley   
60. C. S. Harrill   
61. P. N. Haubenreich   
62. G.M.Herbert   
63. P. G. Herndon   
64. V. D. Holt   
65. P.P.Holz   
66. T. L. Hudson   
67. P. R. Kasten   
68. R.J.Kedl   
69. M. J. Kelly

70-109. T. W. Kerlin   
110. S. S. Kirslis   
111. D. J. Knowles   
112. A. I. Krakoviak   
113. J. W. Krewson   
114. R.C.Kryter   
115. C. G. Lawson   
116. R.B.Lindauer   
117. M. I. Lundin   
118. R.N.Lyon   
119. J.H.Marable   
120. C. D. Martin   
121. C. E. Mathews   
122. H. G. MacPherson   
123. R.E. MacPherson   
124. H. C. McCurdy   
125. H.F. McDuffie   
126. C. K. McGlothlan   
127. L. E. McNeese   
128. A. J. Miller   
129. R.V.Miskell (Y-12)   
130. W. R. Mixon   
131. R. L. Moore   
132. H. G. O'Brien   
133. P. Patriarca   
134. H. R. Payne   
135. A.M.Perry   
136. H. B. Piper   
137. B. E. Prince   
138. J. L. Redford   
139. M. Richardson   
140: R. C. Robertson   
141. H.C.Roller   
142. D. P. Roux

143. H. C. Savage   
144. A. W. Savolainen   
145. D. Scott   
146. H. E. Seagren   
147. J.H.Shaffer   
148. M. J. Skinner   
149. A. N. Smith   
150. P. G. Smith   
151. W. F. Spencer   
152. I. Spiewak   
153. B. Squires   
154. R.C. Steffy   
155. H.H. Stone   
156. R.S. Stone   
157. A. Taboada   
158. J. R. Tallackson   
159. R.E.Thoma   
160. G.M.Tolson   
161. D. B. Trauger   
162. J. R. Trinko

163. W.C.Ulrich

164. B. H. Webster

165. A.M. Weinberg

166. K.W. West

167. M. E. Whatley

168. J.C. White

169. G. D. Whitman

170. R.E.Whitt

171. H. D. Wills

172. J. V. Wilson

173. L. V. Wilson

174. M. M. Yarosh

175. MSRP Director's Office, Rm. 219, 9204-1

177. Central Research Library

178-179. Y-12 Document Reference Section   
180-184. Laboratory Records Department   
185. Laboratory Records Department, LRDA-RC

# External Distribution

186-200. Division of Technical Information Extension (DTIE)   
201. Research and Development Division, ORO   
202-203. Reactor Division, ORO   
204. S. J. Gage, University of Texas, Austin, Texas   
205. R. P. Gardner, Research Triangle Institute, Durham, N. C.   
206. R.W.Garrison,AEC,Washington,D.C.   
207. S. H. Hanauer, University of Tennessee, Knoxville   
208. P. F. Pasqua, University of Tennessee, Knoxville   
209. J. W. Prados, University of Tennessee, Knoxville   
210. J. C. Robinson, University of Tennessee, Knoxville   
211. R. F. Saxe, North Carolina State University, Raleigh, N. C.   
212. W. L. Smalley, AEC, ORO   
213. S. E. Stephenson, University of Arkansas, Fayetteville, Ark.   
214. R. E. Uhrig, University of Florida, Gainesville, Fla.   
215. Otis Updike, University of Virginia, Charlottesville   
216. A. A. Wasserman, Westinghouse Astronuclear Laboratory, P. O. Box 10864, Pittsburgh, Pa.   
217. M. J. Whitman, AEC, Washington, D. C.