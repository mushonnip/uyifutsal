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

Route::get('/', function () {
    return view('home');
});

Route::group(['prefix' => 'dashboard'], function () {
    Route::get('admin', function () {
        return view('dashboard.dashboard');
    });
    Route::get('admin/lapangan', function () {
        return view('dashboard.admin.lapangan');
    });
    Route::get('admin/booking', function () {
        return view('dashboard.admin.booking');
    });
    Route::get('admin/users', function () {
        return view('dashboard.admin.users');
    });
});

Route::get('detail', function () {
    return view('detail');
});

Auth::routes();

// Route::get('/admin', 'HomeController@index')->name('admin');

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');
