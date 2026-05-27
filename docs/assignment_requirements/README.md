**READ THIS FIRST**

This assignment is done in pairs, or individually if you have received approval in advance.

The assignment is divided into several parts, but the main thread is simple:

you will take a messy historical dataset, create a curated dataset that can be trusted, store it in a database, and then make it available through an API. Part 1 should be done within 1-2 days max, part 2 probably 1 week, and part 3 most likely around 1 week, is a reasonable time frame.  Start by reading the entire assignment, then you can focus on one part at a time, you really don’t have to worry about the next part until you get there. Part 2 and 3 might be slightly related, but I would say: don’t worry, just one at a time.

## Clone the repository
Link: 

## Assignment Description

You will work from the instructions in `part_1` and `part_2`.

You will also record a video presentation where both of you are visible on camera and talk through your work. More on that further down.

## Why Are We Doing This Assignment?

In the pandas lessons, you learned how to read data, inspect it, clean it, and export it.

In this assignment, we take the next step.

You are not only analyzing data. You are creating a dataset that another application could use. This is where the connection to the upcoming lessons on APIs and SQL comes in.

Think of it like this:

- pandas helps you transform the data
- SQL helps you store it in a more realistic way
- FastAPI helps you make the data available to others

## Part 1. Pandas

In `part_1` there is a smaller notebook where you practice pandas.

This is a warm-up part. You are expected to do it together. You are not allowed to divide the tasks between you and work separately. Sit together physically or over Discord. Take turns writing code. Live Share in VS Code is recommended.

## Part 2. Build a Curated Dataset

This is the main focus of the assignment.

You will work with MYH's public Excel files containing results from application rounds for higher vocational education programs:

https://www.myh.se/yrkeshogskolan/resultat-ansokningsomgangar/resultat-for-program

### Your Task

Imagine that someone wants to follow the development of applications to vocational education programs over time.

The problem is that the data is spread across multiple Excel files, over several years, with slightly different structures, different column names, and different ways of expressing the same thing.

Your task is to:

1. choose relevant years
2. understand which sheets are relevant
3. harmonize the data
4. clean it
5. document your decisions
6. export a finished dataset
7. load it into SQL
8. build a small API on top of it

### Recommended Scope

To keep the assignment reasonable, I recommend that you use:

- at least `3` years
- preferably `2022` to `2025`

Older years can also be used, but the harmonization becomes harder. If you decide to include `2020` or `2021`, that is completely fine, but do it intentionally.

### Important Note About the Excel Sheets

If you inspect the files, you will notice that they contain several different tables.

For the main table, I recommend that you build your solution around `Tabell 3`.

That is the table that works best as a main applications table.

`Tabell 4` can also be interesting, but it is at a different level of detail. The same application can appear several times there because one program may be connected to several municipalities. Because of that, you should not mix that table into the main table without thinking carefully.

A good approach is:

- use `Tabell 3` as the main source
- treat `Tabell 4` as a separate extra table if you want to go further

## What the Notebook in Part 2 Should Contain

Your notebook should be possible to follow step by step. It should not only contain code. It should also show how you are thinking.

A good structure is:

1. Short introduction to the data source
2. Which years and sheets you chose, and why
3. First exploratory look at the raw data
4. Description of your target table
5. Harmonization of columns and values
6. Data cleaning
7. Enrichment
8. Validation and quality checks
9. Export
10. Short reflection

### Target Table

You should try to create a clear main table that represents applications.

You do not have to use exactly these names, but the table should roughly contain:

- `source_year`
- `source_file`
- `source_sheet`
- `diarienummer`
- `utbildningsnamn`
- `utbildningsområde`
- `beslut`
- preferably also a normalized version of the decision
- `kommun`
- `län`
- `yh_poang`
- `studieform`
- `studietakt_procent`
- `utbildningsanordnare`
- `huvudmannatyp`

If you use newer years, you may also include things like:

- `sun5_inriktning`
- `sun5_inriktning_namn`
- `seqf_niva`
- `smalt_yrkesomrade`

You do not have to include everything. What matters is that you create a consistent and well-documented dataset.

### Harmonization

This is an important part, but it is not the whole assignment.

Examples of things you will likely need to handle:

- column names that differ between years
- provider fields that are almost the same but not quite
- `Beslut` which in some years is written as `Ej beviljad` and in others as `Avslag`
- `Huvudmannatyp` where values like `Landsting` and `Region` may need to be harmonized
- sheets where the real header is not on the first row

### Data Cleaning

You are expected to clean the data in a thoughtful way.

Examples:

- remove unnecessary columns
- rename columns
- convert data types
- normalize text values
- handle null values where needed
- investigate duplicates

### Enrichment

Transformation is not only about cleaning. Sometimes it also means making the data more useful.

That can mean adding new columns created from existing data, or connecting new information if it adds clear value.

Examples:

- a normalized decision value, such as `approved` or `rejected`
- boolean flags, such as whether the program is distance-based or not
- traceability back to the source with `source_year`, `source_file`, and `source_sheet`

If you want to use external data sources for enrichment, that is allowed, but it is not required.

## Part 3. Store and Expose the Data

Once you have built your curated dataset, you should also make it usable for other parts of a system.

### SQL

You should load the finished data into a SQL database, for this lab, using a file based database such as sqllite - otherwise I’d recommend postgresql due to its great support.
The goal is to show that the data does not only live in a notebook, but can also be stored in a more realistic way.

There should be:

- a table structure that fits your dataset
- code or SQL that creates the tables
- code that loads the transformed data

### API

You should also build a small API on top of your database.

The point here is to show that the data you created can be used by other systems.

You do not need to build a large product, but the API should still feel like a real small internal data service rather than a thin demo.

That means the API should do more than return one table without any useful logic.

It should let a consumer:

- fetch individual records
- browse lists of records
- filter the data in useful ways
- get aggregated statistics

### What the API should roughly include

At minimum, your API should include endpoints in these categories:

1. Record access
2. Filtering or browsing
3. Statistics or aggregation

In practice, a good minimum would be something like:

- `GET /applications`
- `GET /applications/{diarienummer}`
- `GET /stats/by-year`
- simple filtering through query parameters on `/applications`

You can then add more endpoints depending on how you structure your solution.

### Good examples of endpoint ideas

- `/applications`
    - returns a list of applications
    - should ideally support query parameters such as year, decision, region, municipality, provider, or study form
- `/applications/{diarienummer}`
    - returns one specific application
- `/stats/by-year`
    - simple yearly statistics
- `/stats/by-education-area`
    - grouped statistics by education area
- `/export/applications`
    - optional export endpoint, for example CSV or JSON

### Export endpoints

Export endpoints can be a very good idea if you want your API to feel more realistic.

For example, another team might want to download filtered data instead of browsing records one by one.

Endpoints like these can make sense:

- `/export/applications?year=2024&decision=approved`
- `/export/applications?provider=...`

This is not a requirement, but it is a strong optional direction if you want your API to feel more useful.

### Operational endpoints

If you want to go a bit further, another realistic idea is an endpoint that triggers a refresh or ingestion run.

In this assignment, the simplest version just means rerunning the pipeline on the source files and refreshing the SQL tables.

A more advanced version could also fetch the latest MYH files before rerunning the pipeline.

Good examples:

- `POST /refresh`
- `POST /ingestion/run`

This is not required, but it is a good advanced direction if you want your API to feel closer to a real internal data service.

### If you use `Tabell 4`

If you choose to model `Tabell 4` as a separate table, your API can become more interesting.

Then you could expose more detailed location-based endpoints, for example locations for a given application or statistics by municipality.

### What I expect from the API design

The API does not need authentication or user accounts.

This should mainly be a read API.

The important part is that it clearly shows that your curated dataset can be queried and reused by another system.

So I expect the API to:

- read from your SQL database
- return JSON responses
- expose several useful read endpoints
- include at least some filtering
- include at least some aggregation done in SQL or in well-structured Python code

### What you do not need to build

You do not need to build:

- login or authentication
- a large number of endpoints
- a frontend
- a production-ready deployment setup

The goal is not to build a full product. The goal is to show that the dataset you created can be operationalized and consumed in a sensible way.

## What You Should Submit

At the end, you should have the following:

- a finished `part_1` notebook
- a clear transformation notebook for the main assignment
- a curated dataset that is exported by the notebook or by a separate script
- code to create and populate a SQL database
- a small FastAPI project that reads from the database
- a git history showing steady work over time
- a video presentation

## What Matters Most in the Assessment

The most important thing is not that you build the most features.

The most important thing is that you show that you understand the journey from raw data to something usable.

Because of that, I will mainly look at:

- whether you understood the source files
- whether you made reasonable harmonization decisions
- whether you can justify your cleaning decisions
- whether the final result feels consistent and useful
- whether the solution can be run again
- whether you can explain why you structured the data the way you did
- whether the SQL and API parts actually connect to the dataset you built

## Godkänd (G)

For `Godkänd`, the goal is to show that you can build a clear, working end-to-end solution without making it overly advanced.

For `G`, you should in practice do the following:

- complete `part_1`
- create a notebook that reads the raw data from the start and transforms it into a finished curated dataset - I should be able to run it and by the end of it, assuming I have the excel files, have a finished dataset exported as CSV or Parquet
- use at least `3` years of MYH data
- use `Tabell 3` as the backbone of your main applications table
- show that you understand harmonization, data cleaning, and at least some enrichment
- export a finished curated table
- load that table into SQL
- build a small read-oriented API on top of it
- present the data journey and your technical decisions in a natural way

For the API, a reasonable `G` level is something like:

- one endpoint for listing applications
- one endpoint for getting a specific application
- one statistics endpoint
- some simple filtering, either through query parameters or a separate endpoint

At `G` level, the important thing is not that the API is large. The important thing is that it clearly works with the dataset you created.

## VG

For `VG`, I expect a stronger and more thoughtful solution.

That usually means that the work is not only correct, but also more realistic, better structured, and more useful for another consumer.

Examples of things that fit well at `VG` level:

- a cleaner and more deliberate overall solution
- stronger harmonization across difficult years
- better validation and data quality checks
- more thoughtful enrichment
- a more capable API with better filtering and more useful aggregated endpoints
- export endpoints, for example CSV or JSON exports of filtered data
- an operational endpoint, for example an endpoint that triggers a refresh or ingestion run
- more polished or more useful `POST` endpoints on the write side

Examples of API features that fit especially well for `VG`:

- `/providers`
- `/providers/{provider_name}/applications`
- `/stats/by-region`
- `/export/applications`
- `/export/stats/by-year`
- `/applications/{diarienummer}/notes`
- `/applications/{diarienummer}/flags`
- `POST /refresh`

You do not need to implement every advanced idea above to reach `VG`.

You also do not need a more advanced multi-table schema just to reach `VG`.

For example, using `Tabell 4` as a separate table can absolutely be a good advanced direction, but it is optional. It is one possible way to go further, not an expectation.

The point is that `VG` should show stronger design choices, stronger technical execution, and a more useful end result, even if the overall data model stays fairly simple.

## Optional Ideas

If you finish early and want to go further, there are still several good directions

- a basic Power BI dashboard
- a basic Streamlit dashboard

This should be treated as a bonus layer on top of the real assignment, not as the main goal.

Power BI and Streamlit are optional here.

## AI

AI is allowed and encouraged, especially in Part 2 when you explore messy Excel files, compare schemas across years, and draft pandas code for harmonization and cleaning. A good example is using a tool like Claude Code or Codex to inspect a few source files, suggest harmonization rules, and give you a first draft that you then review, adapt, test, and explain yourselves.

For Part 3, I recommend a more hybrid approach. It is fine to use AI for SQL help, FastAPI boilerplate, debugging, and endpoint ideas, but the final structure and glue code should still be something you genuinely understand. Do not paste in a full AI-generated solution and stop there. In the video, it should be clear that you can explain what the code does, why you structured it the way you did, and where AI helped you.

## Video Presentation - around 15-30 minutes

At the end, you should record a video, the length is not that important.

Show:

- your transformation notebook
- what the raw data looked like
- how you reasoned about harmonization and cleaning
- the finished SQL database
- your API

The purpose of the video is to let you explain your work as if you were demoing it to a colleague.

You do not need to present every single detail. Focus on the most important parts:

- problems you discovered
- decisions you made
- how you solved them
- what the final result became

### Upload the Video

Upload the video to Google Drive and make it public. Test the link in an incognito window before you submit it.

## Recording With 2 Cameras

A simple solution is to have a video call in Discord and keep both video windows visible at the same time.

- create a Discord call with video
- choose the full screen as a source in OBS
- make sure OBS captures audio from both of you
- Live Share is recommended if the person not sharing the screen also needs to control the code
- light editing is OK, but do not overdo it
- make sure both of you are clearly visible and audible
- make sure both of you get roughly equal time to speak