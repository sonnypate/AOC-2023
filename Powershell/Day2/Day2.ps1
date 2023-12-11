function Get-GameID {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Line
    )
    
    $re = $Line -match "^Game (?'GameID'\d+)"
    $gameID = $Matches["GameID"]
    
    return $gameID
}

function Get-CubeCount {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Line,

        [Parameter(Mandatory)]
        [ValidateSet('Red', 'Green', 'Blue')]
        [string]$Color
    )
    
    $re = $Line.Split(';') | Select-String -Pattern "(?'CubeCount'\d+) $($Color.ToLower())"
    if ($re.Matches) {
        $cubes = @($re.Matches.ForEach({$_.Groups[1].Value}))

    }
    else {
        $cubes = 0
    }

    return $cubes
}

function Get-SolutionPart1 {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Path
    )
    
    begin {
        $InputData = Get-Content $Path

        $MaxCubes = @{
            Red = 12
            Green = 13
            Blue = 14
        }
    }
    
    process {
        $totalGameID = 0

        foreach ($line in $InputData) {
            $id = Get-GameID -Line $line
            $redCubes = Get-CubeCount -Line $line -Color Red
            $greenCubes = Get-CubeCount -Line $line -Color Green
            $blueCubes = Get-CubeCount -Line $line -Color Blue

            $possibleGame = $true

            foreach ($cube in $redCubes) {
                if ([int]$cube -gt $MaxCubes['Red']) {
                    $possibleGame = $false
                }
            }

            foreach ($cube in $greenCubes) {
                if ([int]$cube -gt $MaxCubes['Green']) {
                    $possibleGame = $false
                }
            }

            foreach ($cube in $blueCubes) {
                if ([int]$cube -gt $MaxCubes['Blue']) {
                    $possibleGame = $false
                }
            }

            if ($possibleGame) {
                $totalGameID += [int]$id
            }
        }

        return $totalGameID
    }
}

function Get-SolutionPart2 {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Path
    )
    
    begin {
        $InputData = Get-Content $Path
    }
    
    process {
        $gameTotal = 0

        foreach ($line in $InputData) {
            $redCubes = (Get-CubeCount -Line $line -Color Red).foreach({[int]$_})
            $greenCubes = (Get-CubeCount -Line $line -Color Green).foreach({[int]$_})
            $blueCubes = (Get-CubeCount -Line $line -Color Blue).foreach({[int]$_})

            $maxRed = $redCubes | Measure-Object -Maximum
            $maxGreen = $greenCubes | Measure-Object -Maximum
            $maxBlue = $blueCubes | Measure-Object -Maximum
            
            $cubePower = $maxRed.Maximum * $maxGreen.Maximum * $maxBlue.Maximum

            $gameTotal += $cubePower
        }

        return $gameTotal
    }
}