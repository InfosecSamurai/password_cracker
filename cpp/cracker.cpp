#include <iostream>
#include <string>
#include <openssl/sha.h>
#include <vector>
#include <thread>

std::string sha256(const std::string &password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char *)password.c_str(), password.length(), hash);
    
    std::string hashed;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        char buf[3];
        sprintf(buf, "%02x", hash[i]);
        hashed += buf;
    }
    return hashed;
}

void bruteForce(const std::string &targetHash, char start, char end) {
    std::string charset = "abcdefghijklmnopqrstuvwxyz0123456789";
    for (char c = start; c < end; c++) {
        std::string attempt(1, c);
        if (sha256(attempt) == targetHash) {
            std::cout << "[+] Password found: " << attempt << std::endl;
            return;
        }
    }
}

int main() {
    std::string targetHash = sha256("pass123");  // Example hash
    int numThreads = 4;

    std::vector<std::thread> threads;
    for (int i = 0; i < numThreads; i++) {
        char start = 'a' + (i * 6);
        char end = start + 6;
        threads.emplace_back(bruteForce, targetHash, start, end);
    }

    for (auto &thread : threads) {
        thread.join();
    }

    return 0;
}
