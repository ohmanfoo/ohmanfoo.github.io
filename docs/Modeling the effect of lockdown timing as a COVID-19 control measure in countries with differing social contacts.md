---
created: 2021-06-09T10:46:04 (UTC -04:00)
tags: []
source: https://www.nature.com/articles/s41598-021-82873-2
author: Mustafa Al-Zoughool
---

# Modeling the effect of lockdown timing as a COVID-19 control measure in countries with differing social contacts | Scientific Reports

> ## Excerpt
> The application, timing, and duration of lockdown strategies during a pandemic remain poorly quantified with regards to expected public health outcomes. Previous projection models have reached conflicting conclusions about the effect of complete lockdowns on COVID-19 outcomes. We developed a stochastic continuous-time Markov chain (CTMC) model with eight states including the environment (SEAMHQRD-V), and derived a formula for the basic reproduction number, R0, for that model. Applying the 
                
                  
                
                $${R}_{0}$$
                
               formula as a function in previously-published social contact matrices from 152 countries, we produced the distribution and four categories of possible 
                
                  
                
                $${R}_{0}$$
                
               for the 152 countries and chose one country from each quarter as a representative for four social contact categories (Canada, China, Mexico, and Niger). The model was then used to predict the effects of lockdown timing in those four categories through the representative countries. The analysis for the effect of a lockdown was performed without the influence of the other control measures, like social distancing and mask wearing, to quantify its absolute effect. Hypothetical lockdown timing was shown to be the critical parameter in ameliorating pandemic peak incidence. More importantly, we found that well-timed lockdowns can split the peak of hospitalizations into two smaller distant peaks while extending the overall pandemic duration. The timing of lockdowns reveals that a “tunneling” effect on incidence can be achieved to bypass the peak and prevent pandemic caseloads from exceeding hospital capacity.

---
## Abstract

The application, timing, and duration of lockdown strategies during a pandemic remain poorly quantified with regards to expected public health outcomes. Previous projection models have reached conflicting conclusions about the effect of complete lockdowns on COVID-19 outcomes. We developed a stochastic continuous-time Markov chain (CTMC) model with eight states including the environment (SEAMHQRD-V), and derived a formula for the basic reproduction number, R0, for that model. Applying the \\({R}\_{0}\\) formula as a function in previously-published social contact matrices from 152 countries, we produced the distribution and four categories of possible \\({R}\_{0}\\) for the 152 countries and chose one country from each quarter as a representative for four social contact categories (Canada, China, Mexico, and Niger). The model was then used to predict the effects of lockdown timing in those four categories through the representative countries. The analysis for the effect of a lockdown was performed without the influence of the other control measures, like social distancing and mask wearing, to quantify its absolute effect. Hypothetical lockdown timing was shown to be the critical parameter in ameliorating pandemic peak incidence. More importantly, we found that well-timed lockdowns can split the peak of hospitalizations into two smaller distant peaks while extending the overall pandemic duration. The timing of lockdowns reveals that a “tunneling” effect on incidence can be achieved to bypass the peak and prevent pandemic caseloads from exceeding hospital capacity.

## Introduction

A cluster of viral pneumonia cases led to identification of a new coronavirus disease 2019 (COVID-19) first reported in Wuhan, China on December 31, 2019. Subsequent reports of human transmission[1](https://www.nature.com/articles/s41598-021-82873-2#ref-CR1 "Majumder, M. & Mandl, K. Early Transmissibility Assessment of a Novel Coronavirus in Wuhan, China (January 26, 2020). 
https://ssrn.com/abstract=3524675
or 
https://doi.org/10.2139/ssrn.3524675
.") and travel-related cases[2](https://www.nature.com/articles/s41598-021-82873-2#ref-CR2 "World Health Organization. Statement on Novel Coronavirus in Thailand. Jan 13, 2020. 
https://www.who.int/news-room/detail/13-01-2020-who-statement-on-novel-coronavirus-in-thailand
.") seeded outbreaks in many other countries. The WHO declared a global pandemic, Phase 6 emergency on January 30, 2020[3](https://www.nature.com/articles/s41598-021-82873-2#ref-CR3 "World Health Organization. Statement on the second meeting of the International Health Regulations (2005) Emergency Committee regarding the outbreak of novel coronavirus (2019-nCoV). Jan 30, 2020. 
https://www.who.int/news-room/detail/30-01-2020-statement-on-the-second-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-outbreak-of-novel-coronavirus-(2019-ncov
) (2020).").

Different country responses to early identified travel-related cases included quarantines and contact tracing[4](https://www.nature.com/articles/s41598-021-82873-2#ref-CR4 "Pan, A. et al. Association of public health interventions with the epidemiology of the COVID-19 outbreak in Wuhan, China. JAMA 323(19), 1915–1923. 
https://doi.org/10.1001/jama.2020.6130
(2020).") to identify and isolate potentially infected individuals, as containment measures. As the outbreaks developed, countries increased diagnostic testing of individuals with COVID-19 risk factors, respiratory symptoms and influenza like illness. However, once widespread local community was confirmed, transmission was present, frequently followed by discrete acceleration events[5](https://www.nature.com/articles/s41598-021-82873-2#ref-CR5 "Schuchat, A. Public health response to the initiation and spread of pandemic COVID-19 in the United States, February 24–April 21, 2020. MMWR Morb. Mortal. Wkly. Rep. 69, 551–556. 
https://doi.org/10.15585/mmwr.mm6918e2external
(2020)."), it rapidly overwhelmed the ability of many public health departments to conduct effective contact tracing and that of the health care system to take care of patients with critical, severe, and moderately severe illness; In response, many jurisdictions adopted mitigation broader strategies to manage the outbreak and slow down the rate of transmissions within the country such as social distancing, quarantines and lockdowns.

The surge in COVID-19 cases during the global pandemic put substantial strain on hospitals and intensive care units in China and other countries[6](https://www.nature.com/articles/s41598-021-82873-2#ref-CR6 "Porcheddu, R., Serra, C., Kelvin, D., Kelvin, N. & Rubino, S. Similarity in case fatality rates (CFR) of COVID-19/SARS-COV-2 in Italy and China. J. Infect. Dev. Ctries. 14(2), 125–128 (2020)."). Interventions in China showed that contact tracing with quarantine, social distancing, and lockdowns to isolate cities and regions with community transmission was effective. The interventions in China were encouraging for modulating and containing the COVID-19 outbreak.

Non-pharmaceutical interventions (NPIs) that limit contact between individuals are proven to be efficacious in reducing COVID-19 transmission[7](https://www.nature.com/articles/s41598-021-82873-2#ref-CR7 "Flaxman, S. et al. Estimating the effects of non-pharmaceutical interventions on COVID-19 in Europe. Nature 
https://doi.org/10.1038/s41586-020-2405-7
(2020)."). Contact limiting strategies include school closures, workplace closures (e.g. work-from-home mandate), stay at home orders and restrictions (e.g. for individuals, regions or entire countries), preventing gatherings (e.g. cancellation of larger events and smaller meetings), limiting visitors to institutional settings (e.g. hospitals, long term care facilities and prisons), voluntary or involuntary quarantine of potentially exposed individuals, quarantine of buildings, regions or lockdowns of entire countries (e.g. stopping most border traffic and international air travel). Various intervention strategies to reduce transmission can be utilized and are viewed as temporary public health measures[8](https://www.nature.com/articles/s41598-021-82873-2#ref-CR8 "Güner, R., Hasanoğlu, I. & Aktaş, F. COVID-19: Prevention and control measures in community. Turk. J. Med. Sci. 50(SI-1), 571–577 (2020).").

Limiting contact is a strategy that attempts to decrease both the frequency and duration of contacts which in turn reduces the basic reproduction number, R0, the average number of persons to whom one case transmits the disease during his/her incubation period. Studies on social contact estimated that schools and daycare centers were the most socially dense locations compared with offices and homes[9](https://www.nature.com/articles/s41598-021-82873-2#ref-CR9 "Ebrahim, S. H., Ahmed, Q. A., Gozzer, E., Schlagenhauf, P. & Memish, Z. A. Covid-19 and community mitigation strategies in a pandemic. BMJ 368, m1066 (2020)."). When school closures and work-from-home strategies are activated, the transmission dynamics shift to the within-households contacts. In this regard, family structures, country population density, country population demographics, and socioeconomics can affect the number of social contacts occurring within the home. In addition, there is a problem of increased contact between individuals house-to-house, which may warrant a complete lockdown within the home.

China was the first country that implemented a regional lockdown of cities in Hubei province as a control measure. The largest city in Hubei province is Wuhan with a population of over 14 million people which used a full lockdown that lasted 76-days[10](https://www.nature.com/articles/s41598-021-82873-2#ref-CR10 "Zhou, T., Nguyen, T. T., Zhong, J. & Liu, J. A COVID-19 descriptive study of life after lockdown in Wuhan, China. R. Soc. Open Sci. 7(9), 200705. 
https://doi.org/10.1098/rsos.200705
(2020).").

Other countries later followed using similar “Wuhan-style” lockdowns including Italy (provinces of Lombardy and Veneto), Spain, Russia, India and the Philippines[11](https://www.nature.com/articles/s41598-021-82873-2#ref-CR11 "Buchholz, K. Strict or Lenient? COVID-19 Lockdowns Compared. Statistica. June 18. 
https://www.statista.com/chart/22048/university-of-oxford-coronavirus-containment-and-health-index-selected-countries/
(2020)."), [12](https://www.nature.com/articles/s41598-021-82873-2#ref-CR12 "Lee, L., Gan, N. & Culver, E. (2020). Lockdowns are being imposed around the world. China's example highlights the costs. CNN. March 17. 
https://www.cnn.com/2020/03/16/asia/coronavirus-xi-wuhan-anger-intl-hnk/index.html
.").

Countries used different lengths of lockdowns with different timing. For example, lockdowns ranged in lengths as short as 4 days in Turkey to as long as nearly 300 days in Qatar[13](https://www.nature.com/articles/s41598-021-82873-2#ref-CR13 "Hürriyet Daily News. Turkey to impose four-day lockdown. April 20. 
https://www.hurriyetdailynews.com/turkey-to-impose-four-day-lockdown-154053
(2020)."), [14](https://www.nature.com/articles/s41598-021-82873-2#ref-CR14 "Reuters. Qatar to lift lockdown in four phases from June 15. Reuters. June 8. 
https://www.reuters.com/article/us-health-coronavirus-qatar-idUSKBN23F2KD
(2020)."). Often lockdowns were put in place and then extended repeatedly for short periods of time (2–3 weeks) as the governments reassessed the country’s situation[15](https://www.nature.com/articles/s41598-021-82873-2#ref-CR15 "Sandhu, K. K. Coronavirus: Lockdown extended for 2 weeks, business activities to resume based on zones. India Times. May 1. 
https://www.indiatoday.in/india/story/covid-19-mha-extends-nationwide-lockdown-by-another-14-days-1673394-2020-05-01
(2020)."). In the United States a nationwide lockdown was not used, instead many individual states put lockdowns in place of various lengths ranging from 20 to 267 days[16](https://www.nature.com/articles/s41598-021-82873-2#ref-CR16 "Bartkowiak, Jr, D. Michigan governor issues ‘stay-at-home’ order as COVID-19 cases increase. March 23. 
https://www.clickondetroit.com/news/local/2020/03/23/watch-live-michigan-gov-whitmer-to-provide-update-on-states-covid-19-response-efforts/
(2020)."), [17](https://www.nature.com/articles/s41598-021-82873-2#ref-CR17 "Calfas, J., Stancati, M. & Yap, C.-W. California Orders Lockdown for State's 40 Million Residents. Wall Street J. March 19. 
https://www.wsj.com/articles/china-reports-no-new-domestic-coronavirus-infections-for-the-first-time-since-outbreak-started-11584611233
(2020)."). In many countries lockdowns were slowly reduced over several months in predetermined phases that eased curfew and lockdown orders. A small number of countries did not use lockdowns at all with COVID-19 outcomes similar to countries that did use them[18](https://www.nature.com/articles/s41598-021-82873-2#ref-CR18 "Yamamoto, T., Uchiumi, C., Suzuki, N., Yoshimoto, J., & Murillo-Rodriguez, E. (2020). The psychological impact of ‘mild lockdown’ in Japan during the COVID-19 pandemic: a nationwide survey under a declared state of emergency. Preprint at 
https://doi.org/10.1101/2020.07.17.20156125
(2020)."),[19](https://www.nature.com/articles/s41598-021-82873-2#ref-CR19 "Lee, S. M. & Lee, D. Lessons learned from battling COVID-19: The Korean experience. Int. J. Environ. Res. Public Health 17(20), 7548. 
https://doi.org/10.3390/ijerph17207548
(2020)."),[20](https://www.nature.com/articles/s41598-021-82873-2#ref-CR20 "Kirby, J. What we can learn from the “second wave” of coronavirus cases in Asia. Vox.com. April 17. 
https://www.vox.com/2020/4/17/21213787/coronavirus-asia-waves-hong-kong-singapore-taiwan
(2020).").

Modelling with data fitted to Wuhan’s lockdown in China revealed a positive effect reducing the contact rate through isolation and quarantine that decreased and delayed COVID-19 infections[21](https://www.nature.com/articles/s41598-021-82873-2#ref-CR21 "Hou, C. et al. The effectiveness of quarantine of Wuhan city against the Corona Virus Disease 2019 (COVID-19): A well-mixed SEIR model analysis. J. Med. Virol. 92(7), 841–848. 
https://doi.org/10.1002/jmv.25827
(2020)."). Experts estimated that the Wuhan lockdown prevented between 0.5 and 3 million infections and 18,000–70,000 deaths in the city at the expense of negative impacts to the economy and restrictions to personal freedoms[22](https://www.nature.com/articles/s41598-021-82873-2#ref-CR22 "Bei, T. The real reason China is pushing for a better global response to the Covid-19 pandemic. The South China Morning Post. November 14. 
https://www.scmp.com/comment/opinion/article/3109634/real-reason-china-pushing-better-global-response-covid-19-pandemic
(2020)."). Bonacini et al. showed that the lockdown measures introduced in Italy generated a reducing effect on the trend of COVID-19 cases[23](https://www.nature.com/articles/s41598-021-82873-2#ref-CR23 "Bonacini, L., Gallo, G., & Patriarca, F. Identifying policy challenges of COVID-19 in hardly reliable data and judging the success of lockdown measures. J. Popul. Econ. 1–27. Advance online publication (2020). 
https://doi.org/10.1007/s00148-020-00799-x
."). Overall, the effect of lockdowns appears to be positive but difficult to quantify given the application of differing lengths, timing, and other interventions. Moreover, other research studies suggest ongoing uncertainty over whether lockdown measures are sufficient to control 2019-nCoV[24](https://www.nature.com/articles/s41598-021-82873-2#ref-CR24 "Wilder-Smith, A. & Freedman, D. O. Isolation, quarantine, social distancing and community containment: Pivotal role for old-style public health measures in the novel coronavirus (2019-nCoV) outbreak. J. Travel Med. 27(2), taaa020 (2020)."). There was significant heterogeneity in the way that lockdowns were applied for both their timing and duration and there was difficulty determining whether the lockdowns were a useful tool for COVID-19 attenuation.

Even though research has investigated and modelled many aspects of lockdown for its policy[25](https://www.nature.com/articles/s41598-021-82873-2#ref-CR25 "Alvarez, F., Argente, D. & Lippi, F. A simple planning problem for COVID-19 lockdown, testing, and tracing. Am. Econ. Rev. 
https://doi.org/10.3386/w26981
(2020)."), economic implications of lockdown[26](https://www.nature.com/articles/s41598-021-82873-2#ref-CR26 "Garibaldi, P., Moen, E., & Pissarides, C. Covid Economics Vetted and Real-Time Papers. CEPR; 2020. June 3. Modelling contacts and transitions in the SIR epidemics model. 
https://web.unicz.it/admin/uploads/2020/06/covideconomics25.pdf
(2020)."), mental health impacts[27](https://www.nature.com/articles/s41598-021-82873-2#ref-CR27 "Singh, S. et al. Impact of COVID-19 and lockdown on mental health of children and adolescents: A narrative review with recommendations. Psychiatry Res. 293, 113429. 
https://doi.org/10.1016/j.psychres.2020.113429
(2020)."), and environmental impacts[28](https://www.nature.com/articles/s41598-021-82873-2#ref-CR28 "Nakada, L. & Urban, R. C. COVID-19 pandemic: Impacts on the air quality during the partial lockdown in São Paulo state, Brazil. Sci. Total Environ. 730, 139087. 
https://doi.org/10.1016/j.scitotenv.2020.139087
(2020).") the evidence base of when to apply a lockdown and for how long to maximize its effect on incidence and hospitalizations as an intervention is not well reported.

We define lockdown effectiveness as the ability to reduce the basic reproduction number, reduce the total incidence and reduce the peak of hospitalization. To better understand the effect of lockdown dynamics for duration and timing, we created a stochastic continuous-time Markov chain model to analyze different hypothetical lockdown scenarios for four representative countries (Canada, China, Mexico, and Niger). The countries were chosen for their variation in social contact rates and ordered by increasing contacts using a scale of differential contract rates based on \\({R}\_{0}\\).

## Methods and model

### Model description

We used an SEAMHQRD-V disease transmission model to depict the spread of SARS-CoV 2 (the cause of COVID-19) in the community, and within households. The model is constructed from a stochastic continuous-time Markov chain (CTMC) with eight states or compartments: susceptible (S), exposed (E), infected but asymptomatic (A), mildly infected and symptomatic (M), severely infected, symptomatic and hospitalized (H), detected and quarantined (Q), recovered (R), and dead (D) (Fig. [1](https://www.nature.com/articles/s41598-021-82873-2#Fig1)). The equivalent number of infected persons represented by deposition of virus particles by infected persons (A + M) in the environment is denoted by V, with removal of virus from the environment by ρ. Compartments were split into three age groups: children (0–18 years), denoted by a (c) subscript, adults (19–64 years) denoted by an (a) subscript, and senior (65 years and more), denoted by an (s) subscript. The possible transitions of individuals between compartments are represented by arrows with rates given above the arrows in Fig. [1](https://www.nature.com/articles/s41598-021-82873-2#Fig1). The subpopulation sizes are denoted by \\({N}\_{c}\\), \\({N}\_{a}\\), and \\({N}\_{s}\\), respectively, and they add up to the total population size \\(N\\) which is assumed to be fixed. See the supplementary material ([S1](https://www.nature.com/articles/s41598-021-82873-2#MOESM1). Model Description) for full description and Table [S3](https://www.nature.com/articles/s41598-021-82873-2#MOESM1) for definition of model’s parameters. We used the methods introduced by Allen and van den Driessche[29](https://www.nature.com/articles/s41598-021-82873-2#ref-CR29 "Allen, L. J. & van den Driessche, P. Relations between deterministic and stochastic thresholds for disease extinction in continuous- and discrete-time infectious disease models. Math. Biosci. 243(1), 99–108 (2013).") to derive \\({R}\_{0}\\) for the CTMC model by approximating it by a multi-type branching process[29](https://www.nature.com/articles/s41598-021-82873-2#ref-CR29 "Allen, L. J. & van den Driessche, P. Relations between deterministic and stochastic thresholds for disease extinction in continuous- and discrete-time infectious disease models. Math. Biosci. 243(1), 99–108 (2013)."), see supplementary material ([S2](https://www.nature.com/articles/s41598-021-82873-2#MOESM1). The Basic Reproduction Number \\({R}\_{0}\\) and Probability of Extinction).

**Figure 1**

[![figure1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig1_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/1)

Schematic diagram of transitions of individuals between compartments in which transmission and transition rates are indicated over the arrows. See Table [S3](https://www.nature.com/articles/s41598-021-82873-2#MOESM1) for definition of model’s parameters. The force of infection \\({\\Lambda }\_{j}\\) is given in Eq. ([1](https://www.nature.com/articles/s41598-021-82873-2#Equ1)), which depends on the environmental contact matrix _(C__V__)_ and social contact matrices _(C)_ for school, work, household, and other.

We used the CTMC to simulate different epidemiological measures and find their statistics. The first measure was the actual incidence, defined to be the proportion of the newly infected individuals to the population every day over the course of the epidemic. The second measure was the total attack rate, defined as the fraction of people that contract the disease in an at-risk population over the epidemic period. The third measure is hospital case load, defined to be the fraction of the population that is hospitalized for COVID-19 treatment at any given time and find its peak. We used the total population as the denominator for all of the measures so as to be able to compare between different counties with different population sizes.

$${\\Lambda }\_{j}={\\beta }\_{j} \\left(\\sum\_{i=c,a,s}{C}\_{ji}^{V}{V}\_{i}+\\sum\_{i=c,a,s}{C}\_{ji}\\frac{\\left({A}\_{i}+{M}\_{i}\\right)}{{N}\_{i}}\\right), \\quad \\text{ for }\\;\\;j= c, a, \\text{and} \\;\\;s.$$

(1)

The social contact matrices used in the CTMC model were adapted from the study by Prem et al.[30](https://www.nature.com/articles/s41598-021-82873-2#ref-CR30 "Prem, K., Cook, A. R. & Jit, M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. PLoS Comput. Biol. 13(9), e1005697 (2017)."), which projected the data from population-based contact diaries in eight European countries from the POLYMOD study[31](https://www.nature.com/articles/s41598-021-82873-2#ref-CR31 "Mossong, J. et al. Social contacts and mixing patterns relevant to the spread of infectious diseases. PLoS Med. 5(3), e74 (2008).") to 144 other countries using a Bayesian hierarchical model that estimated age-and-location-specific contact patterns for the different countries. Applying household-level demographic and health survey data from the 152 countries to Markov chain Monte Carlo simulations, they produced five different types of social contact rates for various settings: work, school, home, other and all. The resulting social contact matrices were available for 5-year age increments from age 0 to 80.

To calculate the contact rates for our study for the assigned age groups of 0–18, 19–64 and 65+ , we added up the contact rates of all columns (of the consequents) of the matrices (see [Supplementary Material S1](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)) representing age increments in each of these three age categories, and then averaged the totals across the rows (of the antecedent) for the corresponding compiled age groups. We assumed that environmental contact matrix is a proportion \\(r\\) of the all-contact matrix. The home contact matrix was normalized by the number of household members in each age group[32](https://www.nature.com/articles/s41598-021-82873-2#ref-CR32 "Pellis, L. et al. Systematic selection between age and household structure for models aimed at emerging epidemic predictions. Nat. Commun. 
https://doi.org/10.1038/s41467-019-14229-4
(2020)."). We obtained data about household sizes and population sizes classified by age groups in different countries from the United Nations, Department of Economic and Social Affairs, Population Dynamics[33](https://www.nature.com/articles/s41598-021-82873-2#ref-CR33 "United Nations. 2019. Data Query. Department of Economic and Social Affairs Population Dynamics. 
https://population.un.org/wpp/DataQuery/
(2020).").

We used the formula of \\({R}\_{0}\\) (calculated at β = 3.5%) as a function in the contact matrices and demographics to produce the distribution and four categories of \\({R}\_{0}\\) for the 152 countries (Fig. [S1](https://www.nature.com/articles/s41598-021-82873-2#MOESM1))[30](https://www.nature.com/articles/s41598-021-82873-2#ref-CR30 "Prem, K., Cook, A. R. & Jit, M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. PLoS Comput. Biol. 13(9), e1005697 (2017)."); and chose one country from each quartile as a representative for each of four social contract categories. For this procedure, it was assumed that the probability of infection is the same in all situations and places. Quartiles of \\({R}\_{0}\\) split the countries into four groups (see [S3](https://www.nature.com/articles/s41598-021-82873-2#MOESM1). Countries Categorization for more details). We picked one country from each one of the four categories, that would also fall in a different continent: Canada, China, Mexico, and Niger; increasing from the lowest to the highest social contact category. The choice of countries taken from the four quartile groups serve two purposes. First, the country chosen represented its quartile. Secondly, we attempted to choose representative countries that would showcase the diversity of social contacts given widely varying lifestyle conditions, GDP, and geography. We chose Canada (North America, G-7 country), China (Asian region) Mexico (North America, non-G7 country) and Niger (African region, low income country). Moreover, each of the four chosen quartile countries employed lockdowns of different stringency, timing, and duration.

We used the tau-leap method[34](https://www.nature.com/articles/s41598-021-82873-2#ref-CR34 "Yang, C. & Gillespie, D. T. Efficient step size selection for the tau-leaping simulation method. J. Chem. Phys. 124, 044109 (2006).") to simulate the stochastic CTMC model for 1000 times. It is known that the size of the epidemic has a chance to be zero in CTMC models[35](https://www.nature.com/articles/s41598-021-82873-2#ref-CR35 "Allen, L. J. S. & Lahodny, G. E. Jr. Extinction thresholds in deterministic and stochastic epidemic models. J. Biol. Dyn. 6(2), 590–611 (2012)."), which we exclude given that attack rates cannot, epidemiologically, have a value of zero and the COVID-19 virus has already a significant potential to spread between individuals. In all the simulations, the initial number of infected individuals was assumed to be one adult who is mildly infected. The list of parameters of the model, their description and values are shown in Table [S3](https://www.nature.com/articles/s41598-021-82873-2#MOESM1). Some of the parameters were found in the literature or guesstimated by experts and the rest of the parameters are found using calibration. We calibrated the model using the mean scenario that was estimated by[36](https://www.nature.com/articles/s41598-021-82873-2#ref-CR36 "Tang, B. et al. Estimation of the transmission risk of the 2019-nCoV and its implication for public health interventions. J. Clin. Med. 9(2), 462 (2020).") to be \\({R}\_{0}=6.47\\) since the model’s structure in[36](https://www.nature.com/articles/s41598-021-82873-2#ref-CR36 "Tang, B. et al. Estimation of the transmission risk of the 2019-nCoV and its implication for public health interventions. J. Clin. Med. 9(2), 462 (2020).") is very close to our model. That value was also very close to the mean value of the 152 values of \\({R}\_{0}\\) shown in Figure [S1](https://www.nature.com/articles/s41598-021-82873-2#MOESM1). We used that value for all the chosen countries to factor out the effect of the reproduction rate of secondary cases on the influence of the lockdown, thus allowing us to compare between the four countries.

To make a run-by-run comparison of the course of the epidemic with and without the lockdown, we simulated the model using a fixed random seed for each one of the 1000 runs. In all those runs, we assumed that the only control measure is the complete lockdown starting before the peak of the actual incidence and for a specified period. The comparison of the effect of the start of the lockdown was done using two measures, which compute the relative reduction of measure X, RD(X), in \\({R}\_{0}\\), the total attack rate, and peak of hospitalization for the non-zero simulation runs with the following formula,

$$RD\\left(X\\right)=\\frac{{X}\_{0}-{X}\_{lockdown}}{{X}\_{0}}\\times 100$$

(2)

where \\({X}\_{0}\\) is the epidemiological quantity (\\({R}\_{0}\\), attack rate or peak of hospitalization) under no control measure and \\({X}\_{lockdown}\\) is the same measure with the lockdown. The mean, median and 2.5% and 97.5% percentiles of \\(RD\\) were calculated for the two measures. We also simulated the actual incidence and hospitalized normalized by the total population sizes for visual comparisons.

## Results

The basic reproduction number was derived (see [Supplementary Material S2](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)) and found to be proportional to the spectral radius \\((\\rho )\\) of a simple transformation of the contact matrix \\(\\stackrel{\\sim }{{\\varvec{C}}}\\). That is,

$${R}\_{0}=\\rho ({\\varvec{B}})\\left\[(1-p)\\frac{1+r {\\stackrel{\\sim }{\\omega }}\_{A}/\\rho }{{\\mu }\_{A}}+p \\frac{1+r {\\stackrel{\\sim }{\\omega }}\_{M}/\\rho }{q+{\\mu }\_{M}+{\\gamma }\_{M}}\\right\]$$

(3)

where

$${\\varvec{B}}=\\textbf{diag}\\left({\\beta }\_{c}{N}\_{c}, 0, 0, 0 ,{\\beta }\_{a}{N}\_{a}, 0 ,0 ,0 ,{\\beta }\_{s}{N}\_{s} \\right)\\cdot\\stackrel{\\sim }{{\\varvec{C}}}\\cdot\\textbf{diag}\\left(\\frac{1}{{N}\_{c}}, 0, 0, 0 ,\\frac{1}{{N}\_{a}}, 0, 0, 0, \\frac{1}{{N}\_{s}}\\right)$$

(4)

The matrix \\(\\stackrel{\\sim }{{\\varvec{C}}}\\) is the effective contact matrix based on social limitations (see [Supplementary Material S1](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)). The proportionality constant is dependent on the disease parameters, whereas the matrix \\({\\varvec{B}}\\) depends on social, demographic parameters as well as the transmission probabilities which are dependent on the strength of the virus and human culture and behavior.

The basic reproduction number \\({R}\_{0}\\) given in Eq. ([3](https://www.nature.com/articles/s41598-021-82873-2#Equ3)) shows direct dependence on the rates of viral environmental shedding and the fraction of contacts individuals make with the environment. Decreasing contact with the environment by use of personal protective equipment (PPE) and increasing environmental decontamination by frequent cleaning, disinfection, hand washing will result in a decrease in basic reproduction number. On the other hand, increasing rates of “removal” of both asymptomatic and mild cases, operationalized through contact tracing, isolation and quarantine, will lower the denominators of the term on the right side of Eq. ([3](https://www.nature.com/articles/s41598-021-82873-2#Equ3)) to a degree proportional to the spectral radius of the matrix \\({\\varvec{B}}\\) in Eq. ([4](https://www.nature.com/articles/s41598-021-82873-2#Equ4)). Strict adherence to social distancing and stopping insalubrious cultural habits by the three age groups can decrease the likelihood of disease transmission (through \\(\\beta\\)’s) resulting in shrinking \\({R}\_{0}\\). Meanwhile, \\(\\stackrel{\\sim }{{\\varvec{C}}}\\) can be altered through mutual social limitations by individuals in each age group, like through partial or full lockdowns.

A full lockdown results in a reduction in the basic reproduction number \\({R}\_{0}\\) by more than 64% and up to 85% (Fig. [2](https://www.nature.com/articles/s41598-021-82873-2#Fig2)). We can conclude that with using this model, household contacts and demographics are among the major factors contributing to \\({R}\_{0}\\).

**Figure 2**

[![figure2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig2_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/2)

Histogram of percentage reduction in values of \\({R}\_{0}\\) for the 152 countries[13](https://www.nature.com/articles/s41598-021-82873-2#ref-CR13 "Hürriyet Daily News. Turkey to impose four-day lockdown. April 20. 
https://www.hurriyetdailynews.com/turkey-to-impose-four-day-lockdown-154053
(2020).") calculated at \\(\\beta =3.5\\%\\) (see Eq. ([2](https://www.nature.com/articles/s41598-021-82873-2#Equ2))). The percentage reduction of the four selected countries are as follows: Canada 82%, China 76%, Mexico 74%, and Niger 73%.

The start and length of lockdown affects attack rates, and hospital flux (Figs. [3](https://www.nature.com/articles/s41598-021-82873-2#Fig3) and [4](https://www.nature.com/articles/s41598-021-82873-2#Fig4)) with different degrees. This is consistent with the various possible levels of reduction in the basic reproduction numbers as can be seen in Fig. [2](https://www.nature.com/articles/s41598-021-82873-2#Fig2). While the magnitude of relative reduction is not the same for the four selected counties, the consequences of timing and length of lockdown appears to be consistent. It appears that starting a complete lockdown will have its optimal reduction on the total attack rate if it starts 5 days before the peak of the actual incidence and lasts for 90 days. While starting a 90-days lockdown 30 days before the peak has a small relative reduction of the total attack rate (Fig. [2](https://www.nature.com/articles/s41598-021-82873-2#Fig2)), it reduces the peak of the actual incidence (Fig. [S4](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)). Shorter lockdowns seem to be of larger relative effect on the total attack rate if they start close enough to the peak of the actual incidence.

**Figure 3**

[![figure3](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig3_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/3)

Mean of percentage relative reduction in COVID-19 total attack rates (see Eq. ([2](https://www.nature.com/articles/s41598-021-82873-2#Equ2))) for (**a**) Canada, (**b**) China, (**c**) Mexico, and (**d**) Niger. They are calculated at \\({R}\_{0}=6.47\\), with initially one adult mild infection. Bars to the right of the figures are percentages.

**Figure 4**

[![figure4](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig4_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/4)

Mean of percentage relative reduction in peak of COVID-19 hospitalization (see Eq. ([2](https://www.nature.com/articles/s41598-021-82873-2#Equ2))) for (**a**) Canada, (**b**) China, (**c**) Mexico, and (**d**) Niger. They are calculated at \\({R}\_{0}=6.47\\), with initially one adult mild infection. Bars to the right of the figures are percentages.

Lockdown, however, has its maximum effect on the hospital case load if it starts 15 days to 20 days prior to the peak of actual incidence, See Fig. [4](https://www.nature.com/articles/s41598-021-82873-2#Fig4). The timing is less consistent between the four countries but shows an overall qualitative resemblance. It appears that a shorter than a 90-days lockdown can achieve the goal of hospital caseload reduction.

The optimality results are significant to a large degree as could be seen in the 95% quartiles interval of the percentage reduction in attack rate and hospitalization flux shown in Figs. [S2](https://www.nature.com/articles/s41598-021-82873-2#MOESM1) and [S3](https://www.nature.com/articles/s41598-021-82873-2#MOESM1).

While the location of the peak of the proportion of the actual incidence of COVID-19 cases to the total population is different for the four countries, the magnitudes of the peaks are very close, as shown in Figs. [5](https://www.nature.com/articles/s41598-021-82873-2#Fig5), [6](https://www.nature.com/articles/s41598-021-82873-2#Fig6), [7](https://www.nature.com/articles/s41598-021-82873-2#Fig7), [8](https://www.nature.com/articles/s41598-021-82873-2#Fig8)a, which might be an outcome of the contact matrices and demographics while keeping \\({R}\_{0}\\) constant. Starting the lockdown 15 days before the actual incidence’s peak results in a tunneling effect of the incidence curve as seen in the simulation runs and their average, Figs. [5](https://www.nature.com/articles/s41598-021-82873-2#Fig5), [6](https://www.nature.com/articles/s41598-021-82873-2#Fig6), [7](https://www.nature.com/articles/s41598-021-82873-2#Fig7), [8](https://www.nature.com/articles/s41598-021-82873-2#Fig8)b (see also Fig. [S4](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)), which resulted in a decrease in the magnitude of the attack rates. The tunneling effect appears as a theoretical solution in environmental Kuznets curves of pollution emission[37](https://www.nature.com/articles/s41598-021-82873-2#ref-CR37 "Munasinghe, M. Is environmental degradation an inevitable consequence of economic growth: Tunneling through the environmental Kuznets curve. Ecol. Econ. 29(1), 89–109 (1999)."). Here it also results in dividing the flux of cases arriving at hospitals into two distinct, smaller peaks which would allow hospitals to deal with a smaller initial peak before restocking for the second smaller peak, Figs. [5](https://www.nature.com/articles/s41598-021-82873-2#Fig5), [6](https://www.nature.com/articles/s41598-021-82873-2#Fig6), [7](https://www.nature.com/articles/s41598-021-82873-2#Fig7), [8](https://www.nature.com/articles/s41598-021-82873-2#Fig8)c,d. Dividing the peak of hospitalization into two smaller peaks creates a more manageable outbreak scenario. Thus, hospitals can “divide and conquer” the expected larger peak of cases with a well-timed lockdown. The benefit of not exceeding hospital capacity is decreased mortality (not explicitly modeled here).

**Figure 5**

[![figure5](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig5_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/5)

The course of the actual incidence (**a**) and (**b**), and fraction of hospitalized COVID-19 infected individuals (**c**) and (**d**) in Canada with no control measure (left panel) and with starting lockdown (right panel) of 15 days before the peak and that lasts for 90 days. They are calculated at \\({R}\_{0}=6.47\\), with initially one adult mild infection. The grey curves are resulting from the stochastic model simulations and the black curve is the mean of those grey curves. They are all normalized by the population size.

**Figure 6**

[![figure6](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig6_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/6)

The course of the actual incidence (**a**) and (**b**), and fraction of hospitalized COVID-19 infected individuals (**c**) and (**d**) in China with no control measure (left panel) and with starting lockdown (right panel) of 15 days before the peak and that lasts for 90 days. They are calculated at \\({R}\_{0}=6.47\\), with initially one adult mild infection. The grey curves are resulting from the stochastic model simulations and the black curve is the mean of those grey curves. They are all normalized by the population size.

**Figure 7**

[![figure7](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig7_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/7)

The course of the actual incidence (**a**) and (**b**), and fraction of hospitalized COVID-19 infected individuals (**c**) and (**d**) in Mexico with no control measure (left panel) and with starting lockdown (right panel) of 15 days before the peak and that lasts for 90 days. They are calculated at \\({R}\_{0}=6.47\\), with initially one adult mild infection. The grey curves are resulting from the stochastic model simulations and the black curve is the mean of those grey curves. They are all normalized by the population size.

**Figure 8**

[![figure8](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig8_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/8)

The course of the actual incidence of COVID-19 (**a**) and (**b**), and fraction of hospitalized infected individuals (**c**) and (**d**) in Niger with no control measure (left panel) and with starting lockdown (right panel) of 15 days before the peak and that lasts for 90 days. They are calculated at \\({R}\_{0}=6.47\\), with initially one adult mild infection. The grey curves are resulting from the stochastic model simulations and the black curve is the mean of those grey curves. They are all normalized by the population size.

While the effect of the length of the lockdown on the two measures is expected, the effect of its start is subtle. In Fig. [9](https://www.nature.com/articles/s41598-021-82873-2#Fig9), we can see some transitions in the hospitalizations based on the decision to start the lockdown according to the four timing options 20, 15, 10, and 5 days before the actual incidence peaks. The model output shows the 15-days before the peak lockdown option to be the most effective for Canada and China while the 20-days option seems best for Mexico and Niger.

**Figure 9**

[![figure9](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-021-82873-2/MediaObjects/41598_2021_82873_Fig9_HTML.png)](https://www.nature.com/articles/s41598-021-82873-2/figures/9)

Hospitalization flux (proportion of COVD-19 cases requiring hospitalization) for Canada, China, Mexico, and Niger at four different times (days) of starting the lockdown before the peak. They are calculated at \\({R}\_{0}=6.47\\), with initial one adult mild infection. The grey curves are resulting from the stochastic model simulations and the black curve is the mean of those grey curves. They are all normalized by the population size.

Similarly, the actual incidence shows transitions (Fig. [S4](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)) with the maximum effect on the peak happening when the lockdown starts 15–20 days before the peak of the actual incidence. Simulations of the total attack rates show reductions consistent with the results (Figs. [S5](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)–[8](https://www.nature.com/articles/s41598-021-82873-2#MOESM1)).

## Discussion

Continuous time Markov chain models are regularly used to model transmission of diseases. To date most of the work done to model COVID-19 has used deterministic modelling which gives an approximation of the mean of the stochastic epidemic curves[29](https://www.nature.com/articles/s41598-021-82873-2#ref-CR29 "Allen, L. J. & van den Driessche, P. Relations between deterministic and stochastic thresholds for disease extinction in continuous- and discrete-time infectious disease models. Math. Biosci. 243(1), 99–108 (2013)."), [38](https://www.nature.com/articles/s41598-021-82873-2#ref-CR38 "Greenwood, P. E. & Gordillo, L. F. Stochastic epidemic modeling. In Mathematical and Statistical Estimation. 366, Approaches in Epidemiology. 31–52. (Springer, Berlin, 2009)."),[39](https://www.nature.com/articles/s41598-021-82873-2#ref-CR39 "Carcione, J. M., Santos, J. E., Bagaini, C. & Ba, J. A simulation of a COVID-19 epidemic based on a deterministic SEIR model. Front. Public Health. 8, 230 (2020)."),[40](https://www.nature.com/articles/s41598-021-82873-2#ref-CR40 "Reno, C. et al. Forecasting COVID-19-associated hospitalizations under different levels of social distancing in Lombardy and Emilia-Romagna, Northern Italy: Results from an extended SEIR compartmental model. J. Clin. Med. 9(5), 1492 (2020)."). However, the deterministic curves will miss the likely timing of the peak of incidence since averaging over values does not imply averaging over time. The outputs of our carefully crafted simulations of the (stochastic) CTMC model demonstrate that the timing of the lockdown relative to the epidemic peak is a key factor in controlling COVID-19 and prevent hospital systems from becoming overwhelmed.

According to this CTMC model, countries with different social contact rates revealed that the optimal starting time to decrease the total attack rate occurs when the lockdown begins about 5 days before the actual peak of the epidemic, which is the peak of incidence. Benefits from lockdown in terms of relative reduction in COVID-19 hospitalizations are also observed around 15–20 days before the epidemic peak. This provides a limited window for public health decision-makers to mobilize and take full advantage of lockdown as an NPI. Lockdowns appear to have a maximum effect if they start close to the actual peak of incidence and last for 3 months.

Timing the start of a complete lockdown 30 days or more prior to the epidemic peak will have little appreciable effect on reducing either the total attack rate or the peak of hospitalizations (as shown in Figs. [3](https://www.nature.com/articles/s41598-021-82873-2#Fig3) and [4](https://www.nature.com/articles/s41598-021-82873-2#Fig4)). Accurate knowledge of the actual peak of incidence, not just of the reported cases may be required for optimal control of the epidemic using lockdown as an intervention, but obtaining a realistic timing of the peak and the actual incidence seem unattainable given the uncertainties involving the COVID-19 pandemic.

Starting the lockdown too early or too late can miss the chance of optimal benefit in controlling the disease. The output of this model illustrates that likely there is an optimal window to start the lockdown and provide maximum benefits for COVID-19 incidence and hospitalizations relative to the width of the 95% quantile interval of the location of the peak. Interventions must take into consideration repercussions such as major economic impacts, mental health consequences, and increased morbidity and mortality from non-COVID-19 diseases[41](https://www.nature.com/articles/s41598-021-82873-2#ref-CR41 "Bausch, D. G. Precision physical distancing for COVID-19: An important tool in unlocking the lockdown. Am. J. Trop Med Hyg. 103(1), 22–24 (2020)."). Poor timing will result in a wasted lockdown effort with little impact on the outbreak while incurring economic losses and psychological tolls to the public and healthcare workers during extended isolation including response and lockdown fatigue[42](https://www.nature.com/articles/s41598-021-82873-2#ref-CR42 "World Health Organization. Statement on the fourth meeting of the International Health Regulations (2005) Emergency Committee regarding the outbreak of coronavirus disease (COVID-19). 
https://www.who.int/news-room/detail/01-08-2020-statement-on-the-fourth-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-outbreak-of-coronavirus-disease-(covid-19)
.").

While the decision of when to begin a lockdown will vary from one country to another, based on their specific outbreak context, the knowledge of the location of the actual peaks makes a difference when comparing the difference between starting at 5 days and 15 days before the peak. Knowledge about delays in testing and reporting COVID-19 cases as well as accurate estimates of the epidemic are required to make evidence-based decisions[43](https://www.nature.com/articles/s41598-021-82873-2#ref-CR43 "Harris, J.E. Overcoming reporting delays is critical to timely epidemic monitoring: The case of COVID-19 in New York City. medRxiv 2020.08.02.20159418 (2020).").

When faced with COVID-19, countries have used multiple NPIs concurrently in various combinations and timings including lockdowns to reduce \\({R}\_{0}\\)[44](https://www.nature.com/articles/s41598-021-82873-2#ref-CR44 "Ngonghala, C. N. et al. Mathematical assessment of the impact of non-pharmaceutical interventions on curtailing the 2019 novel Coronavirus. Math. Biosci. 325, 108364 (2020)."). Curbing \\({R}\_{0}\\) (see Eq. [2](https://www.nature.com/articles/s41598-021-82873-2#Equ2)) can be achieved by decreasing the probability of transmission via social distance and changes in cultural norms. Limiting contact, frequent cleaning and environmental disinfection as well as wearing masks and face coverings can also result in a linear decrease in \\({R}\_{0}\\).

Past studies showed that the strongest approach to limit social contacts is achieved through a partial or complete lockdown; e.g. China used aggressive city and regional lockdowns to prevent transmission from symptomatic and asymptomatic cases, thus flattening the epidemic curve and pushing the peak further into the future. Use of strict lockdowns along with other NPIs allow healthcare systems to treat a more manageable caseload and gain time to plan, educate the public, optimize the public health response while advancing efforts for vaccine development[45](https://www.nature.com/articles/s41598-021-82873-2#ref-CR45 "Imai, N. et al. Adoption and impact of non-pharmaceutical interventions for COVID-19. Wellcome Open Res. 5, 59 (2020).").

We modelled hypothetical lockdowns 4 weeks longer than those used in Wuhan and other Chinese cities without other NPIs, revealing that the timing of lockdowns is critical for its effectiveness in reducing actual incidence[46](https://www.nature.com/articles/s41598-021-82873-2#ref-CR46 "Lau, H. et al. The positive impact of lockdown in Wuhan on containing the COVID-19 outbreak in China. J Travel Med. 27(3), taaa037 (2020)."), [47](https://www.nature.com/articles/s41598-021-82873-2#ref-CR47 "Ji, T. et al. Lockdown contained the spread of 2019 novel coronavirus disease in Huangshi city, China: Early epidemiological findings. Clin. Infect. Dis. ciaa390 (2020)."). Our modeling shows the benefit of an accurately timed lockdown which results in a tunneling effect and can provide relief by avoiding overwhelming the hospitals, the public health response capabilities and the health care system. However, the lockdown, while reducing case load, can be expected to extend the duration of the epidemic. Extending its duration could result in unforeseen outcomes in healthcare such as higher immediate healthcare costs (e.g. extended need for personal protective equipment, testing kits, laboratory diagnostics, and increased intense hospital cleaning), decreased utilization of healthcare services for other diseases resulting in worse outcomes and increased mortality (e.g., reduced cancer screening or treatment for heart disease or diabetes), increased incidence of psychological outcomes (e.g., suicide), and health care worker psycho-social impacts (stress, fatigue, and burn out) which may need further evaluation when applying the results of this model.

One important limitation of compartmental models, as used in this paper, are less suitable to model household infection dynamics since homes have limited numbers of individuals and once infected, they are removed from the ongoing epidemic. This modeling weakness is difficult to incorporate by compartmental models in general, so incidence may be overestimated. On the other hand, since household contact rates tend to increase during lockdowns the resulting incidence might also increase, counter-balancing this issue; which we did not incorporate in this model trying to overcome some of the inherent limitations to this type of compartmental modeling of household transmission. Also, all timing scenarios in this paper are subjected to the same limitation and so the qualitative rather than quantitative findings of the paper are to be considered.

In our study the effect of lockdown is considered independently from other public health measures that may have occurred such as social distancing, hand washing and mask wearing which may be considered as a potential weakness in our approach. However, hypothetical lockdowns represent one of the most stringent public health measures that can be implemented to reduce contact rates and viral transmissions in a population. A full lockdown would nearly eliminate transmission outside the home as measured by other studies. For example, the Danish mask study[48](https://www.nature.com/articles/s41598-021-82873-2#ref-CR48 "Bundgaard, H. et al. Effectiveness of adding a mask recommendation to other public health measures to prevent SARS-CoV-2 infection in Danish mask wearers: A randomized controlled trial. Ann. Intern. Med. M20-6817 (2020).") showed the overall effects from mask wearing and social distancing were modest. It was a randomized controlled trial that investigated whether recommending surgical mask use when outside the home reduces wearers' risk for SARS-CoV-2 infection in a setting where masks were uncommon and not among recommended public health measures.

Finally, estimation of the pandemic peak by individual countries at the start of a pandemic with limited epidemiological case data remains a significant challenge for public health officials. Accurately timing lockdowns to achieve a “tunneling effect” is vital to maximize its benefits. We can see the results of this study are not sensitive qualitatively to changes in the contact matrices while quantitatively sensitive.

Our results endorse that hypothetical lockdown scenarios for representative countries (Canada, China, Mexico, and Niger) spanning a continuum of increasing rates of social contact can all benefit from well-timed lockdown interventions.

## Data availability

Data availability is available upon request from the corresponding author.

## Code availability

Code availability is available upon request from the corresponding author.

## References

1.  1.
    
    Majumder, M. & Mandl, K. Early Transmissibility Assessment of a Novel Coronavirus in Wuhan, China (January 26, 2020). [https://ssrn.com/abstract=3524675](https://ssrn.com/abstract=3524675) or [https://doi.org/10.2139/ssrn.3524675](https://doi.org/10.2139/ssrn.3524675).
    
2.  2.
    
    World Health Organization. Statement on Novel Coronavirus in Thailand. Jan 13, 2020. [https://www.who.int/news-room/detail/13-01-2020-who-statement-on-novel-coronavirus-in-thailand](https://www.who.int/news-room/detail/13-01-2020-who-statement-on-novel-coronavirus-in-thailand).
    
3.  3.
    
    World Health Organization. Statement on the second meeting of the International Health Regulations (2005) Emergency Committee regarding the outbreak of novel coronavirus (2019-nCoV). Jan 30, 2020. [https://www.who.int/news-room/detail/30-01-2020-statement-on-the-second-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-outbreak-of-novel-coronavirus-(2019-ncov](https://www.who.int/news-room/detail/30-01-2020-statement-on-the-second-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-outbreak-of-novel-coronavirus-(2019-ncov)) (2020).
    
4.  4.
    
    Pan, A. _et al._ Association of public health interventions with the epidemiology of the COVID-19 outbreak in Wuhan, China. _JAMA_ **323**(19), 1915–1923. [https://doi.org/10.1001/jama.2020.6130](https://doi.org/10.1001/jama.2020.6130) (2020).
    
    [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXhtVertbjK)  [Article](https://doi.org/10.1001%2Fjama.2020.6130)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32275295)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Association%20of%20public%20health%20interventions%20with%20the%20epidemiology%20of%20the%20COVID-19%20outbreak%20in%20Wuhan%2C%20China&journal=JAMA&doi=10.1001%2Fjama.2020.6130&volume=323&issue=19&pages=1915-1923&publication_year=2020&author=Pan%2CA&author=Liu%2CL&author=Wang%2CC) 
    
5.  5.
    
    Schuchat, A. Public health response to the initiation and spread of pandemic COVID-19 in the United States, February 24–April 21, 2020. _MMWR Morb. Mortal. Wkly. Rep._ **69**, 551–556. [https://doi.org/10.15585/mmwr.mm6918e2external](https://doi.org/10.15585/mmwr.mm6918e2external) (2020).
    
    [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXptlWgsrc%253D)  [Article](https://doi.org/10.15585%2Fmmwr.mm6918e2external)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32379733)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7737947)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Public%20health%20response%20to%20the%20initiation%20and%20spread%20of%20pandemic%20COVID-19%20in%20the%20United%20States%2C%20February%2024%E2%80%93April%2021%2C%202020&journal=MMWR%20Morb.%20Mortal.%20Wkly.%20Rep.&doi=10.15585%2Fmmwr.mm6918e2external&volume=69&pages=551-556&publication_year=2020&author=Schuchat%2CA) 
    
6.  6.
    
    Porcheddu, R., Serra, C., Kelvin, D., Kelvin, N. & Rubino, S. Similarity in case fatality rates (CFR) of COVID-19/SARS-COV-2 in Italy and China. _J. Infect. Dev. Ctries._ **14**(2), 125–128 (2020).
    
    [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXnvFWjtr0%253D)  [Article](https://doi.org/10.3855%2Fjidc.12600)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Similarity%20in%20case%20fatality%20rates%20%28CFR%29%20of%20COVID-19%2FSARS-COV-2%20in%20Italy%20and%20China&journal=J.%20Infect.%20Dev.%20Ctries.&volume=14&issue=2&pages=125-128&publication_year=2020&author=Porcheddu%2CR&author=Serra%2CC&author=Kelvin%2CD&author=Kelvin%2CN&author=Rubino%2CS) 
    
7.  7.
    
    Flaxman, S. _et al._ Estimating the effects of non-pharmaceutical interventions on COVID-19 in Europe. _Nature_ [https://doi.org/10.1038/s41586-020-2405-7](https://doi.org/10.1038/s41586-020-2405-7) (2020).
    
    [Article](https://doi.org/10.1038%2Fs41586-020-2405-7)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=33361788)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Estimating%20the%20effects%20of%20non-pharmaceutical%20interventions%20on%20COVID-19%20in%20Europe&journal=Nature&doi=10.1038%2Fs41586-020-2405-7&publication_year=2020&author=Flaxman%2CS) 
    
8.  8.
    
    Güner, R., Hasanoğlu, I. & Aktaş, F. COVID-19: Prevention and control measures in community. _Turk. J. Med. Sci._ **50**(SI-1), 571–577 (2020).
    
    [Article](https://doi.org/10.3906%2Fsag-2004-146)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=COVID-19%3A%20Prevention%20and%20control%20measures%20in%20community&journal=Turk.%20J.%20Med.%20Sci.&volume=50&issue=SI-1&pages=571-577&publication_year=2020&author=G%C3%BCner%2CR&author=Hasano%C4%9Flu%2CI&author=Akta%C5%9F%2CF) 
    
9.  9.
    
    Ebrahim, S. H., Ahmed, Q. A., Gozzer, E., Schlagenhauf, P. & Memish, Z. A. Covid-19 and community mitigation strategies in a pandemic. _BMJ_ **368**, m1066 (2020).
    
    [Article](https://doi.org/10.1136%2Fbmj.m1066)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Covid-19%20and%20community%20mitigation%20strategies%20in%20a%20pandemic&journal=BMJ&volume=368&publication_year=2020&author=Ebrahim%2CSH&author=Ahmed%2CQA&author=Gozzer%2CE&author=Schlagenhauf%2CP&author=Memish%2CZA) 
    
10.  10.
    
    Zhou, T., Nguyen, T. T., Zhong, J. & Liu, J. A COVID-19 descriptive study of life after lockdown in Wuhan, China. _R. Soc. Open Sci._ **7**(9), 200705. [https://doi.org/10.1098/rsos.200705](https://doi.org/10.1098/rsos.200705) (2020).
    
    [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020RSOS....700705Z)  [Article](https://doi.org/10.1098%2Frsos.200705)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=33047032)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7540789)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20COVID-19%20descriptive%20study%20of%20life%20after%20lockdown%20in%20Wuhan%2C%20China&journal=R.%20Soc.%20Open%20Sci.&doi=10.1098%2Frsos.200705&volume=7&issue=9&publication_year=2020&author=Zhou%2CT&author=Nguyen%2CTT&author=Zhong%2CJ&author=Liu%2CJ) 
    
11.  11.
    
    Buchholz, K. Strict or Lenient? COVID-19 Lockdowns Compared. _Statistica_. June 18. [https://www.statista.com/chart/22048/university-of-oxford-coronavirus-containment-and-health-index-selected-countries/](https://www.statista.com/chart/22048/university-of-oxford-coronavirus-containment-and-health-index-selected-countries/) (2020).
    
12.  12.
    
    Lee, L., Gan, N. & Culver, E. (2020). Lockdowns are being imposed around the world. China's example highlights the costs. _CNN_. March 17. [https://www.cnn.com/2020/03/16/asia/coronavirus-xi-wuhan-anger-intl-hnk/index.html](https://www.cnn.com/2020/03/16/asia/coronavirus-xi-wuhan-anger-intl-hnk/index.html).
    
13.  13.
    
    Hürriyet Daily News. Turkey to impose four-day lockdown. April 20. [https://www.hurriyetdailynews.com/turkey-to-impose-four-day-lockdown-154053](https://www.hurriyetdailynews.com/turkey-to-impose-four-day-lockdown-154053) (2020).
    
14.  14.
    
    Reuters. Qatar to lift lockdown in four phases from June 15. _Reuters_. June 8. [https://www.reuters.com/article/us-health-coronavirus-qatar-idUSKBN23F2KD](https://www.reuters.com/article/us-health-coronavirus-qatar-idUSKBN23F2KD) (2020).
    
15.  15.
    
    Sandhu, K. K. Coronavirus: Lockdown extended for 2 weeks, business activities to resume based on zones. _India Times_. May 1. [https://www.indiatoday.in/india/story/covid-19-mha-extends-nationwide-lockdown-by-another-14-days-1673394-2020-05-01](https://www.indiatoday.in/india/story/covid-19-mha-extends-nationwide-lockdown-by-another-14-days-1673394-2020-05-01) (2020).
    
16.  16.
    
    Bartkowiak, Jr, D. Michigan governor issues ‘stay-at-home’ order as COVID-19 cases increase. March 23. [https://www.clickondetroit.com/news/local/2020/03/23/watch-live-michigan-gov-whitmer-to-provide-update-on-states-covid-19-response-efforts/](https://www.clickondetroit.com/news/local/2020/03/23/watch-live-michigan-gov-whitmer-to-provide-update-on-states-covid-19-response-efforts/) (2020).
    
17.  17.
    
    Calfas, J., Stancati, M. & Yap, C.-W. California Orders Lockdown for State's 40 Million Residents. _Wall Street J._ March 19. [https://www.wsj.com/articles/china-reports-no-new-domestic-coronavirus-infections-for-the-first-time-since-outbreak-started-11584611233](https://www.wsj.com/articles/china-reports-no-new-domestic-coronavirus-infections-for-the-first-time-since-outbreak-started-11584611233) (2020).
    
18.  18.
    
    Yamamoto, T., Uchiumi, C., Suzuki, N., Yoshimoto, J., & Murillo-Rodriguez, E. (2020). The psychological impact of ‘mild lockdown’ in Japan during the COVID-19 pandemic: a nationwide survey under a declared state of emergency. Preprint at [https://doi.org/10.1101/2020.07.17.20156125](https://doi.org/10.1101/2020.07.17.20156125) (2020).
    
19.  19.
    
    Lee, S. M. & Lee, D. Lessons learned from battling COVID-19: The Korean experience. _Int. J. Environ. Res. Public Health_ **17**(20), 7548. [https://doi.org/10.3390/ijerph17207548](https://doi.org/10.3390/ijerph17207548) (2020).
    
    [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXisVKls7zL)  [Article](https://doi.org/10.3390%2Fijerph17207548)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7590030)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Lessons%20learned%20from%20battling%20COVID-19%3A%20The%20Korean%20experience&journal=Int.%20J.%20Environ.%20Res.%20Public%20Health&doi=10.3390%2Fijerph17207548&volume=17&issue=20&publication_year=2020&author=Lee%2CSM&author=Lee%2CD) 
    
20.  20.
    
    Kirby, J. What we can learn from the “second wave” of coronavirus cases in Asia. _Vox.com_. April 17. [https://www.vox.com/2020/4/17/21213787/coronavirus-asia-waves-hong-kong-singapore-taiwan](https://www.vox.com/2020/4/17/21213787/coronavirus-asia-waves-hong-kong-singapore-taiwan) (2020).
    
21.  21.
    
    Hou, C. _et al._ The effectiveness of quarantine of Wuhan city against the Corona Virus Disease 2019 (COVID-19): A well-mixed SEIR model analysis. _J. Med. Virol._ **92**(7), 841–848. [https://doi.org/10.1002/jmv.25827](https://doi.org/10.1002/jmv.25827) (2020).
    
    [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXnslOntr0%253D)  [Article](https://doi.org/10.1002%2Fjmv.25827)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32243599)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20effectiveness%20of%20quarantine%20of%20Wuhan%20city%20against%20the%20Corona%20Virus%20Disease%202019%20%28COVID-19%29%3A%20A%20well-mixed%20SEIR%20model%20analysis&journal=J.%20Med.%20Virol.&doi=10.1002%2Fjmv.25827&volume=92&issue=7&pages=841-848&publication_year=2020&author=Hou%2CC&author=Chen%2CJ&author=Zhou%2CY&author=Hua%2CL&author=Yuan%2CJ&author=He%2CS&author=Guo%2CY&author=Zhang%2CS&author=Jia%2CQ&author=Zhao%2CC&author=Zhang%2CJ&author=Xu%2CG&author=Jia%2CE) 
    
22.  22.
    
    Bei, T. The real reason China is pushing for a better global response to the Covid-19 pandemic. _The South China Morning Post_. November 14. [https://www.scmp.com/comment/opinion/article/3109634/real-reason-china-pushing-better-global-response-covid-19-pandemic](https://www.scmp.com/comment/opinion/article/3109634/real-reason-china-pushing-better-global-response-covid-19-pandemic) (2020).
    
23.  23.
    
    Bonacini, L., Gallo, G., & Patriarca, F. Identifying policy challenges of COVID-19 in hardly reliable data and judging the success of lockdown measures. _J. Popul. Econ._ 1–27. Advance online publication (2020). [https://doi.org/10.1007/s00148-020-00799-x](https://doi.org/10.1007/s00148-020-00799-x).
    
24.  24.
    
    Wilder-Smith, A. & Freedman, D. O. Isolation, quarantine, social distancing and community containment: Pivotal role for old-style public health measures in the novel coronavirus (2019-nCoV) outbreak. _J. Travel Med._ **27**(2), taaa020 (2020).
    
    [Article](https://doi.org/10.1093%2Fjtm%2Ftaaa020)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Isolation%2C%20quarantine%2C%20social%20distancing%20and%20community%20containment%3A%20Pivotal%20role%20for%20old-style%20public%20health%20measures%20in%20the%20novel%20coronavirus%20%282019-nCoV%29%20outbreak&journal=J.%20Travel%20Med.&volume=27&issue=2&publication_year=2020&author=Wilder-Smith%2CA&author=Freedman%2CDO) 
    
25.  25.
    
    Alvarez, F., Argente, D. & Lippi, F. A simple planning problem for COVID-19 lockdown, testing, and tracing. _Am. Econ. Rev._ [https://doi.org/10.3386/w26981](https://doi.org/10.3386/w26981) (2020).
    
    [Article](https://doi.org/10.3386%2Fw26981)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20simple%20planning%20problem%20for%20COVID-19%20lockdown%2C%20testing%2C%20and%20tracing&journal=Am.%20Econ.%20Rev.&doi=10.3386%2Fw26981&publication_year=2020&author=Alvarez%2CF&author=Argente%2CD&author=Lippi%2CF) 
    
26.  26.
    
    Garibaldi, P., Moen, E., & Pissarides, C. Covid Economics Vetted and Real-Time Papers. CEPR; 2020. June 3. Modelling contacts and transitions in the SIR epidemics model. [https://web.unicz.it/admin/uploads/2020/06/covideconomics25.pdf](https://web.unicz.it/admin/uploads/2020/06/covideconomics25.pdf) (2020).
    
27.  27.
    
    Singh, S. _et al._ Impact of COVID-19 and lockdown on mental health of children and adolescents: A narrative review with recommendations. _Psychiatry Res._ **293**, 113429. [https://doi.org/10.1016/j.psychres.2020.113429](https://doi.org/10.1016/j.psychres.2020.113429) (2020).
    
    [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXhslOgu7rN)  [Article](https://doi.org/10.1016%2Fj.psychres.2020.113429)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32882598)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7444649)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Impact%20of%20COVID-19%20and%20lockdown%20on%20mental%20health%20of%20children%20and%20adolescents%3A%20A%20narrative%20review%20with%20recommendations&journal=Psychiatry%20Res.&doi=10.1016%2Fj.psychres.2020.113429&volume=293&publication_year=2020&author=Singh%2CS&author=Roy%2CD&author=Sinha%2CK&author=Parveen%2CS&author=Sharma%2CG&author=Joshi%2CG) 
    
28.  28.
    
    Nakada, L. & Urban, R. C. COVID-19 pandemic: Impacts on the air quality during the partial lockdown in São Paulo state, Brazil. _Sci. Total Environ._ **730**, 139087. [https://doi.org/10.1016/j.scitotenv.2020.139087](https://doi.org/10.1016/j.scitotenv.2020.139087) (2020).
    
    [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020ScTEn.730m9087N)  [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXosleitbk%253D)  [Article](https://doi.org/10.1016%2Fj.scitotenv.2020.139087)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32380370)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7189200)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=COVID-19%20pandemic%3A%20Impacts%20on%20the%20air%20quality%20during%20the%20partial%20lockdown%20in%20S%C3%A3o%20Paulo%20state%2C%20Brazil&journal=Sci.%20Total%20Environ.&doi=10.1016%2Fj.scitotenv.2020.139087&volume=730&publication_year=2020&author=Nakada%2CL&author=Urban%2CRC) 
    
29.  29.
    
    Allen, L. J. & van den Driessche, P. Relations between deterministic and stochastic thresholds for disease extinction in continuous- and discrete-time infectious disease models. _Math. Biosci._ **243**(1), 99–108 (2013).
    
    [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3068692)  [CAS](https://www.nature.com/articles/cas-redirect/1%3ASTN%3A280%3ADC%252BC3svjtVOntw%253D%253D)  [Article](https://doi.org/10.1016%2Fj.mbs.2013.02.006)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Relations%20between%20deterministic%20and%20stochastic%20thresholds%20for%20disease%20extinction%20in%20continuous-%20and%20discrete-time%20infectious%20disease%20models&journal=Math.%20Biosci.&volume=243&issue=1&pages=99-108&publication_year=2013&author=Allen%2CLJ&author=Driessche%2CP) 
    
30.  30.
    
    Prem, K., Cook, A. R. & Jit, M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. _PLoS Comput. Biol._ **13**(9), e1005697 (2017).
    
    [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2017PLSCB..13E5697P)  [Article](https://doi.org/10.1371%2Fjournal.pcbi.1005697)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Projecting%20social%20contact%20matrices%20in%20152%20countries%20using%20contact%20surveys%20and%20demographic%20data&journal=PLoS%20Comput.%20Biol.&volume=13&issue=9&publication_year=2017&author=Prem%2CK&author=Cook%2CAR&author=Jit%2CM) 
    
31.  31.
    
    Mossong, J. _et al._ Social contacts and mixing patterns relevant to the spread of infectious diseases. _PLoS Med._ **5**(3), e74 (2008).
    
    [Article](https://doi.org/10.1371%2Fjournal.pmed.0050074)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Social%20contacts%20and%20mixing%20patterns%20relevant%20to%20the%20spread%20of%20infectious%20diseases&journal=PLoS%20Med.&volume=5&issue=3&publication_year=2008&author=Mossong%2CJ) 
    
32.  32.
    
    Pellis, L. _et al._ Systematic selection between age and household structure for models aimed at emerging epidemic predictions. _Nat. Commun._ [https://doi.org/10.1038/s41467-019-14229-4](https://doi.org/10.1038/s41467-019-14229-4) (2020).
    
    [Article](https://doi.org/10.1038%2Fs41467-019-14229-4)  [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32060265)  [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7021781)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Systematic%20selection%20between%20age%20and%20household%20structure%20for%20models%20aimed%20at%20emerging%20epidemic%20predictions&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-019-14229-4&publication_year=2020&author=Pellis%2CL&author=Cauchemez%2CS&author=Ferguson%2CNM) 
    
33.  33.
    
    United Nations. 2019. Data Query. Department of Economic and Social Affairs Population Dynamics. [https://population.un.org/wpp/DataQuery/](https://population.un.org/wpp/DataQuery/) (2020).
    
34.  34.
    
    Yang, C. & Gillespie, D. T. Efficient step size selection for the tau-leaping simulation method. _J. Chem. Phys._ **124**, 044109 (2006).
    
    [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2006JChPh.124d4109C)  [Article](https://doi.org/10.1063%2F1.2159468)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Efficient%20step%20size%20selection%20for%20the%20tau-leaping%20simulation%20method&journal=J.%20Chem.%20Phys.&volume=124&publication_year=2006&author=Yang%2CC&author=Gillespie%2CDT) 
    
35.  35.
    
    Allen, L. J. S. & Lahodny, G. E. Jr. Extinction thresholds in deterministic and stochastic epidemic models. _J. Biol. Dyn._ **6**(2), 590–611 (2012).
    
    [Article](https://doi.org/10.1080%2F17513758.2012.665502)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Extinction%20thresholds%20in%20deterministic%20and%20stochastic%20epidemic%20models&journal=J.%20Biol.%20Dyn.&volume=6&issue=2&pages=590-611&publication_year=2012&author=Allen%2CLJS&author=Lahodny%2CGE) 
    
36.  36.
    
    Tang, B. _et al._ Estimation of the transmission risk of the 2019-nCoV and its implication for public health interventions. _J. Clin. Med._ **9**(2), 462 (2020).
    
    [Article](https://doi.org/10.3390%2Fjcm9020462)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Estimation%20of%20the%20transmission%20risk%20of%20the%202019-nCoV%20and%20its%20implication%20for%20public%20health%20interventions&journal=J.%20Clin.%20Med.&volume=9&issue=2&publication_year=2020&author=Tang%2CB) 
    
37.  37.
    
    Munasinghe, M. Is environmental degradation an inevitable consequence of economic growth: Tunneling through the environmental Kuznets curve. _Ecol. Econ._ **29**(1), 89–109 (1999).
    
    [Article](https://doi.org/10.1016%2FS0921-8009%2898%2900062-7)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Is%20environmental%20degradation%20an%20inevitable%20consequence%20of%20economic%20growth%3A%20Tunneling%20through%20the%20environmental%20Kuznets%20curve&journal=Ecol.%20Econ.&volume=29&issue=1&pages=89-109&publication_year=1999&author=Munasinghe%2CM) 
    
38.  38.
    
    Greenwood, P. E. & Gordillo, L. F. Stochastic epidemic modeling. In _Mathematical and Statistical Estimation_. 366, Approaches in Epidemiology. 31–52. (Springer, Berlin, 2009).
    
39.  39.
    
    Carcione, J. M., Santos, J. E., Bagaini, C. & Ba, J. A simulation of a COVID-19 epidemic based on a deterministic SEIR model. _Front. Public Health._ **8**, 230 (2020).
    
    [Article](https://doi.org/10.3389%2Ffpubh.2020.00230)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20simulation%20of%20a%20COVID-19%20epidemic%20based%20on%20a%20deterministic%20SEIR%20model&journal=Front.%20Public%20Health.&volume=8&publication_year=2020&author=Carcione%2CJM&author=Santos%2CJE&author=Bagaini%2CC&author=Ba%2CJ) 
    
40.  40.
    
    Reno, C. _et al._ Forecasting COVID-19-associated hospitalizations under different levels of social distancing in Lombardy and Emilia-Romagna, Northern Italy: Results from an extended SEIR compartmental model. _J. Clin. Med._ **9**(5), 1492 (2020).
    
    [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXhtFWku7zP)  [Article](https://doi.org/10.3390%2Fjcm9051492)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Forecasting%20COVID-19-associated%20hospitalizations%20under%20different%20levels%20of%20social%20distancing%20in%20Lombardy%20and%20Emilia-Romagna%2C%20Northern%20Italy%3A%20Results%20from%20an%20extended%20SEIR%20compartmental%20model&journal=J.%20Clin.%20Med.&volume=9&issue=5&publication_year=2020&author=Reno%2CC) 
    
41.  41.
    
    Bausch, D. G. Precision physical distancing for COVID-19: An important tool in unlocking the lockdown. _Am. J. Trop Med Hyg._ **103**(1), 22–24 (2020).
    
    [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4051989)  [Article](https://doi.org/10.4269%2Fajtmh.20-0359)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Precision%20physical%20distancing%20for%20COVID-19%3A%20An%20important%20tool%20in%20unlocking%20the%20lockdown&journal=Am.%20J.%20Trop%20Med%20Hyg.&volume=103&issue=1&pages=22-24&publication_year=2020&author=Bausch%2CDG) 
    
42.  42.
    
    World Health Organization. Statement on the fourth meeting of the International Health Regulations (2005) Emergency Committee regarding the outbreak of coronavirus disease (COVID-19). [https://www.who.int/news-room/detail/01-08-2020-statement-on-the-fourth-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-outbreak-of-coronavirus-disease-(covid-19)](https://www.who.int/news-room/detail/01-08-2020-statement-on-the-fourth-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-outbreak-of-coronavirus-disease-(covid-19)).
    
43.  43.
    
    Harris, J.E. Overcoming reporting delays is critical to timely epidemic monitoring: The case of COVID-19 in New York City. _medRxiv_ 2020.08.02.20159418 (2020).
    
44.  44.
    
    Ngonghala, C. N. _et al._ Mathematical assessment of the impact of non-pharmaceutical interventions on curtailing the 2019 novel Coronavirus. _Math. Biosci._ **325**, 108364 (2020).
    
    [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4097986)  [CAS](https://www.nature.com/articles/cas-redirect/1%3ACAS%3A528%3ADC%252BB3cXovFKhs7Y%253D)  [Article](https://doi.org/10.1016%2Fj.mbs.2020.108364)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mathematical%20assessment%20of%20the%20impact%20of%20non-pharmaceutical%20interventions%20on%20curtailing%20the%202019%20novel%20Coronavirus&journal=Math.%20Biosci.&volume=325&publication_year=2020&author=Ngonghala%2CCN) 
    
45.  45.
    
    Imai, N. _et al._ Adoption and impact of non-pharmaceutical interventions for COVID-19. _Wellcome Open Res._ **5**, 59 (2020).
    
    [Article](https://doi.org/10.12688%2Fwellcomeopenres.15808.1)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Adoption%20and%20impact%20of%20non-pharmaceutical%20interventions%20for%20COVID-19&journal=Wellcome%20Open%20Res.&volume=5&publication_year=2020&author=Imai%2CN) 
    
46.  46.
    
    Lau, H. _et al._ The positive impact of lockdown in Wuhan on containing the COVID-19 outbreak in China. _J Travel Med._ **27**(3), taaa037 (2020).
    
    [Article](https://doi.org/10.1093%2Fjtm%2Ftaaa037)  [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20positive%20impact%20of%20lockdown%20in%20Wuhan%20on%20containing%20the%20COVID-19%20outbreak%20in%20China&journal=J%20Travel%20Med.&volume=27&issue=3&publication_year=2020&author=Lau%2CH) 
    
47.  47.
    
    Ji, T. _et al_. Lockdown contained the spread of 2019 novel coronavirus disease in Huangshi city, China: Early epidemiological findings. _Clin. Infect. Dis_. ciaa390 (2020).
    
48.  48.
    
    Bundgaard, H. _et al._ Effectiveness of adding a mask recommendation to other public health measures to prevent SARS-CoV-2 infection in Danish mask wearers: A randomized controlled trial. _Ann. Intern. Med._ M20-6817 (2020).
    

[Download references](https://citation-needed.springer.com/v2/references/10.1038/s41598-021-82873-2?format=refman&flavour=references)

## Acknowledgements

M.A. gratefully acknowledge the assistance and support of Kuwait University and the Kuwait Foundation for the Advancement of Sciences (KFAS) grant number “CORONA PROP 46” to complete this research.

## Funding

M.A. received Grant number “CORONA PROP 46” from the Kuwait Foundation for the Advancement of Sciences (KFAS).

## Author information

### Affiliations

1.  School of Mathematical and Statistical Sciences, The University of Texas Rio Grande Valley, Edinburg, TX, 78539, USA
    
    Tamer Oraby & Kristina Vatcheva
    
2.  McLaughlin Centre for Population Health Risk Assessment, Faculty of Medicine, University of Ottawa, Ottawa, ON, K1N 6N5, Canada
    
    Michael G. Tyshenko
    
3.  School of Medicine, The University of Texas Rio Grande Valley, Edinburg, TX, 78539, USA
    
    Jose Campo Maldonado
    
4.  Department of Pathology and Laboratory Medicine, Faculty of Medicine, University of Ottawa, Ottawa, ON, K1H 8M5, Canada
    
    Susie Elsaadany
    
5.  Department of Epidemiology and Biostatistics, Faculty of Public Health, Kuwait University, 13110, Safat, Kuwait
    
    Walid Q. Alali
    
6.  Department of Public Health Practice, Faculty of Public Health, Kuwait University, 13110, Safat, Kuwait
    
    Joseph C. Longenecker
    
7.  Department of Environmental and Occupational Health, Faculty of Public Health, Kuwait University, 13110, Safat, Kuwait
    
    Mustafa Al-Zoughool
    

### Contributions

T.O., M.G.T., S.E. and M.A. conceived conception and designed the model. T.O. worked on the mathematical model establishment, simulation, coding and analytical work. T.O., W.A., M.G.T., and M.A. contributed to the acquisition of data. T.O., M.G.T., M.A., K.V., J.C.L., W.Q.A. and M.A. contributed to analysis and interpretation of outputs. T.O., M.G.T., J.C.M., K.V., S.E., W.Q.A., J.C.L. and M.A. worked on reviewing different drafts of the manuscript. T.O., M.G.T., J.C.M., K.V., S.E., W.Q.A., J.C.L. and M.A. contributed to the final revision. All authors reviewed the final manuscript.

### Corresponding author

Correspondence to [Tamer Oraby](https://www.nature.com/articles/s41598-021-82873-2/email/correspondent/c1/new).

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Additional information

### Publisher's note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Supplementary Information

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).

[Reprints and Permissions](https://s100.copyright.com/AppDispatchServlet?title=Modeling%20the%20effect%20of%20lockdown%20timing%20as%20a%20COVID-19%20control%20measure%20in%20countries%20with%20differing%20social%20contacts&author=Tamer%20Oraby%20et%20al&contentID=10.1038%2Fs41598-021-82873-2&copyright=The%20Author%28s%29&publication=2045-2322&publicationDate=2021-02-08&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY)

## About this article

[![Verify currency and authenticity via CrossMark](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjgxIiB3aWR0aD0iNTciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJtMTcuMzUgMzUuNDUgMjEuMy0xNC4ydi0xNy4wM2gtMjEuMyIgZmlsbD0iIzk4OTg5OCIvPjxwYXRoIGQ9Im0zOC42NSAzNS40NS0yMS4zLTE0LjJ2LTE3LjAzaDIxLjMiIGZpbGw9IiM3NDc0NzQiLz48cGF0aCBkPSJtMjggLjVjLTEyLjk4IDAtMjMuNSAxMC41Mi0yMy41IDIzLjVzMTAuNTIgMjMuNSAyMy41IDIzLjUgMjMuNS0xMC41MiAyMy41LTIzLjVjMC02LjIzLTIuNDgtMTIuMjEtNi44OC0xNi42Mi00LjQxLTQuNC0xMC4zOS02Ljg4LTE2LjYyLTYuODh6bTAgNDEuMjVjLTkuOCAwLTE3Ljc1LTcuOTUtMTcuNzUtMTcuNzVzNy45NS0xNy43NSAxNy43NS0xNy43NSAxNy43NSA3Ljk1IDE3Ljc1IDE3Ljc1YzAgNC43MS0xLjg3IDkuMjItNS4yIDEyLjU1cy03Ljg0IDUuMi0xMi41NSA1LjJ6IiBmaWxsPSIjNTM1MzUzIi8+PHBhdGggZD0ibTQxIDM2Yy01LjgxIDYuMjMtMTUuMjMgNy40NS0yMi40MyAyLjktNy4yMS00LjU1LTEwLjE2LTEzLjU3LTcuMDMtMjEuNWwtNC45Mi0zLjExYy00Ljk1IDEwLjctMS4xOSAyMy40MiA4Ljc4IDI5LjcxIDkuOTcgNi4zIDIzLjA3IDQuMjIgMzAuNi00Ljg2eiIgZmlsbD0iIzljOWM5YyIvPjxwYXRoIGQ9Im0uMiA1OC40NWMwLS43NS4xMS0xLjQyLjMzLTIuMDFzLjUyLTEuMDkuOTEtMS41Yy4zOC0uNDEuODMtLjczIDEuMzQtLjk0LjUxLS4yMiAxLjA2LS4zMiAxLjY1LS4zMi41NiAwIDEuMDYuMTEgMS41MS4zNS40NC4yMy44MS41IDEuMS44MWwtLjkxIDEuMDFjLS4yNC0uMjQtLjQ5LS40Mi0uNzUtLjU2LS4yNy0uMTMtLjU4LS4yLS45My0uMi0uMzkgMC0uNzMuMDgtMS4wNS4yMy0uMzEuMTYtLjU4LjM3LS44MS42Ni0uMjMuMjgtLjQxLjYzLS41MyAxLjA0LS4xMy40MS0uMTkuODgtLjE5IDEuMzkgMCAxLjA0LjIzIDEuODYuNjggMi40Ni40NS41OSAxLjA2Ljg4IDEuODQuODguNDEgMCAuNzctLjA3IDEuMDctLjIzcy41OS0uMzkuODUtLjY4bC45MSAxYy0uMzguNDMtLjguNzYtMS4yOC45OS0uNDcuMjItMSAuMzQtMS41OC4zNC0uNTkgMC0xLjEzLS4xLTEuNjQtLjMxLS41LS4yLS45NC0uNTEtMS4zMS0uOTEtLjM4LS40LS42Ny0uOS0uODgtMS40OC0uMjItLjU5LS4zMy0xLjI2LS4zMy0yLjAyem04LjQtNS4zM2gxLjYxdjIuNTRsLS4wNSAxLjMzYy4yOS0uMjcuNjEtLjUxLjk2LS43MnMuNzYtLjMxIDEuMjQtLjMxYy43MyAwIDEuMjcuMjMgMS42MS43MS4zMy40Ny41IDEuMTQuNSAyLjAydjQuMzFoLTEuNjF2LTQuMWMwLS41Ny0uMDgtLjk3LS4yNS0xLjIxLS4xNy0uMjMtLjQ1LS4zNS0uODMtLjM1LS4zIDAtLjU2LjA4LS43OS4yMi0uMjMuMTUtLjQ5LjM2LS43OC42NHY0LjhoLTEuNjF6bTcuMzcgNi40NWMwLS41Ni4wOS0xLjA2LjI2LTEuNTEuMTgtLjQ1LjQyLS44My43MS0xLjE0LjI5LS4zLjYzLS41NCAxLjAxLS43MS4zOS0uMTcuNzgtLjI1IDEuMTgtLjI1LjQ3IDAgLjg4LjA4IDEuMjMuMjQuMzYuMTYuNjUuMzguODkuNjdzLjQyLjYzLjU0IDEuMDNjLjEyLjQxLjE4Ljg0LjE4IDEuMzIgMCAuMzItLjAyLjU3LS4wNy43NmgtNC4zNmMuMDcuNjIuMjkgMS4xLjY1IDEuNDQuMzYuMzMuODIuNSAxLjM4LjUuMjkgMCAuNTctLjA0LjgzLS4xM3MuNTEtLjIxLjc2LS4zN2wuNTUgMS4wMWMtLjMzLjIxLS42OS4zOS0xLjA5LjUzLS40MS4xNC0uODMuMjEtMS4yNi4yMS0uNDggMC0uOTItLjA4LTEuMzQtLjI1LS40MS0uMTYtLjc2LS40LTEuMDctLjctLjMxLS4zMS0uNTUtLjY5LS43Mi0xLjEzLS4xOC0uNDQtLjI2LS45NS0uMjYtMS41MnptNC42LS42MmMwLS41NS0uMTEtLjk4LS4zNC0xLjI4LS4yMy0uMzEtLjU4LS40Ny0xLjA2LS40Ny0uNDEgMC0uNzcuMTUtMS4wNy40NS0uMzEuMjktLjUuNzMtLjU4IDEuM3ptMi41LjYyYzAtLjU3LjA5LTEuMDguMjgtMS41My4xOC0uNDQuNDMtLjgyLjc1LTEuMTNzLjY5LS41NCAxLjEtLjcxYy40Mi0uMTYuODUtLjI0IDEuMzEtLjI0LjQ1IDAgLjg0LjA4IDEuMTcuMjNzLjYxLjM0Ljg1LjU3bC0uNzcgMS4wMmMtLjE5LS4xNi0uMzgtLjI4LS41Ni0uMzctLjE5LS4wOS0uMzktLjE0LS42MS0uMTQtLjU2IDAtMS4wMS4yMS0xLjM1LjYzLS4zNS40MS0uNTIuOTctLjUyIDEuNjcgMCAuNjkuMTcgMS4yNC41MSAxLjY2LjM0LjQxLjc4LjYyIDEuMzIuNjIuMjggMCAuNTQtLjA2Ljc4LS4xNy4yNC0uMTIuNDUtLjI2LjY0LS40MmwuNjcgMS4wM2MtLjMzLjI5LS42OS41MS0xLjA4LjY1LS4zOS4xNS0uNzguMjMtMS4xOC4yMy0uNDYgMC0uOS0uMDgtMS4zMS0uMjQtLjQtLjE2LS43NS0uMzktMS4wNS0uN3MtLjUzLS42OS0uNy0xLjEzYy0uMTctLjQ1LS4yNS0uOTYtLjI1LTEuNTN6bTYuOTEtNi40NWgxLjU4djYuMTdoLjA1bDIuNTQtMy4xNmgxLjc3bC0yLjM1IDIuOCAyLjU5IDQuMDdoLTEuNzVsLTEuNzctMi45OC0xLjA4IDEuMjN2MS43NWgtMS41OHptMTMuNjkgMS4yN2MtLjI1LS4xMS0uNS0uMTctLjc1LS4xNy0uNTggMC0uODcuMzktLjg3IDEuMTZ2Ljc1aDEuMzR2MS4yN2gtMS4zNHY1LjZoLTEuNjF2LTUuNmgtLjkydi0xLjJsLjkyLS4wN3YtLjcyYzAtLjM1LjA0LS42OC4xMy0uOTguMDgtLjMxLjIxLS41Ny40LS43OXMuNDItLjM5LjcxLS41MWMuMjgtLjEyLjYzLS4xOCAxLjA0LS4xOC4yNCAwIC40OC4wMi42OS4wNy4yMi4wNS40MS4xLjU3LjE3em0uNDggNS4xOGMwLS41Ny4wOS0xLjA4LjI3LTEuNTMuMTctLjQ0LjQxLS44Mi43Mi0xLjEzLjMtLjMxLjY1LS41NCAxLjA0LS43MS4zOS0uMTYuOC0uMjQgMS4yMy0uMjRzLjg0LjA4IDEuMjQuMjRjLjQuMTcuNzQuNCAxLjA0Ljcxcy41NC42OS43MiAxLjEzYy4xOS40NS4yOC45Ni4yOCAxLjUzcy0uMDkgMS4wOC0uMjggMS41M2MtLjE4LjQ0LS40Mi44Mi0uNzIgMS4xM3MtLjY0LjU0LTEuMDQuNy0uODEuMjQtMS4yNC4yNC0uODQtLjA4LTEuMjMtLjI0LS43NC0uMzktMS4wNC0uN2MtLjMxLS4zMS0uNTUtLjY5LS43Mi0xLjEzLS4xOC0uNDUtLjI3LS45Ni0uMjctMS41M3ptMS42NSAwYzAgLjY5LjE0IDEuMjQuNDMgMS42Ni4yOC40MS42OC42MiAxLjE4LjYyLjUxIDAgLjktLjIxIDEuMTktLjYyLjI5LS40Mi40NC0uOTcuNDQtMS42NiAwLS43LS4xNS0xLjI2LS40NC0xLjY3LS4yOS0uNDItLjY4LS42My0xLjE5LS42My0uNSAwLS45LjIxLTEuMTguNjMtLjI5LjQxLS40My45Ny0uNDMgMS42N3ptNi40OC0zLjQ0aDEuMzNsLjEyIDEuMjFoLjA1Yy4yNC0uNDQuNTQtLjc5Ljg4LTEuMDIuMzUtLjI0LjctLjM2IDEuMDctLjM2LjMyIDAgLjU5LjA1Ljc4LjE0bC0uMjggMS40LS4zMy0uMDljLS4xMS0uMDEtLjIzLS4wMi0uMzgtLjAyLS4yNyAwLS41Ni4xLS44Ni4zMXMtLjU1LjU4LS43NyAxLjF2NC4yaC0xLjYxem0tNDcuODcgMTVoMS42MXY0LjFjMCAuNTcuMDguOTcuMjUgMS4yLjE3LjI0LjQ0LjM1LjgxLjM1LjMgMCAuNTctLjA3LjgtLjIyLjIyLS4xNS40Ny0uMzkuNzMtLjczdi00LjdoMS42MXY2Ljg3aC0xLjMybC0uMTItMS4wMWgtLjA0Yy0uMy4zNi0uNjMuNjQtLjk4Ljg2LS4zNS4yMS0uNzYuMzItMS4yNC4zMi0uNzMgMC0xLjI3LS4yNC0xLjYxLS43MS0uMzMtLjQ3LS41LTEuMTQtLjUtMi4wMnptOS40NiA3LjQzdjIuMTZoLTEuNjF2LTkuNTloMS4zM2wuMTIuNzJoLjA1Yy4yOS0uMjQuNjEtLjQ1Ljk3LS42My4zNS0uMTcuNzItLjI2IDEuMS0uMjYuNDMgMCAuODEuMDggMS4xNS4yNC4zMy4xNy42MS40Ljg0LjcxLjI0LjMxLjQxLjY4LjUzIDEuMTEuMTMuNDIuMTkuOTEuMTkgMS40NCAwIC41OS0uMDkgMS4xMS0uMjUgMS41Ny0uMTYuNDctLjM4Ljg1LS42NSAxLjE2LS4yNy4zMi0uNTguNTYtLjk0LjczLS4zNS4xNi0uNzIuMjUtMS4xLjI1LS4zIDAtLjYtLjA3LS45LS4ycy0uNTktLjMxLS44Ny0uNTZ6bTAtMi4zYy4yNi4yMi41LjM3LjczLjQ1LjI0LjA5LjQ2LjEzLjY2LjEzLjQ2IDAgLjg0LS4yIDEuMTUtLjYuMzEtLjM5LjQ2LS45OC40Ni0xLjc3IDAtLjY5LS4xMi0xLjIyLS4zNS0xLjYxLS4yMy0uMzgtLjYxLS41Ny0xLjEzLS41Ny0uNDkgMC0uOTkuMjYtMS41Mi43N3ptNS44Ny0xLjY5YzAtLjU2LjA4LTEuMDYuMjUtMS41MS4xNi0uNDUuMzctLjgzLjY1LTEuMTQuMjctLjMuNTgtLjU0LjkzLS43MXMuNzEtLjI1IDEuMDgtLjI1Yy4zOSAwIC43My4wNyAxIC4yLjI3LjE0LjU0LjMyLjgxLjU1bC0uMDYtMS4xdi0yLjQ5aDEuNjF2OS44OGgtMS4zM2wtLjExLS43NGgtLjA2Yy0uMjUuMjUtLjU0LjQ2LS44OC42NC0uMzMuMTgtLjY5LjI3LTEuMDYuMjctLjg3IDAtMS41Ni0uMzItMi4wNy0uOTVzLS43Ni0xLjUxLS43Ni0yLjY1em0xLjY3LS4wMWMwIC43NC4xMyAxLjMxLjQgMS43LjI2LjM4LjY1LjU4IDEuMTUuNTguNTEgMCAuOTktLjI2IDEuNDQtLjc3di0zLjIxYy0uMjQtLjIxLS40OC0uMzYtLjctLjQ1LS4yMy0uMDgtLjQ2LS4xMi0uNy0uMTItLjQ1IDAtLjgyLjE5LTEuMTMuNTktLjMxLjM5LS40Ni45NS0uNDYgMS42OHptNi4zNSAxLjU5YzAtLjczLjMyLTEuMy45Ny0xLjcxLjY0LS40IDEuNjctLjY4IDMuMDgtLjg0IDAtLjE3LS4wMi0uMzQtLjA3LS41MS0uMDUtLjE2LS4xMi0uMy0uMjItLjQzcy0uMjItLjIyLS4zOC0uM2MtLjE1LS4wNi0uMzQtLjEtLjU4LS4xLS4zNCAwLS42OC4wNy0xIC4ycy0uNjMuMjktLjkzLjQ3bC0uNTktMS4wOGMuMzktLjI0LjgxLS40NSAxLjI4LS42My40Ny0uMTcuOTktLjI2IDEuNTQtLjI2Ljg2IDAgMS41MS4yNSAxLjkzLjc2cy42MyAxLjI1LjYzIDIuMjF2NC4wN2gtMS4zMmwtLjEyLS43NmgtLjA1Yy0uMy4yNy0uNjMuNDgtLjk4LjY2cy0uNzMuMjctMS4xNC4yN2MtLjYxIDAtMS4xLS4xOS0xLjQ4LS41Ni0uMzgtLjM2LS41Ny0uODUtLjU3LTEuNDZ6bTEuNTctLjEyYzAgLjMuMDkuNTMuMjcuNjcuMTkuMTQuNDIuMjEuNzEuMjEuMjggMCAuNTQtLjA3Ljc3LS4ycy40OC0uMzEuNzMtLjU2di0xLjU0Yy0uNDcuMDYtLjg2LjEzLTEuMTguMjMtLjMxLjA5LS41Ny4xOS0uNzYuMzFzLS4zMy4yNS0uNDEuNGMtLjA5LjE1LS4xMy4zMS0uMTMuNDh6bTYuMjktMy42M2gtLjk4di0xLjJsMS4wNi0uMDcuMi0xLjg4aDEuMzR2MS44OGgxLjc1djEuMjdoLTEuNzV2My4yOGMwIC44LjMyIDEuMi45NyAxLjIuMTIgMCAuMjQtLjAxLjM3LS4wNC4xMi0uMDMuMjQtLjA3LjM0LS4xMWwuMjggMS4xOWMtLjE5LjA2LS40LjEyLS42NC4xNy0uMjMuMDUtLjQ5LjA4LS43Ni4wOC0uNCAwLS43NC0uMDYtMS4wMi0uMTgtLjI3LS4xMy0uNDktLjMtLjY3LS41Mi0uMTctLjIxLS4zLS40OC0uMzctLjc4LS4wOC0uMy0uMTItLjY0LS4xMi0xLjAxem00LjM2IDIuMTdjMC0uNTYuMDktMS4wNi4yNy0xLjUxcy40MS0uODMuNzEtMS4xNGMuMjktLjMuNjMtLjU0IDEuMDEtLjcxLjM5LS4xNy43OC0uMjUgMS4xOC0uMjUuNDcgMCAuODguMDggMS4yMy4yNC4zNi4xNi42NS4zOC44OS42N3MuNDIuNjMuNTQgMS4wM2MuMTIuNDEuMTguODQuMTggMS4zMiAwIC4zMi0uMDIuNTctLjA3Ljc2aC00LjM3Yy4wOC42Mi4yOSAxLjEuNjUgMS40NC4zNi4zMy44Mi41IDEuMzguNS4zIDAgLjU4LS4wNC44NC0uMTMuMjUtLjA5LjUxLS4yMS43Ni0uMzdsLjU0IDEuMDFjLS4zMi4yMS0uNjkuMzktMS4wOS41M3MtLjgyLjIxLTEuMjYuMjFjLS40NyAwLS45Mi0uMDgtMS4zMy0uMjUtLjQxLS4xNi0uNzctLjQtMS4wOC0uNy0uMy0uMzEtLjU0LS42OS0uNzItMS4xMy0uMTctLjQ0LS4yNi0uOTUtLjI2LTEuNTJ6bTQuNjEtLjYyYzAtLjU1LS4xMS0uOTgtLjM0LTEuMjgtLjIzLS4zMS0uNTgtLjQ3LTEuMDYtLjQ3LS40MSAwLS43Ny4xNS0xLjA4LjQ1LS4zMS4yOS0uNS43My0uNTcgMS4zem0zLjAxIDIuMjNjLjMxLjI0LjYxLjQzLjkyLjU3LjMuMTMuNjMuMi45OC4yLjM4IDAgLjY1LS4wOC44My0uMjNzLjI3LS4zNS4yNy0uNmMwLS4xNC0uMDUtLjI2LS4xMy0uMzctLjA4LS4xLS4yLS4yLS4zNC0uMjgtLjE0LS4wOS0uMjktLjE2LS40Ny0uMjNsLS41My0uMjJjLS4yMy0uMDktLjQ2LS4xOC0uNjktLjMtLjIzLS4xMS0uNDQtLjI0LS42Mi0uNHMtLjMzLS4zNS0uNDUtLjU1Yy0uMTItLjIxLS4xOC0uNDYtLjE4LS43NSAwLS42MS4yMy0xLjEuNjgtMS40OS40NC0uMzggMS4wNi0uNTcgMS44My0uNTcuNDggMCAuOTEuMDggMS4yOS4yNXMuNzEuMzYuOTkuNTdsLS43NC45OGMtLjI0LS4xNy0uNDktLjMyLS43My0uNDItLjI1LS4xMS0uNTEtLjE2LS43OC0uMTYtLjM1IDAtLjYuMDctLjc2LjIxLS4xNy4xNS0uMjUuMzMtLjI1LjU0IDAgLjE0LjA0LjI2LjEyLjM2cy4xOC4xOC4zMS4yNmMuMTQuMDcuMjkuMTQuNDYuMjFsLjU0LjE5Yy4yMy4wOS40Ny4xOC43LjI5cy40NC4yNC42NC40Yy4xOS4xNi4zNC4zNS40Ni41OC4xMS4yMy4xNy41LjE3LjgyIDAgLjMtLjA2LjU4LS4xNy44My0uMTIuMjYtLjI5LjQ4LS41MS42OC0uMjMuMTktLjUxLjM0LS44NC40NS0uMzQuMTEtLjcyLjE3LTEuMTUuMTctLjQ4IDAtLjk1LS4wOS0xLjQxLS4yNy0uNDYtLjE5LS44Ni0uNDEtMS4yLS42OHoiIGZpbGw9IiM1MzUzNTMiLz48L2c+PC9zdmc+)](https://crossmark.crossref.org/dialog/?doi=10.1038/s41598-021-82873-2)

### Cite this article

Oraby, T., Tyshenko, M.G., Maldonado, J.C. _et al._ Modeling the effect of lockdown timing as a COVID-19 control measure in countries with differing social contacts. _Sci Rep_ **11,** 3354 (2021). https://doi.org/10.1038/s41598-021-82873-2

[Download citation](https://citation-needed.springer.com/v2/references/10.1038/s41598-021-82873-2?format=refman&flavour=citation)

-   Received: 09 August 2020
    
-   Accepted: 21 January 2021
    
-   Published: 08 February 2021
    
-   DOI: [https://doi.org/10.1038/s41598-021-82873-2](https://doi.org/10.1038/s41598-021-82873-2)
    

## Comments

By submitting a comment you agree to abide by our [Terms](https://www.nature.com/info/tandc.html) and [Community Guidelines](https://www.nature.com/info/community-guidelines.html). If you find something abusive or that does not comply with our terms or guidelines please flag it as inappropriate.
