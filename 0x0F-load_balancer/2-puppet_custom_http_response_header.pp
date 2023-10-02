# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
package { 'nginx':
  ensure => installed,
}

exec { 'default':
  command => 'sed -r -i "/^\s+server_name .+;/a\ \\tadd_header X-Served-By \$HOSTNAME\;\n" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
