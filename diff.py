import difflib

def compare_configs(config1_file:str, config2_file:str, report_file:str):
    """
    Compare two Cisco router running-configurations and write the differences to a report file.
    
    Params:
    -------
    config1_file : str
        Path to the first running-config file.
    config2_file : str
        Path to the second running-config file.
    report_file: str
        Path to the output report file.
    """
    # Open both configuration files
    with open(config1_file, 'r') as file1, open(config2_file, 'r') as file2:
        config1_lines = file1.readlines()
        config2_lines = file2.readlines()

    # Create a Differ object and compute the differences
    differ = difflib.Differ()
    diff = list(differ.compare(config1_lines, config2_lines))

    # Write the differences to the report file
    with open(report_file, 'w') as report:
        report.write("Differences between the configurations:\n\n")
        for line in diff:
            report.write(line)

    print(f"Report of differences saved to {report_file}")