#fixing apache bug
exec { 'fixing':
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  provider => shell,
}

exec { 'apache restart':
  command  => '/etc/init.d/apache2 restart',  
  provider => shell,
}
