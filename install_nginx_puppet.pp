# install nginx and create redirects
package {'nginx':
        ensure => installed
}

file {'/var/www/html/index.nginx-debian.html':
  mode    => '0744',
  content => "Hello World!\n"
}

file_line {'redirections':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => "\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n"
}

service {'nginx':
  ensure => running
}
