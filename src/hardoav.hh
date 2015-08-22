#ifndef HARDOAV_HH
#define HARDOAV_HH

namespace hardoav {
class Config {
public:
    Config(std::string site, std::string dir, int topic_num)
        : m_site(site), m_dir(dir), m_topic_num(topic_num){}
    const std::string& getSite() {return m_site;}
    const std::string& getDir() {return m_dir;}
    int getTopic_num() {return m_topic_num;}
private:
    std::string m_site;
    std::string m_dir;
    int m_topic_num;
};
}

#endif
