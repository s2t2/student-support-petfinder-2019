# student-support-petfinder-2019

## Notes and Resources

  + https://www.petfinder.com/developers/api-docs (OLD)
  + https://www.petfinder.com/developers/api-key (OLD)

> Attention developers! We are hard at work improving our API and are excited to unveil a new version for public use. Please note that the Petfinder API v1.0 will be deprecated in January 2020. If you do not currently use the Petfinder API, or you are ready to transition from v1.0 to v2.0, please go here to create a new account. If you are currently using version 1.0 of the API, please contact us so we can help you move to our new API!

  + https://www.petfinder.com/developers/ (NEW)
  + https://www.petfinder.com/user/developer-settings/
  + https://www.petfinder.com/developers/v2/docs/#get-animals
  + https://github.com/aschleg/petpy
  + https://petpy.readthedocs.io/en/latest/




## Prerequisites

[Obtain an API Key for the Petfinder API](https://www.petfinder.com/developers/), and note its value (e.g. "abc123"). During the process, you may be asked to register for an account and also to create an application. When asked about the details of your app, you can specify any name and URL you'd like, for example you can use the URL to your GitHub project repo.

Add a file called ".env" with the following contents (except use your own API Key):

    PETFINDER_API_KEY="abc123"
    PETFINDER_CLIENT_SECRET="def456"

## Setup

Create a new virtual environment:

```sh
conda create -n pets-env-6 python=3.6
conda activate pets-env-6
```

Install package dependencies listed in the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

## Usage

Run the script:

```sh
python find_pets.py
#> json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

Need to figure out how to resolve this error.
