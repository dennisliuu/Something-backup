<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use GuzzleHttp\Client;

class videoController extends Controller
{
    public function upload(Request $request){
        if ($request->hasFile('video')) {
            // 解開上傳限制 https://github.com/laradock/laradock/issues/721
            $file = $request->file('video');  //獲取UploadFile例項
            if ( $file->isValid()) { //判斷檔案是否有效
                //$filename = $file->getClientOriginalName(); //檔案原名稱
                $extension = $file->getClientOriginalExtension(); //副檔名
                $filename = time() . "." . $extension;    //重新命名
                $path = '/var/www/res/flask/video';
                if(!is_dir(($path))){
                    \File::makeDirectory($path, 0755);
                }

                $file->move($path, $filename); //移動至指定目錄
                // TODO: flask 那邊 youtube api 設定好就能執行以下程式碼
//                $client = new Client([
//                    // Base URI is used with relative requests
//                    'base_uri' => 'http://127.0.0.1:8999',
//                ]);
//
//                $res = $client->request('POST', '/upload-video', [
//                    'form_params' => [
//                        'title' => $request->title,
//                        'description' => $request->description,
//                        'video_path' => $path . $filename
//                    ]
//                ]);
//
//                $res_arr = json_decode($res->getBody(), true);
//                $video_url = 'https://www.youtube.com/watch?v=' . $res_arr['id'];
//                return view('video.upload', ["video_url" => $video_url]);

            }
        }
        return view('video.upload', ["video_url" => null]);
    }
}
