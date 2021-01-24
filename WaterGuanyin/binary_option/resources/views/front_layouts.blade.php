<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>二元期權</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" />
    <link rel="stylesheet" href="{{asset('css/home.css')}}" />
    <link rel="stylesheet" href="{{asset('css/ogg.css')}}" />

    <link rel="stylesheet" href="{{asset('css/animate.css')}}" />
    @yield('style')
    <script type="text/javascript" src="https://v2.zopim.com/w?3GWVlz4YyqBQb8oIzky6JCjyL0eTo3MA"></script>
    <script type="text/javascript" src="{{asset('js/vendors-chart.js')}}"></script>
    <script type="text/javascript" src="{{asset('js/chart.js')}}"></script>
    <!-- Fix for iOS Safari zooming bug -->
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />

</head>
<body>
<main id="app">
    <div class="app ready drawer-closed">
        <div class="app-container">
        <div>@yield('modal')</div>
        <div class="notifications-global" id="notifications-global"></div>
            @include("front_headers")
            @include("front_menu")
            @include("front_right_menu")
            @yield('content')
        </div>
    </div>
</main>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
</script>
<script async="" charset="utf-8" src="https://v2.zopim.com/?3GWVlz4YyqBQb8oIzky6JCjyL0eTo3MA" type="text/javascript"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
<script src="https://v2.zopim.com/bin/v/widget_v2.319.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="{{asset('js/jquery-min.js')}}" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript" src="{{asset('charting_library/charting_library.min.js')}}"></script>
<script src="{{asset('js/dataUpdater.js')}}" type="text/javascript" charset="utf-8"></script>
<script src="{{asset('js/datafees.js')}}" type="text/javascript" charset="utf-8"></script>
<script src="{{asset('js/socket.js')}}" type="text/javascript" charset="utf-8"></script>
<script src="{{asset('js/TVjsApi.js')}}" type="text/javascript" charset="utf-8"></script>
<script src="{{asset('js/runtime.js')}}" type="text/javascript" charset="utf-8"></script>
<script src="{{asset('js/vendors.js')}}" type="text/javascript" charset="utf-8"></script>
<script src="{{asset('js/calc.js')}}" type="text/javascript" charset="utf-8"></script>
{{--<script src="{{asset('js/app_expert.js')}}" type="text/javascript" charset="utf-8"></script>--}}
@yield('scripts')
</body>
</html>