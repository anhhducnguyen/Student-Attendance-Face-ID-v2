<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Admin Dashboard</title>
  <!-- Google Font: Source Sans Pro -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
  <!-- Font Awesome -->

  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/plugins/fontawesome-free/css/all.min.css' %}">
  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css' %}">
  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/plugins/icheck-bootstrap/icheck-bootstrap.min.css' %}">
  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/plugins/jqvmap/jqvmap.min.css' %}">
  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/css/adminlte.min.css' %}">
  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/plugins/overlayScrollbars/css/OverlayScrollbars.min.css' %}">
  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/plugins/daterangepicker/daterangepicker.css' %}">
  {% load static %}
  <link rel="stylesheet" href="{% static 'assets/css/Admin/admin/assets/plugins/summernote/summernote-bs4.min.css' %}">
</head>
<body class="hold-transition sidebar-mini layout-fixed">
<div class="wrapper">
    <!-- Sidebar Container -->
  <aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <a href="#" class="brand-link">
      <span class="brand-text font-weight-light">Hotel Manager</span>
    </a>

    <!-- Sidebar -->
    <div class="sidebar">
      <!-- Sidebar user panel (optional) -->
      <div class="user-panel mt-3 pb-3 mb-3 d-flex">
      
      </div>

      <!-- Sidebar Menu -->
      <nav class="mt-2">
        <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
          <li class="nav-item menu-open">
            <a href="/bostt" class="nav-link">
              <i class="nav-icon fas fa-tachometer-alt"></i>
              <p>
                Tổng quan
              </p>
            </a>
          </li>
          <li class="nav-item menu-open">
            <a href="#" class="nav-link active">
              <i class="nav-icon fas fa-user"></i>
              <p>
                Users
              </p>
            </a>
          </li>
          <li class="nav-item menu-open">
            <a href="/demo" class="nav-link ">
              <i class="nav-icon fas fa-book"></i>
              <p>
                Posts
              </p>
            </a>
          </li>
          <li class="nav-item menu-open">
            <a href="#" class="nav-link ">
              <i class="nav-icon fas fa-table"></i>
              <p>
                Room list
              </p>
            </a>
          </li>
          <li class="nav-item menu-open">
            <a href="#" class="nav-link ">
              <i class="nav-icon fas fa-bars"></i>
              <p>
                Book room
              </p>
            </a>
          </li>
          <li class="nav-item menu-open">
            <a href="#" class="nav-link ">
              <i class="nav-icon fas fa-comments"></i>
              <p>
                Comments
              </p>
            </a>
          </li>
          <li style="margin-top: 300px;" class="nav-item menu-open">
            <a href="/signout" class="nav-link ">
            <i class="fas fa-sign-out-alt"></i>
              <p>
                SignOut
              </p>
            </a>
          </li>
        </ul>
      </nav>
      <!-- /.sidebar-menu -->
    </div>
    
    <!-- /.sidebar -->
  </aside>

  <!-- Content -->
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <div class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1 class="m-0">Users</h1>
          </div><!-- /.col -->
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">User</li>
            </ol>
          </div><!-- /.col -->
        </div><!-- /.row -->
      </div><!-- /.container-fluid -->
    </div>
    <!-- /.content-header -->

    

  <!-- Footer -->
  <footer class="main-footer">
    <strong><a href="#">HotelManager</a></strong>
    <div class="float-right d-none d-sm-inline-block">
      <b>Thecappahotel@gmail.com</b>
    </div>
  </footer>
</div>
</body>
</html>
