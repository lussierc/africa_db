#### Date: 5 May 2019
#### Name(s): Christian Lussier, Robert Samuel, Jordan Wilson

#### Final Report

##### Project Overview
Our project looks into a variety of questions surrounding African development and economics using database systems. African development and economic trajectories are a hot topic for researchers and organizations tasked with implementing sustainable growth in African countries. As a result, our project looks into a number of things, such as why Africa's Real GDP growth rate suddenly declined after years of steady growth and if there is a correlation between region of residence and citizen happiness. Our research has provided a number insights into these questions, finding for instance, that African citizens of countries in the MENA region seem to be much happier than those in Sub-Saharan Africa. Our project will use database systems to try and answer questions related to the development and economic trajectories of African countries.

###### Motivation
We were motivated to pursue this project for a number of reasons. For one, despite African countries gaining independence from their colonial masters in the mid-1900s and receiving financial aid, loans, and more, African countries have faced great problems in their development and with developing their economies to compete in the global market. We were motivated to try and see if we could try to solve some of these problems or at least find clues/correlations relating to these problems. Additionally, a few of our group members are economics minors taking classes relating to African Development, making them interested in learning more outside of that class.

This project has real-world relevance in that it is looking at real data regarding Africa. With this, economists and development experts are trying to solve problems relating to Africa's poor development and economic patterns. This research could benefit others in this regard, such as the experts researching Africa everyday to try and solve problems. We feel that trying to answer the questions below could provide some valuable insights into what is stopping African economic development. With this, these questions could find correlations between different ideas to see if they have any impact on another. The correlations and results stemming from this research could provide valuable insights into these problems. Additionally, the casual observer who is interested in African economics could also be benefitted by this research as they could find out more about the topic.

* Why did we choose this project?
* How will this research benefit others?

###### Background Information
* Explanation of related works
  * How are they relevant to our Project?

There are a variety of related works that discuss Africa's slow development patterns and poor economic trajectories. For example, the source ["Why Has Africa Grown Slowly"](https://www.aeaweb.org/articles?id=10.1257/jep.13.3.3) touches upon a number of ideas surrounding Africa's slow growth over the last twentieth century, while discussing some of the issues African economies have faced. For instance, the authors Collier, Paul, and Gunning, note that one the many factors contributing to the poor and ever-changing economies of African countries is a heavy reliance on natural resources. This reliance often leads to unsustainable and unpredictable outcomes that comes with the market value of the resources on a global scale. This is part of the reason why for question 5, we are looking into the economics of countries with higher natural resource rents.

Additionally, the [a related work from the Wiley Online Library](https://onlinelibrary.wiley.com/doi/epdf/10.1111/roiw.12013) also touches upon this subject, discussing the contemporary statistical foundations of the recent growth in per-capita GDP and reduction in poverty, finding that these "growths" were actually quite weak in reality.

####### References
- Collier, Paul, and Jan Willem Gunning. 1999. "Why Has Africa Grown Slowly?" Journal of Economic Perspectives, 13 (3): 3-22.
- Devarajan, S. (2013), Africa's Statistical Tragedy. Review of Income and Wealth, 59: S9-S15. doi:10.1111/roiw.12013

###### Building Our Database System
We took a variety of steps to build our database system. We began by acquiring data from credible online sources, such as the World Bank (the data used will be detailed below for the relevant questions). After procuring our data, we began to build our database system using Sqlite3. To do this, we first created a database builder file called `africaDB-build.txt`. This file contains a command to run the builder file, `africaDB-build.txt | sqlite3 africaDB.sqlite3`. It also contains code that will drop/create the necessary tables that will be used to store the data acquired from online sources. Additionally, the builder file also contains schema that will be used for some of the tables where necessary, that will put the attributes and lay out the necessary information for each table.

After this, the builder file sets the separator which will be used to separate the data being read in by the Sqlite3 database. In this case, the separator is set as a comma, `,`, because the database will be reading in CSV files where the values are separated by commas. The builder file then contains code that will read the CSV files into the database, putting them in their specific tables, so that they can be accessed for work with queries and other database-related tasks.

<!-- OUTLINE:
##### Research Question 1
Question
###### Introduction
Why are we asking it? Why is relevant?

###### Methods
How did we answer it? What tools did we use? What data?
Query

###### Results
Results
How we know results from query are correct

###### Graphics
Graphics for results.  -->

##### Research Question 1
Africa's Real GDP Growth rate seemed to steadily increase for a few decades, but then it took a downturn. When did this downturn occur and why?

###### Introduction
Why are we asking it? Why is relevant?

###### Methods
How did we answer it? What tools did we use? What data?
The query used in the database was:
```
select "2008", "2009","2010","2011","2012" from RealGDPGrowth;
```

###### Results
Results
How we know results from query are correct

###### Graphics
Graphics for results.

<!-- ------------------------------------------------------------------ -->
##### Research Question 2
Do countries with higher GDP growth/GDP per capita have higher Happy Planet Indexes (representing citizen happiness)?

###### Introduction

###### Methods

###### Results

###### Graphics

<!-- ------------------------------------------------------------------ -->
##### Research Question 3
Is there a correlation between living standards (HPI) and GDP per capita?

###### Introduction

###### Methods

###### Results

###### Graphics

<!-- ------------------------------------------------------------------ -->
##### Research Question 4
Are countries that live in a specific region overall happier than countries that don't live in that region? (i.e. Sub-Saharan Africa and MENA)

###### Introduction

###### Methods

The query used in the database was:
```
select * from HPI where region = "Sub Saharan Africa" OR "Middle East and North Africa";
```

###### Results

###### Graphics

<!-- ------------------------------------------------------------------ -->
##### Research Question 5
Do African countries with a higher natural resources rent (as a % of GDP) have a higher GDP per capita or vice versa? Do the findings from this question make steps to validate the idea of the resource curse?

###### Introduction

###### Methods

Queries:
```
select * from Resources WHERE "2011" > 11;
```
```
select * from DevIndicators WHERE "Time" = 2011;
```

###### Results

###### Graphics

<!-- ------------------------------------------------------------------ -->
##### Concluding Remarks

##### References

###### Please add screen shots in your report. The code to add graphics is the following:
![myImage](graphics/gators.png)
(edit as necessary)
