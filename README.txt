[^]Who doesn't like a mediocre denial of service attack tool?
[?]RAZE v0.3 
[?]IDGADWUDWTC License (I DON'T GIVE A DAMN WHAT YOU DO WITH THE CODE)
[?]This program uses several external libraries that you will need to be able to run
[?]Libs: colorama(for text color), requests(for requests) 
[!]Project is work in progress so please don't mock my inability to use the argparse library.
[!]Raze uses not so advanced techniques to mass send get requests to a website using the requests library.
[!]I decided to use requests because it's easy to learn/use and it does the job. I'm working on adding a 
[!]special feature which could disguise an attack as a webcrawler (some ddos protection services allow 
[!]webcrawlers to send a more than usual amount of requests). It will in really just send a modified request 
[!]every two normal requests which will usually result in a 404 return code. The modified request will request the
[!]target for a file or sub-directory in the website that usually won't exist, hence the 404 return code.
[!]i.e. : instead of: requests.get('http://www.google.com') it will request: 'http://www.google.com/login'
[!]This may be able to trick some ddos protection services into allowing the requests through (very experimental)

[-]To be honest, I don't even know if this has been done before. Hell, I don't even know if this will work...
[-]Oh well, it's worth a shot.
