#search and replace bad name
exec {'web debugging':
  command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  provider => shell,
}
exec {'apache start':
  command  => '/etc/init.d/apache2 restart',
  provider => shell,
}
