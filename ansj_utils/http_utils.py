
import json
import requests


def post_json(url, body=None, url_parameter_dict=None):
    if body is None:
        body = {}
    if url_parameter_dict is not None and len(url_parameter_dict) > 0:
        url += "?"
        for key in url_parameter_dict:
            url += key
            url += "="
            url += url_parameter_dict[key]
            url += "&"
        url = url[0, len(url) - 1]
    headers = {"content-type": "application/json"}
    result = requests.post(url, json.dumps(body, ensure_ascii=False).encode(), headers=headers)
    return result.json()


def get_json(url, body=None, url_parameter_dict=None):
    if body is None:
        body = {}
    if url_parameter_dict is not None and len(url_parameter_dict) > 0:
        url += "?"
        for key in url_parameter_dict:
            url += key
            url += "="
            url += url_parameter_dict[key]
            url += "&"
        url = url[0: len(url) - 1]
    headers = {"content-type": "application/json"}
    result = requests.get(url, json.dumps(body, ensure_ascii=False).encode(), headers=headers)
    return result.json()


def response_error_msg(error_code, message, data_obj=None):
    return {"code": error_code, "message": message, "data": data_obj}


if __name__ == '__main__':
    url_parameter_dict = {"grant_type": "client_credentials", "client_id": "cnbFH44RVqdG4621rHatP3nx",
                          "client_secret": "XLr9aOXOUFia2F59ZMV8mqAaAZMrN2zv"}
    body = {}
    print(get_json("https://aip.baidubce.com/oauth/2.0/token", url_parameter_dict, body))
