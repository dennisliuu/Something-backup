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
                   {!! Form::model($asset, ['route' => ['assets.update', $asset->id], 'method' => 'patch', 'files' => true]) !!}

                        @include('assets.fields')

                   {!! Form::close() !!}
               </div>
           </div>
       </div>
   </div>
@endsection