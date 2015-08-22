#ifndef HARDOAV_CAOLIU_HH
#define HARDOAV_CAOLIU_HH
#include <string>
#include <curl/curl.h>
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
}

#endif
