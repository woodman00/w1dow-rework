from colorama import Fore

res = Fore.RESET
lye = Fore.LIGHTYELLOW_EX
lre = Fore.LIGHTRED_EX


menu = f"""
{lye}
[1] - Found Nick Information
[2] - Find Torrent Information
[3] - Find Phone or Car Number Information
{lre}[4] - Exit {res}
"""

chsystem = f"""
{lre}[!]Choose Your System[!]{lye}
[1] - Windows
[2] - Linux/Termux{res}
"""

banner = f""" {lye}
          $                 $
        $$                  $$
       $$                    $$
       $$                     $$
       $$                     $$
       $$                     $
       $$                     $
    $$ $$                    $$  $
    $$  $$                   $$  $$
   $$    $$                 $$    $$
   $      $$$              $$$     $$
   $$      $$$           $$$      $$
   $$$      $$$  $$$$$  $$     $$$$$
    $$$$$$   $$$$$$$$$ $$   $$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
   $$$ $$$$$$$$$$$$$$$$$$$$$$$$  $$$
  $$$         $$$$$$$$$$$$         $$
 $$         $$$$$$$$$$$$$$$$$       $$
 $$     $$$$$$$$$$$$$$$$$$$$$$$$    $$$
$$     $$$  $$$$$$$$$$$$$$$$  $$     $$
 $$    $$   $$$$$$$  $$$$$$$   $     $
  $    $$   $$$$$$$  $$$$$$$   $    $
   $   $$   $$$$$$$$$$$$$$$$  $$   $
    $  $$    $$$$$$$$$$$$$$   $$
       $$     $$$$$$$$$$$$    $$
       $$       $$$$$$$$      $$
        $$                   $$

  {lye}[>>] created by {lre}malorento
  {lye}[>>] for channels {lre}"@bh_menu" {lye}and{lre} "staide"
  {lye}[>>] the idea belongs to {lre}NezukA{res}
"""

sher_menu = f"""{lye}
[1] - Phone Information
[2] - Car Information{res}
"""
print(banner)
print(menu)
