from os import listdir

# listdir contains the filenames of all the `.yml` files
# print(listdir())

# open the output file
with open( 'SUMMARY.csv', 'w') as out:
    # print output file header
    print( 'name,x,z,', file=out)

    # open warpfiles
    for warpfile in listdir():
        with open( warpfile , 'r') as f: #keeps file open 
            linenum = 0
            for str_line in f: # reads every line
                # TODO: from here on out, this needs to be edited
                str_line = str_line.split()
                str_line = str_line[1]
                name = ''
                x_coord = ''
                z_coord = ''
                linenum = linenum + 1 
                if linenum == 2:
                    x_coord = str_line
                elif linenum == 4:
                    z_coord = str_line
                elif linenum == 7:
                    name = str_line 
            
                
                # # split each line into an `temp_N`, and `temp_P`
                # str_N, str_P = str_line.split()
                # # call the `move_digits` function, store the result
                # x = (str_N,str_P) # takes info from warps 
                # # print the result to the console

                outstring = (
                    '%s,%s,%s'
                    %
                    ( name, x_coord, z_coord,)
                )
                print( outstring, file=out)


#open folder 
# make list of all folder names 
# read each part of list and open file
# from each file read each line 
# make lists of name, x, y ,z , name  ...
# print lists and copy into spreadsheets 
# seperate by commas 