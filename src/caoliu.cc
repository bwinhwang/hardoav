#include "caoliu.hh"
#include <iostream>
#include <cstdio>
#include <cstring>
#include <stringprep.h>
#include <iconv.h>
#include <errno.h>
using namespace hardoav;

std::string ParseTopic::getEmbedSrc(CURL* easyhandle) {
    curl_easy_setopt(easyhandle, CURLOPT_URL, m_topic_url.data());
    // TODO write a callback class
    ResponseHandler res_handler;
    curl_easy_setopt(easyhandle, CURLOPT_WRITEFUNCTION, &ResponseHandler::write_data);
    curl_easy_setopt(easyhandle, CURLOPT_HEADERFUNCTION, &ResponseHandler::write_header);
    curl_easy_setopt(easyhandle, CURLOPT_WRITEDATA, &res_handler);
    curl_easy_setopt(easyhandle, CURLOPT_HEADERDATA, &res_handler);
    auto status = curl_easy_perform(easyhandle);
    if(status != CURLE_OK) {
        std::cerr << "curl_easy_perform() failed: "
                  << curl_easy_strerror(status) << std::endl;
    }
    /*return std::string(
                stringprep_convert(res_handler.get_content().data(), "UTF-8//IGNORE", "gb2312")
                );
    */
    return res_handler.get_utf8_content();
}
size_t ResponseHandler::write_data(void *buffer, size_t size, size_t nmemb, void *userp) {
    ResponseHandler *res_handler = (ResponseHandler*)userp;
    size_t realsize = size * nmemb;
    std::string chunk;
    chunk.append((char*)buffer, realsize);
    //const static char *to_code = "UTF-8//IGNORE";
    //chunk = stringprep_convert(chunk.data(), to_code, res_handler->get_from_charset().data());
    res_handler->append(chunk);
    return realsize;
}
size_t ResponseHandler::write_header(void *buffer, size_t size, size_t nmemb, void *userp) {
    ResponseHandler *res_handler = (ResponseHandler*)userp;
    size_t realsize = size * nmemb;
    std::string header;
    header.append((char*)buffer, realsize);
    std::cout << header << std::endl;
    return realsize;
}
const std::string ResponseHandler::get_utf8_content() {
    const static char *to_code = "UTF-8//IGNORE";
    utf8_content = stringprep_convert(get_content().data(), to_code, get_from_charset().data());
    return utf8_content;
}

GumboOutput* ResponseHandler::to_gumbo_parser() {
    return gumbo_parse(get_utf8_content().data());
}
void ResponseHandler::destory_gumbo_output(GumboOutput * output) {
    gumbo_destroy_output(&kGumboDefaultOptions, output);
}
