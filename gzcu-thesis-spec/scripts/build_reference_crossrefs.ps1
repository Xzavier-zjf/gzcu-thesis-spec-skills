$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "build_reference_crossrefs.py"

if (-not (Test-Path $PythonScript)) {
    throw "Missing Python script: $PythonScript"
}

py $PythonScript @args
exit $LASTEXITCODE
