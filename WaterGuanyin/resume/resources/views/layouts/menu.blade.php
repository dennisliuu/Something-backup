<li class="{{ Request::is('users*') ? 'active' : '' }}">
    <a href="{{ route('users.index') }}"><i class="fa fa-edit"></i><span>用戶資訊</span></a>
</li>
<li>
    <a href="{{ route('profile') }}"><i class="fa fa-edit"></i><span>名片設定</span></a>
</li>

<li class="{{ Request::is('products*') ? 'active' : '' }}">
    <a href="{{ route('products.index') }}"><i class="fa fa-edit"></i><span>{{ __('Products') }}</span></a>
</li>

<li>
    <a href="{{ route('video_upload') }}"><i class="fa fa-edit"></i><span>上傳影片</span></a>
</li>


