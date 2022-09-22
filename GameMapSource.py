import pygame,sys
##_map_tile


##_map
map1 = """
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
       WWWWW WWWWWWWWWWWWWWWW           
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                W                       
                W                       
         WWW    WW                      
       WWWWW  WWWWWW                    
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"""

@staticmethod
def getMapStr(map) -> list:
    if map ==1 :
        return map1.splitlines()
    