# 05 - ROS2 and Gazebo

This section introduces robotics development workflows using ROS 2 and Gazebo inside a container.

This and the next stages are built around [gazebosim/ros_gz_project_template](https://github.com/gazebosim/ros_gz_project_template) - 
a template project integrating ROS and Gazebo simulator.
For a full project, see [this directory](../full-project/README.md).


## Goals

- Understand how ROS 2 can be used in a containerized environment
- Learn how simulation tools such as Gazebo fit into embedded and robotics workflows
- Explore how a devcontainer can support robotics development

## Suggested activities

<!--TODO switch to https://github.com/lopsided98/nix-ros-overlay ?-->

### Step 1. Base image

In this phase, we will construct a base image for running ROS2 and Gazebo in a 
Dev Container.

1. Review the ROS-related files and package layout in [project](./project/).
2. Launch the Dev Container
3. Ensure that the environment is in place

```sh
rosdep update
sudo apt-get update 
rosdep install --from-paths . --ignore-src -r -i -y --rosdistro kilted
```

4. Run the project build

```bash
colcon build --cmake-args -DBUILD_TESTING=ON
```

### Step 2. Simulation with Gazebo

1. Start the simulation environment and inspect the available tools.
2. Experiment with layout

```bash
ros2 launch ros_gz_example_bringup diff_drive.launch.py
```

For a more detailed guide on using this template see [documentation](https://gazebosim.org/docs/latest/ros_gz_project_template_guide).


## Expected outcome

You should be able to appreciate how containerized environments can support complex robotics development and simulation.

## When completed

Return to the [main workshop README](../README.md).
