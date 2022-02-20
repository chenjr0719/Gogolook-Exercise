# Contribution Guide

Here is some helpful information to help you contribute to this project.

## Project structure

### Models

The models define the ORM model and the schema for an entity like `Task`. We are using the `SQLAlchemy` as the ORM framework to abstract the operation with DB. All the schemas are built on top of `Pydantic` so that we can validate the input is correct or not.

### Services

In this project, we dedicated the business logic to services. Currently, we only have `CRUDService` and `TaskCRUDService`. They are responsible for handling DB object essential CRUD operation and using the schema to verify the input data.

### API Server

The apiserver responds to the serving HTTP interface to consume the services. Currently, we only have the implementation of the Task service.

To ensure ease of extensionality, we use the `Blueprint` from `Flask` framework to build the Task API. With this approach, we can decouple the dependencies between the `Task` API and the apiserver.

### Migrations

We are using `alembic` package to help us manage the DB migrations. You can find all the migration records under [gogolook/db/migrations/versions](gogolook/db/migrations/versions).

After modifying anything in the ORM models, we can use the script to generate the migration records automatically:

```shell
./scripts/make_migration.sh
```

## Test

You can test the service and API server with `tox` or `pytest`.

To test with `tox`, please ensure you have installed Python from 3.7 ~ 3.10 on your system. And, you can run the tests with:

```shell
pip install tox
tox
```

If you only install one version of Python, you can run the tests with `pytest` with:

```shell
pip install .[test]
pytest
```

After the tests are done, you can find the test report and coverage report under [test_reports](test_reports).

## CI

We have two CI in this project. The one is tested with `tox` and uses `sqlite` as the DB. Another is tested with the `docker-compose` to make sure the whole system is stable. You can check the content of [workflows](.github/workflows) to get more insight.