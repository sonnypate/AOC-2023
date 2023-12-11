Import-Module Pester

BeforeAll {
    . (Join-Path $PSScriptRoot "Day2.ps1")
    $example_line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    $example_input = Join-Path $PSScriptRoot "example1.txt"
}

Describe 'Get-GameID' {
    It 'Gets the game ID from the puzzle input.' {
        $id = Get-GameID -Line $example_line
        $id | Should -Be '3'
    }
}

Describe 'Get-CubeCount' {
    It 'Gets array of number of cubes in each round specified by color.' {
        $total = Get-CubeCount -Line $example_line -Color Blue
        $total | Should -Be @(6, 5)
    }
}

Describe 'Get-SolutionPart1' {
    It 'Gets the total number of possible games added together by game IDs.' {
        $total = Get-SolutionPart1 -Path $example_input
        $total | Should -Be 8
    }
}

Describe 'Get-SolutionPart2' {
    It 'Gets the total number of possible games added together by game IDs.' {
        $total = Get-SolutionPart2 -Path $example_input
        $total | Should -Be 2286
    }
}