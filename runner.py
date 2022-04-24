# Standard library import
import configparser
import report

# Third party imports

# Local imports
import source_data


def read_configuration():
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('config.ini')
    return config['paths']['source_files'], config['paths']['output_files'], config['prace_wewnetrzne'],\
           config['ogolne'], config['sprint']


if __name__ == "__main__":
    path_source_files, path_output_files, group_internal_work, group_general, group_sprint = read_configuration()

    #TODO: parametry group z pliku ini jakoś obsłużyć
    for aa in group_sprint.keys():
        print(aa)

    source_days_list = source_data.get_source_data(path_source_files)

    work_report = report.Report()
    work_report.create_report(source_days_list)
    work_report.save_report_to_file(path_output_files)

    # TODO: poniższe usunąć po zakończeniu programu
    for pos in source_days_list:
        print(pos)
