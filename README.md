# odm-taxonomy

[![Build Status](https://travis-ci.org/OpenDevelopmentMekong/odm-taxonomy.svg?branch=master)](https://travis-ci.org/OpenDevelopmentMekong/odm-taxonomy)

Repository with definition for the taxonomic structure used across ODM components

See https://wiki.opendevelopmentmekong.net/internal:updating_the_system_s_taxonomy

### Testing

Install tests dependencies

```
pip install -r dev-requirements
```

Run tests

Run ```nosetests tests/```

### Continuous deployment

Everytime code is pushed to the repository, travis will run the tests available on **/tests**. In case the code has been pushed to **master** branch and tests pass, the **_ci/deploy.sh** script will be called for deploying code in CKAN's DEV instance. Analog to this, and when code from **master** branch has been **tagged as release**, travis will deploy to CKAN's PROD instance automatically
