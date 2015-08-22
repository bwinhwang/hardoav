#include "caoliu.hh"
#include <iostream>
#include <cstdio>
using namespace hardoav;
std::string ParseTopic::getEmbedSrc(CURL* easyhandle) {
    curl_easy_setopt(easyhandle, CURLOPT_URL, m_topic_url.data());
    auto status = curl_easy_perform(easyhandle);
    if(status != CURLE_OK) {
        std::cerr << "curl_easy_perform() failed: "
                  << curl_easy_strerror(status);
    }
    return std::string("");
}
