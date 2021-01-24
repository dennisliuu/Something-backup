@extends('layouts.app')

@section('content')
<section class="content-header">
    <h1 class="pull-left">{{__("Products")}}</h1>
    <h1 class="pull-right">
        <button class="btn btn-primary pull-right" style="margin-top: -10px;margin-bottom: 5px" data-toggle="modal" data-target="#exampleModal">新增</button>
        <button class="btn btn-primary pull-right" style="margin-top: -10px;margin-bottom: 5px" data-toggle="modal" data-target="#exampleModal_manual">手動新增</button>
    </h1>
</section>
<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">請輸入網址</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <input type="text" name="url" id="spider_url" />
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>
                <button type="button" class="btn btn-primary" id="add_btn">新增</button>
            </div>
        </div>
    </div>
</div>
<div class="modal fade" id="exampleModal_manual" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">請輸入資訊</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="form-group">
                        <label for="inputAddress">地址</label>
                        <input type="text" class="form-control" name="estate_address" id="estate_address" placeholder="ex. 100台北市中正區重慶南路一段122號">
                    </div>
                    <div class="form-group">
                        <label for="exampleFormControlFile1">上傳照片</label>
                        <input type="file" class="form-control-file" name="estate_picture" id="estate_picture">
                    </div>
                    <div class="form-group ">
                        <label>類型</label>
                        <input type="text" class="form-control" name="estate_type" id="estate_type">
                    </div>
                    <div class="form-group ">
                        <label>坪數</label>
                        <input type="text" class="form-control" name="estate_size" id="estate_size">
                    </div>
                    <div class="form-group">
                        <label>價格</label>
                        <input type="text" class="form-control" name="estate_price" id="estate_price" />
                    </div>
                    <div class="form-row">
                        <div class="form-group col-md-6" style="padding-left: 0px; padding-right:0px">
                            <label>房數</label>
                            <input type="text" class="form-control" name="estate_rooms" id="estate_rooms" placeholder="房數" />
                        </div>
                        <div class="form-group col-md-6"  style="padding-left: 0px; padding-right:0px">
                            <label>廳數</label>
                            <input type="text" class="form-control" name="estate_rests" id="estate_rests" placeholder="廳數" />
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>
                <button type="button" class="btn btn-primary" id="add_btn_manual">新增</button>
            </div>
        </div>
    </div>
</div>

<div class="content">
    <div class="clearfix"></div>

    @include('flash::message')

    <div class="clearfix"></div>
    <div class="box box-primary">
        <div class="box-body">
            @include('products.table')
        </div>
    </div>
    <div class="text-center">

    </div>
</div>
@endsection

@php

$user = Auth::user();

@endphp
@section('scripts')
<script>
    $('#add_btn').click(function() {
        // $('#add_btn').attr('disabled', true);
        $.ajax({
            url: "http://{{env('Flask_Host')}}/get-house-info",
            type: "POST",
            data: {
                "url": $('#spider_url').val()
            },
            success: function(data) {
                data = JSON.parse(data);
                console.log(data)
                // if(data[0].status){
                //     location.reload();
                // }

                for (let i = 0; i < data.length; i++) {
                    // console.log(data)
                    var item = data[i];
                    item['user_id'] = {
                        {
                            $user - > id
                        }
                    }
                    $.ajax({
                        url: "/api/products",
                        type: "POST",
                        data: item,
                        success: function(data) {},
                        error: function() {}
                    });
                }
                $('.close').click()
                setTimeout(() => {
                    location.reload();
                }, 1);

            },
            error: function() {}
        })
    })

    $('#add_btn_manual').click(function() {
        let estate_address = $('#estate_address').val()
        let estate_picture = $('#estate_picture').val()
        let estate_type = $('#estate_type').val()
        let estate_size = $('#estate_size').val()
        let estate_price = $('#estate_price').val()
        let estate_rooms = $('estate_rooms').val()
        let estate_rests = $('estate_halls').val()
        let data = {
            'address': estate_address,
            'size': estate_size,
            'image': estate_picture,
            'type': estate_type,
            'room_num': estate_rooms,
            'rest_num': estate_rests,
            'price': estate_price
        }
        alert(data)
        for (let i = 0; i < data.length; i++) {
            console.log(data)
            var item = data[i];
            item['user_id'] = {
                {
                    $user - > id
                }
            }
            $.ajax({
                url: "/api/products",
                type: "POST",
                data: item,
                success: function(data) {},
                error: function() {}
            });
        }
        $('.close').click()
        setTimeout(() => {
            location.reload();
        }, 1);


    })
</script>
@endsection