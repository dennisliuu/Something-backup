<?php

namespace App\Http\Controllers;

use App\Models\asset;
use Illuminate\Http\Request;

class frontendController extends Controller
{
    public function index() {
        return view('index');
    }

    public function index_copy() {
        return view('index copy');
    }

    public function mobile_black() {
        return view('mobile_black');
    }

    public function mobile_white() {
        return view('mobile_white');
    }

    public function test() {
        return view('test');
    }

    public function home() {
        return view('home');
    }

    public function sample() {
        $asset = asset::all();
        return view('sample', ['data' => $asset]);
    }

    public function user_info() {
        return view('user_info');
    }
    public function user_deals() {
        return view('user_deals');
    }
    public function user_edit() {
        return view('user_edit');
    }
    public function user_session() {
        return view('user_logout');
    }
}
