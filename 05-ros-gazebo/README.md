# 05 - ROS and Gazebo

This section introduces robotics development workflows using ROS 2 and Gazebo inside a container.

This and the next stages are built around [gazebosim/ros_gz_project_template](https://github.com/gazebosim/ros_gz_project_template) - 
a template project integrating ROS and Gazebo simulator.
For a full project, see [this directory](../full-project/README.md).


## Goals

- Understand how ROS 2 can be used in a containerized environment
- Learn how simulation tools such as Gazebo fit into embedded and robotics workflows
- Explore how a devcontainer can support robotics development

## Suggested activities

1. Review the ROS-related files and package layout in [full-project](../full-project/).
2. Start the simulation environment and inspect the available tools.
3. Run a small example or launch command to confirm the setup.

#TODO
#rosdep update
#sudo apt-get update 
#rosdep install --from-paths . --ignore-src -r -i -y --rosdistro kilted

## Expected outcome

You should be able to appreciate how containerized environments can support complex robotics development and simulation.

## When completed

Return to the [main workshop README](../README.md).
