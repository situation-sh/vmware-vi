# GuestProgramSpec

This describes the arguments to *GuestProcessManager.StartProgramInGuest*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_path** | **str** | The absolute path to the program to start.  For Linux guest operating systems, /bin/bash is used to start the program.  For Solaris guest operating systems, /bin/bash is used to start the program if it exists. Otherwise /bin/sh is used. If /bin/sh is used, then the process ID returned by *GuestProcessManager.StartProgramInGuest* will be that of the shell used to start the program, rather than the program itself, due to the differences in how /bin/sh and /bin/bash work. This PID will still be usable for watching the process with *GuestProcessManager.ListProcessesInGuest* to find its exit code and elapsed time.  ***Since:*** vSphere API 5.0  | 
**arguments** | **str** | The arguments to the program.  In Linux and Solaris guest operating systems, the program will be executed by a guest shell. This allows stdio redirection, but may also require that characters which must be escaped to the shell also be escaped on the command line provided.  For Windows guest operating systems, prefixing the command with \&quot;cmd /c\&quot; can provide stdio redirection.  ***Since:*** vSphere API 5.0  | 
**working_directory** | **str** | The absolute path of the working directory for the program to be run.  VMware recommends explicitly setting the working directory for the program to be run. If this value is unset or is an empty string, the behavior depends on the guest operating system. For Linux guest operating systems, if this value is unset or is an empty string, the working directory will be the home directory of the user associated with the guest authentication. For other guest operating systems, if this value is unset, the behavior is unspecified.  ***Since:*** vSphere API 5.0  | [optional] 
**env_variables** | **List[str]** | An array of environment variables, specified in the guest OS notation (eg PATH&#x3D;c:\\\\bin;c:\\\\windows\\\\system32 or LD\\_LIBRARY\\_PATH&#x3D;/usr/lib:/lib), to be set for the program being run.  Note that these are not additions to the default environment variables; they define the complete set available to the program. If none are specified the values are guest dependent.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_program_spec import GuestProgramSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestProgramSpec from a JSON string
guest_program_spec_instance = GuestProgramSpec.from_json(json)
# print the JSON string representation of the object
print GuestProgramSpec.to_json()

# convert the object into a dict
guest_program_spec_dict = guest_program_spec_instance.to_dict()
# create an instance of GuestProgramSpec from a dict
guest_program_spec_form_dict = guest_program_spec.from_dict(guest_program_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


