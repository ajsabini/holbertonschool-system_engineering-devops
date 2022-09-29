#change OS config for login w/holberton user
exec {'change OS':
    command => '',
    provider => shell,
}
