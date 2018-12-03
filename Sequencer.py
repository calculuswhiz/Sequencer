import sublime
import sublime_plugin
import re, math

class SequencerPromptCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def Sequence(input):
			self.view.run_command('generate_sequence', { 'args' : input })
		
		settings = sublime.load_settings("Sequencer.sublime-settings")
		start = settings.get('start')
		interval = settings.get('interval')
		flags = settings.get('flags')
		command = (start + ' ' + interval + ' ' + flags).strip()
		
		sublime.active_window().show_input_panel('[start number] [interval] [flags (see README for flags)]', command, Sequence, None, None)
		
class GenerateSequenceCommand(sublime_plugin.TextCommand):
	def run(self, edit, args = None):
		config = {}
		
		if args is None:
			settings = sublime.load_settings("Sequencer.sublime-settings")
			args = str(settings.get('start')) + ' '
			args += str(settings.get('interval')) + ' '
			args += settings.get('flags')
			
		args = args.strip()
		if args == "":
			return
		else:
			args = args.split(' ')	
	
		# Parse arguments
		for argI in range(len(args)):
			arg = args[argI]
			if argI is 0:
				config['start'] = arg
			elif argI is 1:
				config['interval'] = arg
			else:
				flagMatch = re.match('([a-zA-Z]+)(:(\\w))?', arg)
				if flagMatch:
					config[flagMatch.group(1).lower()] = flagMatch.group(3)
		
		if 'interval' in config:
			interval = float(config['interval'])
		else:
			interval = 1
		
		counter = float(config['start'])
		isFloatSeq = False
		if 'f' in config:
			isFloatSeq = True
		
		if 'w' in config:
			padding = int(config['w'])
		else:
			padding = 0
			
		isPrefixMode = False
		if 'pre' in config:
			isPrefixMode = True
			
		for pos in self.view.sel():
			counterOut = counter
			if not isFloatSeq:
				counterOut = math.floor(counter)
			
			if isPrefixMode:
				position = pos.begin()
			else:
				position = pos.end()
				
			self.view.insert(edit, position, str(counterOut).zfill(padding))

			counter += interval

