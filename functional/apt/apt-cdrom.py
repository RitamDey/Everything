import apt
import apt_pkg
import sys

INFO_MSG = 'apt {0} compiled on {1} {2}'.format(apt_pkg.VERSION, apt_pkg.DATE, apt_pkg.TIME)

def show_help():
        print(INFO_MSG)

        if apt_pkg.config.find_b('version'):
                return 0

        print(
                "Usage: apt-cdrom [options] command\n"
                "\n"
                "apt-cdrom is a tool to add CDROM's to APT's source list. The\n"
                "CDROM mount point and device information is taken from apt.conf\n"
                "and /etc/fstab.\n"
                "\n"
                "Commands:\n"
                "   add - Add a CDROM\n"
                "   ident - Report the identity of a CDROM\n"
                "\n"
                "Options:\n"
                "  -h   This help text\n"
                "  -d   CD-ROM mount point\n"
                "  -r   Rename a recognized CD-ROM\n"
                "  -m   No mounting\n"
                "  -f   Fast mode, don't check package files\n"
                "  -a   Thorough scan mode\n"
                "  -c=? Read this configuration file\n"
                "  -o=? Set an arbitrary configuration option, eg -o "
                "dir::cache=/tmp\n"
                "See fstab(5)"
        )


def main(args):
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
                show_help()
        elif apt_pkg.config.find_b('version'):
                print("Version: 0.0.0-0-pre-pre-pre-gamma")
                sys.exit(0)


        # Progress notifier and main cdrom object
        progress = apt.progress.text.CdromProgress()
        cdrom = apt_pkg.Cdrom()


        # Check arguments to get actions requested
        if apt_pkg.config.find_b('help'):
                show_help()

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
                print('E: Invalid operation {}'.format(arguments[0]), file=sys.stderr)
                sys.exit(1)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
