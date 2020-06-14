import logparser as logparser
from logparser import LONGDATE1, SEPARATOR1, VECTORR, parser


def main(logfile="example.log", linemarker=LONGDATE1, separator=SEPARATOR1): 
    listlines = parser.parselog(linemarker, separator, logfile, VECTORR)
    return listlines


if __name__ =="__main__":
    main()