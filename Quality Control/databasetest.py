 import unit test
from functools import wraps
import memory_profiler
from app import app,dbmodule
 
@app.route("/addPorts")
  @my_profiler
  def route_one():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200)
# checkind users endpoints
@app.route("allusers")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200)


@app.route("findusers")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200)  

    @app.route("addusers")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200)  

       @app.route("updateusers")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 

       @app.route("deleteusers")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 
#checking posts enpoints

       @app.route("addposts")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 


       @app.route("updateposts")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 


       @app.route("deleteposts")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 
# Checking comments endpoints

       @app.route("addcomments")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 
 

       @app.route("deletecomments")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 


       @app.route("updatecomments")
@my_profiler
  def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200) 