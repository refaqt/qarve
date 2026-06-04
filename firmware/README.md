# Firmware

Software targets (motion controller, pendant, etc.) live in subfolders here. Each target is a normal software project (e.g. PlatformIO or CMake).

Firmware may later be extracted to its own repository and linked back as a submodule, same as hardware modules.

## Layout per target

```
firmware/<target>/
  README.md
  platformio.ini   # or CMakeLists.txt
  src/
  include/
  config/machine.json
  docs/dev-log/
  docs/decisions/
```

Runtime machine parameters belong in `config/machine.json` (validated against `doqs/schemas/firmware-machine-config.schema.json`).
