<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
use App\models\Users;
use App\models\products;

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');


Auth::routes(); 

Route::get('/home', 'HomeController@index');
Route::get('profile', function () {
    return view('profile.index');
    })->name("profile");
    Route::get('resume/{id}', function ($id) {
       
        $user_data = Users::find($id);
        $products = products::where('user_id',$id)->get();
        return view('profile.resume')->with('user_data',$user_data)->with('products',$products);
        })->name("resume");
    


// Route::get('/profile')->view('profile.index');



Route::resource('users', 'usersController');

Route::get('/user-profile/{id}', 'usersController@editProfile')->name('profile_setting');
Route::get('/upload/video', 'videoController@upload')->name('video_upload');
Route::post('/upload/video', 'videoController@upload')->name('video_upload');

Route::resource('products', 'productsController');