#ifndef HARDOAV_HH
#define HARDOAV_HH

namespace hardoav {
class Config {
public:
    Config(const std::string &site, const std::string &dir,
           int topic_num, const std::string &proxy)
        : m_site(site), m_dir(dir), m_topic_num(topic_num), m_proxy(proxy){}
    const std::string& get_site() {return m_site;}
    const std::string& get_dir() {return m_dir;}
    int get_topic_num() {return m_topic_num;}
    const std::string& get_proxy() {return m_proxy;}
private:
    std::string m_site;
    std::string m_dir;
    int m_topic_num;
    std::string m_proxy;
};
}

#endif
