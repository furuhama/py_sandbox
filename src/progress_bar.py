import sys
import time

END = 170

MAX_LEN = 30

def get_progressbar_str(prog):
    BAR_LEN = int(MAX_LEN * prog)
    return ('[' + '=' * BAR_LEN +
            ('>' if BAR_LEN < MAX_LEN else '') +
            ' ' * (MAX_LEN - BAR_LEN) +
            '] %.1f%%' % (prog * 100.))

for i in range(END + 1):
    time.sleep(0.01)
    progress = 1.0 * i / END
    sys.stderr.write('\r\033[K' + get_progressbar_str(progress))
    sys.stderr.flush()

sys.stderr.write('\n')
sys.stderr.flush()
