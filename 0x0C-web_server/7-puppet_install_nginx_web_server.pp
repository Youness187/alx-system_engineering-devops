# Installs nginx
package { 'nginx':
  ensure => installed,
}

file { 'index.html':
  path    => '/var/www/html/index.html',
  ensure  => present,
  content => 'Hello World!',
}

file_line { 'default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
