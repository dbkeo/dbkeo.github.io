Title: Hosting a Pelican blog on Github (1st post)
Date: 2014-07-07 14:01
Slug: pelican-github-blog
Author: Tom Pollard
Summary: Creating a static blog with Pelican, Github, and Disqus

This blog was created with the help of:

* [Gandi](http://gandi.net/), to register the domain name. Gandi in my experience are excellent. Zero spam, no upselling of unnecessary packages, and great community support. Plus, as far as I know, the staff [aren't elephant hunters](http://www.huffingtonpost.com/2011/03/31/bob-parsons-godaddy-ceo-elephant-hunt_n_843121.html).
* [Pelican](http://getpelican.com/), a simple python framework for creating static websites. Lacks the pizzazz of frameworks like Django, but that's okay (/good).
* [Monospace theme](https://github.com/getpelican/pelican-themes/tree/master/monospace) for Pelican. Might change later, but I like the simple look for now.
* [Github](https://github.com/), for hosting the site. Offers free hosting for a single website, which is nice.
* [Disqus](https://disqus.com/), to allow comments. Initially I'd wanted to avoid relying on an external service for comments, but the simplicity of Disqus was difficult to argue with. They have nice customer service too, as it turns out.

The rough process was:

1. Create a [personal site](https://pages.github.com/) on Github.
2. Register a domain with Gandi. [Point domain](http://wiki.gandi.net/dokuwiki/en/dns/zone/a-record) to Github via the zone file. The settings will take a few hours to propogate.
3. [Clone Pelican](https://github.com/getpelican/) into a local folder, on a branch named 'source'
4. Add the theme files to the source branch.
5. Add personal settings to the [pelicanconf.py](https://github.com/tompollard/tompollard.github.io/blob/source/pelicanconf.py) and [publishconf.py](https://github.com/tompollard/tompollard.github.io/blob/source/publishconf.py) files. 
6. Add a favicon.ico and CNAME file to the source folder.
7. Modify the 'github' command in the [Makefile](https://github.com/tompollard/tompollard.github.io/blob/source/Makefile) to push to a personal site, rather than project site. Also add line to the 'publish' command to copy the favicon and CNAME files.
8. Add blog posts to the content folder.
9. Run 'make github', which compiles the site on the 'master' branch and pushes to Github.
10. For an overview of the file structure, see the [source](https://github.com/tompollard/tompollard.github.io/tree/source) and [master](https://github.com/tompollard/tompollard.github.io) branches on Github.

So now, to add a new blog post, I create a markdown file to the content folder (on the source branch) and run 'make github'. Easy!
