<li class="{{ Request::is('users*') ? 'active' : '' }}">
    <a href="{{ route('users.index') }}"><i class="fa fa-edit"></i><span>Users</span></a>
</li>

<li class="{{ Request::is('assets*') ? 'active' : '' }}">
    <a href="{{ route('assets.index') }}"><i class="fa fa-edit"></i><span>資產</span></a>
</li>

