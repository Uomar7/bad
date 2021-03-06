# HEALTH-E-NET

A web application to scan handwritten forms and extract the required information.

---

## Contributors

* [Umar Ali Ngare](uomarearlie7@gmail.com)

* [Maurine Sinami](maurine.sinami@gmail.com)

* [Kenneth Maina](kenmaina2022@gmail.com)

* [Klaus Orioki](oriokiklaus@gmail.com)

* [Anthony Maina](antonynganga05@gmail.com)

---

## BDD

| Input | Behaviour| Output |
|-|:-:|-|
|fill in login credentials| Authentication takes place.| Routed to the landing page.|
|Click on the profile to view profile page.| Routed to the profile page to view user details.| Can update the user instance and even view all the forms in her record. |
| Click statics | Routed to the statistics page. | View statistics generated based on the data collected.|
| Click on add forms| import an image of the form / scan the phone via your phone.|App will save the scanned form and extract information based on the filled fields.|

---

### Installing

* Clone the project from github `git clone <https://github.com/Uomar7/health-e-net.git> .

* Extract the folder into your preffered location.

* Open terminal and create a virtual environment. `python -m venv --without-pip virtual` .

* Activate virtual environment. `source virtual/bin/activate`.

* Install python pip. `curl https://bootstrap.pypa.io/get-pip.py | python`

* Install the requirements via `pip install -r requirements`

* Create an a database with name 'pro'

* Migrate the changes in the models;

* Finally run server to confirm running.

## Built With

* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* Angular Web Framework
* Bootstrap 4

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

---

## Acknowledgments

* MC17 TMs
