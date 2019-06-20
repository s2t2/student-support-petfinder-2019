# student-support-petfinder-2019

## Prerequisites

[Obtain an API Key for the Petfinder API](https://www.petfinder.com/developers/), and note its value (e.g. "abc123"). During the process, you may be asked to register for an account and also to create an application. When asked about the details of your app, you can specify any name and URL you'd like, for example you can use the URL to your GitHub project repo.

There is a one-time setup step which requires you to use the API KEY and the CLIENT SECRET from your developer account to also [obtain an access token](https://www.petfinder.com/developers/v2/docs/#getting-authenticated). To get the token, issue the following command from the Terminal, replacing the `{PETFINDER_API_KEY}` and `{PETFINDER_CLIENT_SECRET}` with your own creds (removing the curly braces)...

```sh
curl -d "grant_type=client_credentials&client_id={PETFINDER_API_KEY}&client_secret={PETFINDER_CLIENT_SECRET}" https://api.petfinder.com/v2/oauth2/token
```

This should get you an access token like:

```
{
    "token_type":"Bearer",
    "expires_in":3600,
    "access_token":"somelongstring-xyz"
}
```

Add a file called ".env" with the following contents to store that `access_token` value in  an environment variable called `PETFINDER_ACCESS_TOKEN` (replacing the example token with your real token):

    PETFINDER_ACCESS_TOKEN="somelongstring-xyz"

## Setup

Create a new virtual environment:

```sh
conda create -n pets-env-7 python=3.7
conda activate pets-env-7
```

Install Python package dependencies listed in the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

## Usage

Find pets:

```sh
python find_pets.py
```
