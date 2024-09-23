## Basic Networking tools

**ipconfig** (Windows) 
**ifconfig** (Mac & Linux)
- Displays network interface configuration for all Internet Protocol (IP) devices
- **Usage:**
- ipconfig /? (Windows)
- ifconfig -h (Mac & Linux)
- **Manual:**
- man ifconfig (Mac & Linux)
- **Examples:**
-  ipconfig /all (Windows)
-  ifconfig -a (Mac & Linux)

## Basic Network Tools
**dig**
**host**
**nslookup (deprecated)**
- Looks up IP addresses for named servers; also reverses lookups
- ** Usage:**
	- dig -h
- **Manual:**
	- man dig
- Examples:
	- dig google.com
	- dig tagmatasecurity.com
	- dig -x [IP address]
	- dig tagmatasecurity.com MX
	- The host command provides very similar functionality and has a
	friendlier output format.
- dig and host are not provided with Windows but you can download
dig from http://www.isc.org/downloads/. By default, Windows uses
nslookup, which has been deprecated for many years.

Basic Network Tools
**netstat**
	- Displays network connections and other related information
- **Usage:**
	- netstat /? (Windows)
	- netstat -h (Mac & Linux)
- **Manual:**
	- man netstat (Mac & Linux)
- **Examples:**
	- netstat -n
	- netstat -a
	- netstat -e
	- netstat -s
	- netstat -r
## Basic Network Tools

**ping**
	- Sends an echo request to a remote host and reports the results
- ** Usage:**
	- ping /? (Windows)
	- ping -h (Mac & Linux)
- **Manual:**
	- man ping (Mac & Linux)
- **Examples:**
	- ping -n 4 tagmatasecurity.com (Windows)
	- ping -c 4 tagmatasecurity.com (Mac & Linux)
