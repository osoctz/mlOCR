import time
from aip import AipOcr


class Aiocr(object):

    def __init__(self, app_id, api_key, secret_key):
        self._app_id = app_id
        self._api_key = api_key
        self._secret_key = secret_key
        self._client = AipOcr(app_id, api_key, secret_key)

    def proc_form(self, image):
        """ 读取图片 """
        image = self.get_file_content(image)
        """ 调用表格文字识别同步接口 """
        return self._client.tableRecognitionAsync(image);

    def proc_from_res(self, req_id):
        """ 如果有可选参数 """
        options = {"result_type": "excel"}
        """ 带参数调用表格识别结果 """
        return self._client.getTableRecognitionResult(req_id, options)

    def get_file_content(self, file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':
    """ 你的 APPID AK SK """
    APP_ID = '11635479'
    API_KEY = 'y52YctCoPhY8KRwtzoFliKsU'
    SECRET_KEY = 'GawZoudCnmRhqq1lDbqkpgky3rpsmk8G'

    ai_ocr = Aiocr(APP_ID, API_KEY, SECRET_KEY)
    res = ai_ocr.proc_form('1.jpg')
    for req in res['result']:
        resp = ai_ocr.proc_from_res(req['request_id'])
        while not ('error_code' in resp) and not resp['result']['ret_code'] == 3:
            time.sleep(10)
            resp = ai_ocr.proc_from_res(req['request_id'])
        print(resp)
