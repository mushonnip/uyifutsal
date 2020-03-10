@extends('adminlte::page')


@section('title', 'Booking')

@section('content_header')
<h1>Booking</h1>
@stop


@section('content')
<section class="content">
    <div class="row">
        <div class="col-12">
            <div class="card">
                <div class="card-header">
                    <div class="container-fluid">
                        <div class="row mb-2">
                            <div class="col-sm-6">
                                <h3 class="card-title">Data Lapangan</h3>
                            </div>
                            <div class="col-sm-6">
                                <a href="#" class="btn btn-primary float-right"><i class="far fa-plus"></i> Tambah</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <table id="tbllapangan" class="table table-bordered table-hover">
                        <thead>
                            <tr>
                                <th>No</th>
                                <th>Nama</th>
                                <th>Foto</th>
                                <th>Jadwal</th>
                                <th>Aksi</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td>Lapangan A</td>
                                <td><img src="{{ asset('img/logo.png') }}" alt="gambar" srcset="" width="150px"></td>
                                <td> 4</td>
                                <td class="text-center">
                                    <button type="button" class="btn btn-sm btn-info ">Lihat</button>
                                    <button type="button" class="btn btn-sm btn-success ">Ubah</button>
                                    <button type="button" class="btn btn-sm btn-danger">Hapus</button>
                                </td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <tr>
                                <th>No</th>
                                <th>Nama</th>
                                <th>Foto</th>
                                <th>Jadwal</th>
                                <th>Aksi</th>
                            </tr>
                        </tfoot>
                    </table>
                </div>
                <!-- /.card-body -->
            </div>
            <!-- /.card -->
        </div>
    </div>
</section>
@stop

@section('css')
<link rel="stylesheet" href="/css/admin_custom.css">
@stop

@section('js')
<script>
    console.log('Hello world!');
</script>
<script>
    $(function () {
        $("#tblbooking").DataTable();
    });
</script>
@stop
