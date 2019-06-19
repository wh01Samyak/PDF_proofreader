import diff_match_patch as dmp_module

def diff(text1,text2):
	dmp = dmp_module.diff_match_patch()
	diff = dmp.diff_main(text1, text2)
	errors = dmp.diff_cleanupSemantic(diff)
	return errors


