// main file
// author: grepcook
#include <iostream>
#include <sstream>

#include <boost/program_options.hpp>
#include <gumbo.h>
#include "config.hh"
#include "hardoav.hh"
#include "caoliu.hh"
void set_proxy(CURL *easyhandle, const std::string &proxy);
int main(int argc, const char *argv[]) {
    using namespace std;
    using namespace boost::program_options;
    try {
        stringstream ss;
        ss << argv[0] << ' ' << HARDOAV_VERSION_MAJOR << '.' << \
                         HARDOAV_VERSION_MINOR << " options";
        options_description desc{ss.str()};
        desc.add_options()
                ("help,h", "help options")
                ("site,s", value<string>()->default_value(DEFAULT_SITE), "caoliu site")
                ("dir,d", value<string>()->default_value(DEFAULT_DIR), "downloads dir")
                ("topic_num,t", value<int>()->default_value(DEFAULT_TOPIC_NUM), "topic num to scan")
                ("url,u", value<string>(), "individual url to downloads")
                ("proxy, p", value<string>()->default_value(DEFAULT_PROXY), "proxy url");
        variables_map vm;
        store(parse_command_line(argc, argv, desc), vm);
        notify(vm);
        if (vm.count("help")) {
            cout << desc << endl;
            exit(0);
        }
        auto easyhandle = curl_easy_init();
        string site(vm["site"].as<string>());
        string dir(vm["dir"].as<string>());
        int topic_num(vm["topic_num"].as<int>());
        string proxy = vm["proxy"].as<string>();
        cout << "current config: " << endl;
        cout << "caoliu site: " << site << endl;
        cout << "downloads dir: " << dir << endl;
        cout << "scanning topic number: " << topic_num << endl;
        cout << "proxy: " << proxy << endl;
        set_proxy(easyhandle, proxy);
        hardoav::Config config(site, dir, topic_num, proxy);
        if(vm.count("url")) {
            // individual url to download
            string url(vm["url"].as<string>());
            cout << "fetching url: " << url << endl;
            hardoav::ParseTopic parseTopic(config, url);
            cout << parseTopic.getEmbedSrc(easyhandle) << endl;
        }
        else {
            // scan

            // TODO
        }
        curl_easy_cleanup(easyhandle);
    }
    catch (const error &ex) {
        std::cerr << ex.what() << std::endl;
        return 1;
    }
    GumboOutput* output = gumbo_parse("<h1>Hello, World!</h1>");
    // Do stuff with output->root
    gumbo_destroy_output(&kGumboDefaultOptions, output);
    return 0;
}
void set_proxy(CURL *easyhandle, const std::string &proxy) {
    if (proxy == std::string("none"))
        return;
    std::cout << "using proxy: " << proxy << std::endl;
    curl_easy_setopt(easyhandle, CURLOPT_PROXY, proxy.data());
    curl_easy_setopt(easyhandle, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5);
}
