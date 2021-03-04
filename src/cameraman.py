import cv2
import logging
import hashlib
logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filemode='w',
        )
class Cameraman:
    def __init__(self):
        self.logger = logging.getLogger('Camera')
        self.logger.info('объект Cameraman был успешно создан')

    def get_image(self):

        cap = cv2.VideoCapture(0)

        ret, img = cap.read()
        if ret == False:
            raise ValueError("Image is empty, please check the camera connection")
        else:
            self.logger.info('Изображение было успешно полученно')


        hash_object = hashlib.md5(img)
        name_obj = hash_object.hexdigest()
        msg1 = f' Имя фотографии сгенерировно: {name_obj}'
        self.logger.info(msg1)

        cv2.imshow("camera", img)



        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    test = Cameraman()
    test.get_image()




