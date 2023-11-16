# GuestProcessNotFound

A GuestProcessNotFound exception is thrown when an operation fails because the guest process specified does not exist.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **int** | The process ID that was not found.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.guest_process_not_found import GuestProcessNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of GuestProcessNotFound from a JSON string
guest_process_not_found_instance = GuestProcessNotFound.from_json(json)
# print the JSON string representation of the object
print GuestProcessNotFound.to_json()

# convert the object into a dict
guest_process_not_found_dict = guest_process_not_found_instance.to_dict()
# create an instance of GuestProcessNotFound from a dict
guest_process_not_found_form_dict = guest_process_not_found.from_dict(guest_process_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


