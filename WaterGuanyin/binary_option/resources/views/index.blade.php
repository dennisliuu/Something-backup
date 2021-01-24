<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>二元期權</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" />
    <link rel="stylesheet" href="{{asset('/css/ogg.css')}}" />
    <link rel="stylesheet" href="{{asset('/css/project.css')}}" />
    <link rel="stylesheet" href="{{asset('/css/main.css')}}" />

    <link rel="stylesheet" href="/css/animate.css" />
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

    <!-- Fix for iOS Safari zooming bug -->
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />

    <script src="./js/jquery-min.js" type="text/javascript" charset="utf-8"></script>
    <script type="text/javascript" src="charting_library/charting_library.min.js"></script>
    <script src="./js/dataUpdater.js" type="text/javascript" charset="utf-8"></script>
    <script src="./js/datafees.js" type="text/javascript" charset="utf-8"></script>
    <script src="./js/socket.js" type="text/javascript" charset="utf-8"></script>
    <script src="./js/TVjsApi.js" type="text/javascript" charset="utf-8"></script>
    {{-- <script src="{{asset('')}}" type="text/javascript" charset="utf-8"></script> --}}
</head>

<body>
    {{-- <header class="header"><a class="logo" href="/"></a>
    <div class="header-block left">
      <div class="header-item language">
        <div class="select-locale">
          <div class="dropdown">
            <div class="current"><img class="flag-icon"
                src="https://static.expertoption.com/flags/2.0/png-optimized/cn.png" width="23" height="15"><span
                class="title">繁體中文</span></div>
            <div class="list">
              <div class="col">
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/gb.png" width="23" height="15"><span
                    class="title">English</span></div>
                <div class="item active"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/cn.png" width="23" height="15"><span
                    class="title">繁體中文</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/cn.png" width="23" height="15"><span
                    class="title">简体中文</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/th.png" width="23" height="15"><span
                    class="title">ภาษาไทย</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/in.png" width="23" height="15"><span
                    class="title">हिन्दी</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/kr.png" width="23" height="15"><span
                    class="title">한국어</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/vn.png" width="23" height="15"><span
                    class="title">Tiếng Việt</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/sa.png" width="23" height="15"><span
                    class="title">العربية</span></div>
              </div>
              <div class="col">
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/tr.png" width="23" height="15"><span
                    class="title">Türkçe</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/my.png" width="23" height="15"><span
                    class="title">Bahasa Malaysia</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/id.png" width="23" height="15"><span
                    class="title">Bahasa Indonesia</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/tl.png" width="23" height="15"><span
                    class="title">Tagalog</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/es.png" width="23" height="15"><span
                    class="title">Español</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/pt.png" width="23" height="15"><span
                    class="title">Portuguese</span></div>
                <div class="item"><img class="flag-icon"
                    src="https://static.expertoption.com/flags/2.0/png-optimized/ru.png" width="23" height="15"><span
                    class="title">Русский</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="header-item nav">
        <nav class="header-nav"><a href="#" title="全螢幕" class="fullscreen"></a><a
            href="https://eo.finance?refid=expertoption&amp;tr=web" title="EO.Finance" target="_blank"
            class="outer"><span
              style="background-image: url(&quot;https://static.expertoption.com/app/nav/icons/eof-hover.png&quot;);"></span></a><a
            href="#" title="如何交易" class="info"></a><a href="#" title="音效" class="sound active"></a><a href="#"
            title="即時聊天" class="support">即時聊天</a></nav>
      </div>
    </div>
    <div class="header-block right">
      <div class="header-item user">
        <div class="user-block-header"><a class="username" href="/user"><span class="avatar"><i class="image dummy"
                style="border-color: rgb(216, 63, 63);"></i></span><span class="name">507-023-752</span></a>
          <div class="balance">
            <div class="drop-balance">
              <div class="current-demo"><span>
                  <div class="animating-balance-width" style="width: 63px;"><span
                      class="money undefined money-medium"><i class="currency">$</i>88,888</span></div>
                </span></div>
            </div>
          </div>
          <div class="deposit"><a class="btn btn-primary btn-success" href="/billing">開啟 真實帳戶</a></div>
        </div>
      </div>
    </div><span class="toggler hamburger"><span></span></span>
  </header> --}}
    <header class="header animated main_header">
        <div class="limiter">
            <div class="language">
                <div class="dropdown">
                    <div class="current"><i class="flag-icon flag-icon-zh-Hant"></i></div>
                    <div class="list">
                        <div class="contents"><a
                                href="https://expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-en"></i><!-- react-text: 36 -->English
                                <!-- /react-text --></a><a
                                href="https://hi.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-hi"></i><!-- react-text: 39 -->हिन्दी
                                <!-- /react-text --></a><a
                                href="https://zh-CN.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-zh-Hans"></i><!-- react-text: 42 -->简体中文
                                <!-- /react-text --></a><a
                                href="https://id.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-id"></i><!-- react-text: 45 -->Bahasa
                                Indonesia
                                <!-- /react-text --></a><a
                                href="https://zh-TW.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item active"><i class="flag-icon flag-icon-zh-Hant"></i>
                                <!-- react-text: 48 -->繁體中文
                                <!-- /react-text --></a><a
                                href="https://ms.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-ms"></i><!-- react-text: 51 -->Bahasa
                                Malaysia
                                <!-- /react-text --></a><a
                                href="https://th.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-th"></i><!-- react-text: 54 -->ภาษาไทย
                                <!-- /react-text --></a><a
                                href="https://pt.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-pt"></i><!-- react-text: 57 -->Portuguese
                                <!-- /react-text --></a><a
                                href="https://ko.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-ko"></i><!-- react-text: 60 -->한국어
                                <!-- /react-text --></a><a
                                href="https://es.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-es"></i><!-- react-text: 63 -->Español
                                <!-- /react-text --></a><a
                                href="https://vi.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-vi"></i><!-- react-text: 66 -->Tiếng Việt
                                <!-- /react-text --></a><a
                                href="https://ru.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-ru"></i><!-- react-text: 69 -->Русский
                                <!-- /react-text --></a><a
                                href="https://ar.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-ar"></i><!-- react-text: 72 -->العربية
                                <!-- /react-text --></a><a
                                href="https://fil.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-fil"></i><!-- react-text: 75 -->Tagalog
                                <!-- /react-text --></a><a
                                href="https://tr.expertoption.money?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"
                                class="item"><i class="flag-icon flag-icon-tr"></i><!-- react-text: 78 -->Türkçe
                                <!-- /react-text --></a></div>
                    </div>
                </div>
            </div><a href="#" class="online-chat"><span>在線諮詢</span></a><a class="logo"
                href="/?_ga_ab_group=0&amp;_fbp=fb.1.1575980084297.580812018"></a>
            <div class="user"><a
                    href="/login"
                    class="button text">登錄</a><a
                    href="/register"
                    class="button frame">真實賬戶</a></div>
        </div>
    </header>
    {{-- <aside class="aside-left"><nav class="nav-main"><a class="traderoom active" href="/"><i></i><span>交易</span></a><a class="deposit" href="/billing"><i></i><span>財政</span></a><a class="dashboard" href="/user"><i></i><span>個人資料</span></a><a class="multiplatform" href="/platforms"><i></i><span>應用程式</span></a><a class="analytics" href="/analytics"><i></i><span>分析</span></a><a class="news" href="/education"><i></i><span>教育</span></a><a class="info" href="/info"><i></i><span>協助</span></a></nav><a class="config" href="#" title="設定"></a><a class="exit" href="#" title="退出"></a></aside> --}}

    <div class="container-fluid">


        <div style="width:100%;margin-top:13vh;">
            <div class="home-hero">
                <div class="limiter">
                    <h1 class="heading"><span>快速&nbsp;<i class="dot"></i>&nbsp;網上&nbsp;交易</span></h1><a
                        href="/sample"
                        class="button fill big">
                        <!-- react-text: 93 -->試用免費模擬賬戶
                        <!-- /react-text --><i class="arrow"></i></a>
                </div>
            </div>
        </div>
        <div style="width:100%;position: absolute;margin-top: 11vh;">
            <div class="limiter">
                <div class="home-platform">
                    <h2 class="heading">如何使用？</h2>
                    <div class="cols">
                        <div class="col">
                            <div class="content">
                                <h2 class="title first">入金</h2>
                                <div class="text">開設真實賬戶，充入資金。我們有20多種支付系統任您選擇。</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="content">
                                <h2 class="title second">營業</h2>
                                <div class="text">100種資產和股票供您選擇。使用技術分析和貿易新聞</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="content">
                                <h2 class="title third">提現</h2>
                                <div class="text">輕鬆把資金提現到您的銀行卡或電子錢包。我們不承認佣金。</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div id="chart_con">
            <canvas id="myChart"></canvas>
        </div>

        {{-- <div class="btn_area">
      <button type="button" class="buy_button btn btn-danger" @click="add_bet('buy',100)">做多100元</button>
      <button type="button" class="sell_button btn btn-success" @click="add_bet('sell',100)">做空100元</button>

    </div> --}}
        <div class="deal-controller" data-deal-controller="1575466791617" style="margin-bottom: 0px;">
            <div class="holder">
                <div class="slider upper">
                    <div class="current-deal">
                        <div class="block amount no-swipe">
                            <div class="title">金額</div>
                            <div class="amount-input"><span class="input-btn minus">−</span><span
                                    class="input currency-once"><i>$</i><input pattern="^((?!(0))[0-9]+)$"
                                        inputmode="decimal" value="45"></span><span class="input-btn plus">+</span>
                            </div>
                        </div>
                        <div class="block amount no-swipe strike-select">
                            <div class="title">行使價比率</div>
                            <div class="amount-input"><span class="input-btn minus down"></span><span
                                    class="input currency-once">1.106297</span><span class="input-btn plus up"></span>
                            </div>
                        </div>
                        <div class="block deal no-swipe">
                            <div class="put-side">
                                <div class="amount-data"><span class="money undefined money-big"><i
                                            class="currency">$</i>0.00</span></div>
                                <div class="deal-button put">12%</div>
                            </div>
                            <div class="call-side">
                                <div class="amount-data"><span class="money undefined money-big"><i
                                            class="currency">$</i>0.00</span></div>
                                <div class="deal-button call">99%</div>
                            </div>
                        </div>
                    </div>
                    <div class="new-deal">
                        <div class="block profit">
                            <div class="title">利潤</div><span class="money value money-big"><i
                                    class="currency">$</i>0</span>
                        </div>
                        <div class="block timer">
                            <div class="title">到期時間</div>
                            <div class="value big">00:00</div>
                        </div>
                        <div class="block new"><i>+</i> 新選擇</div>
                    </div>
                </div>
            </div>
        </div>

    </div>
    {{-- <hr /> --}}
    {{-- <ul class="list-group list-group-horizontal">
      <li class="list-group-item">目前賽局：@{{work_hash}}</li>
    <li class="list-group-item">現在價格：@{{now_price}}</li>
    <li class="list-group-item">@{{af_time}}秒後結束</li>

    </ul>
    <ul class="list-group list-group-horizontal">

        <li class="list-group-item">總資產：@{{balance}}</li>
        <li class="list-group-item">盈利狀況：@{{pofit}}</li>
    </ul> --}}

    {{-- <table class="table">
      <thead>
        <tr>
          <th scope="col">投資時間</th>
          <th scope="col">方向</th>
          <th scope="col">標的價格</th>
          <th scope="col">金額</th>

        </tr>
      </thead>
      <tbody class="buy_tr">
        <tr v-for="item in buyer_list" :class="item['type']">
          <th scope="row">@{{item["time"]}}</th>
    <td>@{{item['type']}}</td>
    <td>@{{item['buy_price']}}</td>
    <td>@{{item['money']}}</td>
    </tr>

    </tbody>
    </table> --}}

    <!-- Modal -->
</body>
<script src="./js/calc.js"></script>
<script type="text/javascript">
    $(document).ready(function () {
        var _TVjsApi = new TVjsApi("btcusdt");

    });

</script>


</html>
