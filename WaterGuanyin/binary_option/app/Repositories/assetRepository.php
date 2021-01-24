<?php

namespace App\Repositories;

use App\Models\asset;
use App\Repositories\BaseRepository;

/**
 * Class assetRepository
 * @package App\Repositories
 * @version December 15, 2019, 8:19 am UTC
*/

class assetRepository extends BaseRepository
{
    /**
     * @var array
     */
    protected $fieldSearchable = [
        'name',
        'type',
        'image',
        'percentage',
        'upsdowns'
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
        return asset::class;
    }
}
