#ifndef BFMATCHER_H
#define BFMATCHER_H

#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/xfeatures2d.hpp>

class BFMatcher : public cv::DescriptorMatcher
{
public:
    BFMatcher(int _normType = cv::NORM_L2, bool _crossCheck = false) {
        normType = _normType;
        crossCheck = _crossCheck;
    }

    static cv::Ptr<BFMatcher> create( int _normType, bool _crossCheck ) {
        //return cv::makePtr<BFMatcher>(_normType, _crossCheck);
        //return new BFMatcher(_normType, _crossCheck);
        //return cv::makePtr<BFMatcher>(_normType, _crossCheck);
    }

    virtual cv::Ptr<DescriptorMatcher> clone( bool emptyTrainData=false ) const;

protected:
    //virtual void knnMatchImpl( InputArray queryDescriptors, std::vector<std::vector<DMatch> >& matches, int k,
        //InputArrayOfArrays masks=noArray(), bool compactResult=false );
    //virtual void radiusMatchImpl( InputArray queryDescriptors, std::vector<std::vector<DMatch> >& matches, float maxDistance,
       //InputArrayOfArrays masks=noArray(), bool compactResult=false );

    int normType;
    bool crossCheck;
};

/*class BFMatcher : public cv::DescriptorMatcher {
public:
    static BFMatcher* create(int _normType = cv::NORM_L2, bool _crossCheck = false) {
        cv::Ptr<int> matcher_typ;
        cv::Ptr<bool> matcher_check;
        matcher_typ = &_normType;
        matcher_check = &_crossCheck;

        return new BFMatcher(matcher_typ, matcher_check);
    }

protected:
    BFMatcher(cv::Ptr<int> _normType, cv::Ptr<bool> _crossCheck) {
        normType = _normType;
        crossCheck = _crossCheck;
    }

    cv::Ptr<int> normType;
    cv::Ptr<bool> crossCheck;
};*/
#endif // BFMATCHER_H
