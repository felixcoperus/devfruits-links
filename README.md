# devfruits-links
Simple hobby project to manage links on devfruits homepage via powershell interface.

## Use python on the webserver
- `cd` to the links folder, then call one of the python files to change links, e.g. `python3 add.py Misc http://bla.com 'The bla page'`
- See the scripts for what input is expected
- All links are in categories, to edit categories use the scripts prefixed with 'c'

## Use powershell interface
- Create the folder '~/Documents/WindowsPowershell/Modules/MyModule`
- Put the Module.ps1 file into that folder, and rename it to 'MyModule.ps1'
- Run `Import-Module MyModule`
- Now you can use the functions in that module.
- You can also load the functions seperately, but you'll have to do that then every time you start powershell

# Commands
The powershell interface adds a call to publish.py to every action that edits the link list. Publish.py creates a new index.html based on the info in links.json.

## Add-Link
- add.py
- Adds a link to a category. If the category does not exist, it will be created.

## Remove-Category
- cdelete.py
- Removes a category. If a TargetCategory is given, existing links will be moved to the target category before the source category is removed
- Can be used to rename a category, just give the new name as the target category, as the target will be created if it doesn't exist

## Remove-Link
- delete.py
- Deletes a link. The input is a single UUID. To get the UUID, run Get-Link

## Get-Link
- list.py
- Returns all links in the format `<uuid> <title> <link>`

## Move-Link
- move.py
- Used to move a link to another category
- First arg is the UUID of the link, the second is the target category

## Set-Category
- cmove.py
- Used to change the order of categories
- Input: 'category', 'order(int)'

## Get-Category
- clist.py
- Prints out `<order> <category name>`
