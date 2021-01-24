<?php

namespace App\Models;

use Eloquent as Model;

/**
 * Class products
 * @package App\Models
 * @version December 7, 2019, 9:21 am UTC
 *
 * @property string address
 * @property string image
 * @property string type
 * @property string size
 * @property string price
 */
class products extends Model
{

    public $table = 'products';
    
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';




    public $fillable = [
        'address',
        'image',
        'type',
        'size',
        'price',
        'room_num',
        'rest_num',
        'user_id',
        'link'
    ];

    /**
     * The attributes that should be casted to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'address' => 'string',
        'image' => 'string',
        'type' => 'string',
        'size' => 'string',
        'price' => 'string',
        'room_num'=>'integer',
        'rest_num'=>'integer'
        
    ];

    /**
     * Validation rules
     *
     * @var array
     */
    public static $rules = [
        'address' => 'required',
        'image' => 'required',
        'type' => 'required',
        'size' => 'required',
        'price' => 'required'
    ];

    
}
