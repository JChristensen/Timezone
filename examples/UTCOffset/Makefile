# REMINDER: Squash this out.

# What board to build for and its core
CORE     ?= arduino:avr
FQBN     ?= arduino:avr:mega

# Arduino CLI
ARDUINO_CLI_URL := https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh

# Locations
ROOT := $(PWD)
BINDIR := $(ROOT)/_build/bin
BUILDDIR := $(ROOT)/_build

# What port to upload on
ifndef SERIAL_DEV
  ifneq (,$(wildcard /dev/ttyUSB0))
    SERIAL_DEV = /dev/ttyUSB0
  else ifneq (,$(wildcard /dev/ttyACM0))
    SERIAL_DEV = /dev/ttyACM0
  else
    SERIAL_DEV = unknown
  endif
endif


.PHONY: all tools build upload

# Do everything
all: tools build


# Only build the code
build: UTCOffset.ino
	$(BINDIR)/arduino-cli core install $(CORE)
	$(BINDIR)/arduino-cli compile -b $(FQBN) UTCOffset

# Only upload the software
upload: build UTCOffset.ino
	$(BINDIR)/arduino-cli upload -b $(FQBN) UTCOffset -p $(SERIAL_DEV)

# Fetches all the tools required
tools:
	mkdir -p $(BINDIR)
	curl -fsSL $(ARDUINO_CLI_URL) | BINDIR=$(BINDIR) sh -s $(ARDUINO_CLI_VERSION)
