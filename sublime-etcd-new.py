import sublime, sublime_plugin
 
class ETCDNewCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	import urllib2
    	response = urllib2.urlopen('https://discovery.etcd.io/new')
		etcd_token = response.read()

        self.view.insert(edit, 0, etcd_token)