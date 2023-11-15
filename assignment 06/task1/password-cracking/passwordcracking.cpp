/**
 * You have found the key (hash) and the salt for Ola’s password on a server:
 * key: “ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6”
 * salt: “Saltet til Ola”
 * You know that PBKDF2 with SHA1 is used by the server with 2048 iterations
 * You know that Ola does not bother to use many letters in his password
 * What is Ola’s password?
*/

#include <iomanip>
#include <iostream>
#include <openssl/evp.h>
#include <openssl/sha.h>
#include <sstream>
#include <string>

const int PASS_SIZE = 3;

// Return hex string from bytes in input string
std::string hex(const std::string &input) {
  std::stringstream hex_stream;
  hex_stream << std::hex << std::internal << std::setfill('0');
  for (auto &byte : input)
    hex_stream << std::setw(2) << (int)(unsigned char)byte;
  return hex_stream.str();
}

// PBKDF2 with SHA1 hash of input string
std::string pbkdf2(const std::string &input, const std::string &salt, unsigned int iterations) noexcept {
    const auto length = SHA_DIGEST_LENGTH;

    std::string hash(length, '\x00');

    PKCS5_PBKDF2_HMAC_SHA1(
        input.data(), input.size(),
        reinterpret_cast<const unsigned char *>(salt.data()), salt.size(),
        iterations, length,
        reinterpret_cast<unsigned char *>(&hash[0])
    );

    return hash;
}

// Function that checks if the password is the same as the given hash (key)
void check_password(std::string key, std::string salt, std::string letters, std::string password) {
    
    // check passwords up to a certain length
    if (password.size() > PASS_SIZE) {
        return;
    }

    // hash the password
    std::string passhash = pbkdf2(password, salt, 2048);
    
    std::cout << "Now checking password: " << password << " Hash: " << hex(passhash) << std::endl;  // print for debugging

    // if the hash of the password is the same as the given one, print it and exit the program
    if (hex(passhash) == key) {
        std::cout << "Password is: " << password << std::endl;
        exit(0);
    }

    // build up other combinations of the password
    for (char c : letters) {
        password.push_back(c);
        check_password(key, salt, letters, password);
        password.pop_back();
    }
}

int main() {
    // given hash and salt and the list of possible letters in the password
    std::string key = "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6";
    std::string salt = "Saltet til Ola";
    std::string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    std::string password;

    check_password(key, salt, letters, password);
}
