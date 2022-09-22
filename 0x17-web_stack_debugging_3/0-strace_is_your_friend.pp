#fixing apache bug
exec {'fixing bug':
  command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  provider => shell,
}
exec {'apache restart':
  command  => '/etc/init.d/apache2 restart',  
  provider => shell,
}

