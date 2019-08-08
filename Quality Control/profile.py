@app.route("/user/<username>", methods=["GET"])
 @my_profiler
def route_one():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200)

@app.route("/login/0000")
@my_profiler
def route_two():
    api_live = ping_api()
    if not api_live:
        return make_response('', 503)
    return make_response('', 200)