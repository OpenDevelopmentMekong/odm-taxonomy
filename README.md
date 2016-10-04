# odm-taxonomy

[![Build Status](https://travis-ci.org/OpenDevelopmentMekong/odm-taxonomy.svg?branch=master)](https://travis-ci.org/OpenDevelopmentMekong/odm-taxonomy)

Repository with definition for the taxonomic structure used across ODM components

See https://wiki.opendevelopmentmekong.net/internal:updating_the_system_s_taxonomy

# Testing

Tests are found on /tests and can be run with ```nosetest```

# Continuous deployment

Everytime code is pushed to the repository, travis will run the tests available on **/tests**. In case the code has been pushed to **master** branch and tests pass, the **_ci/deploy.sh** script will be called for deploying code in CKAN's DEV instance. Analog to this, and when code from **master** branch has been **tagged as release**, travis will deploy to CKAN's PROD instance automatically.

For the automatic deployment, the scripts on **_ci/** are responsible of downloading the odm-automation repository, decrypting the **odm_tech_rsa.enc** private key file ( encrypted using Travis-ci encryption mechanism) and triggering deployment in either DEV or PROD environment.
