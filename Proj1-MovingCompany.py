# Author: [Jaden Nobles]
# COMP163, Section [003]

# CONSTANTS set below
storage_capacity = 1600
facility = 0
# variables set below
request_location = float(input('Where is the next pickup? '))
request_size = float(input('How large is the next pickup? '))
drop_offs = 0
drop_off_size = 0
facility2 = 0
# rest of code below
while drop_offs < 3:
    facility2 = 0
    drop_off_size2 = 0
    while drop_offs < 3 and facility2 == 0:
        if request_location != 0 and request_location >= -5 and request_location <= 5 and request_size >= 1 and request_size <= storage_capacity:
                print('Pick up at:', request_location, 'Size:', request_size, 'cubic feet')
                drop_off_size += request_size
                facility = request_location
                facility2 = 1
        else:
            print('Declined')
            request_location = float(input('Where is the next pickup? '))
            request_size = float(input('How large is the next pickup? '))
        while facility2 == 1:
            facility = request_location
            request_location = float(input('Where is the next pickup? '))
            request_size = float(input('How large is the next pickup? '))
            if request_location == request_location <= facility + 2 and request_location >= facility - 2:
                if request_size <= storage_capacity and request_size > 0 and drop_off_size + request_size <= storage_capacity and request_location < 10 and request_location > -10:
                    print('Pick up at:', request_location, 'Size:', request_size, 'cubic feet')
                    drop_off_size += request_size
                else:
                    print('Declined')
                    print('Dropoff Size:', drop_off_size, 'cubic feet')
                    drop_off_size2 += drop_off_size
                    drop_off_size = 0
                    drop_offs += 1
                    facility2 = 0
                    if drop_offs == 3:
                        print('All done. Total storage amount:', drop_off_size2, 'cubic feet' )
                        break
                    else:
                        request_location = float(input('Where is the next pickup? '))
                        request_size = float(input('How large is the next pickup? '))
            elif request_location < 0 and request_location > facility:
                if request_size <= storage_capacity and request_size > 0 and drop_off_size + request_size <= storage_capacity and request_location < 10 and request_location > -10:
                    print('Pick up at:', request_location, 'Size:', request_size, 'cubic feet')
                    drop_off_size += request_size
                else:
                    print('Declined')
                    print('Dropoff Size:', drop_off_size, 'cubic feet')
                    drop_off_size2 += drop_off_size
                    drop_off_size = 0
                    drop_offs += 1
                    facility2 = 0
                    if drop_offs == 3:
                        print('All done. Total storage amount:', drop_off_size2, 'cubic feet' )
                        break
                    request_location = float(input('Where is the next pickup? '))
                    request_size = float(input('How large is the next pickup? '))
            elif request_location > 0 and request_location < facility:
                if request_size <= storage_capacity and request_size > 0 and drop_off_size + request_size <= storage_capacity and request_location < 10 and request_location > -10:
                    print('Pick up at:', request_location, 'Size:', request_size, 'cubic feet')
                    drop_off_size += request_size
                else:
                    print('Declined')
                    print('Dropoff Size:', drop_off_size, 'cubic feet')
                    drop_off_size2 += drop_off_size
                    drop_off_size = 0
                    drop_offs += 1
                    facility2 = 0
                    if drop_offs == 3:
                        print('All done. Total storage amount:', drop_off_size2, 'cubic feet' )
                        break
                    request_location = float(input('Where is the next pickup? '))
                    request_size = float(input('How large is the next pickup? '))
            else:
                print('Declined')
                print('Dropoff Size:', drop_off_size, 'cubic feet')
                drop_off_size2 += drop_off_size
                drop_off_size = 0
                drop_offs += 1
                facility2 = 0
                if drop_offs == 3:
                    print('All done. Total storage amount:', drop_off_size2, 'cubic feet' )
                    break
                request_location = float(input('Where is the next pickup? '))
                request_size = float(input('How large is the next pickup? '))