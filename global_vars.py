#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:42:20 2017

@author: tz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:16:40 2017

@author: tz
"""

a=1
b=2
def process_image():
    global a
    global b
    
    a, b = a*2, b*2
    c=3
    return c
 

    
def main():
    print(a)

    for i in [1,2,3]:
        print(process_image())
        print(a)
        
    
    
    
if __name__ == '__main__':
    main()


