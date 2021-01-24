<!-- Name Field -->
<div class="form-group">
    {!! Form::label('name', 'Name:') !!}
    <p>{{ $asset->name }}</p>
</div>

<!-- Type Field -->
<div class="form-group">
    {!! Form::label('type', 'Type:') !!}
    <p>{{ $asset->type }}</p>
</div>

<!-- Image Field -->
<div class="form-group">
    {!! Form::label('image', 'Image:') !!}
    <p>{{ $asset->image }}</p>
</div>

<!-- Percentage Field -->
<div class="form-group">
    {!! Form::label('percentage', 'Percentage:') !!}
    <p>{{ $asset->percentage }}</p>
</div>

<!-- Upsdowns Field -->
<div class="form-group">
    {!! Form::label('upsdowns', 'Upsdowns:') !!}
    <p>{{ $asset->upsdowns }}</p>
</div>

<!-- Created At Field -->
<div class="form-group">
    {!! Form::label('created_at', 'Created At:') !!}
    <p>{{ $asset->created_at }}</p>
</div>

<!-- Updated At Field -->
<div class="form-group">
    {!! Form::label('updated_at', 'Updated At:') !!}
    <p>{{ $asset->updated_at }}</p>
</div>

