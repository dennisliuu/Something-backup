<div class="table-responsive">
    <table class="table" id="products-table">
        <thead>
            <tr>
                <th>{{ __("Address") }}</th>
        <th>{{ __("Image") }}</th>
        <th>{{ __("Type") }}</th>
        <th>{{ __("Size") }}</th>
        <th>{{ __("Price") }}</th>
        <th>{{ __("Room_num") }}</th>
        <th>{{ __("Rest_num") }}</th>
        
                <th colspan="3">{{ __("Action") }}</th>
            </tr>
        </thead>
        <tbody>
        @foreach($products as $products)
            <tr>
                <td>{{ $products->address }}</td>
            <td><img src="{{ $products->image }}" class="house_img" /></td>
            <td>{{ $products->type }}</td>
            <td>{{ $products->size }}</td>
            <td>{{ $products->price }}</td>
            <td>{{ $products->room_num }}</td>
            <td>{{ $products->rest_num }}</td>
                <td>
                    {!! Form::open(['route' => ['products.destroy', $products->id], 'method' => 'delete']) !!}
                    <div class='btn-group'>
                        <a href="{{ route('products.show', [$products->id]) }}" class='btn btn-default btn-xs'><i class="glyphicon glyphicon-eye-open"></i></a>
                        <a href="{{ route('products.edit', [$products->id]) }}" class='btn btn-default btn-xs'><i class="glyphicon glyphicon-edit"></i></a>
                        {!! Form::button('<i class="glyphicon glyphicon-trash"></i>', ['type' => 'submit', 'class' => 'btn btn-danger btn-xs', 'onclick' => "return confirm('Are you sure?')"]) !!}
                    </div>
                    {!! Form::close() !!}
                </td>
            </tr>
        @endforeach
        </tbody>
    </table>
</div>
