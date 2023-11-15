cmake_minimum_required(VERSION 3.5)

project(password-cracking)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall -Wextra")

if(APPLE)
    if(EXISTS /usr/local/opt/openssl)
        set(OPENSSL_ROOT_DIR /usr/local/opt/openssl)
    elseif(EXISTS /opt/homebrew/opt/openssl)
        set(OPENSSL_ROOT_DIR /opt/homebrew/opt/openssl)
    endif()
endif()

find_package(OpenSSL REQUIRED)
include_directories(${OPENSSL_INCLUDE_DIR})

add_executable(passwordcracking passwordcracking.cpp)
target_link_libraries(passwordcracking ${OPENSSL_CRYPTO_LIBRARY})
