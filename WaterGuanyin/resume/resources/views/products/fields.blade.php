<!-- Address Field -->
<div class="form-group col-sm-6">
    {!! Form::label('address', '{{ __("Address") }}:') !!}
    {!! Form::text('address', null, ['class' => 'form-control']) !!}
</div>

<!-- Image Field -->
<div class="form-group col-sm-6">
    {!! Form::label('image', '{{ __("Image") }}:') !!}
    {!! Form::file('image') !!}
</div>
<div class="clearfix"></div>

<!-- Type Field -->
<div class="form-group col-sm-6">
    {!! Form::label('type', '{{ __("Type") }}:') !!}
    {!! Form::text('type', null, ['class' => 'form-control']) !!}
</div>

<!-- Size Field -->
<div class="form-group col-sm-6">
    {!! Form::label('size', '{{ __("Size") }}:') !!}
    {!! Form::text('size', null, ['class' => 'form-control']) !!}
</div>

<!-- Price Field -->
<div class="form-group col-sm-6">
    {!! Form::label('price', '{{ __("Price") }}:') !!}
    {!! Form::text('price', null, ['class' => 'form-control']) !!}
</div>

<!-- Submit Field -->
<div class="form-group col-sm-12">
    {!! Form::submit('Save', ['class' => 'btn btn-primary']) !!}
    <a href="{{ route('products.index') }}" class="btn btn-default">{{ __("Cancel") }}</a>
</div>
