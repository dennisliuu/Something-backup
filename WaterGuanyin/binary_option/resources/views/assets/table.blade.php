<div class="table-responsive">
    <table class="table" id="assets-table">
        <thead>
            <tr>
                <th>名稱</th>
        <th>類型</th>
        <th>圖片</th>
        <th>百分比</th>
        <th>漲跌</th>
                <th colspan="3">動作</th>
            </tr>
        </thead>
        <tbody>
        @foreach($assets as $asset)
            <tr>
                <td>{{ $asset->name }}</td>
            <td>{{ $asset->type }}</td>
            <td>{{ $asset->image }}</td>
            <td>{{ $asset->percentage }}</td>
            <td>{{ $asset->upsdowns }}</td>
                <td>
                    {!! Form::open(['route' => ['assets.destroy', $asset->id], 'method' => 'delete']) !!}
                    <div class='btn-group'>
                        <a href="{{ route('assets.show', [$asset->id]) }}" class='btn btn-default btn-xs'><i class="glyphicon glyphicon-eye-open"></i></a>
                        <a href="{{ route('assets.edit', [$asset->id]) }}" class='btn btn-default btn-xs'><i class="glyphicon glyphicon-edit"></i></a>
                        {!! Form::button('<i class="glyphicon glyphicon-trash"></i>', ['type' => 'submit', 'class' => 'btn btn-danger btn-xs', 'onclick' => "return confirm('Are you sure?')"]) !!}
                    </div>
                    {!! Form::close() !!}
                </td>
            </tr>
        @endforeach
        </tbody>
    </table>
</div>
