@extends('layouts.app')

@section('content')
<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->
@php
$user = Auth::user();
// print_r($user);
@endphp
<style>
.edit-box{
    background: #555;
    width: 100%;
    color: #fff;
    display: block;
    text-align: center;
    padding: 3px;
    /* border-radius: 10px; */
    margin-top: 5px;
    cursor: pointer;
}
.citem{
    float: left;
    margin-right: 10px;
}
.edit-box-mini{
    background: #555;
  
    color: #fff;
}
.edit-box:hover{
    color:#555;
    background: #ccc;
}
</style>
<div class="container">
    <div class="row">
        <div class="col-xs-12 col-sm-6 col-md-6">
            <div class="well well-sm">
                <div class="row">
                    <div class="col-sm-6 col-md-4">

                        
                        @if ($user ->profile_image != null)
                    <img src="{{$user->profile_image}}" alt="" class="img-rounded img-responsive" />
                  
                        @else
                            <img src="http://placehold.it/380x500" alt="" class="img-rounded img-responsive" />
                  
                        @endif

<span class="edit-box">點擊上傳</span>
                         </div>
                    <div class="col-sm-6 col-md-8">
                            @if ($user ->name != null)
                    <h4 onclick="edit_user('name')">{{$user->name}}(點擊更新)</h4>
                            @else
                            <h4 onclick="edit_user('name')">未取名(點擊更新)</h4>
                           
                            
                            @endif
                          
                        <p class="citem" onclick="edit_user('phone')">
                            <i class="glyphicon glyphicon-earphone" style="margin-right:10px;"></i>
                            @if ($user->phone)
                            {{$user->phone}}(點擊修改)
                                @else
                                未輸入(點擊修改)
                            @endif
                        </p>
                         
{{-- <span class="edit-box-mini citem"><i class="glyphicon glyphicon-pencil" style="margin-right:10px;"></i>編輯</span> --}}
                           
<hr />
                            <div class="btn-group">
                            <a href="/resume/{{$user->id}}" target="_blank">
                                    <button type="button" class="btn btn-primary">
                                        前往查看名片</button>
                                    </a>
                            </div>
                            
                          
                        <!-- Split button -->
                        {{-- <div class="btn-group">
                            <button type="button" class="btn btn-primary">
                                Social</button>
                            <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                <span class="caret"></span><span class="sr-only">Social</span>
                            </button>
                            <ul class="dropdown-menu" role="menu">
                                <li><a href="#">Twitter</a></li>
                                <li><a href="https://plus.google.com/+Jquery2dotnet/posts">Google +</a></li>
                                <li><a href="https://www.facebook.com/jquery2dotnet">Facebook</a></li>
                                <li class="divider"></li>
                                <li><a href="#">Github</a></li>
                            </ul>
                        </div> --}}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

@endsection
@section('scripts')

<script>
        function edit_user(col_name){
            let foo = prompt('請輸入新的數值');
            $.ajax({
                                type: "PUT",
                                url: "/api/users/{{$user->id}}",
                                data:JSON.parse('{"'+col_name+'":"'+foo+'"}'),
                                success: function (msg)
                                {
                                  location.reload()
                                   //$("#TextBoxName").value(msg.d);
                                }
        });
        }
        </script>
@endsection