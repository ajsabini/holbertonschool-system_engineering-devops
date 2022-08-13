# kill proess
exec { 'killmenow':
  command  => '',
  provider => 'shell',
  returns  => [0, 1],
}
