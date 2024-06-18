#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <curl/curl.h>
#include <ifaddrs.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstdio>
#include <cstring>

// Classe Rede
class Rede {
public:
    // Verifica a conexão com a internet
    static void checkInternetConnection();

    // Verifica a presença de proxies nas variáveis de ambiente
    static void checkProxy();

    // Obtém o IP público
    static std::string getPublicIP();

    // Compara o IP público com o IP local para detectar proxies transparentes
    static void compareIpAddresses();

private:
    // Callback para escrever a resposta da requisição HTTP
    static size_t writeCallback(void* contents, size_t size, size_t nmemb, void* userp);

    // Callback para capturar os cabeçalhos da resposta HTTP
    static size_t headerCallback(char* buffer, size_t size, size_t nitems, void* userdata);

    // Obtém o IP local da máquina
    static std::string getLocalIP();
};
