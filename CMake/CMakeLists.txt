CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

PROJECT(libjpeg C)

configure_file ( ${PROJECT_SOURCE_DIR}/jconfig.h.cmake ${PROJECT_SOURCE_DIR}/jconfig.h )

SET(libjpeg_SRCS jmemnobs.c jaricom.c jcapimin.c jcapistd.c jcarith.c jccoefct.c jccolor.c
	jcdctmgr.c jchuff.c jcinit.c jcmainct.c jcmarker.c jcmaster.c jcomapi.c jcparam.c
	jcprepct.c jcsample.c jctrans.c jdapimin.c jdapistd.c jdarith.c jdatadst.c jdatasrc.c
	jdcoefct.c jdcolor.c jddctmgr.c jdhuff.c jdinput.c jdmainct.c jdmarker.c jdmaster.c
	jdmerge.c jdpostct.c jdsample.c jdtrans.c jerror.c jfdctflt.c jfdctfst.c jfdctint.c
	jidctflt.c jidctfst.c jidctint.c jquant1.c jquant2.c jutils.c jmemmgr.c)
SET(libjpeg_HDRS cderror.h cdjpeg.h jdct.h jinclude.h jmemsys.h jpegint.h
	jversion.h transupp.h jerror.h jmorecfg.h jpeglib.h jconfig.h)

#IF(MSVC)
#    ADD_DEFINITIONS(/D_UNICODE /DUNICODE)
#    LIST(APPEND libjpeg_SRCS win32/jpeg.def)
#ENDIF(MSVC)

if(MSVC AND CONAN_LINK_RUNTIME)
	#by default CMake sets /MD for VS, replace it with ${CONAN_LINK_RUNTIME}
	set(variables
	  CMAKE_C_FLAGS_DEBUG
	  CMAKE_C_FLAGS_MINSIZEREL
	  CMAKE_C_FLAGS_RELEASE
	  CMAKE_C_FLAGS_RELWITHDEBINFO
	  CMAKE_CXX_FLAGS_DEBUG
	  CMAKE_CXX_FLAGS_MINSIZEREL
	  CMAKE_CXX_FLAGS_RELEASE
	  CMAKE_CXX_FLAGS_RELWITHDEBINFO
	)

	foreach(variable ${variables})
		if(${variable} MATCHES "/MD")
			string(REGEX REPLACE "/MD" ${CONAN_LINK_RUNTIME} ${variable} "${${variable}}")
		endif()
	endforeach()
endif(MSVC)

ADD_LIBRARY(jpeg ${libjpeg_SRCS} ${libjpeg_HDRS})

INSTALL(TARGETS jpeg
    RUNTIME DESTINATION bin
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib)

INSTALL(FILES ${libjpeg_HDRS} DESTINATION include)
