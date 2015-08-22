#ifndef HARDOAV_CAOLIU_HH
#define HARDOAV_CAOLIU_HH
/**
 * @brief The Caoliu class
 */
namespace hardoav {
class Config;
class Caoliu {
public:
    Caoliu(const Config &config);

};
class FileDownload {
    FileDownload(const Config &config, std::string download_url, std::string referer);
};
class ParseTopic {
  ParseTopic(const Config &config, std::string topic_url, std::string referer = nullptr);
};
}

#endif
