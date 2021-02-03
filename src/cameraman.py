import cv2

class Cameraman:
    def __init__(logging):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filemode='w',
        )

        logging.info("объект Cameraman был успешно создан")

        #self.logger = logging.getLogger('Camera')
        #self.logger.setLevel(logging.INFO)
        #self.logger.info('объект Cameraman был успешно создан')
    def get_image(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow("camera", img)
            if cv2.waitKey(10) == 27:  # Клавиша Esc
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    test = Cameraman("test")
    test.get_image()




