# C++ Tooling Basics Sample Project

A minimal CMake + GoogleTest project used to explore the C/C++ devcontainer tooling.

## Prerequisites

Open this directory in VS Code and choose **Reopen in Container** so that CMake, a compiler, and vcpkg are available.

## Configure and build

```shell
cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE=$VCPKG_ROOT/scripts/buildsystems/vcpkg.cmake
cmake --build build
```

## Run the app

```shell
./build/calculator_app
```

## Run the tests

```shell
ctest --test-dir build --output-on-failure
```
