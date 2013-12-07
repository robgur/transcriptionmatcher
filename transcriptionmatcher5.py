import csvimport osimport codecsimport itertools as itimport numpy as npimport refrom fuzzywuzzy import fuzzfrom fuzzywuzzy import process from collections import defaultdictcsvname = raw_input('Enter name of your file: ')while (not os.path.isfile(csvname)):   print 'There is no file named', csvname  csvname = raw_input('Enter location and name of your file: ')csvfile=open(str(csvname), 'rb')#opens csv fileheader=csvfile.next()header=header.translate(None,"\000")headlist=re.split(',', header)print "Your file has the following fields: "print '\n'.join(headlist)#list fields in csvuserheader = raw_input('Get text matching scores for which field?: ')while (not str(userheader) in headlist):   print 'There is no header field named', userheader   userheader = raw_input('Get text matching scores for which field?: ')#user can pick a field for processingprint 'Processing...'   csvfile=open(str(csvname), 'rb')dictReader = csv.DictReader(x.replace('\000', '') for x in csvfile)#reopens file and creates dictionary that has null chars removedTransDat = [row for row in dictReader] subj_uniqid = [(i['subject_id'],i[str(userheader)]) for i in TransDat]newsubid=defaultdict(list)for k,v in subj_uniqid:  newsubid[k].append(v)newsubsc=defaultdict(list)for newsubid_key,newsubid_values in newsubid.iteritems():      for pair in it.combinations(newsubid_values,2) :         pair=map(str.lower, pair)         c=int(fuzz.token_sort_ratio(str(pair[0]),str(pair[1])))         newsubsc[newsubid_key].append(c)#create a dictionary of lists.  Loop through contents of newsubid, get selected field values related to each subj_id, take all combinations of those values, lower case them, and then run fuzz.token_sort_ratio on each combination, send the scores to that dictionary of lists with subj_id as key and fuzzymatch scores as integer values.print '{:30} {:2} {:7} {:2} {:8} {:2} {:7}'.format('subject_id', '\t', '    #compare', '\t', 'avgmatch', '\t', 'stddev')for newsubsc_key, newsubsc_values in newsubsc.iteritems():        length=int(len(newsubsc_values))        avg=sum(newsubsc_values)/len(newsubsc_values)        stddev=np.std(newsubsc_values)        print '{:30} {:2} {:7} {:2} {:8} {:2} {:5.3f}'.format(str(newsubsc_key), '\t', length, '\t',avg, '\t', stddev)#last step is to simply print out a summary, right now to STDOUT, which includes the subj_id, number of combinations tried,  average of all scores for a particular field and subj_id, and standard deviation.  