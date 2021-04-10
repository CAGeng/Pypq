from wsgiref.simple_server import make_server
import json



def application(env, response): 
    # response('200 OK', [('Content-type', 'application/json;charset=utf-8')])  
    msg = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1, "pageSize": 60}
    return json.dumps(msg)


if __name__ == "__main__": 

    http_server = make_server('', 8000, application)
    print('server is starting...') 

    http_server.serve_forever()  