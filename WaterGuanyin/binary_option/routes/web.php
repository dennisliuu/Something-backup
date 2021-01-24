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

Route::get('/', 'frontendController@index');

Route::resource('users', 'UsersController');

Route::get('/mobile_black', 'frontendController@mobile_black');

Route::get('/mobile_white', 'frontendController@mobile_white');

Route::get('/test', 'frontendController@test');

Route::get('/sample', 'frontendController@sample');
Route::get('/user-info', 'frontendController@user_info');
Route::get('/user/deals', 'frontendController@user_deals');
Route::get('/user/edit', 'frontendController@user_edit');
Route::get('/user/session', 'frontendController@user_session');

Route::get('/home', 'frontendController@home');

Auth::routes();

Route::get('/home', 'HomeController@index');



Route::resource('assets', 'assetController');