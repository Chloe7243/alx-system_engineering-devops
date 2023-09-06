# Define a class for Nginx configuration
class nginx_custom_header {

  # Update package repositories and install Nginx
  exec { 'update_apt':
    command => 'apt-get -y update',
    path    => '/usr/bin:/usr/sbin:/bin',
  }

  package { 'nginx':
    ensure  => 'installed',
    require => Exec['update_apt'],
  }

  # Define Nginx service and ensure it is running
  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    require   => Package['nginx'],
    subscribe => Exec['update_apt'],
  }

  # Find the line number for "location / {" in the Nginx default site config
  exec { 'find_line_number':
    command => 'grep -n "location / {" /etc/nginx/sites-enabled/default | cut -d: -f1',
    path    => '/usr/bin:/usr/sbin:/bin',
    unless  => 'test -f /etc/nginx/sites-enabled/default', # Only run if the config file exists
    require => Package['nginx'],
  }

  # Calculate the line number for adding the custom header
  $line_number = Exec['find_line_number'] + 3

  # Add the custom header to the Nginx config file
  file { '/etc/nginx/sites-enabled/default':
    ensure  => present,
    content => template('nginx_custom_header/nginx_config.erb'),
    require => [Package['nginx'], Exec['find_line_number']],
    notify  => Service['nginx'],
  }
}

# Apply the nginx_custom_header class
include nginx_custom_header

