### Date: 5 May 2019
### Name(s): Christian Lussier, Robert Samuel, Jordan Wilson

### Final Report

#### Project Overview
Our project looks into a variety of questions surrounding African development and economics using database systems. African development and economic trajectories are a hot topic for researchers and organizations tasked with implementing sustainable growth in African countries. As a result, our project looks into a number of things, such as why Africa's Real GDP growth rate suddenly declined after years of steady growth and if there is a correlation between region of residence and citizen happiness. Our research has provided a number insights into these questions, finding for instance, that African citizens of countries in the MENA region seem to be much happier than those in Sub-Saharan Africa. Our project will use database systems to try and answer questions related to the development and economic trajectories of African countries.

##### Motivation
We were motivated to pursue this project for a number of reasons. For one, despite African countries gaining independence from their colonial masters in the mid-1900s and receiving financial aid, loans, and more, African countries have faced great problems in their development and with developing their economies to compete in the global market. We were motivated to try and see if we could try to solve some of these problems or at least find clues/correlations relating to these problems. Additionally, a few of our group members are economics minors taking classes relating to African Development, making them interested in learning more outside of that class.

This project has real-world relevance in that it is looking at real data regarding Africa. With this, economists and development experts are trying to solve problems relating to Africa's poor development and economic patterns. This research could benefit others in this regard, such as the experts researching Africa everyday to try and solve problems. We feel that trying to answer the questions below could provide some valuable insights into what is stopping African economic development. With this, these questions could find correlations between different ideas to see if they have any impact on another. The correlations and results stemming from this research could provide valuable insights into these problems. Additionally, the casual observer who is interested in African economics could also be benefitted by this research as they could find out more about the topic.

* Why did we choose this project?
* How will this research benefit others?

##### Background Information
* Explanation of related works
  * How are they relevant to our Project?

There are a variety of related works that discuss Africa's slow development patterns and poor economic trajectories. For example, the source ["Why Has Africa Grown Slowly"](https://www.aeaweb.org/articles?id=10.1257/jep.13.3.3) touches upon a number of ideas surrounding Africa's slow growth over the last twentieth century, while discussing some of the issues African economies have faced. This source notes that while Africa's economic and development future looked bright in the 1960s, political deterioration stemming from the implementation of dictatorship and autocratic regimes hurt the economic trajectories of many African countries. With this, the source also notes that African countries seem to have much higher trade barriers and misaligned exchange rates than their global peers. Additionally, the authors Collier, Paul, and Gunning, note that one the many factors contributing to the poor and ever-changing economies of African countries is a heavy reliance on natural resources. This reliance often leads to unsustainable and unpredictable outcomes that comes with the market value of the resources on a global scale. This is part of the reason why for question 5, we are looking into the economics of countries with higher natural resource rents.

Additionally, [a related work from the Wiley Online Library](https://onlinelibrary.wiley.com/doi/epdf/10.1111/roiw.12013) also touches upon this subject, discussing the contemporary statistical foundations of the recent growth in per-capita GDP and reduction in poverty, finding that these "growths" were actually quite weak in reality. This source also discusses how the data published by African companies about their economies is often weak or inflated from previous works. This is because many African countries do not have the capability to collect, manage, and properly analyze data that they are actually able to collect. This is in part because of a lack of funding for this area and fragmentation between groups assigned to work with this data.

Another source that discusses African economies comes in the form of ["Foreign Direct Investment and Economic Growth: The Case of Developing African Economies"](https://link.springer.com/article/10.1007/s11205-014-0679-6). This work looks into the relationship between foreign direct investment (FDI) and economic growth for 23 African countries over a period spanning from 1970 to 2011. The research from this source indicates that there is a "bidirectional causal relationship between economic growth and FDI". With this, the authors note that while FDI was found to have a positive impact on the economies of African countries, that these effects do vary from country to country. The study goes on to note that African countries should take more steps to promote FDI.

###### References
- Collier, Paul, and Jan Willem Gunning. 1999. "Why Has Africa Grown Slowly?" Journal of Economic Perspectives, 13 (3): 3-22.
- Devarajan, S. (2013), Africa's Statistical Tragedy. Review of Income and Wealth, 59: S9-S15. doi:10.1111/roiw.12013
- Seyoum, Mebratu, Renshui Wu, and Jihong Lin. "Foreign direct investment and economic growth: The case of developing African economies." Social Indicators Research 122.1 (2015): 45-64.

##### Building Our Database System
We took a variety of steps to build our database system. We began by acquiring data from credible online sources, such as the World Bank (the data used will be detailed below for the relevant questions). After procuring our data, we began to build our database system using Sqlite3. To do this, we first created a database builder file called `africaDB-build.txt`. This file contains a command to run the builder file, `africaDB-build.txt | sqlite3 africaDB.sqlite3`. It also contains code that will drop/create the necessary tables that will be used to store the data acquired from online sources. Additionally, the builder file also contains schema that will be used for some of the tables where necessary, that will put the attributes and lay out the necessary information for each table.

After this, the builder file sets the separator which will be used to separate the data being read in by the Sqlite3 database. In this case, the separator is set as a comma, `,`, because the database will be reading in CSV files where the values are separated by commas. The builder file then contains code that will read the CSV files into the database, putting them in their specific tables, so that they can be accessed for work with queries and other database-related tasks.

###### Tables & Schema

![SQLite3 Database Terminal](graphics/current-database.png)



###### User Interface
We looked into a variety of different ways to create a user interface for our project. The user interface needed to allow users to interact with the database but not contain visible querying code. With this criteria in mind, we narrowed down our interface options to three different tools, Djano, Flask, or a command-line based Python interface. Eventually, we decided to create a Python command-line interface for a few reasons. For one, we felt that we had more experience in using Python with Sqlite3 for such a purpose which would make it easier and less time consuming to implement than the other options. Additionally, we felt that for the criteria required, a command-line interface would be very simple to use while still allowing the user to complete all necessary actions.

The command line interface allows the user to complete a number of tasks, by giving users a variety of different options with how to run the program. For instance, it allows the user to display all of the data from a table of their choosing, without forcing them to write a query and instead allowing them to just enter a table name. Additionally, there are features in place that allow the user to get the names of the tables in the database, a brief description of each, and the table schema. The user can also perform a query in a table of their choosing, using conditions that they specify. Additionally, users can also insert content into tables of their choosing and update/edit tables. Also, users can use a feature that will display the research questions for the project, the query used to solve them, and the query results.

The user interface when the program is first ran (using the command `python3 interface.py`):
![User interface start up screen with welcome message.](graphics/user-interface-startup.png)

Upon starting the program and seeing this interface, the user can then choose which option they would like to use by reading the description of the option and then simply entering the number pertaining to their chosen option. This option will then call a method pertaining to this option.

For instance, here is the output of a user who choose to run option 1 which allows them to display the data from a selected table:
![User interface running with option 1.](graphics/user-interface-1.png)

Additionally, here is the output of a user running option 6 which allows the user to update the table:
![User interface running with option 6.](graphics/user-interface-6.png)

Also, the program has functionality that allows the user to continue using the program after running through an option, meaning that they can choose to exit the program or run another option. Here is an example of this:
![User interface displaying the exit option after using option 1.](graphics/user-interface-exit.png)

This user interface, created using Python and the Sqlite3 package, allows the user to easily interact with the Sqlite3 database in a text-based setting. With this, it does not force the user to concern themselves with writing Sqlite3 queries or insert statements. It instead allows the user to interact with the database in a simple manner, allowing them to do things such as look at a table's data and schema, perform update and insert commands for a specified table, and perform customized queries. This interface enhances the user experience when interacting with the project database.

#### Research Question 1
Africa's Real GDP Growth rate seemed to steadily increase for a few decades, but then it took a downturn. When did this downturn occur and why?

##### Introduction
Why are we asking it? Why is relevant?

##### Queries
How did we answer it? What tools did we use? What data?
The query used in the database was:
```
select "2008", "2009","2010","2011","2012" from RealGDPGrowth;
```

##### Results
Results
How we know results from query are correct

###### Graphics
Graphics for results.

<!-- ------------------------------------------------------------------ -->
#### Research Question 2
Is there a correlation between GDP per capita and inequality rankings (income inequality)?

#### Introduction

It can be reasoned that wealthier countries should have a lower inequality gap since there is more wealth to be distributed. However, this may not always be the case due to various reasons. For example, the style of government could facilitate mass hoarding of wealth by the upper class, which tends to happen in dictatorships. The goal of this question find a correlation between inequality and a countries GDP.

#### Queries
This question used data from the HPI table to get information regarding inequality. It also used data from the DevIndicators table in order to look at the GDP Per Capita for African countries.

The queries used in this question were:
```
SELECT Country, Inequality from HPI WHERE region = "Sub Saharan Africa" OR "Middle East and North Africa";

SELECT "Time", "Country Name", "GDP per capita (current US$) [NY.GDP.PCAP.CD]" from DevIndicators WHERE "Country Name" = "Mauritius" OR "Country Name" = "Ethiopia" OR "Country Name" = "Zambia" OR "Country Name" = "Kenya" OR "Country Name" = "Mozambique" OR "Country Name" = "Comoros" OR "Country Name" = "Nigeria" OR "Country Name" = "Liberia" OR "Country Name" = "Tanzania" OR "Country Name" = "Malawi" OR "Country Name" = "Zimbabwe" OR "Country Name" = "Senegal" OR "Country Name" = "Namibia" OR "Country Name" = "Ghana" OR "Country Name" = "Rwanda" OR "Country Name" = "Uganda" OR "Country Name" = "Republic of Congo" OR "Country Name" = "Mauritania" OR "Country Name" = "Burkina Faso" OR "Country Name" = "Gabon" OR "Country Name" = "Niger" OR "Country Name" = "Cameroon" OR "Country Name" = "Lesotho" OR "Country Name" = "Botswana" OR "Country Name" = "Djibouti" OR "Country Name" = "South Africa" OR "Country Name" = "Guinea" OR "Country Name" = "Burundi" OR "Country Name" = "Swaziland" OR "Country Name" = "Sierra Leone" OR "Country Name" = "Cote d'Ivoire" OR "Country Name" = "Benin" OR "Country Name" = "Togo" OR "Country Name" = "Chad";
```

The first query used to answer this question gets the country name and inequality percentage ranking from the HPI table where the region is either Sub-Saharan Africa or the MENA region so that only African countries are outputted. The second query selects the year ("Time"), Country Name, and GDP Per Capita from the DevIndicators table. Additionally, this query uses "OR" statements to find and display data from African countries only.

##### Results

###### Graphics

<!-- ------------------------------------------------------------------ -->
#### Research Question 3
Is there a correlation between living standards (HPI) and GDP per capita?

##### Introduction

In most cases wealthier countries are able provide a better standard of living for their citizens. For example, in the U.S. inequality tends to be high between different economic classes, however this tends to negligible in many cases because the living standard for almost any American is higher than that of of a third world country. In some cases the living standard for the poorest segment of Americans could be better than that of the upper class of other poorer nations. For a continent like Africa, which has many third world nations,

##### Queries

The queries used in the question were:
```
SELECT Country, HPI from HPI WHERE region = "Sub Saharan Africa" OR "Middle East and North Africa";

select "Time", "Country Name", "GDP per capita (current US$) [NY.GDP.PCAP.CD]" from DevIndicators;
```
##### Results

###### Graphics

<!-- ------------------------------------------------------------------ -->
#### Research Question 4
Are countries that live in a specific region overall happier than countries that don't live in that region? (i.e. Sub-Saharan Africa and MENA)

##### Introduction

##### Queries

The query used in the database was:
```
select * from HPI where region = "Sub Saharan Africa" OR "Middle East and North Africa";
```

##### Results

##### Graphics

<!-- ------------------------------------------------------------------ -->
#### Research Question 5
Do African countries with a higher natural resources rent (as a % of GDP) have a higher GDP per capita or vice versa? Do the findings from this question make steps to validate the idea of the resource curse?

##### Introduction
Many countries in Africa are afflicted by the resource curse, which when a country has an abundance of natural resources, but they are unable to properly collect them due to various reasons. Major reasons include intercontinental wars, civil wars, a lack of technology, or they're simply too dangerous to extract. This has led to several countries that have a low GDP, yet an abundance of resources. The queries for this question aim to affirm whether this resource curse is true.

##### Queries

The following queries were used to answer this question:
```
select "Country Name", "2011" from Resources;

select * from DevIndicators WHERE "Time" = 2011;
```

##### Results


###### Graphics

<!-- ------------------------------------------------------------------ -->
#### Concluding Remarks


###### Please add screen shots in your report. The code to add graphics is the following:
![myImage](graphics/gators.png)
(edit as necessary)
