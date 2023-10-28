import psutil
import time
import xlsxwriter

def get_mem_usage():
	"""
    Get the current system's memory (RAM) usage as a percentage.

    This function uses the psutil library to retrieve information about the system's
    virtual memory (RAM). It returns the percentage of used memory.

    Returns:
        float: The percentage of used memory.
        int: If there is an error (FileNotFoundError), it returns 404 to indicate an error.

    Example:
    >>> memory_usage = get_mem_usage()
    >>> print(f"Memory usage: {memory_usage}%")
    Memory usage: 65.3%
    """
    try:
        ram_info = psutil.virtual_memory()
    except FileNotFoundError:
        ram_info = 404
        return ram_info
    return ram_info.percent

def get_cpu_usage():
	"""
    Get the current system's CPU usage as a percentage.

    This function uses the psutil library to retrieve information about the system's
    CPU usage. It returns the percentage of CPU usage.

    Returns:
        float or int: The percentage of CPU usage as a float, or 404 if there is an error.

    Raises:
        FileNotFoundError: If there is an error in accessing the CPU usage information.

    Example:
    >>> cpu_usage = get_cpu_usage()
    >>> if cpu_usage == 404:
    ...     print("Error: CPU information not available.")
    >>> else:
    ...     print(f"CPU usage: {cpu_usage}%")
    CPU usage: 25.7%
    """
    try:
            cpu_percent = psutil.cpu_percent()
    except FileNotFoundError:
            cpu_percent= 404
    return cpu_percent

def generate_excel_sheet(workbook_name: str,a: list, b: list):

	 """
    Generate an Excel workbook and populate it with CPU and memory usage data.

    This function creates an Excel workbook using the xlsxwriter library with the specified name.
    It populates a worksheet named "Sheet 1" with CPU usage and memory usage data from two lists, 'a' and 'b'.

    Args:
        workbook_name (str): The name of the Excel workbook to be created.
        a (list): A list containing CPU usage data.
        b (list): A list containing memory usage data.

    Returns:
        None

    Example:
    >>> cpu_data = [10, 20, 30]
    >>> mem_data = [50, 60, 70]
    >>> generate_excel_sheet("UsageData", cpu_data, mem_data)
    # Generates an Excel workbook named "UsageData.xlsx" with CPU and memory usage data.
    """
    
    workbook = xlsxwriter.Workbook(workbook_name+".xlsx")
    worksheet = workbook.add_worksheet("Sheet 1")
    
    worksheet.write(0,0,"Entry No")
    worksheet.write(0,1,"CPU Usage")
    worksheet.write(0,2,"Memmory Usage")
    
    for (c_index,cpu),(m_index,mem) in zip(enumerate(a),enumerate(b)):
        worksheet.write(c_index+1,0,str(c_index))
        worksheet.write(c_index+1,1,cpu)
        worksheet.write(m_index+1,2,mem)
    workbook.close()

w_name= input("Enter a name which doesn't already exist in your directory for your excel file:")
duration = "wrong"
while duration.isdigit()==False:
    duration = input("How long do you want to run your program in minutes?(Enter an integer):")
duration = int(duration)
cpu_usage=[]
mem_usage=[]
t_end= time.time()+60*duration
while t_end> time.time():
    cpu_usage.append(get_cpu_usage())
    mem_usage.append(get_mem_usage())
    time.sleep(10)
generate_excel_sheet(w_name,cpu_usage,mem_usage)
print(f"\nExcel File {w_name}.xlsx will be created in the same folder where the .py file is stored")
