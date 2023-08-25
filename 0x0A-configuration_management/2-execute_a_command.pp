# kills a process 
exec { 'pkill killmenow':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
