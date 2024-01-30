import datetime

file=open("output.txt","wt")
file.write("future programmer")
file.write(f"\tISLAMIC UNIVERSIRTY IN UGANDA\n\t\tKAMPALA COMPUS \n\t\tP.O.BOX 2223 \nNAME:\t\t\tRASHIDAH ABBAS\t\nREG NO:\t\t\t223-063012-27600 \nLECTURER NAME:\t\tMR.HAKIM \nDATE:\t\t\t{datetime.date.today()} \t\nCOURSE UNIT:\t\tSTRUCTURED PROGRAMMING \n\t\t**** END ****")
print (f"\tISLAMIC UNIVERSIRTY IN UGANDA\n\t\tKAMPALA COMPUS \n\t\tP.O.BOX 2223 \nNAME:\t\t\tRASHIDAH ABBAS\t\nREG NO:\t\t\t223-063012-27600 \nLECTURER NAME:\t\tMR.HAKIM \nDATE:\t\t\t{datetime.date.today()} \t\nCOURSE UNIT:\t\tSTRUCTURED PROGRAMMING \n\t\t**** END ****")