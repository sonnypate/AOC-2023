function Convert-FromSpelledDigit {
    [CmdletBinding()]
    [OutputType([string])]
    param (
        [Parameter(Mandatory)]
        [string]$Line
    )
    
    process {
        $spelledNumbers = @{
            one = "o1e"
            two = "t2o"
            three = "t3e"
            four = "f4r"
            five = "f5e"
            six = "s6x"
            seven = "s7n"
            eight = "e8t"
            nine = "n9e"
        }

        foreach ($number in $spelledNumbers.GetEnumerator()) {
            if ($Line -match $number.Key) {
                $Line = $Line.Replace($number.Key, $number.Value)
            }
        }
        return $Line
    }
}

function Get-FirstAndLastDigits {
    [CmdletBinding()]
    [OutputType([int])]
    param (
        # Line from puzzle input.
        [Parameter(Mandatory)]
        [string]$Line
    )

    # Convert to char array so that match
    # returns each digit in the string.
    $chars = $Line.ToCharArray()
    $re = $chars -match "\d+"
    
    # Combine the digits as a string
    $number = "$($re[0])$($re[-1])"

    # Return the number cast as int.
    return [int]$number
}

function Get-Solution {
    [CmdletBinding()]
    [OutputType([int])]
    param (
        # Path to the puzzle input.
        [Parameter(Mandatory)]
        [string]$Path
    )
    
    begin {
        $InputData = Get-Content $Path
    }

    process {
        $total = 0
        foreach ($line in $InputData) {
            # Convert spelled numbers to digits first if they're in the string.
            $convertedLine = Convert-FromSpelledDigit $line

            # Then get the calibration value based on first and last
            # number in the string.
            $number = Get-Part1CalibrationValue -Line $convertedLine

            # Add those numbers to the total
            $total += $number
        }

        return $total
    }
}