cmake_minimum_required(VERSION 3.0.2)
project(Homework4)

# Remove or comment out the following lines:
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  std_msgs
  message_generation
)

add_service_files(
  FILES
  OddEvenCheck.srv
)

generate_messages(
  DEPENDENCIES
  sensor_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Comment out or remove the following lines:
# add_executable(rpm_pub src/rpm_pub.py)
# target_link_libraries(rpm_pub ${catkin_LIBRARIES})

# add_executable(speed_calc src/speed_calc.py)
# target_link_libraries(speed_calc ${catkin_LIBRARIES})

# add_executable(service_server src/service_server.py)
# target_link_libraries(service_server ${catkin_LIBRARIES})
# add_dependencies(service_server Homework5_generate_messages_py)

# add_executable(service_client src/service_client.py)
# target_link_libraries(service_client ${catkin_LIBRARIES})
# add_dependencies(service_client Homework4_generate_messages_py)

# Instead, use the following to install Python scripts:
catkin_install_python(PROGRAMS
  src/rpm_pub.py
  src/speed_calc.py
  src/service_server.py
  src/service_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
