# Install script for directory: /home/maanz-ai/PycharmProjects/av-ws/src/test_pkg

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/maanz-ai/PycharmProjects/av-ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/test_pkg.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_pkg/cmake" TYPE FILE FILES
    "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/test_pkgConfig.cmake"
    "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/test_pkgConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_pkg" TYPE FILE FILES "/home/maanz-ai/PycharmProjects/av-ws/src/test_pkg/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/carla_status.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/carla_world_info.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/ackermann_publisher.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/ackermann_subscriber.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/carla_map.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/carla_spawn_controller.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/carla_spawn_object.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/carla_spawn_sensor.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/debug_marker.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/distroy_object.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/tf_subscriber.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/waypoint.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/test_pkg" TYPE PROGRAM FILES "/home/maanz-ai/PycharmProjects/av-ws/build/test_pkg/catkin_generated/installspace/xodr_map_to_json.py")
endif()

