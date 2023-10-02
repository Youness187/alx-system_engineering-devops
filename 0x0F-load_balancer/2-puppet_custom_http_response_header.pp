# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
package { 'nginx':
  ensure => installed,
}

exec { 'command':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default',
  provider => shell,
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
