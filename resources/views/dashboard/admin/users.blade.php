@extends('adminlte::page')

@section('title', 'Users')

@section('content_header')
<h1>Users</h1>
@stop

@section('content')
<!-- Main content -->
<section class="content">
    <div class="row">
        <div class="col-12">
            <div class="card">
                <div class="card-header">
                    <div class="container-fluid">
                        <div class="row mb-2">
                            <div class="col-sm-6">
                                <h3 class="card-title">Data Users</h3>
                            </div>
                            <div class="col-sm-6">
                                <a href="#" class="btn btn-primary float-right"><i class="far fa-plus"></i> Tambah</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <table class="table user-list" id="tblusers">
                        <thead>
                            <tr>
                                <th><span>User</span></th>
                                <th><span>Points</span></th>
                                <th><span>Created</span></th>
                                <th class="text-center"><span>Status</span></th>
                                <th><span>Email</span></th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt=""
                                        class="rounded-circle" width="50px">
                                    <a href="#" class="user-link">Mila Kunis</a>
                                </td>
                                <td>
                                    <button type="button" class="btn btn-outline-warning">100</button>
                                </td>
                                <td>
                                    2013/08/08
                                </td>
                                <td class="text-center">
                                    <button type="button" class="btn btn-block btn-danger btn-sm">Inactive</button>
                                </td>
                                <td>
                                    <a href="#">mila@kunis.com</a>
                                </td>
                                <td style="width: 20%;">
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-pencil fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link danger">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fas fa-trash fa-stack-1x fa-inverse"></i>
                                        </span>

                                    </a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <img src="https://bootdey.com/img/Content/avatar/avatar6.png" alt=""
                                        class="rounded-circle" width="50px">
                                    <a href="#" class="user-link">Robert Downey Jr.</a>
                                </td>
                                <td>
                                    <button type="button" class="btn btn-outline-warning">50</button>
                                </td>
                                <td>
                                    2013/12/31
                                </td>
                                <td class="text-center">
                                    <button type="button" class="btn btn-block btn-success btn-sm">Active</button>
                                </td>
                                <td>
                                    <a href="#">spencer@tracy</a>
                                </td>
                                <td style="width: 20%;">
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-pencil fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link danger">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fas fa-trash fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <!-- /.card-body -->
            </div>
            <!-- /.card -->
        </div>
    </div>
</section>
{{-- <div class="container">
    <div class="row">
        <div class="col-lg-12">
            <div class="main-box clearfix">
                <div class="table-responsive">
                    <table class="table user-list" id="tblusers">
                        <thead>
                            <tr>
                                <th><span>User</span></th>
                                <th><span>Created</span></th>
                                <th class="text-center"><span>Status</span></th>
                                <th><span>Email</span></th>
                                <th>&nbsp;</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt=""
                                        class="rounded-circle" width="50px">
                                    <a href="#" class="user-link">Mila Kunis</a>
                                    <span class="user-subhead">Admin</span>
                                </td>
                                <td>
                                    2013/08/08
                                </td>
                                <td class="text-center">
                                    <span class="label label-default">Inactive</span>
                                </td>
                                <td>
                                    <a href="#">mila@kunis.com</a>
                                </td>
                                <td style="width: 20%;">
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-pencil fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link danger">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-trash-o fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <img src="https://bootdey.com/img/Content/avatar/avatar6.png" alt="" class="rounded-circle" width="50px">
                                    <a href="#" class="user-link">Robert Downey Jr.</a>
                                    <span class="user-subhead">Admin</span>
                                </td>
                                <td>
                                    2013/12/31
                                </td>
                                <td class="text-center">
                                    <span class="label label-success">Active</span>
                                </td>
                                <td>
                                    <a href="#">spencer@tracy</a>
                                </td>
                                <td style="width: 20%;">
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-pencil fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                    <a href="#" class="table-link danger">
                                        <span class="fa-stack">
                                            <i class="fa fa-square fa-stack-2x"></i>
                                            <i class="fa fa-trash-o fa-stack-1x fa-inverse"></i>
                                        </span>
                                    </a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div> --}}
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
        $("#tblusers").DataTable();
    });
</script>
@stop
