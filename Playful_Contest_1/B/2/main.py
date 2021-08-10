import cv2 as cv
from skimage.metrics import structural_similarity as compare_ssim

A = cv.imread('A.jpg', 0)
B = cv.imread('B.jpg', 0)
(score, diff) = compare_ssim(A, B, full=True)
cv.imshow('d', diff)
s = cv.waitKey(0)
