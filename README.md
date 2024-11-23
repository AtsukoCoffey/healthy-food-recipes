<script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.0/dist/mermaid.min.js"></script>


# UX DESIGN

## 1. Strategy Plane
### Target users 
1.	Everyone who cares about food additives, health and simply enjoys cooking.
2.	Specially who already has some health issues, to give them easy search options.
3.  Young people who are about to start living independently, as well as their parents.
### User value 
1.	Users can find a community which promotes everyone’s health through healthy recipe sharing, posts and discussions.
2.	Users can access and learn crucial information that could have an impact on their health and well-being by the community activities.
3.	Users can learn alternative cooking knowledge to avoid potentially dangerous food additives and unnaturally excessively processed food.
### Difference from competitors and substitutions
1.  The "Healthy Food Club" is not just recipes, but has more emphasis on learning and communication.

## 2. Scope Plane 
### First time visitor
*	As a user, I want to clearly understand what services are offered on this website.
*	As a user, I want to be able to easily navigate through to find contents.
*	As a user, I want the website to work on different devices and formats that I use.
*	As a user, I want the forms are simple and want some feedbacks about my actions.
*	As a user, I want to see articles that offer a variety of perspectives on health to increase my awareness and knowledge.
### Returning and frequent visitor
*	As a user, I want to share my favorite recipes with easy and intuitive form inputs.
* As a user, I want to share my thoughts by posting the articles.
* As a user, I want to communicate with other members by the comment feature.
* As a user, I want the useful search options to look for my needs.
* As a user, I want to see the rating score by other members about recipes.
### The website owner stories
*	As a site owner, I want to encourage people for joining the healthy eathing community.
*	As a site owner, I want to convey clearly who we are and our purpose, to give users a sense of trust and confidence.
*	As a site owner, I want the users to share their favorite recipes, thoughts and useful information about healthy eating.
*	As a site owner, I want to encourage people’s awareness about chemicals in our life.  
*	As a site owner, I want to inform and educate about European and national regulations on food additives.  
*	As a site owner, I want to provide inspiration for alternative cooking ideas by search options in the recipes.  
*	As a site owner, I want to convey clearly that the "Healthy Food Club" is not just about recipes and cooking.  

## 3. Structure Plane
* The website should have a Navigation menu that is consistent across all pages.
* The website should have a fixed footer to access anytime to see this site's SNS.
* The website should have breadcrumbs to help users feel a strong sense of place and also give access to previous pages when it expands to become a larger website.
*	The website should have hover interaction for links, abbreviation, and tooltips with additional information to enhance user experience.
* The landing page should show what this site is offering intuitively.
* Burger icon is commonly used on smaller screens, so using this convention suits users' expectations.
*	The Sign-up page submit button should be clearly visible and interactive when the mouse hovers over it. 

## 4. Skeleton Plane
### Structure diagram

![Database relationship diagram](readme-img/ux-structure-diagram.png "Database relationship diagram")

<details open>
<summary>Database relationship diagram</summary>

![Database relationship diagram](readme-img/ux-db-diagram.jpg "Database relationship diagram")
</details>  

For the mobile screen wireframe, I simply lined up important and necessary information under the flow of UX design strategy as I thought there wasn't much excess spaces.  
<details>
<summary>Mobile - 320px - Wireframe</summary>

<!-- ![Home page mobile Wireframe](readme-img/wireframe/ "Home page mobile Wireframe") -->
</details>  

For PC monitor wireframe, for first time visitor.   
<details open>
<summary>Tablet - 768px - and PC - 1440px - Wireframes</summary>

![Home page tablet and PC Wireframe](readme-img/wireframe/pc-top-noauth.webp "Home page tablet and PC Wireframe")
</details>

For PC monitor wireframe, for authenticated user.   
<details>
<summary>Tablet - 768px - and PC - 1440px - Wireframes</summary>

![Home page tablet and PC Wireframe](readme-img/wireframe/pc-top.webp "Home page tablet and PC Wireframe")
</details>

## 5. Surface Plane

### Colour
At the planning stage, I chose this colour scheme, which has a healthy, lively, clear and optimistic feeling, from the Adobe colour website. [CREDITS Content References - Adobe Color API](#credits-content) 
  
<!-- ![Colour scheme](readme-img/colour-scheme1.png "Colour scheme") -->

However, using only these colors couldn’t provide enough contrast, so I adjusted the color scheme as below.  
  
<!-- ![Colour scheme 2](readme-img/colour-scheme2.png "Colour scheme 2") -->


### Typography

I selected "Poiret One" for the “Healthy Food Club” Logo from Google font API. It is attractive and has sharp features and it’s not too heavy.  
For the site's basic font, I was considering using "Quicksand" for the best readability, however our target users are young people and since it’s not a huge business website so a little bit unique font like "Josefin Sans" might appeal well to this unique community. [TECHNOLOGY USED - Google Fonts](#tech)  

* "Poiret One"  
<!-- ![Typography Poiret One](readme-img/typo-poiret1.png "Typography Poiret One")   -->

* "Josefin Sans"  
<!-- ![Typography Josefin Sans](readme-img/typo-josefinsans.png "Typography Josefin Sans") -->


<a id="features"></a>

# EXISTING FEATURES

## The Header And Navigation Bar


# Future features

Any open issues can be tracked [here](). These are the "Won't Have's" for this project that, for a variety of reasons, will not be included in this projct submission. These may be revisited and added in the future.

# Bugs


- Bug title.

    ![screenshot](readme-img/)

    - To fix this, ....

## Unfixed Bugs

There are no remaining bugs that I am aware of.

# CREDIT

## Code References 
* Bootstrap Navbar toggle screen beakpoint `navbar-expand`  
Adjustment the size that screen's breakpoint. Default was `-lg` change into `-md`  
 ![Bootstrap Navbar expand](readme-img/credit-code-css-navbar-expand.png "Bootstrap Navbar expand")  

 * `request.resolver_match`  
 request.resolver_match to check if the current URL matches a specific pattern or path.  
 ![Medium-How to Get the Current URL within a Django Template](readme-img/credit-code-request.resolver_match.png "Medium-How to Get the Current URL within a Django Template")  
 [Medium-How to Get the Current URL within a Django Template](https://medium.com/@iamalisaleh/how-to-get-the-current-url-within-a-django-template-8270b977f280 "Medium-How to Get the Current URL within a Django Template")

* Medium - Django: Implementing Star Rating  
How to set the star rating system  
[Medium-How to Implementing Star Rating](https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c "Medium-How to Implementing Star Rating")  

* `DEFAULT_FILE_STORAGE`  
In Django media files are storing in the media directory in default, using `DEFAULT_FILE_STORAGE` we can store the image files into the outside server like Cloudinary.  
[`DEFAULT_FILE_STORAGE`](https://docs.djangoproject.com/en/4.2/ref/settings/#default-file-storage "DEFAULT_FILE_STORAGE")  

* Resizing images  
Using Django resized and pillow. Resizing images for user to upload their images into specified size and quality.    
['Resizing images'](https://www.codu.co/articles/resizing-images-and-converting-formats-in-django-1rj9kdho "Resizing images")  

* Integrating Summernote Rich Text Editor  
I was planning to use Django RichTextField but changed my mind to summernote, these are the really good sites I referenced.  
[django-summernote](https://summernote.org/getting-started/#run-summernote "django-summernote")  
[django-summernote GitHub page](https://github.com/lqez/django-summernote "django-summernote GitHub page")  
[Integrating Summernote Rich Text Editor](https://medium.com/@vineetaneekhra4/integrating-summernote-rich-text-editor-into-your-django-project-fa8b3f331c97 "Integrating Summernote Rich Text Editor")   


* `slug` field   
I wanted to fill the slug field automatically with title value. These links are some references.  
[Add default to slug field in model django](https://pleypot.com/blog/add-default-to-slug-field-in-model-django/ "Add default to slug field in model django")  
[How to generate slug based on title](https://stackoverflow.com/questions/64374947/how-to-generate-slug-based-on-title-of-post-in-django "How to generate slug based on title")   
![How to generate slug based on title](readme-img/credit-code-slug-generate-from-title.png "How to generate slug based on titl")  


* How to Get the Current URL within a Django Template  
[How to Get the Current URL within a Django Template](https://medium.com/@iamalisaleh/how-to-get-the-current-url-within-a-django-template-8270b977f280 "How to Get the Current URL within a Django Template")  

* Securing Django Views from Unauthorized Access | by Daisy McGirr  
`UserPassesTestMixin` To secure the data from the view as well by doing checks before content to load.  
`LoginRequiredMixin` If non-authenticated users send request, that will be redirect to login page.  
[Securing Django Views](https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to_ "Securing Django Views")

* Success message from class based view  
As a part of the relevant responses to user actions for UX design, I wanted to implement the `message`. I learned the `Django contrib messages` in LMS learning but class based views has a different one called `SuccessMessageMixin`.
[Success message from class based view](readme-img/credit-code-message-mixin.png "Success message from class based view")  

* Setting `success_url` in the UpdateView   
After the editing the recipe, I wanted to go back to the detail's page, so that user don't need to click the recipe to check the updated details.
I found the function `get_success_url` and using this `reverse` 
[Setting `success_url` in the UpdateView](readme-img/credit-code-setting-successurl.png "Setting `success_url` in the UpdateView")



*
[]( "")

* `With`  
Using `with`, we can hold the complex variables under the simple names.  
[Using `with`](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#with "Using `with`")  
![Using `with`](readme-img/credit-code-django-with.png "Using `with`") 

* using `aggregation`   
[Django-Aggregation](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/ "Django-Aggregation")   

* django-crispy-forms Layouts  
This website is showing how to layout the crispy forms  
[django-crispy-forms Layouts](https://django-crispy-forms.readthedocs.io/en/latest/layouts.html "django-crispy-forms Layouts")   
https://django-crispy-forms.readthedocs.io/en/latest/layouts.html  

* Encoding format   
I think this is really important information for security.  
![Encoding format](readme-img/credit-code-encoding-format1.png "Encoding format")  
![Encoding format2](readme-img/credit-code-encoding-format2.png "Encoding format2")  

Credit referenced projects
* Django Recipe Sharing | Dee Mc - Youtube tutorial
[Django Recipe Sharing | Dee Mc](https://www.youtube.com/watch?v=dCvkAVN5uas&list=PLXuTq6OsqZjYSa-lrjd5wMGl23zpnhvln "Django Recipe Sharing | Dee Mc")

* NicoleJackson89 | pp4-recipe-share
[NicoleJackson89 | pp4-recipe-share](https://github.com/NicoleJackson89/pp4-recipe-share "NicoleJackson89 | pp4-recipe-share")


Technology
* Mermaid
[JavaScript-based diagramming and charting tool](https://github.com/mermaid-js/mermaid/blob/develop/README.md "JavaScript-based diagramming and charting tool")

