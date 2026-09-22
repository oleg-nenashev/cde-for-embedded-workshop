# 06 - CI Integrations

This section focuses on how the same devcontainer-based environment can be reused in continuous integration pipelines.

## Goals

- Understand the benefits of using the same environment locally and in CI
- Learn how containerized workflows support repeatable automation
- Explore common patterns for build and test execution in pipelines

## Suggested activities

### Step 1. Test run

1. Review the CI configuration used by the repository.
2. Add the `.github/workflows/ci.yml` to the test project.
3. Push your local code to the `main` branch and see how it is running

### Step 2. Test build caching

1. Copy the `ci.yml` file and save it as a `cd.yml` one
2. Configure the file to run only when pushed to main
3. Modify the image settings to `push: always` and, after the first failed run, configure the branch protection for the deployment.
4. Push a test change to the `main` branch and see how the pipeline is running with the new settings. The speed should increase considerably.

## Expected outcome

You should understand how Dev Containers help bridge the gap between local development environment and the CI/CD one.

> NOTE: Whether you want to use such a setup for production environment... probably not

## When completed

Return to the [main workshop README](../README.md).
