# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
package { 'nginx':
  ensure => installed,
}

$lin = "add_header X-Served-By ${hostname};"

-> file_line { 'default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => $lin,
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
