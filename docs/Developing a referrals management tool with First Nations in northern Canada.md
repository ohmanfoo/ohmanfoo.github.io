created: 2021-07-18T01:25:03 (UTC -04:00)
tags: [PDF,Markdown,converter,online]
source: https://pdf2md.morethan.io/
author:
Developing a referrals management tool with  [[First Nations]]  in northern Canada
Excerpt
Converts PDF files to Markdown.
UCL Press
Chapter Title: Developing a referrals management tool with  [[First Nations]]  in northern Canada: an iterative programming approach
Chapter Author(s): Jon Corbett and Aaron Derrickson
Book Title: Geographic Citizen  [[Science]]  Design
Book Subtitle: No one left behind
Book Editor(s): Artemis Skarlatidou, Muki Haklay
Published by: UCL Press. (2021)
Stable URL: https://www.jstor.org/stable/j.ctv15d8174.
JSTOR is a not-for-profit service that helps scholars,  [[research]] ers, and students discover, use, and build upon a wide
range of content in a trusted digital archive. We use information technology and tools to increase productivity and
facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.
Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at
https://about.jstor.org/terms
This book is licensed under a Creative Commons Attribution 4.0 International License (CC
BY 4.0). To view a copy of this license, visit
https://creativecommons.org/licenses/by/4.0/.
UCL Press is collaborating with JSTOR to digitize, preserve and extend access to Geographic
Citizen  [[Science]]  Design
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
209
Jon Corbett and Aaron derrickson
Highlights
There is a need for an open-source digital tool to support  [[Canadian]]
  First Nation communities to communicate more effectively with
  industries in regard to proposed resource extraction projects.
Gather was the result of an iterative, responsive and ‘just-in-time’
  approach to co-design a geographic citizen  [[science]]  data gathering
  and management tool.
The Gather software and the latest version of the tool diverged from
  the programming team’s initial ideas as a result of the co-design
  process.
Implementation challenges tended not to be technical or design
  focused. Rather, they related to the individuals and organisations
  involved in the project, and the sensitivity of the information being
  handled.

Introduction
All proposed resource development projects in Canada, whether a new
mine or a major new piece of infrastructure, are required to consult with
the  [[indigenous]]  parties that will be impacted by the work. This referral
process has emerged as the result of a series of precedent-setting court
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
210 GEOGRAPHIC CITIZEN SCIENCE DESIGN
cases which found that the Provincial and Federal  [[Crown]] ^1 have a legal
duty to consult and, where necessary, accommodate First Nation^2 com-
munities (Harris  [[2006]] ) when development activities are being carried
out within their traditional territories (Ecotrust Canada  [[2017]] ). Regard-
less of scale, the First Nation who has rights on the land where the devel-
opment will take place is given the opportunity to examine the proposed
project for potential adverse environmental, economic, social, heritage
and health impacts that may occur during the project life cycle. The pro-
cess is rigorous and often involves extensive documentation provided by
the proponents, who in turn draw on the expertise of specialist consult-
ants. In  [[British]]  Columbia, once a referral is submitted, the First Nation
must respond with written comments within a 20-day period. If the
review cannot be completed within this time frame, the  [[government]]
notes that the proponent has fulfilled their obligatory duty to consult
with the community.
With the continued and growing presence of large-scale resource
development (particularly  [[mining]]  and forestry operations) in northern
Canada, First Nation communities are becoming overwhelmed by the
obligation to manage, review and respond to these impact assessment
proposals (Power  [[2017]] ). First Nation leaders and community lands
departments recognise a clear need to  [[research]] , design, develop, imple-
ment and evaluate affordable tools that could streamline the duty to
consult between  [[government]] , proponents and communities, as well as
facilitate community decision making related to the referral process. In
 [[2015]] , several First Nation communities and their  [[representative]] s
approached the Spatial Information for Community Engagement (SpICE)
lab at the  [[University]]  of  [[British]]  Columbia seeking the development of a
web-based tool that might be used to improve their capacity to under-
stand the extent of all proposed resource developments, as well as man-
age and respond to the referrals. The project also involved the co-design,
development and implementation of a mobile app to enable community
members to collect spatial information on their contemporary use of lands
and resources. This information in turn can be accessed and viewed using
a map interface by community lands department members and commu-
nity leaders in order to inform lands-related decision-making processes.
This chapter describes the development and initial implementation of
‘Gather: The referral management tool’ that we co-designed to address
these needs.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 211
Supporting  [[First Nations]] ’ land-management needs
2.1 Context
Speaking in general terms,  [[First Nations]]  throughout Canada have a
unique, respectful and stewardship-focused relationship with the lands
on which they live (Berkes, Folke and Colding  [[2000]] ; Turner, Ignace and
Ignace  [[2000]] ). This relationship has developed over millennia. It directly
contributes to the social, cultural, economic, subsistence, health and spir-
itual well-being of First Nation communities throughout the country
(Berkes  [[2017]] ). Traditional knowledge, languages, cultural practices and
oral traditions are all connected to the land (Alfred and Corntassel  [[2005]] ).
 [[Europe]] an colonisation and settlement in Canada have profoundly chal-
lenged this relationship. Over the past 125 years, resource industries have
harvested and sold natural resources from First Nation lands (Angell and
Parkins  [[2011]] ). These businesses have become major drivers for the Cana-
dian economy and employment.
The Royal Proclamation, signed in  [[1763]]  by  [[King]]  George III, has
helped shape the legal relationship between the  [[Crown]]  and  [[First Nations]] .
The Proclamation implicitly recognises  [[First Nations]]  as owners of their
lands, and in doing so, it provides the basis of the legal recognition of
their rights to land (Borrows  [[1994]] ). In  [[1973]] , the Supreme Court of Can-
ada, through the Calder decision, recognised that  [[aboriginal]]  title existed
in law, and therefore could be enforced (Foster, Raven and Webber  [[2011]] ).
That decision was followed in  [[1997]]  with the Delgamuukw and Gisday’way,
as well as Sparrow and Tsilhqot’in, decisions that found that  [[aboriginal]]
title was something substantive and robust and should be considered ‘a
right to the land itself’ (Morse  [[2017]] ). These court cases are significant
because they mean that the provincial and federal  [[government]] s now have
a legal duty to consult and, where necessary, accommodate First Nation
groups when development activities are being carried out within their
traditional territories.
It is important to note that although the duty to consult can be con-
flictual in nature (Zietsma et al.  [[2002]] ; Hayter  [[2003]] ), most levels of gov-
ernment as well as industry leaders have accepted that consultation with
 [[First Nations]]  is a legal, necessary and important aspect of doing business
with  [[First Nations]]  (Joseph  [[2015]] ) on First Nation territory. Furthermore,
many businesses conduct their own engagement process with  [[indigenous]]
communities as a part of their project planning before they apply for
regulatory approvals ( [[Canadian]]  Chamber of Commerce  [[2016]] ). This
often involves establishing relationships with community decision makers
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
212 GEOGRAPHIC CITIZEN SCIENCE DESIGN
and including them in initial project planning processes and developing
impact and benefit agreements (Gogal, Reigert and Jamieson  [[2005]] ;
Caine and Krogman  [[2010]] ). This is done to help avoid the delay or cancel-
lation of projects that might occur if consultation only takes place during
the formal referral process.
The consequence of this legal requirement to consult is that many
small  [[First Nations]] , often operating with limited staff and resources, have
been overwhelmed by the number of referrals that they receive daily. It
has proven to be a major logistical and administrative challenge to organ-
ise, prioritise, analyse and respond to these referrals in a meaningful and
effective way (Ecotrust Canada  [[2017]] ). This is especially the case in smaller,
more geographically remote communities where most resource develop-
ment projects take place in Canada. For example, in  [[2014]] , Saulteau First
Nations (SFN), a community in northern  [[British]]  Columbia, received more
than 3,500 applications referred by federal, provincial and local govern-
ments. The current procedural requirements within the regulatory pro-
cess oblige SFN to assign significant resources to manage, review and
respond to each referral. This process also necessitates understanding the
spatial extent of the proposed development intervention and how it poten-
tially impacts the traditional and contemporary uses of the land. Pres-
ently, the capacity for SFN to acknowledge the infringement of their
 [[indigenous]]  and  [[treaty]]  rights from a proposed development in an effec-
tive and timely way is both limited and costly.
A number of proprietary software tools have been, and continue to
be, developed in response to this challenge. A report written in  [[July]]
by Ecotrust Canada and the  [[Aboriginal]]  Mapping Network identified eight
software applications used in 44 different communities around the prov-
ince of  [[British]]  Columbia. Most of these tools included a mapping compo-
nent to the software, but none directly linked their software platforms to
community-contributed geographic citizen  [[science]]  information. The
report further identified several critical challenges to implementing and
using this software. These were related to access to training, usability,
licensing costs, updates and software bugs. There are currently no open-
source tools to facilitate the management of the referral process at the
community level, nor are there any examples of where software has been
co-developed from inception with the communities who use them.
In  [[2017]] , community members from the Wabun Tribal Council
(WTC), SFN, the Firelight Group and the SpICE lab began to co-develop
a web-based collaborative tool referred to as ‘Gather: The referrals man-
agement tool’ (hereafter ‘Gather’). From its inception, we intended Gather
to be an open-source, free to implement, easy to set up, intuitive to use,
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 213
extendible and integrated contemporary geographic citizen  [[science]]  tool.
It was designed to capture data that could provide evidence to the gov-
ernment and industry that community members are still active land stew-
ards and that resource extraction activities would impinge on their current,
and not just historical, livelihood activities. At the time of writing this
chapter, we have finished an initial draft of Gather and its associated
smartphone data-collection applications. Because of this, we can only
talk about the development of the tool and share some of the challenges
and barriers to the tool’s design, development and pilot launch. We do
not yet have any specific examples of interaction and uptake in the field.
2.2 Partners
The WTC is the regional  [[representative]]  for the  [[First Nations]]  of Brunswick
House, Chapleau Ojibway, Flying Post, Matachewan, Mattagami and Bea-
verhouse. These communities are located in north-eastern  [[Ontario]]  (see
Figure 10.1). The WTC’s Board of Directors comprises the chiefs of the
six communities. The WTC work in the fields of health, education, eco-
nomic development and resource development. WTC staff are responsi-
ble for negotiating  [[mining]]  development agreements in collaboration with
community leaders and acting as a point of contact for project propo-
nents and as a liaison in communications between  [[government]] , industry
and the communities.
SFN are located in Moberly Lake, northern  [[British]]  Columbia (see
Figure 10.1) and are a  [[Treaty]]  8 First Nation.  [[Treaty]]  8 territory covers
approximately 840,000 km^2 in what is now northern Alberta, north-east-
ern  [[British]]  Columbia, north-western Saskatchewan and the southern-
most portion of the  [[North]] west Territories. The  [[Treaty]]  provides the SFN
membership with (among other things) the constitutionally protected
right to hunt, fish and trap, and to gain a livelihood from the lands and
resources within  [[Treaty]]  8 territory. As SFN notes in its  [[2015]]  Comprehen-
sive Community Plan, ‘Practicing our  [[Treaty]]  Rights provides our people
with the means for a rich spiritual, social, and economic life. The land
and the activities carried out upon the land connect our people to their
past and provide them with the resources they need to build a healthy,
stable, culturally rich future’ (Saulteau  [[First Nations]]   [[2015]] , 7). Although
SFN were a key project partner during the initial stages of the project
design, staff turnover has meant that they are no longer involved in the
ongoing development of Gather.
The Firelight Group are a consulting group that works with indige-
nous and local communities throughout Canada and internationally. They
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
214 GEOGRAPHIC CITIZEN SCIENCE DESIGN
work in collaboration with many First Nation communities to provide
 [[research]] , policy, planning, negotiation and advisory services. Their work
focuses on culture, health, socio-economics, ecology and governance to
support the rights and interests of  [[indigenous]]  communities. Firelight are
driven by the principles of participation and capacity building. They
funded the initial stages of developing Gather through their Social Return
fund.
The SpICE lab, based at the  [[University]]  of  [[British]]  Columbia, Okanagan,
partners with  [[Canadian]]  and international communities to co-develop,
deploy and evaluate digital participatory mapping tools. The lab’s part-
nerships are framed within the practice of community-based  [[research]]
and represent a collaborative enterprise between  [[research]] ers and commu-
nity members. The SpICE lab’s  [[research]]  programme explores questions
related to how digital mapping technologies and associated processes
impact  [[indigenous]]  and vulnerable communities, and whether these tech-
Fig. 10.1 Location of Gather project partners.
Source: author.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 215
nologies can effectively capture – and add value and authority to – local
knowledge.
2.3 Project methodology
Because of the nature of the partners involved, the project is grounded in
the paradigms of  [[indigenous]]  methodologies (Kovach  [[2010]] ; Smith  [[2013]] )
and community-based  [[research]]  ( [[Israel]]  et al.  [[2001]] ; Minkler and Waller-
stein  [[2011]] ). This means that all aspects of this project (design, evalua-
tion, extension and outreach) are conducted in a reciprocal and an
empowering manner; the outcomes are of tangible benefit to the part-
nering  [[First Nations]] ; and community members feel a strong sense of own-
ership over the co-design process and the final technology. In concrete
terms, this has meant that the programming team responded directly to
the needs and concerns of our community partners. The community part-
ners became the principal architects and designers for Gather. This co-
design approach involved all actors in the project. We did not record any
of our meetings, as our intent was not for our process to be considered a
 [[research]]  exercise. Rather, we focused on the design of the tool itself and
its functionality. For this reason, we are not interested in conveying the
personal thoughts or details of the meetings, or in the geographic citizen
 [[science]]  data gathered using the tool. Once the tool is operational, we will
consider evaluating its usefulness, in which case we will be bound by our
university’s  [[research]]  ethics board requirements. However, we are not yet
at that point of deployment in the community.
Over the summer of  [[2017]]  ( [[May]] – [[August]] ), we co-designed and co-
developed the first iteration of Gather with the WTC and the lands man-
agers from the Beaverhouse First Nation, Brunswick House First Nation,
Chapleau Ojibway First Nation, Flying Post First Nation and Matachewan
First Nation, as well as the referrals team from SFN. We held a five-day
workshop in Timmins and a two-day workshop in Chetwynd with repre-
sentatives from the lands department. We used the materials produced
from these sessions to co-design the first draft of Gather. We continued to
meet regularly through videoconferencing. We also met for a third one-
day workshop in  [[Winnipeg]] , which was held prior to the Indigenous Map-
ping Workshop ( [[November]]   [[2017]] ). During these community workshops,
participants discussed their specific concerns and needs, including how
the software should look and function to address the varying require-
ments of each community.
Our design and development process was based on a ‘just-in-time’
iterative programming approach ( Wiki  Wiki Web  [[2005]] ). In other words,
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
216 GEOGRAPHIC CITIZEN SCIENCE DESIGN
during the workshops, we would focus on developing only the immedi-
ate requirements and functionality identified as being important by the
participants. This meant that in the mornings, we discussed and planned
the application’s functionality and workflow. During the afternoon and
evenings, the programming and digital design team coded Gather. Each
day, the team reported back, were offered additional suggestions and then
adapted the draft tool to meet those further recommendations. By the
end of the workshops, we had developed a partially functioning version
of Gather. As a result of this approach, participants were considerably
invested in the design of the tool and continued to work with the pro-
gramming team on its subsequent (and ongoing) development. Overall,
it was a successful and fulfilling – though at times exhausting – experience
in community engagement.
Creating Gather
3.1 initial intent
Prior to commencing the design and development workshops, we envi-
sioned the creation of a web-based platform that would focus on two user
groups: members of First Nation lands departments and industry propo-
nents. The tool would allow First Nation lands department members to
manage existing community traditional land-use data and also to view
the spatial intersection of proposed development projects and traditional
and contemporary community land uses. The software and associated
 [[database]] s could sit on  [[University]]  of  [[British]]  Columbia, community-located
or cloud-based servers, depending on the server management capacity
within the community and the availability of high-bandwidth hardware.
Industry proponents would upload all the project proposal documenta-
tion, including letters and permits, as well as a SHP (a common spatial
file type used by GIS software) or KML (the spatial file type used in  [[Google]]
Maps and other web mapping applications) file delineating the spatial
extent of the project. Lands department members would then overlay the
industry spatial extent file on [[top]] of their traditional use data and thus
have a clear visual representation of the impact of proposed projects on
the social, cultural, economic, subsistence, health and spiritual well-being
of the community and its membership (see Figure 10.2).
We wanted the user interface (UI) to be straightforward and intui-
tive, and for the tool itself to facilitate a semi-automated workflow built
around a structured set of predetermined steps. As specific steps are com-
pleted in the lands department’s workflow, automated messages are sent
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 217
to the industry proponent who can monitor their proposed project as it
moves through the community decision-making process. Thus, both the
lands department – through a more efficient referral management system –
and industry – through having an increased ability to monitor their indi-
vidual proposals – benefit from the tool.
Our design and development workshops largely supported our ini-
tial ideas, with one notable exception. Lands department members clearly
recognised the need to include all members of the community in the pro-
ject in order to encourage their engagement in the referrals process and
to contribute their own information related to contemporary community
use of the lands and resources. This helped to articulate clearly the need
for Gather to be usable for three unique user groups, each with their own
distinct set of needs and ways in which they interact with the system. In
other words, there was a need for Gather to enable:

Community members to volunteer and selectively share informa-
  tion pertaining to their contemporary use of the land through an
  intuitive mobile phone-based geographic citizen  [[science]]  data-
  collection app;
Fig. 10.2 Hypothetical example of the extent of an industry-proposed
project, represented by the grey polygon, overlaying community-
contributed geographic information.
Source: Gather app. Credit: Spatial Information for Community
Engagement Lab (SpICE). Basemap ©  [[Google]]  Maps.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
218 GEOGRAPHIC CITIZEN SCIENCE DESIGN
Community lands department managers and technicians to review,
  manage, delegate and respond to referrals, and produce reports that
  help clarify how proposed projects impact both traditional and con-
  temporary land uses; and
Industry to standardise their referral submission process and track
  the review of their referrals within the community’s workflow.
3.2 ui design
Gather’s initial UI design was loosely built around previous online par-
ticipatory geographic applications developed over the past 12  years in
the SpICE lab. The referrals document management functionality was
built directly into a map interface and made accessible through a single
web page view (see Figure 10.3). The specific interactive functions avail-
able through the UI varied according to the three unique user groups
(lands department, community member and industry). At its most basic
level, this meant that lands department members would see and interact
with a set of controls, queries and functions that supported the manage-
ment and response to referrals; these controls were not visible to the other
two user groups. Lands department members could also view commu-
Fig. 10.3 Referrals management tool – initial map-centric information
management interface.
Source: Gather app. Credit: SpICE. Basemap ©  [[Google]]  Maps.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 219
nity geographic citizen  [[science]]  contributions. Community members could
see and comment on their own and other community member contribu-
tions, but they could not interact with the referral data. Industry could
only view their own referrals and no other information.
The programming team’s prior experience developing online map-
ping tools meant that our initial draft of Gather was map-centric. Referral
data were managed entirely through the map interface, and data-manage-
ment tools were associated with icons and drop-down menus built around
the outside edges of the map (see Figure 10.3). After the community co-
design workshops, the UI was redesigned to focus on projects, tasks and
deadlines (see Figure 10.4). The map still plays an important role, but its
significance is muted, and it is only accessible when viewing informa-
tion about a specific project. This change was made because of the limi-
tations of the map interface for filtering and viewing large numbers of
proposed projects (sometimes in the thousands).
3.3 Mobile app
At the outset of the project, the programming team were focused on devel-
oping a tool that would be exclusively browser based and used primarily
by lands department members and secondarily by industry and govern-
ment proponents. This browser-based approach meant that the tool would
function on any operating system and not require any specialised soft-
ware, and that it would support the ability to share the same information
seamlessly between different user groups, as well as have a low entry
cost. After working directly with the lands managers, we modified the
system to include the development and integration of a mobile geographic
citizen  [[science]]  app to enable community members to volunteer (i.e. cap-
ture and share) examples of contemporary land use from the territory
using their own smartphones. Data could be collected by community
members at any time of the year and act as a repository of current and
relevant community land-use practices. This required developing both
iOS and Android apps that could be used by resource managers, hunters
and community members to record and share their activities.
Lands managers considered this to be of the upmost importance
because the data could be used to provide evidence to the  [[government]]
and industry that community members are still active land stewards and
that any resource extraction activity would impinge on their current, not
just historical, livelihood activities. However, the design, development
and use of a geographic citizen  [[science]]  app to support data collection
in northern Canada present their own sets of challenges. These include
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
Fig. 10.
Redesigned referrals management tool interface.
Source: Gather app. Credit: SpICE.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 221
limited (and largely non-existent) connectivity, the need to program for
a broad range of devices (due to both the age of the devices and the pres-
ence of multiple operating system versions) and issues related to  [[testing]] ,
training and app distribution. We recognise that these are common issues
in information and communications technology for development projects
around the world (Rashid and Elder  [[2009]] ; Aker and Mbiti  [[2010]] ) that
have been addressed through the development of tools, such as Sapelli
or ODK (Open Data Kit), which are open source, offer mobile data collec-
tion and can operate offline. However, we chose to develop our own suite
of apps, partially to develop the long-term s [[kill]] s and capacity in the SpICE
lab to offer these services to our partners, but also to ensure data consist-
ency and interoperability with our project servers,  [[database]] s and design
components.
4. Challenges to the community’s interaction
with the tool
Throughout the design, development and initial implementation stages
of Gather, we have both realised and constantly been reminded of the
needs and challenges of working with multiple users handling sensitive
 [[indigenous]]  information in digital form in a politically contentious envi-
ronment. It should be further noted that each community partner has
differing experiences with industry proponents, which in turn means that
each partner has a specific set of needs; this is reflected in the variations
in functionality required for the tool. We discuss these barriers and chal-
lenges in this section.
4.1 the challenge of getting people to use the software
The project has benefitted from a high level of participation by First Nation
land managers and community leaders. These groups were closely
involved in the co-design of both the overall project as well as the specific
software functionality. They are champions of the software both within
the community as well as in other  [[indigenous]]  communities in Canada
through presenting the tool at gatherings, such as the Indigenous Map-
ping Workshop. However, anecdotal evidence shows that it is hard for
them to introduce and encourage the use of mobile geographic citizen
 [[science]]  apps within their own communities. This is partially due to lim-
ited connectivity and many people in remote areas not having access to
high-speed mobile Internet. However, it is also difficult to persuade
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
222 GEOGRAPHIC CITIZEN SCIENCE DESIGN
people that their contributions are important and useful for lands depart-
ment managers and can be used to inform community decision making.
This remains a constant challenge. Furthermore, many of the community
members that continue to use the land for hunting, fishing and medicine
gathering tend to be older and are often less likely to use a mobile phone.
There is a need for the champions to communicate better the purpose of
data gathering to community members, as well as to express the impor-
tance of the community’s contributions and how their data will be used.
4.2 tension with commercial operations
One of the challenges we had not anticipated at the beginning of the pro-
ject was the tensions that emerged between our development team and
commercial referral management software providers. One business con-
tacted us several times about Gather’s functionality, and expressed con-
cern about the composition of our project partnerships. They were
especially uneasy about the role of the Firelight Group in the project,
who they felt had a conflict of interest and an unfair business advantage
through their involvement with our university-based programming
team. This did help us understand that within the university, we have
advantages regarding institutional support and access to resources that
are not available to many small businesses. The business was also con-
cerned that the software being made available as an open-source prod-
uct that is freely available might undermine the business model of small
 [[companies]]  offering referral management tools to other First Nation com-
munities. This tension is hard for us to reconcile. On one hand, we under-
stand the importance of not under [[mining]]  small business, but on the
other, we recognise that many small rural  [[First Nations]]  are overwhelmed
with the number of referrals, and they lack the financial and human
resources to respond effectively to this challenge. After discussions
between project partners and the university, we held true to our original
objectives of making Gather open source and freely available. We also
invited the concerned business to examine and use our open-source soft-
ware to augment their own offerings.
4.3 difficulty of creating generic software applications
Given the varying histories of the relationships between  [[indigenous]]  peo-
ples, industry and the  [[Crown]] , as well as the nature and/or scope of dif-
fering proposed projects, it is unrealistic to expect that the referrals process
will be same for  [[First Nations]]  throughout Canada. The WTC, for exam-
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 223
ple, had a close and long-term working relationship with several  [[mining]]
interests in their region. Therefore, they expected Gather to be a useful
tool to store and access existing project referral documentation and engage
community members through the mobile app. They did not view Gather
as a tool to structure their relationship with existing partnering indus-
tries. In contrast, SFN deals with a far greater number of industry propo-
nents, many of whom they do not have a relationship with. They hoped
that Gather would provide a structured approach to dealing with indus-
try. The SFN Lands Department already had a clear set of regulations and
protocols which systematised the ways in which they managed and
responded to referrals. SFN wanted Gather to emulate these protocols in
order to create greater efficiencies in their dealings with industry propos-
als and the  [[Crown]] .
In past projects, the SpICE lab has focused on custom code design
for projects that involve a limited number of partners. However, because
of the varying circumstances and different needs within different com-
munities involved in this project, there was limited agreement about the
specific functions required to manage large numbers of referrals. For some
of our project partners, Gather provides a rudimentary set of limited func-
tions; for others, the software provides too many functions, making it
overly complicated and difficult to implement. It has become important
to be able to articulate and communicate clearly who the software is tar-
geting and how they might use it. We decided it should be aimed at small
communities with limited resources; it is not designed for large commu-
nities that receive many thousands of referrals a year.
4.4 Mistrust between  [[representative]] s and communities
There is often a naivety among university  [[research]] ers working with First
Nations, particularly in regards to understanding ongoing community–
 [[government]]  tensions, such as those found when addressing issues of
land claims and land-use studies, as well as internal community tensions
related to the identification of community priorities through to the nature
of the information that members should be volunteering. This complexity
increases as more communities become involved in the design and devel-
opment of the technology. The programming team did not have the lux-
ury of remaining uninvolved in these tensions. We often had to engage in
soft mediation during decision-making sessions, which usually involved
offering technical solutions to human concerns. This was particularly the
case around how community information is managed and accessed and
by whom.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
224 GEOGRAPHIC CITIZEN SCIENCE DESIGN
4.5 Limitations of our map-centric approach
As noted above, this project required us to rethink our cartographic per-
spective. The referrals management tools were originally built directly
into a map interface and made accessible through a single web page view,
but the space constraints of this UI were too limiting. Nor did the tight UI
allow for the management of specific tasks related to projects. Our rede-
signed UI tried to mimic the steps of the SFN’s existing workflow and
tasks associated with managing each referral using a series of tabs with
the addition of a task management tool (see Figure  10.4). Ultimately,
this meant that the interface was considerably more textual in nature,
and the role of the map was diminished. This forced us to rethink our
approach to the significance of the geographic component and the geo-
graphic citizen  [[science]]  data. This has also helped us to increase the range
of software services that we can offer in other community-engaged
 [[research]]  projects.
4.6 Challenges of including  [[government]]  and industry
At the beginning of the project, we envisioned that Gather would be as
useful for  [[government]]  and industry proponents as for  [[First Nations]] . The
tool currently supports the uploading of industry referrals as both digital
text documents and spatial files (SHP and KML). However, we have found
it difficult to secure the participation of  [[government]]  and industry in the
project. Often, these actors are innovation averse and tied into their own
existing data-management systems. However, perhaps the explicit role
reversal of Gather – in other words,  [[First Nations]]  taking control of the
means and processes by which information is shared – might act as a fur-
ther challenge to these proponents’ involvement. In the next phase, we
will more directly consult industry and develop strategic partnerships to
ensure that the interface and workflow align with their existing data pro-
tocols and processes.
5. Conclusions
When we set out to design Gather, we did not intend that this would be a
commercial undertaking. Our motivations were driven by the clear need
to develop open-source software that can be used in small rural First
Nation communities to help them address the overwhelming nature of
the referrals process. Many of these communities do not have either the
financial or human resources to be able to deploy and use often complex
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 225
proprietary software. Our community partners also clearly recognised the
need for innovative approaches to include their membership base in con-
tributing information about how they currently use their lands and
resources. This was a vital step in informing referral decision making,
but also served to include the broader community in land-management
processes. We therefore feel that the components of Gather, including an
intuitive interface, the associated mobile apps and an industry upload
section, mean that the tool is relatively easy to use once it is set up. How-
ever, we recognise that several critical obstacles to successful and long-
term usability remain. The principal issue is that of connectivity. Many
areas in northern Canada remain outside of mobile phone coverage. Many
communities find it hard to maintain servers and server architecture
within the community. Therefore, if communities want to manage the
referrals effectively, they have often turned to commercial solutions. How-
ever, the cost of these solutions, as well as other challenges related to
usability, make it a difficult choice for many small communities to make.
Despite the barriers identified, the project has drawn considerable
interest among our project partners, as well as other First Nation com-
munities throughout Canada. We anticipate having an operational ver-
sion of the software available to communities by mid- [[2020]]  using an
open-source licence. We continue to be somewhat concerned about the
ongoing sustainability of the software because, as with any open-source
project, there will be a need to update both the usability as well as the
security required by the software in the future. We will therefore likely
consider some form of donation model from our users. However, this will
not be obligatory. In the meantime, we have secured grant funding for
the next three years (until  [[2022]] ) and will continue to improve function-
ality and scale up and make Gather available to whomever might want to
use the software.
6. Lessons learned
Be prepared to let go of your preconceived notions of what is needed.
  Just because it worked in the past or in another community does
  not mean that it will work in new contexts.
Be sufficiently agile to develop tools that suit the needs, capacity
  and limitations of the community with whom you work and regions
  in which you are based.
Try to remain separated from enduring and embedded politics, rec-
  ognising the need to seek to develop relationships with all potential
  actors, not just the easy ones.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
226 GEOGRAPHIC CITIZEN SCIENCE DESIGN
Ensure that all partners have a collective and common understand-
  ing of the purpose(s) of the project. Sometimes, it is useful to docu-
  ment this in a project charter so that if there are disruptions in the
  project, this road map may help reorient and reinvigorate your
  efforts.
Acknowledgements
We would like to acknowledge respectfully the ideas, input and enthusi-
asm of the lands managers from the Beaverhouse First Nation, Brunswick
House First Nation, Chapleau Ojibway First Nation, Flying Post First Nation
and Matachewan First Nation, as well as the members of Wabun Tribal
Council and the Resource Department of the Saulteau  [[First Nations]] . We
would also like to formally recognise our project funders, the Firelight
Group, Mitacs, the Real Estate Foundation of  [[British]]  Columbia and the
Mitsubishi Corporation Foundation for the Americas.
Notes
1 In Canada, the  [[Crown]]  is the source of sovereign authority and a part of the legislative, execu-
tive and judicial powers that govern the country (Harris  [[2006]] ). The term is commonly used
to refer to the functions of the  [[government]] .
2  [[First Nations]]  is a term used to describe the  [[indigenous]]  peoples of Canada. They have been
present on the land since time immemorial. There are more than 600  [[First Nations]]  communi-
ties in Canada, speaking more than 100 distinct languages.
References
Aker, Jenny C., and Isaac M. Mbiti.  [[2010]] . ‘Mobile phones and economic development in  [[Africa]] ’,
Journal of Economic Perspectives 24: 207–32.
Alfred, Taiaiake, and Jeff Corntassel.  [[2005]] . ‘Being  [[indigenous]] : Resurgences against contemporary
 [[colonialism]] ’, Government and Opposition 40: 597–614.
Angell, Angela C., and John R. Parkins.  [[2011]] . ‘Resource development and  [[aboriginal]]  culture in
the  [[Canadian]]  north’, Polar Record 47: 67–79.
Berkes, Fikret.  [[2017]] . Sacred Ecology , 4th ed. [[New York]]: Routledge.
Berkes, Fikret, Carl Folke and Johan Colding.  [[2000]] . Linking Social and Ecological Systems:
Management practices and social mechanisms for building resilience. Cambridge: Cambridge
 [[University]]  Press.
Borrows, John.  [[1994]] . ‘Constitutional law from a First Nation perspective: Self- [[government]]  and
the Royal Proclamation’,  [[University]]  of  [[British]]  Columbia Law Review 28: 1–47.
Caine, Ken J., and Naomi Krogman.  [[2010]] . ‘Powerful or just plain power-full? A power analysis of
impact and benefit agreements in Canada’s north’, Organization and Environment 23: 76–98.
 [[Canadian]]  Chamber of Commerce.  [[2016]] . Seizing Six Opportunities for More Clarity in the Duty to
Consult and Accommodate Process.  [[Ottawa]] :  [[Canadian]]  Chamber of Commerce.
Ecotrust Canada.  [[2017]] . Referrals Software an Analysis of Options. Portland, OR: Ecotrust Canada
and  [[Aboriginal]]  Mapping Network.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
dEvELoPing A rEfErrALS MAnAgEMEnt tooL in nortHErn CAnAdA 227
Foster, Hamar, Heather Raven and Jeremy Webber.  [[2011]] . Let Right Be Done:  [[Aboriginal]]  title, the
Calder case, and the future of  [[indigenous]]  rights.  [[Vancouver]] , Canada: UBC Press.
Gogal, Sandra, Richard Reigert and JoAnn Jamieson.  [[2005]] . ‘ [[Aboriginal]]  impact and benefit
agreements: Practical considerations’, Alberta Law Review 43: 129.
Harris, Carolyn.  [[2006]] .  [[Crown]] . Accessed 21  [[September]]   [[2020]] . https:// www. thecanadian
encyclopedia. ca / en / article / crown.
Hayter, Roger.  [[2003]] . ‘ “The  War  in the Woods”: Post-Fordist restructuring, globalization, and the
contested remapping of  [[British]]  Columbia’s forest economy’, Annals of the Association of Ameri-
can Geographers 93: 706–29.
 [[Israel]] , Barbara A., Amy J. Schulz, Edith A. Parker and Adam B. Becker.  [[2001]] . ‘Community-based
participatory  [[research]] : Policy recommendations for promoting a partnership approach in
health  [[research]] ’, Education for Health (Abingdon, England) 14: 182–97.
Joseph, Bob.  [[2015]] . 12 Common mistakes in First Nation consultation. Accessed 21 Febru-
ary  [[2017]] . http:// www. ictinc. ca / blog / 12 - common - mistakes - in - first - nation - consultation.
Kovach, Margaret.  [[2010]] . Indigenous Methodologies: Characteristics, conversations, and contexts.
 [[Toronto]] , Canada:  [[University]]  of  [[Toronto]]  Press.
Minkler, Meredith, and Nina Wallerstein.  [[2011]] . Community-Based Participatory  [[Research]]  for
Health: From process to outcomes. San Francisco, CA: John Wiley.
Morse, Bradford W.  [[2017]] . ‘Tsilhqot’in Nation v.  [[British]]  Columbia: Is it a game changer in  [[Canadian]]
 [[aboriginal]]  title law and  [[Crown]] –Indigenous Relations?’, Lakehead Law Journal 2: 65–88.
Power, Alex.  [[2017]] . ‘Duty to consult’ a cruel joke if  [[First Nations]]  can’t handle the load. Accessed
12  [[February]]   [[2020]] . https:// thetyee. ca / Opinion /  [[2017]]  / 01 / 16 / Duty - Consult - Cruel - Joke /.
Rashid, Ahmed T., and Laurent Elder.  [[2009]] . ‘Mobile phones and development: An analysis of
IDRC-supported projects’, The Electronic Journal of Information Systems in Developing
Countries 36: 1–16.
Saulteau  [[First Nations]] .  [[2015]] . Our Comprehensive Community Plan. Moberly Lake, Canada:
Saulteau  [[First Nations]] .
Smith, Linda Tuhiwai.  [[2013]] . Decolonizing Methodologies:  [[Research]]  and  [[indigenous]]  peoples. London:
Zed Books.
Turner, Nancy J., Marianne Boelscher Ignace and Ronald Ignace.  [[2000]] . ‘Traditional ecological
knowledge and wisdom of  [[aboriginal]]  peoples in  [[British]]  Columbia’, Ecological Applications 10:
1275–87.
 Wiki  Wiki Web.  [[2005]] . Just in time programming. Accessed 2  [[March]]   [[2019]] . http:// c2. com / xp
/ JustInTime [[Programming]] . html.
Zietsma, Charlene, Monika Winn, Oana Branzei and Ilan Vertinsky.  [[2002]] . ‘The  War  of the Woods:
Facilitators and impediments of organizational learning processes’,  [[British]]  Journal of
Management 13: S61–74.
This content downloaded from 192.30.202.8 on Fri, 16 Jul 2021 02:25:43 UTC
