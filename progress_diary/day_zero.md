# Day 0 - Setting up a game plan

Tuesday 13 October 2020

[confirms.pepper.spilling](https://what3words.com/confirms.pepper.spilling)

---

Today is my zero'th day working on my portfolio project. A summary of what my 
portfolio project is about can be found [here](https://docs.google.com/document/d/1u1YjIWu_SO1AMHZtYyueebLgWwt5T2az9wG3lOARwNY/edit?usp=sharing).

I fully expect the final product of this adventure to be very different from
that original game plan. Let's see how it goes. 

## Priorities today

* It's time to find and clean up all the data I intend to use.
    * I will be downloading all the 2019-2020 municipal budgets for all
    Puerto Rico municipalities.

* I want to make sure I have a minimum viable piece of code. Anything. Just
to start getting my feet wet. I'll be creating an instance of a Flask web app
and an example of an initial API today.

* Lastly, I want to make sure I have a viable architecture, so I'll just be
double-checking that.

## Finding and cleaning the data

* So all the Puerto Rico municipal budgets are available as PDFs in the
Puerto Rico Office of Management and Budget Website. The specific link is
this one: http://ogp.pr.gov/PresupuestoMunicipal

* Thankfully for me, all the pdfs are stored in a standardized URL format, so
I can probably build a quick python script to download them all.
    * I can use [this list of municipalities](https://gist.github.com/rubenvarela/8475772)
        * (thanks [Ruben Varela](https://github.com/rubenvarela)!)
    * Going to use (this wget module)[https://pypi.org/project/wget] 
    to mimic the behavior of the bash terminal command wget 
    because that's what I'm accustomed to. `pip install wget` for those
    following along at home.
        * **UPDATE!** Forget wget. The requests module is good enough and 
        does exactly what I need it to.
    * We'll install the Unidecode module (`pip install Unidecode`() to get rid
    of those special spanish language characters `(e.g. á, ñ, ü, etc)` when we
    save the files. just in case.

    ### 20 minutes later
    * Ok, it's been twenty minutes making this python script and at this point
    I am aware it would have taken less time if I had just downloaded each file
    individually and patiently... maybe? I don't know.
        * I'll try to compensate for that by making this file dynamic enough
        to be used next year.
    
    ### 40 minutes after that
    * Okay, lesson learned. Programming is fun, but it's too fun. I have 
    to remember to make my work about the product, not about the code. 
    Taking too long on this script. Victim of a sunk cost fallacy here.
    
    ### And 10 minutes after *that*
    * So, at this point, I'm just continuing because it's fun to learn. But 
    yeah, I should have just downloaded them manually. **Currently stuck
    because the OGP website is blocking my requests. I have to mimic that
    I am coming from a browser**.

### And finally, after 1.5 hours of work and 30 minutes of downloads...
* We have the pdf files! (I'll make these public soon). It worked like a 
charm, not gonna lie. Certainly, downloading them manually would have been 
a lot faster, but-- and this is very important-- 

> **the reason I´m doing this project in the first place is to put my coding skills to practice.** 

So, yeah, for the sake of progress on my project, I can't take this long on 
side mini-projects every day, otherwise I'll never finish. **BUT!** I must 
say, I am very, very satisfied and feel very accomplished about the fact that 
I took an hour of my time today to learn how to build a basic web scraping 
script.

## Work Completed for the Day

* All municipal budgets have been downloaded.
* I built my first web scraping (is this really web scraping) script! [Check
it out by clicking here!](https://github.com/jicruz96/portfolio_project/tree/main/helper_scripts/get_municipal_budgets.py) It's quite the looker if you ask me...

## Intended Work for Today I Failed to Complete

* I have not cleaned up the data, and after downloading the bunch, **I am now 
very aware it will likely take several days to clean up all the data.**

* I did not build a basic Flask app. I shall do this tomorrow.

## Conclusions for the Day

* A side mini-project for learning's sake is good-- in moderation. Best not 
to repeat a day like this until I at least have an MVP.

* Sometimes, it's best just to keep your approaches simple

## Improvements for tomorrow

* Tomorrow, I will start writing these diaries in Spanish. I've chosen that 
**it matters more to me that my progress diary help inspire other Puerto Rican 
and Latin American coders than it matters to me that I show an employer my 
work flow.**

* I will also start including timestamps for all my posts on this diary. That 
way, I can demonstrably show how much time I'm working on things and how much
total time I've spent working on the project.

## Fun Facts

### The Peñuelas budget failed to download because the government uploaded the file with the name "Panuelas"

## Stats

### Time spent working: 2 hours
### Other stats
Significant lines of code written: 28
Total lines of code: 123
Total scripts: 1
