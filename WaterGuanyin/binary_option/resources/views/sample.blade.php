@extends("front_layouts")
@section('modal')
<div id="sample" class="modals-container-default show modals-container modal-animation-enter-done">
  <div class="modal modal-container-asset-selector zh-hant" style="width: 570px; margin-left: -285px;display: block;height: 50%;">
    <div class="asset-selector-modal">
      <div class="head">
        <h1 id="currency_name" class="title">
          <i class="icon animate-in" style="background-image: url('https://static.expertoption.com/asset-icons/png/EURUSD@2x.png');">
          </i>EUR/USD</h1>
        <span class="close"></span>
      </div>
      <div class="body">
        <div class="group-selector">
          <div data-id="0" class="item active">
            <i class="icon" style="background-image: url('https://static.expertoption.com/asset-group-icons/png/0@2x.png');"></i>
            <span class="name">全部</span>
          </div>
          <div data-id="4" class="item"><i class="icon" style="background-image: url('https://static.expertoption.com/asset-group-icons/png/4@2x.png');"></i>
            <span class="name">貨幣</span>
          </div>
          <div data-id="5" class="item">
            <i class="icon" style="background-image: url('https://static.expertoption.com/asset-group-icons/png/5@2x.png');"></i>
            <span class="name">加密貨幣</span>
          </div>
          <div data-id="2" class="item">
            <i class="icon" style="background-image: url('https://static.expertoption.com/asset-group-icons/png/2@2x.png');"></i>
            <span class="name">股票</span>
          </div>
          <div data-id="3" class="item">
            <i class="icon" style="background-image: url('https://static.expertoption.com/asset-group-icons/png/3@2x.png');"></i>
            <span class="name">貨品</span>
          </div>
        </div>
        <div class="assets-list">
          <div class="search">
            <form class="select-group form search-form">
              <input placeholder="搜尋" class="controls" value=""><i class="clear hide"></i>
            </form>
          </div>
          <div style="position: relative; overflow: hidden; width: 282px; height: 345px; will-change: transform; direction: ltr;">
            <div class="scrollbars-view" style="position: absolute; top: 0px; left: 0px; right: 0px; bottom: 0px; overflow: scroll; margin-right: -20px; margin-bottom: -20px; padding-right: 20px; padding-bottom: 20px;">
              <div style="height: 4140px; width: 100%;">
                <div id="tables" data-to="179" class="item" style="position: absolute; left: 0px; top: 0px; height: 60px; width: 100%;">
                  <div onclick="change_sym('https\:\/\/static.expertoption.com/asset-icons/png/EURUSD@2x.png', 'EUR/USD')" class="item__inner">
                    <i class="icon" style="background-image: url('https://static.expertoption.com/asset-icons/png/EURUSD@2x.png');"></i>
                    <div class="left">
                      <div class="name major">EUR/USD</div>
                      <div class="group minor">貨幣</div>
                    </div>
                    <div class="right">
                    </div>
                  </div>
                </div>
                <!-- @foreach($data as $key => $item)
              @if($loop->first)
                <div class="scrollbars-view" style="position: absolute; top: 0px; left: 0px; right: 0px; bottom: 0px; overflow: scroll; margin-right: -20px; margin-bottom: -20px; padding-right: 20px; padding-bottom: 20px;">
                  <div style="height: 4140px; width: 100%;">
                    <div data-to="179" class="item" style="position: absolute; left: 0px; top: 0px; height: 60px; width: 100%;">
                      <div class="item__inner">
                        <i class="icon" style="background-image: url('{{$item->image}}');"></i>
                        <div class="left"><div class="name major">{{$item->name}}</div>
                          <div class="group minor">{{$item->type}}</div>
                        </div>
                        <div class="right">
                          <div class="profit major">{{$item->percentage}}%</div>
                          <div class="changes minor">{{$item->upsdowns}}%</div>
                        </div>
                      </div>
                    </div>
              @else
                  <div data-to="172" class="item" style="position: absolute; left: 0px; top: {{ 60 * ($key) }}px; height: 60px; width: 100%;">
                    <div class="item__inner">
                      <i class="icon" style="background-image: url('{{$item->image}}');"></i>
                      <div class="left">
                        <div class="name major">{{$item->name}}</div>
                        <div class="group minor">{{$item->type}}</div>
                      </div>
                      <div class="right">
                        <div class="profit major">{{$item->percentage}}%</div>
                        <div class="changes minor">{{$item->upsdowns}}%</div>
                      </div>
                    </div>
                  </div>
              @endif
            @endforeach -->
              </div>
            </div>
            <div style="position: absolute; height: 6px; right: 2px; bottom: 2px; left: 2px; border-radius: 3px;">
              <div style="position: relative; display: block; height: 100%; cursor: pointer; border-radius: inherit; background-color: rgba(0, 0, 0, 0.2); width: 0px;">

              </div>
            </div>
            <div class="scrollbars-track" style="position: absolute; width: 6px;">
              <div class="scrollbars-thumb" style="position: relative; display: block; width: 100%; height: 30px; transform: translateY(0px);">

              </div>
            </div>
          </div>
        </div>
        <div class="exptimes-list">
          <div class="exptimes-container">
            <div data-id="Sun Dec 15 2019 15:56:00 GMT+0800 (台北標準時間)" class="item active">
              <div class="major">1 分钟</div>
              <div class="minor">下午03:56:00
              </div>
            </div>
          </div>
          <div class="save" style="box-sizing: border-box; padding: 0 20px 0 10px; position: absolute; bottom: 100px;">
            <a id="application" href="#" class="btn btn-primary">應用</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
@endsection
@section("content")
<div class="content-container">
  <div class="chart-settings">
    <div class="settings-button long asset-selector"><span class="button-content"><span id="currency_title" class="title">EUR/USD (OTC)</span><span class="divider"> </span><span id="currency_exptime" class="exptime">下午01:43:00</span></span></div>
    <div class="settings-button charts-selector area"></div>
    <div class="settings-button indicators-selector"></div>
    <div class="settings-button buildings-selector"></div>
    <div class="settings-button crosshair enabled" title="圖表十字線"></div>
    <div class="settings-button social-toggler enabled"></div>
    <div class="settings-button lay-selector"></div>
  </div>
  <div class="page traderoom">
    <div>
      <div class="charts single">
        <div id="chart_con" class="chart" style="width: 100%; height: 100%; left: 0px; top: 0px;">
          <canvas id="myChart"></canvas>
        </div>
        <div id="infomation">
          <div class="btn_area">
            {{-- <button type="button" class="buy_button btn btn-danger" @click="add_bet('buy',100)">做多100元</button>--}}
            {{-- <button type="button" class="sell_button btn btn-success" @click="add_bet('sell',100)">做空100元</button>--}}
            <div class="deal-controller" data-deal-controller="1576299830518" style="margin-bottom: 0px;">
              <div class="holder">
                <div class="slider upper">
                  <div class="current-deal">
                    <div class="block amount no-swipe">
                      <div class="title">金額</div>
                      <div class="amount-input">
                        <span class="input-btn minus">−</span>
                        <span class="input currency-once"><i>$</i>
                          <input pattern="^((?!(0))[0-9]+)$" inputmode="decimal" value="50">
                        </span>
                        <span class="input-btn plus">+</span>
                      </div>
                    </div>
                    <div class="block amount no-swipe strike-select">
                      <div class="title">行使價比率</div>
                      <div class="amount-input">
                        <span class="input-btn minus down"></span>
                        <span class="input currency-once">1.117585</span>
                        <span class="input-btn plus up"></span>
                      </div>
                    </div>
                    <div class="block deal no-swipe">
                      <div class="put-side">
                        <div class="amount-data">
                          <span class="money undefined money-big"><i class="currency">$</i>0.00</span>
                        </div>
                        <div class="deal-button put" @click="add_bet('buy',100)">81%</div>
                      </div>
                      <div class="call-side">
                        <div class="amount-data">
                          <span class="money undefined money-big">
                            <i class="currency">$</i>0.00</span>
                        </div>
                        <div class="deal-button call" @click="add_bet('sell',100)">81%</div>
                      </div>
                    </div>
                  </div>
                  <div class="new-deal">
                    <div class="block profit">
                      <div class="title">利潤</div>
                      <span class="money value money-big">
                        <i class="currency">$</i>0
                      </span>
                    </div>
                    <div class="block timer">
                      <div class="title">到期時間</div>
                      <div class="value big">00:00</div>
                    </div>
                    <div class="block new"><i>+</i> 新選擇
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {{-- <hr />--}}
          {{-- <ul class="list-group list-group-horizontal">--}}
          {{-- <li class="list-group-item">目前賽局：@{{work_hash}}</li>--}}
          {{-- <li class="list-group-item">現在價格：@{{now_price}}</li>--}}
          {{-- <li class="list-group-item">@{{af_time}}秒後結束</li>--}}

          {{-- </ul>--}}
          {{-- <ul class="list-group list-group-horizontal">--}}

          {{-- <li class="list-group-item">總資產：@{{balance}}</li>--}}
          {{-- <li class="list-group-item">盈利狀況：@{{pofit}}</li>--}}
          {{-- </ul>--}}

          {{-- <table class="table">--}}
          {{-- <thead>--}}
          {{-- <tr>--}}
          {{-- <th scope="col">投資時間</th>--}}
          {{-- <th scope="col">方向</th>--}}
          {{-- <th scope="col">標的價格</th>--}}
          {{-- <th scope="col">金額</th>--}}

          {{-- </tr>--}}
          {{-- </thead>--}}
          {{-- <tbody class="buy_tr">--}}
          {{-- <tr v-for="item in buyer_list" :class="item['type']">--}}
          {{-- <th scope="row">@{{item["time"]}}</th>--}}
          {{-- <td>@{{item['type']}}</td>--}}
          {{-- <td>@{{item['buy_price']}}</td>--}}
          {{-- <td>@{{item['money']}}</td>--}}
          {{-- </tr>--}}

          {{-- </tbody>--}}
          {{-- </table>--}}

        </div>
      </div>
    </div>
  </div>
</div>
<!-- Modal -->
@endsection
@section("scripts")
<script type="text/javascript">
  var _TVjsApi = new TVjsApi("btcusdt");

  $(document).ready(function() {
    document.querySelector("#currency_exptime").innerText = new Date()
    $('div.modal-animation-enter-done').hide()
    var currency = ["USD/JPY", "GBP/USD", "USD/CAD", "USD/CHF", "AUD/USD", "NZD/USD", "EUR/GBP", "EUR/CHF", "EUR/CAD", "EUR/AUD", "EUR/JPY", "GBP/JPY", "CHF/JPY", "CAD/JPY", "AUD/JPY", "GBP/CHF", "GBP/AUD"]
    document.querySelector("#tables").innerHTML = `<div onclick="change_sym('https\:\/\/static.expertoption.com/asset-icons/png/EURUSD@2x.png', 'EUR/USD')" class="item__inner"> <i class="icon" style="background-image: url('https://static.expertoption.com/asset-icons/png/EURUSD@2x.png');"></i> <div class="left"> <div class="name major">EUR/USD</div> <div class="group minor">貨幣</div> </div> <div class="right"> </div> </div>`
    for (let i = 0; i < currency.length; i++) {
      document.querySelector("#tables").innerHTML += `<div onclick="change_sym('https\:\/\/static.expertoption.com/asset-icons/png/${currency[i].slice(0,3) + currency[i].slice(4,7)}@2x.png', '${currency[i]}')" class="item__inner"> <i class="icon" style="background-image: url('https\:\/\/static.expertoption.com/asset-icons/png/${currency[i].slice(0,3) + currency[i].slice(4,7)}@2x.png');"></i> <div class="left"> <div class="name major">${currency[i]}</div> <div class="group minor">貨幣</div> </div> <div class="right"> </div> </div>`
    }

  });

  $("div.asset-selector").click(function() {
    $('div.modal-animation-enter-done').show()
  });
  $("span.close").click(function() {
    $('div.modal-animation-enter-done').hide()
  });

  $("div.save").click(function() {
    $('div.modal-animation-enter-done').hide()
  });

  $('#application').click(function() {
    $('#sample').hide()
  })

  function change_sym(url, name) {
    // _TVjsApi.unSubscribe(999)
    // var _TVjsApi = new TVjsApi(name)
    document.querySelector("#currency_name").innerHTML = `<i class="icon animate-in" style="background-image: url(${url});"></i>${name}`
    document.querySelector("#currency_title").innerText = name
    let time1 = new Date()
    document.querySelector("#currency_exptime").innerText = time1

  }
</script>
@endsection