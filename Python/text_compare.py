import diff_match_patch as dmp_module

def diff(text1,text2):
	dmp = dmp_module.diff_match_patch()
	diff = dmp.diff_main(text1, text2)
	dmp.diff_cleanupSemantic(diff)
