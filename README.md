# Healthy Food Recipe
This website aims to raise awareness of health and wellness by sharing recipes with an emphasis on good and safe ingredients.   
  
The target users are people looking for healthier living and recipes, especially those with health issues such as diabetes or allergies.  
One notable feature in this website is the various search options for recipe categories for the target peoples.  
And if the user create a new recipe that uses safe ingredients, sharing it is a great option for others to use too.  
  
We also provide a health article posting and sharing feature to encourage active communication, information sharing, and sometimes discussion in community groups.  
I hope that these activities will inspire all of us to make better food and lifestyle choices.
 

![Healthy Food Recipe](readme-img/amiresponsive.png "Healthy Food Recipe")
  
**[Heroku deployed site - Healthy Food Recipe](https://healthy-food-c44b0f8f09a5.herokuapp.com/ "Heroku deployed site - Healthy Food Recipe")**  

## UX DESIGN
### 1. Strategy Plane
#### Target users 
1.	Everyone who cares about food additives, health and simply enjoys cooking.
2.	Specially who already has some health issues, to give them easy search options.
3.  Young people who are about to start living independently, as well as their parents.
#### User value 
1.	Users can find a community which promotes everyone’s health through healthy recipe sharing, posts and discussions.
2.	Users can access and learn crucial information that could have an impact on their health and well-being by the community activities.
3.	Users can learn alternative cooking knowledge to avoid potentially dangerous food additives and unnaturally excessively processed food.
#### Difference from competitors and substitutions
1.  The "Healthy Food Recipe" is not just recipes, but has more emphasis on learning and communication.

### 2. Scope Plane 
#### First time visitor
*	As a user, I want to clearly understand what services are offered on this website.
*	As a user, I want to be able to easily navigate through to find contents.
*	As a user, I want the website to work on different devices and formats that I use.
*	As a user, I want the forms are simple and want some feedbacks about my actions.
*	As a user, I want to see articles that offer a variety of perspectives on health to increase my awareness and knowledge.
#### Returning and frequent visitor
*	As a user, I want to share my favorite recipes with easy and intuitive form inputs.
*   As a user, I want to share my thoughts by posting the articles.
*   As a user, I want to communicate with other members by the comment feature.
*   As a user, I want the useful search options to look for my needs.
*   As a user, I want to see the rating score by other members about recipes.
#### The website owner stories
*	As a site owner, I want to encourage people for joining the healthy eathing community.
*	As a site owner, I want to convey clearly who we are and our purpose, to give users a sense of trust and confidence.
*	As a site owner, I want the users to share their favorite recipes, thoughts and useful information about healthy eating.
*	As a site owner, I want to encourage people’s awareness about chemicals in our life.  
*	As a site owner, I want to inform and educate about European and national regulations on food additives.  
*	As a site owner, I want to provide inspiration for alternative cooking ideas by search options in the recipes.  
*	As a site owner, I want to convey clearly that the "Healthy Food Recipe" is not only about recipes.  

### 3. Structure Plane
*   The website should have a Navigation menu that is consistent across all pages.
*   The website should have breadcrumbs to help users feel a strong sense of place and also give access to previous pages when it expands to become a larger website.
*	The website should have hover interaction for links, abbreviation, and tooltips with additional information to enhance user experience.
*   The landing page should show what this site is offering intuitively.
*   Burger icon is commonly used on smaller screens, so using this convention suits users' expectations.
*   The link buttons, form buttons should be clearly visible and interactive. 

### 4. Skeleton Plane  

#### Structure diagram

![Database relationship diagram](readme-img/ux-structure-diagram.png "Database relationship diagram")

#### Database relationship diagram

![Database relationship diagram](readme-img/ux-db-diagram.jpg "Database relationship diagram")

#### Wireframes
This website was originally planned as part of a previous project, but midway through my development, my cohort facilitator Lewis advised for me that it would be better to make it a standalone project separate from the previous one to avoid confusion. Therefore, I have made some design & colour changes from this wireframes though I couldn't have time to create another wireframes. 

<details open>
<summary>For first time visitor - tablet and PC monitor</summary>

![For first time visitor - tablet and PC monitor](readme-img/wireframe/pc-top-noauth.webp "For first time visitor - tablet and PC monitor")
</details>
   
<details>
<summary>For authenticated user - tablet and PC monitor</summary>

![For authenticated user - tablet and PC monitor](readme-img/wireframe/pc-top.webp "For authenticated user - tablet and PC monitor")
</details>

<details>
<summary>Option search modal - tablet and PC monitor</summary>

![Option search modal - tablet and PC monitor](readme-img/wireframe/pc-filter.webp "Option search modal - tablet and PC monitor")
</details>


<details>
<summary>Recipe app Create page - tablet and PC monitor</summary>

![Recipe app Create page - tablet and PC monitor](readme-img/wireframe/pc-recipe-create.webp "Recipe app Create page - tablet and PC monitor")
</details>
<details>
<summary>Recipe app Read page - tablet and PC monitor</summary>

![Recipe app Read page - tablet and PC monitor](readme-img/wireframe/pc-recipe-read.webp "Recipe app Read page - tablet and PC monitor")
</details>
<details>
<summary>Post app Create page - tablet and PC monitor</summary>

![Post app Create page - tablet and PC monitor](readme-img/wireframe/pc-post-create.webp "Post app Create page - tablet and PC monitor")
</details>


<details>
<summary>Profile App ( Won't have - Future feature ) - tablet and PC monitor</summary>

![Profile App ( Won't have - Future feature )](readme-img/wireframe/pc-login.webp "Profile App ( Won't have - Future feature )")
</details>

### 5. Surface Plane

#### Colour
The color scheme that was originally planned has been changed to one that is more neutral and calming. [TECHNOLOGY - Coolor](#tech) 
  
![Colour scheme](readme-img/ux-colour.png "Colour scheme")

#### Typography

I selected "Poiret One" for the Logo from Google font API. It is attractive and has sharp features and it’s not too heavy.  
For the site's basic font, I was considering using "Quicksand" for the best readability, however our target users are young people and since it’s not a huge business website so a little bit unique font like "Josefin Sans" might appeal well to this unique community. [TECHNOLOGY USED - Google Fonts](#tech)  

* "Poiret One"  
* "Josefin Sans"  
![Typography  "Poiret One", "Josefin Sans"](readme-img/ux-fonts.gif "Typography Josefin Sans")


<a id="features"></a>

## EXISTING FEATURES  

### Authentication pages  

* Sign-up - AllAuth default settings and validations are applied   
![ Sign-up ](readme-img/feat-a-signup.png " Sign-up ")  

* Log-in  
![ Log-in ](readme-img/feat-a-login.png " Log-in ")  

* Log-out  
![ Log-out ](readme-img/feat-a-logout.png " Log-out ")  

### Top page - Home  
* Header and navigation - Unauthenticated user can see Sign-up and Log-in link  
![Header and navigation - Unauthenticated user](readme-img/feat-home-header2.png "Header and navigation - First time visiter")   
* Header and navigation - Authenticated user can see only Log-out link  
![Header and navigation - Authenticated user](readme-img/feat-home-header.png "Header and navigation - Authenticated user")   

* Welcome message - Unauthenticated user  
![ Welcome message - Unauthenticated user](readme-img/feat-home-intro2.png " Welcome message - First time visiter")   
*  Welcome message - Authenticated user can see their name on the message 
![ Welcome message - Authenticated user](readme-img/feat-home-intro.png " Welcome message - Authenticated user")  

* Home content - A list of Recipes in the main section and A list of Posts are in the article section. We have both search option buttons. Authenticated users can rate other user's recipes, and the average rating score is displayed on the recipe image. 
![ Home content - Recipes list](readme-img/feat-home-content.webp " Home content - Recipes list")   
Only Authenticated user can see the + button (Create recipe) beside the list title.   
![ Home content - Recipes list](readme-img/feat-home-contenta.png " Home content - Recipes list")  

* Footer  
![ Footer ](readme-img/feat-home-footer.png " Footer ")  

* Recipes search options modal - The main feature of this website is this optional search funstion that can filter by 8 categories and include words and avoid words search and more.  
![ Recipes search options modal ](readme-img/feat-recipesearch.png " Recipes search options modal ")  

* Posts search options modal -   
![ Posts search options modal ](readme-img/feat-postssearch.png " Posts search options modal ")  

### Recipe detail page
* Detail content - A selected recipes' details are displayed. Authenticated users can rate other user's recipes, and the averaged rating score will be displayed. When I was working on this page, I didn't know how to use CBV with POST request, so build with FBV.
![ Home content - Recipes list](readme-img/feat-detail-content.png " Home content - Recipes list")   
Only Authenticated user and the recipes' owner can see the "Edit" / "Delete" buttons   
![ Home content - Recipes list](readme-img/feat-detail-edit-delete-button.png " Home content - Recipes list")  
The star rating button and comment function, those functions are NOT displyed for unauthenticated users, they can find the links to Sign-up and Log-in   
![ Home content - Recipes list](readme-img/feat-detail-content-unauth.png " Home content - Recipes list")  


### Recipes CRUD pages

* Create recipe page - This page is constructed by CBV (CreateView) and `LoginRequiredMixin` is used for preventing unauthenticated users.
I choose summernote for user's rich text editor though I found a lot of nested tags and unnecessary tags, those were generated by automatically. For future project, I guess I should research more about better rich text editors. Here I'm using image resizing, setting to 400 px width.
![ Create recipe form page ](readme-img/feat-recipe-add.webp " Create recipe form page ")  

* Edit recipe form page - This Edit page has `LoginRequiredMixin, UserPassesTestMixin,` both mixin for preventing other users can access there pages.  
![ Edit recipe form page ](readme-img/feat-recipe-edit.png " Edit recipe form page ")   

* Delete recipe confirmation page - This Delete page is same as Edit page, using `LoginRequiredMixin, UserPassesTestMixin,` for security 
![ Delete recipe confirmation page ](readme-img/feat-recipe-delete.png " Delete recipe confirmation page ")   

### Posts list page  
* Lead sentense - Unauthenticated user  
![ Lead sentense - Unauthenticated user](readme-img/feat-posts-intro.webp " Lead sentense - First time visiter")    

* Lead sentense - Authenticated user can see their name on the message  
![ Lead sentense - Authenticated user](readme-img/feat-posts-intro2.webp " Lead sentense - Authenticated user")   

* Posts list Approved - These posts are not published until approved. Only authenticatted user can see the + button     
![ Posts list - Approved](readme-img/feat-posts-content1.png " Posts list - Approved")    
Only Authenticated user can see the + button (Create post) beside the list title.    
![ Posts list - Approved](readme-img/feat-posts-content1a.png " Posts list - Approved")    

* Posts list Waiting to be approved - Only Aithenticated and the post author can see thier unapproved posts here. The font colours are faded to imply not approved 
![ Posts list - Waiting to be approved](readme-img/feat-posts-content2.png " Posts list - Waiting to be approved")  

### Posts detail page
Post detail content - A selected post details are displayed. Authenticated users can comment on the other user's recipes, When I was working on this page, I didn't know how to use CBV with POST request, so build with FBV.
* Create post form page  
![ Create post form page ](readme-img/feat-posts-add.png " Create post form page ")  

### Posts CRUD pages

* Create post form page  
![ Create post form page ](readme-img/feat-posts-add.png " Create post form page ")  

* Edit post form page  
![ Edit post form page ](readme-img/feat-posts-edit.png " Edit post form page ")   

* Delete post confirmation page  
![ Delete post confirmation page ](readme-img/feat-posts-delete.png " Delete post confirmation page ")  

### Other parts

* Star rating - Only authenticated users can rate other members recipes. Each ratings are averaged using the aggregate() clouse.  In recipe detail page, left bottom part of the page 
![ Star rating ](readme-img/feat-starrating.webp " Star rating ")  

* Message  
![ Message ](readme-img/feat-message.png " Message ")  

* Breadcrumb  
![ Breadcrumb ](readme-img/feat-breadcrumb.png " Breadcrumb ")  
This breadcrumb is for a Post's single page's edit page.   
The hierarchy is in this order:　Top page > List Page > Single post page > Edit 　
The recipe's app doesn't have it's own list page as the Home (Top) page is working as a recipe's list page.

## FUTURE FEATURES

Any open issues can be tracked [here](https://github.com/users/AtsukoCoffey/projects/6). These are the "Won't Have" for this project that will not be included in this projct submission. These may be revisited and added in the future. I stopped development at this point because the website already had enough functionality for an MVP.
<a id="tech"></a>

## TECHNOLOGY USED
* HTML, CSS used for structure my webpages and layout   
* JavaScript used for a part of the comment functionality. Programming language.
* Python used for all functionality. Programming language.
* Gitpod used as a cloud-based IDE for development.
* Git used for recording changes. A version control system.
* GitHub Used for our project's platformused for secure online code storage.
* Heroku Used for our project's platform. The deployed site.

* Font Awesome used for all the icons in this project  
* Google Fonts used for all the fonts used in this project and to compare potential fonts.  

* [tinipng](https://tinypng.com/ "tinipng") - Smart WebP, PNG and JPEG Compression for Faster Websites
* Am I Responsive? used for creating responsivity example image
* [favicon.io](https://favicon.io/favicon-generator/ "favicon.io") used for creating an original favicon icon
* [coolors](https://coolors.co/232018-4b483d-758761-bfe077-f1eddb "coolors") used for the formating of colour scheme

<a id="testing"></a>

# TESTING
I performed most of the testing myself and had some support from family members with different mobile devices.

## TESTING
For testing I created `README-TEST.md` file
[Tests- README-TEST](/README-TEST.md "Tests- README-TEST")

## BUGS
I had a lot of bugs and difficulties through the developement procedure. However can't write everything. 
The bugs that I mention here are something I felt clicked. 

### Pagination for the query data  
When I was working at the option search, the query result recipes displayed correctly, however pagiination links are resetting the
query list and I could never see the 2nd page with that same query data. The view was made by CBV and the pagination is default setting in the view. I couldn't find anything Django docs. After looking for around 2 days I finally asked to the tutor support.   
The tutor Rebecca found the article about pagination with FBV view pages but I explained it did't work and my view is CBV. Then she quickly found the "ListView" doesn't take the parameter from `GET request` so she write the this code below for me. - [Solution](#pagination)

This `copy()` method returns a copy of the page_obj, then `pop()` method removed the `page` part of the parameter, so it's duplicated in the GET request. The `urlencode()` function will encode the GET parameters to format it for the URL. Then, in the template, add the `query_string` after the pagination tag. `href="?page={{ page_obj.previous_page_number }}&{{ query_string }}"` 
I could never solve this issue by my self, great thank you for tutor Rebecca. <a id="pagination"></a>

- Solution 
```
def get_context_data(self, **kwargs):
context = super().get_context_data(**kwargs)

# Add GET parameters to context
query_params = self.request.GET.copy()
if 'page' in query_params:
    query_params.pop('page') 
context['query_string'] = query_params.urlencode()
```

### `slug=slug`   
When I was working on `get_context_data` I was straggling to set the kwargs "comments" ( all the relavant comments to the specific post) into  `get_context_data` `kwargs`, in PostDetail CBV view. I wanted to write something like this familier way "slug=slug" but slug was not defind inside the function. I was looking for how to get the global variable into the function only but those were not even close. After looking everywhere I found this article, he’s writing like `Project.objects.get(slug=self.kwargs['slug'])` Then finally realised that inside `get_context_data` I could access the kwargs it self. I thought that must be the one that I wanted to do it. [forun.djangoproject](https://forum.djangoproject.com/t/passing-slug-to-createview/4287/12)
![screenshot](readme-img/bug-code-self.kwargs-slug.png)

- Solution -  And it worked. `slug=self.kwargs["slug"]`


### Another 500 error for sign up form
This bug was found at the middle of the end-point reveiw. I had different 500 server error that took a long time to solve it so I broke out into my cold sweat. However the mentor gave me a great advice that this error is not coming from the logic error. So possibly from template or soemthing similar things. After the meeting, the DEBUG explained the issue was caused from the AllAuth's password validation. Then now I remember that I just did all the PEP8 linting and even settings.py.    

- Solution -  Long lines generated by the system can be reverted and left as it was before.

**There were more than three bug reports, but I am writing only the ones that I clicked on.**

### Unfixed Bugs

<!-- There are no remaining bugs that I am aware of. -->

## DEPLOYMENT
### Preparation
#### Django
First we are using Django, so install Django:   
1. Creating a Django project `django-admin startproject my_project .`
2. Add `ALLOWED_HOSTS` to the settings.py 
3. For security, we always hide sensitive information, so the `SECRET_KEY` and any API keys we use will not be where accessible place.
Create `env` file and store `SECRET_KEY`, API key, `DATABASE_URL`, also for automatically debug on/off environmane add DEBUG environment variable `DEVELOPMENT` too.
4. Add `env` file name to gitignore list
5. Create Django app `python3 manage.py startapp <app_name>`
6. Add the app into the `INSTALLED_APPS ` settings.py

#### Connect Database
1. set the environment variable. `os.environ.setdefault("DATABASE_URL", "......")`
2. install two packages `pip3 install dj-database-url~=0.5 psycopg2~=2.9` `pip3 freeze --local > requirements.txt`
3. Connect settings.py to the env.py - import `dj_database_url ` into the settings.py and `if` statement  
`if os.path.isfile('env.py'): import env` or you can write like this too `if os.path.exists('env.py'): import env`
4. Change the already selected local sqlite3 database connection into CI database in settings.py  
`DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL")),
}`  
5. Create database table `python3 manage.py migrate`
6. Superuser can be created using the `python3 manage.py createsuperuser`

#### Install modules - Crispy Forms and crispy-bootstrap
1. install `pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7`
2. Add it to  `INSTALLED_APPS`
3. Add `CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"` and `CRISPY_TEMPLATE_PACK = "bootstrap5"` into the settings.py
4. Add 
``` 
TEMPLATES = 'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field'         ] 
```

#### Install modules - Django AllAuth
1. `pip3 install django-allauth~=0.57.0`
2. Add it to  `INSTALLED_APPS`
3. Add `SITE_ID = 1 `, `LOGIN_REDIRECT_URL = '/' `, `LOGOUT_REDIRECT_URL = '/'`
4. Append `'allauth.account.middleware.AccountMiddleware',` into `MIDDLEWARE `
5. Add `ACCOUNT_EMAIL_VERIFICATION = 'none'` below the `AUTH_PASSWORD_VALIDATORS`
6. Save all the file and migrate `python3 manage.py migrate`
7. Add `urlpatterns` in project's urls `path("accounts/", include("allauth.urls")),`
8. Collect Allauth template `pip3 show django-allauth` copy into templates folder `cp -r <Location>/allauth/templates/* ./templates/`

#### Install modules - Cloudinary
1. install `pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15`
2. Set API key and URL into the `env.py`
3. Add `'cloudinary_storage'` and `'cloudinary'` into `INSTALLED_APPS` 

#### Install modules - summernote
1. Install `pip3 install django-summernote~=0.8.20.0`
2. Add it to  `INSTALLED_APPS`
3. For admin page, add `path('summernote/', include('django_summernote.urls')),` into the project's urls

**After all the installation finished record this to `pip3 freeze --local > requirements.txt`**

### Other settings
#### CSRF tokens Setting
set `CSRF_TRUSTED_ORIGINS` in settings.py ( CSRF stands for Cross-Site Request Forgery)
```Under the DATABASES
CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]
```
#### The base template
1. createa `TEMPLATES_DIR` constant to build a path for our subdirectory 'templates' in settings.py  
`TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`
2. `TEMPLATES ` add `TEMPLATES_DIR` constant to the list of `DIR` - `'DIRS': [TEMPLATES_DIR],`
3. Create `templates` directory at root top-level and `base.html `
4. Create `index.html` to the existing app level template (app/template/app/index.html)

#### Path for static
1. Link to files in the static directory from a template, add `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]`

### Deploy setting
1. install `gunicorn` for production-ready server
`pip3 install gunicorn~=20.1`
2. Create a file named Procfile (no file extension)  
Declare `web: gunicorn my_project.wsgi` 
3. Install whitenoise   
`pip3 install whitenoise~=5.3.0` and wire up to `MIDDLEWARE` in settings.py  
`'whitenoise.middleware.WhiteNoiseMiddleware',` Not forget `pip3 freeze --local > requirements.txt`
4. Add `STATIC_ROOT` path `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`
5. Run `collectstatic` command `python3 manage.py collectstatic`
6. Check the python version `python3 -V`
7. Look up the supported runtimes from the Heroku web site and copy the runtime closest to the one used in your IDE.
8. Add a runtime.txt file to your app's root directory
9. Add the Python version you copied from the list of supported runtimes to runtime.txt file

### Heroku
0. For prevent Heroku from uploading static files, click on the Settings tab and reveal the config vars, `DISABLE_COLLECTSTATIC` and value of `1`
 click "Add"
#### Create Heroku app
1. Click "New" in the top-right corner of drop down list in Dashboard page, and select "Create new app"
2. Decide the App name (it must be only lowercase letters, numbers and dashes), and then choose a region "Europe"
3. Click the "Settings" to go Setting page
4. Goes to "Config Vars". We are using confidential credentials, so copy the contents of the credentials in json file and paste into the Config Variables. Also set the value of KEY to `"PORT"`, and the value to `"8000"` then select Add
5. Underneath `"Config Vars"` there is `"Buildpacks"`. Add the buildpack (The order of the buildpacks is important)

#### Manual deploy and Automatic deploys  
1. Click on the Deploy tab, click connect to "GitHub" 
2. Click on "Deploy Branch" to start a manual deployment of the main branch
3. Click on "Automatic deploys" and "Manual deploy" so that it deploys automatically evertime GitHub pushing

## Forking  
>A fork is a new repository that shares code and visibility settings with the original “upstream” repository. Forks are often used to iterate on ideas or changes before they are proposed back to the upstream repository, such as in open source projects or when a user does not have write access to the upstream repository. [Quote from GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)  

We can make a copy of someone's original repository on our GitHub account, so we can make changes without affecting the original repository.  

1. Locate the objective repository using my Github account (I can’t fork my own repository),
top-right of the Repository (not top of page) just right hand side of the repository title, click the "Fork" Button.  
2. Input available new repository name and click “Create fork”. Now there is a copy of the original repository in my own GitHub account.

## CREDIT

### CREDITS - Code references

* Function based views and their class based view equivalents in Django   
In my development steps required me to understand the difference between using these two different views. This good article helped me to understand a lot.
 [Function based views and their class based view equivalents in Django](https://cpadiernos.github.io/function-based-views-and-their-class-based-view-equivalents-in-django-part-one.html "Function based views and their class based view equivalents in Django")


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

### CREDITS - Content References
* [BBC Foods](https://www.bbc.co.uk/food/recipes/halloumi_salad_19294 "BBC Foods") I borrowed all the recipes from this BBC Food recipe website   
* [Refind oil article](https://latourangelle.com/blogs/general/refined-vs-unrefined-oils?srsltid=AfmBOoqtQU2k4U2or4hnRSGHYO3Ce8dc4TT4DziozTaKUYa0mq6G554O "Refind oil article") 


https://www.reddit.com/



### CREDITS - Imagery
Egg - Pexels - Antoni Shkraba 
Photo by Kampus Production: https://www.pexels.com/photo/a-woman-deciding-on-what-to-buy-8422719/

Image by <a href="https://pixabay.com/users/lincerta-689260/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1492258">Hrayr Movsisyan</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1492258">Pixabay</a>


### CREDITS - Editing And Proofreading


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


### ACKNOWLEDGEMENTS
I would like to give great thanks to my mentor Gareth Mc Girr and cover session's mentor David Bowers for their exellent advice and support.
Also my cohort facilitator Lewis Dillon for all the support and assistance.

And great thanks to my family Sean Coffey and Dean Coffey for all the support.