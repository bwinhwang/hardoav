#ifndef HARDOAV_CAOLIU_HH
#define HARDOAV_CAOLIU_HH
#include <string>
#include <curl/curl.h>
#include <gumbo.h>

/**
 * @brief The Caoliu class
 */
namespace hardoav {
class Config;
class Caoliu {
public:
    Caoliu(const Config &config);
private:
  const Config &m_config;
};
class FileDownload {
    FileDownload(const Config &config, const std::string &download_url,
                 const std::string &referer, const std::string &filename = nullptr)
        : m_config(config), m_download_url(download_url), m_referer(referer), m_filename(filename){}
private:
  const Config &m_config;
  std::string m_download_url;
  std::string m_referer;
  std::string m_filename;

};
class ParseTopic {
public:
  ParseTopic(const Config &config, const std::string &topic_url,
             const std::string &referer = "none")
      : m_config(config), m_topic_url(topic_url), m_referer(referer){}
  std::string getEmbedSrc(CURL *easyhandle);
  std::string getDownloadUrl(const std::string &embed_src);
private:
  const Config &m_config;
  std::string m_topic_url;
  std::string m_referer;
};

class ResponseHandler {
public:
    static size_t write_data(void *buffer, size_t size, size_t nmemb, void *userp);
    static size_t write_header(void *buffer, size_t size, size_t nmemb, void *userp);
    ResponseHandler& append(const std::string &chunk){
        content.append(chunk);
        return *this;
    }
    const std::string get_content() {return content;}
    const std::string get_from_charset() {return from_charset;}
    const std::string get_utf8_content();
    GumboOutput *to_gumbo_parser();
    void destory_gumbo_output(GumboOutput * output);
private:
    std::string content;
    std::string utf8_content;
    std::string from_charset = "gbk";
};
}

#endif
