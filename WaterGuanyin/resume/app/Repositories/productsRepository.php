<?php

namespace App\Repositories;

use App\Models\products;
use App\Repositories\BaseRepository;

/**
 * Class productsRepository
 * @package App\Repositories
 * @version December 7, 2019, 9:21 am UTC
*/

class productsRepository extends BaseRepository
{
    /**
     * @var array
     */
    protected $fieldSearchable = [
        'address',
        'image',
        'type',
        'size',
        'price'
    ];

    /**
     * Return searchable fields
     *
     * @return array
     */
    public function getFieldsSearchable()
    {
        return $this->fieldSearchable;
    }

    /**
     * Configure the Model
     **/
    public function model()
    {
        return products::class;
    }
}
