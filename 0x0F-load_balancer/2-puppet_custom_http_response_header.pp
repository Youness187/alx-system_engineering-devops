# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
exec { 'update':
  command => '/usr/bin/apt-get update -y',
}

package { 'nginx':
  ensure => installed,
}

file_line { 'default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By ${hostname};",
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
