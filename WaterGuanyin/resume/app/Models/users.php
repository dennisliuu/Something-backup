<?php

namespace App\Models;

use Eloquent as Model;

/**
 * Class users
 * @package App\Models
 * @version December 6, 2019, 12:55 pm UTC
 *
 * @property string name
 * @property string email
 * @property string|\Carbon\Carbon email_verified_at
 * @property string password
 * @property string content
 * @property string profile_image
 * @property string remember_token
 */
class users extends Model
{

    public $table = 'users';
    
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';




    public $fillable = [
        'name',
        'email',
        'email_verified_at',
        'password',
        'content',
        'profile_image',
        'remember_token',
        'phone'
    ];

    /**
     * The attributes that should be casted to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'name' => 'string',
        'email' => 'string',
        'email_verified_at' => 'datetime',
        'password' => 'string',
        'content' => 'string',
        'profile_image' => 'string',
        'remember_token' => 'string'
    ];

    /**
     * Validation rules
     *
     * @var array
     */
    public static $rules = [
//        'name' => 'required',
//        'email' => 'required',
//        'password' => 'required'
    ];

    
}
