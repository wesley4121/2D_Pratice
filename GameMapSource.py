import pygame,sys
##_map_tile


##_map
map1 = """
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                               WWWWWWWWWWWWWWWWWWWWW                    
                                                                                                                        
                                                                                                                        
                                                              WWWWWWWWWWWWW                                             
                                                                                                                        
                                                   WWWW                                                                 
                                                                                                                        
                                                                                                                        
                                          WWWWW                                                                         
                                 WWWW                                                                                   
                          WWWWW                                                                                         
                  WWWW                                                                                                  
          WWWWW                                                                                                         
                                                                                                                        
                                                                                                                        
WWW  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                               WWWWWWWWWWWWWWWWWWWWW                    
                                                                                                                        
                                                                                                                        
                                                              WWWWWWWWWWWWW                                             
                                                                                                                        
                                                   WWWW                                                                 
                                                                                                                        
                                                                                                                        
                                          WWWWW                                                                         
                                 WWWW                                                                                   
                          WWWWW                                                                                         
                  WWWW                                                                                                  
          WWWWW                                                                                                         
                                                                                                                        
                                                                                                                        
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"""

def getMapStr(index) -> list:
    if index ==1 :
        return map1.splitlines()
    