# copyroles

Utilities for copying alma roles and users

## Required ENV
```shell
PROD_ALMA_API_KEY=# an Alma API key for the Alma `production` environemnt with `user` read/write permissions and `conf` read permissions
SANDBOX_ALMA_API_KEY=# an Alma API key for the Alma `sandbox` environemnt with `user` read/write permissions and `conf` read permissions
```
## Optional ENV
```shell
ALMA_API_ENDPOINT=# The base URL for the Alma API. Default is https://api-na.hosted.exlibrisgroup.com/almaws/v1/
```
## To run

- Create a virtual environment and install dependencies
    
    `make install`

- Run the `copy` command from the virtual environment, passing in the required parameters 
    - copy-roles: 
        - copy alma rules from one user to another in the same alma environment
        - the roles of the target user will be completely overwritten

         `pipenv run copy copy-roles [primary_id_of_source_user] [primary_id_of_target_user] --environment [prod|sandbox]`
    - copy-user: 
        - Copy a user from Production to Sandbox

         `pipenv run copy copy-user [primary_id_of_source_user]`
    
 