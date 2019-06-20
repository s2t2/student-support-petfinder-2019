# Credits, Notes, and Reference

  + https://www.petfinder.com/developers/api-docs (OLD)
  + https://www.petfinder.com/developers/api-key (OLD)

> Attention developers! We are hard at work improving our API and are excited to unveil a new version for public use. Please note that the Petfinder API v1.0 will be deprecated in January 2020. If you do not currently use the Petfinder API, or you are ready to transition from v1.0 to v2.0, please go here to create a new account. If you are currently using version 1.0 of the API, please contact us so we can help you move to our new API!

  + https://www.petfinder.com/developers/ (NEW)
  + https://www.petfinder.com/user/developer-settings/
  + https://www.petfinder.com/developers/v2/docs/#getting-authenticated
  + https://www.petfinder.com/developers/v2/docs/#get-animals
  + https://github.com/aschleg/petpy
  + https://petpy.readthedocs.io/en/latest/


<hr>

Trying from scratch...

First step is to [get an access token](https://www.petfinder.com/developers/v2/docs/#getting-authenticated), issuing this command from the Terminal and replacing the `{PETFINDER_API_KEY}` and `{PETFINDER_CLIENT_SECRET}` with your own creds (remove the curly braces)...

```sh
curl -d "grant_type=client_credentials&client_id={PETFINDER_API_KEY}&client_secret={PETFINDER_CLIENT_SECRET}" https://api.petfinder.com/v2/oauth2/token
```

This will get you an access token like:

```
{
    "token_type":"Bearer",
    "expires_in":3600,
    "access_token":"somelongstring-xyz"
}
```

Store the access token in an environment variable called `PETFINDER_ACCESS_TOKEN`.

This kind of curl command does work (replacing with your actual token, without curly braces):

```sh
curl -H "Authorization: Bearer {PETFINDER_ACCESS_TOKEN}" GET https://api.petfinder.com/v2/animals
```

Implementing an equivalent request in python now...

```sh
python roll_my_own.py
```
