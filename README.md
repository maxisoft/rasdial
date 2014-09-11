#Rasdial

Library to manipulate windows VPN connections with [Python programming language](https://www.python.org/).  
Behind the hood, this library use the [rasdial](http://technet.microsoft.com/en-us/library/ff859533%28WS.10%29.aspx) 
command to perform desired actions.

This library allow to programmatically :  
    * (re)connect to a vpn  
    * disconnect a vpn connection  
    * get the current connected vpn connection's name  

##example
```python
import rasdial

rasdial.get_current_vpn()  # return the current vpn name as string
rasdial.connect('MyVpnConnection', 'user', 'password')  # connect to a vpn
rasdial.disconnect('MyVpnConnection')  # close a vpn connection
```





