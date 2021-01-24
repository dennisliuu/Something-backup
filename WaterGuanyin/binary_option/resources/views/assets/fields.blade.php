<!-- Name Field -->
<div class="form-group col-sm-6">
    {!! Form::label('name', '名稱:') !!}
    {!! Form::text('name', null, ['class' => 'form-control']) !!}
</div>

<!-- Type Field -->
<div class="form-group col-sm-6">
    {!! Form::label('type', '類型:') !!}
    {!! Form::text('type', null, ['class' => 'form-control']) !!}
</div>

<!-- Image Field -->
<div class="form-group col-sm-6">
    {!! Form::label('image', '圖片:') !!}
    {!! Form::file('image') !!}
</div>
<div class="clearfix"></div>

<!-- Percentage Field -->
<div class="form-group col-sm-6">
    {!! Form::label('percentage', '百分比(%):') !!}
    {!! Form::number('percentage', null, ['class' => 'form-control']) !!}
</div>

<!-- Upsdowns Field -->
<div class="form-group col-sm-6">
    {!! Form::label('upsdowns', '漲跌(%):') !!}
    {!! Form::number('upsdowns', null, ['class' => 'form-control']) !!}
</div>

<!-- Submit Field -->
<div class="form-group col-sm-12">
    {!! Form::submit('Save', ['class' => 'btn btn-primary']) !!}
    <a href="{{ route('assets.index') }}" class="btn btn-default">取消</a>
</div>
