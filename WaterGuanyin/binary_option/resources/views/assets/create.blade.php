@extends('layouts.app')

@section('content')
    <section class="content-header">
        <h1>
            Asset
        </h1>
    </section>
    <div class="content">
        @include('adminlte-templates::common.errors')
        <div class="box box-primary">
            <div class="box-body">
                <div class="row">
                    {!! Form::open(['route' => 'assets.store', 'files' => true]) !!}

                        @include('assets.fields')

                    {!! Form::close() !!}
                </div>
            </div>
        </div>
    </div>
@endsection
