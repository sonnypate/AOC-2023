Import-Module Pester

BeforeAll {
    . (Join-Path $PSScriptRoot "Day1.ps1")
    $example_input = Join-Path $PSScriptRoot "example1.txt"
    $example2_input = Join-Path $PSScriptRoot "example2.txt"
}

Describe 'Get-FirstAndLastDigits' {
    It 'Will return the first and last number in a string as an integer.' {
        $inputString = "a1b2c3d4e5f"
        $number = Get-FirstAndLastDigits -Line $inputString
        $number | Should -Be 15
    }
}

Describe 'Get-Solution' {
    It 'Example1 input will return the sum of all numbers from the puzzle input.' {
        $solution = Get-Solution -Path $example_input
        $solution | Should -Be 142
    }
}

Describe 'Get-Solution' {
    It 'Example2 input will return the sum of all numbers from the puzzle input.' {
        $solution = Get-Solution -Path $example2_input
        $solution | Should -Be 281
    }
}

Describe 'Convert-FromSpelledDigit' {
    It 'Will return a modified string converting spelled digits to numeric digits.' {
        $solution = Convert-FromSpelledDigit "zoneight234"
        $solution | Should -Be "zo1e8t234"
    }
}