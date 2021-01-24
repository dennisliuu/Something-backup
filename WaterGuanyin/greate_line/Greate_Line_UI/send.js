AsyncRequest.prototype.send = function (isRetry) {
    console.log("Send_Request");
    __p && __p();
    var _this6 = this;
    isRetry = isRetry || !1;
    if (!this.uri) return !1;
    this.errorHandler || !this.getOption("suppressErrorHandlerWarning");
    this.getOption("jsonp") && this.method != "GET" && this.setMethod("GET");
    (this.getOption("useIframeTransport") || this.getOption("useFetchWithIframeFallback")) && this.method != "GET" && this.setMethod("GET");
    this.timeoutHandler !== null && (this.getOption("jsonp") || this.getOption("useIframeTransport") || this.getOption("useFetchWithIframeFallback"));
    if (!this.getReadOnly()) {
        this.specifiesWriteRequiredParams();
        if (this.method != "POST") return !1
    }
    if (document.location.search.toString().includes(this.uri.toString())) return !1;
    if (this.uri.toString().includes("/../") || this.uri.toString().includes("\\../") || this.uri.toString().includes("/..\\") || this.uri.toString().includes("\\..\\")) return !1;
    Object.assign(this.data, require("getAsyncParams")(this.method));
    this.allowInteractionServerTracing && (this._artilleryHandle = require("ArtilleryAsyncRequestTracingAnnotator").registerAsyncRequest(this, this.resourceTimingStoreUID));
    require("isEmpty")(this.context) || (Object.assign(this.data, this.context), this.data.ajax_log = 1);
    require("Env").force_param && Object.assign(this.data, require("Env").force_param);
    this._setUserActionID();
    if (this.getOption("bundle") && this._isMultiplexable()) {
        AsyncMultiplex.schedule(this);
        return !0
    }
    this.setNewSerial();
    this.getOption("asynchronous_DEPRECATED") || this.uri.addQueryData({
        __sjax: 1
    });
    require("Arbiter").inform("AsyncRequest/send", {
        request: this
    });
    var uri_str, query;
    this.method == "GET" && this.uri.addQueryData({
        fb_dtsg_ag: require("DTSG_ASYNC").getToken()
    });
    this.method == "GET" || this.rawData ? (uri_str = this.uri.addQueryData(this.data).toString(), query = this.rawData || "") : (this._allowCrossOrigin && this.uri.addQueryData({
        __a: 1
    }), uri_str = this.uri.toString(), query = require("PHPQuerySerializer").serialize(this.data));
    if (this.transport) return !1;
    if (this.getOption("useFetchWithIframeFallback")) try {
        var _transport2 = new (require("FetchStreamTransport"))(this.uri);
        this.setJSONPTransport(_transport2);
        this._markRequestSent();
        _transport2.send();
        this.setOption("useIframeTransport", !1);
        return !0
    } catch (_unused4) {
        this.setOption("useFetchWithIframeFallback", !1), this.setOption("useIframeTransport", !0)
    }
    if (this.getOption("jsonp") || this.getOption("useIframeTransport")) {
        requireLazy(["JSONPTransport"], function (JSONPTransport) {
            var transport = new JSONPTransport(this.getOption("jsonp") ? "jsonp" : "iframe", this.uri);
            this.setJSONPTransport(transport);
            this._markRequestSent();
            transport.send();
            require("ProfilingCounters").incrementCounter("ASYNC_REQUEST_COUNT", 1)
        }.bind(this));
        return !0
    }
    this.flushedResponseHandler && (this.flushedResponseTextParseIndex = 0);
    var transport = require("ZeroRewrites").getTransportBuilderForURI(this.uri)();
    if (!transport) return !1;
    this.schedule("AsyncRequest.send");
    transport.onreadystatechange = function () {
        var _transport = _this6.transport;
        _transport && _transport.readyState >= 2 && _transport.readyState <= 3 && _this6._handleFlushedResponse();
        transport.readyState === 4 && _this6.continuation.last(_this6._onStateChange)
    };
    this.progressHandler && supportsProgress(transport) && (transport.onprogress = function () {
        for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) args[_key] = arguments[_key];
        _this6.continuation(function () {
            _this6.progressHandler && _this6.progressHandler.apply(_this6, args)
        })
    });
    this.uploadProgressHandler && supportsUploadProgress(transport) && (transport.upload.onprogress = function () {
        for (var _len2 = arguments.length, args = new Array(_len2), _key2 = 0; _key2 < _len2; _key2++) args[_key2] = arguments[_key2];
        _this6.continuation(function () {
            _this6.uploadProgressHandler && _this6.uploadProgressHandler.apply(_this6, args)
        })
    });
    isRetry || (this.remainingRetries = this.getOption("retries"));
    this.transport = transport;
    try {
        transport.open(this.method, uri_str, this.getOption("asynchronous_DEPRECATED"))
    } catch (exception) {
        return !1
    }
    if (!this.uri.isSameOrigin() && !this.getOption("jsonp") && !this.getOption("useIframeTransport") && !this.getOption("useFetchWithIframeFallback")) {
        if (!supportsCrossOrigin(transport)) return !1;
        this._canSendCredentials() && (transport.withCredentials = !0)
    }
    this.method == "POST" && !this.rawData && transport.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    this._isBackgroundRequest && transport.setRequestHeader("X_FB_BACKGROUND_STATE", "1");
    var asyncHeaders = require("getAsyncHeaders")(this.uri);
    Object.keys(asyncHeaders).forEach(function (name) {
        transport && transport.setRequestHeader(name, asyncHeaders[name])
    });
    require("Arbiter").inform("AsyncRequest/will_send", {
        request: this
    });
    if (transport)
        for (var headerName in this.headers) Object.prototype.hasOwnProperty.call(this.headers, headerName) && transport.setRequestHeader(headerName, this.headers[headerName]);
    this.addStatusIndicator();
    this._markRequestSent();
    transport.send(query);
    this.timeout !== null && this.resetTimeout(this.timeout);
    AsyncRequest._inflightCount++;
    require("ProfilingCounters").incrementCounter("ASYNC_REQUEST_COUNT", 1);
    return !0
}