import imgaug as ia
import cv2
import augmentation as aug

label_faces, aug_faces = aug.Make_Data("avengers")

for i in range(len(aug_faces)):
    ia.imshow(ia.draw_grid(aug_faces[i], cols = 8))

# cv2.imshow("img", aug_faces[0][0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
