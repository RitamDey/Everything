import apt
import apt_pkg
import sys

# Handles dislaying of progress and asking questions
cdrom = apt.Cdrom(apt.progress.text.CdromProgress())


# Parse arguments
arguments = apt_pkg.parse_commandline(apt_pkg.config,
                            [('h', "help", "help"),
                             ('v', "version", "version"),
                             ('d', "cdrom", "Acquire::cdrom::mount", "HasArg"),
                             ('r', "rename", "APT::CDROM::Rename"),
                             ('m', "no-mount", "APT::CDROM::NoMount"),
                             ('f', "fast", "APT::CDROM::Fast"),
                             ('n', "just-print", "APT::CDROM::NoAct"),
                             ('n', "recon", "APT::CDROM::NoAct"),
                             ('n', "no-act", "APT::CDROM::NoAct"),
                             ('a', "thorough", "APT::CDROM::Thorough"),
                             ('c', "config-file", "", "ConfigFile"),
                             ('o', "option", "", "ArbItem")],
                                     args)


# Check if help or version was passed
if apt_pkg.config.find_b('help'):
    print('Help message')
    sys.exit(0)
elif apt_pkg.config.find_b('version'):
    print("Version: 0.0.0-0-pre-pre-pre-gamma")
    sys.exit(0)


# Progress notifier and main cdrom object
progress = apt.progress.text.CdromProgress()
cdrom = apt_pkg.Cdrom()


# Check arguments to get actions requested
if apt_pkg.config.find_b('help'):
    print('The HELP!!!')
    sys.exit(0)
elif apt_pkg.config.find_b('version'):
    print('Version: 0.0.0-0-pre-pre-pre-gamma')
    sys.exit(0)
if not arguments:
    sys.stderr.write('E: No operation specified')
    sys.exit(1)
elif arguments[0] == 'add':
    cdrom.add(progress)
elif arguments[0] == 'ident':
    cdrom.ident(progress)
else:
    print(f'E: Invalid operation {arguments[0]}', file=sys.stderr)
    sys.exit(1)

