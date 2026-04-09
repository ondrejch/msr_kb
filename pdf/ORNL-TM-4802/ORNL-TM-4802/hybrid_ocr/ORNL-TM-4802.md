# The Molten-Salt Reactor Information System

P. N. Haubenreich

D. W. Cardwell

J. R. Engel

MASTER

![](images/9ef5fa9bdab3263a645512bf755c3fad6efe98d68c21bce1c3fe3fb49df79e62.jpg)

OAK RIDGE NATIONAL LABORATORY

OPERATED BY UNION CARBIDE CORPORATION • FOR THE U.S. ATOMIC ENERGY COMMISSION

Printed in the United States of America. Available from

National Technical Information Service

U.S. Department of Commerce

5285 Port Royal Road, Springfield, Virginia 22161

Price: Printed Copy $5.45; Microfiche $2.25

This report was prepared as an account of work sponsored by the United States Government. Neither the United States nor the Energy Research and Development Administration, nor any of their employees, nor any of their contractors, subcontractors, or their employees, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness or usefulness of any information, apparatus, product or process disclosed, or represents that its use would not infringe privately owned rights.

ORNL-TM-4802

UC-76 - Molten-Salt

Reactor Technology

Contract No. W-7405-eng-26

Reactor Division

THE MOLTEN-SALT REACTOR INFORMATION SYSTEM

P. N. Haubenreich   
D. W. Cardwell   
J. R. Engel

JUNE 1975

This report was prepared as an account of work sponsored by the United States Government. Neither Research and Development Administration, nor any of subcontractors, or their employees, makes any liability or responsibility for the accuracy, completeness process disclosed, or represents that its use would not infringe privately owned rights.

NOTICE: This document contains information of a preliminary nature and was prepared primarily for internal use at the Oak Ridge National Laboratory. It is subject to revision or correction and therefore does not represent a final report.

OAK RIDGE NATIONAL LABORATORY

Oak Ridge, Tennessee 37830

operated by

UNION CARBIDE CORPORATION

for the

U.S. ENERGY RESEARCH AND DEVELOPMENT ADMINISTRATION

![](images/81e3e0de089b15098cfa95ee2df31360903c0bb3870f5b1e2f373a314b06ac2a.jpg)

# CONTENTS

# Abstract 1

1. INTRODUCTION 1   
2. DOCUMENTS AND INFORMATION STORED IN MSRIS 2  
3.SEARCHING THE DATA FILE 6

Searching by Keywords 7   
Subject Categories 8

# 4. PREPARATION OF INFORMATION FOR MSRIS 10

Format for Reference Information 12   
Abstracts 12   
Choice of Keywords 13   
Assignment of Categories and Accession Number 14

# REFERENCES 14

# APPENDIXES 15

Appendix A. MSRIS Keyword List 17  
Appendix B. Subject Categories in MSRIS 30

# Appendix C. Instructions for Use of MSRIS from an Interactive Computer Terminal 33

#

![](images/c36e445d1ca80f4a33038954c4d0ab01bcca34eff089c3967413e5a134254b39.jpg)

P. N. Haubenreich   
D. W. Cardwell   
J. R. Engel

# Abstract

The Molten-Salt Reactor Information System (MSRIS) is a computer-based file of abstracts of documents dealing with the technology of molten-salt reactors. The file is stored in the IBM-360 system at ORNL, and may be searched through the use of established interactive computer programs from remote terminals connected to the computer via telephone lines. The system currently contains 373 entries and is subject to updating and expansion as additional information is developed.

This document describes the nature and general content of the data file, a general approach for obtaining information from it, and the manner in which material is added to the file. Appendixes provide the list of keywords currently in use, the subject categories under which information is filed, and simplified procedures for searching the file from remote terminals.

# 1. INTRODUCTION

Nuclear reactors in which the fissile and fertile materials are incorporated in molten-salt mixtures offer a route to long-term, economical power that is both promising and distinctly different from other reactors now being built and developed. Molten-salt reactor technology is not new, having its beginnings in the aircraft reactor program in 1947. Thus, there exists a considerable store of information which has been built up over the years.<sup>1</sup> During most of this time, a formal system for information retrieval was unnecessary, because the preponderance of the work on MSR technology was done at one site (the Oak Ridge National Laboratory), within a closely knit project organization. As other organizations began to participate in this activity a need was created that the MSRIS was designed to meet.

The MSRIS is intended to contain an up-to-date and readily accessible file of abstracts of selected documents dealing with all aspects of molten-salt reactor technology. The purpose is to help searchers find the information they seek by quickly identifying the documents that contain the desired information and by displaying brief abstracts so the searchers can decide which documents they need to read. The abstracts are stored in the IBM-360 computer system at ORNL and various remote terminals can be used for search instructions and output.*

The original data file was established over a period of time in 1971 and 1972 from information that was then available; an indexed compilation<sup>2</sup> of the first 321 entries was published in 1971. Subsequent additions raised the total number of entries to 373. This work was stopped when the entire MSR program was discontinued early in 1973. With the reactivation of the program (in 1974), the MSRIS was restored to its prior condition. It is anticipated that the data file will be gradually updated and then kept current as this program continues.

The sections which follow describe the kinds of documents and information that are included in the MSRIS, general procedures for retrieving information, and how the abstracts are prepared and indexed. Appendixes provide the list of keywords, the subject categories, and detailed computer procedures.

# 2. DOCUMENTS AND INFORMATION STORED IN MSRIS

The kinds of documents included in the MSRIS are all those that are generally available to the public. This includes ORNL reports (ORNL-xxxxx) and technical memoranda (ORNL-TM-xxxxx) and similar reports from other sites. Letters and internal correspondence (even though assigned an MSR memo number) are not included. No ORNL-CF memo is included unless it contains information of wide interest which is not otherwise available. (There are some older ORNL-CF memos like this; if a forthcoming ORNL-CF memo seems to fit this description, consideration should be given to putting out the information in a more accessible form.) Books, journal

articles, papers given at meetings for which reprints were made available; all are subject to inclusion in MSRIS.

Although its spectrum of documents is quite broad, the MSRIS is by no means intended to include every single document published on molten salts or even on molten-salt reactors.* Selection of documents from among those published prior to 1971 was by a panel of experts from all parts of the molten-salt reactor program at ORNL. The criterion was that the chosen documents give an adequate description of all significant developments at least as far back as the initiation of the MSRE design in 1960. All externally available documents originating in the molten-salt reactor program at ORNL since 1970 are to be routinely abstracted by the authors and then filed in the MSRIS. The staff of the MSRIS (all part-time) may also abstract significant public documents originating elsewhere and add them to the MSRIS file.

The information that is stored in MSRIS for each document is illustrated by Fig. 1 which is a reproduction of a complete entry for one report as it was retrieved from the file. Numbers have been added to identify the seven information fields that are actually used in MSRIS and to provide a key to the description of these fields below. It may be noted that three additional labels - <AUTHSHIP>, <REFERENCE>, and <KEYTERMS> - appear on the illustration; these identify groups, or subsets, of information fields. Use of one of these expressions (or its abbreviation) causes the computer to deal with all of the information fields in that subset.

1. <HEADER >: This field provides an explicit identification for every document or entry in the file, as well as some very general information about the document itself. The first three characters (alphabetic) define the primary category** into which the material contained in the document falls. This is the category which best describes the main thrust of the document, the greatest proportion of its content, or the purpose

321

1 <HEADER >MCD700019 <AUTHSHIP>   
2 <AUTHOR >Engel, J.R.; Haubenreich, P.N.; Houtzeel, A.   
3 <TITLE >SPRAY, MIST, BUBBLEs, AND FOAM IN THE MOLTEN-SALT REACTOR EXPERIMENT <REFERENCE>   
4. <PUB DESC>Oak Ridge National Laboratory, Tenn. ORNL-TM-3027 (June 1970), 102 p, 33 fig, 65 ref.  
<KEYTERMS>   
5 <SUBJ CAT>MCD; MDB; KAB   
6 <KEYWORDS> *analysis; *experience; *MSRE; *operation; beryllium; bubbles; corrosion products; density; foaming; gas injection; interfacial tension; liquid level measurement; mists; off-gas systems; physical properties; pumps; sprays; void fractions; primary system   
7 In the fuel pump bowl $50\mathrm{~gpm}$ of salt was sprayed through the cover gas and into the salt pool. Effects included not only the intended xenon stripping but several others which became the subject of investigations reported here. The spray produced a mist of salt droplets, some of which drifted into the off-gas line at a rate of a few grams per month. The resultant salt deposits required cleanout at intervals of six months to a year. The stripper jets also drove bubbles several inches into the salt pool, reducing the average density and raising the actual level above that indicated by the bubbler level elements. Some salt transferred into the overflow line, apparently as froth although there was no evidence of persistent foam. Most of the bubbles driven into the salt returned to the surface, but a small fraction was drawn into the circulating loop. The situation was such that small changes in pump speed or physical properties of the salt changed the depth of the bubble zone enough to change the volume fraction of gas in the loop over the range from $0.02\%$ to $0.7\%$ .

Fig. 1. Example of MSRIS entry.

for which it was written. Since the content of a document frequently does not fit completely into any one category, other categories may be listed elsewhere in the entry (see below). The remainder of the header consists of a 6-digit number that identifies the entry. The first two digits identify the year of publication and the last four are assigned serially to entries of that year as they are added to the MSRIS file. Topical reports normally are treated in only one entry; however, reports covering a variety of subjects, such as MSRP semiannual progress reports, may have an entry for each of the several subjects covered. In such cases the header for each entry has both a different primary category and a different identifying number. In addition to the header identification, each individual entry is assigned a simple sequential number (beginning with 1) to identify its position in the data file. Thus, the document used in the example for Fig. 1 is number 321 in the data set.   
2. <AUTHOR>: The "author" field is one of several fields in a subset that carries the generic title of "authorship" or, in computer terminology, <AUTHHSHIP>. Since author is the only member of this subset used in MSRIS, either designation could be used. This field contains the names of all authors, where they are explicitly identified. Where individual authors are not identified, as in the case of MSRIP semiannual progress reports, the expression "(Staff Report)" is entered in the author field.   
3. <TITLE>: This is a unique field label, and the field contains the full title of the document as it appears on the published version. Section titles are used along with the document title for progress reports.   
4. <PUB DESC>: The "publication description" is a member of the subset of fields containing reference information, <REFERENCE>. Again, only one member of the subset is used in MSRIS. This field contains the name of the organization that originated the document, the document number, its publication date, and some indication of its size and breadth of scope (numbers of pages, figures, and references).   
5. <SUBJ CAT>: The "subject category" is one of two fields used in MSRIS out of the subset generically identified as <KEYTERMS>. This field contains, first, the primary category (from the "header"), and then any other categories to which the document may have been assigned.

6. <KEYWORDS>: This field is the other member of the "keyterms" that appear in the file. The most important, or most relevant, keywords appear at the beginning of the field, and each is preceded by an asterisk (*). All of the keywords that appear in the file were selected from the list given in Appendix A; however, some of the keywords in that list may not yet have been used. The list is subject to revision as the information file expands.

7. <ABSTRACT>: This field contains the text of the document abstract. Often it is the same abstract that appears at the beginning of the document itself, but this is not a requirement.

# 3. SEARCHING THE DATA FILE

The MSRIS file is stored in the memory of the IBM-360 computer system at the Oak Ridge National Laboratory. Also stored there are the programs that are needed for searching the file. Wide access is provided through various kinds of remote terminals, including Teletype, IBM-2741, and NOVAR terminals, which can be connected through the telephone system to ORNL's IBM-360/75. The file may be used freely by ORNL staff members and outside organizations who have access to the ORNL computing facilities.

The MSRIS file is only one of many (32 at the present time) in the ORNL computer that can be searched by the ORLOOK program. This program was designed to be quite versatile, providing many options for searching these files, and, in fact, is so versatile that learning to exercise all of its potential would require considerable time. We believe, however, that the needs of most users of the MSRIS will be satisfied by a few options that are relatively simple to learn to use. A discussion of the equipment and programs and step-by-step procedures for using them with MSRIS are given in Appnedix C. Additional details may be found in Ref. 3. That which follows is a discussion of the basic logic and general procedures that are involved.

If one wishes to sift the file to find all records on a chosen subject, the best way is by subject category, by keywords, or by some

combination of the two. Of course, if one is looking for a specific reference and has some clue, such as the name of one of the author or the report number, these can be used to narrow and speed his search.

# Searching by Keywords

The current list of keywords for MSRIS is given in Appendix A. A few have not yet been used and so do not appear as keywords in the computer file. Others may appear in many separate records. (The ORLOOK program refers to the filed material for each document as a "record".) At the moment there are 373 records in the MSRIS file.

A searcher could select one keyword that most nearly identifies the subject in which he is interested, and look at all records having that keyword. But usually a single keyword fetches more records than a person may have time to examine. So one narrows the search by specifying more than one keyword. There is more than one way to go about this. One could start by selecting a set of several keywords that he feels should define precisely what he is interested in, and retrieve only those records that include among their keywords all those in the specified set. The other way would be to narrow the file in stages; first to those records having the one or two most important keywords; then, from among these, the records having the next most significant keyword; and so on. Finally, the file would either be narrowed to the specific subject of interest or contain so few records that the searcher could afford to have them all displayed for his examination. (The conversational program tells the searcher how many records he is dealing with at each stage in his search.) The first way is quicker, but runs the risk of omitting some records that may be of interest, but might not have been given every one of the keywords in the searcher's set. (When searching one should remember the human element; that is, that the person who assigned keywords to the document inevitably viewed it from a standpoint different from that of the searcher.)

Sometimes it may prove useful to use the option of discriminating against documents having some keyword or other feature. For example, it may be desirable to examine all pertinent records other than progress reports. This procedure is also explained in Appendix C.

# Subject Categories

The subject category system is like a set of 14 large file boxes, each containing several smaller boxes in which the records are stored.* The 14 large boxes correspond to the 14 broad areas or first-order categories listed in Table 1. As shown in Appendix B, all but two (D and N) are further subdivided.

Table 1. MSRIS first-order categories  

<table><tr><td>Category</td><td>Subject</td></tr><tr><td>A</td><td>Molten-salt reactor programs</td></tr><tr><td>B</td><td>Reactor analysis</td></tr><tr><td>C</td><td>Reactor chemistry</td></tr><tr><td>D</td><td>Analytical chemistry</td></tr><tr><td>E</td><td>Graphite</td></tr><tr><td>F</td><td>Hastelloy N and related alloys</td></tr><tr><td>G</td><td>Materials other than Hastelloy N and graphite</td></tr><tr><td>H</td><td>Reactor component development</td></tr><tr><td>I</td><td>Reactor design</td></tr><tr><td>J</td><td>Instrumentation and controls</td></tr><tr><td>K</td><td>Operation and maintenance</td></tr><tr><td>L</td><td>Fuel preparation and processing</td></tr><tr><td>M</td><td>MSRE</td></tr><tr><td>N</td><td>Miscellaneous</td></tr></table>

The way the subject category system works is illustrated in Fig. 2, which is a schematic representation of a portion of the category M file. The outer box encompasses all documents dealing to any significant extent with any aspect of the MSRE. A document that is essentially a review of all aspects of the MSRE would be tagged with the designation MXX and be put into a box with all other comprehensive documents having this tag.\*\*

ORNL-DWG75-3242

M. MSRE

MXX

documents comprehensively treating MSRE:

MA. MSRE Design

MAX

documents comprehensively treating design of MSRE

MAA

MSRE Plant Design

MAB

MSRE Major Comp. Design

AE

MSRE Aux. Comp. Design

MB. MSRE Construction

MBX

MBA

MBB

Fig. 2. Schematic representation of a portion of the MSRIS category system of filing.

Documents dealing with MSRE design go into box MA. Those covering design of many or all parts of the MSRE are tagged MAX and go into the box so designated. Documents dealing only with the design of specific parts of the MSRE are tagged MAA, MAB, etc., as appropriate, and go into separate boxes. Documents on MSRE construction, operation, etc., are similarly sorted.

# 4. PREPARATION OF INFORMATION FOR MSRIS

For each document that is to be included in MSRIS, the required information is assembled in the form shown in Fig. 3. The material is, in many respects, the same as that discussed earlier in the description of a representative entry, but it has been rearranged to facilitate its preparation. Whenever possible, this information is supplied to the MSRIS staff by one of the authors when the document is published. Preparation of the computer entry and insertion into the data file then follow routinely. The following discussion of the information items is keyed to the numbers beside the example in Fig. 3.

1. **Authors:** List all authors, last names first, initials, no punctuation except +.   
2. Title: Give the complete title as on the published document.   
3. Originating organization: Use a brief form of the name, but do not abbreviate to the point of being cryptic; for ORNL, use the form shown.   
4. Reference information: Generally this includes document identification, date of publication, and number of pages, figures and references. Formats for various kinds of documents are illustrated below.   
5. Abstract: Guidelines for abstracting are given below.   
6. Keywords: These are to be selected from the MSRIS Keyword List in Appendix A.   
7. Proposed keywords: If an author or abstracter feels that a keyword is needed which is not in the MSRIS Keyword List, he should list it on a separate line for consideration when the list is next revised.

Key to text

Example

Fig. 3. Example of form in which abstracts are submitted for the molten-salt reactor information system.   

<table><tr><td>1</td><td>Engel JR + Haubenreich PN + Houtzeel A</td></tr><tr><td>2</td><td>SPRAY, MIST, BUBBLEs, AND FOAM IN THE MOLTEN-SALT REACTOR EXPERIMENT</td></tr><tr><td>3</td><td>Oak Ridge National Laboratory, Tenn.</td></tr><tr><td>4</td><td>ORNL-TM-3027 (June 1970), 102 p, 33 fig, 65 ref.</td></tr><tr><td>5</td><td>In the fuel pump bowl 50 gpm of salt was sprayed through the cover gas and into the salt pool. Effects included not only the intended xenon stripping but several others which became the subject of investigations reported here. The spray produced a mist of salt droplets, some of which drifted into the offgas line at a rate of a few grams per month. The resultant salt deposits required cleanout at intervals of six months to a year. The stripper jets also drove bubbles several inches into the salt pool, reducing the average density and raising the actual level above that indicated by the bubbler level elements. Some salt transferred into the overflow line, apparently as froth although there was no evidence of persistent foam. Most of the bubbles driven into the salt returned to the surface, but a small fraction was drawn into the circulating loop. The situation was such that small changes in pump speed or physical properties of the salt changed the depth of the bubble zone enough to change the volume fraction of gas in the loop over the range from 0.02% to 0.7%.</td></tr><tr><td>6</td><td>*analysis + *experience + *MSRE + *operation + beryllium + bubbles + corrosion products + density + foaming + fused salts + gas injection + interfacial tension + liquid level measurement + mists + off-gas systems + physical properties + pumps + sprays + void fractions + primary systems</td></tr><tr><td>7</td><td>overflow</td></tr></table>

# Format for Reference Information

The "reference" line (item 4 in Fig. 3) not only gives the information needed to locate or to order the document, but also gives clues as to how "meaty" it is (how many pages, figures, and references are included). Examples of reference lines for various kinds of documents follow:

# USAEC report

ORNL-4233 (Feb. 1968), 60 p, 24 fig, 25 ref.

# Other reports

AECL-3293 (Mar. 1969), 30 p, 15 fig, 18 ref.

US Govt. Printing Office (Jan. 1970), 138 p, 59 fig, 23 ref.

Edison Electric Institute Publication No. 70-30 (Apr. 70), 53 p, 12 fig, 5 ref.

Unnumbered report (Aug. 1970), 113 p, 41 fig.

# Journal and magazine articles

Nucl. Appl. Tech. 8, 118 (Feb. 1970), 18 p, 6 fig, 16 ref.

Nucl. Engrg. International 14 (155) 325 (Apr. 1970), 5 p, 3 fig.

# Conference papers

Preprint of Paper 103, 1970 Am. Power Conf., Chicago, Apr. 20-23, 1970, 14 p, 3 fig, 11 ref.

# Abstracts

An abstract may be "indicative" or "informative" or a combination. A purely indicative abstract simply lists or describes the contents of a document, the aim being to do so sufficiently well for a reader of the abstract to decide whether or not to take the time to look at the document itself. An informative abstract, in principle, conveys the major factual results of the document in sufficient detail that most readers would not find it necessary to examine the document itself. Insofar as

is practical, abstracts for the MSRIS are informative. Numbers that require lengthy explanation and qualifications to be meaningful (fuel-cycle costs, for example) are avoided, however. Some documents, such as progress reports and review articles, which cover a wide range of topics, lend themselves only to indicative abstracts. In most other cases, an actual abstract will probably tend to be a combination of indicative and informative.

Whether indicative or informative, the abstract should be written clearly and concisely so as to be quick and easy to read. There is no fixed limit on MSRIS abstracts, but few should exceed about 200 words in length. Having all abstracts as succinct as possible is a great advantage to the user of the file; great enough to warrant special efforts on the part of the writer. In writing an abstract, one should first of all jot down the items of information that he wants to include. Then he should draft the abstract, using direct, concise sentences. Next the writers should edit his draft to eliminate superfluous words and, if necessary, selectively cut the content to get the length down to about 200 words. Finally, he should critically reread his abstract to make sure that each sentence is still complete and clear and that the most important information is still included.

# Choice of Keywords

The MSRIS is intended to help anyone seeking information on a chosen subject to find abstracts of all documents containing information pertinent to that subject. Without any knowledge of report titles, authors' names or the like, he should be able to pull the right abstracts from among a multitude of others and be confident that he has not missed any essential information. The keyword index is a mechanism designed to facilitate this.

Each entry in the MSRIS includes a set of keywords chosen from the MSR Keyword List which appears in Appendix A.* In assigning keywords to a

document, the reviewer or author should ask himself, "If a user wanted this particular abstract, under what set of keywords would he ask the computer to search?" As many keywords may be used as is necessary to fully define the contents of the document. (This varies widely, averaging roughly a dozen.)

The person preparing an MSRIS entry may list keywords in any order, but should place an asterisk immediately before each of the most important keywords. When the computer input is prepared, these will be placed at the head of the list so they can be seen at first glance.

# Assignment of Categories and Accession Number

In addition to the information shown in Fig. 3, each entry in the MSRIS file contains an accession number and category identification. The accession number follows routinely from the publication date of the document and its order of processing. The categories are assigned by the MSRIS staff on the basis of suggestions made by the abstractor of the document. Suggestions should be provided both for the primary and any other categories that may be appropriate.

# REFERENCES

1. M. W. Rosenthal, P. R. Kasten, and R. B. Briggs, "Molten-Salt Reactors - History, Status, and Potential," Nucl. Appl. Tech., 8, 107 (1970).   
2. D. W. Cardwell and P. N. Haubenreich, Indexed Abstracts of Selected References on Molten-Salt Reactor Technology, ORNL-TM-3595 (December 1971).   
3. V. A. Singletary, An On-Line Conversational Retrieval System for ORCHIS Text-Oriented Data Bases, User's Manual, ORNL-4951 (April 1974).

APPENDIXES

![](images/7c8279ad0564a392c8ee5fac2f34946aaf736d5d2410329a1b80da280b45e37f.jpg)

# Appendix A

# MSRISKEYWORDLIST

This list contains 544 keywords that abstractors for MSRIS can use. Interspersed in the list are notes directing anyone with other words in mind to equivalent or related keywords that can be used. An amended list will be issued if significant additions or changes are made.

# A

absorbers

absorption

accidents

acids

actinides

administration

adsorption

AEC

afterheat

aging

air

(for Aircraft Reactor Experiment use ARE)

alloy composition

alloys

aluminum

(for amplifiers use electronics)

analog systems

analysis

analytical chemistry

antimony

applications

architect-engineering

ARE

# argon

(for ASME codes use construction codes)

# B

barium

batch processing

bearings

behavior

(for bending strength use flexural properties)

beryllium

beryllium fluoride

beryllium oxide

beta decay

bibliographies

(for biological effects use health physics)

(for biological shielding use shielding)

bismuth

blanket

blowers

(for boilers use steam generators)

boiling

borates

borides

boron

boron trifluoride

(for braze alloys use brazing)

brazing

(for breeder reactors use IMFBR or MSBR)

(for breeding gain use breeding performance)

breeding performance

(for breeding ratio use breeding performance)

bromides

bromine

Brookhaven National Laboratory

bubbles

budgets

(for buildings use structures)

(for burnable poison use reactivity)

burnout

turnup

# C

cadmium

calcium

calculations

capacity

capital costs

capital equipment

capsules

capture

carbides

carbon

(for carbon tetrafluoride use fluorocarbons)

carbonates

carriers

casting

catalysts

(for cavitation use fluid flow)

cells

(for centrifugal pumps use pumps)

ceramics

(for cerium use rare earths)

cermets

certification

cesium

(for $\mathrm{CF_4}$ use fluorocarbons)

charcoal

(for charcoal beds use absorbers)

chemical properties

chemical reactions

chemistry

chlorides

chlorine

chromium

(for chromium fluoride use corrosion products)

circulation

(forcircuits useelectricalcircuits)

cleaning

closures

coatings

cobalt

(for codes use construction codes or computer codes)

coke

(for columbium use niboium)

columns

compatibility

components

compressive properties

compressors

computer codes

computers

concentration

conceptual design

condensers

(for conductivity use electrical conductivity or thermal conductivity)

conferences

(for confinement use containment)

(for conservation use natural resources)

(for conservation coefficient use breeding performance)

construction

construction codes

contactors

containers

containment

contamination

contracts

control

control-rod drives

control rods

(for convection use thermal convection)

converters

coolant loops

coolants

cooling

cooling towers

copper

cores

corrosion

corrosion products

corrosion protection

costs

cover gas

cracks

cranes

creep

(for crevice corrosion use corrosion)

(for critical assemblies use neutron physics)

criticality

cross sections

crystallization

cutting tools

# D

data

data acquisition systems

data processing

deaerators

decay

(for decay heat use afterheat)

decommissioning

decomposition

decontamination

defects

(for degassing use gas separation)

```txt
delayed neutrons   
density   
deposition   
description   
design   
design criteria   
design data   
development   
diagrams   
diffusion (for digital computer use computers)   
disconnects   
dismantling   
dispersions   
disposal   
dissolving   
distillation   
distribution   
disturbances (for doppler effect use reactivity) (for doubling time use breeding performance)   
drain tanks   
drying   
ductility (for duplex tubing use tubing) (for dye-penetrant inspection use inspection)   
dynamic characteristics   
dynamics tests 
```

# E

```txt
earthquakes economics 
```

```txt
efficiency   
elasticity   
electrical circuits   
electrical conductivity   
electrical system   
electrical insulation   
electrical power   
electrical properties   
electrolysis (for electrolytes use electrolysis) (for electrolytic cells use electrolysis) (for electromagnetic pumps use pumps)   
electronics   
electrons   
embrittlement   
emergency cooling   
emission   
energy   
engineered safeguards   
engineering   
enriched materials   
enrichment (for enthalpy use thermodynamics)   
entrainment (for entropy use thermodynamics)   
environment   
epithermal neutrons (for equations use models)   
equilibrium   
equipment   
erosion   
errors 
```

(for eta use neutron yield)

Euratom

evaporation

examinations

excursions

expansion

experience

experiment

(for explosion use safety)

extraction columns

extrusion

# F

fabrication

failures

fast neutrons

fatigue

feedback

(for feedwater heaters use steam systems or components)

ferroalloys

fertile materials

films

filters

filtration

(for fire hazard use safety)

fissile materials

fission

(for fission chambers use instrumentation)

fission neutrons

fission products

fittings

flanges

(for flaws use defects)

flexural properties

flooding

flow measurement

(for flowmeters use flow measurement)

flowsheets

fluid flow

fluids

fluorides

fluorination

fluorine

fluoroborates

fluorocarbons

(for fluxes use neutron flux or brazing)

foaming

foreign

forming

freeze flanges

freeze valves

freezing

(for freezing point use solidus)

(for frequency response use dynamic characteristics)

(for friction factors use fluid flow)

(for frozen walls use corrosion protection)

fuel cycle

fuel cycle costs

fuel preparation

(for fuel processing use processing)

fuels

furnaces

(for furnace brazing use brazing

(for fused salts use molten salts)

# G

gages

(for gain

use breeding performance)

(for gamma heating

use radiation heating)

gamma radiation

(for gamma radiography use inspection)

gamma sources

gamma spectrometry

gas analysis

gas flow

gas injection

gas separation

gases

(for gaskets

use closures)

generators

germanium

glass

gold

(for grain boundaries use microstructure)

(for grain density use microstructure)

(for grain orientation use microstructure)

(for grain size use microstructure)

graphite

(for graphite moderator use graphite)

(for greases use lubrication)

# H

hafnium

halogens

handling

hardness

Hastelloy N

(for hazards use safety)

(for health hazards use safety)

health physics

heat

heat balance

(for heat capacity use specific heat)

heat exchangers

heat generation

heat transfer

heat treatments

heaters

helium

(for Henry's law use solubility)

(for high-temperature gas-cooled reactor use HTGR)

holdup

hot cells

HTGR

hydrates

hydraulics

hydrocarbons

hydrodynamics

hydrofluorination

hydrogen

hydrogen compounds

(for hydrostatic tests

use testing)

hydroxides

# I

IAEA

impact strength

impregnation

impurities

incidents

(for in-core instruments

use instrumentation)

inclusions

inconels

industrial development

industrial studies

industry

inert gases

(for inhibitor

use corrosion protection)

(for INOR-8

use Hastelloy N)

in-pile tests

inspection

instrumentation

(for instruments

use instrumentation)

(for insulation

use electrical insulation or

thermal insulation)

interactions

interfacial tension

(for intergranular corrosion use corrosion)

(for International Atomic Energy Agency use IAEA)

intrusion

inventories

iodides

iodine

ion exchange

ionization

ions

iron

iron alloys

iron compounds

(for iron fluoride

use corrosion products)

irradiation

isotopes

# J

jigs

joints

# K

kinetic equations

krypton

# L

laboratory equipment

(for laminar flow

use fluid flow)

lattice

layout

lead

lead cooling

lead detectors

leak testing

leakage

leaks

(for light-water breeder reactor use LWBR)

limits

linings

liquid level measurement

(for liquid metal-cooled fast breeder reactor use LMFBR)

(for liquid metal-fuel reactor use LMFBR)

liquid metals

liquids

liquidus

lithium

lithium chloride

lithium fluoride

LMFBR

LMR

loading

load factor

loop

losses

(for lubricants use lubrication)

lubrication

LWBR

# M

machining

magnetic properties

maintenance

manganese

manipulators

mass transfer

materials

materials testing

mathematics

measurement

mechanical properties

mechanics

melting

(for melting point use liquidus)

membranes

mercury

metal transfer process

metallography

metallurgy

metals

methods

microprobe

microstructure

mists

mixer-settlers

mixing

mixtures

models

moderators

modified Hastelloy N

modular design

(for modulus of elasticity use elasticity)

molecular weights

molten salts

(for Molten-Salt Breeder Experiment use MSBE)

(for Molten-Salt Breeder Reactor use MSBR)

(for Molten-Salt Reactor Experiment use MSRE)

```txt
(for Molten-Salt Reactor Program use MSRP)   
molybdenum (for molybdenum fluoride use corrosion products)   
monitors   
MSBE   
MSBR   
MSBR Associates   
molten-salt group   
MSRE   
MSRP 
```

# N

(for NaF use sodium fluoride) (for $\mathrm{NaBF_4}$ or $\mathrm{NaBF_4 - NaF}$ use fluoroborates)   
NaK (for natural convection use thermal convection)   
natural resources   
neptunium   
neutron fluence   
neutron flux (for neutron heating use radiation heating)   
neutron physics   
neutron sources   
neutron spectra   
neutron yield   
nickel   
nickel alloys (for nickel fluoride use corrosion products)   
niobium   
nitrates   
nitrogen

```txt
noble metals  
noise analysis  
nuclear analysis  
nuclear reactions 
```

# 0

```txt
off-gas systems (for on-line computers use computers) 
```

```txt
operating costs 
```

```txt
operation 
```

```txt
operators 
```

```txt
optics 
```

```txt
optimizations 
```

```txt
(for ore   
use natural resources)   
organics   
oxidation   
oxide precipitation proces   
oxides   
oxygen 
```

# P

```txt
parametric studies (for passivation use corrosion protection)   
performance (for periscopes use viewing devices)   
phase equilibria   
physical properties   
pilot plants   
piping   
plans   
plant   
plutonium   
plutonium fluorides 
```

```txt
(for poisoning (neutron) use reactivity)   
potassium   
potassium fluorides (for power use electrical power or thermal power)   
power costs   
power measurement   
precipitation   
pressure   
pressure vessels   
primary salt   
primary system   
procedures   
processing   
procurement   
production   
progress report   
protactinium   
protactinium fluorides   
prototypes   
pumps (for purchasing use procurement)   
pyrocarbon 
```

```txt
Q  
qualifications  
quality assurance  
quenching 
```

```txt
R radiation damage radiation heating 
```

```txt
radiation measurement (for radioactive wastes use wastes)   
radioactivity (for radiography use inspection)   
radiolysis (for Rankine cycle use steam cycle)   
rare earths   
rare gases (for rates use reaction rates)   
reaction rates   
reactivity (for reactor core use core)   
reactors   
reactor vessel   
recombination   
reduction   
reductive extraction process   
refractory metals (for regulating rod use control rods)   
reliability   
remote maintenance   
remote welding   
replacement   
research (for resources use natural resources)   
reviews (for Reynolds number use fluid flow) (for rod drives use control-rod drives) 
```

rupture

(for rupture life use creep)

(for ruthenium use noble metals)

# S

safety

safety limits

(for safety rods use control rods)

(for samarium use rare earths)

samplers

sampling

schedules

sealing

seals

secondary salts

secondary systems

separations

shielding

(for shim rods use control rods)

shrinkage

simulation

single-fluid reactors

sites

siting

sodium

sodium fluoride

(for sodium fluoroborate use fluoroborates)

solidus

solvability

solvents

(for sources

use gamma sources or heat sources or neutron sources)

sparging

specific heat

specific inventory

specifications

spectrophotometry

spheres

sprays

stability

stacks

stainless steels

standards

startup

statistics

steam cycle

steam generators

steam systems

storage

stress

(for stress corrosion use corrosion)

(for stress cycling use fatigue)

stress rupture

strontium

structures

sulfur

(for supercritical water use steam cycle)

surface tension

surveillance

systems

# T

```txt
tantalum (for techniques use methods) (for television use viewing devices) (for tellurium use noble metals) (for temperature coefficient of reactivity use reactivity)   
temperature measurement (for Tennessee Valley Authority; use TVA   
tensile properties   
test facilities   
testing   
theory   
thermal conductivity   
thermal convection   
thermal effects   
thermal insulation   
thermal neutrons   
thermal power   
thermal properties   
thermal shield   
thermal shock (for thermocouples use temperature measurements)   
thermodynamics (for thermometry use temperature measurement)   
thorium   
thorium fluorides   
titanium (for titanium additions use alloy composition) 
```

```txt
tools (for toughness use impact strength)   
tracers   
training   
tritium   
tubing   
tungsten   
turbines (for turbogenerators use turbines) (for turbulent flow use fluid flow)   
TVA   
two-fluid reactor 
```

```txt
U (for ultimate strength use tensile properties) (for ultrasonic inspection use inspection) uranium uranium fluorides uranium-232 uranium-233 uranium-235 (for U. S. Atomic Energy commission use AEC) utilities 
```

```txt
V (for vacuum distillation use distillation) valves vapor pressure vibration 
```

```txt
viewing devices viscosity  
void fractions  
volatility  
volume fractions 
```

# W

```txt
wastage  
waste disposal  
wastes  
water  
weigh cell  
welding  
wetting 
```

# X

```txt
xenon x-rays 
```

# Y

```txt
(for yield strength use tensile properties) 
```

# Z

```txt
zirconium zirconium fluoride 
```

# Appendix B

# SUBJECT CATEGORIES IN MSRIS

This list presents the current set of subject categories to be used for documents abstracted in MSRIS.

A Molten-Salt Reactor Programs

AA MSRP - Plans and Organizations

AB MSRP - Technical Summaries

AC MSRP - Progress Reports

ACA MSRE

ACB Large MSRs

ACC Salt Processing

ACD Chemistry

ACE Materials

AD MSR Activities Outside MSRP

B Reactor Analysis

BA Nuclear Data

BB Static Neutronics

BC Dynamics

BD Thermal Effects

BE Activation, Radiation and Shielding

BF Fuel Cycle and Economics

BG Safety

BH Computer Programs

C Reactor Chemistry

CA Phase Relations

CB Thermodynamics and Equilibria

CC Rates and Diffusion

CE Corrosion Reactions

CF Fission Product Behavior

CG Tritium Behavior

CH Oxide Behavior

CI Crystal Studies

CJ Surface Effects

CK Electrochemistry

CL Radiolysis

D Analytical Chemistry

E Graphite

EA Fabrication

EB Unirradiated Properties

EC Irradiation Effects

ED Applications

F Hastelloy N and Related Alloys

FA Alloys Leading to Hastelloy N

FB Standard Hastelloy N

FBA Microstructure

FBB Fabrication

FBC Mechanical and Physical Properties

FBD Corrosion

FBE Radiation Damage

FC Modified Hastelloy N

FCA Microstructure

FCB Fabrication

FCC Mechanical and Physical Properties

FCD Corrosion

FCE Radiation Damage

G Materials Other Than Hastelloy N and Graphite

GA Stainless Steels

GB Steels other than Stainless

GC Nickel and Ni-Base Alloys other than Hastelloy N

GD Molybdenum and Mo-Base Alloys

GE Brazing Alloys

GF Other Metals

GG Nuclear Control Materials

H Reactor Component Development

HA Core

HB Pumps

HC Heat Exchangers

HD Steam Generators

HE Gas Injection and Removal

HF Valves

HFA Freeze Valves

HFB Mechanical Valves

HG Flanges

HH Heaters

HI Other Components

I Reactor Design

IA Reactor Plant

IAA Early Molten-Salt Reactors

IAB MSRE

IAC One-Fluid MSBR (Reference Design)

IAD Other Themal Molten-Salt Reactors

IAE MSBE

IAF Fast and Epithermal Molten-Salt Reactors

IB Systems

IBA Fuel

IBB Coolant

IBC Steam

IBD Gas

IBE Containment

J Instrumentation and Controls

JA General

JAA Instrument Development

JAB Plant Control

JB Nuclear Control and Plant Safety

JC Process

JD Radiation and Contamination Monitoring

JE Data Collection and Analysis

JF Communication and Surveillance

JG Electrical and Pneumatic Systems

K Operation and Maintenance

KA Operation

KAA ARE

KAB MSRE

KAC Other Molten-Salt Systems

KB Maintenance

KBA MSRE Maintenance

KBB Other Molten-Salt and Radioactive Systems

L Fuel Preparation and Processing

LA Salt Procurement and Preparation   
LB Fluorination   
LC Distillation  
LCA Experimental Basis  
LCB Engineering Development  
LCC Operating Experience   
LD Reductive Extraction  
LDA Experimental Basis  
LDB Engineering Development   
LE Metal Transfer  
LEA Experimental Basis  
LEB Engineering Development   
LF Oxide Precipitation LFA Experimental Basis LFB Engineering Development   
LG Adsorption and Reduction   
LH Salt Purification   
LI MSRE Salt Processing   
LJ Plants for Two-Fluid MSBR   
LK Plants for One-Fluid MSBR

M MSRE

MA Design

MAA Plant

MAB Major Component

MAC Instrumentation and Controls

MAD Auxiliary Systems and Components

MB Construction

MC Operation

MCA Program

MCB Procedures

MCC Training

MCD Experience

MD Analysis

MDA Theoretical

MDB System Performance

MDC Nuclear Performance

ME Maintenance

MEA Principles

MEB Procedures

MEC Experience

MF Decommissioning

# Appendix C

# INSTRUCTIONS FOR USE OF MSRIS FROM AN

# INTERACTIVE COMPUTER TERMINAL

Searches of the MSRIS file may be conducted by simultaneous users from teleprinter terminals connected to the ORNL central computer through the public dial telephone system. These searches are carried out by the computer program, ORLOOK, which has access to a number of other analogous files. ORLOOK, in turn, is only one of many computer procedures that can be used from remote terminals through the computer Time Sharing Option (TSO). Thus, the prospective user of MSRIS must:

1. Establish a telephone connection to the computer.   
2. Gain access to TSO by appropriate user identification.   
3. Invoke the ORLOOK procedure.   
4. Select the MSRIS file.

Upon completion of the search, the user must:

1. Terminate the ORLOOK session.   
2. Sign off from TSO.   
3. Release the telephone connection.

In preparation for an initial session, the user will need first to gain some understanding of distinctive characteristics of the terminal available to him as they relate to operations desired.

# Obtaining Terminal Connection to Computer

For purposes of these instructions, terminals may be considered to fall into two general classes:

Class I: IBM compatible-15 Char./Sec., Upper and Lower Case

(IBM Model 2741, NOVAR Model 5-50, etc.)

Class II: Teletype compatible

a. 10 Char./Sec., Upper Case Only

(Teletype Models 33 or 35, etc.)

b. 30 Char./Sec., Upper and Lower Case

(Teletype Model 37, G.E. Terminet

Model 300, I/O Devices Model 100,

Tex. Instr. Model 700, Beehive CRT

Model IA, etc.)

For Class I Terminals (IBM compatible), the following steps are required to obtain a telephone connection to the computer:

1. In preparation for typing messages to the computer, the user must recognize the difference between the numeric character "l" (key number zero on a standard typewriter keyboard) and the alphabetic character "l" (key number 34) which is often used as a l in typing. Care must also be taken not to confuse the zero numeric key (number 35) with the alphabetic "0" key (number 33). Of the various print balls available, IBM selectric typewriter, No. 527 (Waterloo correspondence) should be used on most terminals to obtain a character set appropriate for the computer system employed for MSRIS.   
2. See that the telephone coupler is turned on and its selector switch is positioned to "HALF DUPLEX" (labeled "H.D.," or "COPY" on some models).   
3. Dial 3-1021 or 3-1041.* Following ring, listen for a steady high-pitched tone, then place the telephone handset firmly in the cradle or coupler, positioning cord-to-cord. (It is assumed here that an acoustic coupler is used; otherwise the user should check with the terminal custodian for variations in procedures.)   
4. Turn on the terminal. If the coupler or teleprinter is equipped with a "CARRIER" or "XMIT" indicator light, it will illuminate to show that connection has been made to the computer. The user may now proceed to give his identification to initiate searches for documents in the MSRIS as will be explained.

For Class II Terminals (Teletype compatible), the steps to obtain telephone connection to the computer are similar to those given for Class I, with a few exceptions, as follows:

1. Characters printed by most terminals in this class are fixed to the standard set for Model 33 teatypes. Some function keys, such as those labeled "CONTROL" and "ESC" are not used with MSRIS, so they will not be explained here.

2. Same as 2 above.   
3. Dial 3-1011 for 10 Char./Sec. teletype-compatible terminals. Dial 3-1051 for 30 Char./Sec. teletype-compatible terminals. Upon hearing the steady high-pitched tone place the handset in the coupler as in 3 above.   
4. Turn on the terminal by positioning the LOCAL/OFF/LINE switch to "LINE."

# Logging On and Off for MSRIS (See Example 1)

After obtaining a telephone connection to the computer, as described above, the user should proceed, without unreasonable delay to "log on" and then invoke the ORLOOK procedure from which the MSRIS file can be selected. In applying the instructions, given below, care must be exercised to type the statements exactly as shown, including spaces. The one exception to this rule is in the use of upper case and lower case alphabetic characters. In this Appendix, we have chosen to show messages typed by the user and responses from the computer in upper case characters to distinguish them from the remainder of the text. However, if the user's terminal has both upper and lower case alphabetic characters, user input may be typed in all upper case, all lower case, or any combination thereof, with due consideration for non-alphabetic characters that may not have equivalent upper and lower case forms. In addition, computer output through such terminals will appear with the usual mix of upper and lower case alphabetic characters.

1. Type LOGON, and press RETURN. (In all cases, after typing the required characters, the user must press the RETURN key to transmit the data to the computer. In all subsequent instructions, proper use of the RETURN key will be assumed.)

NOTE: With IBM-compatible terminals, if a wrong key is struck, use BACKSPACE and strike over to correct the error; with teletype compatibles, use BACKARROW, which is obtained by holding down the SHIFT while striking the alphabetic O key.

2. The computer responds to LOGON with a set of characters identifying the job and the request ENTER USERID-. The user may then transmit the 3-character user identification (e.g. XXX) as assigned by computer center personnel.   
3. When the USERID is accepted, the computer prompts the user to ENTER PASSWORD FOR XXX-. The user may then enter a 3-character password, also assigned by computer center personnel.   
4. If the password is also acceptable, the computer responds with: XXX LOGON IN PROGRESS AT (time) ON (date), followed by any current bulletins to TSO users and a listing of any special procedures specifically cataloged under XXX. A final message, READY, indicates that the user now has gained access to TSO and the computer is ready for action.   
5. The ORLOOK procedure is then invoked by simply transmitting the word ORLOOK. The computer response is then the date, time, any user messages, and the question:

DATABASE PUBLIC/PRIVATE/OTHER/STOP?

The proper user response to lead to use of MSRIS is to transmit the word PUBLIC.

6. The computer responds by typing a list of the number of each data FILE and the title of the associated DATABASE. (Example 1 presents only part of the total listing. This listing, and any other message being transmitted by the computer, may be interrupted by pressing the ATTN key on IBM-compatible terminals or the BREAK key on teletype terminals. The computer will then proceed to the next step in the procedure that is in effect. The exclamation point in DATABASE #6 indicates that the message was interrupted.) Upon completion, or interruption, of the ORLOOK list, the computer requests:

SELECT FILE #:

and the user, noting (or knowing) that the Molten Salt Reactor Information File is item #4, types simply

7. The computer then responds:

4 MOLTEN SALT REACTOR INFORMATION FILE

ORLOOK READY

The user may now conduct selective searches for molten salt reactor publications through various avenues of approach as will be described. The period (.) on the last line of the computer response is the ORLOOK system's indication that it is the user's turn to transmit a command.

Upon completion of a session the user must release the ORLOOK procedure and "sign off" from TSO. The procedure, also illustrated in Example 1, is as follows:

1. At any time that ORLOOK is ready to accept a command (as indicated by the period), simply transmit the command:

STOP

The computer responds with the message:

END ORLOOK SESSION

plus an indication of the computer time used and the present time.

2. Since the user is still in the TSO mode of operation, the computer then transmits the TSO message:

READY

to indicate that another procedure may be invoked. The user then transmits the command:

LOGOFF

to which the computer responds with

XXX LOGGED OFF TSO AT (time) ON (date) +

3. Finally the user must hang up the telephone handset or otherwise sever the telephone connection. It is important that this be done in order not to hold open one of the computer communication lines.

# Elementary Search of the MSRIS File (See Example 2)

Having selected the MSRIS file, searches may be conducted for documents containing specified subject matter by typing LOOK* commands which take the general form of:

LOOK

where words describing the subject matter are placed between the single quotes. Always follow primary commands, such as LOOK, by a space. (The elementary command, as here written, can be given a number of optional modifications for more refined searches which will be explained later.) To each such command the computer responds with a period. The user may then supply additional commands or request execution of the commands that have been given. To initiate action on a LOOK command or a series of such commands, the user must type END, and the search will be initiated.** In the initial search, the computer responds:

SEARCHINGSUBSETNO.0

After a pause, that varies in length depending on the size of the file and how busy the computer is at the moment, the following response will be received:

...DOCUMENTS IN FILE

ANSWERS IN SUBSET NO. 1

...DOCUMENTS IN RESULT

where the first blank is the size of the whole MSRIS file, and the second blank gives the number of file entries found to contain the subject matter specified. (The search is conducted without any distinction between upper case and lower case characters in subject matter.) Usually, the second number is large, so subsequent LOOK commands are entered to refine the search further, before asking the computer to LIST the findings. Answers

will be collected in SUBSETS 1, 2, 3, etc. It is important to emphasize here that each successive search is automatically applied to the most recently isolated subset file unless the user enters the command SUBSET followed by a number. For a new search against all of MSRIS, enter SUBSET O. At any time that the computer provides a period, the command LIST can be given to cause the last acknowledged subset to be typed out on the terminal. (The local printout can be interrupted before completion by pressing the ATTN key on IBM compatible terminals, or the BREAK key on teletype compatible terminals.) For large listings, it will be preferable to give the command PRINT rather than LIST, to produce printouts on a high-speed line printer at the computer center for subsequent delivery by courier. As will be shown later, the LIST and PRINT commands can be given optional modifiers to select portions of subsets to be produced in any order that may be desired.

# Selective Search for Documents by Field Labels and Selective Print (See Example 3)

From the last example, it will be noted that each MSRIS file entry has labels that define fields for each reference. Searches may be conducted, (and listings can be made) according to fields or combinations of fields. The labels actually used and their abbreviations are as follows:

<table><tr><td>Label</td><td>Abbreviation</td></tr><tr><td>HEADER</td><td>H</td></tr><tr><td>AUTHOR</td><td>AU</td></tr><tr><td>TITLE</td><td>TI</td></tr><tr><td>PUB DESC</td><td>PU</td></tr><tr><td>SUBJ CAT</td><td>SU</td></tr><tr><td>KEYWORDS</td><td>KE</td></tr><tr><td>ABSTRACT</td><td>A</td></tr></table>

In entering a search command, labels must be enclosed within prescribed delimiter characters. For the IBM-compatible terminals (with Waterloo correspondence print ball) the command will have the form:

$$
. \text {L O OK} <   \mathrm {A U} > = ^ {\prime} \text {T A L L A C K S O N} ^ {\prime}
$$

where the delimiter symbol "<" comes from pressing the SHIFT and striking

the first key on the top row and the "<" symbol comes from SHIFT and striking the last key on the second row. (If the Waterloo correspondence print ball is not used, the characters will usually print as "l" and "l/4" respectively.) With teletype-compatible terminals, the delimiter "<" is obtained by holding down the SHIFT key and striking the comma key and "<" is obtained with SHIFT and the period key. Where searches are delimited by labels, only the designated fields will be searched, whereas without labels every word of the text is searched, which takes more time to accomplish.

The LIST or PRINT command may be given modifiers to either limit which fields of a reference are provided, or to change the sequence of the fields. Such a command takes the form:

.LIST AU, TI, A

where a space must follow the primary command and modifiers are separated by commas. A command in this form will be applied to the preceding subset that has been isolated, unless a reference number is given in the form:

.LIST 8,AU,TI,A

This will give the AUTHOR, TITLE, and ABSTRACT for reference number 8 (the eighth sequential reference of the entire MSRIS file and printed as $\# \# \# 8$ ###).

Searching by delimited fields and listing or printing by delimited fields are independent of each other, so they can be mixed as may be desired.

Searching by Logical Combinations (See Example 4)

To achieve more efficient searches for MSRIS documents, the elementary LOOK command may be given sharper focus by expanding to one or more of the following forms:

(a) .LOOK 'X' and 'Y'

.END

This combination will find references containing both 'X' and 'Y'. (If "and" is omitted in this command, viz., LOOK 'X' 'Y', it will get the same result.) From one to four search items may be specified. Note that for the combination used in Example 4, only one document was found in the data file.

(b) .LOOK 'X'   
. LOOK 'Y'   
.END

This combination will find all references in which either 'X' or 'Y' occurs. Up to ten LOOK commands may be entered, and they may contain single or multiple search items. In the example, 35 documents were found when the same two keywords were specified in the OR format.

(c) .LOOK 'X'

. LOOK NOT 'Y'   
.END

This format will collect references containing the search item 'X' but not containing 'Y'. As many as ten LOOK commands may be specified with NOT preceding the search items in addition to the ten allowed without NOT specified.

In these combination commands, individual search items may be given label delimiters confining the fields to be scanned, as in this example, or they may be left unlabeled. For instance,

. LOOK 'HEAT TRANSFER'   
. LOOK NOT <AU> = 'MCCOY'   
.END

will find references that contain, in any field, the words 'heat transfer' and are authored by others than McCoy.

# Correcting Errors in Search Commands

As the user learns to formulate increasingly complex commands to achieve efficient searches, the likelihood of making errors will become greater. Most such errors can readily be corrected, employing conventions available within ORLOOK. At any point during a session between LOGON and LOGOFF, miskeying can be remedied by the BACKSPACE (or BACKARROW on teletypes). While in the course of typing a LOOK command before RETURN has been pressed, that line can be entirely deleted by striking the @ key. If it is desired to eliminate an immediately preceding LOOK command, type CANCEL and press RETURN. If it is desired to eliminate an entire series of LOOK COMMANDS, type CANCEL ALL, and re-enter the desired commands. The ATTN key (BREAK on teletype) may be employed to interrupt any computer operation and return control to the user.

# Efficient Search Strategies

Before initiating a terminal search for MSRIS documents, a user should select a strategy most likely to achieve his objective accurately and rapidly. Taking full advantage of interactive capabilities, the usual approach will involve entering an initial LOOK command describing the general area of interest to obtain SUBSET #1 against which file of reduced size subsequent searches may be directed. Without returning to the complete MSRIS library (SUBSET #0), he may proceed to: (1) browse through that collection of references to obtain an overall idea of information available on selected topics; (2) locate a set of documents to generate a bibliography; or (3) make a definitive search for a specific publication or publications.

# Browsing (See Example 5)

To illustrate strategy for browsing, let us assume the user wishes to discover what documents are available on properties of Hastelloy N and modified Hastelloy N. Entering the command LOOK 'Hastelloy N', although permissible, would cause the computer to painstakingly examine every line of the MSRIS file looking for this string of characters and would, of

course, collect in a subset a large number of references, many of them irrelevant. So, a preferable beginning would be made (observing from the MSRIS subject categories list that category FB denotes "Hastelloy N" and FC denotes "Modified Hastelloy N") by typing:

$$
. \mathrm {L O O K} <   \mathrm {H} > = ^ {\prime} \mathrm {F B} ^ {\prime}
$$

$$
. L O O K <   H > = ^ {\prime} F C ^ {\prime}
$$

.END

As SUBSET #1, the computer would combine the references from the FB and FC categories and indicate the total number found. This group of references could then be explored with further LOOK commands to determine what documents include information on specified properties.

When the topic to be browsed does not fall into an MSRIS subject category, an initial search command employing some other delimiter or combination of delimiters may be employed to obtain a representative SUBSET #1. For instance, to explore outside literature collected on "heat transfer," a search might begin with:

$$
. \text {L O O K} <   \mathrm {K E} > = ^ {\prime} \text {H E A T T R N S F E R} ^ {\prime}
$$

$$
. \text {L O O K N O T} <   \text {P U B} > = ^ {\prime} O A K R I D G E ^ {\prime}
$$

.END

Bibliographies (See Example 6)

Where it is desired to obtain a collection of documents covering an extensive topic for time-consuming study, a broad search should be initiated, followed by entry of a PRINT command to produce complete copy on the computer center high-speed line printer for courier delivery. For instance, a user wishing to make a bibliographic study of "corrosion products" may enter on the terminal:

$$
. \text {L O O K} <   \mathrm {K E} > = ^ {\prime} \text {C O R R O S I O N} ^ {\prime}
$$

.END

If the number of documents reported appears too large to handle, other search commands may be entered.

From subsets of related references it will sometimes be desirable to obtain combinations using the COMBINE command as follows:

.COMBINE 1 AND 2

will assemble a new subset of references common to both SUBSET #1 and SUBSET #2

.COMBINE1OR2

will assemble a new subset containing all references that appear in either SUBSET #1 or SUBSET #2

.COMBINE 1 NOT 2

will assemble a new subset containing SUBSET #1 references but excluding those that also appear in SUBSET #2.

Occasionally a user may wish to have a hard copy of results, but does not want to wait for it to be typed at the terminal. Such copy may be obtained by entering the command:

PRINT

When the computer returns the word PRINTED and a period, terminal-control has been restored to the user. The LIST (or PRINT) command with modifiers can be used to obtain a structured bibliographic summary. Another type of bibliographic search often useful is a search by authors, either modified or unmodified by some topical parameter.

# Definitive searches

Definitive searches to pinpoint some discrete piece of information may take many forms. As users become experienced with the system operation and familiar with the file structure, they may be able to formulate single search combinations that will hit their objectives, but that is somewhat risky with respect to the possibility of missing relevant documents. Thus, it will usually prove desirable to first define the general area of interest so as to set up an initial SUBSET of reasonable size on which successive LOOK commands may operate. If first attempts do not hit desired targets, returns can be made to that SUBSET for further operations

using different combinations of field delimiters. The various subsets generated in Example 6 could, for example, be used in additional searches.

# Auxiliary Operations

Summary tabulations (See Example 7)

It is useful either at the end of an ORLOOK session, or sometime during the course of a rather extensive one, to have the computer formulate on the terminal a tabulation of the successive search transactions. Such an output can be obtained whenever desired by entering the command:

# - REQUEST

The first column of the tabulation provides a ready reference of the SUBSET # developed for the search items shown in the last column, as a guide to further probing among designated collections of references. Efficiencies of successive sessions can be improved by study of request summaries.

Search-field LABEL identification (See Example 8)

During the course of an ORLOOK session, if a user needs a reminder of field identifier LABELS and their abbreviations, he may enter the command LABELS. All LABELS recognized by the general ORLOOK program will be listed; however, only a few of these are applicable to MSRIS as shown in Example 8.

The LOOK command when used without a field delimiter (as in Example 2) causes the computer to search all fields of each entry for the object of the command. (This is the "default" option built into the program.) This rather time-consuming process can be avoided by designating a field as in Example 3. However, field designation can also become time consuming (and monotonous) if a user wishes to execute a large number of LOOK commands within a given field type. To avoid this latter problem, the user may change the default option to cause searching of any one field when an un-modified LOOK is entered. To accomplish this the user enters the command:

to which the computer response is:

# KEY FIELD LABEL?

After the user enters the abbreviation of the LABEL selected, e.g., KE, and the computer acknowledges

# KEYWORDS SELECTED

that LABEL will be applied in all subsequent LOOK commands that are not otherwise delimited. In this example, the command:

LOOK 1

will search only the KEYWORDS fields for the desired expression. A return to the original mode, where all fields are searched when LABELS are undesignated, may be accomplished by entering RESET again and responding to the computer's question with ALL.

# Terminal controls

The standard length of a line in ORLOOK transactions is limited to 80 characters for IBM compatible terminals and 70 characters for teletypes. To alter the length, the following command may be entered:

.LINE TERMINAL, - - -

substituting a two-or-three-digit figure for the dashes to designate the number of characters desired. Similarly, prior to using the PRINT command, maximum length of lines produced by the central computer line printer can be altered by entering the command:

.LINE PRINTER, -

Return to original line length limitations can be obtained by reentering the commands and specifying 80 characters for IBM-compatible terminals and 70 characters for teletypes.

NOTE: Operations such as RESET and LINE TERMINAL appear to, and in fact do, alter the basic ORLOOK program. However, these alterations do not affect others who may be using the program at the same time; nor do they remain in effect after the user concludes his session. Each user who invokes the ORLOOK procedure is provided with a "fresh" copy of the

original (and unalterable) program in a volatile region of the computer memory. That copy, and any changes made in it by the user, remain available only for the duration of that session (unless special storage is prearranged and used). Thus, special features must be entered each time they are used, but they need not be removed.

# Glossary of ORLOOK Commands for MSRIS

# To begin and end a session

<table><tr><td>LOGON</td><td>Begins session with TSO</td></tr><tr><td>ORLOOK</td><td>Invokes ORLOOK procedure</td></tr><tr><td>STOP</td><td>Ends ORLOOK session</td></tr><tr><td>LOGOFF</td><td>Terminates TSO</td></tr></table>

# To conduct searches

<table><tr><td>LOOK &#x27;aaaa&#x27;</td><td>Searches all fields of references for aaaa.</td></tr><tr><td>LOOK &#x27;aaaa&#x27; &#x27;bbb&#x27;</td><td>Searches all fields for aaaa and bbbb occurring in the same reference, not necessarily in the same field.</td></tr><tr><td>LOOK not &#x27;bbb&#x27;</td><td>Searches all fields for each reference withoutbbb.</td></tr><tr><td>LOOK &#x27;aaaa&#x27;</td><td rowspan="2">Searches all fields for aaaa orbbb and combines the results.</td></tr><tr><td>LOOK &#x27;bbb&#x27;</td></tr><tr><td>LOOK &lt; -- &gt; = &#x27;aaaa&#x27;</td><td>Searches -- field for aaaa.</td></tr><tr><td>END</td><td>Completes the set of LOOK commands and starts the search.</td></tr></table>

# To define reference sets to be searched

<table><tr><td>SUBSET 0</td></tr><tr><td>SUBSET --</td></tr><tr><td>COMBINE 1 AND 2</td></tr><tr><td>COMBINE 1 OR 2</td></tr></table>

<table><tr><td>Directs the subsequent search against the entire MSRIS file.</td></tr><tr><td>Directs subsequent search against the previously collected SUBSET #--.</td></tr><tr><td>Assembles a new subset of references common to SUBSET #1 and SUBSET #2.</td></tr><tr><td>Assembles a new subset combining all references that appear in either SUBSET #1 or SUBSET #2.</td></tr></table>

<table><tr><td>COMBINE 1 NOT 2</td><td>Assembles a new subset from SUBSET #1, excluding any that also appear in SUBSET #2.</td></tr><tr><td>@</td><td>Deletes the line being typed.</td></tr><tr><td>CANCEL</td><td>Cancels the preceding LOOK command; when modified with ALL, cancels the current series of LOOK commands.</td></tr><tr><td>LABELS</td><td>Lists key-field labels.</td></tr><tr><td>RESET</td><td>Indicates user&#x27;s desire to name a new default label.</td></tr><tr><td colspan="2">To obtain results</td></tr><tr><td>LIST</td><td>Types out, on the terminal, all fields of the last subset.</td></tr><tr><td>LIST ---</td><td>Types out, on the terminal, all fields of reference number ---.</td></tr><tr><td>LIST ,-, -, -</td><td>Types out, on the terminal, the fields specified by the blanks, and in that order, from the last subset.</td></tr><tr><td>SUBSET --</td><td>Types out, on the terminal, the references collected in subset -, for the fields specified in LIST.</td></tr><tr><td>LIST ---, ---</td><td>Prints, on a computer-center line printer, all fields of the last subset - may be given modifiers as shown for LIST.</td></tr><tr><td>LINE TERMINAL ,---</td><td>Changes the maximum line length typed on the terminal to --- characters.</td></tr><tr><td>LINE PRINTER ,---</td><td>Changes the maximum line length produced by the line printer to --- characters.</td></tr><tr><td>REQUEST</td><td>Types out, on the terminal, a summary tabulation of LOOK commands and results obtained during the current session.</td></tr></table>

# Example 1

Logging On and Off for MSRIS Via

IBM-Compatible Terminal

logon

IKJ56700A ENTER USERID -

![](images/e48bc73a27cc7f756452e453fec055f52a5a5efd3a265957324aa14eaea93013.jpg)

ENTER PASSWORD FOR

![](images/2b34effa209e48b8879c905ca9ad4f6b065b93008c813dead9f8e1cf9b2fbf2b.jpg)

LOGON IN PROGRESS AT 13:35:11 ON APRIL 17, 1975

10/21/74 TSU phone nos.- 2741: 31001, 31021, 31041; tty: 31011 (10cps), 31051 (30 cps)

READY

orlook

DATE $= 04 - 17 - 75$ TIME NOW $= 13.36.27$

++++ 3-5-75 ++++ WELCOME TO ORLOOK, CALL 3-6097 IF PROBLEMS ARISE

DATABASE PUBLIC/PRIVATE/OTHER/STOP?PUBLIC

# FILE#

# DATABASE

1 FORESTRY SOURCE FILE I   
2 IBP ABSTRACT   
3 COAL TECHNOLOGY LIBRARY FILE  
4 MOLTEN SALT REACTOR INFORMATION FILE   
5 URBAN TECHNOLOGY   
6 MODELING BI!

SELECTFILE#:4

4 MOLTEN SALT REACTOR INFORMATION FILE

ORLOOK READY

.stop

END URLOOK SESSION

CPU(SEC) USED = 3.40 LAPSED (HR.MIN.SEC) = 00.04.28

TIME NOW = 13.40.55

READY

logoff

LOGGED OFF TSO AT 13:41:50 ON APRIL 17, 1975+

# Example 1

Logging On and Off for MSRIS Via

Teletype Terminal

LOGON

IKJS6700A ENTER USERID -

![](images/0717a6afccb017f20c1ff671e510d676dfc16f5d8d70420c277e02bd77000090.jpg)

ENTER PASSWORD FOR

![](images/a7d4249baea060e6575866153315a21026d8cbe0328151f60c611969e5aa160f.jpg)

LOGON IN PROGRESS AT 17:20:11 ON MARCH 11, 1975

10/21/74 TS0 PHONE N05.- S741: 31001, 31021, 31041; TTY: 31011 (10CPS),

31051 (30 CPS)

8/15/74 NEW COMMAND PROCEDURE SQUISH NOW AVAILABLE. TYPE ORNLTS0 SQUISH.

SHOWFAILED-NOCATALOGENTRIESFOUNDFOR

READY

ORLOK

DATE $= 03 - 11 - 75$ TIME NOW $= 17.21.01$

+++ 3-5-75 ++++ WFLCOMF TO ORL0OK, CALL 3-1604 IF PROBLEMS ARISE

DATABASE PUBLIC/PRIVATE/OTHER/STOP?PUBLIC

FILE# DATABASE

1 FORESTRY SOURCE FILE I   
2 IBP ABSTRACT   
3 COAL TECHNOLOGY LIBRARY FILE  
4 MOLTEN SALT REACTOR INFORMATION FILE   
5 URBAN TECH!

SELECTFILE#84

4 MOLTFN SALT REACTOR INFORMATION FILE

ORLOOK READY

- STOP

END ORL0OK SESSION

CPU（SEC）USED $= 3.00$ LAPSFD（HR·MIN·SEC） $= 00.01.31$

TIME NOW = 17.22.32

READY

L0G0FF

LOGGED OFF TS0 AT 17:23:07 ON MARCH 11, 1975+

$> R$

# Example 2

Elementary Search of the MSRIS File

look 'safety'

. end

SEARCHINGSUBSET#0

373 DOCUMENTS IN FILE

ANSWERS IN SUBSET # 1

22 DOCUMENTS IN RESULT

look 'control rod'

. end

SEARCHINGSUBSET#1

ANSWERS IN SUBSET # 2

5 DOCUMENTS IN RESULT

.list

\*\*\*SUBSET#2\*\*\*

8

<HEADER >AAX670010

<AUTHSHIP>

<AUTHOR >Kasten, P.R.

<TITLE >SAFETY PROGRAM FOR MOLTEN-SALT BREEDER REACTORS

<REFERENC>

<POB DESC>Oak Ridge National Laboratory, Tenn. ORNL-TM-1858 (June 1967) 42 p, 6 fig, 3 ref.

<KEYTERMS>

<SUBJ CAT>AAX; BGX

<KEYWORDS>MSRP; *safety; *analysis; *plans; reactivity; MSBR; accidents;

costs; containment; stability ; dynamic characteristics; off-gas systems; processing

<ABSTRACT>Investigations required in determining the safety characteristics of MSBR power plants are outlined, and the safety features of the major plant systems are described. Reactivity additions w-hic!

# Example 3

Selective Search for Documents by Field

Labels and Selective Listing

look $\langle \mathrm{au}\rangle =$ 'Tallackson'

-end

SEARCHINGSUBSET#0

ANSWERS IN SUBSET # 3

4 DOCUMENTS IN RESULT

.list au,ti,pub

\*\*\*\*SUBSET#3\*\*\*

6

<AUTHOR >Tallackson, J.R.; Moore, R.L.; Ditto, S.J.

<TITLE >INSTRUMENTATION AND CONTROLS DEVELOPMENT FOR MOLTEN-SALT BREEDER REACTORS

<POB DESC>Oak Ridge National Laboratory, Tenn. ORNL-TM-1856 (May 1967), 36 p, 2 ref.

247

<AUTHOR >Tallackson, J.R.

<TITLE >THERMAL RADIATION TRANSFER OF AFTER HEAT IN MSBR HEAT EXCHANGERS

<Pub DESC>Oak Ridge National Laboratory, Tenn. ORNL-TM-3145 (March 1971), 108 p, 43 fig, 28 ref.

302

<AUTHOR >Tallackson, J.R.

<TITLE >NUCLEAR AND PROCESS INSTRUMENTATION -- PART IIA, MSRE DESIGN AND

OPERATIONS REPORT

<.PUB DESC>Oak Ridge National Laboratory, Tenn. ORNL-TM-729 (Feb. 1968), 397 p.

180 fig, 102 ref.

331

<AUTHOR >Beall, S.E.; Haubenreich, P.N.; Lindauer, R.B.; Tallackson, J.R.

<TITLE >MSRE DESIGN AND OPERATIONS REPORT, PART V -- REACTOR SAFETY ANALYSIS REPORT

<POB DESC>Oak Ridge National Laboratory, Tenn. ORNL-TM-732 (Aug. 1964), 300 p, 109 fig. 50 ref.

\*\*\*ENDLIST

.list 6,a

6

<ABSTRACT>Instrumentation used in the MSRE is a good basis for development of the instrumentation for large molten-salt br!

# Example 4

Searching by Logical Combinations

look $\langle \mathrm{ke}\rangle =$ 'heat transfer' and $\langle \mathrm{ke}\rangle =$ 'liquid metals'

-end

SEARCHINGSUBSET#0

373 DOCUMENTS IN FILE

ANSWERS IN SUBSET # 1

1 DOCUMENTS IN RESULT

subset 0

look $\langle \mathrm{ke}\rangle =$ 'heat transfer'

look $\langle \mathrm{ke}\rangle =$ 'liquid metals'

. end

SEARCHINGSUBSET#0

ANSWERS IN SUBSET # 2

35 DOCUMENTS IN RESULT

-.subset 0

look $\langle \mathrm{ke}\rangle =$ 'heat transfer'

look not $\langle \mathrm{ke}\rangle =$ 'liquid metals'

.end

SEARCHINGSUBSET#0

ANSWERS IN SUBSET # 3

18 DOCUMENTS IN RESULT

subset 0

look 'heat transfer'

look not <au> = 'McCoy'

.end

SEARCHINGSUBSET#0

ANSWERS IN SUBSET # 4

22 DOCUMENTS IN RESULT

# Example 5

Search Strategy for Browsing

look <h> = 'fb'

look <h> = 'fc'

. end

SEARCHINGSUBSET#0

ANSWERS IN SUBSET # 6

39 DOCUMENTS IN RESULT

look $\langle \mathrm{ke}\rangle =$ 'ductility' $\langle \mathrm{ke}\rangle =$ 'heat treatments'

. end

SEARCHINGSUBSET#6

ANSWERS IN SUBSET # 7

9 DOCUMENTS IN RESULT

.subset 0

look $\langle \mathrm{ke}\rangle =$ 'heat transfer'

look not <pub> = 'Oak Ridge'

.end

SEARCHINGSUBSET#0

ANSWERS IN SUBSET # 8

2 DOCUMENTS IN RESULT

.list au,ti

\*\*\*\*SUBSET#8\*\*\*\*

111 #

<AUTHOR >Gat, U.

<TITLE >COOLING CONCEPTS FOR A COMPACT MOSEL (MOLTEN SALT) REACTOR

366

<AUTHOR >Voznick, H.P.; Uhl, V.W.

<TITLE >HOLTEN SALT FOR HEAT TRANSFER

*** END LIST

# Example 6

Preparation and Combination of Subsets

look <ke> = 'corrosion'

.end SEARCHINGSUBSET#0

373 DOCUMENTS IN FILE

ANSWERS IN SUBSET # 1

69 DOCUMENTS IN RESULT

look <ke> = 'MSRE'

.end

SEARCHINGSUBSET#1

ANSWERS IN SUBSET # 2

41 DOCUMENTS IN RESULT

subset 0

look <ke> = 'Hastelloy'

. end

SEARCHINGSUBSET#0

ANSWERS IN SUBSET # 3

84 DOCUMENTS IN RESULT

combine 2 and 3

ANSWERS IN SUBSET # 4

24 DOCUMENTS IN COMBINED RESULT

combine 2 or 3

ANSWERS IN SUBSET # 5

101 DOCUMENTS IN COMBINED RESULT

combine 2 not 3

ANSWERS IN SUBSET # 6

17 DOCUMENTS IN COMBINED RESULT

combine 3 not 2

ANSWERS IN SUBSET # 7

60 DOCUMENTS IN COMBINED RESULT

.subset 4

.print

PRINTED

.stop

# Example 7

Summary Tabulation of Commands Used

During an ORLOOK Session

.request

<table><tr><td colspan="4">:RESULT:SEARCH: NO.: DEFAULT: SEARCH ITEM(S) OF REQUEST(S): IN # :FROM # : HITS: LABELS</td></tr><tr><td>1:</td><td>0:</td><td>1:</td><td>ALL</td></tr><tr><td>1:</td><td>0:</td><td>35:</td><td>ALL</td></tr><tr><td>2:</td><td>0:</td><td>18:</td><td>ALL</td></tr><tr><td>3:</td><td>0:</td><td>22:</td><td>ALL</td></tr><tr><td>4:</td><td>0:</td><td>0:</td><td>ALL</td></tr><tr><td>5:</td><td>4:</td><td>0:</td><td>ALL</td></tr><tr><td>6:</td><td>0:</td><td>39:</td><td>ALL</td></tr><tr><td>7:</td><td>6:</td><td>9:</td><td>ALL</td></tr><tr><td>8:</td><td>0:</td><td>2:</td><td>ALL</td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td></tr></table>

# Example 8

Labels Available in ORLOOK Procedure

.labels

<table><tr><td>LABELS(ABBREV)</td><td>MODE</td><td>TYPE</td></tr><tr><td>HEADER(H)</td><td>TEXT</td><td>LIST*</td></tr><tr><td>AUTHSHIP(AUT)</td><td>TEXT</td><td>SUBSET*</td></tr><tr><td>AUTHOR(AU)</td><td>TEXT</td><td>LIST*</td></tr><tr><td>CORPAUTH(COR)</td><td>TEXT</td><td>LIST</td></tr><tr><td>SPONSOR(SP)</td><td>TEXT</td><td>LIST</td></tr><tr><td>MENTOR(M)</td><td>TEXT</td><td>LIST</td></tr><tr><td>TITLE(TI)</td><td>TEXT</td><td>LIST*</td></tr><tr><td>REFERENC(R)</td><td>TEXT</td><td>SUBSET*</td></tr><tr><td>LIT TYPE(LI)</td><td>TEXT</td><td>LIST</td></tr><tr><td>PUB DATE(PU)</td><td>TEXT</td><td>LIST*</td></tr><tr><td>PUB DESC(PUB)</td><td>TEXT</td><td>LIST</td></tr><tr><td>LANGUAGE(L)</td><td>TEXT</td><td>LIST</td></tr><tr><td>COUNTRY(COU)</td><td>TEXT</td><td>LIST</td></tr><tr><td>AVAIL(AV)</td><td>TEXT</td><td>LIST</td></tr><tr><td>OR AVAIL(O)</td><td>TEXT</td><td>LIST</td></tr><tr><td>SEC SOUR(S)</td><td>TEXT</td><td>LIST</td></tr><tr><td>KEYTERMS(K)</td><td>TEXT</td><td>SUBSET*</td></tr><tr><td>SUBJ CAT(SU)</td><td>TEXT</td><td>LIST*</td></tr><tr><td>KEYWORDS(KE)</td><td>TEXT</td><td>LIST*</td></tr><tr><td>GEOGDESC(G)</td><td>TEXT</td><td>LIST</td></tr><tr><td>DATADATE(DA)</td><td>TEXT</td><td>LIST</td></tr><tr><td>TAXON(T)</td><td>TEXT</td><td>LIST</td></tr><tr><td>PARMLIST(P)</td><td>TEXT</td><td>LIST</td></tr><tr><td>PVT KWD(PV)</td><td>TEXT</td><td>LIST</td></tr><tr><td>TAXON 2(TA)</td><td>TEXT</td><td>LIST</td></tr><tr><td>CHEMICAL(C)</td><td>TEXT</td><td>LIST</td></tr><tr><td>ABSTRACT(A)</td><td>TEXT</td><td>LIST*</td></tr><tr><td>COMMENT(CU)</td><td>TEXT</td><td>LIST</td></tr><tr><td>INPUTTEAM(I)</td><td>TEXT</td><td>LIST</td></tr><tr><td>DATA FLD(D)</td><td>TEXT</td><td>SUBSET</td></tr><tr><td>DATADESC(DAT)</td><td>TEXT</td><td>LIST</td></tr><tr><td>NUM DATA(N)</td><td>TEXT</td><td>LIST</td></tr></table>

.stop

END ORLOOK SESSION

CPU(SEC) USED = 52.66 LAPSED (HR.MIN.SEC) = 00.48.10

TIME NOW = 14.51.50

![](images/849fc94d138e70f4cb1b6f02033241d7542622a0c0f9b5d7a1c21bc2a082e120.jpg)

# Internal Distribution

1. E.J. Allen   
2. R.F.Apple   
3. C. F. Baes, Jr.   
4. C. E. Bamberger   
5. C. J. Barton   
6. H. C. Beeson   
7. J. T. Bell   
8. M. Bender   
9. M. R. Bennett   
10. C. E. Bettis   
11. E. S. Bettis   
12. J. O. Blomeke   
13. A. L. Boch   
14. E. G. Bohlmann   
15. C. Brashear   
16. D. N. Braski   
17. J. Braunstein   
18. M. A. Bredig   
19. C. R. Brinkman   
20. H. R. Bronstein   
21. R. E. Brooksbank   
22. C. H. Brown   
23. G. D. Brunton   
24. J. Brynestad   
25. W. D. Burch   
26. S. Cantor   
27. D. W. Cardwell   
28. J. A. Carter   
29. W. L. Carter   
30. B. R. Clark   
31. R. E. Clausing   
32. J. A. Conlin   
33. W. H. Cook   
34. J. H. Cooper   
35. L. T. Corbin   
36. J. M. Corum   
37. W. B. Cottrell   
38. R. M. Counce   
39. J. L. Crowley   
40. F. L. Culler   
41. J. M. Dale   
42. F. L. Daley   
43. J. H. DeVan   
44. J. R. DiStefano   
45. S. J. Ditto   
46. A. S. Dworkin

47. W. P. Eatherly   
48-72. J.R. Engel   
73. G.G.Fee   
74. D. E. Ferguson   
75. L. M. Ferris   
76. M. H. Fontana   
77. A. P. Fraas   
78. L. O. Gilpatrick   
79. M. J. Goglia   
80. W.R.Grimes   
81. A. G. Grindell   
82. R.H.Guymon   
83. W. O. Harms   
84. P. N. Haubenreich   
85. P. W. Hembree   
86. P. G. Herndon   
87. J. R. Hightower, Jr.   
88. R.M.Hill   
89. B. F. Hitch   
90. H. W. Hoffman   
91. P. P. Holz   
92. R.W.Horton   
93. W.R.Huntley   
94. C. R. Hyman   
95.P.R.Kasten   
96. C.W. Kee   
97. J.R.Keiser   
98. O. L. Keller   
99. A. D. Kelmers   
100. H. T. Kerr   
101. W.R.Leing   
102. J. M. Leitnaker   
103. R.B. Lindauer   
104. M. I. Lundin   
105. R.N.Lyon   
106. R.E. MacPherson   
107. A. P. Malinauskas   
108. G. Mamantov   
109. D. L. Manning   
110. W. R. Martin   
111. L. Maya   
112. G. T. Mays   
113. W. J. McCarthy, Jr.   
114. H. E. McCoy   
115. H.F. McDuffie   
116. C. J. McHargue

117. H. A. McLain

118. B. McNabb

119. A. S. Meyer

120. R. L. Moore

121. F. H. Neill

122. J.P.Nichols

123. P. Patriarca

124. T. W. Pickel

125. C. B. Pollock

126. F. A. Posey

127. H. Postma

128. T. K. Roche

129. M. W. Rosenthal

130. A. D. Ryon

131. H. C. Savage

132. W.F. Scheffer, Jr.

133. C. D. Scott

134. H. E. Seagren

135. J. H. Shaffer

136. Myrtleen Sheldon

137. W. D. Shults

138. M. D. Silverman

139. M. J. Skinner

140. A. N. Smith

141. F. J. Smith

142. G.P. Smith

143. I. Spiewak

144. J. O. Stiegler

145. R.A. Strehlow

146. O.K. Tallent

147. J. J. Taylor

148. R.E.Thoma

149. J. A. Thompson

150. L. M. Toth

151. D. B. Trauger

152. W. E. Unger

153. D. Y. Valentine

154. W. C. Waggener

155. T. N. Washburn

156. J.R.Weir

157. J.C. White

158. G. D. Whitman

159. W.J.Wilcox

160. M. K. Wilkinson

161. W. R. Winsbro

162. J. W. Woods

163. R.G.Wymer

164. G. T. Yahr

165. J.P. Young

166. E. L. Youngblood

167-168. Central Research Library

169. Document Reference Section

170-172. Laboratory Records Department

173. Laboratory Records (LRD-RC)

174-176. MSRP Director's Office,

Bldg. 450ONM, Rm. 147

# External Distribution

177-178. Director, Division of Reactor Research and Development, ERDA, Washington, D. C. 20545

179. Director, Reactor Division, ERDA, ORO

180. Research and Technical Support Division, ERDA, ORO

181-284. For distribution as shown in TID-4500 under UC-76, Molten-Salt Reactor Technology