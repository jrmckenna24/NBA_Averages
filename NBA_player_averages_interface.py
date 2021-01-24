# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:22:22 2020

@author: jrmck
"""
import numpy as np
import os
import glob
import pandas 

PPG_PG = RPG_PG = APG_PG = SPG_PG = BPG_PG = FG_PG = THREE_PG = FT_PG = TOV_PG = PGCounter = 0
PPG_SG = RPG_SG = APG_SG = SPG_SG = BPG_SG = FG_SG = THREE_SG = FT_SG = TOV_SG = SGCounter = 0
PPG_SF =  RPG_SF = APG_SF = SPG_SF = BPG_SF = FG_SF = THREE_SF = FT_SF = TOV_SF = SFCounter = 0
PPG_PF =  RPG_PF = APG_PF = SPG_PF = BPG_PF = FG_PF = THREE_PF = FT_PF = TOV_PF = PFCounter = 0
PPG_C =  RPG_C = APG_C = SPG_C = BPG_C = FG_C = THREE_C = FT_C = TOV_C = CCounter = 0
done = 1



#Functions
def menu(): #Displays the menu for users to select from
    print("Welcome! How can I help you today?")
    print("1. League averages for all players in NBA")
    print("2. League averages sorted by position, games played, and average minutes")
    print("3. Average player at each position")
    print("4. Compare two different years")
    print("5. Change the file you are using")
    print("0. Quit program")
    return

def allStats(): #Displays league averages without any filtors
    PPG_mean = csv["PTS"].mean()
    RPG_mean = csv["TRB"].mean()
    APG_mean = csv["AST"].mean()
    SPG_mean = csv["STL"].mean()
    BPG_mean = csv["BLK"].mean()
    MPG_mean = csv["MP"].mean()
    Games_mean = csv["G"].mean()
    FG_mean = csv["FG%"].mean()
    three_mean = csv["3P%"].mean()
    FT_mean = csv["FT%"].mean()
    TOV_mean = csv["TOV"].mean()
    print("  Points: ", round(PPG_mean, 2))
    print("Rebounds: ", round(RPG_mean, 2))
    print(" Assists: ", round(APG_mean, 2))
    print("  Steals: ", round(SPG_mean, 2))
    print("  Blocks: ", round(BPG_mean, 2))
    print(" Minutes: ", round(MPG_mean, 2))
    print("   Games: ", round(Games_mean, 2))
    print("     FG%: ", round(FG_mean, 2))
    print("     3P%: ", round(three_mean, 2))
    print("     FT%: ", round(FT_mean, 2))
    print("     TOV: ", round(TOV_mean, 2))
    print(" ")
    return

def sortedStats(PPG_PG,RPG_PG,APG_PG,SPG_PG,BPG_PG,FG_PG,THREE_PG,FT_PG,TOV_PG,PGCounter,
                PPG_SG,RPG_SG,APG_SG,SPG_SG,BPG_SG,FG_SG,THREE_SG,FT_SG,TOV_SG,SGCounter,
                PPG_SF,RPG_SF,APG_SF,SPG_SF,BPG_SF,FG_SF,THREE_SF,FT_SF,TOV_SF,SFCounter,
                PPG_PF,RPG_PF,APG_PF,SPG_PF,BPG_PF,FG_PF,THREE_PF,FT_PF,TOV_PF,PFCounter,
                PPG_C,RPG_C,APG_C,SPG_C,BPG_C,FG_C,THREE_C,FT_C,TOV_C,CCounter): #Gives league averages based on games and minutes played
    index = csv.index
    index_len = len(index)
    player_last = 0 
    player_current = csv.iloc[0,0]
    
    games_played = int(input("Minimum number of games: "))
    minutes_played = int(input("Minimum number of minutes per game: "))
    for i in range(0,index_len):
        player_current = csv.iloc[i,0]
        if (csv.iloc[i,2] == "PG" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_PG = PPG_PG + csv.iloc[i, 29]
            RPG_PG = RPG_PG + csv.iloc[i, 23]
            APG_PG = APG_PG + csv.iloc[i, 24]
            SPG_PG = SPG_PG + csv.iloc[i, 25]
            BPG_PG = BPG_PG + csv.iloc[i, 26]
            FG_PG = FG_PG + csv.iloc[i, 10]
            THREE_PG = THREE_PG + csv.iloc[i, 13]
            FT_PG = FT_PG + csv.iloc[i, 20]
            TOV_PG = TOV_PG + csv.iloc[i, 27]
            PGCounter = PGCounter+1
            player_last = player_current
            
        if (csv.iloc[i,2] == "SG" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_SG = PPG_SG + csv.iloc[i, 29]
            RPG_SG = RPG_SG + csv.iloc[i, 23]
            APG_SG = APG_SG + csv.iloc[i, 24]
            SPG_SG = SPG_SG + csv.iloc[i, 25]
            BPG_SG = BPG_SG + csv.iloc[i, 26]
            FG_SG = FG_SG + csv.iloc[i, 10]
            THREE_SG = THREE_SG + csv.iloc[i, 13]
            FT_SG = FT_SG + csv.iloc[i, 20]
            TOV_SG = TOV_SG + csv.iloc[i, 27]
            SGCounter = SGCounter+1
            player_last = player_current
            
        if (csv.iloc[i,2] == "SF" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_SF = PPG_SF + csv.iloc[i, 29]
            RPG_SF = RPG_SF + csv.iloc[i, 23]
            APG_SF = APG_SF + csv.iloc[i, 24]
            SPG_SF = SPG_SF + csv.iloc[i, 25]
            BPG_SF = BPG_SF + csv.iloc[i, 26]
            FG_SF = FG_SF + csv.iloc[i, 10]
            THREE_SF = THREE_SF + csv.iloc[i, 13]
            FT_SF = FT_SF + csv.iloc[i, 20]
            TOV_SF = TOV_SF + csv.iloc[i, 27]
            SFCounter = SFCounter+1
            player_last = player_current
        
        if (csv.iloc[i,2] == "PF" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_PF = PPG_PF + csv.iloc[i, 29]
            RPG_PF = RPG_PF + csv.iloc[i, 23]
            APG_PF = APG_PF + csv.iloc[i, 24]
            SPG_PF = SPG_PF + csv.iloc[i, 25]
            BPG_PF = BPG_PF + csv.iloc[i, 26]
            FG_PF = FG_PF + csv.iloc[i, 10]
            THREE_PF = THREE_PF + csv.iloc[i, 13]
            FT_PF = FT_PF + csv.iloc[i, 20]
            TOV_PF = TOV_PF + csv.iloc[i, 27]
            PFCounter = PFCounter+1
            player_last = player_current

        if (csv.iloc[i,2] == "C" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_C = PPG_C + csv.iloc[i, 29]
            RPG_C = RPG_C + csv.iloc[i, 23]
            APG_C = APG_C + csv.iloc[i, 24]
            SPG_C = SPG_C + csv.iloc[i, 25]
            BPG_C = BPG_C + csv.iloc[i, 26]
            FG_C = FG_C + csv.iloc[i, 10]
            if(np.isnan(csv.iloc[i,13]) == 0):
                THREE_C = THREE_C + csv.iloc[i, 13]
                FT_C = FT_C + csv.iloc[i, 20]
                TOV_C = TOV_C + csv.iloc[i, 27]
                CCounter = CCounter+1
            player_last = player_current

            
    PPG_PG = PPG_PG/PGCounter
    RPG_PG = RPG_PG/PGCounter
    APG_PG = APG_PG/PGCounter
    SPG_PG = SPG_PG/PGCounter
    BPG_PG = BPG_PG/PGCounter
    FG_PG = FG_PG/PGCounter
    THREE_PG = THREE_PG/PGCounter
    FT_PG = FT_PG/PGCounter
    TOV_PG = TOV_PG/PGCounter
    
    PPG_SG = PPG_SG/SGCounter 
    RPG_SG = RPG_SG/SGCounter
    APG_SG = APG_SG/SGCounter
    SPG_SG = SPG_SG/SGCounter
    BPG_SG = BPG_SG/SGCounter
    FG_SG = FG_SG/SGCounter
    THREE_SG = THREE_SG/SGCounter
    FT_SG = FT_SG/SGCounter
    TOV_SG = TOV_SG/SGCounter
    
    PPG_SF = PPG_SF/SFCounter
    RPG_SF = RPG_SF/SFCounter
    APG_SF = APG_SF/SFCounter
    SPG_SF = SPG_SF/SFCounter
    BPG_SF = BPG_SF/SFCounter
    FG_SF =FG_SF/SFCounter
    THREE_SF = THREE_SF/SFCounter
    FT_SF = FT_SF/SFCounter
    TOV_SF = TOV_SF/SFCounter
    
    PPG_PF = PPG_PF/PFCounter 
    RPG_PF = RPG_PF/PFCounter
    APG_PF = APG_PF/PFCounter
    SPG_PF = SPG_PF/PFCounter
    BPG_PF = BPG_PF/PFCounter
    FG_PF = FG_PF/PFCounter
    THREE_PF = THREE_PF/PFCounter
    FT_PF = FT_PF/PFCounter
    TOV_PF = TOV_PF/PFCounter
    
    PPG_C = PPG_C/CCounter 
    RPG_C = RPG_C/CCounter
    APG_C = APG_C/CCounter
    SPG_C = SPG_C/CCounter
    BPG_C = BPG_C/CCounter
    FG_C = FG_C/CCounter
    THREE_C = THREE_C/CCounter
    FT_C = FT_C/CCounter
    TOV_C = TOV_C/CCounter
    
    print("Point Guard: ")   
    print("PPG: ", round(PPG_PG, 2))
    print("RPG: ", round(RPG_PG, 2))
    print("APG: ", round(APG_PG, 2))
    print("SPG: ", round(SPG_PG, 2))
    print("BPG: ", round(BPG_PG, 2))
    print("FG%: ", round(FG_PG, 2))
    print("3P%: ", round(THREE_PG, 2))
    print("FT%: ", round(FT_PG, 2))
    print("TOV: ", round(TOV_PG, 2))
    print("")     
    
    print("Shooting Guard: ")   
    print("PPG: ", round(PPG_SG, 2))
    print("RPG: ", round(RPG_SG, 2))
    print("APG: ", round(APG_SG, 2))
    print("SPG: ", round(SPG_SG, 2))
    print("BPG: ", round(BPG_SG, 2))
    print("FG%: ", round(FG_SG, 2))
    print("3P%: ", round(THREE_SG, 2))
    print("FT%: ", round(FT_SG, 2))
    print("TOV: ", round(TOV_SG, 2))
    print("")     
    
    print("Small Forward: ")   
    print("PPG: ", round(PPG_SF, 2))
    print("RPG: ", round(RPG_SF, 2))
    print("APG: ", round(APG_SF, 2))
    print("SPG: ", round(SPG_SF, 2))
    print("BPG: ", round(BPG_SF, 2))
    print("FG%: ", round(FG_SF, 2))
    print("3P%: ", round(THREE_SF, 2))
    print("FT%: ", round(FT_SF, 2))
    print("TOV: ", round(TOV_SF, 2))
    print("")     
    
    print("Power Forward: ")   
    print("PPG: ", round(PPG_PF, 2))
    print("RPG: ", round(RPG_PF, 2))
    print("APG: ", round(APG_PF, 2))
    print("SPG: ", round(SPG_PF, 2))
    print("BPG: ", round(BPG_PF, 2))
    print("FG%: ", round(FG_PF, 2))
    print("3P%: ", round(THREE_PF, 2))
    print("FT%: ", round(FT_PF, 2))
    print("TOV: ", round(TOV_PF, 2))
    print("")     
    
    print("Center: ")   
    print("PPG: ", round(PPG_C, 2))
    print("RPG: ", round(RPG_C, 2))
    print("APG: ", round(APG_C, 2))
    print("SPG: ", round(SPG_C, 2))
    print("BPG: ", round(BPG_C, 2))
    print("FG%: ", round(FG_C, 2))
    print("3P%: ", round(THREE_C, 2))
    print("FT%: ", round(FT_C, 2))
    print("TOV: ", round(TOV_C, 2))
    print("")
    print(PGCounter + SGCounter + SFCounter + PFCounter +CCounter)
    return

def averagePlayers(PPG_PG,RPG_PG,APG_PG,SPG_PG,BPG_PG,FG_PG,THREE_PG,FT_PG,TOV_PG,PGCounter,
                PPG_SG,RPG_SG,APG_SG,SPG_SG,BPG_SG,FG_SG,THREE_SG,FT_SG,TOV_SG,SGCounter,
                PPG_SF,RPG_SF,APG_SF,SPG_SF,BPG_SF,FG_SF,THREE_SF,FT_SF,TOV_SF,SFCounter,
                PPG_PF,RPG_PF,APG_PF,SPG_PF,BPG_PF,FG_PF,THREE_PF,FT_PF,TOV_PF,PFCounter,
                PPG_C,RPG_C,APG_C,SPG_C,BPG_C,FG_C,THREE_C,FT_C,TOV_C,CCounter):
    
    index = csv.index
    index_len = len(index)
    player_last = 0
    player_current = csv.iloc[0,0]
    games_played = int(input("Minimum number of games: "))
    minutes_played = int(input("Minimum number of minutes per game: "))
    
    for i in range(0,index_len):
        player_current = csv.iloc[i,0]
        if (csv.iloc[i,2] == "PG" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_PG = PPG_PG + csv.iloc[i, 29]
            RPG_PG = RPG_PG + csv.iloc[i, 23]
            APG_PG = APG_PG + csv.iloc[i, 24]
            SPG_PG = SPG_PG + csv.iloc[i, 25]
            BPG_PG = BPG_PG + csv.iloc[i, 26]
            FG_PG = FG_PG + csv.iloc[i, 10]
            THREE_PG = THREE_PG + csv.iloc[i, 13]
            FT_PG = FT_PG + csv.iloc[i, 20]
            TOV_PG = TOV_PG + csv.iloc[i, 27]
            PGCounter = PGCounter+1
            player_last = player_current
            
        if (csv.iloc[i,2] == "SG" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_SG = PPG_SG + csv.iloc[i, 29]
            RPG_SG = RPG_SG + csv.iloc[i, 23]
            APG_SG = APG_SG + csv.iloc[i, 24]
            SPG_SG = SPG_SG + csv.iloc[i, 25]
            BPG_SG = BPG_SG + csv.iloc[i, 26]
            FG_SG = FG_SG + csv.iloc[i, 10]
            THREE_SG = THREE_SG + csv.iloc[i, 13]
            FT_SG = FT_SG + csv.iloc[i, 20]
            TOV_SG = TOV_SG + csv.iloc[i, 27]
            SGCounter = SGCounter+1
            player_last = player_current
            
        if (csv.iloc[i,2] == "SF" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_SF = PPG_SF + csv.iloc[i, 29]
            RPG_SF = RPG_SF + csv.iloc[i, 23]
            APG_SF = APG_SF + csv.iloc[i, 24]
            SPG_SF = SPG_SF + csv.iloc[i, 25]
            BPG_SF = BPG_SF + csv.iloc[i, 26]
            FG_SF = FG_SF + csv.iloc[i, 10]
            THREE_SF = THREE_SF + csv.iloc[i, 13]
            FT_SF = FT_SF + csv.iloc[i, 20]
            TOV_SF = TOV_SF + csv.iloc[i, 27]
            SFCounter = SFCounter+1
            player_last = player_current
        
        if (csv.iloc[i,2] == "PF" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_PF = PPG_PF + csv.iloc[i, 29]
            RPG_PF = RPG_PF + csv.iloc[i, 23]
            APG_PF = APG_PF + csv.iloc[i, 24]
            SPG_PF = SPG_PF + csv.iloc[i, 25]
            BPG_PF = BPG_PF + csv.iloc[i, 26]
            FG_PF = FG_PF + csv.iloc[i, 10]
            FT_PF = FT_PF + csv.iloc[i, 20]
            TOV_PF = TOV_PF + csv.iloc[i, 27]
            if(np.isnan(csv.iloc[i,13]) == 0):
                THREE_PF = THREE_PF + csv.iloc[i, 13]
            PFCounter = PFCounter+1
            player_last = player_current
            
        if (csv.iloc[i,2] == "C" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PPG_C = PPG_C + csv.iloc[i, 29]
            RPG_C = RPG_C + csv.iloc[i, 23]
            APG_C = APG_C + csv.iloc[i, 24]
            SPG_C = SPG_C + csv.iloc[i, 25]
            BPG_C = BPG_C + csv.iloc[i, 26]
            FG_C = FG_C + csv.iloc[i, 10]
            if(np.isnan(csv.iloc[i,13]) == 0):
                THREE_C = THREE_C + csv.iloc[i, 13]
            FT_C = FT_C + csv.iloc[i, 20]
            TOV_C = TOV_C + csv.iloc[i, 27]
            CCounter = CCounter+1
            player_last = player_current
            
    PPG_PG = PPG_PG/PGCounter
    RPG_PG = RPG_PG/PGCounter
    APG_PG = APG_PG/PGCounter
    SPG_PG = SPG_PG/PGCounter
    BPG_PG = BPG_PG/PGCounter
    FG_PG = FG_PG/PGCounter
    THREE_PG = THREE_PG/PGCounter
    FT_PG = FT_PG/PGCounter
    TOV_PG = TOV_PG/PGCounter
    
    PPG_SG = PPG_SG/SGCounter 
    RPG_SG = RPG_SG/SGCounter
    APG_SG = APG_SG/SGCounter
    SPG_SG = SPG_SG/SGCounter
    BPG_SG = BPG_SG/SGCounter
    FG_SG = FG_SG/SGCounter
    THREE_SG = THREE_SG/SGCounter
    FT_SG = FT_SG/SGCounter
    TOV_SG = TOV_SG/SGCounter
    
    PPG_SF = PPG_SF/SFCounter
    RPG_SF = RPG_SF/SFCounter
    APG_SF = APG_SF/SFCounter
    SPG_SF = SPG_SF/SFCounter
    BPG_SF = BPG_SF/SFCounter
    FG_SF =FG_SF/SFCounter
    THREE_SF = THREE_SF/SFCounter
    FT_SF = FT_SF/SFCounter
    TOV_SF = TOV_SF/SFCounter
    
    PPG_PF = PPG_PF/PFCounter 
    RPG_PF = RPG_PF/PFCounter
    APG_PF = APG_PF/PFCounter
    SPG_PF = SPG_PF/PFCounter
    BPG_PF = BPG_PF/PFCounter
    FG_PF = FG_PF/PFCounter
    THREE_PF = THREE_PF/PFCounter
    FT_PF = FT_PF/PFCounter
    TOV_PF = TOV_PF/PFCounter
    
    PPG_C = PPG_C/CCounter 
    RPG_C = RPG_C/CCounter
    APG_C = APG_C/CCounter
    SPG_C = SPG_C/CCounter
    BPG_C = BPG_C/CCounter
    FG_C = FG_C/CCounter
    THREE_C = THREE_C/CCounter
    FT_C = FT_C/CCounter
    TOV_C = TOV_C/CCounter
    
    switch_PG = 0
    switch_SG = 0
    switch_SF = 0
    switch_PF = 0
    switch_C = 0
    
    player_PG = 0
    player_SG = 0
    player_SF = 0
    player_PF = 0
    player_C = 0
    
    PG_margin = 0
    SG_margin = 0
    SF_margin = 0
    PF_margin = 0
    C_margin = 0
    
    PG_tmp_margin = 0
    SG_tmp_margin = 0
    SF_tmp_margin = 0
    PF_tmp_margin = 0
    C_tmp_margin = 0

    for i in range(0,index_len):
        player_current = csv.iloc[i,0]
        if (csv.iloc[i,2] == "PG" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PG_margin = (abs(csv.iloc[i,29] - PPG_PG) + 
                         abs(csv.iloc[i,23] - RPG_PG) +
                         abs(csv.iloc[i,24] - APG_PG) + 
                         abs(csv.iloc[i,25] - SPG_PG) + 
                         abs(csv.iloc[i,26] - BPG_PG) +
                         abs(csv.iloc[i,10] - FG_PG) +
                         abs(csv.iloc[i,13] - THREE_PG) +
                         abs(csv.iloc[i,20] - FT_PG) +
                         abs(csv.iloc[i,27] - TOV_PG))
            if switch_PG == 0:
                player_PG = i
                switch_PG = 1
                PG_tmp_margin = PG_margin
                
            if (PG_margin < PG_tmp_margin):
                player_PG = i
                PG_tmp_margin = PG_margin
            player_last = player_current
            
        if (csv.iloc[i,2] == "SG" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            SG_margin = (abs(csv.iloc[i,29] - PPG_SG) + 
                         abs(csv.iloc[i,23] - RPG_SG) +
                         abs(csv.iloc[i,24] - APG_SG) + 
                         abs(csv.iloc[i,25] - SPG_SG) + 
                         abs(csv.iloc[i,26] - BPG_SG) +
                         abs(csv.iloc[i,10] - FG_SG) +
                         abs(csv.iloc[i,13] - THREE_SG) +
                         abs(csv.iloc[i,20] - FT_SG) +
                         abs(csv.iloc[i,27] - TOV_SG))
    
            if switch_SG == 0:
                player_SG = i
                switch_SG = 1
                SG_tmp_margin = SG_margin
                
            if (SG_margin < SG_tmp_margin):
                player_SG = i
                SG_tmp_margin = SG_margin
            player_last = player_current
            
        if (csv.iloc[i,2] == "SF" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            SF_margin = (abs(csv.iloc[i,29] - PPG_SF) + 
                         abs(csv.iloc[i,23] - RPG_SF) +
                         abs(csv.iloc[i,24] - APG_SF) + 
                         abs(csv.iloc[i,25] - SPG_SF) + 
                         abs(csv.iloc[i,26] - BPG_SF) +
                         abs(csv.iloc[i,10] - FG_SF) +
                         abs(csv.iloc[i,13] - THREE_SF) +
                         abs(csv.iloc[i,20] - FT_SF) +
                         abs(csv.iloc[i,27] - TOV_SF))
            if switch_SF == 0:
                player_SF = i
                switch_SF = 1
                SF_tmp_margin = SF_margin
                
            if (SF_margin < SF_tmp_margin):
                player_SF = i
                SF_tmp_margin = SF_margin
            player_last = player_current
            
        if (csv.iloc[i,2] == "PF" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            PF_margin = (abs(csv.iloc[i,29] - PPG_PF) + 
                         abs(csv.iloc[i,23] - RPG_PF) +
                         abs(csv.iloc[i,24] - APG_PF) + 
                         abs(csv.iloc[i,25] - SPG_PF) + 
                         abs(csv.iloc[i,26] - BPG_PF) +
                         abs(csv.iloc[i,10] - FG_PF) +
                         abs(csv.iloc[i,13] - THREE_PF) +
                         abs(csv.iloc[i,20] - FT_PF) +
                         abs(csv.iloc[i,27] - TOV_PF))
         
            if switch_PF == 0:
                player_PF = i
                switch_PF = 1
                PF_tmp_margin = PF_margin
                
            if (PF_margin < PF_tmp_margin):
                player_PF = i
                PF_tmp_margin = PF_margin
            player_last = player_current
            
        if (csv.iloc[i,2] == "C" and csv.iloc[i, 5] > games_played and csv.iloc[i, 7] >= minutes_played and player_last != player_current):
            C_margin = (abs(csv.iloc[i,29] - PPG_C) + 
                         abs(csv.iloc[i,23] - RPG_C) +
                         abs(csv.iloc[i,24] - APG_C) + 
                         abs(csv.iloc[i,25] - SPG_C) + 
                         abs(csv.iloc[i,26] - BPG_C) +
                         abs(csv.iloc[i,10] - FG_C) +
                         abs(csv.iloc[i,20] - FT_C) +
                         abs(csv.iloc[i,27] - TOV_C))
            if(np.isnan(csv.iloc[i,13]) == 0):
                C_margin = C_margin + abs(csv.iloc[i,13] - THREE_C)
            else:
                C_margin = C_margin + THREE_C
    
            if switch_C == 0:
                player_C = i
                switch_C = 1
                C_tmp_margin = C_margin
                
            if (C_margin < C_tmp_margin):
                player_C = i
                C_tmp_margin = C_margin
            player_last = player_current
            
    print(" ")            
    print("Point Guard: ", csv.iloc[player_PG, 1])
    print("PPG: ", round(PPG_PG, 2), "   ", csv.iloc[player_PG, 29])
    print("RPG: ", round(RPG_PG, 2), "    ", csv.iloc[player_PG, 23])
    print("APG: ", round(APG_PG, 2), "     ", csv.iloc[player_PG, 24])
    print("SPG: ", round(SPG_PG, 2), "    ", csv.iloc[player_PG, 25])
    print("BPG: ", round(BPG_PG, 2), "    ", csv.iloc[player_PG, 26])
    print("FG%: ", round(FG_PG, 2), "    ", csv.iloc[player_PG, 10])
    print("3P%: ", round(THREE_PG, 2), "    ", round(csv.iloc[player_PG, 13], 2))
    print("FT%: ", round(FT_PG, 2), "    ", csv.iloc[player_PG, 20])
    print("TOV: ", round(TOV_PG, 2), "    ", csv.iloc[player_PG, 27])
    print("")     
    print("Shooting Guard: ", csv.iloc[player_SG, 1])
    print("PPG: ", round(PPG_SG, 2), "     ", csv.iloc[player_SG, 29])
    print("RPG: ", round(RPG_SG, 2), "      ", csv.iloc[player_SG, 23])
    print("APG: ", round(APG_SG, 2), "      ", csv.iloc[player_SG, 24])
    print("SPG: ", round(SPG_SG, 2), "      ", csv.iloc[player_SG, 25])
    print("BPG: ", round(BPG_SG, 2), "       ", csv.iloc[player_SG, 26])
    print("FG%: ", round(FG_SG, 2), "      ", csv.iloc[player_SG, 10])
    print("3P%: ", round(THREE_SG, 2), "      ", round(csv.iloc[player_SG, 13], 2))
    print("FT%: ", round(FT_SG, 2), "      ", csv.iloc[player_SG, 20])
    print("TOV: ", round(TOV_SG, 2), "      ", csv.iloc[player_SG, 27])
    print("")     
    print("Small Forward: ", csv.iloc[player_SF, 1])
    print("PPG: ", round(PPG_SF, 2), "    ", csv.iloc[player_SF, 29])
    print("RPG: ", round(RPG_SF, 2), "     ", csv.iloc[player_SF, 23])
    print("APG: ", round(APG_SF, 2), "     ", csv.iloc[player_SF, 24])
    print("SPG: ", round(SPG_SF, 2), "     ", csv.iloc[player_SF, 25])
    print("BPG: ", round(BPG_SF, 2), "     ", csv.iloc[player_SF, 26])
    print("FG%: ", round(FG_SF, 2), "     ", round(csv.iloc[player_SF, 10], 2))
    print("3P%: ", round(THREE_SF, 2), "     ", round(csv.iloc[player_SF, 13], 2))
    print("FT%: ", round(FT_SF, 2), "     ", csv.iloc[player_SF, 20])
    print("TOV: ", round(TOV_SF, 2), "     ", csv.iloc[player_SF, 27])
    print("")     
    print("Power Forward: ", csv.iloc[player_PF, 1])
    print("PPG: ", round(PPG_PF, 2), "   ", csv.iloc[player_PF, 29])
    print("RPG: ", round(RPG_PF, 2), "    ", csv.iloc[player_PF, 23])
    print("APG: ", round(APG_PF, 2), "    ", csv.iloc[player_PF, 24])
    print("SPG: ", round(SPG_PF, 2), "    ", csv.iloc[player_PF, 25])
    print("BPG: ", round(BPG_PF, 2), "    ", csv.iloc[player_PF, 26])
    print("FG%: ", round(FG_PF, 2), "    ", round(csv.iloc[player_PF, 10], 2))
    print("3P%: ", round(THREE_PF, 2), "    ", round(csv.iloc[player_PF, 13], 2))
    print("FT%: ", round(FT_PF, 2), "    ", csv.iloc[player_PF, 20])
    print("TOV: ", round(TOV_PF, 2), "    ", csv.iloc[player_PF, 27])
    print("")     
    print("Center: ", csv.iloc[player_C, 1])
    print("PPG: ", round(PPG_C, 2), "   ", csv.iloc[player_C, 29])
    print("RPG: ", round(RPG_C, 2), "    ", csv.iloc[player_C, 23])
    print("APG: ", round(APG_C, 2), "    ", csv.iloc[player_C, 24])
    print("SPG: ", round(SPG_C, 2), "    ", csv.iloc[player_C, 25])
    print("BPG: ", round(BPG_C, 2), "    ", csv.iloc[player_C, 26])
    print("FG%: ", round(FG_C, 2), "    ", csv.iloc[player_C, 10])
    print("3P%: ", round(THREE_C, 2), "    ", round(csv.iloc[player_C, 13], 2))
    print("FT%: ", round(FT_C, 2), "    ", csv.iloc[player_C, 20])
    print("TOV: ", round(TOV_C, 2), "    ", csv.iloc[player_C, 27])
    print("")     
##################################################################

file = input("Hello! Please enter the name of the file you wish to use (.csv): ")

csv = pandas.read_csv(file, header = 0)

while(done != 0):
    menu()
    user_choice = input()
    if (user_choice == "0"):
        done = 0
    if (user_choice == "1"):
        allStats()
    if (user_choice == "2"):
        sortedStats(PPG_PG,RPG_PG,APG_PG,SPG_PG,BPG_PG,FG_PG,THREE_PG,FT_PG,TOV_PG,PGCounter,
                PPG_SG,RPG_SG,APG_SG,SPG_SG,BPG_SG,FG_SG,THREE_SG,FT_SG,TOV_SG,SGCounter,
                PPG_SF,RPG_SF,APG_SF,SPG_SF,BPG_SF,FG_SF,THREE_SF,FT_SF,TOV_SF,SFCounter,
                PPG_PF,RPG_PF,APG_PF,SPG_PF,BPG_PF,FG_PF,THREE_PF,FT_PF,TOV_PF,PFCounter,
                PPG_C,RPG_C,APG_C,SPG_C,BPG_C,FG_C,THREE_C,FT_C,TOV_C,CCounter)
    if (user_choice == "3"):
        averagePlayers(PPG_PG,RPG_PG,APG_PG,SPG_PG,BPG_PG,FG_PG,THREE_PG,FT_PG,TOV_PG,PGCounter,
                PPG_SG,RPG_SG,APG_SG,SPG_SG,BPG_SG,FG_SG,THREE_SG,FT_SG,TOV_SG,SGCounter,
                PPG_SF,RPG_SF,APG_SF,SPG_SF,BPG_SF,FG_SF,THREE_SF,FT_SF,TOV_SF,SFCounter,
                PPG_PF,RPG_PF,APG_PF,SPG_PF,BPG_PF,FG_PF,THREE_PF,FT_PF,TOV_PF,PFCounter,
                PPG_C,RPG_C,APG_C,SPG_C,BPG_C,FG_C,THREE_C,FT_C,TOV_C,CCounter)
    
    '''if (user_choice == "4"):
        second_year = input("Please input the file of the second year you would like to compare to: ")
        csv_second = pandas.read_csv(second_year, header = 0)
        filter_input = input("Do you want to filter the averages?(Y/N) ")
        if (filter_input == "N"):
            '''
            
        
    if (user_choice == "5"):
        new_file = input("Please enter the file name you wish to use (.csv): ")
        csv = pandas.read_csv(new_file, header = 0)
    
        
