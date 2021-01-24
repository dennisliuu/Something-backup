@extends("front_layouts")
@section("content")
<div class="content-container">
    <div class="page edit-profile-page">
        <nav class="tabs">
            <a class="tab" href="/user-info">個人資料</a>
            <a class="tab" href="/user/deals">交易日誌</a>
            <a class="tab active" href="/user/edit">編輯個人資料</a>
            <a class="tab" href="/user/session">可用時段</a>
        </nav>
        <div class="edit-profile">
            <div class="vertical-scroll" style="height: calc(100% - 55px);">
                <div class="custom-scrollbar">
                    <div class="custom-scroll-handle" style="height: 1506.56px; transform: translateY(0px);">
                        <div class="inner-handle">

                        </div>
                    </div>
                </div>
                <div class="inner-scroll-container">
                    <div>
                        <div class="content">
                            <div class="user-info animated-item">
                                <div class="name">
                                    <i class="mark"></i>
                                    @if(Auth::user()){{Auth::user()->name}}@endif
                                </div>
                                <div class="id">戶口 # 310-487-161</div>
                            </div>
                            <div class="cols">
                                <div class="col animated-item">
                                    <h2>地址</h2>
                                    <form class="" name="">
                                        <div class="form-message error small-bottom">

                                        </div>
                                        <div class="form-row"><label>國家<i class="mark"></i></label>
                                            <input type="text" class="controls" disabled="" value="Taiwan">
                                        </div>
                                        <div class="form-row">
                                            <div class="form-col col-2-3">
                                                <label>城市</label>
                                                <input name="city" type="text" class="controls valid" value=""></div>
                                            <div class="form-col col-1-3">
                                                <label>郵政編碼</label>
                                                <input name="zip" type="text" class="controls valid" value="">
                                            </div>
                                        </div>
                                        <div class="form-row">
                                            <label>街道</label>
                                            <input name="address" type="text" class="controls valid" value="">
                                        </div>
                                    </form>
                                </div>
                                <div class="col animated-item">
                                    <h2>個人資料</h2>
                                    <form class="" name="">
                                        <div class="form-message error small-bottom"></div>
                                        <div class="form-row"><label>性別</label><div class="form-col">
                                                <div class="ui-form-select"><div class="dropdown">
                                                        <div class="current"></div>
                                                        <input type="text" readonly="" class="controls current-position" value="性別">
                                                        <div class="sel-dropdown" style="height: 115px;">
                                                            <div class="vertical-scroll" style="height: calc(100% - 0px);">
                                                                <div class="custom-scrollbar">
                                                                    <div class="custom-scroll-handle" style="height: 38px; transform: translateY(0px);">
                                                                        <div class="inner-handle">

                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="inner-scroll-container">
                                                                    <div><div class="items">
                                                                            <div class="item active" data-id="0">
                                                                                <span class="value">性別</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="1">
                                                                                <span class="value">男</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="2">
                                                                                <span class="value">女</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="empty">Empty...</div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="form-row">
                                            <label>出生日期</label>
                                            <div class="form-col col-1-3">
                                                <div class="ui-form-select">
                                                    <div class="dropdown">
                                                        <div class="current">

                                                        </div>
                                                        <input type="text" readonly="" class="controls current-position" value="">
                                                        <div class="sel-dropdown" style="height: 191px;">
                                                            <div class="vertical-scroll" style="height: calc(100% - 0px);">
                                                                <div class="custom-scrollbar">
                                                                    <div class="custom-scroll-handle" style="height: 38px; transform: translateY(0px);">
                                                                        <div class="inner-handle"></div>
                                                                    </div>
                                                                </div>
                                                                <div class="inner-scroll-container">
                                                                    <div>
                                                                        <div class="items">
                                                                            <div class="item" data-id="1">
                                                                                <span class="value">1</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="2">
                                                                                <span class="value">2</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="3">
                                                                                <span class="value">3</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="4">
                                                                                <span class="value">4</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="5">
                                                                                <span class="value">5</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="6">
                                                                                <span class="value">6</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="7">
                                                                                <span class="value">7</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="8">
                                                                                <span class="value">8</span>
                                                                                <span class="postfix"></span>
                                                                            </div>
                                                                            <div class="item" data-id="9">
                                                                                <span class="value">9</span><span class="postfix"></span></div><div class="item" data-id="10"><span class="value">10</span><span class="postfix"></span></div><div class="item" data-id="11"><span class="value">11</span><span class="postfix"></span></div><div class="item" data-id="12"><span class="value">12</span><span class="postfix"></span></div><div class="item" data-id="13"><span class="value">13</span><span class="postfix"></span></div><div class="item" data-id="14"><span class="value">14</span><span class="postfix"></span></div><div class="item" data-id="15"><span class="value">15</span><span class="postfix"></span></div><div class="item" data-id="16"><span class="value">16</span><span class="postfix"></span></div><div class="item" data-id="17"><span class="value">17</span><span class="postfix"></span></div><div class="item" data-id="18"><span class="value">18</span><span class="postfix"></span></div><div class="item" data-id="19"><span class="value">19</span><span class="postfix"></span></div><div class="item" data-id="20"><span class="value">20</span><span class="postfix"></span></div><div class="item" data-id="21"><span class="value">21</span><span class="postfix"></span></div><div class="item" data-id="22"><span class="value">22</span><span class="postfix"></span></div><div class="item" data-id="23"><span class="value">23</span><span class="postfix"></span></div><div class="item" data-id="24"><span class="value">24</span><span class="postfix"></span></div><div class="item" data-id="25"><span class="value">25</span><span class="postfix"></span></div><div class="item" data-id="26"><span class="value">26</span><span class="postfix"></span></div><div class="item" data-id="27"><span class="value">27</span><span class="postfix"></span></div><div class="item" data-id="28"><span class="value">28</span><span class="postfix"></span></div><div class="item" data-id="29"><span class="value">29</span><span class="postfix"></span></div><div class="item" data-id="30"><span class="value">30</span><span class="postfix"></span></div><div class="item" data-id="31"><span class="value">31</span><span class="postfix"></span></div><div class="empty">Empty...</div></div></div></div></div></div></div></div></div><div class="form-col col-1-3"><div class="ui-form-select"><div class="dropdown"><div class="current"></div><input type="text" readonly="" class="controls current-position" value=""><div class="sel-dropdown" style="height: 191px;"><div class="vertical-scroll" style="height: calc(100% - 0px);"><div class="custom-scrollbar"><div class="custom-scroll-handle" style="height: 38px; transform: translateY(0px);"><div class="inner-handle"></div></div></div><div class="inner-scroll-container"><div><div class="items"><div class="item" data-id="1"><span class="value">1月</span><span class="postfix"></span></div><div class="item" data-id="2"><span class="value">2月</span><span class="postfix"></span></div><div class="item" data-id="3"><span class="value">3月</span><span class="postfix"></span></div><div class="item" data-id="4"><span class="value">4月</span><span class="postfix"></span></div><div class="item" data-id="5"><span class="value">5月</span><span class="postfix"></span></div><div class="item" data-id="6"><span class="value">6月</span><span class="postfix"></span></div><div class="item" data-id="7"><span class="value">7月</span><span class="postfix"></span></div><div class="item" data-id="8"><span class="value">8月</span><span class="postfix"></span></div><div class="item" data-id="9"><span class="value">9月</span><span class="postfix"></span></div><div class="item" data-id="10"><span class="value">10月</span><span class="postfix"></span></div><div class="item" data-id="11"><span class="value">11月</span><span class="postfix"></span></div><div class="item" data-id="12"><span class="value">12月</span><span class="postfix"></span></div><div class="empty">Empty...</div></div></div></div></div></div></div></div></div><div class="form-col col-1-3"><div class="ui-form-select"><div class="dropdown"><div class="current"></div><input type="text" readonly="" class="controls current-position" value=""><div class="sel-dropdown" style="height: 191px;"><div class="vertical-scroll" style="height: calc(100% - 0px);"><div class="custom-scrollbar"><div class="custom-scroll-handle" style="height: 38px; transform: translateY(0px);"><div class="inner-handle"></div></div></div><div class="inner-scroll-container"><div><div class="items"><div class="item" data-id="2001"><span class="value">2001</span><span class="postfix"></span></div><div class="item" data-id="2000"><span class="value">2000</span><span class="postfix"></span></div><div class="item" data-id="1999"><span class="value">1999</span><span class="postfix"></span></div><div class="item" data-id="1998"><span class="value">1998</span><span class="postfix"></span></div><div class="item" data-id="1997"><span class="value">1997</span><span class="postfix"></span></div><div class="item" data-id="1996"><span class="value">1996</span><span class="postfix"></span></div><div class="item" data-id="1995"><span class="value">1995</span><span class="postfix"></span></div><div class="item" data-id="1994"><span class="value">1994</span><span class="postfix"></span></div><div class="item" data-id="1993"><span class="value">1993</span><span class="postfix"></span></div><div class="item" data-id="1992"><span class="value">1992</span><span class="postfix"></span></div><div class="item" data-id="1991"><span class="value">1991</span><span class="postfix"></span></div><div class="item" data-id="1990"><span class="value">1990</span><span class="postfix"></span></div><div class="item" data-id="1989"><span class="value">1989</span><span class="postfix"></span></div><div class="item" data-id="1988"><span class="value">1988</span><span class="postfix"></span></div><div class="item" data-id="1987"><span class="value">1987</span><span class="postfix"></span></div><div class="item" data-id="1986"><span class="value">1986</span><span class="postfix"></span></div><div class="item" data-id="1985"><span class="value">1985</span><span class="postfix"></span></div><div class="item" data-id="1984"><span class="value">1984</span><span class="postfix"></span></div><div class="item" data-id="1983"><span class="value">1983</span><span class="postfix"></span></div><div class="item" data-id="1982"><span class="value">1982</span><span class="postfix"></span></div><div class="item" data-id="1981"><span class="value">1981</span><span class="postfix"></span></div><div class="item" data-id="1980"><span class="value">1980</span><span class="postfix"></span></div><div class="item" data-id="1979"><span class="value">1979</span><span class="postfix"></span></div><div class="item" data-id="1978"><span class="value">1978</span><span class="postfix"></span></div><div class="item" data-id="1977"><span class="value">1977</span><span class="postfix"></span></div><div class="item" data-id="1976"><span class="value">1976</span><span class="postfix"></span></div><div class="item" data-id="1975"><span class="value">1975</span><span class="postfix"></span></div><div class="item" data-id="1974"><span class="value">1974</span><span class="postfix"></span></div><div class="item" data-id="1973"><span class="value">1973</span><span class="postfix"></span></div><div class="item" data-id="1972"><span class="value">1972</span><span class="postfix"></span></div><div class="item" data-id="1971"><span class="value">1971</span><span class="postfix"></span></div><div class="item" data-id="1970"><span class="value">1970</span><span class="postfix"></span></div><div class="item" data-id="1969"><span class="value">1969</span><span class="postfix"></span></div><div class="item" data-id="1968"><span class="value">1968</span><span class="postfix"></span></div><div class="item" data-id="1967"><span class="value">1967</span><span class="postfix"></span></div><div class="item" data-id="1966"><span class="value">1966</span><span class="postfix"></span></div><div class="item" data-id="1965"><span class="value">1965</span><span class="postfix"></span></div><div class="item" data-id="1964"><span class="value">1964</span><span class="postfix"></span></div><div class="item" data-id="1963"><span class="value">1963</span><span class="postfix"></span></div><div class="item" data-id="1962"><span class="value">1962</span><span class="postfix"></span></div><div class="item" data-id="1961"><span class="value">1961</span><span class="postfix"></span></div><div class="item" data-id="1960"><span class="value">1960</span><span class="postfix"></span></div><div class="item" data-id="1959"><span class="value">1959</span><span class="postfix"></span></div><div class="item" data-id="1958"><span class="value">1958</span><span class="postfix"></span></div><div class="item" data-id="1957"><span class="value">1957</span><span class="postfix"></span></div><div class="item" data-id="1956"><span class="value">1956</span><span class="postfix"></span></div><div class="item" data-id="1955"><span class="value">1955</span><span class="postfix"></span></div><div class="item" data-id="1954"><span class="value">1954</span><span class="postfix"></span></div><div class="item" data-id="1953"><span class="value">1953</span><span class="postfix"></span></div><div class="item" data-id="1952"><span class="value">1952</span><span class="postfix"></span></div><div class="item" data-id="1951"><span class="value">1951</span><span class="postfix"></span></div><div class="item" data-id="1950"><span class="value">1950</span><span class="postfix"></span></div><div class="item" data-id="1949"><span class="value">1949</span><span class="postfix"></span></div><div class="item" data-id="1948"><span class="value">1948</span><span class="postfix"></span></div><div class="item" data-id="1947"><span class="value">1947</span><span class="postfix"></span></div><div class="item" data-id="1946"><span class="value">1946</span><span class="postfix"></span></div><div class="item" data-id="1945"><span class="value">1945</span><span class="postfix"></span></div><div class="item" data-id="1944"><span class="value">1944</span><span class="postfix"></span></div><div class="item" data-id="1943"><span class="value">1943</span><span class="postfix"></span></div><div class="item" data-id="1942"><span class="value">1942</span><span class="postfix"></span></div><div class="item" data-id="1941"><span class="value">1941</span><span class="postfix"></span></div><div class="item" data-id="1940"><span class="value">1940</span><span class="postfix"></span></div><div class="item" data-id="1939"><span class="value">1939</span><span class="postfix"></span></div><div class="item" data-id="1938"><span class="value">1938</span><span class="postfix"></span></div><div class="item" data-id="1937"><span class="value">1937</span><span class="postfix"></span></div><div class="item" data-id="1936"><span class="value">1936</span><span class="postfix"></span></div><div class="item" data-id="1935"><span class="value">1935</span><span class="postfix"></span></div><div class="item" data-id="1934"><span class="value">1934</span><span class="postfix"></span></div><div class="item" data-id="1933"><span class="value">1933</span><span class="postfix"></span></div><div class="item" data-id="1932"><span class="value">1932</span><span class="postfix"></span></div><div class="item" data-id="1931"><span class="value">1931</span><span class="postfix"></span></div><div class="item" data-id="1930"><span class="value">1930</span><span class="postfix"></span></div><div class="item" data-id="1929"><span class="value">1929</span><span class="postfix"></span></div><div class="item" data-id="1928"><span class="value">1928</span><span class="postfix"></span></div><div class="item" data-id="1927"><span class="value">1927</span><span class="postfix"></span></div><div class="item" data-id="1926"><span class="value">1926</span><span class="postfix"></span></div><div class="item" data-id="1925"><span class="value">1925</span><span class="postfix"></span></div><div class="item" data-id="1924"><span class="value">1924</span><span class="postfix"></span></div><div class="item" data-id="1923"><span class="value">1923</span><span class="postfix"></span></div><div class="item" data-id="1922"><span class="value">1922</span><span class="postfix"></span></div><div class="empty">Empty...</div></div></div></div></div></div></div></div></div></div><div class="form-row"><label>電話號碼</label><div class="form-col col-1-3"></div><div class="form-col col-2-3"><input type="text" class="controls" disabled="" value=""></div></div><div class="form-row"><label>電郵 <i class="mark"></i></label>
                                            @if(Auth::user())
                                                <input type="text" class="controls" disabled="" value="{{Auth::user()->email}}">
                                            @else
                                                <input type="text" class="controls" disabled="" value="email@email.com">
                                            @endif
                                        </div></form><div class="form-row"><button class="btn btn-primary">儲存變更</button></div></div><div class="col animated-item"><h2>頭像</h2><form class="form"><div class="form-row"><label for="fileInputAvatar" class="avatar-uploader"><input type="file" accept="image/*"><div class="file"><img class="image"></div><div class="upload"></div><div class="avatar"><i class="done"></i><img class="image" src="imagepath"></div><div class="text">拖曳此處或點擊選取</div></label></div><div class="form-row"><button disabled="" class="btn btn-primary" type="submit">上載</button></div></form></div></div><br><div class="form-disclaimer animated-item-opacity"><p><i class="mark"></i><span>名字、姓氏、電郵和國家均不可更改。<br>要編輯這些資料，請 <a target="_blank" href="/info">通知服務支援</a>。</span></p></div></div></div></div></div></div></div></div>
@endsection

@section("scripts")
    <script>
        $('.dropdown').click(function(event) {
            $('.dropdown').removeClass("highlight open");
            $(event.target).parent().addClass("highlight open");
        });
    </script>
@endsection