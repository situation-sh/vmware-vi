# GuestWindowsProgramSpec

This describes the arguments to *GuestProcessManager.StartProgramInGuest* that apply only for Windows guests.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_minimized** | **bool** | Makes any program window start minimized.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.guest_windows_program_spec import GuestWindowsProgramSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GuestWindowsProgramSpec from a JSON string
guest_windows_program_spec_instance = GuestWindowsProgramSpec.from_json(json)
# print the JSON string representation of the object
print GuestWindowsProgramSpec.to_json()

# convert the object into a dict
guest_windows_program_spec_dict = guest_windows_program_spec_instance.to_dict()
# create an instance of GuestWindowsProgramSpec from a dict
guest_windows_program_spec_form_dict = guest_windows_program_spec.from_dict(guest_windows_program_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


