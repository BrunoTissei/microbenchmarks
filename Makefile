CC := gcc
LD := gcc

SRCDIR := bench
BUILDDIR := obj
BINDIR := bin

SOURCES := $(shell find $(SRCDIR) -type f -name *.c)
OBJECTS := $(patsubst $(SRCDIR)/%, $(BUILDDIR)/%, $(SOURCES:.c=.o))
TARGETS := $(patsubst $(SRCDIR)/%, $(BINDIR)/%, $(SOURCES:.c=))

FLAGS = -O1 -Wall -Wextra -Werror -static -march=cascadelake  # -ggdb
LDFLAGS = -static # -ggdb
CFLAGS = $(FLAGS)

all: $(TARGETS)

$(BINDIR)/%: $(BUILDDIR)/%.o
	@mkdir -p $(BINDIR)
	$(LD) $(LDFLAGS) $< -o $@

$(BUILDDIR)/%.o: $(SRCDIR)/%.c
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) -r $(BUILDDIR) $(BINDIR)
