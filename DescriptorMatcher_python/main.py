# -*- coding: utf-8 -*-

from DescriptorMacher import *
import cv2

def createHandlers() :
	handlers = []
	handlers.append(DescHandler.factory("sift", "bf"))
	handlers.append(DescHandler.factory("surf", "flann"))
	handlers.append(DescHandler.factory("orb", "flann"))
	
	return handlers

def main() :
	print("Press 'f' to change reference frame,")
	print("'u' to increase match accept ratio,")
	print("'d' to decrease match accept ratio,")
	print("and 'q' to quit.")

	cap = cv2.VideoCapture(0)
	if cap.isOpened() :
		pass
	else :
		return

	curDesc = createHandlers()
	refDesc = createHandlers()

	ret, initframe = cap.read()
	#initframe = cv2.flip(initframe, 1)
	for des in refDesc :
		des.detectAndCompute(initframe)

	acceptRatio = 0.5
	
	while(True):
        	#print('width: {}, height : {}'.format(cap.get(3), cap.get(4)))
		ret, frame = cap.read()

		for des in curDesc :
			des.detectAndCompute(frame)
		
		key = cv2.waitKey(10) & 0xFF

		if key == ord('f') or key == ord('F') :
			print("set fixed reference result")
			for des in refDesc :
				des.detectAndCompute(frame)
		elif key == ord('u') or key == ord('U') :
			acceptRatio = min(acceptRatio + 0.1, 1.)
		elif key == ord('d') or key == ord('D') :
			acceptRatio = max(acceptRatio - 0.1, 0.)
		elif key == ord('q') or key == ord('Q') :
			break

		result_img = 'a'
		for i in range(len(curDesc)) :
			#print(i)
			matches = curDesc[i].match(refDesc[i].getDescriptors(), acceptRatio)
			result_img = DescHandler.drawAndAppendResult(result_img, curDesc[i], refDesc[i], matches)

		result = DescHandler.getResultingImg(result_img, 1000)
		cv2.imshow("matches", result)

if __name__ == '__main__':
	main()
