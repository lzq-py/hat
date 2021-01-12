from rest_framework.response import Response


class APIResponse(Response):

    def __init__(self, data_status=200, data_message=0, results=None,
                 http_status=None, headers=None, exceptions=False, **kwargs):
        # 定义数据返回的状态
        data = {
            "status": data_status,
            "message": data_message,
        }

        # 判断results是否有结果
        if results is not None:
            data['results'] = results

        # 如果还有自定义参数 使用kwargs接收
        # 如果kwargs有值 则添加到data中  如果没值 则不会做任何操作
        data.update(kwargs)

        # 获取一个response对象 需要将子弟傍依的response响应回去
        super().__init__(data=data, status=http_status, headers=headers, exception=exceptions)