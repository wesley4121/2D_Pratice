import pygame,sys
##_map_tile


##_map
map1 = """
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
       WWWWW WWWWWWWWWWWWWWWW                  WWWWW WWWWWWWWWWWWWWWW                  WWWWW WWWWWWWWWWWWWWWW           
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                W                                       W                                       W                       
                W                                       W                                       W                       
         WWW    WW                                      W                                       W                       
       WWWWW  WWWWWW                                    W                                       W                       
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"""

def getMapStr(map) -> list:
    if map ==1 :
        return map1.splitlines()
    