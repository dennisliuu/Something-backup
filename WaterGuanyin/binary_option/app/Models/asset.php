<?php

namespace App\Models;

use Eloquent as Model;
use Illuminate\Database\Eloquent\SoftDeletes;

/**
 * Class asset
 * @package App\Models
 * @version December 15, 2019, 8:19 am UTC
 *
 * @property string name
 * @property string type
 * @property string image
 * @property integer percentage
 * @property integer upsdowns
 */
class asset extends Model
{
    use SoftDeletes;

    public $table = 'assets';
    

    protected $dates = ['deleted_at'];



    public $fillable = [
        'name',
        'type',
        'image',
        'percentage',
        'upsdowns'
    ];

    /**
     * The attributes that should be casted to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'name' => 'string',
        'type' => 'string',
        'image' => 'image',
        'percentage' => 'integer',
        'upsdowns' => 'integer'
    ];

    /**
     * Validation rules
     *
     * @var array
     */
    public static $rules = [
        'name' => 'required',
        'type' => 'required'
    ];

    
}
