# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
package { 'nginx':
  ensure => installed,
}

file_line { 'default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "\tadd_header X-Served-By \$HOSTNAME;\n",
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
