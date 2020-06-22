# Install script for directory: /home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_amplificador_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_mean_meter.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_sumador.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_diezma_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_zero_order_hold2_cc.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_diezmador_cc.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_e_canal_BER.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_unipolar_to_bipolar_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_retrazo_cc.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_usrp2usrp1_cc.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/tool_borrado.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_vec_diagrama_ojo_f.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_retrazo_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_zero_order_hold_bb.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_e_BERtool.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_max_xx.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_ej_amplificador_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_fft_jesus.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_Zero_Order_Hold.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_decisor_fb.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/BackUp_E3TRadio_acumulador_truncado_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_power_meter.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_delay_hob_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_averager.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_decisor_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_Averager_onate.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_ifft_jesus.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_vector_average_hob.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_decisor_fi.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_sum_vectors_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_FFT_SDRCol_triangular.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_acumulador_truncado_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_diezmoppenh3_ff.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_time_averager_jesus.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_v_delay.block.yml"
    "/home/cloudmanager/MisGNURadio/MisGits/comdig_Lib_OOT_E3TRadio_python3/grc/E3TRadio_vec_diagrama_ojo2_f.block.yml"
    )
endif()

