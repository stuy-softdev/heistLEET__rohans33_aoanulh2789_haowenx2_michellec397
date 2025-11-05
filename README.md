# Rohanspace by HeistLEET
Rohan Sen - PM <br>
Haowen Xiao - Frontend/Design <br>
Michelle Chen - Backend <br>
Aoanul Hoque - Bug fixing, feature testing <br>

# Description of Website/App:
Rohanspace allows you to create an account to create blogs and publish them for other users. Users will be able to search and edit past blogs. All that is needed is an email and password of your choice, and you can sign up to Rohanspace for free. Rohanspace uses Flask to run our website along with SQL to store blogs and account information. Guests are able to create accounts and login with our `login.html`. Similarly, they are able to logout with the `logout.html`. Our `home.html` allows users to scroll through other user's blogs and search for blogs. All blog data is stored in our SQL database, allowing users to view and edit past blogs anytime. Any account information like usernames, password, and profile images are also stored in our SQL database and will be displayed to others on the author's blog. 

# Install Guide:
1) git clone the ssh link (`git@github.com:stuy-softdev/heistLEET__rohans33_aoanulh2789_haowenx2_michellec397.git`) onto local computer (reccomendeded to clone it into your desktop folder for easy access)
2) Navigate into Git Repo installed using `cd heistLEET__rohans33_aoanulh2789_haowenx2_michellec397.git`. If installed into desktop, downloads, or anything else. Do `cd (input whatever directory you installed our repo into (e.g desktop, downloads, etc)) Then navigate into `app` directory via `cd app`
3) Create a virtual enviornment using command: `python3 -m venv venv`
4) Activate the virtual enviornment by doing: `cd venv/bin`. Then `source activate`
5) Navigate back to home repo via `cd ..` (3x) to install dependencies 
6) Install the dependencies using command: `pip install -r requirements.txt`


# Launch Codes:
## First Option:
- Open up the `app` directory into the Python IDE of your choice (Make sure the IDE can run files)
- Navigate into `__init__.py` and run the file (usually a green play button).

## Second Option:
- Open up terminal and route to `app` using command: `cd heistLEET__rohans33_aoanulh2789_haowenx2_michellec397.git/app` or `cd (Directory you installed our repo into)/heistLEET__rohans33_aoanulh2789_haowenx2_michellec397.git/app` 
- Run command: `python3 __init__.py` or `python __init__.py`

