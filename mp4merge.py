__author__ = 'Jean-Bernard Ratte - jean.bernard.ratte@unary.ca'

import os
import subprocess


SOURCE_FOLDER = "Where are located the containing folder of MP4s to merge? "
CONFLICTING_MERGE = "Prompt conflicting merges (Y/N)? "
BATCH_MERGE = "Merge all video in subfolders (Y/N)? "
VALIDATION = ' - The output file is named "%s"'
MERGE_THIS = ' - Do you want to merge for "%s" (Y/N)? '
ERROR_FILE_COUNT = ' /!\ Could not merge, not enough files in folder %s'


def is_choice(val):
    if val.upper() in ['Y', 'N']:
        return True


def ask(msg, keep_asking=None):
    resp = str(raw_input(msg))

    if is_choice(resp):
        if resp.upper() == "Y":
            return True

        else:
            return False

    print '/!\ Invalid answer'
    if keep_asking:
        ask(msg, keep_asking=keep_asking)


def append_dir(dirname, filename):
    return ''.join([dirname, '/', filename])


def ask_source(msg, keep_asking=None):
    resp = str(raw_input(msg))

    if os.path.exists(resp):
        return resp

    print '/!\ Invalid path'
    if keep_asking:
        ask_source(msg, keep_asking=keep_asking)


def build_cmd(dir, output, *files):
    files = list(files)
    return ["mp4box", "-force-cat", "-add", append_dir(dir, files.pop(0))] + \
           [cat for pairs in [["-cat", append_dir(dir, s)] for s in files] for cat in pairs] + \
           [append_dir(dir, output)]


if __name__ == '__main__':
    print '---------------------------------'
    print '-     This tool uses MP4Box     -'
    print '-  http://gpac.sourceforge.net  -'
    print '---------------------------------'

    created_files = []

    try:
        version = subprocess.Popen(['mp4box', '-version'], stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE).communicate()[0]

        prompt_conflict = ask(CONFLICTING_MERGE, keep_asking=True)
        is_batch = ask(BATCH_MERGE, keep_asking=True)

        if not prompt_conflict:
            source = ask_source(SOURCE_FOLDER, keep_asking=True)
            print ' - Preparing for merge'

            for dirname in [s for s in os.listdir(source) if not s[0] == '.']:
                fulldir = source +'/'+ dirname
                filenames = [s for s in os.listdir(fulldir) if not s[0] == "." and s.find('.mp4') > -1]
                output = ''.join([dirname[dirname.rfind("/") + 1:], '.mp4'])
                merge = True

                if not is_batch:
                    merge = ask(MERGE_THIS % output, keep_asking=True)

                if merge:

                    if len(filenames) > 1:
                        print VALIDATION % output
                        print ' - Merging...'
                        result = subprocess.Popen(build_cmd(fulldir, output, *filenames), stderr=subprocess.STDOUT,
                            stdout=subprocess.PIPE).communicate()[0]
                        created_files.append(append_dir(fulldir, output))

                    else:
                        print ERROR_FILE_COUNT % dirname[dirname.rfind("/") + 1:]

                else:
                    print ' - Skipping'

            print "Done!"

    except OSError:
        print '/!\ Unable to check MP4Box version, you should check your MP4Box installation'
        print '/!\ Compile from source, see http://gpac.sourceforge.net/'

    except (KeyboardInterrupt, SystemExit):
        print '\r\n/!\ Deleting newly created files'

        for file in created_files:
            subprocess.call(['rm', file])

        print 'Bye.'