@extends('adminlte::page')

@section('title', 'Dashboard')

@section('content_header')
<h1>Dashboard</h1>
@stop

@section('content')
<div class="container">
    <div class="row">
        <div class="col-sm">
            <div class="small-box bg-info">
                <div class="inner">
                    <h3>150</h3>
                    <p>Bookings</p>
                </div>
                <div class="icon">
                    <i class="fad fa-book"></i>
                </div>
                <a href="#" class="small-box-footer">
                    More info <i class="fas fa-arrow-circle-right"></i>
                </a>
            </div>
        </div>
        <div class="col-sm">
            <div class="small-box bg-gradient-success">
                <div class="inner">
                  <h3>44</h3>
                  <p>User Registrations</p>
                </div>
                <div class="icon">
                  <i class="fas fa-user-plus"></i>
                </div>
                <a href="#" class="small-box-footer">
                  More info <i class="fas fa-arrow-circle-right"></i>
                </a>
              </div>

        </div>
        <div class="col-sm">
            {{-- One of three columns --}}
        </div>
    </div>
</div>



@stop

@section('css')
<link rel="stylesheet" href="/css/admin_custom.css">
@stop

@section('js')
<script>
    console.log('Hello world!');
</script>
@stop
