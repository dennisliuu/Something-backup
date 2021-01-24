<?php

/** @var \Illuminate\Database\Eloquent\Factory $factory */

use App\Models\asset;
use Faker\Generator as Faker;

$factory->define(asset::class, function (Faker $faker) {

    return [
        'name' => $faker->word,
        'type' => $faker->word,
        'image' => $faker->word,
        'percentage' => $faker->randomDigitNotNull,
        'upsdowns' => $faker->randomDigitNotNull,
        'created_at' => $faker->date('Y-m-d H:i:s'),
        'updated_at' => $faker->date('Y-m-d H:i:s')
    ];
});
