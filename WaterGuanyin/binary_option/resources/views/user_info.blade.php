@extends("front_layouts")
@section("content")
<div class="content-container">
    <div class="page dashboard">
        <nav class="tabs">
            <a class="tab active" href="/user">個人資料</a>
            <a class="tab" href="/user/deals">交易日誌</a>
            <a class="tab" href="/user/edit">編輯個人資料</a>
            <a class="tab" href="/user/session">可用時段</a>
        </nav>
        <div class="tiles">
            <div class="vertical-scroll" style="height: calc(100% - 55px);">
                <div class="custom-scrollbar active"><div class="custom-scroll-handle" style="height: 380.358px; transform: translateY(0px);">
                        <div class="inner-handle"></div>
                    </div>
                </div>
                <div class="inner-scroll-container">
                    <div>
                        <div class="tile tile-user">
                            <a class="edit-user-info-avatar" href="/user/edit"><span class="avatar">
                                    <i class="pad"></i>
                                    <i class="image dummy" style="border-color: rgb(216, 63, 63);"></i></span>
                            </a>
                            <div class="username">
                                <span parametr="310487161" class="copy">310-487-161</span>
                            </div>
                            <div class="balance drop-balance">
                                <span class="handle">
                                    <span class="money undefined money-big">
                                        <i class="currency">$</i>0
                                    </span><i class="arrow"></i>
                                </span>
                            </div>
                            <div class="progress">
                                <div class="bar">
                                    <div class="animated-item user-status-indicator">
                                        <div class="si-inner">
                                            <div class="si-labels">
                                                <span class=""><i>Basic</i></span>
                                                <span class=""><i>Silver</i></span>
                                                <span class=""><i>Gold</i></span>
                                                <span class=""><i>Platinum</i></span>
                                                <span class=""><i>Exclusive</i></span>
                                            </div>
                                            <div class="si-bar">
                                                <div class="real" style="width: 0%; background-color: rgb(216, 63, 63);">
                                                    <i style="background-color: rgb(216, 63, 63);"></i>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="tile tile-personal-info">
                            <h2>個人資料</h2>
                            <div class="list">
                                <div class="item email">@if(Auth::user()){{Auth::user()->email}}@endif</div>
                                <div class="item id">
                                    <span parametr="310487161" class="copy">310-487-161</span>
                                </div>
                                <div class="item country">
                                    Taiwan
                                </div>
                            </div>
                        </div>
                        <div class="tile tile-assets-chart">
                            <h2>資產圖表</h2>
                            <div class="analytics-empty">
                                <div class="animated-item analytics-empty-text">
                                    <span>資產圖表顯示您交易過的資產</span>
                                </div>
                                <a class="btn btn-primary animated-item" href="/">交易</a>
                            </div>
                        </div>
                        <div class="tile tile-banner-eof">
                            <div class="banner-eof">
                                <span class="close"></span>
                                <div class="btc-logo">

                                </div>
                                <div class="title">Buy Crypto</div>
                                <div class="desc">with your credit or debit card</div>
                                <a class="button" href="https://eo.finance/?refid=expertoption&amp;tr=web" target="_blank">Buy Crypto</a>
                            </div>
                        </div>
                        <div class="tile tile-trading-journal">
                            <h2>交易日誌</h2>
                            <a class="next-link" href="/user/deals">更多</a>
                            <div class="analytics-empty">
                                <div class="animated-item analytics-empty-text">
                                    <span>你的交易記錄會在這裡顯示</span>
                                </div>
                                <a class="btn btn-primary animated-item" href="/">交易</a>
                            </div>
                        </div>
                        <div class="tile tile-profile-analytics">
                            <h2>交易量<div class="ui-tooltip">
                                    <div class="tooltip-splash pos-top" style="width: 250px; top: 0px; left: 0px;">
                                        交易量為所有交易的總和。例如您完成了 100 次 $10 的交易，您的交易量就是 $1000。
                                    </div>
                                    <div class="analytics-info-click icons icon-question">

                                    </div>
                                </div>
                            </h2>
                            <div class="selector-period"></div>
                            <div class="analytics-empty">
                                <div class="animated-item analytics-empty-text">
                                    <span>您的每日交易量會在這裡顯示</span>
                                </div>
                                <a class="btn btn-primary animated-item" href="/">交易</a>
                            </div>
                            <div class="chart-period month animated-item">

                            </div>
                            <div class="info animated-item">
                                <div class="item animated-item">
                                    <div class="value">0%</div>
                                    <div class="desc">勝出交易</div>
                                </div>
                                <div class="item animated-item">
                                    <div class="value">
                                        <span class="money undefined money-big"><i class="currency">$</i>0</span>
                                    </div>
                                    <div class="desc">
                                        交易量
                                    </div>
                                </div>
                                <div class="item animated-item">
                                    <div class="value">0</div>
                                    <div class="desc">交易</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection