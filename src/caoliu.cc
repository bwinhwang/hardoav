#include "caoliu.hh"
#include <iostream>
#include <functional>
#include <cstdio>
using namespace hardoav;
size_t ResponseHandler::write_data(void *buffer, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    std::string chunk;
    chunk.append((char*)buffer, realsize);
    std::cout << chunk;
    content += chunk;
    return realsize;
}
std::string ParseTopic::getEmbedSrc(CURL* easyhandle) {
    using namespace std::placeholders;
    curl_easy_setopt(easyhandle, CURLOPT_URL, m_topic_url.data());
    // TODO write a callback class
    ResponseHandler res_handler;
    auto callback = std::bind(&ResponseHandler::write_data,
                              &res_handler, _1, _2, _3, _4);
    std::string t("1234");
    callback((void*)t.data(), (size_t)t.length(), (size_t)1, (void*)0);
    // curl_easy_setopt(easyhandle, CURLOPT_WRITEFUNCTION, callback);
    auto status = curl_easy_perform(easyhandle);
    if(status != CURLE_OK) {
        std::cerr << "curl_easy_perform() failed: "
                  << curl_easy_strerror(status) << std::endl;
    }
    return res_handler.get_content();
}

