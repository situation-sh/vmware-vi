# ActiveDirectoryFault

Base fault for Active Directory related problems.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | The error code reported by the Active Directory API.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.active_directory_fault import ActiveDirectoryFault

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryFault from a JSON string
active_directory_fault_instance = ActiveDirectoryFault.from_json(json)
# print the JSON string representation of the object
print ActiveDirectoryFault.to_json()

# convert the object into a dict
active_directory_fault_dict = active_directory_fault_instance.to_dict()
# create an instance of ActiveDirectoryFault from a dict
active_directory_fault_form_dict = active_directory_fault.from_dict(active_directory_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


