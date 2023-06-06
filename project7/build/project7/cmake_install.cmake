# Install script for directory: /home/ubuntu/catkin_make/project7/src/project7

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ubuntu/catkin_make/project7/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/project7/action" TYPE FILE FILES
    "/home/ubuntu/catkin_make/project7/src/project7/action/Navigate2D.action"
    "/home/ubuntu/catkin_make/project7/src/project7/action/FollowPath.action"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/project7/msg" TYPE FILE FILES
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/Navigate2DAction.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/Navigate2DActionGoal.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/Navigate2DActionResult.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/Navigate2DActionFeedback.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/Navigate2DGoal.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/Navigate2DResult.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/Navigate2DFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/project7/msg" TYPE FILE FILES
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/FollowPathAction.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/FollowPathActionGoal.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/FollowPathActionResult.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/FollowPathActionFeedback.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/FollowPathGoal.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/FollowPathResult.msg"
    "/home/ubuntu/catkin_make/project7/devel/share/project7/msg/FollowPathFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/project7/cmake" TYPE FILE FILES "/home/ubuntu/catkin_make/project7/build/project7/catkin_generated/installspace/project7-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/ubuntu/catkin_make/project7/devel/include/project7")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/ubuntu/catkin_make/project7/devel/share/roseus/ros/project7")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/ubuntu/catkin_make/project7/devel/share/common-lisp/ros/project7")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/ubuntu/catkin_make/project7/devel/share/gennodejs/ros/project7")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/ubuntu/catkin_make/project7/devel/lib/python3/dist-packages/project7")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/ubuntu/catkin_make/project7/devel/lib/python3/dist-packages/project7")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ubuntu/catkin_make/project7/build/project7/catkin_generated/installspace/project7.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/project7/cmake" TYPE FILE FILES "/home/ubuntu/catkin_make/project7/build/project7/catkin_generated/installspace/project7-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/project7/cmake" TYPE FILE FILES
    "/home/ubuntu/catkin_make/project7/build/project7/catkin_generated/installspace/project7Config.cmake"
    "/home/ubuntu/catkin_make/project7/build/project7/catkin_generated/installspace/project7Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/project7" TYPE FILE FILES "/home/ubuntu/catkin_make/project7/src/project7/package.xml")
endif()

