#ifndef BFMATCHER_H
#define BFMATCHER_H

#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/xfeatures2d.hpp>


class BFMatcher : public cv::DescriptorMatcher {
public:
    static BFMatcher* factory(cv::Ptr<cv::NormTypes> _param = cv::NORM_HAMMING, bool _crossCheck = false, float _distance) {
        distance = _distance;

        return new BFMatcher(_param, _crossCheck);
    }

private:
    BFMatcher(cv::Ptr<cv::NormTypes> _param, bool _crossCheck) {
        param = _param;
        crossCheck = _crossCheck;
    }

    cv::Ptr<cv::NormTypes> param;
    bool crossCheck;
    float distance;
};

#endif // BFMATCHER_H
