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

Route::get('admin', function () {
    return view('dashboard.dashboard');
});
Route::get('admin/lapangan', function () {
    return view('admin.lapangan');
});
Route::get('admin/booking', function () {
    return view('admin.booking');
});
Route::get('admin/users', function () {
    return view('admin.users');
});

Auth::routes();

// Route::get('/admin', 'HomeController@index')->name('admin');
