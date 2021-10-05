$PrivateKeyPath = "C:\Users\Installer\.ssh\pushvid.ppk"

Function Add-Link {
    param(
        $Link, 
        $Title,
        $Description,
        $Category = 'misc',
        $PrivateKeyPath = $script:PrivateKeyPath        
    )

    # Compile script to be run on the linux host
    $script = "cd /home/user/www/devfruits/links`n"
    $script += "python3 add.py '$Category' '$Link' '$Title' '$Description'`n"
    $script += "python3 publish.py"
    [System.IO.File]::WriteAllLines("$($env:TEMP)\_addlink.sh", $script)

    # Run script
    plink -batch -i $PrivateKeyPath user@web002 -m "$($env:TEMP)\_addlink.sh"
}

Export-ModuleMember -Function Add-Link

Function Remove-Link {
    param(
        $uuid, 
        $PrivateKeyPath = $script:PrivateKeyPath        
    )

    # Compile script to be run on the linux host
    $script = "cd /home/user/www/devfruits/links`n"
    $script += "python3 delete.py '$uuid'`n"
    $script += "python3 publish.py"
    [System.IO.File]::WriteAllLines("$($env:TEMP)\_removelink.sh", $script)

    # Run script
    plink -batch -i $PrivateKeyPath user@web002 -m "$($env:TEMP)\_removelink.sh"
}

Export-ModuleMember -Function Remove-Link

Function Move-Link {
    param(
        $UUID, 
        $TargetCategory,
        $PrivateKeyPath = $script:PrivateKeyPath
    )

    # Compile script to be run on the linux host
    $script = "cd /home/user/www/devfruits/links`n"
    $script += "python3 move.py '$UUID' '$TargetCategory'`n"
    $script += "python3 publish.py"
    [System.IO.File]::WriteAllLines("$($env:TEMP)\_movelink.sh", $script)

    # Run script
    plink -batch -i $PrivateKeyPath user@web002 -m "$($env:TEMP)\_movelink.sh"
}

Export-ModuleMember -Function Move-Link

Function Get-Link {
    param(
        $Category = $null,
        $PrivateKeyPath = $script:PrivateKeyPath     
    )

    # Compile script to be run on the linux host
    $script = "cd /home/user/www/devfruits/links`n"
    if ($null -ne $Category){
        $script += "python3 list.py '$Category'"
    } else {
        $script += "python3 list.py"
    }
    [System.IO.File]::WriteAllLines("$($env:TEMP)\_listlink.sh", $script)

    # Run script
    plink -batch -i $PrivateKeyPath user@web002 -m "$($env:TEMP)\_listlink.sh"
}

Export-ModuleMember -Function Get-Link

Function Get-Category {
    param(
        $PrivateKeyPath = $script:PrivateKeyPath        
    )

    # Compile script to be run on the linux host
    $script = "cd /home/user/www/devfruits/links`n"
    $script += "python3 clist.py"
    [System.IO.File]::WriteAllLines("$($env:TEMP)\_listcat.sh", $script)

    # Run script
    plink -batch -i $PrivateKeyPath user@web002 -m "$($env:TEMP)\_listcat.sh"
}

Export-ModuleMember -Function Get-Category

Function Set-Category {
    param(
        $Category,
        $Order,
        $PrivateKeyPath = $script:PrivateKeyPath        
    )

    # Compile script to be run on the linux host
    $script = "cd /home/user/www/devfruits/links`n"
    $script += "python3 cmove.py '$Category' '$Order'`n"
    $script += "python3 publish.py"
    [System.IO.File]::WriteAllLines("$($env:TEMP)\_movecat.sh", $script)

    # Run script
    plink -batch -i $PrivateKeyPath user@web002 -m "$($env:TEMP)\_movecat.sh"
}

Export-ModuleMember -Function Set-Category

Function Remove-Category {
    param(
        $Category,
        $TargetCategory,
        $PrivateKeyPath = $script:PrivateKeyPath        
    )

    # Compile script to be run on the linux host
    $script = "cd /home/user/www/devfruits/links`n"
    $script += "python3 cdelete.py '$Category' '$TargetCategory'`n"
    $script += "python3 publish.py"
    [System.IO.File]::WriteAllLines("$($env:TEMP)\_deletecat.sh", $script)

    # Run script
    plink -batch -i $PrivateKeyPath user@web002 -m "$($env:TEMP)\_deletecat.sh"
}

Export-ModuleMember -Function Remove-Category
