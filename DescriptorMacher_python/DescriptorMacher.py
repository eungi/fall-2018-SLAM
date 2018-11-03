# -*- coding: utf-8 -*-

import cv2
import copy
import sys

class DescHandler :
	__descMarker = []
	__matcher = []
	__name = 0
	__image = []
	__keypoints = []
	__descriptors = []

	def __init__(self, _name, _descMarker, _matcher) :
		self.__name = _name
		self.__descMarker = _descMarker
		self.__matcher = _matcher

	@staticmethod
	def factory(descType, matcherType) :

		if descType == "sift" :
			desc = cv2.xfeatures2d.SIFT_create()
		elif descType == "surf" :
			desc = cv2.xfeatures2d.SURF_create()
		elif descType == "orb" :
			desc = cv2.ORB_create()
		else :
			print("error")

		if matcherType == "flann" :
			if descType == "orb" :
				FLANN_INDEX_LSH = 6
				index_params= dict(algorithm = FLANN_INDEX_LSH, table_number = 6, key_size = 12, multi_probe_level = 1)
				search_params = dict(checks = 50)
				__matcher = cv2.FlannBasedMatcher(index_params, search_params)
			else :
				__matcher = cv2.FlannBasedMatcher()
		elif matcherType == "bf" :
			if descType == "orb" :
				__matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
			else :
				__matcher = cv2.BFMatcher(cv2.NORM_L1)
		else :
			print("error")

		return DescHandler(descType, desc, __matcher)

	def detectAndCompute(self, _image) :
		self.__image = _image
		self.__keypoints, self.__descriptors = self.__descMarker.detectAndCompute(self.__image, None)

	def match(self, otherDescriptors, acceptRatio = 0.5) :
		matches = self.__matcher.match(self.__descriptors, otherDescriptors)
		
		matches = sorted(matches, key=lambda x:x.distance)
		numGoodMatches = len(matches) * acceptRatio

		good = []
		for m in range(int(numGoodMatches)) :
			good.append(matches[m])

		return good

	@staticmethod
	def drawAndAppendResult(_result, desc1, desc2, _matches) :
		matchimg = None
		matchimg = cv2.drawMatches(desc1.getImage(), desc1.getKeypoints(), desc2.getImage(), desc2.getKeypoints(), _matches, matchimg, flags=0)
		cv2.putText(matchimg, desc1.getName(), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

		if _result == 'a' :
			_result = matchimg
		else :
			himgs = (_result, matchimg)
			_result = cv2.vconcat(himgs, _result)
		
		return _result

	def getDescriptors(self) :
		return self.__descriptors

	def getImage(self) :
		return self.__image

	def getName(self) :
		return self.__name

	def getKeypoints(self) :
		return self.__keypoints

	@staticmethod
	def getResultingImg(_result, maxheight = 0) :
		resimg = copy.deepcopy(_result)
		
		if maxheight > 100 and maxheight < resimg.shape[0] :
			scale = float(maxheight) / float(resimg.shape[0])
			resimg = cv2.resize(resimg, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
		
		return resimg
