@extends('layouts.app')

@section('js')
<script>
    $(document).ready(function () {
        $(".card").hover(
            function () {
                $(this).addClass('shadow-lg').css('cursor', 'pointer');
            }, function () {
                $(this).removeClass('shadow-lg');
            }
        )
    });
</script>
@endsection
@section('content')

<div class="container">
    <div class="text-center">
        <img src="{{asset('img/full-team.svg')}}" alt="" srcset="" width="750px" class="img-fluid">
        <h2 class="text-center">Selamat Datang Di Website Kami</h2>
    </div>
    <hr>
    <h2 class="text-center">Lapangan UYI Futsal</h2>
    <div class="card-deck">
        <div class="card mb-4"">
        <img class=" card-img-top img-fluid" src="{{ asset('img/img1.jpeg') }}" alt="Card image cap">
            <div class="card-body">
                <h4 class="card-title">Lapangan A</h4>
                {{-- <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p> --}}
                {{-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> --}}
                <a href="#" class="btn btn-primary">Booking
                    <span class="fa fa-trash-o fa-lg" aria-hidden="true"></span>
                </a>
            </div>
        </div>
        <div class="card mb-4"">
            <img class=" card-img-top img-fluid" src="{{ asset('img/img1.jpeg') }}" alt="Card image cap">
            <div class="card-body">
                <h4 class="card-title">Lapangan B</h4>
                {{-- <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p> --}}
                {{-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> --}}
                <a href="#" class="btn btn-primary">Booking</a>
            </div>
        </div>
    </div>
</div>
<hr>
<p class="text-center">© 2020 Kelompok 1</p>
@endsection
