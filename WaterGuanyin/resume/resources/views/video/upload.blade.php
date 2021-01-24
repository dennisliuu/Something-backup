@extends('layouts.app')

@section('content')
    <form method="POST" style="margin-left: 20px;" enctype="multipart/form-data">
        @csrf
        <div class="form-group">
            <label for="title">影片標題</label>
            <input type="text" class="form-control" id="title" name="title">

        </div>
        <div class="form-group">
            <label for="description">影片描述</label>
            <input type="text" class="form-control" id="description" name="description">
        </div>
        <div class="form-group form-check">
            <label for="video">影片</label>
            <input type="file" class="form-control" id="video" name="video">
        </div>
        <button type="submit" class="btn btn-primary">送出</button>
        @if ($video_url)
            <a href="{{ $video_url }}">影片網址</a>
        @endif
    </form>
@endsection

