import argparse
import logging
import os

logger = logging.getLogger(__name__)


def scan_and_fix_if_needed(module_path, dry_run=False):
    # first read in the file
    logger.info("scanning module {module_path}".format(**locals()))
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    with open(module_path) as f:
        lines_with_info = (fix_line_if_needed(line, module_name) for line in f)
        lines, was_corrected = tuple(zip(*lines_with_info))

    # if any corrections were made, overwrite the original
    number_corrected = sum(was_corrected)
    if not dry_run and number_corrected > 0:
        logger.info("scan corrected {number_corrected} lines in {module_path}; overwriting".format(**locals()))
        with open(module_path, 'w') as f:
            f.write(''.join(lines))


def fix_line_if_needed(line, module_name):
    if is_from_import(line):  # and is_circular_import(line, module_name):
        return '# {line}'.format(line=line), True
    else:
        return line, False


def is_from_import(line):
    """The only valid line that starts with `from` in Python is one of the form
    `from X import Y`. Is this one of those or not?
    """
    return line.startswith('from')


def is_circular_import(line, module_name):
    """Return True if import is circular, else False.
    
    Args:
        line (str): line to check; this function assumes this is a "from" import line.
            example:
            from client.models.business_dto import BusinessDTO  # noqa: F401,E501
        module_name (str): name of module the line is from.

    Returns:
        bool: True if import is circular, else False.
    """
    from_module_with_package = line.split()[1]
    from_module = from_module_with_package.split('.')[-1]
    return from_module == module_name


def make_parser():
    parser = argparse.ArgumentParser(
        description="swagger-codegen generates code with circular references due to some"
                    "modules importing their own members; this script removes the problem imports")
    parser.add_argument(
        'package_path',
        help='path to directory with modules to correct imports in')
    parser.add_argument(
        '--dry-run', action='store_true', default=False,
        help='log info about what would be done but take no action')
    parser.add_argument(
        '-v', '--verbosity',
        type=int, default=1,
        help='increase value to increase logging verbosity; 0 logs only errors')
    return parser


if __name__ == "__main__":
    # read in all the lines lazily
    # look for imports of the form
    #   "from <x.y.module_name> import <C>"
    #   where the module_name is the same as the current module being parsed
    # e.g. from client.models.business_dto import BusinessDTO  # noqa: F401,E501
    # comment out these lines and overwrite the file if any such lines are found

    args = make_parser().parse_args()
    logging.basicConfig(
        level=(logging.ERROR if args.verbosity < 1 else
               logging.INFO if args.verbosity == 1 else
               logging.DEBUG),
        format='[%(levelname)s][%(asctime)s]: %(message)s')

    if args.dry_run:
        logger.info("this is a dry run; actions will be logged but not taken")

    logger.info("scanning modules in {args.package_path}".format(**locals()))
    if os.path.isfile(args.package_path):
        module_paths = [args.package_path]
    else:
        module_paths = [os.path.join(args.package_path, path)
                        for path in os.listdir(args.package_path)
                        if path.endswith('.py')]
    logger.info("found {} packages to scan".format(len(module_paths)))

    for module_path in module_paths:
        scan_and_fix_if_needed(module_path, args.dry_run)
