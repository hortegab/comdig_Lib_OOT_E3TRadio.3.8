INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_E3TRADIO_PRUEBA E3TRadio_prueba)

FIND_PATH(
    E3TRADIO_PRUEBA_INCLUDE_DIRS
    NAMES E3TRadio_prueba/api.h
    HINTS $ENV{E3TRADIO_PRUEBA_DIR}/include
        ${PC_E3TRADIO_PRUEBA_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    E3TRADIO_PRUEBA_LIBRARIES
    NAMES gnuradio-E3TRadio_prueba
    HINTS $ENV{E3TRADIO_PRUEBA_DIR}/lib
        ${PC_E3TRADIO_PRUEBA_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/E3TRadio_pruebaTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(E3TRADIO_PRUEBA DEFAULT_MSG E3TRADIO_PRUEBA_LIBRARIES E3TRADIO_PRUEBA_INCLUDE_DIRS)
MARK_AS_ADVANCED(E3TRADIO_PRUEBA_LIBRARIES E3TRADIO_PRUEBA_INCLUDE_DIRS)