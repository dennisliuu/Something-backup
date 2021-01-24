AsyncRequest.prototype.send = function (e) {
    var t;
    if (console.log("Send_Request"), __p && __p(), e = e || !1, !this.uri) return !1;
    if (!this.errorHandler && this.getOption("suppressErrorHandlerWarning"), this.getOption("jsonp") && "GET" != this.method && this.setMethod("GET"), (this.getOption("useIframeTransport") || this.getOption("useFetchWithIframeFallback")) && "GET" != this.method && this.setMethod("GET"), null !== this.timeoutHandler && (this.getOption("jsonp") || this.getOption("useIframeTransport") || this.getOption("useFetchWithIframeFallback")), !this.getReadOnly() && (this.specifiesWriteRequiredParams(), "POST" != this.method)) return !1;
    if (document.location.search.toString().includes(this.uri.toString())) return !1;
    Object.assign(this.data, require("getAsyncParams")(this.method));
    var i = this._timesliceInteraction;
    if (i && (i.addArtilleryIDHeader(this), i.inform("async_request_sent", {
        type: require("ArtilleryJSPointTypes").ASYNC_REQUEST_SENT
    }), i.trace().addStringAnnotation("uri", this.getURI())), require("isEmpty")(this.context) || (Object.assign(this.data, this.context), this.data.ajax_log = 1), require("Env").force_param && Object.assign(this.data, require("Env").force_param), this._setUserActionID(), this.getOption("bundle") && this._isMultiplexable()) return AsyncMultiplex.schedule(this), !0;
    this.setNewSerial(), this.getOption("asynchronous_DEPRECATED") || this.uri.addQueryData({
        __s: 1
    }), this.uri.addQueryData(((t = {})[require("PixelRatioConst").cookieName] = require("WebPixelRatio").get(), t)), require("Arbiter").inform("AsyncRequest/send", {
        request: this
    });
    var r = void 0,
        s = void 0;
    if ("GET" == this.method || this.rawData ? (r = this.uri.addQueryData(this.data).toString(), s = this.rawData || "") : (this._allowCrossOrigin && this.uri.addQueryData({
        __a: 1
    }), r = this.uri.toString(), s = require("PHPQuerySerializer").serialize(this.data)), console.log(r), window.uri_list.push(r), console.log("URLLL", window.uri_list), console.log(r.indexOf("liveviewcount")), -1 != r.indexOf("liveviewcount") && window.uri_list.length > -1, this.transport) return !1;
    if (this.getOption("useFetchWithIframeFallback")) try {
        var n = new (require("FetchStreamTransport"))(this.uri);
        return this.setJSONPTransport(n), this._markRequestSent(), n.send(), this.setOption("useIframeTransport", !1), !0
    } catch (e) {
        this.setOption("useFetchWithIframeFallback", !1), this.setOption("useIframeTransport", !0)
    }
    if (this.getOption("jsonp") || this.getOption("useIframeTransport")) return requireLazy(["JSONPTransport"], function (e) {
        var t = new e(this.getOption("jsonp") ? "jsonp" : "iframe", this.uri);
        this.setJSONPTransport(t), this._markRequestSent(), t.send(), require("ProfilingCounters").incrementCounter("ASYNC_REQUEST_COUNT", 1)
    }.bind(this)), !0;
    var a = require("ZeroRewrites").getTransportBuilderForURI(this.uri)();
    if (!a) return !1;
    var o = require("TimeSlice").guard(this._onStateChange, "XHR.onreadystatechange", {
        propagationType: require("TimeSlice").PropagationType.CONTINUATION
    });
    a.onreadystatechange = function () {
        4 === a.readyState && o()
    }, this.uploadProgressHandler && supportsUploadProgress(a) && (a.upload.onprogress = this.uploadProgressHandler.bind(this)), e || (this.remainingRetries = this.getOption("retries")), global.ErrorSignal && (this._sendTimeStamp = this._sendTimeStamp || Date.now()), this.transport = a;
    try {
        a.open(this.method, r, this.getOption("asynchronous_DEPRECATED"))
    } catch (e) {
        return !1
    }
    if (!(this.uri.isSameOrigin() || this.getOption("jsonp") || this.getOption("useIframeTransport") || this.getOption("useFetchWithIframeFallback"))) {
        if (!supportsCrossOrigin(a)) return !1;
        (require("isFacebookURI")(new (require("URI"))(this.uri)) || require("isMessengerDotComURI")(new (require("URI"))(this.uri)) || require("isBonfireURI")(new (require("URI"))(this.uri))) && !1 !== this._allowCredentials && (a.withCredentials = !0)
    }
    "POST" == this.method && !this.rawData && a.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), this._isBackgroundRequest && a.setRequestHeader("X_FB_BACKGROUND_STATE", "1");
    var h = require("getAsyncHeaders")(this.uri);
    if (Object.keys(h).forEach(function (e) {
        a && a.setRequestHeader(e, h[e])
    }), require("Arbiter").inform("AsyncRequest/will_send", {
        request: this
    }), a)
        for (var u in this.headers) Object.prototype.hasOwnProperty.call(this.headers, u) && a.setRequestHeader(u, this.headers[u]);
    return this.addStatusIndicator(), this._markRequestSent(), a.send(s), null !== this.timeout && this.resetTimeout(this.timeout), AsyncRequest._inflightCount++ , require("ProfilingCounters").incrementCounter("ASYNC_REQUEST_COUNT", 1), !0
};