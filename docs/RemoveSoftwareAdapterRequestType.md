# RemoveSoftwareAdapterRequestType

The parameters of *HostStorageSystem.RemoveSoftwareAdapter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hba_device_name** | **str** | The device name of the adapter to be removed.  | 

## Example

```python
from vmware_vi.models.remove_software_adapter_request_type import RemoveSoftwareAdapterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSoftwareAdapterRequestType from a JSON string
remove_software_adapter_request_type_instance = RemoveSoftwareAdapterRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveSoftwareAdapterRequestType.to_json()

# convert the object into a dict
remove_software_adapter_request_type_dict = remove_software_adapter_request_type_instance.to_dict()
# create an instance of RemoveSoftwareAdapterRequestType from a dict
remove_software_adapter_request_type_form_dict = remove_software_adapter_request_type.from_dict(remove_software_adapter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


